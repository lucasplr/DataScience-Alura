# %% [markdown]
# Relatório de Análise III

# %%
import pandas as pd

data = pd.read_csv('./modulo2/data/aluguel.csv', sep=';')

data.head()

# %%
list(data.Tipo.drop_duplicates())

# %%
residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']

# %%
residencial

# %%
data.head()

# %%
selecao = data.Tipo.isin(residencial)

# %%
dados_residencial = data[selecao]

dados_residencial

# %%
list(dados_residencial.Tipo.drop_duplicates())

# %%
dados_residencial.shape[0]

# %%
dados_residencial.index = range(dados_residencial.shape[0]) #cria o index

# %%
dados_residencial

# %% [markdown]
# Exportando a Base de Dados

# %%
dados_residencial.to_csv('./modulo2/data/aluguel_residencial.csv', sep=';')

# %%
dados_residencial_2 = pd.read_csv('./modulo2/data/aluguel_residencial.csv', sep=';')

# %%
dados_residencial_2

# %%
dados_residencial.to_csv('./modulo2/data/aluguel_residencial.csv', sep=';', index=False) #exportar dados

# %%
dados_residencial_2 = pd.read_csv('./modulo2/data/aluguel_residencial.csv', sep=';')

# %%
dados_residencial_2

# %%



