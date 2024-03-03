#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


# Create a DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value1': [1, 2, 3, 4, 5, 6],
    'Value2': [10, 20, 30, 40, 50, 60],
    'Value3': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)


# In[6]:


df


# In[7]:


# Group by 'Category' column
grouped = df.groupby('Category')

# Apply different aggregate functions to different columns
result = grouped.agg({'Value1': 'sum', 'Value2': 'mean','Value3': 'median'}).reset_index()

# Display the result DataFrame
print(result)


# In[ ]:




