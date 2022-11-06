#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[4]:


import pandas as pd


# In[8]:


data = pd.read_csv('C:/Users/lucas/OneDrive/Área de Trabalho/DataScience/modulo2/data/aluguel_residencial.csv', sep=';')


# In[9]:


data


# In[15]:


data.boxplot('Valor')


# In[20]:


data[data.Valor >= 500000]


# In[23]:


valor = data.Valor


# ![compressed_box-plot.png](attachment:compressed_box-plot.png)

# In[37]:


Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


# In[42]:


selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = data[selecao]


# In[55]:


selecao_alto = (data.Valor >= 15000)
selecao_normal = (data.Valor <= 15000)


# In[56]:


data_alto = data[selecao_alto]
data_normal = data[selecao_normal]


# In[57]:


data_alto


# In[58]:


data_normal


# In[59]:


data_alto.hist(['Valor'])


# In[60]:


data_normal.hist(['Valor'])


# In[40]:


dados_new.boxplot(['Valor'])


# In[41]:


dados_new.hist(['Valor'])
data.hist(['Valor'])


# In[ ]:




