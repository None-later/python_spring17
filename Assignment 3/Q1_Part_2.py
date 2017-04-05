
# coding: utf-8

# In[1]:

import pandas as pd
import datetime


# In[2]:

df=pd.read_csv('vehicle_collisions.csv',sep=',')


# In[3]:

Borough_count=pd.DataFrame(df.groupby(['BOROUGH']).size())


# In[4]:

Borough_count[0]=list(Borough_count.index.values)


# In[5]:

Borough_count['One_Vehicle_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==True)& (df['VEHICLE 3 TYPE'].isnull()==True)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[6]:

Borough_count['Two_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==True)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[7]:

Borough_count['Three_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==False)& (df['VEHICLE 4 TYPE'].isnull()==True)& (df['VEHICLE 5 TYPE'].isnull()==True)]))


# In[8]:

Borough_count['More_Vehicles_Involved']=Borough_count[0].apply(lambda x : len(df[(df['BOROUGH']==x) & (df['VEHICLE 1 TYPE'].isnull()==False) & (df['VEHICLE 2 TYPE'].isnull()==False)& (df['VEHICLE 3 TYPE'].isnull()==False)& (((df['VEHICLE 4 TYPE'].isnull()==False)& (df['VEHICLE 5 TYPE'].isnull()==True))|((df['VEHICLE 4 TYPE'].isnull()==False)& (df['VEHICLE 5 TYPE'].isnull()==False)))]))


# In[9]:

del Borough_count[0]
Borough_count.to_csv('Q1_Part_2_Output.csv')
print(Borough_count)

