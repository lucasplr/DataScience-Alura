# %% [markdown]
# Relatório de Análise II

# %%
import pandas as pd

data = pd.read_csv('./modulo2/data/aluguel.csv', sep=';') 

data.head()

# %%
data.columns.name = "Index"

data.head()

# %%


# %%
tipo_de_imovel = data.Tipo

tipo_de_imovel

# %%
tipo_de_imovel.drop_duplicates()

# %%
tipo_de_imovel.drop_duplicates(inplace=True)

# %%
tipo_de_imovel

# %% [markdown]
# Organizando a visualização

# %%
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
tipo_de_imovel.columns.name = "Index"

# %%
tipo_de_imovel

# %%
tipo_de_imovel.index

# %%
tipo_de_imovel.shape[0]

# %%
range(tipo_de_imovel.shape[0])

# %%
for i in range(tipo_de_imovel.shape[0]):
    print(i)

# %%
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])

# %%
tipo_de_imovel.index

# %%
tipo_de_imovel

# %%



