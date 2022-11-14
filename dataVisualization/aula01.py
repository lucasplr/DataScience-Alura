#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


data = pd.read_csv('Curso/monitoramento_tempo.csv')


# In[10]:


data.info()


# In[11]:


data.data = pd.to_datetime(data.data)


# In[12]:


data.info()


# In[14]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


data.head()


# In[29]:


plt.figure(figsize=(15,8))
plt.title('Gráfixo de Temperatura x Tempo', size=(18))
plt.ylabel('Temperatura', size=(14))
plt.xlabel('Tempo', size=(14))
plt.plot(data.data, data.temperatura)


# In[32]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura)

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(18))


# In[37]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura)

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))


# In[39]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura)

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[42]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='dimgrey')

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[44]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='g', lw=.4)

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[46]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='g', ls='dotted')

eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[50]:


import datetime


# In[51]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='g', ls='dotted')

eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[52]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='g', ls='dotted', marker='o')

eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)


# In[53]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(data.data, data.temperatura, color='g', ls='dotted', marker='o')

eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Gráfico da variação de Temperatura no momento', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))

eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.grid(True)


# In[68]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.1,0.5,0.4,0.4])

eixo.plot(data.data, data.temperatura, color='g')
eixo.grid(True)
eixo.set_title('Variação da temperatura x tempo', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))
eixo.legend(['Temperatura'], loc='best', fontsize=15)

eixo2.plot(data.data, data.temperatura, color='darkgray')
eixo2.grid(True)
eixo2.set_title('Variação da temperatura x tempo', size=(10))
eixo2.set_xlabel('Tempo', size=(8))
eixo2.set_ylabel('Temperatura', size=(8))
eixo2.legend(['Temperatura'], loc='best', fontsize=7)


# In[75]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.plot(data.data, data.temperatura, color='g')
eixo.grid(True)
eixo.set_title('Variação da temperatura x tempo em 2014', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)

eixo2.plot(data.data, data.temperatura, color='darkgray')
eixo2.grid(True)
eixo2.set_title('Variação da temperatura x tempo', size=(10))
eixo2.set_xlabel('Tempo', size=(8))
eixo2.set_ylabel('Temperatura', size=(8))

eixo2.legend(['Temperatura'], loc='best', fontsize=7)


# In[76]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.plot(data.data, data.temperatura, color='g')
eixo.grid(True)
eixo.set_title('Variação da temperatura x tempo em 2014', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))
eixo.set_xlim(datetime.datetime(2014,5,1),datetime.datetime(2014,6,1))
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)

eixo2.plot(data.data, data.temperatura, color='darkgray')
eixo2.grid(True)
eixo2.set_title('Variação da temperatura x tempo', size=(10))
eixo2.set_xlabel('Tempo', size=(8))
eixo2.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo2.set_ylabel('Temperatura', size=(8))

eixo2.legend(['Temperatura'], loc='best', fontsize=7)


# In[77]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.plot(data.data, data.temperatura, color='g')
eixo.grid(True)
eixo.set_title('Variação da temperatura x tempo em 2014', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))
eixo.set_xlim(datetime.datetime(2014,5,1),datetime.datetime(2014,6,1))
eixo.set_ylim(270, 320)
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)

eixo2.plot(data.data, data.temperatura, color='darkgray')
eixo2.grid(True)
eixo2.set_title('Variação da temperatura x tempo', size=(10))
eixo2.set_xlabel('Tempo', size=(8))
eixo2.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo2.set_ylabel('Temperatura', size=(8))

eixo2.legend(['Temperatura'], loc='best', fontsize=7)


# In[90]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.plot(data.data, data.temperatura, color='g')
eixo.grid(True)
eixo.set_title('Variação da temperatura x tempo em 2014', size=(20))
eixo.set_xlabel('Tempo', size=(16))
eixo.set_ylabel('Temperatura', size=(16))
eixo.set_xlim(datetime.datetime(2014,5,1),datetime.datetime(2014,6,1))
eixo.set_ylim(270, 320)
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)

azul_esquerda = data.data < datetime.datetime(2014,5,1)
azul_direita = data.data > datetime.datetime(2014,6,1)

eixo2.plot(data.data, data.temperatura, color='g')
eixo2.plot(data[azul_esquerda]['data'], data[azul_esquerda]['temperatura'], color='b')
eixo2.plot(data[azul_direita]['data'], data[azul_direita]['temperatura'], color='b')
eixo2.grid(True)
eixo2.set_title('Variação da temperatura x tempo', size=(10))
eixo2.set_xlabel('Tempo', size=(8))
eixo2.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo2.set_ylabel('Temperatura', size=(8))

eixo2.legend(['Temperatura'], loc='best', fontsize=7)


# In[100]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

eixo.plot(data.data, data.temperatura, color='g')
eixo.set_title('Temperatura na variação dos anos', size=25, pad=20)
eixo.set_xlabel('Tempo', size=18)
eixo.set_ylabel('Temperatura', size=18)
eixo.legend(['Temperatura'], loc='best', fontsize=15)
eixo.grid(True)

eixo.axhline(max(data.temperatura), color='k', linestyle='--')
eixo.axhline(min(data.temperatura), color='k', linestyle='--')


# In[107]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

eixo.plot(data.data, data.temperatura, color='g')
eixo.set_title('Temperatura na variação dos anos', size=25, pad=20)
eixo.set_xlabel('Tempo', size=18)
eixo.set_ylabel('Temperatura', size=18)
eixo.legend(['Temperatura'], loc='best', fontsize=15)
eixo.grid(True)

x1 = data.data[data.temperatura.idxmax()]
y1 = max(data.temperatura)

x2 = data.data[data.temperatura.idxmin()]
y2 = min(data.temperatura)

eixo.annotate('Máximo', xy=(x1,y1), fontsize=20)
eixo.annotate('Mínimo', xy=(x2,y2), fontsize=20)

eixo.axhline(max(data.temperatura), color='k', linestyle='--')
eixo.axhline(min(data.temperatura), color='k', linestyle='--')


# In[123]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

eixo.plot(data.data, data.temperatura, color='g')
eixo.set_title('Temperatura na variação dos anos', size=25, pad=20)
eixo.set_xlabel('Tempo', size=18)
eixo.set_ylabel('Temperatura', size=18)
eixo.legend(['Temperatura'], loc='best', fontsize=15)
eixo.grid(True)

x1 = data.data[data.temperatura.idxmax()]
y1 = max(data.temperatura)

x2 = data.data[data.temperatura.idxmax() - 7000]
y2 = max(data.temperatura - 5)

x3 = data.data[data.temperatura.idxmin()]
y3 = min(data.temperatura)

x4 = data.data[data.temperatura.idxmin() - 7000]
y4 = min(data.temperatura + 2)

eixo.annotate('Máximo', xy=(x1,y1), fontsize=20,
             xytext=(x2,y2), arrowprops=dict(facecolor='k'))
eixo.annotate('Mínimo', xy=(x3,y3), fontsize=20,
             xytext=(x4,y4), arrowprops=dict(facecolor='k'))

eixo.axhline(max(data.temperatura), color='k', linestyle='--')
eixo.axhline(min(data.temperatura), color='k', linestyle='--')


# In[ ]:




