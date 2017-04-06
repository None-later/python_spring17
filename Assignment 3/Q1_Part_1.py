
# coding: utf-8

# In[1]:

import pandas as pd
import datetime


# In[2]:

df=pd.read_csv('vehicle_collisions.csv',sep=',') #Loading data into a dataframe from csv file.


# In[3]:

df['DATE'] = pd.to_datetime(df['DATE']) #Converting the Date column to datetime format.
ny_accident=df[(df['DATE']<"1/1/17")& (df['DATE']>"12/31/15")] #Data for entire newyork, 2016
man_accident=df[(df['DATE']<"1/1/17")& (df['DATE']>"12/31/15")&(df['BOROUGH']=='MANHATTAN')] #Data for manhattan, 2016


# In[4]:

pd.options.mode.chained_assignment = None #'warn'
ny_accident['MONTH']=ny_accident['DATE'].apply(lambda x : x.strftime("%b")) #Adding column  of correspoding month names.


# In[5]:

man_accident['MONTH']=man_accident['DATE'].apply(lambda x : x.strftime("%b")) #Adding column  of correspoding month names.


# In[6]:

ny_accident=ny_accident[['MONTH','DATE','BOROUGH','UNIQUE KEY']]
ny_count=pd.DataFrame(ny_accident.groupby(['MONTH']).size()) #Taking the count of each month
print(ny_count.head())


# In[7]:

man_accident=man_accident[['MONTH','DATE','BOROUGH','UNIQUE KEY']]
man_count=pd.DataFrame(man_accident.groupby(['MONTH']).size()) #Taking the count of each month
print(man_count.head())


# In[8]:

man_count.rename(columns={0: 'MANHATTAN'}, inplace=True)
ny_count.rename(columns={0: 'NYC'}, inplace=True)
percent_out=pd.concat([man_count, ny_count], axis=1, join='inner') #Joining the newyork and manhattan data.


# In[9]:

percent_out['PERCENTAGE']=percent_out['MANHATTAN']/percent_out['NYC'] #Calculating percentage


# In[10]:

percent_out.to_csv('Q1_Part_1_Output.csv')
print(percent_out.head())

