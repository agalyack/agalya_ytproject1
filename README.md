# agalya_ytproject1
###YouTube-Data-Harvesting-and-Warehousing-using-Python-MySQL-and-Streamlit.
Problem Statement:
The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. The application should have the following features:
1.	Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, total view count, playlist ID, video ID, likes, comments, comment count of each video) using Google API.
2.	Storing the retrieved data in the form of python DataFrame.
3.	Ability to migrate data for up to 10 different YouTube channels and store them in the data lake Sql database by clicking a button.
4.	Using SQl queries to join the tables in SQL data warehouse  and retrieve data for specific channels based on user input and use  Python SQL Library such as SQLAlchemy to interact with databases.
5.	Display the retrieved data in the streamlit app.

Approach: 
1.	Setup a Streamlit App:
Streamlit is a great choice for building data visualization and analyse tools easily and quickly. Create a simple streamlit app by which the user enter the you tube Channel ID  and migrate to data warehouse.
2.	Connect to Youtube API:
Use the Google API client library for python to make the requests to the API.
3.	Store and Clean data:
Pandas DataFrames is used to store the retrieved data temporarily before migrating to the data warehouse.
4.	Migrate data to SQL data warehouse:
After collecting data from multiple channels, data are migrated to MYSQL data warehouse.
5.	Query the SQL data warehouse:
SQL Alchemy is used to interact with SQL data base and retrieving data using queries with joins
6.	Display data in Streamlit App:
Finally, data are displayed in streamlit app.

 Code Breakdown:
1.	Import necessary libraries such as googleapiclient.discovery and googleapiclient.errors for intercting with youtube api, streamlit for use interface, pandas for dataframes,mysql.connector for establishing sql connection and sqlalchemy to interact with databases.
2.	Set the YouTube API key for making requests to the YouTube API.

3.	The function dfinfo() converts the data from youtube into dataframes for temporary storage.
4.	The function sqlupload() uploads the dataframes into MySql as tables  into the database.
5.	The function exe_query() executes the queries and interact with Sql database for retrieving the data
6.	Also it displays the data in the streamlit app.

