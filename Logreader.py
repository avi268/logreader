#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import json
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import LabelEncoder


# In[2]:


with open('./july_31.log','r') as f:
    log = f.readlines()
    print(log)


# In[35]:


date = []
#time = []
Info = []
with open('./july_31.log','r') as f:
    read = f.readlines()
    #print(read)
    for a in read:
        dt = a.split(',')[0]
        #tm = a.split(' ')[1]
        info = a.split(': ')[1]
        date.append(dt)
        time.append(tm)
        Info.append(info)


# In[36]:


date


# In[37]:


log_df = pd.DataFrame()


# In[38]:


log_df['Date'] = date
#log_df['Time'] = time
log_df['Info'] = Info


# In[39]:


log_df['Info'].value_counts()


# In[40]:


log_df.replace(to_replace='Person Detected\n',value='Person Detected',inplace=True)


# In[41]:


log_df.head()


# In[9]:


rm_ms = []
for i in list(log_df['Time']):
    clc = re.match(r'\d+:\d+:\d+',i)
    rm_ms.append(clc.group(0))


# In[10]:


log_df['Time'] = rm_ms


# In[42]:


log_df


# In[43]:


log_df.info()


# In[13]:


#log_df['Date'] = pd.to_datetime(log_df['Date'])


# In[14]:


#log_df['Time'] = pd.to_timedelta(log_df['Time'])


# In[44]:


log_df.info()


# In[45]:


le = LabelEncoder()


# In[46]:


log_df['Info'] = le.fit_transform(log_df['Info'])


# In[47]:


timegroup = log_df.groupby('Date')


# In[49]:


data = pd.DataFrame(log_df['Date'].value_counts())


# In[50]:


data.reset_index(inplace=True)


# In[51]:


Final_df = pd.DataFrame()


# In[53]:


Final_df['Time'] = data['index']
Final_df['Count'] = data['Date']


# In[54]:


sorted(list(Final_df['Time']))


# In[55]:


Final_df.sort_values(by='Time',inplace=True)


# In[56]:


Final_df.reset_index(inplace=True)


# In[57]:


Final_df.head(3)


# In[58]:


Final_Data = Final_df[['Time','Count']]


# In[59]:


Final_Data


# In[60]:


Final_Data.to_csv('log_data.csv')


# In[61]:


plt.figure(figsize=(20,4))
plt.bar(Final_Data['Time'],Final_Data['Count'])


# In[62]:


plt.figure(figsize=(15,4))
sns.barplot(Final_Data['Time'],Final_Data['Count'])
plt.xticks(rotation=270)


# In[ ]:




