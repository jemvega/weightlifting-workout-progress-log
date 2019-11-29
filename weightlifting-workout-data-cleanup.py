#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This file was used to input data into a .csv file, clean the data using pandas,
and organize the data to be written into a MySQL .db file format.
"""


# In[1]:


import pandas as pd 
from datetime import datetime


# In[ ]:


def batch_input(file_name):
    if not ".csv" in file_name: 
        file_rename = file_name + ".csv" 
    output_file = open(file_rename, "a", newline = "")
    output_writer = csv.writer(output_file, lineterminator = "\n")
    user_input = ""

    while user_input != "q".lower(): 
        user_input = input("Please input your data. \n")
        if user_input == "q".lower():
            print("Goodbye!\n")
            output_file.close()
            break
        else:
            output_writer.writerow(user_input.split())
            continue


# In[ ]:


def string_to_integer(list_string):
    try:
        converted_list = list_string.copy()
        for i in converted_list:
            if i.isdigit() == True:
                integer = int(i)
                index = converted_list.index(i)
                converted_list.pop(index)
                converted_list.insert(index, integer)
        return converted_list
    except:
        print("Error!")


# In[ ]:


# This is a function for writing workout data into csv from user input. 
batch_input("workout_data_raw")


# In[2]:


column_names = "exercise, sets, reps, weight_lbs, datetime, duration_minutes".split(", ")
column_names


# In[3]:


exercise_names = "BackSquat OverheadSquat FrontSquat BenchPress Deadlift Snatch Clean&Jerk ShoulderPress SnatchPress".split()
exercise_names


# In[4]:


workout_data_raw = pd.read_csv("workout_data_raw.csv")


# In[5]:


workout_data_raw.head()


# In[6]:


workout_data_raw.fillna("", inplace = True)
workout_data_raw.head()


# In[7]:


# Note: the exercise names do not match the exercise names from above. 
workout_data_raw["exercise"].unique()


# In[8]:


# Need to change "BackSquats" to "BackSquat" for consistency.
rename_exercise = workout_data_raw.index[workout_data_raw["exercise"] == "BackSquats"].tolist()
for i in rename_exercise:
    workout_data_raw["exercise"][i] = "BackSquat"
workout_data_raw["exercise"].unique()


# In[9]:


# Need to change "FrontSquats" to "FrontSquat" for consistency. 
rename_exercise = workout_data_raw.index[workout_data_raw["exercise"] == "FrontSquats"].tolist()
for i in rename_exercise:
    workout_data_raw["exercise"][i] = "FrontSquat"
workout_data_raw["exercise"].unique()


# In[10]:


# Need to change "Deadlifts" to "Deadlift" for consistency. 
rename_exercise = workout_data_raw.index[workout_data_raw["exercise"] == "Deadlifts"].tolist()
for i in rename_exercise:
    workout_data_raw["exercise"][i] = "Deadlift"
workout_data_raw["exercise"].unique()


# In[11]:


# Need to change "ShouldPress" to "ShoulderPress" for consitency. 
rename_exercise = workout_data_raw.index[workout_data_raw["exercise"] == "ShouldPress"].tolist()
for i in rename_exercise:
    workout_data_raw["exercise"][i] = "Deadlift"
workout_data_raw["exercise"].unique()


# In[12]:


workout_data_raw.to_csv(r'C:\Users\jacqu\Desktop\Github Portfolio\weightlifting-workout-tracker\workout_data_clean.csv')


# In[13]:


workout_data_clean = pd.read_csv("workout_data_clean.csv")
workout_data_clean.head()


# In[14]:


workout_data_clean.fillna("", inplace=True)
workout_data_clean.head()


# In[15]:


workout_data_clean.drop(columns = ["Unnamed: 0"], inplace = True)
workout_data_clean.head()


# In[16]:


workout_data_clean.head()


# In[17]:


# Check to see if .csv headers match .db headers
col_headers = set(list(workout_data_clean))
col_headers == set(column_names)


# In[18]:


# Check to see if exercise_names have duplicates or errors
set(exercise_names) == set(workout_data_clean["exercise"].unique())


# In[19]:


workout_data_list = workout_data_clean.values.tolist()
workout_data_list[0:5]


# In[20]:


len(workout_data_list)


# In[21]:


# This changes the "%m/%d/%Y" string format in the list to datetime format "%Y-%m-%d %H:%M:%S"
for i in range(len(workout_data_list)):
    try:
        temp = datetime.strptime(workout_data_list[i][4], "%m/%d/%Y")
        temp.strftime("%Y-%m-%d %H:%M:%S")
        workout_data_list[i][4] = temp
    except:
        pass


# In[22]:


# This changes the "%Y-%m-%dT%H-%M-%S" string format in the list to datetime format "%Y-%m-%d %H:%M:%S"
for i in range(len(workout_data_list)):
    try:
        temp = datetime.strptime(workout_data_list[i][4], "%Y-%m-%dT%H:%M:%S")
        temp.strftime("%Y-%m-%d %H:%M:%S")
        workout_data_list[i][4] = temp
    except:
        pass


# In[23]:


# This changes the "%Y-%m-%dT%H-%M-%S" string format in the list to datetime format "%Y-%m-%d %H:%M:%S"
for i in range(len(workout_data_list)):
    try:
        temp = datetime.strptime(workout_data_list[i][4], "%Y-%m-%dT%H-%M-%S")
        temp.strftime("%Y-%m-%d %H:%M:%S")
        workout_data_list[i][4] = temp
    except:
        pass


# In[24]:


workout_data_list[0:5]


# In[25]:


workout_data_list.insert(0, column_names)


# In[26]:


workout_data_list[0:5]


# In[27]:


workout_data_tuple = [tuple(i) for i in workout_data_list]
workout_data_tuple[0:5]


# In[28]:


workout_data_database = pd.DataFrame(workout_data_tuple)
workout_data_database.head()


# In[29]:


workout_data_database.columns = column_names
workout_data_database.head()


# In[30]:


workout_data_database.to_csv(r'C:\Users\jacqu\Desktop\Github Portfolio\weightlifting-workout-tracker\workout_data_database.csv')

