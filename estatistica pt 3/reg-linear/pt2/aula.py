#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: green; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear II</h1>

# # <font color='red' style='font-size: 30px;'>1.2 Conhecendo o Dataset</font>
# <hr style='border: 2px solid red;'>

# ## Importando a biblioteca pandas
# 
# https://pandas.pydata.org/

# In[1]:


import pandas as pd


# ## O Dataset e o Projeto
# <hr>
# 
# ### Descrição:
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify; text-indent: 35px;'>O mercado imobiliário vem sendo objeto de diversos estudos e pesquisas nos últimos tempos. A crise financeira que afeta a economia tem afetado significativamente os investimentos e ganhos advindos deste setor. Este cenário incentiva o aumento do interesse por estudos de previsão de demanda baseados em características deste mercado, dos imóveis e do entorno destes imóveis.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify; text-indent: 35px;'>Neste contexto o objetivo principal do nosso projeto é desenvolver um sistema de avaliação imobiliária utilizando a metodologia de regressões lineares que é uma das técnicas de machine learning.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify; text-indent: 35px;'>Nosso *dataset* é uma amostra aleatória de tamanho 5000 de imóveis disponíveis para venda no município do Rio de Janeiro.</p>
# 
# ### Dados:
# <ul style='font-size: 18px; line-height: 2; text-align: justify;'>
#     <li><b>Valor</b> - Valor (R$) de oferta do imóvel</li>
#     <li><b>Area</b> - Área do imóvel em m²</li>
#     <li><b>Dist_Praia</b> - Distância do imóvel até a praia (km) (em linha reta)</li>
#     <li><b>Dist_Farmacia</b> - Distância do imóvel até a farmácia mais próxima (km) (em linha reta)</li>
# </ul>

# ## Leitura dos dados

# In[2]:


data = pd.read_csv('dataset.csv', sep=';')


# ## Visualizar os dados

# In[3]:


data.head()


# ## Verificando o tamanho do dataset

# In[4]:


data.shape


# # <font color='red' style='font-size: 30px;'>1.3 Análises Preliminares</font>
# <hr style='border: 2px solid red;'>

# ## Estatísticas descritivas

# In[5]:


data.describe().round(2)


# ## Matriz de correlação
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>coeficiente de correlação</b> é uma medida de associação linear entre duas variáveis e situa-se entre <b>-1</b> e <b>+1</b> sendo que <b>-1</b> indica associação negativa perfeita e <b>+1</b> indica associação positiva perfeita.</p>

# In[6]:


data.corr().round(4)


# # <font color='red' style='font-size: 30px;'>2.1 Comportamento da Variável Dependente (Y)</font>
# <hr style='border: 2px solid red;'>

# ## Importando biblioteca seaborn
# https://seaborn.pydata.org/
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O Seaborn é uma biblioteca Python de visualização de dados baseada no matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos.</p>

# In[7]:


import seaborn as sns


# ## Configurações de formatação dos gráficos

# In[8]:


# palette -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
sns.set_palette('Accent')
# style -> white, dark, whitegrid, darkgrid, ticks
sns.set_style('darkgrid')


# ## Box plot da variável *dependente* (y)

# <img width='700px' src='../Dados/img/Box-Plot.png'>

# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot

# In[9]:


ax = sns.boxplot(data=data.Valor, orient='h', width=0.3)
ax.figure.set_size_inches(20, 6)
ax.set_title('Preço dos Imóveis', fontsize=20)
ax.set_xlabel('Reais', fontsize=16)
ax


# # <font color='red' style='font-size: 30px;'>2.2 Distribuição de Frequências</font>
# <hr style='border: 2px solid red;'>

# ## Distribuição de frequências da variável *dependente* (y)

# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=distplot#seaborn.distplot

# In[10]:


ax = sns.distplot(data.Valor)
ax.figure.set_size_inches(20, 6)
ax.set_title('Distribuição de Frequências', fontsize=20)
ax.set_xlabel('Preço dos Imóveis (R$)', fontsize=16)
ax


# <img width='800px' src='../Dados/img/Box-Plot II.png'>

# # <font color='red' style='font-size: 30px;'>2.3 Dispersão Entre as Variáveis</font>
# <hr style='border: 2px solid red;'>

# ## Gráficos de dispersão entre as variáveis do dataset

# ## seaborn.pairplot
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota o relacionamento entre pares de variáveis em um dataset.</p>

# In[11]:


ax = sns.pairplot(data, y_vars='Valor', x_vars=['Area', 'Dist_Praia', 'Dist_Farmacia'], height=5)
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize=20, y=1.05)
ax


# In[12]:


ax = sns.pairplot(data, y_vars='Valor', x_vars=['Area', 'Dist_Praia', 'Dist_Farmacia'], kind='reg', height=5)
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize=20, y=1.05)
ax


# # <font color='red' style='font-size: 30px;'>3.1 Transformando os Dados</font>
# <hr style='border: 2px solid red;'>

# ## Distribuição Normal
# <hr>
# 
# ### Por quê? 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Testes paramétricos assumem que os dados amostrais foram coletados de uma população com distribuição de probabilidade conhecida. Boa parte dos testes estatísticos assumem que os dados seguem uma distribuição normal (t de Student, intervalos de confiança etc.).</p>
# 
# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'></p>

# ## Importando biblioteca numpy

# In[13]:


import numpy as np


# ## Aplicando a transformação logarítmica aos dados do *dataset*
# 
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.log.html

# In[14]:


data['log_Valor'] = np.log(data.Valor)


# In[15]:


data['log_Area'] = np.log(data.Area)
data['log_Valor'] = np.log(data.Valor)

data['log_Dist_Praia'] = np.log(data['Dist_Praia'] + 1)
data['log_Dist_Farmacia'] = np.log(data['Dist_Farmacia'] + 1)


# In[16]:


data.head()


# ## Distribuição de frequências da variável *dependente transformada* (y)

# In[17]:


ax = sns.distplot(data['log_Valor'])
ax.figure.set_size_inches(20, 6)
ax.set_title('Distribuição de Frequências', fontsize=20)
ax.set_xlabel('Preço dos Imóveis (R$)', fontsize=16)
ax


# # <font color='red' style='font-size: 30px;'>3.2 Verificando Relação Linear</font>
# <hr style='border: 2px solid red;'>

# ## Gráficos de dispersão entre as variáveis transformadas do dataset

# In[18]:


ax = sns.pairplot(data, y_vars='log_Valor', x_vars=['log_Area', 'log_Dist_Praia', 'log_Dist_Farmacia', ], kind='reg', height=5)
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize=20, y=1.05)
ax
ax.fig.suptitle('Dispersão entre as Variáveis Transformadas', fontsize=20, y=1.05)
ax


# # <font color='red' style='font-size: 30px;'>4.1 Criando os *Datasets* de Treino e Teste</font>
# <hr style='border: 2px solid red;'>

# ## Importando o *train_test_split* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# In[19]:


from sklearn.model_selection import train_test_split


# ## Criando uma Series (pandas) para armazenar o Preço dos Imóveis (y)

# In[20]:


y = data['log_Valor']


# ## Criando um DataFrame (pandas) para armazenar as variáveis explicativas (X)

# In[21]:


X = data[['log_Area', 'log_Dist_Praia', 'log_Dist_Farmacia']]


# ## Criando os datasets de treino e de teste

# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2811)


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

# <img width='800px' src='../Dados/img/Log-linear.png'>

# ## Importando a biblioteca statsmodels
# 
# https://www.statsmodels.org/stable/index.html

# In[23]:


import statsmodels.api as sm

X_train_com_constante = sm.add_constant(X_train)


# ## Estimando o modelo com statsmodels

# In[24]:


model_statsmodels = sm.OLS(y_train, X_train_com_constante, hasconst=True).fit()


# # <font color='red' style='font-size: 30px;'>4.2 Avaliando o Modelo Estimado</font>
# <hr style='border: 2px solid red;'>

# ## Avaliando as estatísticas de teste do modelo

# In[25]:


model_statsmodels.summary()


# # <font color='red' style='font-size: 30px;'>4.3 Modificando o Modelo e Avaliando Novamente o Ajuste</font>
# <hr style='border: 2px solid red;'>

# ## Criando um novo conjunto de variáveis explicativas (X)

# In[27]:


X = data[['log_Area', 'log_Dist_Praia']]


# ## Criando os datasets de treino e de teste

# In[28]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2811)


# ## Estimando o modelo com o statsmodels

# In[32]:


X_train_com_constante = sm.add_constant(X_train)
model_statsmodels = sm.OLS(y_train, X_train_com_constante, hasconst=True).fit()


# ## Avaliando as estatísticas de teste do novo modelo

# In[34]:


model_statsmodels.summary()


# # <font color='red' style='font-size: 30px;'>5.1 Estimando o Modelo com os Dados de Treino</font>
# <hr style='border: 2px solid red;'>

# ## Importando *LinearRegression* e *metrics* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# https://scikit-learn.org/stable/modules/classes.html#regression-metrics

# In[37]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# ## Instanciando a classe *LinearRegression()*

# In[36]:


model_1 = LinearRegression()


# ## Utilizando o método *fit()* do objeto "modelo" para estimar nosso modelo linear utilizando os dados de TREINO (y_train e X_train)
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit

# In[38]:


model_1.fit(X_train, y_train)


# ## Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score
# 
# ### Coeficiente de Determinação - R²
# 
# O coeficiente de determinação (R²) é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entra 0 e 1.
# 
# $$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$

# In[40]:


print(f'R²{model_1.score(X_train, y_train).round(2)}')


# ## Gerando previsões para os dados de TESTE (X_test) utilizando o método *predict()* do objeto "modelo"
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict

# In[43]:


y_previsto = model_1.predict(X_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões do nosso modelo
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

# In[44]:


print(f'{metrics.r2_score(y_test, y_previsto)}')


# In[ ]:





# # <font color='red' style='font-size: 30px;'>5.2 Obtendo Previsões Pontuais</font>
# <hr style='border: 2px solid red;'>

# ## Dados de entrada

# In[46]:


entrada = X_test[0:1]
entrada


# ## Gerando previsão pontual

# In[47]:


model_1.predict(entrada)


# ## Invertendo a transformação para obter a estimativa em R$
# 
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.exp.html

# In[48]:


np.exp(model_1.predict(entrada)[0])


# ## Criando um simulador simples

# In[52]:


area = 250
Dist_Praia = 1
entrada = [[np.log(area), np.log(Dist_Praia + 1)]]

print(f'{np.exp(model_1.predict(entrada)[0]).round(2)}')


# # <font color='red' style='font-size: 30px;'>5.3 Interpretação dos Coeficientes Estimados</font>
# <hr style='border: 2px solid red;'>

# ## Obtendo o intercepto do modelo
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>intercepto</b> representa o efeito médio em $Y$ (Preço do Imóveis) tendo todas as variáveis explicativas excluídas do modelo. No caso do modelo log-linear este coeficiente deve ser transformado com o uso da função exponencial para ser apresentado em R$.</p>

# In[53]:


model_1.intercept_


# In[54]:


np.exp(model_1.intercept_)


# ## Obtendo os coeficientes de regressão
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>Os <b>coeficientes de regressão</b> $\beta_2$ e $\beta_3$ são conhecidos como <b>coeficientes parciais de regressão</b> ou <b>coeficientes parciais angulares</b>. </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>Um aspecto interessante do modelo log-linear, que o tornou muito utilizado nos trabalhos aplicados, é que os coeficientes angulares $\beta_2$ e $\beta_3$ medem as elasticidades de Y em relação a $X_2$ e $X_3$, isto é, a variação percentual de Y correspondente a uma dada variação percentual (pequena) em $X_2$ e $X_3$.</p>

# In[55]:


model_1.coef_


# ## Confirmando a ordem das variáveis explicativas no DataFrame

# In[56]:


X.columns


# ## Criando uma lista com os nomes das variáveis do modelo

# In[60]:


index = ['Intercept', 'Area', 'Dist_Praia']


# ## Criando um DataFrame para armazenar os coeficientes do modelo
# 
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html?#numpy.append

# In[61]:


pd.DataFrame(data=np.append(model_1.intercept_, model_1.coef_), index=index, columns=['Parâmetros'])


# ## Interpretação dos Coeficientes Estimados
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Intercepto</b> → Excluindo o efeito das variáveis explicativas ($X_2=X_3=0$) o efeito médio no Preço dos Imóveis seria de <b>R$ 11.326,68</b> (exp[9.334916]).
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Área (m²)</b> → Mantendo-se o valor de $X_3$ (Distância até a Praia) constante, um acréscimo de 1% na Área de um imóvel gera, em média, um acréscimo de <b>1.06%</b> no Preço do Imóvel.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Distância até a Praia (km)</b> → Mantendo-se o valor de $X_2$ (Área) constante, um acréscimo de 1% na Distância de um imóvel até a praia gera, em média, um decréscimo de <b>0.49%</b> no Preço do Imóvel.
# </p>

# # <font color='red' style='font-size: 30px;'>5.4 Análises Gráficas dos Resultados do Modelo</font>
# <hr style='border: 2px solid red;'>

# ## Gerando as previsões do modelo para os dados de TREINO

# In[63]:


y_previsto_train = model_1.predict(X_train)


# ## Gráfico de dispersão entre valor estimado e valor real
# 
# https://seaborn.pydata.org/generated/seaborn.scatterplot.html

# In[68]:


ax = sns.scatterplot(x=y_previsto_train, y=y_train)
ax.figure.set_size_inches(12, 6)
ax.set_title('Previsão X Real', fontsize=18)
ax.set_xlabel('log do Preço - Previsão', fontsize=14)
ax.set_ylabel('log do Preço - Real', fontsize=14)
ax


# ## Obtendo os resíduos

# In[70]:


residuo = y_train - y_previsto_train
residuo


# ## Plotando a distribuição de frequências dos resíduos

# In[71]:


ax = sns.distplot(residuo)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências dos Resíduos', fontsize=18)
ax.set_xlabel('log do Preço', fontsize=14)
ax


# In[ ]:




