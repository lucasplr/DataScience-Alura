# %% [markdown]
# 

# %% [markdown]
# # Relatório de Análise |

# %% [markdown]
# ## Importando a Base de Dados

# %%
import pandas as pd

aluguel = pd.read_csv('./modulo2/data/aluguel.csv', sep=';')

print(aluguel)

# %%
aluguel.head()

# %%
aluguel.info()

# %% [markdown]
# ## Informações gerais sobre a Base de Dados

# %%
aluguel.dtypes

# %%
tipos_de_dados = pd.DataFrame(aluguel.dtypes, columns = ['Tipos de dados'])

# %%
tipos_de_dados.columns.name = "Váriaveis"
tipos_de_dados

# %%
aluguel.shape

# %%
aluguel.shape[0]
aluguel.shape[1]

print(f'A base de dados apresenta {aluguel.shape[0]} registros e {aluguel.shape[1]} variáveis')


