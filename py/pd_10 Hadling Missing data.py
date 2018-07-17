
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[6]:


style.use('ggplot')


# In[22]:


def OneYear_Resampling():
    HPI_data = pd.read_pickle('../src/fiddy_states_pct.pickle')
    columns = HPI_data.columns.values
    for column in columns:
        HPI_data[column] = HPI_data[column].resample('A').mean()
    return HPI_data


# In[23]:


HPI_data = OneYear_Resampling()


# In[24]:


print(HPI_data.head()) #there are lots of na


# In[25]:


HPI_data_drop = HPI_data.dropna()


# In[26]:


print(HPI_data_drop.head())


# In[27]:


HPI_data_fill = HPI_data.fillna(method='ffill')
print(HPI_data_fill.head())

