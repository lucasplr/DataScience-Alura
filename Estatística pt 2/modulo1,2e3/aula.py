#!/usr/bin/env python
# coding: utf-8

# ***
# # <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 2</font>
# ***

# # <font color=green>1 CONHECENDO OS DADOS</font>
# ***

# ## <font color=green>1.1 Dataset do projeto</font>
# ***

# ### Pesquisa Nacional por Amostra de Domicílios - 2015
# 
# A **Pesquisa Nacional por Amostra de Domicílios - PNAD** investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

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
# > 1. Foram eliminados os registros onde a **Renda** era inválida (999 999 999 999);
# > 2. Foram eliminados os registros onde a **Renda** era missing;
# > 3. Foram considerados somente os registros das **Pessoas de Referência** de cada domicílio (responsável pelo domicílio).

# ### Importando pandas e lendo o dataset do projeto
# 
# https://pandas.pydata.org/

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('dados.csv')


# In[3]:


data


# In[ ]:





# ---
# ---

# # <font color=green>2 DISTRIBUIÇÕES DE PROBABILIDADE</font>
# ***

# ## <font color=red>Problema</font>
# ***

# Em um concurso para preencher uma vaga de cientista de dados temos um total de **10 questões** de múltipla escolha com **3 alternativas possíveis** em cada questão. **Cada questão tem o mesmo valor.** Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova **vale 10 pontos e a nota de corte seja 5**, obtenha a probabilidade deste candidato **acertar 5 questões** e também a probabilidade deste candidato **passar para a próxima etapa do processo seletivo**.

# ## <font color=green>2.1 Distribuição Binomial</font>
# ***

# Um evento **binomial** é caracterizado pela possibilidade de ocorrência de apenas duas categorias. Estas categorias somadas representam todo o espaço amostral, sendo também mutuamente excludentes, ou seja, a ocorrência de uma implica na não ocorrência da outra.
# 
# Em análises estatísticas o uso mais comum da distribuição binomial é na solução de problemas que envolvem situações de **sucesso** e **fracasso**.

# # $$P(k)=\binom{n}{k} p^k q^{n-k}$$
# 
# Onde:
# 
# $p$ = probabilidade de sucesso
# 
# $q = (1 - p)$ = probabilidade de fracasso
# 
# $n$ = número de eventos estudados
# 
# $k$ = número de eventos desejados que tenham sucesso

# ### Experimento Binomial

# 1. Realização de $n$ ensaios idênticos.
# 
# 2. Os ensaios são independentes.
# 
# 3. Somente dois resultados são possíveis, exemplo: Verdadeiro ou falso; Cara ou coroa; Sucesso ou fracasso.
# 
# 4. A probabilidade de sucesso é representada por $p$ e a de fracasso por $1-p=q$. Estas probabilidades não se modificam de ensaio para ensaio.

# ### Média da distribuição binomial

# O valor esperado ou a média da distribuição binomial é igual ao número de experimentos realizados multiplicado pela chance de ocorrência do evento.
# 
# # $$\mu = n \times p$$

# ### Desvio padrão da distribuição binomial

# O desvio padrão é o produto entre o número de experimentos, a probabilidade de sucesso e a probabilidade de fracasso.
# 
# # $$\sigma = \sqrt{n \times p \times q}$$

# ### Importando bibliotecas
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html

# In[5]:


from scipy.special import comb


# ### Combinações
# 
# Número de combinações de $n$ objetos, tomados $k$ a cada vez, é:
# 
# # $$C_{k}^{n} = \binom{n}{k} = \frac{n!}{k!(n - k)!}$$
# 
# Onde
# 
# ## $$n! = n\times(n-1)\times(n-2)\times...\times(2)\times(1)$$
# ## $$k! = k\times(k-1)\times(k-2)\times...\times(2)\times(1)$$
# 
# Por definição
# 
# ## $$0! = 1$$

# ## <font color='blue'>Exemplo: Mega Sena</font>

# Em um volante de loteria da Mega Sena temos um total de **60 números** para escolher onde a aposta mínima é de **seis números**. Você que é curiosa(o) resolve calcular a probabilidade de se acertar na Mega Sena com apenas **um jogo**. Para isso precisamos saber quantas **combinações de seis números podem ser formadas com os 60 números disponíveis**.
# 
# ### $$C_{6}^{60} = \binom{60}{6} = \frac{60!}{6!(60 - 6)!}$$

# combinacoes = comb(60, 6)
# combinacoes

# In[11]:


probabilidade = 1 / combinacoes
print('%0.15f' % probabilidade)


# ## <font color='blue'>Exemplo: Concurso para cientista de dados</font>

# Em um concurso para preencher uma vaga de cientista de dados temos um total de **10 questões** de múltipla escolha com **3 alternativas possíveis** em cada questão. **Cada questão tem o mesmo valor.** Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova **vale 10 pontos e a nota de corte seja 5**, obtenha a probabilidade deste candidato **acertar 5 questões** e também a probabilidade deste candidato **passar para a próxima etapa do processo seletivo**.

# ### Qual o número de ensaios ($n$)?

# In[16]:


n=10 #10 questões


# ### Os ensaios são independentes?

# Sim. A opção escolhida em uma questão não influencia em nada a opção escolhida em outra questão.

# ### Somente dois resultados são possíveis em cada ensaio?

# Sim. O candidato tem duas possibilidades, ACERTA ou ERRAR uma questão. 

# ### Qual a probabilidade de sucesso ($p$)?

# In[18]:


alternativas_por_questao = 3
p = 1/alternativas_por_questao
p


# ### Qual a probabilidade de fracasso ($q$)?

# In[19]:


q = 1 - p
q


# ### Qual o total de eventos que se deseja obter sucesso ($k$)?

# In[20]:


k = 5


# ### Solução 1

# In[23]:


probabilidade = (comb(n, k) * (p**k)*(q**(n-k)))
print('%0.8f'%probabilidade)


# ### Importando bibliotecas
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

# In[25]:


from scipy.stats import binom


# ### Solução 2

# In[27]:


probabilidade = binom.pmf(k, n, p)
print('%0.8f'%probabilidade)


# ### Obter a probabilidade do candidato passar

# ### $$P(acertar \geq 5) = P(5) + P(6) + P(7) + P(8) + P(9) + P10)$$

# In[28]:


probabilidade = binom.pmf(5, n, p)  + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)
probabilidade


# In[30]:


binom.pmf([5,6,7,8,9,10], n, p).sum()


# In[33]:


1 - binom.cdf(4, n, p)


# In[34]:


binom.sf(4,n,p)


# ## <font color='blue'>Exemplo: Gincana</font>

# Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. Na última gincana se sabe que a **proporção de participantes do sexo feminino foi de 60%**. **O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30**. Com as informações acima responda: Quantas equipes deverão ser formadas por **8 mulheres**?

# ### Solução

# In[37]:


p=0.6


# In[38]:


n=12


# In[39]:


k=8


# In[43]:


probabilidade = binom.pmf(k,n,p)
probabilidade


# In[44]:


30*probabilidade


# ---
# ---

# ## <font color=red>Problema</font>
# ***

# Um restaurante recebe em média **20 pedidos por hora**. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba **15 pedidos**?

# ## <font color=green>2.2 Distribuição Poisson</font>
# ***

# É empregada para descrever o número de ocorrências em um intervalo de tempo ou espaço específico. Os eventos são caracterizados pela possibilidade de contagem dos sucessos, mas a não possibilidade de contagem dos fracassos.
# 
# Como exemplos de processos onde podemos aplicar a distribuição de Poisson temos a determinação do número de clientes que entram em uma loja em determinada hora, o número de carros que chegam em um drive-thru de uma lanchonete na hora do almoço, a determinação do número de acidentes registrados em um trecho de estrada etc.

# # $$P(k) = \frac{e^{-\mu}(\mu)^k}{k!}$$
# 
# Onde:
# 
# $e$ = constante cujo valor aproximado é 2,718281828459045
# 
# $\mu$ = representa o número médio de ocorrências em um determinado intervalo de tempo ou espaço
# 
# $k$ = número de sucessos no intervalo desejado

# ### Experimento Poisson

# 1. A probabilidade de uma ocorrência é a mesma em todo o intervalo observado.
# 
# 2. O número de ocorrências em determinado intervalo é independente do número de ocorrências em outros intervalos.
# 
# 3. A probabilidade de uma ocorrência é a mesma em intervalos de igual comprimento.

# ### Média da distribuição Poisson

# # $$\mu$$

# ### Desvio padrão da distribuição Poisson

# # $$\sigma = \sqrt{\mu}$$

# ### Importando bibliotecas
# 
# http://www.numpy.org/

# In[45]:


import numpy as np


# In[46]:


np.e


# ## <font color='blue'>Exemplo: Delivery</font>

# Um restaurante recebe em média **20 pedidos por hora**. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba **15 pedidos**?

# ### Qual o número médio de ocorrências por hora ($\mu$)?

# In[47]:


media = 20


# ### Qual o número de ocorrências que queremos obter no período ($k$)?

# In[48]:


k = 15


# ### Solução 1

# In[49]:


probabilidade = ((np.e**(-media)) * (media**k)) / (np.math.factorial(k))
print('%0.8f'%probabilidade)


# ### Importando bibliotecas

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

# ### Solução 2

# In[51]:


from scipy.stats import poisson
probabilidade = poisson.pmf(k,media)
probabilidade


# ---
# ---

# ## <font color=red>Problema</font>
# ***

# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma **distribuição aproximadamente normal**, com **média 1,70** e **desvio padrão de 0,1**. Com estas informações obtenha o seguinte conjunto de probabilidades:
# 
# > **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
# 
# > **B.** probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    
# 
# > **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

# ## <font color=green>2.3 Distribuição Normal</font>
# ***

# A distribuição normal é uma das mais utilizadas em estatística. É uma distribuição contínua, onde a distribuição de frequências de uma variável quantitativa apresenta a forma de sino e é simétrica em relação a sua média.

# ![Normal](https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img001.png)

# ### Características importantes

# 1. É simétrica em torno da média;
# 
# 2. A área sob a curva corresponde à proporção 1 ou 100%;
# 
# 3. As medidas de tendência central (média, mediana e moda) apresentam o mesmo valor;
# 
# 4. Os extremos da curva tendem ao infinito em ambas as direções e, teoricamente, jamais tocam o eixo $x$;
# 
# 5. O desvio padrão define o achatamento e largura da distribuição. Curvas mais largas e mais achatadas apresentam valores maiores de desvio padrão;
# 
# 6. A distribuição é definida por sua média e desvio padrão;
# 
# 7. A probabilidade sempre será igual à área sob a curva, delimitada pelos limites inferior e superior.

# # $$f(x) = \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
# 
# Onde:
# 
# $x$ = variável normal
# 
# $\sigma$ = desvio padrão
# 
# $\mu$ = média

# A probabilidade é obtida a partir da área sob a curva, delimitada pelos limites inferior e superior especificados. Um exemplo pode ser visto na figura abaixo.

# ![alt text](https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img002.png)
# 

# Para obter a área acima basta calcular a integral da função para os intervalos determinados. Conforme equação abaixo:

# # $$P(L_i<x<L_s) = \int_{L_i}^{L_s}\frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
# 
# Onde:
# 
# $x$ = variável normal
# 
# $\sigma$ = desvio padrão
# 
# $\mu$ = média
# 
# $L_i$ = limite inferior
# 
# $L_s$ = limite superior

# ### Tabelas padronizadas

# As tabelas padronizadas foram criadas para facilitar a obtenção dos valores das áreas sob a curva normal e eliminar a necessidade de solucionar integrais definidas.
# 
# Para consultarmos os valores em uma tabela padronizada basta transformarmos nossa variável em uma variável padronizada $Z$.
# 
# Esta variável $Z$ representa o afastamento em desvios padrões de um valor da variável original em relação à média.

# # $$Z = \frac{x-\mu}{\sigma}$$
# 
# Onde:
# 
# $x$ = variável normal com média $\mu$ e desvio padrão $\sigma$
# 
# $\sigma$ = desvio padrão
# 
# $\mu$ = média

# ### Construindo tabela normal padronizada
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

# In[52]:


import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada


# <img src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img003.png' width='250px'>
# 
# A tabela acima fornece a área sob a curva entre $-\infty$ e $Z$ desvios padrão acima da média. Lembrando que por se tratar de valores padronizados temos $\mu = 0$.

# ## <font color='blue'>Exemplo: Qual sua altura?</font>

# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma **distribuição aproximadamente normal**, com **média 1,70** e **desvio padrão de 0,1**. Com estas informações obtenha o seguinte conjunto de probabilidades:
# 
# > **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
# 
# > **B.** probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    
# 
# > **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

# ### Problema A - Identificação da área sob a curva

# <img style='float: left' src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img004.png' width='350px'>

# ### Obter a variável padronizada $Z$

# In[53]:


media = 1.70


# In[56]:


desvio = 0.1


# In[64]:


Z_superior = (1.8 - media) / desvio
Z_superior


# ### Solução 1 - Utilizando tabela

# In[ ]:


probabilidade = 0.8413


# ### Solução 2 - Utilizando Scipy

# In[58]:


from scipy.stats import norm
norm.cdf(Z)


# ### Problema B - Identificação da área sob a curva

# <img style='float: left' src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img005.png' width='350px'>

# ### Obter a variável padronizada $Z$

# In[67]:


Z_inferior = (1.6 - media) / desvio
round(Z_inferior, 2)


# In[68]:


Z_superior = (1.8 - media) / desvio
round(Z_superior, 2)


# ### Solução 1 - Utilizando tabela

# In[63]:


probabilidade = (0.8413447460685431 - 0.5) * 2
probabilidade


# In[ ]:





# ### Solução 2 - Utilizando Scipy

# In[71]:


probabilidade = norm.cdf(Z_superior) - (1 - norm.cdf(Z_superior))
probabilidade


# In[72]:


probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
probabilidade


# ### Problema C - Identificação da área sob a curva

# <img style='float: left' src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img006.png' width='350px'>

# ### Obter a variável padronizada $Z$

# In[73]:


Z = (1.90 - media)/desvio
Z


# ### Solução 1 - Utilizando tabela

# In[76]:


probabilidade = 1 -0.9767
probabilidade


# ### Solução 2 - Utilizando Scipy

# In[77]:


probabilidade = norm.cdf(-Z)


# In[78]:


probabilidade


# # <font color=green>3 AMOSTRAGEM</font>
# ***

# ## <font color=green>3.1 População e Amostra</font>
# ***

# ### População
# Conjunto de todos os elementos de interesse em um estudo. Diversos elementos podem compor uma população, por exemplo: pessoas, idades, alturas, carros etc.
# 
# Com relação ao tamanho, as populações podem ser limitadas (populações finitas) ou ilimitadas (populações infinitas).

# ### Populações finitas
# 
# Permitem a contagem de seus elementos. Como exemplos temos o número de funcionário de uma empresa, a quantidade de alunos em uma escola etc.

# ### Populações infinitas
# 
# Não é possível contar seus elementos. Como exemplos temos a quantidade de porções que se pode extrair da água do mar para uma análise, temperatura medida em cada ponto de um território etc.
# 
# <font color=red>Quando os elementos de uma população puderem ser contados, porém apresentando uma quantidade muito grande, assume-se a população como infinita.</font>.

# ### Amostra
# Subconjunto representativo da população.

# Os atributos numéricos de uma população como sua média, variância e desvio padrão, são conhecidos como **parâmetros**. O principal foco da inferência estatística é justamente gerar estimativas e testar hipóteses sobre os parâmetros populacionais utilizando as informações de amostras.

# ## <font color=green>3.2 Quando utilizar uma amostra?</font>
# ***

# ### Populações infinitas
# 
# O estudo não chegaria nunca ao fim. Não é possível investigar todos os elementos da população.

# ### Testes destrutivos
# 
# Estudos onde os elementos avaliados são totalmente consumidos ou destruídos. Exemplo: testes de vida útil, testes de segurança contra colisões em automóveis.

# ### Resultados rápidos
# 
# Pesquisas que precisam de mais agilidade na divulgação. Exemplo: pesquisas de opinião, pesquisas que envolvam problemas de saúde pública.

# ### Custos elevados
# 
# Quando a população é finita mas muito numerosa, o custo de um censo pode tornar o processo inviável.

# ## <font color=green>3.3 Amostragem Aleatória Simples</font>
# ***

# É uma das principais maneiras de se extrair uma amostra de uma população. A exigência fundamental deste tipo de abordagem é que cada elemeto da população tenha as mesmas chances de ser selecionado para fazer parte da amostra.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## <font color=green>3.4 Amostragem Estratificada</font>
# ***

# É uma melhoria do processo de amostragem aleatória simples. Neste método é proposta a divisão da população em subgrupos de elementos com características similares, ou seja, grupos mais homogêneos. Com estes subgrupos separados, aplica-se a técnica de amostragem aleatória simples dentro de cada subgrupo individualmente.

# ## <font color=green>3.5 Amostragem por Conglomerados</font>
# ***

# Também visa melhorar o critério de amostragem aleatória simples. Na amostragem por conglomerados são também criados subgrupos, porém não serão homogêneas como na amostragem estratificada. Na amostragem por conglomerados os subgrupos serão heterogêneos, onde, em seguida, serão aplicadas a amostragem aleatória simples ou estratificada.
# 
# Um exemplo bastante comum de aplicação deste tipo de técnica é na divisão da população em grupos territoriais, onde os elementos investigados terão características bastante variadas.

# # <font color=green>4 ESTIMAÇÃO</font>
# ***

# ## <font color='red'>Problema </font>

# Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de **desvio padrão populacional igual a 150 g**. Selecionada uma **amostra aleatório de 20 sacos** de um lote específico, obteve-se um **peso médio de 5.050 g**. Construa um **intervalo de confiança para a média populacional** assumindo um **nível de significância de 5%**.

# ---

# É a forma de se fazer suposições generalizadas sobre os parâmetros de uma população tendo como base as informações de uma amostra.
# 
# - **Parâmetros** são os atributos numéricos de uma população, tal como a média, desvio padrão etc.
# 
# - **Estimativa** é o valor obtido para determinado parâmetro a partir dos dados de uma amostra da população.

# ## <font color=green>4.1 Teorema do limite central</font>
# ***

# > O **Teorema do Limite Central** afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal com média igual à média da população e desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. Este fato é assegurado para $n$ maior ou igual a 30.

# # $$\sigma_\bar{x} = \frac{\sigma}{\sqrt{n}}$$
# 
# O desvio padrão das médias amostrais é conhecido como **erro padrão da média**

# ### Entendendo o Teorema do Limite Central

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# > O Teorema do Limite Central afirma que, **com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal** com média igual à média da população e desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. Este fato é assegurado para n maior ou igual a 30.

# In[ ]:





# > O Teorema do Limite Central afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal **com média igual à média da população** e desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. Este fato é assegurado para n maior ou igual a 30.

# In[ ]:





# In[ ]:





# > O Teorema do Limite Central afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal com média igual à média da população e **desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra**. Este fato é assegurado para n maior ou igual a 30.
# 
# # $$\sigma_\bar{x} = \frac{\sigma}{\sqrt{n}}$$

# In[ ]:





# In[ ]:





# In[ ]:





# ## <font color=green>4.2 Níveis de confiança e significância</font>
# ***

# O **nível de confiança** ($1 - \alpha$) representa a probabilidade de acerto da estimativa. De forma complementar o **nível de significância** ($\alpha$) expressa a probabilidade de erro da estimativa.
# 
# O **nível de confiança** representa o grau de confiabilidade do resultado da estimativa estar dentro de determinado intervalo. Quando fixamos em uma pesquisa um **nível de confiança** de 95%, por exemplo, estamos assumindo que existe uma probabilidade de 95% dos resultados da pesquisa representarem bem a realidade, ou seja, estarem corretos.
# 
# O **nível de confiança** de uma estimativa pode ser obtido a partir da área sob a curva normal como ilustrado na figura abaixo.

# ![alt text](https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img007.png)

# ## <font color=green>4.3 Erro inferencial</font>
# ***

# O **erro inferencial** é definido pelo **desvio padrão das médias amostrais** $\sigma_\bar{x}$ e pelo **nível de confiança** determinado para o processo.

# # $$e = z \frac{\sigma}{\sqrt{n}}$$

# ## <font color=green>4.4 Intervalos de confiança</font>
# ***

# ### Intevalo de confiança para a média da população

# #### Com desvio padrão populacional conhecido
# 
# ## $$\mu = \bar{x} \pm z\frac{\sigma}{\sqrt{n}}$$
# 
# #### Com desvio padrão populacional desconhecido
# 
# ## $$\mu = \bar{x} \pm z\frac{s}{\sqrt{n}}$$

# ## <font color='blue'>Exemplo: </font>

# Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de **desvio padrão populacional igual a 150 g**. Selecionada uma **amostra aleatório de 20 sacos** de um lote específico, obteve-se um **peso médio de 5.050 g**. Construa um intervalo de confiança para a **média populacional** assumindo um **nível de significância de 5%**.

# ### Média amostral

# In[ ]:





# ### Nível de significância ($\alpha$)

# In[ ]:





# ### Nível de confiança ($1 - \alpha$)

# In[ ]:





# ### Obtendo $z$

# In[ ]:





# ### Obtendo $z$

# ![alt text](https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img008.png)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Valores de $z$ para os níveis de confiança mais utilizados
# 
# |Nível de<br>confiança|Valor da área sob<br>a curva normal| $z$ |
# |:----------------:|:---------------------------------:|:---:|
# |90%               |0,95                               |1,645|
# |95%               |0,975                              |1,96 |
# |99%               |0,995                              |2,575|

# ### Obtendo $\sigma_\bar{x}$

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Obtendo $e$

# In[ ]:





# ### Solução 1 - Calculando o intervalo de confiança para a média

# In[ ]:





# ### Solução 2 - Calculando o intervalo de confiança para a média

# In[ ]:





# # <font color=green>5 CÁLCULO DO TAMANHO DA AMOSTRA</font>
# ***

# ## <font color='red'>Problema </font>

# Estamos estudando o rendimento mensal dos chefes de domicílios com renda até R$\$$ 5.000,00 no Brasil. Nosso supervisor determinou que o **erro máximo em relação a média seja de R$\$$ 10,00**. Sabemos que o **desvio padrão populacional** deste grupo de trabalhadores é de **R$\$$ 1.082,79**. Para um **nível de confiança de 95%**, qual deve ser o tamanho da amostra de nosso estudo?

# ## <font color=green>5.1 Variáveis quantitativas e população infinita</font>
# ***

# # $$e = z \frac{\sigma}{\sqrt{n}}$$

# #### Com desvio padrão conhecido
# 
# ## $$n = \left(z\frac{\sigma}{e}\right)^2$$
# 
# #### Com desvio padrão desconhecido
# 
# ## $$n = \left(z\frac{s}{e}\right)^2$$
# 
# Onde:
# 
# $z$ = variável normal padronizada
# 
# $\sigma$ = desvio padrão populacional
# 
# $s$ = desvio padrão amostral
# 
# $e$ = erro inferencial

# ### <font color='red'>Observações</font>
# 
# 1. O desvio padrão ($\sigma$ ou $s$) e o erro ($e$) devem estar na mesma unidade de medida.
# 
# 2. Quando o erro ($e$) for representado em termos percentuais, deve ser interpretado como um percentual relacionado à média.

# ## <font color='blue'>Exemplo: Rendimento médio</font>

# Estamos estudando o rendimento mensal dos chefes de domicílios no Brasil. Nosso supervisor determinou que o **erro máximo em relação a média seja de R$\$$ 100,00**. Sabemos que o **desvio padrão populacional** deste grupo de trabalhadores é de **R$\$$ 3.323,39**. Para um **nível de confiança de 95%**, qual deve ser o tamanho da amostra de nosso estudo?

# In[ ]:





# In[ ]:





# In[ ]:





# ### Obtendo $\sigma$

# In[ ]:





# ### Obtendo $e$

# In[ ]:





# ### Obtendo $n$

# In[ ]:





# ---
# ---

# ## <font color='red'>Problema</font>

# Em um lote de **10.000 latas** de refrigerante foi realizada uma amostra aleatória simples de **100 latas** e foi obtido o **desvio padrão amostral do conteúdo das latas igual a 12 ml**. O fabricante estipula um **erro máximo sobre a média populacional de apenas 5 ml**. Para garantir um **nível de confiança de 95%** qual o tamanho de amostra deve ser selecionado para este estudo?

# ## <font color=green>5.2 Variáveis quantitativas e população finita</font>
# ***

# #### Com desvio padrão conhecido
# 
# ## $$n = \frac{z^2 \sigma^2 N}{z^2 \sigma^2 + e^2(N-1)}$$
# 
# #### Com desvio padrão desconhecido
# 
# ## $$n = \frac{z^2 s^2 N}{z^2 s^2 + e^2(N-1)}$$
# 
# Onde:
# 
# $N$ = tamanho da população
# 
# $z$ = variável normal padronizada
# 
# $\sigma$ = desvio padrão populacional
# 
# $s$ = desvio padrão amostral
# 
# $e$ = erro inferencial

# ## <font color='blue'>Exemplo: Indústria de refrigerantes</font>

# Em um lote de **10.000 latas** de refrigerante foi realizada uma amostra aleatória simples de **100 latas** e foi obtido o **desvio padrão amostral do conteúdo das latas igual a 12 ml**. O fabricante estipula um **erro máximo sobre a média populacional de apenas 5 ml**. Para garantir um **nível de confiança de 95%** qual o tamanho de amostra deve ser selecionado para este estudo?

# ### Obtendo $N$

# In[ ]:





# ### Obtendo $z$

# In[ ]:





# ### Obtendo $s$

# In[ ]:





# ### Obtendo $e$

# In[ ]:





# ### Obtendo $n$
# 
# ## $$n = \frac{z^2 s^2 N}{z^2 s^2 + e^2(N-1)}$$

# In[ ]:





# # <font color=green>6 FIXANDO O CONTEÚDO</font>
# ***

# ## <font color='blue'>Exemplo: Rendimento médio</font>

# Estamos estudando o **rendimento mensal dos chefes de domicílios com renda até R$\$$ 5.000,00 no Brasil**. Nosso supervisor determinou que o **erro máximo em relação a média seja de R$\$$ 10,00**. Sabemos que o **desvio padrão populacional** deste grupo de trabalhadores é de **R$\$$ 1.082,79** e que a **média populacional** é de **R$\$$ 1.426,54**. Para um **nível de confiança de 95%**, qual deve ser o tamanho da amostra de nosso estudo? Qual o intervalo de confiança para a média considerando o tamanho de amostra obtido?

# ### Construindo o dataset conforme especificado pelo problema

# In[ ]:





# In[ ]:





# In[ ]:





# ### Calculando o tamanho da amostra

# In[ ]:





# ### Calculando o intervalo de confiança para a média

# In[ ]:





# ### Realizando uma prova gráfica

# In[ ]:





# In[ ]:




