#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('C:/Users/lucas/OneDrive/Área de Trabalho/DataScience/modulo2/data/aluguel_amostra.csv', sep=';')


# In[4]:


data


# In[7]:


metro = data['Valor m2']


# In[9]:


Q1 = metro.quantile(.25)
Q3 = metro.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


# In[10]:


selecao = (metro >= limite_inferior) & (metro <= limite_superior)


# In[11]:


Q1


# In[12]:


Q3


# In[13]:


IIQ


# In[14]:


IIQ.round(2)


# In[15]:


limite_inferior


# In[16]:


limite_inferior.round(2)


# In[17]:


limite_superior.round(2)


# In[ ]:




