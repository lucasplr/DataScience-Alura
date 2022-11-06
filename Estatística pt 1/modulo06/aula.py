#!/usr/bin/env python
# coding: utf-8

# ***
# # <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 1</font>
# ***
# 
# ## Trabalho de Análise Descritiva de um Conjunto de Dados
# 
# Utilizando os conhecimentos adquiridos em nosso treinamento realize uma análise descritiva básica de um conjunto de dados retirados da Pesquisa Nacional por Amostra de Domicílios - 2015 do IBGE. 
# 
# Vamos construir histogramas, calcular e avaliar medidas de tendência central, medidas separatrizes e de dispersão dos dados.
# 
# Siga o roteiro proposto e vá completando as células vazias. Procure pensar em mais informações interessantes que podem ser exploradas em nosso dataset.

# # <font color=green>DATASET DO PROJETO</font>
# ***

# ### Pesquisa Nacional por Amostra de Domicílios - 2015
# 
# A <b>Pesquisa Nacional por Amostra de Domicílios - PNAD</b> investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

# ### Fonte dos Dados
# 
# https://ww2.ibge.gov.br/home/estatistica/populacao/trabalhoerendimento/pnad2015/microdados.shtm

# ### Variáveis utilizadas
# 
# > ### Renda
# > ***
# 
# Rendimento mensal do trabalho principal para pessoas de 10 anos ou mais de idade.
# 
# > ### Idade
# > ***
# 
# Idade do morador na data de referência em anos.
# 
# > ### Altura (elaboração própria)
# > ***
# 
# Altura do morador em metros.
# 
# > ### UF
# > ***
# 
# |Código|Descrição|
# |---|---|
# |11|Rondônia|
# |12|Acre|
# |13|Amazonas|
# |14|Roraima|
# |15|Pará|
# |16|Amapá|
# |17|Tocantins|
# |21|Maranhão|
# |22|Piauí|
# |23|Ceará|
# |24|Rio Grande do Norte|
# |25|Paraíba|
# |26|Pernambuco|
# |27|Alagoas|
# |28|Sergipe|
# |29|Bahia|
# |31|Minas Gerais|
# |32|Espírito Santo|
# |33|Rio de Janeiro|
# |35|São Paulo|
# |41|Paraná|
# |42|Santa Catarina|
# |43|Rio Grande do Sul|
# |50|Mato Grosso do Sul|
# |51|Mato Grosso|
# |52|Goiás|
# |53|Distrito Federal|
# 
# > ### Sexo	
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Masculino|
# |1|Feminino|
# 
# > ### Anos de Estudo
# > ***
# 
# |Código|Descrição|
# |---|---|
# |1|Sem instrução e menos de 1 ano|
# |2|1 ano|
# |3|2 anos|
# |4|3 anos|
# |5|4 anos|
# |6|5 anos|
# |7|6 anos|
# |8|7 anos|
# |9|8 anos|
# |10|9 anos|
# |11|10 anos|
# |12|11 anos|
# |13|12 anos|
# |14|13 anos|
# |15|14 anos|
# |16|15 anos ou mais|
# |17|Não determinados| 
# ||Não aplicável|
# 
# > ### Cor
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Indígena|
# |2|Branca|
# |4|Preta|
# |6|Amarela|
# |8|Parda|
# |9|Sem declaração|

# #### <font color='red'>Observação</font>
# ***
# > Os seguintes tratamentos foram realizados nos dados originais:
# > 1. Foram eliminados os registros onde a <b>Renda</b> era inválida (999 999 999 999);
# > 2. Foram eliminados os registros onde a <b>Renda</b> era missing;
# > 3. Foram considerados somente os registros das <b>Pessoas de Referência</b> de cada domicílio (responsável pelo domicílio).

# ***
# ***

# ### Utilize a célula abaixo para importar as biblioteca que precisar para executar as tarefas
# #### <font color='red'>Sugestões: pandas, numpy, seaborn</font>

# In[242]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ### Importe o dataset e armazene o conteúdo em uma DataFrame

# In[243]:


data = pd.read_csv('dados.csv')


# ### Visualize o conteúdo do DataFrame

# In[244]:


data


# ### Para avaliarmos o comportamento da variável RENDA vamos construir uma tabela de frequências considerando as seguintes classes em salários mínimos (SM)
# #### <font color='blue'>Descreva os pontos mais relevantes que você observa na tabela e no gráfico.</font>
# 
# Classes de renda:
# 
# <b>A</b> ► Acima de 25 SM
# 
# <b>B</b> ► De 15 a 25 SM
# 
# <b>C</b> ► De 5 a 15 SM
# 
# <b>D</b> ► De 2 a 5 SM
# 
# <b>E</b> ► Até 2 SM
# 
# Para construir as classes de renda considere que o salário mínimo na época da pesquisa era de <b>R$ 788,00</b>.
# 
# #### Siga os passos abaixo:

# ### 1º Definir os intevalos das classes em reais (R$)

# In[245]:


classes = [data.Renda.min(), 788*2, 5*788, 15*788, 25*788, data.Renda.max()]


# ### 2º Definir os labels das classes

# In[246]:


labels = ['E', 'D', 'C', 'B', 'A']


# ### 3º Construir a coluna de frequências

# In[247]:


frequencia = pd.value_counts(
             pd.cut(x = data.Renda,
            bins = classes,
            labels = labels,
            include_lowest=True)
)
frequencia


# ### 4º Construir a coluna de percentuais

# In[248]:


percentuais = pd.value_counts(
  pd.cut(x = data.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True),
         normalize=True
) * 100
percentuais


# ### 5º Juntar as colunas de frequência e percentuais e ordenar as linhas de acordo com os labels das classes

# In[249]:


dist_freq_quantitativas = pd.DataFrame({"Frequência": frequencia, "Porcentagem %": percentuais})
dist_freq_quantitativas.sort_index(ascending = False)


# ### Construa um gráfico de barras para visualizar as informações da tabela de frequências acima

# In[250]:


#%matplotlib inline

#ax = sns.barplot(
 #   y=frequencia, x=labels)
#ax.figure.set_size_inches(12, 6)
#sns.set_theme(style='whitegrid')
#ax.set_title('Distribuição de Frequências - Classe', fontsize=18)
#ax.set_xlabel('Classe', fontsize=14)
#ax.set_ylabel('Renda', fontsize=14)

#for p in ax.patches:
 #   h = p.get_height() #get height
  #  ax.text(x = p.get_x()+(p.get_width()/2), #x-coordinate position of
   #         #data label, padded to be in the middle of the bar
   # y = h+100, #y-coordinate position of data label,
   #         #padded 100 above bar
   # s = '{:.0f}'.format(h),
   #         #data label, formatted to ignore decimals
   #         
   # ha = 'center'#sets horizontal alignment (ha) to center
   # )
#ax 

dist_freq_quantitativas['Frequência'].plot.bar(width=1, color = 'blue', alpha=0.3, figsize=(14,6))


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ### Crie um histograma para as variáveis QUANTITATIVAS de nosso dataset
# #### <font color='blue'>Descreva os pontos mais relevantes que você observa nos gráficos (assimetrias e seus tipos, possíveis causas para determinados comportamentos etc.)</font>

# In[251]:


#idades = data.Idade
#sns.histplot(
 #   data,
  #  x='Idade',
   # multiple='stack')

#aparentemente apresenta uma assimetria à direita, visto que pessoas idosas puxam o gráfico

ax = sns.distplot(data['Idade'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - IDADE', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[252]:


sns.histplot(
    data,
    x='Renda'
)


# In[253]:


sns.histplot(
    data,
    x='Altura'
)

#aparentemente o gráfico apresenta uma configuração simétrica, visto que as alturas tendem a seguir um padrão


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ### Para a variável RENDA, construa um histograma somente com as informações das pessoas com rendimento até R$ 20.000,00

# In[254]:


#renda = data.query('Renda < 20000')
#renda
#sns.histplot(
#    renda,
 #   x='Renda')

ax = sns.distplot(data.query('Renda < 20000')['Renda'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - RENDA - Pessoas com renda até R$ 20.000,00', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


# ### Construa uma tabela de frequências e uma com os percentuais do cruzando das variáveis SEXO e COR
# #### <font color='blue'>Avalie o resultado da tabela e escreva suas principais conclusões</font>
# #### <font color='red'>Utilize os dicionários abaixo para renomear as linha e colunas das tabelas de frequências e dos gráficos em nosso projeto</font>

# In[255]:


sexo = {
    0: 'Masculino', 
    1: 'Feminino'
}
cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda', 
    9: 'Sem declaração'
}
anos_de_estudo = {
    1: 'Sem instrução e menos de 1 ano', 
    2: '1 ano', 
    3: '2 anos', 
    4: '3 anos', 
    5: '4 anos', 
    6: '5 anos', 
    7: '6 anos', 
    8: '7 anos', 
    9: '8 anos', 
    10: '9 anos', 
    11: '10 anos', 
    12: '11 anos', 
    13: '12 anos', 
    14: '13 anos', 
    15: '14 anos', 
    16: '15 anos ou mais', 
    17: 'Não determinados'
}
uf = {
    11: 'Rondônia', 
    12: 'Acre', 
    13: 'Amazonas', 
    14: 'Roraima', 
    15: 'Pará', 
    16: 'Amapá', 
    17: 'Tocantins', 
    21: 'Maranhão', 
    22: 'Piauí', 
    23: 'Ceará', 
    24: 'Rio Grande do Norte', 
    25: 'Paraíba', 
    26: 'Pernambuco', 
    27: 'Alagoas', 
    28: 'Sergipe', 
    29: 'Bahia', 
    31: 'Minas Gerais', 
    32: 'Espírito Santo', 
    33: 'Rio de Janeiro', 
    35: 'São Paulo', 
    41: 'Paraná', 
    42: 'Santa Catarina', 
    43: 'Rio Grande do Sul', 
    50: 'Mato Grosso do Sul', 
    51: 'Mato Grosso', 
    52: 'Goiás', 
    53: 'Distrito Federal'
}


# In[256]:


freq_cruzada = pd.crosstab(data.Sexo, data.Cor)
freq_cruzada.rename(index = sexo, inplace=True)
freq_cruzada.rename(columns = cor, inplace=True)
freq_cruzada


# In[257]:


freq_cruzada = pd.crosstab(data.Sexo, data.Cor, normalize=True) * 100
freq_cruzada.rename(index = sexo, inplace=True)
freq_cruzada.rename(columns = cor, inplace=True)
freq_cruzada


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ## Realize, para a variável RENDA, uma análise descritiva com as ferramentas que aprendemos em nosso treinamento

# ### Obtenha a média aritimética

# In[258]:


data.Renda.mean()


# ### Obtenha a mediana

# In[259]:


data.Renda.median()


# ### Obtenha a moda

# In[260]:


data.Renda.mode()[0]


# ### Obtenha o desvio médio absoluto

# In[261]:


data.Renda.mad()


# ### Obtenha a variância

# In[262]:


data.Renda.var()


# ### Obtenha o desvio-padrão

# In[263]:


data.Renda.std()


# ### Obtenha a média, mediana e valor máximo da variável RENDA segundo SEXO e COR
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = {'mean', 'median', 'max'}</i></font>

# In[264]:


rendas = pd.crosstab( data.Cor, data.Sexo, data.Renda, 
                    aggfunc={'mean', 'median', 'max'})
rendas.rename(columns = sexo, inplace=True)
rendas.rename(index = cor, inplace=True)
rendas


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ### Obtenha as medidas de dispersão da variável RENDA segundo SEXO e COR
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = {'mad', 'var', 'std'}</i></font>

# In[265]:


disp_por_renda = pd.crosstab( data.Cor, data.Sexo, data.Renda, 
                    aggfunc={'mad', 'var', 'std'})
disp_por_renda.rename(columns = sexo, inplace=True)
disp_por_renda.rename(index = cor, inplace=True)
disp_por_renda


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ### Construa um box plot da variável RENDA segundo SEXO e COR
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos de pessoas analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>
# #### <font color='red'>2º - Para incluir uma terceira variável na construção de um boxplot utilize o parâmetro <i>hue</i> e indique a variável que quer incluir na subdivisão.</font>
# #### Mais informações: https://seaborn.pydata.org/generated/seaborn.boxplot.html

# In[266]:


renda_max = data.query('Renda < 10000')

renda_max['Sexo'] = renda_max['Sexo'].map({1: 'Feminino', 0: 'Masculino'})
renda_max['Cor'] = renda_max['Cor'].map({0: 'Indígena', 
                                         2: 'Branca', 
                                         4: 'Preta', 
                                         6: 'Amarela', 
                                         8: 'Parda', 
                                         9: 'Sem declaração'})

ax = sns.boxplot(
    x='Renda',
    y='Cor',
    hue='Sexo',
    data=renda_max,
    orient='h'
    )
ax.figure.set_size_inches(14, 8)
ax.set_title('Renda por Sexo e Cor', fontsize=25)
ax.set_xlabel('Salário', fontsize=18)
ax


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# # <font color="red">DESAFIO<font>
# ### Qual percentual de pessoas de nosso <i>dataset</i> ganham um salário mínimo (R$ 788,00) ou menos?
# #### <font color='red'>Utilize a função <i>percentileofscore()</i> do <i>scipy</i> para realizar estas análises.</font>
# #### Mais informações: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.percentileofscore.html
# 

# In[267]:


from scipy import stats
percentual = stats.percentileofscore(data.Renda, 788, kind='weak')
print(f'{percentual:.2f}%')


# ### Qual o valor máximo ganho por 99% das pessoas de nosso <i>dataset</i>?
# #### <font color='red'>Utilize o método <i>quantile()</i> do <i>pandas</i> para realizar estas análises.</font>

# In[268]:


data.Renda.quantile([i / 100 for i in range(1, 100)])


# ### Obtenha a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo ANOS DE ESTUDO e SEXO
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = ['mean', 'median', 'max', 'std']</i></font>

# In[269]:


status_renda_por_estudo_sexo = pd.crosstab( data['Anos de Estudo'], data.Sexo, data.Renda,
                                          aggfunc = {'mean', 'median', 'max', 'std'})
status_renda_por_estudo_sexo.rename(columns = sexo, inplace=True)
status_renda_por_estudo_sexo.rename(index = anos_de_estudo, inplace=True)
status_renda_por_estudo_sexo


# ### Construa um box plot da variável RENDA segundo ANOS DE ESTUDO e SEXO
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos de pessoas analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>
# #### <font color='red'>2º - Utilize a variável IDADE para identificar se a desigualdade se verifica para pessoas de mesma idade. Exemplo: <i>data=dados.query('Renda < 10000 and Idade == 40')</i> ou <i>data=dados.query('Renda < 10000 and Idade == 50')</i></font>
# #### <font color='red'>3º - Para incluir uma terceira variável na construção de um boxplot utilize o parâmetro <i>hue</i> e indique a variável que quer incluir na subdivisão.</font>
# #### Mais informações: https://seaborn.pydata.org/generated/seaborn.boxplot.html

# In[270]:


data['Sexo'] = data['Sexo'].map({1: 'Feminino', 0: 'Masculino'})
data['Anos de Estudo'] = data['Anos de Estudo'].map({1: 'Sem instrução e menos de 1 ano', 
    2: '1 ano', 
    3: '2 anos', 
    4: '3 anos', 
    5: '4 anos', 
    6: '5 anos', 
    7: '6 anos', 
    8: '7 anos', 
    9: '8 anos', 
    10: '9 anos', 
    11: '10 anos', 
    12: '11 anos', 
    13: '12 anos', 
    14: '13 anos', 
    15: '14 anos', 
    16: '15 anos ou mais', 
    17: 'Não determinados'})

ax = sns.boxplot(
    x='Renda',
    y='Anos de Estudo',
    hue='Sexo',
    data=data.query('Renda < 10000 and Idade == 50'),
    orient='h')


ax.figure.set_size_inches(20, 12)
ax.set_title('Renda por Sexo', fontsize=25)
ax.set_xlabel('Salário', fontsize=18)
ax.set_ylabel('Anos de Estudo', fontsize=18)
ax.set_yticklabels([key for key in anos_de_estudo.values()], fontsize=12)
ax


# > ### Conclusões
# 
# Escreva suas conclusões aqui...

# ### Obtenha a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>Utilize o método <i>groupby()</i> do <i>pandas</i> juntamente com o método <i>agg()</i> para contruir a tabulação. O método <i>agg()</i> pode receber um dicionário especificando qual coluna do DataFrame deve ser utilizada e qual lista de funções estatísticas queremos obter, por exemplo: <i>dados.groupby(['UF']).agg({'Renda': ['mean', 'median', 'max', 'std']})</i></font>

# In[271]:


data.UF = data.UF.map({
    11: 'Rondônia', 
    12: 'Acre', 
    13: 'Amazonas', 
    14: 'Roraima', 
    15: 'Pará', 
    16: 'Amapá', 
    17: 'Tocantins', 
    21: 'Maranhão', 
    22: 'Piauí', 
    23: 'Ceará', 
    24: 'Rio Grande do Norte', 
    25: 'Paraíba', 
    26: 'Pernambuco', 
    27: 'Alagoas', 
    28: 'Sergipe', 
    29: 'Bahia', 
    31: 'Minas Gerais', 
    32: 'Espírito Santo', 
    33: 'Rio de Janeiro', 
    35: 'São Paulo', 
    41: 'Paraná', 
    42: 'Santa Catarina', 
    43: 'Rio Grande do Sul', 
    50: 'Mato Grosso do Sul', 
    51: 'Mato Grosso', 
    52: 'Goiás', 
    53: 'Distrito Federal'
})

data_em_query = data.groupby(['UF']).agg({'Renda':['mean', 'median', 'max', 'std']})
#status_renda_por_uf_sexo = pd.DataFrame(data.groupby(['uf']).agg({'Renda':['mean', 'median', 'max', 'std']})
#status_renda_por_UF_sexo.rename(index = sexo, inplace=True)
#status_renda_por_UF_sexo.rename(columns = anos_de_estudo, inplace=True)
#status_renda_por_uf_sexo
data_em_query


# ### Construa um box plot da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>

# In[272]:


renda_max = data.query('Renda < 10000')


renda_max

ax = sns.boxplot(
        x='Renda',
        y='UF',
        data=renda_max,
        orient='h')
ax


# > ### Conclusões
# 
# Escreva suas conclusões aqui...
