# %%
import pandas as pd

# %%
data = pd.read_csv('./modulo2/data/aluguel_residencial.csv', sep=';', index_col=False)

data

# %%
data.Valor.mean()

# %%
bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']

#data.Bairro.isin(bairros)

selecao = data.Bairro.isin(bairros)

data = data[selecao]

data

# %%
data.Bairro.drop_duplicates()

# %%
grupo_bairro = data.groupby('Bairro')

# %%
for bairro, data in grupo_bairro:
    print(f'{bairro} -> {data.Valor.mean()}')

# %%
grupo_bairro.Valor.mean()

# %%



