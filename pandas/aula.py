#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')


# In[3]:


nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')


# In[4]:


np.random.seed(123)


# In[5]:


frames = [nomes_f, nomes_m]


# In[6]:


nomes = pd.concat(frames)['nome'].to_frame()


# In[7]:


nomes.head()


# In[8]:


total_alunos = len(nomes)


# In[9]:


nomes['id_aluno'] = np.random.permutation(total_alunos)+1


# In[10]:


dominios = ['@gmail.com', '@hotmail.com']


# In[11]:


nomes['dominio'] = np.random.choice(dominios, total_alunos)


# In[12]:


nomes.head()


# In[13]:


nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()


# In[14]:


nomes.head()


# Criando a tabela Cursos

# In[15]:


#pip install html5lib


# In[16]:


#pip install lxml


# In[17]:


link = 'http://tabela-cursos.herokuapp.com/index.html'


# In[18]:


cursos = pd.read_html(link)


# In[19]:


cursos = cursos[0]


# In[20]:


cursos.head()


# In[21]:


cursos = cursos.rename(columns={'Nome do curso': 'Curso'})


# In[22]:


cursos['id'] = cursos.index + 1


# In[23]:


cursos = cursos.set_index('id')


# In[ ]:





# Matriculando alunos nos cursos

# In[24]:


nomes['matriculas'] = np.ceil(np.random.exponential(size=total_alunos) * 1.5).astype(int)


# In[25]:


nomes


# In[26]:


import seaborn as sns


# In[27]:


sns.distplot(nomes.matriculas, kde=False)


# In[28]:


nomes.matriculas.value_counts()


# Selecionando cursos

# In[29]:


todas_matriculas = []
x = np.random.rand(20)
prob = x / sum(x)


# In[30]:


for index, row in nomes.iterrows():
    id= row.id_aluno
    matriculas = row.matriculas
    for i in range(matriculas):
        mat = [id, np.random.choice(cursos.index, p=prob)]
        todas_matriculas.append(mat)

matriculas = pd.DataFrame(todas_matriculas, columns = ['id_aluno', 'id_curso'])


# In[31]:


matriculas.head()


# In[32]:


matriculas_por_curso = matriculas.groupby('id_curso').count().join(cursos['Curso']).rename(columns={'id_aluno': 'alunos_matriculados'})
matriculas_por_curso.head()


# Saida em diferentes formatos

# In[33]:


matriculas_por_curso.to_csv('matriculas_por_curso.csv', index=False)


# Criando banco SQL

# In[34]:


get_ipython().system('pip install sqlalchemy')


# In[35]:


from sqlalchemy import create_engine, MetaData, Table


# In[36]:


engine = create_engine('sqlite:///:memory:')


# In[37]:


engine


# In[38]:


matriculas_por_curso.to_sql('matriculas', engine)


# In[39]:


print(engine.table_names())


# Buscando no banco SQL

# In[40]:


query = 'select * from matriculas where alunos_matriculados < 200'


# In[41]:


pd.read_sql(query, engine)


# In[42]:


pd.read_sql_table('matriculas', engine, columns=['Curso', 'alunos_matriculados'])


# In[43]:


muitas_matriculas = pd.read_sql_table('matriculas', engine, columns=['Curso', 'alunos_matriculados'])


# In[44]:


muitas_matriculas.query('alunos_matriculados < 70')


# Escrevendo no banco

# In[45]:


muitas_matriculas.to_sql('muitas_matriculas', con=engine)


# In[46]:


print(engine.table_names())


# Nomes dos alunos da proxima turma

# In[51]:


matriculas_por_curso.head()


# In[52]:


id_curso = 16


# In[54]:


proxima_turma = matriculas.query(f'id_curso == {id_curso}')


# In[55]:


proxima_turma


# In[56]:


proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))


# In[57]:


proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome']


# In[59]:


proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome'].to_frame()


# In[67]:


nome_curso = cursos.loc[id_curso]
nome_curso = nome_curso.Curso
nome_curso


# In[68]:


proxima_turma = proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome'].to_frame()


# In[70]:


proxima_turma = proxima_turma.rename(columns = {'nome': f'Alunos do curso de {nome_curso}'})


# Excel

# In[71]:


proxima_turma.to_excel('proxima_turma.xlsx', index=False)


# In[ ]:




