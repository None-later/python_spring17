
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv('employee_compensation.csv',sep=',') #Loading data into a dataframe from csv file.


# In[3]:

job_comp=df[(df['Year Type']=='Calendar')] #Filtering out the data with calendar as year type


# In[4]:

job_comp=pd.DataFrame(job_comp.groupby(['Employee Identifier','Job Family']).mean())  #Grouping the data by employes and getting avg salary per employee 


# In[5]:

job_comp.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True) #Removing unwanted columns


# In[6]:

print(job_comp.head())


# In[7]:

overtime=job_comp[(job_comp['Overtime']>(.05*job_comp['Salaries']))] #Filtering out employees with with overtime more than 5% of salary
print(overtime.head())


# In[8]:

top_family=overtime
top_family=top_family.groupby([top_family.index.get_level_values(1)]).mean() #Grouping the data according to job family.


# In[9]:

top_family=top_family[['Total Benefits','Total Compensation']] #Taking the necessary column from the data.
top_family['Percent_Total_Benefit']=100*(top_family['Total Benefits']/top_family['Total Compensation']) #Calculating the %
top_family=top_family.sort_values(['Percent_Total_Benefit'], ascending=[False]) #Sorting according to the %
top_family.to_csv('Q2_Part_2_Output.csv')
print(top_family.head(5))

