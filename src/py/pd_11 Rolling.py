
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[35]:


style.use('ggplot')


# In[39]:


HPI_data = pd.read_pickle('../src/fiddy_states.pickle')


# In[36]:


def Rolling_data_12ma(HPI_data):
    
    '''if you want to get onw huge dataframe, then this is gonna be a solution.
    HPI_data[{}_12ma.format(column)] = HPI_data[column].rolling(12).mean()'''
    
    columns = HPI_data.columns.values
    HPI_data_12ma = HPI_data.rolling(12).mean()
    for column in columns:
        HPI_data_12ma.rename(columns={column : '{}_12ma'.format(column)}, inplace=True) 
    HPI_data_12ma.to_pickle('../src/fiddy_states_12ma.pickle')
    return HPI_data_12ma


# In[37]:


HPI_data_12ma = Rolling_data(HPI_data)


# In[38]:


print(HPI_data_12ma)


# In[42]:


def Rolling_data_12std(HPI_data):
    columns = HPI_data.columns.values
    HPI_data_12std = HPI_data.rolling(12).std()
    for column in columns:
        HPI_data_12std.rename(columns={column : '{}_12std'.format(column)}, inplace=True) 
    HPI_data_12std.to_pickle('../src/fiddy_states_12std.pickle')
    return HPI_data_12std


# In[45]:


HPI_data_12std = Rolling_data_12std(HPI_data)
print(HPI_data_12std)


# In[46]:


fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

HPI_data['TX'].plot(ax = ax1)
HPI_data_12ma['TX_12ma'].plot(ax = ax1)
HPI_data_12std['TX_12std'].plot(ax = ax2)
plt.legend().remove()
plt.show()

