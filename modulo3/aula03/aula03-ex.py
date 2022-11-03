#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
                 index = ['Matemática',
                          'Português',
                          'Inglês',
                          'Geografia',
                          'História',
                          'Física',
                          'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
df


# In[13]:


df['Fulano'].mean()


# In[14]:


df['Fulano'].median()


# In[39]:


notas_fulano = df.Fulano
#notas_fulano.columns = ['Materias', 'Notas']
notas_fulano


# In[40]:


notas_fulano = notas_fulano.sort_values()


# In[41]:


notas_fulano


# In[42]:


notas_fulano = notas_fulano.reset_index()


# In[43]:


notas_fulano


# In[44]:


n = notas_fulano.shape[0]
n


# In[45]:


elemento_md = (n + 1)/ 2


# In[46]:


elemento_md


# In[47]:


notas_fulano.loc[elemento_md]


# In[48]:


notas_fulano.median()


# In[49]:


notas_beltrano = df.Beltrano.sample(6, random_state = 101)


# In[50]:


notas_beltrano


# In[51]:


notas_beltrano.median()


# In[52]:


n = notas_beltrano.shape[0]
n


# In[57]:


element_md = (n)/2
element_md


# In[60]:


df.mode()


# In[61]:





# In[ ]:





# In[ ]:




