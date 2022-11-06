#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'


# In[5]:


eventos = {'m1': list(m1),
           'm2': list(m2),
           'm3': list(m3),
           'm4': list(m4),
           'm5': list(m5)}
moedas = pd.DataFrame(eventos)

moedas


# In[6]:


df = pd.DataFrame(data = ['Cara', 'Coroa'],
                             index = ['c', 'C'],
                             columns = ['Faces'])
df


# In[7]:


for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()],
                  axis=1) #value counts é aplicavel somente a séries, desta forma é somado para cada série individualmente
df


# In[9]:


#for item in moedas:
 #   df = pd.concat([df, moedas[item].sum()],
 #                 axis=1)
#df #não é possivel pois não se pode concatenar str em soma


# In[ ]:


for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()],
                  axis=1)
df

