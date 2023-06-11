#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data={'a':[1,2,7,8],'b':[7,7,6,4],'c':['pooja','komal','sharma','ladu']}


# In[3]:


data=pd.DataFrame(data)


# In[4]:


data


# In[5]:


data.set_index('a',inplace=True)


# In[6]:


data


# In[7]:


df=data.reset_index()


# In[8]:


df


# In[9]:


data={'a':[1,2,7,8],'b':[7,7,6,4],'c':['pooja','komal','sharma','ladu']}
df1=pd.DataFrame(data,index=['a','b','c','d'])


# In[10]:


df1


# # Rearrange Indexes

# In[11]:


df2=df1.reindex(['b','c','a','d'])


# In[12]:


df2


# In[13]:


df1


# In[14]:


for i in df.iterrows():
    print(i)


# In[15]:


for i,j in df.iterrows():
    print(i,j)


# In[16]:


for i in df1.iteritems():
    print(i)


# In[17]:


df1


# In[18]:


[i for i in df['a']]


# In[19]:


df1.reindex(['b','a','c','d'])


# In[20]:


df1.apply(lambda x:x.sum())


# In[21]:


def test(x):
    return x.sum()
df1.apply(test)


# In[22]:


df1
    


# In[23]:


df2=df1[['a','b']]


# In[24]:


df2


# In[25]:


df2.applymap(lambda x:x**2)


# In[26]:


df1.sort_values('c')


# In[27]:


df1.sort_index(ascending=False)


# In[28]:


pd.set_option("display.max_colwidth",1000)
df3=pd.DataFrame({"Desc":["Data Science Masters course is highly curated and uniquely designed according to the latest industry standards. This program instills students the skills essential to knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical, and computational skills needed to meet the large-scale data science challenges of today's professional world. You will learn all the stack required to work in data science, data analytics, and big data industry including cloud infrastructure and real-time industry projects.","My name is pooja","I used to teach dataScience"]})


# In[29]:


df3


# In[30]:


df3.apply(lambda x:len(x))


# In[31]:


df3.apply(len)


# In[32]:


df3['new']=df3['Desc'].apply(len)


# In[33]:


df3


# In[34]:


t="i used to love with Data Science"


# In[35]:


len(t.split())


# In[36]:


df3['word_count']= df3['Desc'].apply(lambda x: len(x.split()))


# In[37]:


df3


# In[38]:


df


# In[39]:


df[['a','b']][0:2]


# In[40]:


df.iloc[0:1]


# In[41]:


print(df.index)


# In[42]:


df.loc[0]


# In[43]:


df


# In[44]:


df['a'].mean()


# In[45]:


df['a'].std()


# In[46]:


df['a'].sum()


# In[47]:


df['a'].var()


# In[48]:


df4=pd.DataFrame({'a':[3,4,5,7,8]})


# In[49]:


df4


# In[50]:


df4['a'].rolling(window=1).mean()


# In[51]:


#-it will take above 2 no to calulate mean for eg 3,4->3+4/2
df4['a'].rolling(window=2).mean() 


# In[52]:


df4['a'].rolling(window=3).mean()


# In[53]:


df4['a'].rolling(window=3).sum()


# In[54]:


df4['a'].cumsum()


# # Date Functionality

# In[55]:


Date= pd.date_range(start='2023-04-23',end='2023-06-23')
Date


# In[60]:


data=pd.DataFrame({'Date':Date})


# In[61]:


data


# In[64]:


d5=pd.DataFrame({'date':['2023-06-20','2023-06-21','2023-06-22']})


# In[66]:


d5.dtypes


# In[68]:


d5['updated_date']=pd.to_datetime(d5['date'])


# In[69]:


d5


# In[70]:


d5.dtypes


# In[72]:


d5['Month']=d5['updated_date'].dt.month


# In[73]:


d5


# In[74]:


d5['Year']=d5['updated_date'].dt.year


# In[75]:


d5['day']=d5['updated_date'].dt.day


# In[76]:


d5


# # Time Delta
# it tells about difference b/w two dates and times

# In[79]:


pd.Timedelta(days=1,hours=5,minutes=45)


# In[80]:


dt=pd.to_datetime('2023-06-22')


# In[81]:


td=pd.Timedelta(days=1)


# In[82]:


dt+td


# # Python Pandas- Categorical Data

# In[83]:


data=["Pooja","Komal","Laddu","Radha"]


# In[85]:


cat=pd.Categorical(data)


# In[86]:


cat


# In[87]:


cat.value_counts()


# # Python Pandas Visulization

# In[89]:


d=pd.Series([1,2,3,3,4,5,5,6])


# In[90]:


d.plot()


# In[91]:


df=pd.DataFrame({'key1':[3,4,5,6],'key2':[4,5,6,7]})


# In[92]:


df


# In[95]:


df.plot(x='key1',y='key2')


# In[96]:


df.plot.scatter(x='key1',y='key2')


# In[97]:


df.plot.hist(x='key1',y='key2')


# In[99]:


d


# In[98]:


d.plot.pie()


# In[ ]:




