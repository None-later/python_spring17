
# coding: utf-8

# In[1]:

import pandas as pd
import re
import numpy as np


# In[2]:

df=pd.read_csv('movies_awards.csv',sep=',') #Loading data into a dataframe from csv file.


# In[3]:

mov_awards=df[['Awards']]
mov_awards=mov_awards[mov_awards['Awards'].isnull()==False ] #Removing rows with Award as null
pd.options.mode.chained_assignment = None #'warn'


# In[4]:

#Extracting the relevant digit from the awards column using regex and placing it in Awards_won column.
mov_awards['Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r"(\d+) win", x)))
#Replacing empty list with '[0]'
mov_awards['Awards_won']=mov_awards['Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
#Replacing the list with the integer values from it.
mov_awards['Awards_won']=mov_awards['Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[5]:

mov_awards['Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'(\d+) nom', x)))
mov_awards['Awards_nominated']=mov_awards['Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Awards_nominated']=mov_awards['Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[6]:

mov_awards['Oscar_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Oscar', x)))
mov_awards['Oscar_Awards_won']=mov_awards['Oscar_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Oscar_Awards_won']=mov_awards['Oscar_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[7]:

mov_awards['Golden_Globe_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Golden', x)))
mov_awards['Golden_Globe_Awards_won']=mov_awards['Golden_Globe_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Golden_Globe_Awards_won']=mov_awards['Golden_Globe_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[8]:

mov_awards['Prime_Emmys_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Prime', x)))
mov_awards['Prime_Emmys_Awards_won']=mov_awards['Prime_Emmys_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Prime_Emmys_Awards_won']=mov_awards['Prime_Emmys_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[9]:

mov_awards['BAFTA_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) BAFTA', x)))
mov_awards['BAFTA_Awards_won']=mov_awards['BAFTA_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['BAFTA_Awards_won']=mov_awards['BAFTA_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[10]:

mov_awards['Oscar_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Oscar', x)))
mov_awards['Oscar_Awards_nominated']=mov_awards['Oscar_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Oscar_Awards_nominated']=mov_awards['Oscar_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[11]:

mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Golden', x)))
mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Golden_Globe_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Golden_Globe_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[12]:

mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Prime', x)))
mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Prime_Emmys_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Prime_Emmys_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[13]:

mov_awards['BAFTA_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) BAFTA', x)))
mov_awards['BAFTA_Awards_nominated']=mov_awards['BAFTA_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['BAFTA_Awards_nominated']=mov_awards['BAFTA_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[14]:

#Taking aggregate of awards won and nominated.
mov_awards['Awards_won']=mov_awards['Awards_won']+mov_awards['Oscar_Awards_won']+mov_awards['Golden_Globe_Awards_won']+mov_awards['Prime_Emmys_Awards_won']+mov_awards['BAFTA_Awards_won']
mov_awards['Awards_nominated']=mov_awards['Awards_nominated']+mov_awards['Oscar_Awards_nominated']+mov_awards['Golden_Globe_Awards_nominated']+mov_awards['Prime_Emmys_Awards_nominated']+mov_awards['BAFTA_Awards_nominated']


# In[15]:

mov_awards.to_csv('Q4_Part_1_Output.csv',  index = False)
print(mov_awards.head())

