#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[8]:


df.head()


# In[18]:


df.columns


# In[15]:


#it will show the Statistical Analysis for only numerical Columns
df.describe()


# In[16]:


type(df)


# In[17]:


df.dtypes


# In[20]:


df[['Name','Sex','Ticket','Cabin','Embarked']]


# In[21]:


df.dtypes=='object'


# In[25]:


df.dtypes[df.dtypes=='object'].index


# In[26]:


df[df.dtypes[df.dtypes=='object'].index].describe()


# In[27]:


df.dtypes


# In[34]:


df[df.dtypes[df.dtypes=='float64'].index]


# In[37]:


df[df.dtypes[df.dtypes=='int64'].index]


# In[38]:


df['Ticket']


# In[44]:


df[['Ticket','Cabin']][4:11:2]


# In[51]:


df['new_col']=1


# In[52]:


df


# In[56]:


df['new_2']=df['PassengerId']+df['Pclass']


# In[57]:


df


# In[58]:


df.head()


# In[61]:


pd.Categorical(df['Pclass'])


# In[62]:


df['Cabin'].unique()


# In[65]:


df.head()


# In[67]:


df[df['Age']>18]


# In[69]:


len(df[df['Age']>18])


# In[70]:


df[df['Fare']>32]


# In[72]:


df[df['Sex']=='male']


# In[74]:


df[df['Sex']=='female']


# In[77]:


df[df["Pclass"]==1]


# In[79]:


df[df['Survived']==1]


# In[80]:


df['Sex']=='female'


# In[82]:


df['Fare']>32


# In[87]:


df[(df['Sex']=='female') & (df['Fare']>32)]


# In[92]:


df[(df['Age'] < 10) & (df['Fare'] > 32)]


# In[93]:


max(df['Fare'])


# In[94]:


df['Fare']==max


# In[96]:


df[df['Fare']==max(df["Fare"])]['Name']


# In[97]:


df.head()


# In[98]:


df[0:2]


# In[99]:


df[0::2]


# In[100]:


df[['PassengerId','Survived','Pclass']][0:2]


# In[104]:


df.iloc[0:2]


# In[109]:


df.iloc[0:2,[1,2,3]]


# In[110]:



df.loc[0:2,['Pclass','PassengerId','Survived']]


# In[ ]:




