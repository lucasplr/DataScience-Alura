#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('iris.csv')


# In[3]:


data.head()


# In[7]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

eixo.scatter(data.comprimento_sépala, data.largura_sépala)
eixo.set_title('Gráfico de dispersão', size=25)
eixo.set_xlabel('Comprimento da sépala', size=20)
eixo.set_ylabel('Largura da sépala', size=20)


# In[9]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

eixo.scatter(data.comprimento_sépala, data.largura_sépala)
eixo.set_title('Gráfico de dispersão', size=25)
eixo.set_xlabel('Comprimento da sépala', size=20)
eixo.set_ylabel('Largura da sépala', size=20)

eixo.tick_params(labelsize=15)


# In[18]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}

for especie in data.espécie.unique():
    tmp = data[data.espécie == especie]
    eixo.scatter(tmp.comprimento_sépala, tmp.largura_sépala, color=cores[especie])

eixo.set_title('Gráfico de dispersão', size=25)
eixo.set_xlabel('Comprimento da sépala', size=20)
eixo.set_ylabel('Largura da sépala', size=20)

eixo.tick_params(labelsize=15)
eixo.legend(cores, fontsize=20)


# In[19]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}
marcadores = {'Iris-setosa': 'x', 'Iris-versicolor': 'o', 'Iris-virginica': 'v'}


for especie in data.espécie.unique():
    tmp = data[data.espécie == especie]
    eixo.scatter(tmp.comprimento_sépala, tmp.largura_sépala, 
                 color=cores[especie], marker=marcadores[especie])

eixo.set_title('Gráfico de dispersão', size=25)
eixo.set_xlabel('Comprimento da sépala', size=20)
eixo.set_ylabel('Largura da sépala', size=20)

eixo.tick_params(labelsize=15)
eixo.legend(cores, fontsize=20)


# In[20]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}
marcadores = {'Iris-setosa': 'x', 'Iris-versicolor': 'o', 'Iris-virginica': 'v'}


for especie in data.espécie.unique():
    tmp = data[data.espécie == especie]
    eixo.scatter(tmp.comprimento_sépala, tmp.largura_sépala, 
                 color=cores[especie], marker=marcadores[especie], s=100)

eixo.set_title('Gráfico de dispersão', size=25)
eixo.set_xlabel('Comprimento da sépala', size=20)
eixo.set_ylabel('Largura da sépala', size=20)

eixo.tick_params(labelsize=15)
eixo.legend(cores, fontsize=20)


# In[24]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

eixo.boxplot(data.largura_pétala)
eixo.set_title('Boxplot de largura das pétalas', size=20)
eixo.set_xticklabels(['largura_pétala'])


# In[27]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

eixo.boxplot(data.drop('espécie', axis=1))
eixo.set_title('Boxplot de largura das pétalas', size=20)
eixo.set_xticklabels(data.drop('espécie', axis=1).columns)


# In[29]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

eixo.boxplot(data.drop('espécie', axis=1), patch_artist=True)
eixo.set_title('Boxplot de largura das pétalas', size=20)
eixo.set_xticklabels(data.drop('espécie', axis=1).columns)


# In[31]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

colors=['red', 'blue', 'orange', 'green']

boxes = eixo.boxplot(data.drop('espécie', axis=1), patch_artist=True)
eixo.set_title('Boxplot de largura das pétalas', size=20)
eixo.set_xticklabels(data.drop('espécie', axis=1).columns)

for box, color in zip(boxes['boxes'], colors):
    box.set(color=color)


# In[33]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])

colors=['red', 'blue', 'orange', 'green']

boxes = eixo.boxplot(data.drop('espécie', axis=1), patch_artist=True)
eixo.set_title('Boxplot de largura das pétalas', size=20)
eixo.set_xticklabels(data.drop('espécie', axis=1).columns)

for box, color in zip(boxes['boxes'], colors):
    box.set(color=color)
    
for outlier in boxes['fliers']:
    outlier.set(marker='x', markersize=8)


# In[40]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

eixo.hist(data.comprimento_pétala, bins=20, density=True)
eixo.set_title('Histograma', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)


# In[45]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

mu, sigma = data.comprimento_pétala.mean(), data.comprimento_pétala.std()

eixo.hist(data.comprimento_pétala, bins=20)
eixo.set_title('Histograma', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)

eixo.annotate(f'$mu = {mu:.2f}$\n$sigma = {sigma:.2f}$',
             xy=(4.5,20), size=20)


# In[59]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

mu, sigma = data.comprimento_pétala.mean(), data.comprimento_pétala.std()

eixo.hist(data.comprimento_pétala, bins=20)
eixo.set_title('Histograma', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)

eixo.annotate(f'$\mu = {mu:.2f}$\n$\sigma = {sigma:.2f}$',
             xy=(4.5,20), size=20)

eixo.axvline(mu, color='k', linestyle='--')
eixo.annotate('Média', xy=(mu-.4, 28), size=15)

eixo.axvline(data.comprimento_pétala.median(), color='g', linestyle='--')
eixo.annotate('Mediana', xy=(data.comprimento_pétala.median()+.2, 28), size=15)


# In[60]:


data.espécie.unique()


# In[77]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

data_iv = data[data['espécie'] == 'Iris-versicolor']

mu, sigma = data_iv.comprimento_pétala.mean(), data.comprimento_pétala.std()

eixo.hist(data_iv.comprimento_pétala, bins=20)
eixo.set_title('Iris Versicolor', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)

eixo.annotate(f'$\mu = {mu:.2f}$\n$\sigma = {sigma:.2f}$',
             xy=(4.6,6), size=20)

eixo.axvline(mu, color='k', linestyle='--')
eixo.annotate('Média', xy=(mu-.15, 5.5), size=15)

eixo.axvline(data_iv.comprimento_pétala.median(), color='g', linestyle='--')
eixo.annotate('Mediana', xy=(data_iv.comprimento_pétala.median()+.01, 7), size=15)

fig.savefig('Histograma_iv.png', bbox_inches='tight')


# In[107]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

data_is = data[data['espécie'] == 'Iris-setosa']

mu, sigma = data_is.comprimento_pétala.mean(), data.comprimento_pétala.std()

eixo.hist(data_is.comprimento_pétala, bins=20)
eixo.set_title('Iris Setosa', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)

eixo.annotate(f'$\mu = {mu:.2f}$\n$\sigma = {sigma:.2f}$',
             xy=(4.6,6), size=20)

eixo.axvline(mu, color='k', linestyle='--')
eixo.annotate('Média', xy=(mu-.05, 11.5), size=15)

eixo.axvline(data_is.comprimento_pétala.median(), color='g', linestyle='--')
eixo.annotate('Mediana', xy=(data_is.comprimento_pétala.median()+.01, 14.2), size=15)

fig.savefig('Histograma_is.png', bbox_inches='tight')


# In[108]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

data_ivg = data[data['espécie'] == 'Iris-virginica']

mu, sigma = data_ivg.comprimento_pétala.mean(), data.comprimento_pétala.std()

eixo.hist(data_ivg.comprimento_pétala, bins=20)
eixo.set_title('Iris Virginica', size=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', size=15)
eixo.grid(True)

eixo.annotate(f'$\mu = {mu:.2f}$\n$\sigma = {sigma:.2f}$',
             xy=(4.6,6), size=20)

eixo.axvline(mu, color='k', linestyle='--')
eixo.annotate('Média', xy=(mu-.15, 8), size=15)

eixo.axvline(data_ivg.comprimento_pétala.median(), color='g', linestyle='--')
eixo.annotate('Mediana', xy=(data_ivg.comprimento_pétala.median()+.05, 7.2), size=15)

fig.savefig('Histograma_ivg.png', bbox_inches='tight')


# In[109]:


from PIL import Image

largura, altura = Image.open('Histograma_ivg.png').size
combinada = Image.new('RGB',(3*largura, altura))
intervalo = 0

for image in map(Image.open, ['Histograma_iv.png', 'Histograma_is.png', 'Histograma_ivg.png']):
    combinada.paste(image, (intervalo, 0))
    intervalo += largura
    
combinada.save('combinada.png')


# In[110]:


combinada


# In[ ]:




