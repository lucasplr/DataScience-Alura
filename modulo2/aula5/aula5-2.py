# %%
import pandas as pd



# %%
import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

alunos = pd.DataFrame(alunos)
alunos

# %%
selecao = alunos.Aprovado == True
selecao

n1 = alunos[selecao].shape[0]
n1

# %%
selecao = (alunos.Sexo == "F") & (alunos.Aprovado == True)
selecao

n2 = alunos[selecao].shape[0]
n2

# %%
#Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos.

selecao = (alunos.Idade > 10) & (alunos.Idade < 20) | (alunos.Idade >= 40)
selecao

n3 = alunos[selecao].shape[0]
n3

# %%



