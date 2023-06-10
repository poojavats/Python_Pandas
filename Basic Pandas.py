#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[3]:


df.head()


# In[4]:


df.columns


# # Drop Column

# In[5]:


df1=df.drop('PassengerId',axis=1,inplace=True)


# In[6]:


df.head()


# In[7]:


df.drop(3,inplace=True)


# In[8]:


df


# # Set Index

# In[9]:


df.set_index('Name',inplace=True)


# In[10]:


df


# In[11]:


df.reset_index(inplace=True)


# In[12]:


df


# In[13]:


d={'a':[3,4,5,7],'b':[8,7,6,7],'c':[7,8,4,6]}


# In[14]:


d=pd.DataFrame(d)


# In[15]:


d


# In[16]:


d.set_index('a')


# In[17]:


d.set_index('c')


# In[18]:


df1=pd.read_csv('taxonomy.csv.xls')


# In[19]:


df1


# In[20]:


df1.dropna(inplace=True)


# In[21]:


df1


# In[22]:


df1.dropna(axis=1)


# In[23]:


df2=pd.read_csv('taxonomy.csv.xls')


# In[24]:


df2


# In[25]:


df2.dropna(axis=1)


# # fill all null values with any name

# In[26]:


df2.fillna("Ram")


# In[27]:


df


# In[28]:


g=df.groupby('Survived')


# In[29]:


g


# In[30]:


g.sum()


# In[31]:


g.mean()


# In[32]:


g1=df.groupby('Pclass')


# In[33]:


g1.sum()


# In[34]:


g1.max()


# In[35]:


g1.mean()


# In[36]:


g1.max()['Fare']


# In[37]:


g1.max()['Fare'].T


# In[38]:


g1.max().T


# In[39]:


df


# In[40]:


df1


# In[41]:


df5=df[['Name','Survived','Pclass']][0:5]


# In[42]:


df6=df[['Name','Survived','Pclass']][6:10]


# # Vertical Concat

# In[43]:


pd.concat([df5,df6])


# # Horizontal Concat

# In[44]:


df7=pd.concat([df5,df6],axis=1)


# In[45]:


df7.fillna("Pooja")


# In[46]:


df11=pd.DataFrame({'key1':[7,8,9,4],'key2':[5,7,9,4],'key3':[5,7,4,3]})


# In[47]:


df11


# In[48]:


df12=pd.DataFrame({'key1':[14,8,9,5,80],'key4':[90,7,7,10,45],'key5':[55,6,70,47,34]})


# In[49]:


df12


# In[50]:


df11


# In[51]:


#pd.concat([df11,df12])


# # It will Take the common numbers and key which will be avilable in bot of the dataset

# In[52]:


pd.merge(df11,df12)


# In[53]:


pd.merge(df11,df12,how='left')


# In[54]:


pd.merge(df11,df12,how='right')


# In[55]:


df11


# In[56]:


df12


# In[57]:


df11=pd.DataFrame({'key1':[7,8,9,4],'key2':[5,7,9,4],'key3':[5,7,4,3]},index=['a','b','c','d'])


# In[58]:


df12=pd.DataFrame({'key11':[14,8,9,5,80],'key4':[90,7,7,10,45],'key5':[55,6,70,47,34]},index=['a','b','h','i','j'])


# In[59]:


df11


# In[60]:


df12


# # The difference between merge and join- merge is working on columns but merge is work on index

# In[61]:


df11.join(df12)


# In[62]:


df11.join(df12,how='cross')


# In[63]:


df


# In[64]:


df['Fare_INR']=df['Fare'].apply(lambda x:x*80)


# In[65]:


df


# In[66]:


def euro_inr(x):
    return x*80
df['Fare_inr']=df['Fare'].apply(euro_inr)


# In[67]:


df


# In[68]:


df['test']=df['Parch'].apply(lambda x:x+2)


# In[69]:


df


# In[70]:


df['Name_len']=df['Name'].apply(lambda x:len(x))


# In[71]:


df


# In[73]:


def cat_fare(x):
    if x<10:
        return "cheap"
    elif x>=10 and x<20:
        return 'mid'
    else:
        return 'high'


# In[74]:


df[cat_fare]=df['Fare'].apply(cat_fare)


# In[75]:


import pandas as pd

# Convert 'Fare' column to numeric
df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')

# Define the function to categorize fares
def cat_fare(x):
    if x < 10:
        return "cheap"
    elif x >= 10 and x < 20:
        return "mid"
    else:
        return "expensive"

# Apply the categorization function to 'Fare' column and assign the result to 'new_fare' column
df['new_fare'] = df['Fare'].apply(cat_fare)


# In[76]:


df


# In[ ]:




