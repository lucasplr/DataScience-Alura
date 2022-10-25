# %%
import pandas as pd

tmdb = pd.read_csv('./tmdb_5000/tmdb_5000_movies.csv')

tmdb.head()

# %%

contagem_de_lingas = tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingas.columns = ["original_language", "total"]
contagem_de_lingas.head()

# %%
import seaborn as sns
#data = contagem_de_lingas)
sns.catplot(x="original_language", kind="count", data=tmdb)

# %% [markdown]
# 

# %%
total_por_lingua = tmdb.original_language.value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

# %% [markdown]
# 

# %%
dados = {
    "lingua": ['ingles', 'outros'],
    "total": [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)
sns.barplot(x+"lingua", y="total", data=dados)

# %%
total_por_linguas_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()

total_por_linguas_de_outros_filmes

# %%
import seaborn as sns

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")

sns.catplot(x="original_language", kind="count", data= filmes_sem_lingua_original_em_ingles)


