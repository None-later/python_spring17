
# coding: utf-8

# In[1]:

import pandas as pd
import datetime


# In[2]:

df=pd.read_csv('vehicle_collisions.csv',sep=',')


# In[3]:

df['DATE'] = pd.to_datetime(df['DATE'])
ny_accident=df[(df['DATE']<"1/1/17")& (df['DATE']>"12/31/15")]
man_accident=df[(df['DATE']<"1/1/17")& (df['DATE']>"12/31/15")&(df['BOROUGH']=='MANHATTAN')]


# In[4]:

pd.options.mode.chained_assignment = None #'warn'
ny_accident['MONTH']=ny_accident['DATE'].apply(lambda x : x.strftime("%b"))


# In[5]:

man_accident['MONTH']=man_accident['DATE'].apply(lambda x : x.strftime("%b"))


# In[6]:

ny_accident=ny_accident[['MONTH','DATE','BOROUGH','UNIQUE KEY']]
ny_count=pd.DataFrame(ny_accident.groupby(['MONTH']).size())
print(ny_count.head())


# In[7]:

man_accident=man_accident[['MONTH','DATE','BOROUGH','UNIQUE KEY']]
man_count=pd.DataFrame(man_accident.groupby(['MONTH']).size())
print(man_count.head())


# In[8]:

man_count.rename(columns={0: 'MANHATTAN'}, inplace=True)
ny_count.rename(columns={0: 'NYC'}, inplace=True)
percent_out=pd.concat([man_count, ny_count], axis=1, join='inner')


# In[9]:

percent_out['PERCENTAGE']=percent_out['MANHATTAN']/percent_out['NYC']


# In[10]:

percent_out.to_csv('Q1_Part_1_Output.csv')
print(percent_out.head())

