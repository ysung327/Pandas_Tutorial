
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])


# In[3]:


''' When does we use the merge?
you might controll all the user data from your website. 
But it is unefficient to manage all of data at one dataframe.
So, dataframe is spilt into small dataframe with sharing common index, 'username'.
When user want to change their username, all of small dataframes should be merged.
'''


# In[4]:


print(pd.merge(df1,df2, on=['HPI','Int_rate']))


# In[5]:


df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
print(joined)


# In[7]:


df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df3 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})


# In[15]:


merged = pd.merge(df1, df3, on='Year')
merged.set_index('Year',inplace=True)
print(merged)

print('\n df1')

merged = pd.merge(df1, df3, on='Year', how='left')
merged.set_index('Year',inplace=True)
print(merged)

print('\n df3')

merged = pd.merge(df1, df3, on='Year', how='right')
merged.set_index('Year',inplace=True)
print(merged)

print('\n 합집합')
#합집합
merged = pd.merge(df1, df3, on='Year', how='outer')
merged.set_index('Year',inplace=True)
print(merged)

print('\n 교집합')
#교집합
merged = pd.merge(df1, df3, on='Year', how='inner')
merged.set_index('Year',inplace=True)
print(merged)

