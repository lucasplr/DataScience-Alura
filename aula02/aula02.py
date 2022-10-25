# %%
import pandas as pd

notas = pd.read_csv('./aula0/ml-latest-small/ratings.csv')

movies = pd.read_csv('./aula0/ml-latest-small/movies.csv')

movies.head()

# %%
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

# %%
movies.columns = ["filmeId", "tituloId", "generos"]
movies['tituloId']

# %%
notas.query("filmeId==1").nota.mean()

# %%
medias_de_notas = notas.groupby("filmeId").mean().nota

medias_de_notas.head()

# %%
import matplotlib.pyplot as plt
plt.figure(figsize=(4,8))
plt.hist(medias_de_notas)
