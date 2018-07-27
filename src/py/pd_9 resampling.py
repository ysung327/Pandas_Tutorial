
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[7]:


style.use('ggplot')


# In[11]:


HPI_data = pd.read_pickle('../src/fiddy_states_pct.pickle')


# In[12]:


#resampling. http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
TX1yr = HPI_data['TX'].resample('A').mean()
print(TX1yr.head())


# In[13]:


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data['TX'].plot(ax = ax1, label='Monthly TX HPI')
TX1yr.plot(ax = ax1, label='Yearly TX HPI')
         
plt.legend(loc=4)
plt.show()

