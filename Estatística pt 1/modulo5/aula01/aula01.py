#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'Matérias': ['Matemática', 'Português', 'Inglês', 'Geografia', 'História', 'Física', 'Química'],
                   'Beltrano': [10.0, 2.0, 0.5, 1.0, 3.0, 9.5, 10.0],
                   'Fulano': [8, 10, 4, 8, 6, 10, 8],
                   'Sicrano': [7.5, 8.0, 7.0, 8.0, 8.0, 8.5, 7.0]}).set_index('Matérias')
df


# In[4]:


notas_fulano = df[['Fulano']]
notas_fulano


# In[5]:


nota_media_fulano = notas_fulano.mean()[0]
nota_media_fulano


# In[6]:


notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano


# In[7]:


notas_fulano


# In[8]:


notas_fulano['Desvio'].sum()


# In[9]:


notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()


# In[10]:


notas_fulano


# In[11]:


notas_fulano['|Desvio|'].mean()


# In[12]:


desvio_medio_absoluto = notas_fulano['Fulano'].mad()
desvio_medio_absoluto


# In[16]:


notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)
notas_fulano


# In[17]:


notas_fulano['(Desvio)^2'].sum() / (len(notas_fulano) - 1)


# In[19]:


notas_fulano['(Desvio)^2'].sum() / (notas_fulano.shape[0] - 1)


# In[20]:


variancia = notas_fulano['Fulano'].var()


# In[21]:


variancia


# In[23]:


import numpy as np


# In[24]:


np.sqrt(variancia)


# In[26]:


desvio_padrão = notas_fulano['Fulano'].std()
desvio_padrão


# In[ ]:




