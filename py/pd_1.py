
# coding: utf-8

# In[11]:


# virtualenv에서 idle 실행하기.  python -m idlelib


# In[12]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style


# In[6]:


style.use('ggplot')


# In[7]:


start = datetime.datetime(2011,6,11)
end = datetime.datetime.now()


# In[8]:


#pull data from morningstar
df = web.DataReader('XOM','morningstar', start, end) 


# In[10]:


print(df.head())


# In[13]:


df['High'].plot()
plt.legend()
plt.show()

