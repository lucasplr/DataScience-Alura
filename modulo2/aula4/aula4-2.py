# %%
import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]

data

# %%
df = pd.DataFrame(data, list('321'), list('ZYX')) #list da nome as linhas e colunas

df

# %%
df.sort_index(inplace=True)

# %%
df

# %%
df.sort_index(inplace=True, axis=1)

# %%
df 

# %%
df.sort_values(by= 'X', inplace=True)

# %%
df

# %%
df.sort_values(by='3',  axis=1,inplace=True)

# %%
df

# %%
new_data = [[1,2,3], [4,5,6], [7,8,9]]
new_data

# %%
new_data = pd.DataFrame(new_data, list('321'), list('ZYX'))
new_data

# %%
new_data.sort_index(inplace=True)
new_data

# %%
new_data.sort_index(inplace=True, axis=1)
new_data

# %%
new_data.sort_values(by='X', inplace=True)
new_data

# %%
new_data.sort_values(by='3', axis=1, inplace=True)
new_data

# %%
new_data.sort_index(axis=1, inplace=True)
new_data


# %%



