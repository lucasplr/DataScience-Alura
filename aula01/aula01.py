# %%
import pandas as pd
pd.read_csv('./aula0/ml-latest-small/ratings.csv')

# %%
notas = pd.read_csv('./aula0/ml-latest-small/ratings.csv')

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]

notas['nota']

# %%
notas.nota.head()

# %%
notas.nota.plot(kind='hist')

# %%
notas.nota.describe()

# %%
import seaborn as sns

sns.boxplot(notas.nota)

