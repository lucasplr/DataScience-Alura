#!/usr/bin/env python
# coding: utf-8

# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize= (15,8))


# In[32]:


data = pd.read_csv('C:/Users/lucas/OneDrive/Área de Trabalho/DataScience/modulo2/extras/aluguel.csv', sep=';')


# In[33]:


data


# In[34]:


area = plt.figure()


# In[35]:


g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)


# In[36]:


g1.scatter(data.Valor, data.Area)
g1.set_title('Valor x Área')

g2.hist(data.Valor)
g2.set_title('Histograma')

dados_g3 = data.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra (valores)')

grupo = data.groupby('Tipo')['Valor']
label = grupo.mean().index
print(label)
valores = grupo.mean().values
print(valores)
g4.bar(label, valores)
g4.set_title('Media por Tipo')


# In[37]:


area


# In[38]:


area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')


# In[ ]:




