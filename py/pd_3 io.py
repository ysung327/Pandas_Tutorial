
# coding: utf-8

# In[2]:


import pandas as pd
import pandas.io


# In[3]:


df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')


# In[4]:


print(df.head())


# In[5]:


df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')


# In[6]:


print(df.head())


# In[9]:


df = pd.read_csv('newcsv2.csv')
print(df.head()) #csv file does not have index. so, it prints default index.

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())


# In[8]:


df.columns = ['Austin_HPI'] #rename column's name
print(df.head())


# In[10]:


df.to_csv('newcsv3.csv')


# In[11]:


df.to_csv('newcsv4.csv', header=False) #delete header


# In[18]:


df = pd.read_csv('newcsv3.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head()) #header remains

print('\n')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())


# In[19]:


#convert dataframe into html table
df.to_html('example.html')


# In[21]:


df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])
print(df.head())

print('\n')

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)
print(df.head())

