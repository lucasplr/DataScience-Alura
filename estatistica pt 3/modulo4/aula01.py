#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: green; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear</h1>

# # <font color='red' style='font-size: 30px;'>Conhecendo o Dataset</font>
# <hr style='border: 2px solid red;'>

# ## Importando bibliotecas
# 
# https://matplotlib.org/
# 
# https://pandas.pydata.org/
# 
# http://www.numpy.org/

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# ## Bibliotecas opcionais
# 
# https://docs.python.org/3/library/warnings.html

# In[2]:


import warnings 
warnings.filterwarnings('ignore')


# ## O Dataset e o Projeto
# <hr>
# 
# ### Fonte: https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo
# 
# ### Descrição:
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>A cerveja é uma das bebidas mais democráticas e consumidas no mundo. Não sem razão, é perfeito para quase todas as situações, desde o happy hour até grandes festas de casamento.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O objetivo deste treinamento será estimar um modelo de <b>Machine Learning</b> utilizando a técnica de <b>Regressão Linear</b> para demonstrar os impactos das variáveis disponibilizadas neste dataset sobre o consumo de cerveja (Y). No final do projeto teremos um modelo de previsão para o consumo médio de cerveja segundo os inputs de um conjunto de variáveis (X's).</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Os dados (amostra) foram coletados em São Paulo - Brasil, em uma área universitária, onde existem algumas festas com grupos de alunos de 18 a 28 anos de idade (média).</p>
# 
# ### Dados:
# <ul style='font-size: 18px; line-height: 2; text-align: justify;'>
#     <li><b>data</b> - Data</li>
#     <li><b>temp_media</b> - Temperatura Média (°C)</li>
#     <li><b>temp_min</b> - Temperatura Mínima (°C)</li>
#     <li><b>temp_max</b> - Temperatura Máxima (°C)</li>
#     <li><b>chuva</b> - Precipitação (mm)</li>
#     <li><b>fds</b> - Final de Semana (1 = Sim; 0 = Não)</li>
#     <li><b>consumo</b> - Consumo de Cerveja (litros)</li>
# </ul>

# ## Leitura dos dados

# In[3]:


data = pd.read_csv('Consumo_cerveja.csv', sep=';')


# ## Visualizar os dados

# In[4]:


data


# ## Verificando o tamanho do dataset

# In[5]:


len(data)


# # <font color='red' style='font-size: 30px;'>Análises Preliminares</font>
# <hr style='border: 2px solid red;'>

# ## Estatísticas descritivas

# In[6]:


data.describe().round(2)


# ## Matriz de correlação
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>coeficiente de correlação</b> é uma medida de associação linear entre duas variáveis e situa-se entre <b>-1</b> e <b>+1</b> sendo que <b>-1</b> indica associação negativa perfeita e <b>+1</b> indica associação positiva perfeita.</p>

# In[7]:


data.corr().round(2)


# # <font color='red' style='font-size: 30px;'>Comportamento da Variável Dependente (Y)</font>
# <hr style='border: 2px solid red;'>

# # Análises gráficas

# ## Plotando a variável *dependente* (y)
# https://pandas.pydata.org/pandas-docs/stable/visualization.html

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Box Plot</font>
# <hr style='border: 2px solid red;'>

# <img width='700px' src='../Dados/img/Box-Plot.png'>

# ## Importando biblioteca seaborn
# https://seaborn.pydata.org/
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O Seaborn é uma biblioteca Python de visualização de dados baseada no matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos.</p>

# In[8]:


import seaborn as sns


# ## Box plot da variável *dependente* (y)

# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot

# In[9]:


data


# # <font color='red' style='font-size: 30px;'>Box Plot com Duas Variáveis</font>
# <hr style='border: 2px solid red;'>

# ## Investigando a variável *dependente* (y) segundo determinada característica

# In[ ]:





# ## Configurações de estilo e cor da biblioteca *seaborn*
# 
# ### Controle de estilo
# 
# > ####  API
# > https://seaborn.pydata.org/api.html#style-api
# 
# > #### Tutorial
# > https://seaborn.pydata.org/tutorial/aesthetics.html#aesthetics-tutorial
# 
# ### Paleta de cores
# 
# > #### API
# > https://seaborn.pydata.org/api.html#palette-api
# 
# > #### Tutorial
# > https://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial

# In[ ]:





# In[ ]:





# # <font color='red' style='font-size: 30px;'>Distribuição de Frequências</font>
# <hr style='border: 2px solid red;'>

# ## Distribuição de frequências da variável *dependente* (y)

# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=distplot#seaborn.distplot

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (pairplot)</font>
# <hr style='border: 2px solid red;'>

# ## Gráficos de dispersão entre as variáveis do dataset

# ## seaborn.pairplot
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota o relacionamento entre pares de variáveis em um dataset.</p>

# In[10]:


ax = sns.pairplot(data)
ax


# ## Plotando o pairplot fixando somente uma variável no eixo y

# In[11]:


ax = sns.pairplot(data, y_vars='consumo', x_vars=['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'])
ax.fig.suptitle('Dispersão entre variáveis', fontsize=20, y=1.1)
ax


# In[12]:


ax = sns.pairplot(data, y_vars='consumo', x_vars=['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'], kind='reg')
ax.fig.suptitle('Dispersão entre variáveis', fontsize=20, y=1.1)
ax


# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (jointplot)</font>
# <hr style='border: 2px solid red;'>

# ## seaborn.jointplot
# 
# https://seaborn.pydata.org/generated/seaborn.jointplot.html?highlight=jointplot#seaborn.jointplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota o relacionamento entre duas variáveis e suas respectivas distribuições de frequência.</p>

# In[13]:


ax = sns.jointplot(x='temp_max', y='consumo', data=data)
ax.fig.suptitle('Dispersão entre variáveis', fontsize=20, y=1.1)
ax


# ## Plotando um jointplot com a reta de regressão estimada

# In[14]:


ax = sns.jointplot(x='temp_max', y='consumo', data=data, kind='reg')
ax.fig.suptitle('Dispersão entre variáveis', fontsize=20, y=1.1)
ax
ax.fig.suptitle('Dispersão entre variáveis', fontsize=20, y=1.1)
ax


# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (lmplot)</font>
# <hr style='border: 2px solid red;'>

# ## seaborn.lmplot
# 
# https://seaborn.pydata.org/generated/seaborn.lmplot.html?highlight=lmplot#seaborn.lmplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota a reta de regressão entre duas variáveis juntamente com a dispersão entre elas.</p>

# In[ ]:





# ## Plotando um lmplot utilizando uma terceira variável na análise (tipo I)

# In[ ]:





# ## Plotando um lmplot utilizando uma terceira variável na análise (tipo II)

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Estimando um Modelo de Regressão Linear para o Consumo</font>
# <hr style='border: 2px solid red;'>

# # Regresão Linear
# <hr>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>A análise de regressão diz respeito ao estudo da dependência de uma variável (a variável <b>dependente</b>) em relação a uma ou mais variáveis, as variáveis explanatórias, visando estimar e/ou prever o valor médio da primeira em termos dos valores conhecidos ou fixados das segundas.</p>
# 
# 
# ## scikit-learn (https://scikit-learn.org/stable/)
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O *scikit-learn* é um módulo Python especializado em soluções para *machine learning*.</p>
# 
# 

# ## Importando o *train_test_split* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# In[15]:


from sklearn.model_selection import train_test_split


# ## Criando uma Series (pandas) para armazenar o Consumo de Cerveja (y)

# In[16]:


y = data.consumo


# ## Criando um DataFrame (pandas) para armazenar as variáveis explicativas (X)

# In[17]:


X = data[['temp_max', 'fds', 'chuva']]


# ## Criando os datasets de treino e de teste

# In[30]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811)


# ## Verificando os tamanhos dos arquivos gerados pela função *train_test_split*

# In[31]:


X_train.shape


# In[32]:


X_test.shape


# In[33]:


y_train.shape


# In[34]:


y_test.shape


# In[ ]:





# <img width='600px' src='../Dados/img/reg_01.jpg'>

# ## Importando *LinearRegression* e *metrics* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# https://scikit-learn.org/stable/modules/classes.html#regression-metrics

# In[26]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# ## Instanciando a classe *LinearRegression()*

# In[27]:


model = LinearRegression()


# ## Utilizando o método *fit()* do objeto "modelo" para estimar nosso modelo linear utilizando os dados de TREINO (y_train e X_train)
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit

# In[35]:


model.fit(X_train, y_train)


# ## Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score
# 
# ### Coeficiente de Determinação - R²
# 
# O coeficiente de determinação (R²) é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entra 0 e 1.
# 
# $$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$

# In[36]:


print(f'R² = {model.score(X_train, y_train).round(2)}')


# ## Gerando previsões para os dados de TESTE (X_test) utilizando o método *predict()* do objeto "modelo"
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict

# In[37]:


y_previsto = model.predict(X_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões do nosso modelo
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

# In[39]:


print('R² = %s' % metrics.r2_score(y_test, y_previsto).round(2))


# # <font color='red' style='font-size: 30px;'>Obtendo Previsões Pontuais</font>
# <hr style='border: 2px solid red;'>

# ## Dados de entrada

# In[ ]:





# ## Gerando previsão pontual

# In[ ]:





# ## Criando um simulador simples

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Interpretação dos Coeficientes Estimados</font>
# <hr style='border: 2px solid red;'>

# <img width='600px' src='../Dados/img/reg_02.jpg'>

# ## Obtendo o intercepto do modelo
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>intercepto</b> representa o efeito médio em $Y$ (Consumo de Cerveja) tendo todas as variáveis explicativas excluídas do modelo. De forma mais simples, o <b>intercepto</b> representa o efeito médio em $Y$ (Consumo de Cerveja) quando $X_2$ (Temperatura Máxima), $X_3$ (Chuva) e $X_4$ (Final de Semana) são iguais a zero.</p>

# In[ ]:





# In[ ]:





# ## Obtendo os coeficientes de regressão
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>Os <b>coeficientes de regressão</b> $\beta_2$, $\beta_3$ e $\beta_4$ são conhecidos como <b>coeficientes parciais de regressão</b> ou <b>coeficientes parciais angulares</b>. Considerando o número de variáveis explicativas de nosso modelo, seu significado seria o seguinte: $\beta_2$ mede a variação no valor médio de $Y$ (Consumo de Cerveja), por unidade de variação em $X_2$ (Temperatura Máxima), mantendo-se os valores de $X_3$ (Chuva) e $X_4$ (Final de Semana) constantes. Em outras palavras, ele nos dá o efeito "direto" ou "líquido" de uma unidade de variação em $X_2$ sobre o valor médio de $Y$, excluídos os efeitos que $X_3$ e $X_4$ possam ter sobre a média de $Y$. De modo análogo podemos interpretar os demais coeficientes de regressão.</p>

# In[ ]:





# In[ ]:





# ## Confirmando a ordem das variáveis explicativas no DataFrame

# In[ ]:





# ## Criando uma lista com os nomes das variáveis do modelo

# In[ ]:





# ## Criando um DataFrame para armazenar os coeficientes do modelo
# 
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html?#numpy.append

# In[ ]:





# ## Interpretação dos Coeficientes Estimados
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Intercepto</b> → Excluindo o efeito das variáveis explicativas ($X_2=X_3=X_4=0$) o efeito médio no Consumo de Cerveja seria de <b>5951,98 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Temperatura Máxima (°C)</b> → Mantendo-se os valores de $X_3$ (Chuva) e $X_4$ (Final de Semana) constantes, o acréscimo de 1°C na Temperatura Máxima gera uma variação média no Consumo de Cerveja de <b>684,74 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Chuva (mm)</b> → Mantendo-se os valores de $X_2$ (Temperatura Máxima) e $X_4$ (Final de Semana) constantes, o acréscimo de 1mm de Chuva gera uma variação média no Consumo de Cerveja de <b>-60,78 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Final de Semana (Sim/Não)</b> → Mantendo-se os valores de $X_2$ (Temperatura Máxima) e $X_3$ (Chuva) constantes, o fato de o dia ser classificado como Final de Semana gera uma variação média no Consumo de Cerveja de <b>5401,08 litros</b>.
# </p>

# # <font color='red' style='font-size: 30px;'>Análises Gráficas das Previsões do Modelo</font>
# <hr style='border: 2px solid red;'>

# ## Gerando as previsões do modelo para os dados de TREINO

# In[ ]:





# ## Gráfico de dispersão entre valor estimado e valor real
# 
# https://seaborn.pydata.org/generated/seaborn.scatterplot.html

# In[ ]:





# ## Obtendo os resíduos

# In[ ]:





# ## Gráfico de dispersão entre valor estimado e resíduos
# 
# Método informal de verificação da hipótese de variância constante dos resíduos (homocedasticidade)

# In[ ]:





# ## Utilizando os resíduos ao quadrado

# <img width='800px' src='../Dados/img/var_u.jpg'>
# Fonte: Econometria Básica - 5ª edição - Gujarati e Porter

# In[ ]:





# ## Plotando a distribuição de frequências dos resíduos

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Comparando Modelos</font>
# <hr style='border: 2px solid red;'>

# ## Estimando um novo modelo com a substituição da variável explicativa Temperatura Máxima pela Temperatuda Média

# In[ ]:





# ## Criando os datasets de treino e de teste

# In[ ]:





# ## Instanciando a classe *LinearRegression()*

# In[ ]:





# ## Utilizando o método *fit()* do objeto "modelo_2" para estimar nosso modelo linear utilizando os dados de TREINO (y2_train e X2_train)

# In[ ]:





# ## Obtendo o coeficiente de determinação (R²) do novo modelo estimado e comparando com o resultado do modelo anterior

# In[ ]:





# In[ ]:





# ## Gerando previsões para os dados de TESTE (X_test e X2_test) utilizando o método *predict()* dos objetos "modelo" e "modelo_2"

# In[ ]:





# ## Obtendo o coeficiente de determinação (R²) para as previsões dos dois modelos

# In[ ]:





# In[ ]:





# # <font color='red' style='font-size: 30px;'>Outras Métricas de Regressão</font>
# <hr style='border: 2px solid red;'>

# ## Métricas da regressão
# <hr>
# 
# fonte: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics
# 
# Algumas estatísticas obtidas do modelo de regressão são muito úteis como critério de comparação entre modelos estimados e de seleção do melhor modelo, as principais métricas de regressão que o scikit-learn disponibiliza para modelos lineares são as seguintes:
# 
# ### Erro Quadrático Médio
# 
# Média dos quadrados dos erros. Ajustes melhores apresentam $EQM$ mais baixo.
# 
# $$EQM(y, \hat{y}) = \frac 1n\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2$$
# 
# ### Raíz do Erro Quadrático Médio
# 
# Raíz quadrada da média dos quadrados dos erros. Ajustes melhores apresentam $\sqrt{EQM}$ mais baixo.
# 
# $$\sqrt{EQM(y, \hat{y})} = \sqrt{\frac 1n\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}$$
# 
# 

# ## Obtendo métricas para o modelo com Temperatura Média

# In[ ]:





# ## Obtendo métricas para o modelo com Temperatura Máxima

# In[ ]:





# # <font color='red' style='font-size: 30px;'>Salvando e Carregando o Modelo Estimado</font>
# <hr style='border: 2px solid red;'>

# ## Dados de entrada

# In[ ]:





# In[ ]:





# ## Gerando previsão pontual

# In[ ]:





# ## Criando um simulador simples

# In[ ]:





# ## Salvando o modelo estimado

# ## pickle (https://docs.python.org/3/library/pickle.html)
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O módulo <b>pickle</b> implementa protocolos binários para serializar e desserializar a estrutura de um objeto Python.</p>

# In[ ]:





# In[ ]:





# ### Em um novo notebook/projeto Python
# 
# <h4 style='color: blue; font-weight: normal'>In [1]:</h4>
# 
# ```sh
# import pickle
# 
# modelo = open('modelo_consumo_cerveja','rb')
# lm_new = pickle.load(modelo)
# modelo.close()
# 
# temp_max = 30.5
# chuva = 12.2
# fds = 0
# entrada = [[temp_max, chuva, fds]]
# print('{0:.2f} litros'.format(lm_new.predict(entrada)[0]))
# ```
# 
# <h4 style='color: red; font-weight: normal'>Out [1]:</h4>
# 
# ```
# 26094.90 litros
# ```

# In[ ]:




