
# coding: utf-8

# In[6]:

import pandas as pd


# In[7]:

df=pd.read_csv('cricket_matches.csv',sep=',') #Loading data into a dataframe from csv file.


# In[8]:

cric_score=df[(df['home']==df['winner'])] #Taking the data of the matches which home team has won.
cric_score=cric_score[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] # Taking the needed columns.


# In[9]:

cric_score['Score']=0 #Adding a column Score with default value 0
pd.options.mode.chained_assignment = None #'warn'
#Checking which innings the home team played and adding it to score.
cric_score['Score'][(cric_score['home']==cric_score['innings1'])] = cric_score['innings1_runs'] 
cric_score['Score'][(cric_score['home']==cric_score['innings2'])] = cric_score['innings2_runs']
cric_score=cric_score[['home','Score']]


# In[10]:

cric_score=pd.DataFrame(cric_score.groupby(['home']).mean()) #Taking the avg score of each team.
cric_score.to_csv('Q3_Part_1_Output.csv')
print(cric_score.head())

