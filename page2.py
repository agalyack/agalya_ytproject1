import streamlit as st
import pandas
import mysql.connector
from sqlalchemy import create_engine
import page1

def page():
    st.title("Page 2")
    st.write("Welcome to Page")
    option = st.selectbox(
    'Shall we go for few Questions?',
    ('What are the names for all the videos and their corressponding channel?',
     'Which channels have the most number of videos,how many videos do they have?',
     'What are the top 10 most viewed videos and their respective channels?',
     'How many comments were made on each video,and what are their corresponding video names?',
     'Which videos have the highest number of likes and what are their corresponding channel names?',
     'What is the total number of likes for each video and what are their corresponding video names?',
     'What is the total total number of views for each channel and what are their corresponding channel names?',
     'What are the names of all the channels that have published videos in 2022?',
     'What is the average duration of all videos in each channel and what are their corresponding channel names?',
     'Which videos have the highest number of comments and what are their corresponding channel names?'))
    st.write('You selected:', option)
    if option=='What are the names for all the videos and their corressponding channel?':
        exe_query1()
    elif option=='Which channels have the most number of videos,how many videos do they have?':
        exe_query2()
    elif option=='What are the top 10 most viewed videos and their respective channels?':
        exe_query3()
    elif option=='How many comments were made on each video,and what are their corresponding video names?':
        exe_query4()
    elif option=='Which videos have the highest number of likes and what are their corresponding channel names?':
        exe_query5()
    elif option=='What is the total number of likes for each video and what are their corresponding video names?':
        exe_query6()
    elif option=='What is the total total number of views for each channel and what are their corresponding channel names?':
        exe_query7()
    elif option=='What are the names of all the channels that have published videos in 2022?':
        exe_query8()
    elif option=='What is the average duration of all videos in each channel and what are their corresponding channel names?':
        exe_query9()
    elif option=='Which videos have the highest number of comments and what are their corresponding channel names?':
        exe_query10()
def exe_query1():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select a.ytchannel_name,b.ytvideo_title from ytproject.ytchannel_detail a inner join ytproject.ytvideoinfo b on a.ytchannel_id=b.ytchannel_id;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head(10))
def exe_query2():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select row_number() over (order by ytvideo_count desc)'row number',ytchannel_name,ytvideo_count from ytproject.ytchannel_detail;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query3():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select row_number() over (order by a.ytview_count desc) 'Most viewed video',a.ytvideo_title,a.ytview_count,b.ytchannel_name from ytproject.ytvideoinfo a inner join ytproject.ytchannel_detail b on a.ytchannel_id=b.ytchannel_id limit 10;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query4():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select ytvideo_title,ytcomment_count from ytproject.ytvideoinfo limit 25;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query5():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select row_number() over (order by a.ytlike_count desc) 'Highly Liked Video',b.ytchannel_name,a.ytlike_count from ytproject.ytvideoinfo a inner join ytproject.ytchannel_detail b on a.ytchannel_id=b.ytchannel_id limit 25;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query6():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select ytvideo_title,ytlike_count from ytproject.ytvideoinfo limit 25;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query7():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select ytchannel_name,ytview_count from ytproject.ytchannel_detail;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head(15))
def exe_query8():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="SELECT distinct a.ytchannel_name from ytproject.ytchannel_detail a JOIN ytproject.ytvideoinfo b ON a.ytchannel_id = b.ytchannel_id WHERE YEAR(b.ytpublished_dates) = 2022;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query9():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="SELECT b.ytchannel_name, AVG(SUBSTRING_INDEX(SUBSTRING_INDEX(a.ytduration, 'T', -1), 'M', 1) * 60 + SUBSTRING_INDEX(SUBSTRING_INDEX(a.ytduration, 'T', -1), 'M', -1))/60 AS average_duration_minutes FROM ytproject.ytvideoinfo a JOIN ytproject.ytchannel_detail b ON a.ytchannel_id = b.ytchannel_id GROUP BY a.ytchannel_id, b.ytchannel_name;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
def exe_query10():
    connection_str = f"mysql+mysqlconnector://{'root'}:{'roots'}@{'localhost'}:{'3306'}/{'ytproject'}"
    engine = create_engine(connection_str)
    sql_query="select row_number() over (order by a.ytcomment_count desc) 'Highly Commented Video',b.ytchannel_name,a.ytvideo_title,a.ytcomment_count from ytproject.ytvideoinfo a inner join ytproject.ytchannel_detail b on a.ytchannel_id=b.ytchannel_id limit 25;"
    df = pandas.read_sql_query(sql_query, engine)
    engine.dispose()
    st.write(df.head())
if __name__ == '__main__':
    page()
