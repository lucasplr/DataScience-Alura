#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: blue; font-size: 34px; font-weight: bold;'> Planejamento de Experimentos 
# </h1>
# 

# # <font color='red' style='font-size: 30px;'>1.0 Introdução   </font>
# <hr style='border: 2px solid red;'>
# 
# 
# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>    
# <i> “Chamar um especialista em estatística depois que o experimento foi feito pode ser o mesmo que pedir para ele fazer um exame post-mortem. Talvez ele consiga dizer do que foi que o experimento morreu.”  </i>     
# </p>    
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: right; text-indent: 0px;'>    
#     <b>Sir Ronald Fisher</b>  
# 
# <hr>
# 
# 
# 
# 
# 

# # <font color='red' style='font-size: 30px;'> Introdução à análise de experimentos   </font>
# <hr style='border: 2px solid red;'>

# # <font color = 'purple'> Inserindo o experimento num Data Frame </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# ## Importando as bibliotecas 

# ### Pandas
# 
# https://pandas.pydata.org/

# In[172]:


import pandas as pd


# ### Numpy
# 
# http://www.numpy.org/

# In[173]:


import numpy as np


# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="red"> <b>Ensaios realizados na forma normalizada</b> 
# 
# 
# <img width='800px' src='figuras/Figura_2.png'>
# 
#  
#    
#    
#     

# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
# <font color="MidnightBlue"> Construindo uma matriz representando todos os ensaios realizados:
# 

# In[174]:


pip install pyDOE2


# ### pyDOE2
# 
# https://pypi.org/project/pyDOE2/

# In[175]:


import pyDOE2 as doe


# ## Costruindo um planejamento fatorial de 2²
# 

# In[176]:


ensaios = doe.ff2n(2)


# In[177]:


ensaios


# ## Incerindo o planejamento em um Data Frame

# In[178]:


experimento = pd.DataFrame(ensaios, columns = ['Farinha', 'Chocolate'])


# In[179]:


experimento


# ### Inserindo coluna com os resultados 

# In[180]:


experimento['Porcoes'] = [19,37,24,49]


# In[181]:


experimento


# <hr>
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="MidnightBlue"> <b>Conclusão:</b> Temos, por fim, nosso experimento representado por um <i>DataFrame</i> do Pandas. Usaremos este <i>DataFrame</i> para iniciarmos a análise do nosso experimento. 
#     
# <hr>   

# # <font color = 'purple'> Analisando graficamente o experimento   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# ###  Importando o Seaborn
# 
# https://seaborn.pydata.org

# In[182]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[183]:


# paletas -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
sns.set_palette('terrain')

# estilo -> white, dark, whitegrid, darkgrid, ticks
sns.set_style('darkgrid')


# ### Para a farinha

# In[184]:


ax1 = sns.lmplot(data=experimento, x='Farinha', y='Porcoes', ci=None, hue = 'Chocolate')

ax1.set(xticks = (-1,1))


# ### Para o chocolate

# In[185]:


ax2 = sns.lmplot(data=experimento, x='Chocolate', y='Porcoes', ci=None, hue='Farinha')
ax2.set(xticks = (-1,1))


# In[ ]:





# # <font color = 'purple'> Ajustando o modelo estatístico </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# <hr>
# 
# <img width='800px' src='figuras/Figura_3.png'>
# 
# <p style='margin: 30px 30px;'> 
# 
# <hr>
# 

# ### Bibliotecas  Stats Model
# 

# In[186]:


import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### .

# In[187]:


modelo = smf.ols(data = experimento, formula= 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')


# In[188]:


modelo_ajustado = modelo.fit()


# In[189]:


print(modelo_ajustado.summary())


# # <font color = 'purple'> Aumentando os Graus de liberdade  </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 
# 
# 
# <p style='margin: 30px 30px;'>     
#     
# 

# <hr>
# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="red"> <b>Replicatas no centro</b>
# 
# 
# <img width='800px' src='figuras/Figura_5.png'> 
# 
# 
# <p style='margin: 30px 30px;'> 
#     
#     
#  
#     
# 
#     
# <hr>    

# In[190]:


centro = np.array([[0,0,29],
                   [0,0,30],
                   [0,0,29],
                   [0,0,30]
])


# In[191]:


centro_dataframe = pd.DataFrame(centro, columns=['Farinha', 'Chocolate', 'Porcoes'], index=[4,5,6,7])


# In[192]:


centro_dataframe


# ### .

# In[193]:


experimento = experimento.append(centro_dataframe)


# In[194]:


experimento


# # <font color = 'purple'>  Análise de significância estatística   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# In[195]:


modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')


# In[196]:


modelo_ajustado = modelo.fit()


# In[197]:


print(modelo_ajustado.summary())


# <p style='margin: 200px 200px;'>    
# 
# 
# <hr>
# 
# 
#     
#  <img width='400px' src='figuras/Figura_6.png'> 
# 
# 
# <p style='margin: 30px 30px;'>    
# 
# <hr>
# 
# 
#  <img width='600px' src='figuras/Figura_7.png'> 
# 
# 
# <p style='margin: 30px 30px;'>        
#     
#     
#  <hr>   
#     
# 
#   
#  <img width='600px' src='figuras/Figura_10.png'> 
# 
# 
# <p style='margin: 30px 30px;'>       
#   
# <hr>        

# 
# # <font color = 'purple'> Teste de significância estatística usando o <b>t<b>    </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 
# 
# 
# 

# <hr>
# <img width='600px' src='figuras/Figura_11.png'> 
# 
# 
# <hr>
#   <p style='margin: 30px 30px;'>     
# <img width='900px' src='figuras/Figura_8.png'> 
# 
# 
# <hr>
# 
# 

# <p style='margin: 150px 150px;'>     
# <img width='1000px' src='figuras/Figura_20.png'
# 
# 
# 
# <hr>
# <p style='margin: 150px 150px;'>    

# In[198]:


t_valores = modelo_ajustado.tvalues


# In[199]:


t_valores


# In[200]:


nome = t_valores.index.tolist()


# In[201]:


nome


# ### .

# In[202]:


from scipy import stats


# ### .
# 

# In[203]:


distribuicao = stats.t(df = 4)


# In[204]:


distribuicao.ppf(q=1-0.025)


# In[205]:


limite = [distribuicao.ppf(q=1-0.025)]*len(nome)


# In[206]:


limite


# ### Plotando o gráfico 

# In[207]:


pareto = sns.barplot(x=t_valores, y=nome)

pareto.figure.set_size_inches(15,6)

pareto.tick_params(labelsize=20)

pareto.set_xlabel('t-valores', size=20)

pareto.plot(limite, nome, 'r')


# # <font color = 'purple'> Propondo um novo modelo   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 

# <hr>
# 
# <img width='800px' src='figuras/Figura_3.png'>
# 
# <p style='margin: 30px 30px;'> 
# 
# <hr>

# <p style='margin: 200px 200px;'>
# 
# 
# <hr>
# 
# <img width='600px' src='figuras/Figura_9.png'> 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
# 
# 
# <p style='margin: 30px 30px;'>
# 
#     
# <hr>    
# 

# In[208]:


modelo_2 = smf.ols(data=experimento, formula = 'Porcoes ~ Farinha+Chocolate')


# In[209]:


modelo_2_ajustado = modelo_2.fit()


# In[210]:


print(modelo_2_ajustado.summary())


# <hr>

# # <font color = 'purple'> Gráfico Padronizado de Pareto do novo modelo    </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 

# In[211]:


t_valores = modelo_2_ajustado.tvalues


# In[212]:


t_valores


# In[213]:


nome = t_valores.index.tolist()
nome


# In[214]:


distribuicao = stats.t(df=5)


# ### .

# In[215]:


distribuicao.ppf(q=1-0.025)


# In[216]:


limite = [distribuicao.ppf(1-0.025)]*len(nome)


# In[217]:


limite


# ### Plotando o gráfico

# In[218]:


pareto = sns.barplot(x=t_valores, y=nome)

pareto.figure.set_size_inches(15,6)

pareto.tick_params(labelsize=20)

pareto.set_xlabel('t-valores', size=20)

pareto.plot(limite, nome, 'r')


# <font color='red' style='font-size: 30px;'> Preditos por observados  </font>
# <hr style='border: 2px solid red;'>

# In[219]:


observado = experimento.Porcoes


# In[220]:


observado


# ### .

# In[221]:


predito = modelo_2_ajustado.predict()


# In[222]:


predito


# ### .

# In[223]:


import matplotlib.pyplot as plt


# In[224]:


fig = plt.figure(figsize=(10,5))
ax = fig.add_axes([0,0,1,1])

ax.set_xlabel('Predito', size=16)
ax.set_ylabel('Observado', size=16)

#linha de guia
x = np.linspace(start = 15, stop=50, num=10)

y = np.linspace(start = 15, stop = 50, num= 10)

ax.plot(x,y,'r')

#comparacao

ax.scatter(x=observado, y=predito)


# <hr>

# In[225]:


print(modelo_2_ajustado.summary())


# ### .

# # <font color = 'purple'> Explorando o modelo   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# In[226]:


parametros = modelo_2_ajustado.params


# In[227]:


parametros


# ### .

# ### Definindo a função

# In[228]:


def modelo_receita(x_f, x_c):
    
    limite_normalizado = [-1,+1]
    
    limite_farinha = [0.5, 1.5]
    
    limite_chocolate = [0.1, 0.5]
    
    #converter - interpolar
    
    x_f_convertido = np.interp(x_f, limite_farinha, limite_normalizado)

    x_c_convertido = np.interp(x_c, limite_chocolate, limite_normalizado)
    
    porcoes = parametros['Intercept'] + parametros['Farinha']*x_f_convertido + parametros['Chocolate']*x_c_convertido
    
    return round(porcoes)


# In[229]:


modelo_receita(5,0.1)


# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='700px' src='figuras/Figura_22.png'> 
# 
# 
# <hr>

# # <font color = 'purple'> Mapa de cores   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='700px' src='figuras/Figura_23.jpg'> 
# 
# #### Fonte: National Centers for Environmental Prediction
# 
# 
# <hr>
# 
# 
# 
# <p style='margin: 50px 50px;'>
# 

# 
# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='600px' src='figuras/Figura_24.png'> 
# 
# 
# <hr>
# 
# 
# 
# <p style='margin: 30px 30px;'>

# In[230]:


x_farinha = np.linspace(start = 0.5, stop = 1.5, num = 10)


# In[231]:


x_farinha


# ### . 

# In[232]:


x_chocolate = np.linspace(start = 0.1, stop=0.5, num = 10)


# In[233]:


x_chocolate


# In[234]:


x_farinha_chocolate_data = []

for i in x_farinha:
    temp = []
    for j in x_chocolate:
        temp.append(modelo_receita(i,j))
    x_farinha_chocolate_data.append(temp)
    

x_farinha_chocolate_data


# ### .

# ### Construindo a superfície de resposta

# In[235]:


import matplotlib.cm as cm


# https://matplotlib.org/users/colormaps.html

# In[245]:


fig = plt.figure(figsize=(16,6))

heat_map = fig.add_axes([0,0,1,1])

heat_map.set_xlabel('Farinha (kg)', size=16)
heat_map.set_ylabel('Chocolate (kg)', size=16)


heat_map = plt.imshow(x_farinha_chocolate_data, origin = 'lower', cmap = cm.rainbow, interpolation = 'quadric', extent = (0.5,1.5, 0.1,0.5))

plt.colorbar().set_label('Porcoes', size=16)

#linha 
linhas = plt.contour(x_farinha, x_chocolate, x_farinha_chocolate_data, colors = 'k',
                    linewidths = 1.5)
plt.clabel(linhas, inline=True, fontsize=15, inline_spacing=10, fmt='%1.0f')


# In[ ]:





# In[ ]:




