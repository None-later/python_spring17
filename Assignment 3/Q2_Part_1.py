
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv('employee_compensation.csv',sep=',') #Loading data into a dataframe from csv file.


# In[3]:

dept_comp=pd.DataFrame(df.groupby(['Organization Group','Department']).mean()) #Grouping data by Organization and Department with their mean compensation.
dept_comp=dept_comp[['Total Compensation']] #Removed all the unwanted columns.
dept_comp.reset_index(level=(0,1), inplace=True)
dept_comp=dept_comp.sort_values(by=['Organization Group','Total Compensation'],ascending=[True,False]) #Sorting the data according to highest to lowest compensation in each organization
dept_comp.reset_index()
dept_comp.to_csv('Q2_Part_1_Output.csv',  index = False)
print(dept_comp.head(10))

