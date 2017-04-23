# Python_Spring17_Final

### Collection & Storage:
Data was downloaded from 'api.football-data.org' which has a call rate of 50/min. Data collection was done in 3 steps in order to maintain the call rate.
- STEP 1 - For the season of 2015-16 and 2016-17 competition data was downloaded and stored separately in the folder with competition name which is in the respective season folder.Also each of the competition fixtures were downloaded and stored separately in fixture folder of the respective competition.
- STEP 2 - Iterating through each of the stored comeptiton data file the competition id was extracted.With this id the competition point table was downloaded and stored in the same folder.
- STEP 3 - Iterating through each of the stored comeptiton data file the competition id was extracted.With this id the data of each team playing in each competiton was downloaded and stored separately in the teams folder.
<img width="420" alt="screen shot 2017-04-22 at 6 13 49 pm" src="https://cloud.githubusercontent.com/assets/22924110/25308736/79a14a6a-2789-11e7-96c0-056ce9e3a843.png">

Other than the API data few extra data about each leagues we taken. the are stored in 'data/extra_data' and details of this data is provided in the extra data notes.txt file.

<img width="420" alt="screen shot 2017-04-22 at 9 54 11 pm" src="https://cloud.githubusercontent.com/assets/22924110/25309896/79c82e10-27a6-11e7-9075-726da0608c78.png">

### Analysis 1:
Analyzed each of the leagues point table data to find which league is more competitive.
- STEP 1 - An empty data frame was created.
- STEP 2 - Iterating through each of the stored league point table the data was added to the data frame.
- STEP 3 - Added the respective league's names to each of the leagues data.
- STEP 4 - A strip plot was ploted with league names as X axsis and the points as Y axsis.
<img width="800" alt="screen shot 2017-04-21 at 9 12 08 pm" src="https://cloud.githubusercontent.com/assets/22924110/25300189/a17d2b60-26d7-11e7-922d-9fd21cc30787.png">



### Analysis 2:
Analyzed each match of each league and found the ratio of home team and away team wining the match after conceding in the first half.
- STEP 1 - For the 2015 season for leagues such as Premier League, 1. Bundesliga, Primera Division, Ligue 1 

<img width="800" alt="screen shot 2017-04-21 at 9 13 34 pm" src="https://cloud.githubusercontent.com/assets/22924110/25300190/a34ef612-26d7-11e7-9193-27f157886fe0.png">




### Analysis 3:
Analyzed each match in premire league 2015 and calculated the conversion rate of chances created by each team home,away and in total.
- STEP 1
<img width="800" alt="screen shot 2017-04-22 at 4 26 44 pm" src="https://cloud.githubusercontent.com/assets/22924110/25307979/f15c5ed4-2778-11e7-9c98-d5b2ccab4b56.png">


<img width="800" alt="screen shot 2017-04-22 at 4 27 03 pm" src="https://cloud.githubusercontent.com/assets/22924110/25307980/f1640f12-2778-11e7-92cf-36bc4934f377.png">


<img width="800" alt="screen shot 2017-04-22 at 4 26 30 pm" src="https://cloud.githubusercontent.com/assets/22924110/25307981/f164ba7a-2778-11e7-9bb0-8c5c23e92e3c.png">
