# %% [markdown]
# Series

# %%
import pandas as pd

# %%
data = [1, 2, 3, 4, 5]

s = pd.Series(data)

s

# %%
index = ['Linha' + str(i) for i in range(5)]

index

# %%
s = pd.Series(data = data, index= index)

s

# %%
s1 = s + 2
s1

# %%
s2 = s1 + s
s2

# %%
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# %%
data

# %%
df1 = pd.DataFrame(data)

df1

# %%
index = ['Linha' + str(i) for i in range(3)]

# %%
index

# %%
df1 = pd.DataFrame(data = data, index = index)

# %%
df1

# %%
columns = ['Coluna' + str(i) for i in range(3)]

# %%
columns

# %%
df1 = pd.DataFrame(data = data, index= index, columns = columns)
df1

# %%
#dados = [[1, 2, 3], [4, 5, 6]]
#index = 'X,Y'.split(',')
#columns = list('CBA')[::-1]
#df = pd.DataFrame(dados, index, columns)
#df


