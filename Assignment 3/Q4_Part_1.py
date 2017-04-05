
# coding: utf-8

# In[384]:

import pandas as pd
import re
import numpy as np


# In[385]:

df=pd.read_csv('movies_awards.csv',sep=',')


# In[386]:

mov_awards=df[['Awards']]
mov_awards=mov_awards[mov_awards['Awards'].isnull()==False ]
pd.options.mode.chained_assignment = None #'warn'


# In[387]:

mov_awards['Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r"(\d+) win", x)))
mov_awards['Awards_won']=mov_awards['Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Awards_won']=mov_awards['Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[388]:

mov_awards['Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'(\d+) nom', x)))
mov_awards['Awards_nominated']=mov_awards['Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Awards_nominated']=mov_awards['Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[389]:

mov_awards['Oscar_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Oscar', x)))
mov_awards['Oscar_Awards_won']=mov_awards['Oscar_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Oscar_Awards_won']=mov_awards['Oscar_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[390]:

mov_awards['Golden_Globe_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Golden', x)))
mov_awards['Golden_Globe_Awards_won']=mov_awards['Golden_Globe_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Golden_Globe_Awards_won']=mov_awards['Golden_Globe_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[391]:

mov_awards['Prime_Emmys_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Prime', x)))
mov_awards['Prime_Emmys_Awards_won']=mov_awards['Prime_Emmys_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Prime_Emmys_Awards_won']=mov_awards['Prime_Emmys_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[392]:

mov_awards['BAFTA_Awards_won']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Won (\d+) BAFTA', x)))
mov_awards['BAFTA_Awards_won']=mov_awards['BAFTA_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['BAFTA_Awards_won']=mov_awards['BAFTA_Awards_won'].apply(lambda x : list(map(int,x))[0])


# In[393]:

mov_awards['Oscar_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Oscar', x)))
mov_awards['Oscar_Awards_nominated']=mov_awards['Oscar_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Oscar_Awards_nominated']=mov_awards['Oscar_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[394]:

mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Golden', x)))
mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Golden_Globe_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Golden_Globe_Awards_nominated']=mov_awards['Golden_Globe_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[395]:

mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Prime', x)))
mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Prime_Emmys_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['Prime_Emmys_Awards_nominated']=mov_awards['Prime_Emmys_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[396]:

mov_awards['BAFTA_Awards_nominated']=mov_awards['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) BAFTA', x)))
mov_awards['BAFTA_Awards_nominated']=mov_awards['BAFTA_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
mov_awards['BAFTA_Awards_nominated']=mov_awards['BAFTA_Awards_nominated'].apply(lambda x : list(map(int,x))[0])


# In[397]:

mov_awards['Awards_won']=mov_awards['Awards_won']+mov_awards['Oscar_Awards_won']+mov_awards['Golden_Globe_Awards_won']+mov_awards['Prime_Emmys_Awards_won']+mov_awards['BAFTA_Awards_won']
mov_awards['Awards_nominated']=mov_awards['Awards_nominated']+mov_awards['Oscar_Awards_nominated']+mov_awards['Golden_Globe_Awards_nominated']+mov_awards['Prime_Emmys_Awards_nominated']+mov_awards['BAFTA_Awards_nominated']


# In[398]:

mov_awards.to_csv('Q4_Part_1_Output.csv',  index = False)
print(mov_awards.head())

