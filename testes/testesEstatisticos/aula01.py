#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd


# In[70]:


movies = pd.read_csv('movies.csv')


# In[71]:


tmdb5000 = pd.read_csv('tmdb_5000_movies.csv')


# In[72]:


rating = pd.read_csv('ratings.csv')


# In[ ]:





# In[73]:


import seaborn as sns
ax = sns.distplot(tmdb5000.vote_average, bins=30)
ax.set_title('Distribuição da média de votação', size=12)
ax.set_xlabel('Média de votação', size=10)
ax.set_ylabel('Densidade', size=10)


# In[74]:


import seaborn as sns
ax = sns.distplot(tmdb5000.vote_average, bins=30, norm_hist=False, kde=False)
ax.set_title('Distribuição da média de votação', size=12)
ax.set_xlabel('Média de votação', size=10)
ax.set_ylabel('Densidade', size=10)


# In[75]:


ax = sns.boxplot(tmdb5000.vote_average, width=0.3)
ax.set(xlabel='Média de votação')
ax


# In[76]:


tmdb5000_mais_de_10_votos = tmdb5000.query('vote_count >= 10')


# In[77]:


import seaborn as sns
ax = sns.distplot(tmdb5000_mais_de_10_votos
.vote_average, norm_hist=False)
ax.set_title('Distribuição da média de votação entre os filmes com 10 ou mais votos', size=12)
ax.set_xlabel('Média de votação', size=10)
ax.set_ylabel('Densidade', size=10)


# In[78]:


ax = sns.boxplot(tmdb5000_mais_de_10_votos.vote_average, width=0.3)
ax.set(xlabel='Média de votação dentre os filmes com 10 ou mais votos')
ax


# In[79]:


ratings = pd.read_csv('ratings.csv')


# In[80]:


nota_media_por_filme = ratings.groupby('movieId').mean().rating


# In[81]:


nota_media_por_filme.head()


# In[82]:


ax = sns.distplot(nota_media_por_filme.values, bins=50)
ax.set_title('Nota média por filmes no Movielens 100k', size=15)


# In[83]:


ratings.describe()


# In[84]:


ratings.query('rating == 5')


# In[85]:


quantidade_de_votos_por_filme = ratings.groupby('movieId').count()

filmes_com_pelo_menos_10_votos = quantidade_de_votos_por_filme.query('rating >= 10').index

filmes_com_pelo_menos_10_votos.values


# In[86]:


nota_media_por_filme_com_pelo_menos_10_votos= nota_media_por_filme.loc[filmes_com_pelo_menos_10_votos.values]
nota_media_por_filme.head()


# In[87]:


nota_media_por_filme_com_pelo_menos_10_votos.mean()


# In[88]:


ax = sns.distplot(nota_media_por_filme_com_pelo_menos_10_votos, bins=50)
ax.set_title('Nota média por filmes no Movielens 100k', size=15)


# In[89]:


ax = sns.boxplot(nota_media_por_filme_com_pelo_menos_10_votos, width=0.3)
ax.set_title('Nota média por filme')


# In[90]:


ax = sns.boxplot(nota_media_por_filme_com_pelo_menos_10_votos, width=0.3)
ax.set_title('Nota média por filme')
ax


# In[91]:


ax = sns.distplot(nota_media_por_filme_com_pelo_menos_10_votos, bins=50,
                    hist_kws = {'cumulative': True},
                    kde_kws = {'cumulative': True})
ax.set_title('Nota média por filmes no Movielens 100k', size=15)
ax.set_ylabel('% acumulada dos filmes')


# Analisando a distribuição dos dados capturados de outros campos

# In[92]:


ax = sns.distplot(tmdb5000_mais_de_10_votos.vote_count, bins=50)
ax.set_title('Nota média por filmes no TMDB com mais de 10 votos', size=15)


# In[93]:


tmdb_budget_maior_que_0 = tmdb5000.query('budget > 0').budget


# In[94]:


ax = sns.distplot(tmdb_budget_maior_que_0, bins=50)
ax.set_title('Budget nos filmes do tmdb', size=15)


# In[95]:


ax = sns.distplot(tmdb5000.popularity, bins=50)
ax.set_title('Popularidade nos filmes do TMDB', size=15)


# In[96]:


ax = sns.distplot(tmdb5000.runtime, bins=50)
ax.set_title('Tempo de duração dos filmes no TMDB', size=15)


# In[97]:


tmdb5000.runtime.isnull().sum()


# In[98]:


tmdb5000.runtime.dropna()


# In[99]:


ax = sns.distplot(tmdb5000.query('runtime > 0').runtime.dropna(), bins=50)
ax.set_title('Tempo de duração dos filmes no TMDB', size=15)


# In[100]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[101]:


medias = list()
np.random.seed(75243)
temp = nota_media_por_filme_com_pelo_menos_10_votos.sample(frac=1)

medias = [temp[0:i].mean() for i in range(1, len(temp))]


# In[102]:


plt.plot(medias)


# In[103]:


from statsmodels.stats.weightstats import zconfint


# In[104]:


zconfint


# In[105]:


zconfint(nota_media_por_filme_com_pelo_menos_10_votos)


# In[106]:


from statsmodels.stats.weightstats import DescrStatsW


# In[107]:


descr_todos_com_10_votos = DescrStatsW(nota_media_por_filme_com_pelo_menos_10_votos)

descr_todos_com_10_votos.tconfint_mean()


# In[108]:


filmes = pd.read_csv('movies.csv')


# In[109]:


filmes.query('movieId == 1')


# In[110]:


notas1 = ratings.query('movieId == 1')


# In[111]:


notas1.head()


# In[112]:


ax = sns.distplot(notas1.rating)
ax.set_title('Nota para Toy Story', size=15)


# In[113]:


ax = sns.boxplot(notas1.rating, width=0.3)
ax.set_title('Nota média do Toy Story')
ax


# In[114]:


notas1.rating.mean()


# In[115]:


zconfint(notas1.rating)


# In[116]:


from statsmodels.stats.weightstats import ztest


# In[117]:


ztest(notas1.rating, value=3.4320503405352603)


# In[118]:


nota_media_toy_story = notas1.rating.mean()


# In[119]:


np.random.seed(75241)
temp = notas1.sample(frac=1).rating

def calcula_teste(i):
    media = temp[0:i].mean()
    stat, p = ztest(temp[0:i], value = 3.4320503405352603)
    return (i, media, p)
    
medias_toy_story = np.array([calcula_teste(i) for i in range(1, len(temp))])


# In[120]:


plt.plot(medias_toy_story[:,0],medias_toy_story[:,1])
plt.plot(medias_toy_story[:,0], medias_toy_story[:,2])
plt.hlines(y=0.05, xmin=2, xmax=len(temp), colors='red')


# In[121]:


print(ztest(notas1.rating, ratings.rating))
zconfint(notas1.rating, ratings.rating)


# In[122]:


desc_de_todas_as_notas = DescrStatsW(ratings.rating)
desc_toy_story = DescrStatsW(notas1.rating)
comparacao = desc_de_todas_as_notas.get_compare(desc_toy_story)
comparacao.summary()


# In[123]:


import statsmodels as sm
sm.__version__


# In[124]:


bplot = plt.boxplot([notas1.rating, ratings.rating], labels=['Toy Story', 'Todos os filmes'], patch_artist=True)
plt.title('Distribuição das notas de acordo com os filmes')
bplot


# Comparar a média de dois filmes

# In[125]:


movies.query('movieId in [1, 593, 72226]')


# In[126]:


notas1 = ratings.query('movieId == 1')
notas593 = ratings.query('movieId == 593')
notas72226 = ratings.query('movieId == 72226')


# In[127]:


bplot = plt.boxplot([notas1.rating, notas593.rating, notas72226.rating], labels=['Toy Story', 'O silêncio dos inocentes', 'Fantástico mr.Fox'], patch_artist=True)
plt.title('Distribuição das notas de acordo com os filmes')
bplot


# In[128]:


bplot = sns.boxplot(x='movieId', y='rating', data=ratings.query('movieId in [1, 593, 72226]'), width=0.4)
bplot.set_xticklabels(['Toy Story', 'O silêncio dos inocentes', 'Fantástico mr.Fox'])


# In[129]:


desc_1 = DescrStatsW(notas1.rating)
desc_593 = DescrStatsW(notas593.rating)
comparacao = desc_1.get_compare(desc_593)
comparacao.summary()


# In[130]:


desc_72226 = DescrStatsW(notas72226.rating)
desc_593 = DescrStatsW(notas593.rating)
comparacao = desc_593.get_compare(desc_72226)
comparacao.summary(use_t=True)


# In[131]:


ratings.query('movieId in [1, 593, 72226]').groupby('movieId').count()


# In[134]:


from scipy.stats import normaltest

stat, p = normaltest(notas1.rating)
p


# In[135]:


from scipy.stats import ranksums


# In[138]:


_, p = ranksums(notas1.rating, notas593.rating)
p


# In[ ]:




