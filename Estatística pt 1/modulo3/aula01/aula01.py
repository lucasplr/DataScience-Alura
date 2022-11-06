#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('dados.csv')


# In[3]:


data


# In[4]:


sexo = {0: 'Masculino',
        1: 'Feminino'}
cor = {0: 'Indígena',
       2: 'Branca',
       4: 'Preta',
       6: 'Amarela',
       8: 'Parda',
       9: 'Sem declaração'}


# In[12]:


frequencia = pd.crosstab(data.Sexo,
                        data.Cor)
frequencia.rename(index = sexo, inplace=True)
frequencia.rename(columns = cor, inplace=True)
frequencia


# In[17]:


percentual = pd.crosstab(data.Sexo,
                        data.Cor,
                        aggfunc = 'mean',
                        values = data.Renda) 
percentual.rename(index = sexo, inplace=True)
percentual.rename(columns = cor, inplace=True)
percentual


# In[ ]:




