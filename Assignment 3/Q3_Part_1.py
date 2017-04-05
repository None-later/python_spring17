
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv('cricket_matches.csv',sep=',')


# In[3]:

cric_score=df[(df['home']==df['winner'])]
cric_score=cric_score[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]


# In[4]:

cric_score['Score']=0
pd.options.mode.chained_assignment = None #'warn'
cric_score['Score'][(cric_score['home']==cric_score['innings1'])] = cric_score['innings1_runs']
cric_score['Score'][(cric_score['home']==cric_score['innings2'])] = cric_score['innings2_runs']
cric_score=cric_score[['home','Score']]


# In[5]:

cric_score=pd.DataFrame(cric_score.groupby(['home']).mean())
cric_score.to_csv('Q3_Part_1_Output.csv')
print(cric_score.head())

