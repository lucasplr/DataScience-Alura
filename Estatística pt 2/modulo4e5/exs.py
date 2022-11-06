#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.special import comb


# In[2]:


comb(25,20)


# In[4]:


prob = 1/53130
print('%0.15f'%prob)


# In[5]:


from scipy.special import comb


# In[6]:


comb(4,2)


# In[7]:


from scipy.stats import binom


# In[20]:


p = 1/2


# In[21]:


k = 2


# In[22]:


n = 4


# In[24]:


binom.pmf(k,n,p)


# In[25]:


p=1/6


# In[32]:


k=2


# In[33]:


n=10


# In[34]:


binom.sf(k,n,p)


# In[35]:


p=0.22


# In[36]:


n=3


# In[37]:


k=2


# In[39]:


probabilidade = binom.pmf(k,n,p)


# In[40]:


50*probabilidade


# In[42]:


media = 20


# In[43]:


k = 25


# In[41]:


from scipy.stats import poisson


# In[44]:


probabilidade = poisson.pmf(k, media)
probabilidade


# In[45]:


media = 70


# In[46]:


desvio = 5


# In[47]:


z = (85-70)/5


# In[49]:


from scipy.stats import norm
norm.cdf(z)


# In[50]:


Z_superior = (350 - 300)/50


# In[53]:


Z_inferior = (250-300)/50


# In[54]:


probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
probabilidade


# In[58]:


Z_superior = (500 - 300)/50


# In[59]:


Z_inferior = (400-300)/50


# In[60]:


probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
probabilidade


# In[61]:


Z_superior= (750 - 720)/30


# In[62]:


Z_inferior = (650-720)/30


# In[63]:


probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
probabilidade


# In[77]:


Z = (800-720)/30


# In[78]:


probabilidade = norm.cdf(-Z)
probabilidade


# In[79]:


Z = (700-720)/30


# In[80]:


probabilidade = norm.cdf(-Z)
probabilidade


# In[87]:


probabilidade = norm.cdf(-0.78)
probabilidade


# In[88]:


desvio_padrao = 6


# In[89]:


n = 50


# In[90]:


z = 1.96


# In[91]:


import numpy as np


# In[92]:


sigma = (desvio_padrao/(np.sqrt(n)))
sigma


# In[94]:


e = z*sigma
e


# In[ ]:





# In[95]:


n = 1976


# In[96]:


desvio_padrao = 11


# In[97]:


media_amostral = 28


# In[102]:


z = 1.645


# In[103]:


sigma = (desvio_padrao/np.sqrt(n))
sigma


# In[105]:


e = z*sigma
e


# In[107]:


confianca = (
    media_amostral - e,
    media_amostral + e
)
confianca


# In[108]:


norm.interval(alpha = 0.90, loc=media_amostral, scale=sigma)


# In[ ]:




