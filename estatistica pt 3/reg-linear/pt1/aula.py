#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: green; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear</h1>

# # <font color='red' style='font-size: 30px;'>Conhecendo o Dataset</font>
# <hr style='border: 2px solid red;'>

# ## Importando bibliotecas

# In[136]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## O Dataset e o Projeto
# <hr>
# 
# ### Fonte: https://www.kaggle.com/greenwing1985/housepricing
# 
# ### Descrição:
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Nosso objetivo neste exercício é criar um modelo de machine learning, utilizando a técnica de Regressão Linear, que faça previsões sobre os preços de imóveis a partir de um conjunto de características conhecidas dos imóveis.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Vamos utilizar um dataset disponível no Kaggle que foi gerado por computador para treinamento de machine learning para iniciantes. Este dataset foi modificado para facilitar o nosso objetivo, que é fixar o conhecimento adquirido no treinamento de Regressão Linear.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Siga os passos propostos nos comentários acima de cada célular e bons estudos.</p>
# 
# ### Dados:
# <ul style='font-size: 18px; line-height: 2; text-align: justify;'>
#     <li><b>precos</b> - Preços do imóveis</li>
#     <li><b>area</b> - Área do imóvel</li>
#     <li><b>garagem</b> - Número de vagas de garagem</li>
#     <li><b>banheiros</b> - Número de banheiros</li>
#     <li><b>lareira</b> - Número de lareiras</li>
#     <li><b>marmore</b> - Se o imóvel possui acabamento em mármore branco (1) ou não (0)</li>
#     <li><b>andares</b> - Se o imóvel possui mais de um andar (1) ou não (0)</li>
# </ul>

# ## Leitura dos dados
# 
# Dataset está na pasta "Dados" com o nome "HousePrices_HalfMil.csv" em usa como separador ";".

# In[137]:


data = pd.read_csv('HousePrices_HalfMil.csv', sep=';')


# ## Visualizar os dados

# In[138]:


data


# ## Verificando o tamanho do dataset

# In[139]:


len(data)


# # <font color='red' style='font-size: 30px;'>Análises Preliminares</font>
# <hr style='border: 2px solid red;'>

# ## Estatísticas descritivas

# In[140]:


data.describe().round(2)


# ## Matriz de correlação
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>coeficiente de correlação</b> é uma medida de associação linear entre duas variáveis e situa-se entre <b>-1</b> e <b>+1</b> sendo que <b>-1</b> indica associação negativa perfeita e <b>+1</b> indica associação positiva perfeita.</p>
# 
# ### Observe as correlações entre as variáveis:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>Quais são mais correlacionadas com a variável dependete (Preço)?</li>
#     <li>Qual o relacionamento entre elas (positivo ou negativo)?</li>
#     <li>Existe correlação forte entre as variáveis explicativas?</li>
# </ul>

# In[141]:


data.corr().round(2)


# # <font color='red' style='font-size: 30px;'>Comportamento da Variável Dependente (Y)</font>
# <hr style='border: 2px solid red;'>

# # Análises gráficas

# <img width='700px' src='../Dados/img/Box-Plot.png'>

# ## Importando biblioteca seaborn

# In[142]:


import seaborn as sns


# ## Configure o estilo e cor dos gráficos (opcional)

# In[143]:


sns.set_style('darkgrid')


# ## Box plot da variável *dependente* (y)
# 
# 
# ### Avalie o comportamento da distribuição da variável dependente:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>Parecem existir valores discrepantes (outliers)?</li>
#     <li>O box plot apresenta alguma tendência?</li>
# </ul>

# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot

# In[144]:


ax = sns.boxplot(data=data.precos, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ## Investigando a variável *dependente* (y) juntamente com outras característica
# 
# Faça um box plot da variável dependente em conjunto com cada variável explicativa (somente as categóricas).
# 
# ### Avalie o comportamento da distribuição da variável dependente com cada variável explicativa categórica:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>As estatísticas apresentam mudança significativa entre as categorias?</li>
#     <li>O box plot apresenta alguma tendência bem definida?</li>
# </ul>

# ### Box-plot (Preço X Garagem)

# In[145]:


ax = sns.boxplot(x='precos', y='garagem', data=data, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ### Box-plot (Preço X Banheiros)

# In[146]:


ax = sns.boxplot(x='precos', y='banheiros', data=data, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ### Box-plot (Preço X Lareira)

# In[147]:


ax = sns.boxplot(x='precos', y='lareira', data=data, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ### Box-plot (Preço X Acabamento em Mármore)

# In[148]:


ax = sns.boxplot(x='precos', y='marmore', data=data, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ### Box-plot (Preço X Andares)

# In[149]:


ax = sns.boxplot(x='precos', y='andares', data=data, orient='h', width=0.3)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax


# ## Distribuição de frequências da variável *dependente* (y)
# 
# Construa um histograma da variável dependente (Preço).
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>A distribuição de frequências da variável dependente parece ser assimétrica?</li>
#     <li>É possível supor que a variável dependente segue uma distribuição normal?</li>
# </ul>

# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=distplot#seaborn.distplot

# In[150]:


ax = sns.histplot(x='precos', data=data, bins=30, kde=True)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de frequências dos preços', fontsize=18)
ax.set_xlabel('Preços', fontsize=14)
ax.set_ylabel('Quantidade', fontsize=14)
ax


# ## Gráficos de dispersão entre as variáveis do dataset

# ## Plotando o pairplot fixando somente uma variável no eixo y
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# 
# Plote gráficos de dispersão da variável dependente contra cada variável explicativa. Utilize o pairplot da biblioteca seaborn para isso.
# 
# Plote o mesmo gráfico utilizando o parâmetro kind='reg'.
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>É possível identificar alguma relação linear entre as variáveis?</li>
#     <li>A relação é positiva ou negativa?</li>
#     <li>Compare com os resultados obtidos na matriz de correlação.</li>
# </ul>

# In[151]:


ax = sns.pairplot(data, y_vars='precos', x_vars=['garagem', 'banheiros', 'lareira', 'marmore', 'andares'])
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize=20, y=1.05)
ax


# In[152]:


ax = sns.pairplot(data, y_vars='precos', x_vars=['garagem', 'banheiros', 'lareira', 'marmore', 'andares'], kind='reg')
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize=20, y=1.05)
ax


# # <font color='red' style='font-size: 30px;'>Estimando um Modelo de Regressão Linear</font>
# <hr style='border: 2px solid red;'>

# ## Importando o *train_test_split* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# In[153]:


from sklearn.model_selection import train_test_split


# ## Criando uma Series (pandas) para armazenar a variável dependente (y)

# In[154]:


y = data['precos']
y.shape


# ## Criando um DataFrame (pandas) para armazenar as variáveis explicativas (X)

# In[155]:


X = data[['area','garagem', 'banheiros', 'lareira', 'marmore', 'andares']]


# ## Criando os datasets de treino e de teste

# In[156]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811)


# ## Importando *LinearRegression* e *metrics* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# https://scikit-learn.org/stable/modules/classes.html#regression-metrics

# In[157]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# ## Instanciando a classe *LinearRegression()*

# In[158]:


model_1 = LinearRegression()


# ## Utilizando o método *fit()* para estimar o modelo linear utilizando os dados de TREINO (y_train e X_train)
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit

# In[159]:


model_1.fit(X_train, y_train)


# ## Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score
# 
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>O modelo apresenta um bom ajuste?</li>
#     <li>Você lembra o que representa o R²?</li>
#     <li>Qual medida podemos tomar para melhorar essa estatística?</li>
# </ul>

# In[160]:


r2_m1 = model_1.score(X_train, y_train).round(2)
print(f'{r2_m1}')


# ## Gerando previsões para os dados de TESTE (X_test) utilizando o método *predict()*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict

# In[161]:


y_previsto = model_1.predict(X_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões do nosso modelo
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

# In[162]:


m1 = metrics.r2_score(y_test, y_previsto).round(2)
print(f'{m1}')


# # <font color='red' style='font-size: 30px;'>Obtendo Previsões Pontuais</font>
# <hr style='border: 2px solid red;'>

# ## Criando um simulador simples
# 
# Crie um simulador que gere estimativas de preço a partir de um conjunto de informações de um imóvel.

# In[163]:


area = 50
andares = 1
garagem = 1
lareira = 0
banheiros = 2
marmore = 0

entrada = [[area, garagem, banheiros, lareira, marmore, andares]]
print(f'{model_1.predict(entrada)[0]:.02f}')


# # <font color='red' style='font-size: 30px;'>Métricas de Regressão</font>
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
# ### Coeficiente de Determinação - R²
# 
# O coeficiente de determinação (R²) é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entra 0 e 1.
# 
# $$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$

# ## Obtendo métricas para o modelo com Temperatura Máxima

# In[167]:


EQM = metrics.mean_squared_error(y_test, y_previsto).round(2)

REQM = np.sqrt(EQM).round(2)

R2 = metrics.r2_score(y_test, y_previsto).round(2)

pd.DataFrame([EQM, REQM, R2], ['EQM', 'REQM', 'R²'], columns=['Coeficientes'])


# # <font color='red' style='font-size: 30px;'>Salvando e Carregando o Modelo Estimado</font>
# <hr style='border: 2px solid red;'>

# ## Importando a biblioteca pickle

# In[168]:


import pickle


# ## Salvando o modelo estimado

# In[170]:


output = open('modelo_preço', 'wb')
pickle.dump(model_1, output)
output.close()


# ### Em um novo notebook/projeto Python
# 
# <h4 style='color: blue; font-weight: normal'>In [1]:</h4>
# 
# ```sh
# import pickle
# 
# modelo = open('modelo_preço','rb')
# lm_new = pickle.load(modelo)
# modelo.close()
# 
# area = 38
# garagem = 2
# banheiros = 4
# lareira = 4
# marmore = 0
# andares = 1
# 
# entrada = [[area, garagem, banheiros, lareira, marmore, andares]]
# 
# print('$ {0:.2f}'.format(lm_new.predict(entrada)[0]))
# ```
# 
# <h4 style='color: red; font-weight: normal'>Out [1]:</h4>
# 
# ```
# $ 46389.80
# ```

# In[ ]:




