# %%
import pandas as pd

# %%
dados = pd.read_csv('./modulo2/data/aluguel.csv', sep=';')
dados.head()

# %%
classes = [0, 2, 4, 6, 100]

# %%
quartos = pd.cut(dados.Quartos, classes)

# %%
quartos.value_counts()

# %%
labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']

# %%
quartos = pd.cut(dados.Quartos, classes, labels= labels)

# %%
quartos

# %%
quartos = pd.cut(dados.Quartos, classes, labels= labels, include_lowest=True)

# %%
quartos.value_counts()

# %%



