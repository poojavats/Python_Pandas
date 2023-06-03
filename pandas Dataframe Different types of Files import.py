#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # import CSV files

# In[2]:


df=pd.read_csv("services.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


type(df)


# In[6]:


list(df.columns)


# In[7]:


df[['name','service_areas','taxonomy_ids']]


# In[8]:


type(df['status'])


# In[9]:


list(df['status'])


# In[10]:


df[['status']]


# In[11]:


type(df[['status']])


# In[12]:


df.dtypes


# # Import Excel Files

# In[13]:


df1=pd.read_excel("LUSID Excel.xlsx")


# In[14]:


type(df1)


# In[15]:


df1.dtypes


# In[16]:


df1.columns


# In[17]:


df1[['Unnamed: 6','Unnamed: 8']]


# # Import Html File

# In[18]:


df2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[19]:


df2


# In[20]:


type(df2)


# In[21]:


df2[['Pclass']]


# In[22]:


type(df2[['Pclass']])


# In[23]:


df2.tail(3)


# # Import HTML File
# 

# In[36]:


df3=pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')


# In[25]:


df3


# In[26]:


len(df3)


# In[27]:


type(df3)


# In[28]:


df3=df3[0]


# In[29]:


df3


# In[30]:


df3.head()


# In[31]:


df3.tail()


# In[32]:


df3.columns


# In[33]:


df3.dtypes


# In[34]:


df3[['Player','TOV']]


# In[35]:


df3.to_csv("player.csv",index=False)


# In[ ]:




