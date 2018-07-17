
# coding: utf-8

# In[1]:


import quandl
import pandas as pd
import pickle


# In[2]:


api_key = open('quandlapikey.txt','r').read()


# In[7]:


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]


# In[8]:


def grab_initial_state_HPI():
    states = state_list()
    main_df = pd.DataFrame()
    
    for abbv in states:
        print("FMAC/HPI_"+str(abbv))
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key, start_date="1999-01-31")
        df.columns = [str(abbv)]
    
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    print('\n')
    print(main_df.head())
    
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    


# In[9]:


#grab_initial_state_HPI()


# In[11]:


pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data.head())


# In[ ]:


# There are also pandas own pickling methodology.
# more faster when dealing with astronomical data set.


# In[ ]:


HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2.head())

