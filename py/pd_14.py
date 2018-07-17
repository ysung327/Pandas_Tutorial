
# coding: utf-8

# In[1]:


import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style


# In[2]:


style.use('ggplot')


# In[3]:


api_key = open('../src/quandlapikey.txt', 'r').read()


# In[4]:


mor30 = pd.read_pickle('../src/fiddy_mortage_30yr.pickle')
HPI_data = pd.read_pickle('../src/fiddy_states_pct.pickle')
benchmark = pd.read_pickle('../src/fiddy_USA.pickle')


# In[5]:


def sp500_data():
    df = quandl.get("BCIW/_INX", start_date="1975-01-01", authtoken=api_key)
    df["Close"] = (df["Close"]-df["Close"][0]) / df["Close"][0] * 100
    df = df.resample('M').mean()
    df.rename(columns={'Close' : 'sp500'}, inplace=True)
    df = df['sp500']
    df.to_pickle('../src/sp500_index.pickle')
    return df


# In[6]:


sp500 = sp500_data()


# In[ ]:


# gdp_data or us_unemployment might be added.


# In[10]:


HPI = HPI_data.join([mor30, sp500])


# In[11]:


print(HPI)
print("\n")
print(HPI.corr())

