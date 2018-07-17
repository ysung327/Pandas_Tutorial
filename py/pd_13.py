
# coding: utf-8

# In[2]:


import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style


# In[3]:


style.use('ggplot')


# In[8]:


api_key = open('../src/quandlapikey.txt', 'r').read()


# In[23]:


def mortage_30yr():
    df = quandl.get("FMAC/MORTG", start_date='1975-01-01', authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100
    df = df.resample('M').mean()
    df.columns = ['M30']
    df.to_pickle('../src/fiddy_mortage_30yr.pickle')
    return df


# In[24]:


mor30 = mortage_30yr()
print(mor30.head())


# In[25]:


HPI_data = pd.read_pickle('../src/fiddy_states_pct.pickle')
benchmark = pd.read_pickle('../src/fiddy_USA.pickle')


# In[27]:


state_HPI_M30 = HPI_data.join(mor30)
print(state_HPI_M30.corr())


# In[28]:


print(state_HPI_M30.corr()['M30'].describe())

