#!/usr/bin/env python
# coding: utf-8

# # zamato-eda
# 
# Use the "Run" button to execute the code.

# In[ ]:


print('Hello World')


# # zamato dataset exploratory dataanalysis 

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df.describe()


# 1. missing values
# 2.explore about numerical variables
# 3.explore categorical variables
# 4.finding relationship between features

# In[11]:


df.isnull().sum()


# In[13]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[15]:


import seaborn as sns


# In[17]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[21]:


pip install openpyxl


# In[22]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[23]:


df.columns


# In[25]:


final_df=pd.merge(df,df_country,on='Country Code',how='left')


# In[26]:


final_df.head(2)


# In[27]:


final_df.dtypes


# In[28]:


final_df.columns


# In[29]:


final_df.Country.value_counts()


# In[30]:


country_names=final_df.Country.value_counts().index


# In[33]:


country_val=final_df.Country.value_counts().values


# # top 3 countries that uses zomato

# In[36]:


plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# In[37]:


#observation:zomato maximum recordsare from india 


# In[38]:


final_df.columns


# In[43]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[44]:


ratings


# In[46]:


#observation: 
#1. when rating between 4.5 to 4.9 -excellent
#2. when rating between 4.0 to 3.4 - very good
#3. when rating between 3.5 to 3.9 - good
#4. when rating between 3.0 to 3.4 - average
#5. when rating between 2.5 to 2.9- aveerage
#6. when rating between 2.0 to 2.4 - poor


# In[49]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating',y='Rating Count',data=ratings)


# In[52]:


sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color',data=ratings,palette=['black','red','orange','yellow','green','green'])


# observation 
# 1. not rated count is very high
# 2. maximum number ofrating are between 2.5 to 3.4

# In[55]:


sns.countplot(x='Rating color',data=ratings,palette=['black','red','orange','yellow','green','green'])


# # find countries name that as given 0 rating

# In[56]:


final_df.columns


# In[59]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# maximum number of 0 ratings are from indian customers

# # find out which currency is used by which country

# In[62]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# # which country has online delivery option

# In[65]:


final_df[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index()


# In[66]:


final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()


# observation:
# 1. online deliveries available in india andd UAE

# In[ ]:




