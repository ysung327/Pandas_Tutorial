
# coding: utf-8

# In[18]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl


# In[21]:


api_key = open('quandlapikey.txt','r').read()


# In[12]:


def Convert_Price_to_Percentage():
    HPI_data = pd.read_pickle('fiddy_states.pickle')
    columns = HPI_data.columns.values
    #print(columns)
    for abbv in columns:
        HPI_data[abbv] = (HPI_data[abbv] - HPI_data[abbv][0]) /  HPI_data[abbv][0] * 100
    print(HPI_data.head())
    HPI_data.to_pickle('fiddy_states_pct.pickle')
    return HPI_data


# In[13]:


HPI_data = Convert_Price_to_Percentage()


# In[14]:


HPI_data.plot()
plt.legend().remove()
plt.show()


# In[ ]:


# define benchmark and use it as standard.


# In[26]:


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key, start_date="1999-01-31")
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100
    return df


# In[27]:


benchmark = HPI_Benchmark()


# In[30]:


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
HPI_data.plot(ax=ax1)
benchmark.plot(ax=ax1, color='k', linewidth=10)


plt.legend().remove()
plt.show()


# In[32]:


# check correlation of HPI_data.
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)


# In[33]:


# how to find max or min correlation of these.
print(HPI_State_Correlation.describe())

