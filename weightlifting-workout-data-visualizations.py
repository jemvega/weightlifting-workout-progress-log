#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
get_ipython().run_line_magic('matplotlib', 'inline')

# #plt.show()


# In[2]:


# Setting custom color palette from hex color codes 
"""
Hexcodes and Color Names
"#B38867", # Coffee
"#283655", # Blueberry
"#69983D", # Green Apple
"#D50000", # Guardsman Red
"#A57298", # Boquet
"#FFAA00", # Web Orange/Goldenrod
"#F18D93", # Pink Tulip
"#F0810F", # Tangerine
"#66A5AD", # Ocean
"""

color_names = "coffee, blueberry, green, red, boquet, goldenrod, pink tulip, tangerine, ocean".split(", ")
hexcodes = "#B38867 #283655 #69983D #D50000 #A57298 #FFAA00 #F18D93 #F0810F #66A5AD".split()
colors_codes = list(zip(color_names, hexcodes))
exercise_names = "Deadlift BackSquat OverheadSquat FrontSquat BenchPress ShoulderPress SnatchPress Snatch Clean&Jerk".split()
color_map= dict(zip(exercise_names, colors_codes))


# In[3]:


color_df = pd.DataFrame.from_dict(color_map, orient="index", columns=["Color Name", "Hexcode"])
color_df


# In[4]:


colors = color_df["Hexcode"].tolist()


# In[5]:


palette = sns.set_palette(sns.color_palette(colors))
sns.set_context("paper")


# In[6]:


df = pd.read_csv("workout_data_database.csv")
df.head()


# In[7]:


df.drop(columns =["Unnamed: 0"], inplace = True)
df.head()


# In[8]:


workout_data_list = df.values.tolist()
workout_data_list[0:5]


# In[9]:


# This changes the "%Y-%m-%d %H:%M:%S" string format in the list to datetime format "%Y-%m-%d %H:%M:%S" 
# to be able to use seaborn graphs below.
for i in range(len(workout_data_list)):
    try:
        temp = datetime.strptime(workout_data_list[i][4], "%Y-%m-%d %H:%M:%S")
        temp.strftime("%Y-%m-%d %H:%M:%S")
        workout_data_list[i][4] = temp
    except:
        pass


# In[10]:


workout_data = pd.DataFrame(workout_data_list)
workout_data.head()


# In[11]:


workout_data.columns = "exercise, sets, reps, weight_lbs, datetime, duration_minutes".split(", ")
workout_data.head()


# In[12]:


# A dataframe for total count of workouts for each exercise
workout_count = workout_data[["exercise", "datetime"]]
workout_count.head()


# In[13]:


# Plot for total count of workouts for each exercise
plt.figure(figsize = (12,9))
sns.set_context("paper", font_scale = 2)
graph = sns.swarmplot(
    x="exercise", 
    y="datetime", 
    data=workout_count, 
    palette=colors, 
    order=exercise_names
    )
graph.set_xticklabels(graph.get_xticklabels(), rotation = 30)
graph.yaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.yaxis.set_major_formatter(mdates.DateFormatter("%b %d, %y"))
graph.set(
    title="Workout Count per Exercise", 
    xlabel="Exercise", 
    ylabel="Date"
    )
plt.savefig("Workout Count per Exercise.png")


# In[14]:


# A dataframe for max weight by each exercise. 
exercise_max = workout_data[["exercise", "weight_lbs"]].groupby("exercise").max()
exercise_max["exercise"] = exercise_max.index
exercise_max


# In[15]:


# Plot of max weight for each exercise
plt.figure(figsize = (12,9))
sns.set_context("paper", font_scale = 2)
graph = sns.barplot(
    x="exercise", 
    y="weight_lbs", 
    data=exercise_max, 
    order=exercise_names
    )
graph.set_xticklabels(graph.get_xticklabels(), rotation = 30)
graph.set(
    title="Max Lifts per Exercise", 
    xlabel="Exercise", 
    ylabel="Weight (lbs)", 
    yticks=np.arange(0, 300, 25)
    )
plt.savefig("Max Lifts per Exercise.png")


# In[16]:


# A dataframe for total intensity(total weight lifted) for each exercise
total_intensity = workout_data[["exercise", "weight_lbs"]].groupby("exercise").sum()
total_intensity["exercise"] = total_intensity.index
total_intensity


# In[17]:


# Plot of total intensity for each exercise
plt.figure(figsize = (12,9))
sns.set_context("paper", font_scale = 2)
graph = sns.barplot(
    x="exercise", 
    y="weight_lbs", 
    data=total_intensity, 
    order=exercise_names
    )
graph.set_xticklabels(graph.get_xticklabels(), rotation=30)
graph.set(
    title="Total Intensity", 
    xlabel="Exercise", 
    ylabel="Total Weight Lifted (lbs)", 
    yticks=np.arange(0, 8000, 500)
    )
plt.savefig("Total Intensity.png")


# In[18]:


# A dataframe for total volume for each exercise
total_reps = workout_data["sets"]*workout_data["reps"]
workout_data["total volume"] = total_reps
total_volume = workout_data[["exercise", "total volume"]].groupby("exercise").sum()
total_volume["exercise"] = total_volume.index
total_volume


# In[19]:


# Plot for total volume for each exercise
plt.figure(figsize = (12,9))
sns.set_context("paper", font_scale = 2)
graph = sns.barplot(
    x="exercise", 
    y="total volume", 
    data=total_volume, 
    order=exercise_names
    )
graph.set_xticklabels(graph.get_xticklabels(), rotation = 30)
graph.set(
    title="Total Volume per Exercise", 
    xlabel="Exercise", 
    ylabel="Total Reps", 
    yticks=np.arange(0, 1200, 100)
    )
plt.savefig("Total Volume.png")


# In[20]:


squats_intensity = workout_data[
    ["exercise", "datetime", "weight_lbs"]
    ].loc[
    (workout_data["exercise"] == "BackSquat") | 
    (workout_data["exercise"] == "OverheadSquat") | 
    (workout_data["exercise"] == "FrontSquat")
    ]
squats_intensity.head()


# In[21]:


squats_volume = workout_data[
    ["exercise", "datetime", "total volume"]
    ].loc[
    (workout_data["exercise"] == "BackSquat") | 
    (workout_data["exercise"] == "OverheadSquat") | 
    (workout_data["exercise"] == "FrontSquat")
    ]
squats_volume.head()


# In[22]:


presses_intensity = workout_data[
    ["exercise", "datetime", "weight_lbs"]
    ].loc[(workout_data["exercise"] == "BenchPress") | 
    (workout_data["exercise"] == "ShoulderPress")]
presses_intensity.head()


# In[23]:


presses_volume = workout_data[
    ["exercise", "datetime", "total volume"]
    ].loc[(workout_data["exercise"] == "BenchPress") | 
    (workout_data["exercise"] == "ShoulderPress")
    ]
presses_volume.head()


# In[24]:


oly_lifts_intensity = workout_data[
    ["exercise", "datetime", "weight_lbs"]
    ].loc[
    (workout_data["exercise"] == "Clean&Jerk") | 
    (workout_data["exercise"] == "Snatch")
    ]
oly_lifts_intensity.head()


# In[25]:


oly_lifts_volume = workout_data[
    ["exercise", "datetime", "total volume"]
    ].loc[(workout_data["exercise"] == "Clean&Jerk") | 
    (workout_data["exercise"] == "Snatch")
    ]
oly_lifts_volume.head()


# In[26]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="weight_lbs", 
    data=squats_intensity, 
    palette=colors[1:4], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(squats_intensity["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Squats Intensity vs. Time", 
    xlabel="Time", 
    ylabel="Weight (lbs)", 
    yticks=np.arange(0, 250, 25)
    )
plt.legend(
    title="Exercise", 
    loc="upper right", 
    labels=squats_intensity["exercise"].unique()
    )
plt.savefig("Squats Intensity.png")


# In[27]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="total volume", 
    data=squats_volume, 
    palette=colors[1:4], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(squats_volume["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Squats Volume vs. Time", 
    xlabel="Time", 
    ylabel="Total Reps per Session", 
    yticks=np.arange(0, 55, 5)
    )
plt.legend(
    title="Exercise", 
    loc="upper left", 
    labels=squats_volume["exercise"].unique()
    )
plt.savefig("Squats Volume.png")


# In[28]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="weight_lbs", 
    data=presses_intensity, 
    palette=colors[4:6], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(presses_intensity["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Presses Intensity vs. Time", 
    xlabel="Time", 
    ylabel="Weight (lbs)", 
    yticks=np.arange(0, 200, 25)
    )
plt.legend(
    title="Exercise", 
    loc="upper right", 
    labels=presses_intensity["exercise"].unique()
    )
plt.savefig("Presses Intensity.png")


# In[29]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="total volume", 
    data=presses_volume, 
    palette=colors[4:6], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(presses_volume["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Presses Volume vs. Time", 
    xlabel="Time", 
    ylabel="Total Reps per Session", 
    yticks=np.arange(0, 55, 5)
    )
plt.legend(
    title="Exercise", 
    loc="upper left", 
    labels=presses_volume["exercise"].unique()
    )
plt.savefig("Presses Volume.png")


# In[30]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="weight_lbs", 
    data=oly_lifts_intensity, 
    palette=colors[7:9], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(oly_lifts_intensity["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Olympic Lifts Intensity vs. Time", 
    xlabel="Time", 
    ylabel="Weight (lbs)",
    yticks=np.arange(0, 150, 25)
    )
plt.legend(
    title="Exercise", 
    loc="upper right", 
    labels=oly_lifts_intensity["exercise"].unique()
    )
plt.savefig("Olympic Lifts Intensity.png")


# In[31]:


# Plot comparison for intensity for squats.
plt.figure(figsize = (16,9))

sns.set_context("paper", font_scale = 2)
graph = sns.lineplot(
    x="datetime", 
    y="total volume", 
    data=oly_lifts_volume, 
    palette=colors[7:9], 
    hue="exercise", 
    linewidth=3
    )
graph.set_xticklabels(oly_lifts_volume["datetime"].values, rotation = 30)
graph.xaxis.set_major_locator(mdates.WeekdayLocator(interval=5))
graph.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
graph.set(
    title="Olympic Lifts Volume vs. Time", 
    xlabel="Time", 
    ylabel="Total Reps per Session",
    yticks=np.arange(0, 30, 3)
    )
plt.legend(
    title="Exercise", 
    loc="upper right", 
    labels=oly_lifts_volume["exercise"].unique()
    )
plt.savefig("Olympic Lifts Volume.png")


# In[32]:


""" Analytics Below """


# In[33]:


# Shoulder Press Volume to Deadlift Volme Percent Ratio
dl = total_volume.loc["Deadlift"][0]
sp = total_volume.loc["ShoulderPress"][0]

round(sp/dl*100, 2)


# In[34]:


# Deadlift Max to Shoulder Press Max Percent Ratio
dl = exercise_max.loc["Deadlift"][0]
sp = exercise_max.loc["ShoulderPress"][0]

round(dl/sp*100, 2)


# In[35]:


# Squats Total Volume to Presses Total Volume Percent Ratio
sq = squats_volume["total volume"].sum()
pr = presses_volume["total volume"].sum()

round(sq/pr*100, 2)


# In[36]:


# Squts Total Intensity to Presses Total Intensity Percent Ratio
sq = squats_intensity["weight_lbs"].sum()
pr = presses_intensity["weight_lbs"].sum()

round(sq/pr*100, 2)


# In[37]:


# Snatch Total Volume to Clean&Jerk Total Volume Percent Ratio
cj = total_volume.loc["Clean&Jerk"][0]
sn = total_volume.loc["Snatch"][0]

round(sn/cj*100, 2)


# In[38]:


# Snatch Total Intensity to Clean&Jerk Total Intensity Percent Ratio
cj = total_intensity.loc["Clean&Jerk"][0]
sn = total_intensity.loc["Snatch"][0]

round(sn/cj*100, 2)


# In[39]:


# Front Squat Max to Back Squat Max Percent Ratio
fs = exercise_max.loc["FrontSquat"][0]
bs = exercise_max.loc["BackSquat"][0]

round(fs/bs*100, 2)


# In[40]:


# Average duration of workouts out of 111 workouts with non-null data in duration_minutes
len(workout_data["duration_minutes"].loc[workout_data["duration_minutes"] != -1]) # No. workouts with non-null duration

avg_duration = workout_data["duration_minutes"].loc[workout_data["duration_minutes"] != -1].mean()
round(avg_duration, 2)


# In[41]:


# Average number of sets in workouts
avg_sets = workout_data["sets"].mean()
round(avg_sets, 2)


# In[42]:


# Average number of reps in workouts
avg_reps = workout_data["reps"].mean()
round(avg_reps, 2)


# In[43]:


# Average weight lifted in workouts
avg_weight = workout_data["weight_lbs"].mean()
round(avg_weight, 2)

