# %% [markdown]
# Relatório de Análise VI

# %% [markdown]
# Criano Novas Variáveis

# %%
import pandas as pd

# %%
data = pd.read_csv('./modulo2/data/aluguel_residencial.csv', sep=';')
data

# %%
data['Valor Bruto'] = data.Valor + data.Condominio + data.IPTU


# %%
data['Valor m2'] = data.Valor / data.Area

# %%
data.head()

# %%
data['Valor m2'] = data['Valor m2'].round(2)

# %%
data

# %%
data['Valor Bruto m2'] = (data['Valor Bruto'] / data['Valor m2']).round(2)

# %%
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

# %%
data['Tipo Agregado'] = data.Tipo.apply(lambda x: 'Casa' if x in casa else 'Apartamento')

# %%
data

# %%
dados_aux = pd.DataFrame(data[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])

# %%
dados_aux

# %%
dados_aux

# %%
dados_aux.pop('Valor Bruto m2')

# %%
dados_aux

# %%
data.drop(['Valor Bruto', 'Valor Bruto m2'], axis=1, inplace=True)

# %%
data

# %%
data.to_csv('./modulo2/data/aluguel_residencial.csv', sep=';')

# %%
dados = pd.read_csv('./modulo2/data/aluguel.csv', sep=';')

# %%
dados.Tipo.unique()

# %%
dados.Tipo.value_counts()

# %%



