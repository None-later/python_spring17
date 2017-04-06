
# coding: utf-8

# In[1]:

import pandas as pd
import datetime


# In[2]:

df=pd.read_csv('vehicle_collisions.csv',sep=',') #Loading data into a dataframe from csv file.


# In[3]:

Borough_count=pd.DataFrame(df.groupby(['BOROUGH']).size()) #Grouping the data in the dataframe according to the BOROUGH


# In[4]:

Borough_count[0]=list(Borough_count.index.values) #Adding BOROUGH names as column values.


# In[5]:

#Using Lambda counted the no of rows with just vehicle 1
Borough_count['One_Vehicle_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==True)& (df['VEHICLE 3 TYPE'].isnull()==True)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[6]:

#Using Lambda counted the no of rows with just vehicle 1 and vehicle 2
Borough_count['Two_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==True)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[7]:

#Using Lambda counted the no of rows with just vehicle 1, vehicle 2 and vehicle 3
Borough_count['Three_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==False)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[8]:

#Using Lambda counted the no of rows with more than 3 vehicles
Borough_count['More_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==False)& (((df['VEHICLE 4 TYPE'].isnull()==False)& (df['VEHICLE 5 TYPE'].isnull()==True))|((df['VEHICLE 4 TYPE'].isnull()==False)& (df['VEHICLE 5 TYPE'].isnull()==False)))]))


# In[9]:

del Borough_count[0]
Borough_count.to_csv('Q1_Part_2_Output.csv')
print(Borough_count)

