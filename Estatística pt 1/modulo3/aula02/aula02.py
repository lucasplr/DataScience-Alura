#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd


# In[39]:


data = pd.read_csv('dados.csv')


# In[40]:


data


# In[41]:


data.Renda


# In[42]:


Salarios = pd.DataFrame(data.Renda)


# In[43]:


variação = pd.DataFrame({min: Salarios.min(), max: Salarios.max()})


# In[44]:


variação


# In[53]:


classes = [0, 1576, 3152, 7880, 15760, 200000]


# In[54]:


label = ['E', 'D', 'C', 'B', 'A']


# In[55]:


pd.cut(x = data.Renda,
       bins = classes,
      labels = label,
       include_lowest = True)


# In[56]:


#classes = pd.DataFrame(classes, label)
#classes.columns = ['Renda']
#classes.columns.name = 'Classe'
#classes


# In[58]:


frequencia = pd.value_counts(pd.cut(x = data.Renda,
       bins = classes,
      labels = label,
       include_lowest = True))
frequencia


# In[60]:


percentual = pd.value_counts(pd.cut(x = data.Renda,
       bins = classes,
      labels = label,
       include_lowest = True),
        normalize = True) * 100
percentual


# In[62]:


dist_freq_quantitativas_personalizadas = pd.DataFrame({"Frequência": frequencia, "Porcentagem %": percentual})
dist_freq_quantitativas_personalizadas


# In[64]:


dist_freq_quantitativas_personalizadas.sort_index(ascending= False)


# In[66]:


classes = [data.Altura.min(), 1.65, 1.75, data.Altura.max()]
labels = ['1 - Baixa', '2 - Média', '3 - Alta']

frequencia = pd.value_counts(
    pd.cut(
        x = data.Altura,
        bins = classes,
        labels = labels,
        include_lowest = True
    )
)

percentual = pd.value_counts(
    pd.cut(
        x = data.Altura,
        bins = classes,
        labels = labels,
        include_lowest = True
    ), normalize = True
) * 100

dist_freq_altura = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)

dist_freq_altura.rename_axis('Estaturas', axis= 'columns', inplace = True)

dist_freq_altura.sort_index(ascending = True, inplace = True)

dist_freq_altura


# In[67]:


import numpy as np


# In[68]:


n = data.shape[0]


# In[69]:


n


# In[70]:


k = 1 + (10/3) * np.log10(n)


# In[71]:


k


# In[72]:


k = int(k.round(0))


# In[73]:


k


# In[84]:


frequencia = pd.value_counts(pd.cut
        (x = data.Renda,
       bins = k,
       include_lowest = True
        ),
        sort = False)


# In[85]:


frequencia


# In[90]:


percentual = pd.value_counts(pd.cut
        (x = data.Renda,
       bins = k,
       include_lowest = True
        ),
        sort = False,
        normalize = True) * 100


# In[91]:


percentual


# In[92]:


dist_freq_quantitativa_amplitude_fixa = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativa_amplitude_fixa


# In[99]:


import seaborn as sns

ax = sns.distplot(data.Altura, kde = False)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de Frequências - KDE', fontsize=18)
ax.set_xlabel('Altura (metros)', fontsize=14)
ax


# In[100]:


ax = sns.distplot(data.Altura)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de Frequências', fontsize=18)
ax.set_xlabel('Metros)', fontsize=14)
ax


# In[101]:


dist_freq_quantitativas_personalizadas


# In[111]:


dist_freq_quantitativas_personalizadas['Frequência'].plot.bar(width = 1, color = 'blue', alpha=0.45, figsize=(12,6))


# In[ ]:




