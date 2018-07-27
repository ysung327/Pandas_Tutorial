
# coding: utf-8

# In[2]:


import quandl
import pandas as pd


# In[3]:


api_key = open('quandlapikey.txt','r').read()

df = quandl.get("FMAC/HPI_ID", authtoken=api_key, start_date="1999-01-01")
#if i use quandl api, the index of dataframe is set by date.


# In[4]:


print(df.head())


# In[5]:


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')


# In[6]:


# this is a list:
print(fiddy_states)


# In[7]:


#this is a dataframe.
print(fiddy_states[0])


# In[9]:


#this is a column
print(fiddy_states[0][1])


# In[11]:


for abbv in fiddy_states[0][1][1:]:
    print("FMAC/HPI_"+str(abbv))

