
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[4]:


style.use('fivethirtyeight')


# In[ ]:


# we want to wipe out the error data from dataset. 
# By using rolling std.


# In[5]:


bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}


# In[21]:


df = pd.DataFrame(bridge_height)
print(df)


# In[22]:


df['STD'] = df['meters'].rolling(2).std()
print(df)


# In[23]:


df_std = df.describe()
df_threshold = df_std['meters']['std'] 
print(df_std)
print('\n')
print(df_threshold)


# In[25]:


# Comparison Operator can select data which satisfies certain condition.

df = df[ (df['STD'] < df_threshold) ] 
print(df)


# In[13]:


df.plot()
plt.show()

