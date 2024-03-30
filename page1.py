import streamlit as st
import pandas
import googleapiclient.discovery
import googleapiclient.errors
import mysql.connector
from sqlalchemy import create_engine
dataframes=None
button1_clicked=None
button2_clicked=None
def dfinfo():
    global dataframes,button1_clicked,input,ytchannel_detail_df,ytplaylist_details,ytvideoinfo_df,ytcommentinfo_df
    if button1_clicked:
        st.write("Extracting data...")
        # taken from channels api
        api_key="extracted api key"
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        channel_id=input       
        youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=api_key)

        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
             )
        response = request.execute()

        channel_name=response['items'][0]['snippet']['title']
        subscription_count=int(response['items'][0]['statistics']['subscriberCount'])
        view_count=int(response['items'][0]['statistics']['viewCount'])
        video_count=int(response['items'][0]['statistics']['videoCount'])
        upload_id=(response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])
        print(channel_name)
        print(channel_id)
        print(video_count)
        print(subscription_count)
        print(view_count)
        print(upload_id)
        ytchannel_detail_df=pandas.DataFrame({
            'ytchannel_name':[channel_name],
            'ytchannel_id':[channel_id],
            'ytvideo_count':[video_count],
            'ytsubscription_count':[subscription_count],
            'ytview_count':[view_count],
            'ytupload_id':[upload_id]
              })

               ## substituting "upload" in playlist item to get video details

        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=upload_id
             )
        response = request.execute()
        ytchannel_id=[]
        ytvideo_description=[]
        ytpublished_date=[]
        ytvideo_id=[]
        ytvideo_title=[]
        for video in response['items']:
            ytchannel_id.append(video['snippet']['channelId'])
            ytvideo_description.append(video['snippet']['description'])
            ytpublished_date.append(video['snippet']['publishedAt'])
            ytvideo_id.append(video['contentDetails']['videoId'])
            ytvideo_title.append(video['snippet']['title'])
 
        ytchannelvideo_df=pandas.DataFrame({
            "ytchannel_id":ytchannel_id,
            "ytvideo_description":ytvideo_description,
            "ytpublished_date":ytpublished_date,
            "ytvideo_id":ytvideo_id,
            "ytvideo_title":ytvideo_title
            })

####call playlist with channel id and get playlist id

        request = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId= channel_id,
            maxResults=25
             )
        response = request.execute()
        ytplaylist_id=[]
        ytchannel_id=[]
        ytplaylist_name=[]
        for video in response['items']:
            ytplaylist_id.append(video['id'])
            ytchannel_id.append(video['snippet']['channelId'])
            ytplaylist_name.append(video['snippet']['title'])

        ytplaylist_details=pandas.DataFrame({
            "ytplaylist_id":ytplaylist_id,
            "ytchannel_id":ytchannel_id,
            "ytplaylist_name":ytplaylist_name
            })

        #pprint.pprint(response)

        #likes views count from each video from video request
        #giving video id as input

        request1 = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            maxResults=25,
            id=",".join(ytchannelvideo_df['ytvideo_id'])
             )
        response1 = request1.execute()
        ytvideo_id=[]
        ytpublished_dates = []
        ytcomment_count=[]
        ytfavourite_count=[]
        ytlike_count=[]
        ytview_count=[]
        ytduration=[]
        for video in response1['items']:
            ytvideo_id.append(video['id'])
            ytpublished_dates.append(video['snippet']['publishedAt'])
            try:
                ytcomment_count.append(video['statistics']['commentCount'])
            except:
                 ytcomment_count.append(0)
            ytfavourite_count.append(video['statistics']['favoriteCount'])
            try:
                ytlike_count.append(video['statistics']['likeCount'])
            except:
                 ytlike_count.append(0)
            ytview_count.append(video['statistics']['viewCount'])
            ytduration.append(video['contentDetails']['duration'])
        ytvideodetails_df = pandas.DataFrame({
            "ytvideo_id": ytvideo_id,
            "ytpublished_dates": ytpublished_dates,
            "ytcomment_count": ytcomment_count,
            "ytfavourite_count": ytfavourite_count,
            "ytlike_count": ytlike_count,
            "ytview_count": ytview_count,
            "ytduration":ytduration
              })
#merging two dataframes using "inner" join 
        ytvideoinfo_df=pandas.merge(ytchannelvideo_df,ytvideodetails_df,on="ytvideo_id",how="inner")


#taken from commentthreads for comment details
#channel id is given as input

        requestc = youtube.commentThreads().list(
            part='snippet',
            allThreadsRelatedToChannelId=channel_id,
            maxResults=20
             )
        responsec = requestc.execute()
        
        ytcomment_Id=[]
        ytauthor_Name=[]
        ytcommentpublished_date=[]
        ytcomment_text=[]
        ytvideo_id=[]
        ytchannel_id=[]
        for video in responsec['items']:
            ytchannel_id.append(video['snippet']['topLevelComment']['snippet']['channelId'])
            ytcomment_Id.append(video['snippet']['topLevelComment']['snippet']['authorChannelId']['value'])
            ytauthor_Name.append(video['snippet']['topLevelComment']['snippet']['authorDisplayName'])
            ytcommentpublished_date.append(video['snippet']['topLevelComment']['snippet']['publishedAt'])
            ytcomment_text.append(video['snippet']['topLevelComment']['snippet']['textDisplay'])
            ytvideo_id.append(video['snippet']['topLevelComment']['snippet']['videoId'])
        print(ytcomment_Id)
#print(ytauthor_Name)
#print(ytcommentpublished_date)
#print(ytcomment_text)
#print(ytvideo_id)
#print(ytchannel_id)
#pprint.pprint(responsec)
        ytcommentinfo_df=pandas.DataFrame({
            "ytchannel_id":ytchannel_id,
            "ytvideo_id":ytvideo_id,
            "ytcomment_Id":ytcomment_Id,
            "ytauthor_Name":ytauthor_Name,
            "ytcommentpublished_date":ytcommentpublished_date,
            "ytcomment_text":ytcomment_text})
        dataframes=(ytchannel_detail_df,ytplaylist_details,ytvideoinfo_df,ytcommentinfo_df) #tuples
    #else:
        #st.error("please enter channel ID")
    return dataframes

    
def sqlupload():
        global dataframes,button2_clicked,ytchannel_detail_df,ytplaylist_details,ytvideoinfo_df,ytcommentinfo_df
        if button2_clicked:
             dataframes=dfinfo()
             if dataframes:
                    st.write("uploading into Mysql")
        
        
                    # Define MySQL connection parameters
                    mysql_username = 'user'
                    mysql_password = 'yourpwd'
                    mysql_host = 'localhost'
                    mysql_port = '3306'
                    mysql_database = 'databasename'

        ############### inserting channel info with channel id as a primary key
                    connection_str = f"mysql+mysqlconnector://{'user'}:{'yourpwd'}@{'localhost'}:{'3306'}/{'databasename'}"

        #creating sqlalchemy engine
                    engine = create_engine(connection_str)

        # Define the table name in MySQL
                    table_name = 'ytchannel_detail'

        # Inserting DataFrame into MySQL
                    ytchannel_detail_df.to_sql(name='ytchannel_detail', con=engine, if_exists='append', index=False)

           


        ########insering playlist id in which playlist id as primary key and channelid as foreign key
                    table_name = 'ytplaylist'
                    ytplaylist_details.to_sql(name='ytplaylist', con=engine, if_exists='append', index=False)


        ###############inserting video info with video id as primary key 

                    table_name = 'ytvideoinfo'
                    ytvideoinfo_df.to_sql(name='ytvideoinfo', con=engine, if_exists='append', index=False)


        ##########inserting comments with comment id video id
                    table_name = 'ytcommentinfo'
                    ytcommentinfo_df.to_sql(name='ytcommentinfo', con=engine, if_exists='append', index=False)

        # Dispose the engine
                    engine.dispose() 
                    ytchannel_detail_df,ytplaylist_details,ytvideoinfo_df,ytcommentinfo_df=dataframes
                    pass
             else:
                    st.error("please upload properly")
    
        
def page():
    global button1_clicked,button2_clicked,input,ytchannel_detail_df,ytplaylist_details,ytvideoinfo_df,ytcommentinfo_df
    st.title("Page 1")
    st.write("Welcome to Youtube Data Harvesting and Warehousing")
    input=st.text_input("Enter the Youtube Channel ID")
    button1_clicked=st.button("Submit")
    if button1_clicked:
         dfinfo()
    button2_clicked=st.button("Upload to MySql")
    sqlupload()
     
if __name__ == '__main__':
    page()

