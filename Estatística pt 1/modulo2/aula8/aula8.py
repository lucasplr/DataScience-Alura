#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[12]:


data = pd.read_csv('/Users/lucas/OneDrive/Área de Trabalho/DataScience/modulo2/data/aluguel_residencial.csv', sep=';')


# In[13]:


data


# In[14]:


bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']

selecao = data.Bairro.isin(bairros)

selecao


# In[15]:


data = data[selecao]
data


# In[16]:


grupo_bairro = data.groupby('Bairro')


# In[17]:


for bairro, data in grupo_bairro:
    print(f'{bairro} -> {data.Valor.mean()}')


# In[18]:


grupo_bairro.Valor.mean()


# In[19]:


grupo_bairro.Valor.describe().round(2)


# In[20]:


grupo_bairro.Valor.aggregate(['min', 'max', 'sum']).rename(columns = {"min": "Mínimo", "max": "Máximo", "sum": "Soma"})


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))


# In[33]:


fig = grupo_bairro.Valor.mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor do Aluguel por Bairro', {'fontsize': 22})


# In[ ]:




