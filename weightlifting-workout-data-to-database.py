#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This file was used to insert automate a .csv file data into a MySQL .db file format."""


# In[1]:


import mysql.connector
import csv
import pandas as pd


# In[2]:


# Use the comments below to set up the username and password strings for connection.
# username = "Enter your username here in this string."
# password = "Enter your password here in this string."

username = ""
password = ""


# In[4]:


mydb = mysql.connector.connect(
    host = "localhost", 
    user = username, 
    passwd = password
)

print(mydb)


# In[5]:


mycursor = mydb.cursor()


# In[6]:


mycursor.execute("CREATE DATABASE IF NOT EXISTS myworkouts")


# In[7]:


mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


# In[ ]:


# mydb = mysql.connector.connect(
#     host = "localhost", 
#     user = username, 
#     passwd = password, 
#     db = "myworkouts"
# )


# In[8]:


query = ("USE myworkouts")
mycursor.execute(query)


# In[9]:


query = ("CREATE TABLE IF NOT EXISTS workouts "
"(workout_no INT PRIMARY KEY AUTO_INCREMENT, "
"exercise VARCHAR(255), "
"sets TINYINT UNSIGNED, "
"reps TINYINT UNSIGNED, "
"weight_lbs SMALLINT UNSIGNED, "
"date_time DATETIME, "
"duration_minutes SMALLINT)")

mycursor.execute(query)


# In[10]:


query = 'DESCRIBE workouts'
mycursor.execute(query)

for x in mycursor:
    print(x)


# In[11]:


query = ("Select * FROM workouts")
mycursor.execute(query)
for x in mycursor:
    print(x)


# In[12]:


workout_data = pd.read_csv("workout_data_database.csv")
workout_data.head()


# In[13]:


workout_data.drop(columns = ["Unnamed: 0"], inplace = True)
workout_data.head()


# In[14]:


workout_data_tuple = [tuple(i) for i in workout_data.values.tolist()]
workout_data_tuple[0:5]


# In[15]:


query = """INSERT INTO workouts
(exercise, sets, reps, weight_lbs, date_time, duration_minutes)
VALUES (%s, %s, %s, %s, %s, %s)"""

for i in range(len(workout_data_tuple)):
    mycursor.execute(query, workout_data_tuple[i])


# In[16]:


query = ("Select * FROM workouts")
mycursor.execute(query)
for x in mycursor:
    print(x)


# In[17]:


mydb.commit()

