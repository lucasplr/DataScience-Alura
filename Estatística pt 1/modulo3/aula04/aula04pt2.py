#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[27]:


df = pd.DataFrame({'Matérias': ['Matemática', 'Português', 'Inglês', 'Geografia', 'História', 'Física', 'Química'],
                   'Beltrano': [10.0, 2.0, 0.5, 1.0, 3.0, 9.5, 10.0],
                   'Fulano': [8, 10, 4, 8, 6, 10, 8],
                   'Sicrano': [7.5, 8.0, 7.0, 8.0, 8.0, 8.5, 7.0]}).set_index('Matérias')
df


# In[33]:


notas_fulano = df[['Fulano']]
notas_fulano


# In[35]:


nota_media_fulano = notas_fulano.mean()[0]
nota_media_fulano


# In[37]:


notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano


# In[38]:


notas_fulano


# In[39]:


notas_fulano['Desvio'].sum()


# In[40]:


notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()


# In[42]:


notas_fulano


# In[44]:


notas_fulano['|Desvio|'].mean()


# In[46]:


desvio_medio_absoluto = notas_fulano['Fulano'].mad()
desvio_medio_absoluto


# In[ ]:




