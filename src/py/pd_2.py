
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


# In[2]:


web_stats = {'Day':[1,2,3,4,5], 'Visitors':[43,53,34,64,34], 'Bounce_Rate':[65,72,43,64,25]}
#if array length is different, pd.DataFrame() cannot convert dic into dataframe.

df = pd.DataFrame(web_stats)
print(df)


# In[3]:


#set index


# In[4]:


print(df.set_index('Day')) #df.set_index() returns new dataframe. 

print(df)


# In[5]:


'''
df = df.set_index('Day') redefine on dataframe
print(df)
'''
#2
df.set_index('Day', inplace=True) #redefine dataframe with inplace params
print(df)


# In[6]:


#print specific columns
print(df['Visitors']) 

print(df.Visitors)


# In[7]:


#multiple columns
print(df[['Visitors','Bounce_Rate']])


# In[8]:


print(df.Visitors.tolist())


# In[9]:


print(df[['Visitors','Bounce_Rate']].tolist())


# In[10]:


#using numpy
print(np.array(df[['Visitors','Bounce_Rate']]))


# In[13]:


#make list to dataframe. there are no column keys.
df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))
print(df2)

