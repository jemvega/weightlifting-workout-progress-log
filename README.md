# Weightlifting Workout Progress Log

## Introduction
As a hobbyist weightlifter, I started this project to find a basic, efficient solution to log my workout exercises for a few reasons: good habits and routine, time organization, accountability, objective measurements of performance, and a summary of progress towards completing my fitness goals. For this project, I logged, cleaned, and analyzed my workout data using Python. I am hoping to make interesting observations or draw conclusions about my progress, my weightlifting programming, or relevant metrics. Once I have more data points, I am hoping to find relationships in the data. 

## Background
My interest in weightlifting began recently because of a shift in my fitness goals: I wanted to gain strength and improve my physique. I quickly learned that, if I wanted to observe my progress towards my achieving my goals, I needed to have objective and quantitative measurements. I began studying various fitness principles and methodologies until I could design my own weightlifting program - i.e. a schedule of selected exercises, frequency of training, intensity (weight, resistance, interval between sets, interval between training days per week), volume (number of repititions and number of sets), periodization (undulation, linearity, and conjugation), and time cycle (microcycle, mesocycle, and macrocycle) - that could fit my goals and ability. Since I started weightlifting, I have been using a journal to plan and log my workouts every week. 

## Data Selection/Entry
Because my workout data is kept in a journal, I created a Python file, `<weightlifting-workout-data-cleanup.py>`, which allowed me to input the data and write it to a .csv file `<workout_data_raw.csv`>.  

When logging my workout data into this repository, I only included the following metrics:
* Exercise, 
* Number of Sets, 
* Number of Reps, 
* Weight in Lbs, 
* Date
* Time, and
* Duration of complete workout including warm-up time in minutes. 
However, even some of these data points are empty/null, as I did not always remember to log the start time, end time, or duration of my workouts.

There is selection bias in the data because I only chose to log the following compound exercises: 
This workout data only takes into account the following exercises:
* Back Squat, 
* Overhead Squat, 
* Front Squat, 
* Deadlift, 
* Bench Press, 
* Shoulder Press, 
* Snatch Press, 
* Snatch, and 
* Clean & Jerk. 
Note that the back squat, bench press, and deadlift are the three competition lifts for powerlifting, and the snatch and clean & jerk are the two competition lifts for Olympic weightlifting. I include the overhead squat, front squat, and shoulder press, and snatch press because they are key supplemental exercises for improving in the snatch and clean & jerk. 

## Data Cleaning and Exporting
After logging my workout data into `<workout_data_raw`>, I used Python's Pandas to clean the data. For instance, I used Pandas to make sure the exercises had consistent names; I filled the null values with -1, and I changed the date and time format to a consistent datetime format. Finally, I saved the dataframe of clean data as a .csv file `<workout_data_database.csv`>.

Once I had a clean data set, I decided to use Python and MySQL Connector to insert the date from my `<workout_data_database.csv`> file into a `<workouts.db>` database file. I originally thought about creating a .db file with a few tables connected by primary and foreign keys, but I decided to just write it into one table. Ultimately, this step was not necessary to my project, but it served as a good opportunity for me to practice integrating Python and MySQL. 

## Data Visualizations
Once I had a clean data set, `<workout_data_database.csv`>, I used Tableau Public to create a few data visualization graphs. This process was fairly simple for me to do. 

I eventually decided to use Python's Pandas and Seaborn in my `<weightlifting-workout-data-visualizations>` file to see if I could replicate my Tableau visualizations. I spent much more time plotting my graphs using Pandas and Seaborn than I did using Tableau, but again, I see this as a good opportunity for practice. 

You can see my graphs in my [weightlifting-workout-data-visualizations.md](https://github.com/jemvega/weightlifting-workout-progress-log/blob/branch-jv/weightlifting-workout-data-visualizations.md)

## Stats
Here are a few stats I have after analyzing the data:
1. The average duration of my workouts in minutes out of 111 timed workouts is 77.41 minutes.
2. The average number of sets in my workouts is 2.46 sets. 
3. The average number of reps in my workouts is 5.37 reps. 
4. The average weight that I lift is 103.93 lbs. 
5. My front squat max to back squat max percent ratio is 68.89%. 
6. My deadlift max to shoulder press max percent ratio is 213.04% even though I my shoulder press total volume to deadlift total volume is 145.64%.
7. My squats total volume (total repitions) to presses total volume percent ratio is 132.97%, whereas my squats total intensity (total weight lifted) to presses total intensity is 160.38%. 
8. My snatch total intensity to clean & jerk total intensity percent ratio is 125.41%, whereas my snatch total volume to clean & jerk total volume is 163.70%. 

## Remarks/Observations on Stats
Here are a few remarks I have after analyzing the data and stats:
1. Even though I work on shoulder presses about 45.64% more than deadlift, my shoulder press max is only 46.93% of my deadlift max. 
2. The intensity of olympic lifts and overhead lifts (clean & jerk, snatch, shoulder press, overhead squat, and front squat) is much lower than the powerlifting lifts (back squat, bench press, and deadlift) more than likely because balancing heavy weight overhead is much more difficult than not. 
3. My Olympic lifts maxes are much lower than the powerlifting lifts maxes probably because they require much more technical profiency than I have. 
4. A comparison between the volume and intensity graphs seems to show a strong inverse relationship between volume (total reps) and intensity (total weight lifted) per workout session. While one could say this is largely due to the inherent bias in my workout program and goals, this is a phenomenon that the weightlifting community has already observed. I will not discuss the merits of high volume vs high intensity training, but by definition, a lifter cannot perform their one repetition personal maximum for multiple seets or reps. Moreover, a program that utilizes high volume and high intensity at the same time will eventually place too much stress on a lifter and probably lead the lifter to injury. 
5. One problem with my workout log as it stands is that it only shows when I did the 9 weightlifting exercises, but that does not necessarily mean that I did not workout on those non-recorded days. For instance, some times I run on non-lift days, or I do an active recovery day of bodyweight/calisthenic exercises.
6. I suspect that over time, I will continue to see gaps around the holidays, like Thanksgiving week, Christmas, and New Year's, as well as over vacation days. 

## Important Considerations
I knowingly exclude the following data from this repository and workout log:
* warm up exercises, 
* accessory workouts (e.g. push ups, dips, pull ups, lunges, calf raises, curls, rows, flyes, squat variations, etc.)
* supplemental exercises (e.g. snatch balance, hang snatch, tall snatch, muscle snatch, snatch exension, snatch turnover, power snatch, power clean, clean turnover, jerks, etc.)
The reason why I exclude these data points has mostly to do with the tediousness and time-consuming process of data entry. 

I understand that there are many factors that can affect fitness and overall health, and a more holistic approach to fitness tracking would take into consideration the following factors: 
* fitness goals,
* nutrition and diet, 
* body weight,
* sleep, 
* injuries,
* individual physique and ability, 
* proper technique, 
* stretching exercises, 
* supersets vs compound sets, 
* compound exercises vs isolation exercises,
* split system training (alternative sessions for muscle groups)
* components of overall fitness (muscular strength, muscular endurance, cardio respiratory endurance, flexbility, mobility, power, speed, joint strength, etc.)
* principles of weightlifting (regularity, specificity, overload, fatigue management, recovery, variation, phase potentiation, balance, etc.)
* training methodology (weight training, circuit training, isometric exercises, gymnastics, plyometrics, yoga, bodyweight training, calisthenics, running, swimming, etc.).

## Tests
As of right now, I have only been manually testing the app. I would like to create integration test checks and unit test checks. 

## Known Issues
* I keep receiving a "FutureWarning: Using a non-tuple sequence for multidimensial indexing is deprecated;" in my `<weightlifting-workout-data-visualizations>` file for what I believe is a scipy issue. 

## Future Changes/Caculations/Features
Here are some features I would like to add in the future:
* I would like to start logging my weight on a daily basis as one of the key metrics of health and fitness. 
* I would like to start logging my sleep start and end times. 
* I would like to log whether my workout sets were done as a superset or compound set. I believe there might be a positive correlation between the duration of my workout and a superset workout. 
* While there are data sets of powerlifting and olympic lifting maxes, I am more interested in the training data sets that produce maximum lifts. If I can find fitness training data sets, I would like to replicate this kind of analysis to observe the results to which various training programs can lead us. I imagine this can be replicated with other individual sports, e.g. running, swimming, cycling, CrossFit, etc. 
* I would like to analyze on which days I most often workout, as well as figure out what time in the day I most often workout. 
* I would like to add two data columns for primary and secondary muscle groups for each exercise. If I do end up adding my accessory and supplemental lifts, I think I may be able to answer questions like, "Which muscle group is being over or under worked?" "Which muscle group has seen the most improvement?" "Which muscle group do I favor to target?" 

## Built With

* [Python](https://www.python.org/downloads/) programming language

* [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) GUI

* [MySQL](https://mysql.com) Database

* [Notepad++](https://notepad-plus-plus.org/) for README.md and LICENSE.txt

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

* **Jem Vega** - *Initial work* - [JemVega](https://github.com/JemVega)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

