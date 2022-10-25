import pandas as pd

notas = pd.read_csv('./aula0/ml-latest-small/ratings.csv')

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]



print(notas['nota'].mean())