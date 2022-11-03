#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('dados.csv')


# In[3]:


data


# In[5]:


data.Renda.head()


# In[6]:


[i/10 for i in range(1,10)]


# In[7]:


data.Renda.quantile([i/10 for i in range(1,10)])


# In[8]:


import seaborn as sns


# In[10]:


ax = sns.distplot(data.Idade, 
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True},
                 bins=10)
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[ ]:


ax = sns.distplot(data.Idade, 
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True})
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[12]:


ax = sns.boxplot(x = 'Altura', data = data, orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Altura', fontsize=18)
#ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[13]:


ax = sns.boxplot(x = 'Altura', y = 'Sexo', data = data, orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Altura', fontsize=18)
#ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[19]:


ax = sns.boxplot(x = 'Renda', y = 'Sexo', data = data.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Altura', fontsize=18)
#ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[20]:


ax = sns.boxplot(x = 'Anos de Estudo', y = 'Sexo', data = data, orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Altura', fontsize=18)
#ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[ ]:




