# %% [markdown]
# Relatório de Análise IV

# %%
import pandas as pd

data = pd.read_csv('./modulo2//data/aluguel_residencial.csv', sep=';')
data

# %%
data.columns.name = "índice"
data

# %%
selecao = data.Tipo == "Apartamento"

n1 = data[selecao].shape[0]
n1


# %%
selecao = (data.Tipo == "Casa") | (data.Tipo == "Casa de Condominio") | (data.Tipo == "Casa de Vila") #mais de um termo necessita parenteses

n2 = data[selecao].shape[0]
n2


# %%
selecao = (data.Area >= 60) & (data.Area <= 100)
selecao

n3 = data[selecao].shape[0]
n3

# %%
selecao = (data.Quartos >= 4) & (data.Valor < 2000)
selecao

n4 = data[selecao].shape[0]
n4



