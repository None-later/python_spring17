
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv('employee_compensation.csv',sep=',')


# In[3]:

dept_comp=pd.DataFrame(df.groupby(['Organization Group','Department']).mean())
dept_comp=dept_comp[['Total Compensation']]
dept_comp.reset_index(level=(0,1), inplace=True)
dept_comp=dept_comp.sort_values(by=['Organization Group','Total Compensation'],ascending=[True,False])
dept_comp.reset_index()
dept_comp.to_csv('Q2_Part_1_Output.csv',  index = False)
print(dept_comp.head(10))

