# %%
import pandas as pd

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])

imoveis

# %%
imoveis.dropna(subset = "Valor", inplace=
True)

imoveis

# %%
selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
imoveis = imoveis[~selecao]
imoveis

# %%
imoveis = imoveis.fillna({'Condominio': 0, 'IPTU': 0})
imoveis

# %%
imoveis.index = range(imoveis.shape[0])
imoveis

# %% [markdown]
# 

# %%



