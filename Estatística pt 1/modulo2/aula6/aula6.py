# %% [markdown]
# Relatório de Análise V

# %%
import pandas as pd 

dados = pd.read_csv('./modulo2/data/aluguel_residencial.csv', sep=';')

# %%
dados.columns.name = 'índice'
dados

# %%
dados.isnull()

# %%
dados[dados["Valor"].isnull()]

# %%
A = dados.shape[0]

dados.dropna(subset = ['Valor'], inplace=True) ##remove valores nulos

B = dados.shape[0]

A - B

# %%
dados[dados["Valor"].isnull()]

# %% [markdown]
# Tratamento de Dados Faltantes

# %%
dados[dados['Condominio'].isnull()].shape[0]

# %%
selecao = (dados.Tipo == "Apartamento") & (dados.Condominio.isnull())
selecao

# %%
A = dados.shape[0]

dados = dados[~selecao] #inverte o booleano
#A = dados.shape[0]
#dados.dropna(subset = ['Condominio'], inplace=True) ##remove valores nulos

#dados.dropna(subset = ['Condominio'], inplace=True)

B = dados.shape[0]

A - B


# %%
dados[dados.Condominio.isnull()].shape[0]

# %%
#dados.fillna(0, inplace=True)
dados = dados.fillna({'Condominio': 0, "IPTU": 0}) #substitui o NaN por 0, para preencher todos os campos


# %%
dados[dados.Condominio.isnull()].shape[0]

# %%
dados[dados.IPTU.isnull()].shape[0]

# %%
dados.info()

# %%
dados.to_csv('./modulo2/data/aluguel_residencial.csv', sep=';', index=False)

# %%



