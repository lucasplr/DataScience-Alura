#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')


# In[ ]:





# In[ ]:





# In[3]:


confirmed.head()


# In[4]:


deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')


# In[5]:


recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')


# In[6]:


confirmed.sample(20)


# In[7]:


confirmed.iloc[0]


# In[8]:


confirmed.set_index('Province/State').loc['Anhui']


# In[9]:


confirmed_by_country = confirmed.groupby('Country/Region').sum()


# In[10]:


confirmed_by_country.sample(10)


# In[11]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(10,5))
confirmed_by_country.loc['China'][2:].plot()
plt.title('Casos confirmados na China', size=16)
plt.xticks(size=12)
plt.yticks(size=12)


# In[12]:


new_cases_china = confirmed_by_country.loc['China'][2:].diff().dropna()


# In[13]:


plt.figure(figsize=(10,5))
new_cases_china.plot()

plt.title('Novos casos na China', size=16)
plt.xticks(size=14)
plt.yticks(size=14)


# In[14]:


new_cases_china_2 = confirmed_by_country.loc['China'][2:43].diff()


# In[15]:


plt.figure(figsize=(10,5))
new_cases_china_2.plot()

plt.title('Novos casos na China', size=16)
plt.xticks(size=14)
plt.yticks(size=14)


# In[16]:


last_date = "3/2/20"
confirmed_by_country[last_date]


# In[17]:


plt.figure(figsize=(10,5))
confirmed_by_country[last_date].plot(kind='pie')

plt.title('Novos casos na China', size=16)


# In[18]:


plt.figure(figsize=(10,5))
confirmed_by_country[last_date].sort_values(ascending=False)[1:10].plot(kind='bar')

plt.title('Confirmados por pais', size=16)
plt.xticks(size=14)
plt.yticks(size=14)


# In[19]:


deaths[last_date]


# In[20]:


def latest_by_country(data):
    return data.groupby('Country/Region').sum()[last_date]


# In[21]:


info = [latest_by_country(confirmed),
latest_by_country(deaths),
latest_by_country(recovered)]


# In[22]:


display(latest_by_country(confirmed))
display(latest_by_country(deaths))
display(latest_by_country(recovered))


# In[23]:


combined = pd.concat(info, axis=1)
combined.columns = ['Confirmed', 'Deaths', 'Recovered']
combined


# In[24]:


sum_up = combined.sum()
letality_rate_1 = sum_up.Deaths/sum_up.Confirmed
letality_rate_2 = sum_up.Deaths/(sum_up.Recovered + sum_up.Deaths)*100
print(letality_rate_1*100)
print(letality_rate_2*100)


# In[25]:


letality_rate_1 = combined.Deaths/combined.Confirmed *100
letality_rate_2 = combined.Deaths/(combined.Recovered + combined.Deaths) *100
combined['letality_rate_1'] = letality_rate_1
combined['letality_rate_2'] = letality_rate_2
combined.dropna().head()


# In[26]:


combined.sort_values("letality_rate_1", ascending=False)


# In[27]:


import seaborn as sns


# In[28]:


sns.scatterplot(x=combined.Confirmed, y=combined.letality_rate_1)


# In[29]:


combined_filtered = combined.query('Confirmed > 40')


# In[30]:


sns.scatterplot(x=combined_filtered.Confirmed, y=combined_filtered.letality_rate_1)


# In[31]:


sns.scatterplot(data = combined.query('Recovered > 40'), x='Confirmed', y='letality_rate_2')


# In[32]:


sns.distplot(combined.query('Confirmed > 40').letality_rate_1, kde=False, bins=10)


# In[33]:


combined.sort_values('letality_rate_1', ascending=False).query('Confirmed > 40').head(10)


# In[34]:


combined.sort_values('letality_rate_2', ascending=False).query('Recovered > 40').head(10)


# In[35]:


confirmed.head()


# In[36]:


def latest_by_country_at(data,date):
    return data.groupby('Country/Region').sum()[date]


# In[37]:


info = [latest_by_country_at(confirmed, '2/20/20'),
latest_by_country_at(deaths, '2/20/20'),
latest_by_country_at(recovered, '2/20/20')]


# In[38]:


combined_2 = pd.concat(info, axis=1)
combined_2.columns = ['Confirmed', 'Deaths', 'Recovered']

sum_up = combined_2.loc['China']
letality_rate_1 = sum_up.Deaths/sum_up.Confirmed
letality_rate_2 = sum_up.Deaths/(sum_up.Recovered + sum_up.Deaths)
print(letality_rate_1*100)
print(letality_rate_2*100)


# In[39]:


sum_up = combined_2.sum()
letality_rate_1 = sum_up.Deaths/sum_up.Confirmed
letality_rate_2 = sum_up.Deaths/(sum_up.Recovered + sum_up.Deaths)
print(letality_rate_1*100)
print(letality_rate_2*100)


# In[40]:


letality_rate_1 = combined.Deaths/combined.Confirmed *100
letality_rate_2 = combined.Deaths/(combined.Recovered + combined.Deaths) *100
combined['letality_rate_1'] = letality_rate_1
combined['letality_rate_2'] = letality_rate_2
combined.dropna().head()


# In[41]:


info = [latest_by_country_at(confirmed, '2/8/20'),
latest_by_country_at(deaths, '2/20/20'),
latest_by_country_at(recovered, '2/20/20')]

combined_12 = pd.concat(info, axis=1)
combined_12.columns = ['Confirmed', 'Deaths', 'Recovered']

sum_up = combined_12.loc['China']
letality_rate = sum_up.Deaths/sum_up.Confirmed
print(letality_rate*100)
display(sum_up)


# In[54]:


confirmed.set_index('Country/Region').loc['China'].sum().tail()


# In[78]:


is_china = confirmed['Country/Region'] == 'China'


# In[79]:


confirmed['is_china'] = is_china


# In[80]:


confirmed.groupby('is_china').sum()['3/2/20'].plot(kind='bar')


# In[ ]:





# In[71]:


confirme_by_china = confirmed.groupby('is_china').sum()


# In[87]:


import numpy as np

confirmed['is_china_label'] = np.where(confirmed['is_china'],'China', 'Others')


# In[90]:


confirmed['is_china_label'].tail()


# In[93]:


confirmed.groupby('is_china_label').sum()[last_date].plot(kind='pie')


# In[96]:


confirmed.groupby('is_china_label').sum()[last_date].plot(kind='pie')
plt.title(f'Casos confirmados até {last_date}')


# In[109]:


summed = confirmed.groupby('is_china_label').sum()
summed['delta'] = summed['3/2/20'] - summed['2/1/20']
summed['delta'].plot(kind='bar')

plt.title(f'Novos casos confirmados em {last_date}')


# In[110]:


summed


# In[ ]:





# In[117]:


summed.T[2:43].plot()


# In[121]:


differences = summed.T[2:43].diff()
differences.plot()


# In[128]:


cases = confirmed.groupby('is_china_label').sum()[last_date].loc['China']
estimated_population = 1437525528
incidence_ratio = cases/estimated_population
incidence_ratio * 100000


# In[141]:


population = pd.read_csv('population.csv')


# In[148]:


population.PopTotal = population.PopTotal*1000


# In[ ]:





# In[183]:


population_test = population.groupby('Location').sum()


# In[152]:


population_total = population.query('Time == 2019')[['Location', 'PopTotal']].set_index('Location')


# In[153]:


combined.join(population_total)


# In[226]:


population.query('Location.str.contains("United States of America") and Time == 2019', engine='python')


# In[154]:


combined.join(population_total).sort_values('Confirmed', ascending=False)


# In[179]:


population.query("Location.str.contains('Korea')", engine='python')


# In[227]:


def rename_location(location):
    if location == 'China (and dependencies)':
        return 'China'
    if location == 'Republic of Korea':
        return 'Korea, South'
    if location == 'Iran (Islamic Republic of)':
        return 'Iran'
    if location == 'United States of America (and dependencies)':
        return 'US'
    return location
population_total['location_for_who'] = population_total.index.map(rename_location)

population_total.query("location_for_who =='China'")
# In[228]:


population_total = population_total.set_index('location_for_who')
population_total.head()


# In[233]:


combined_expanded = combined.join(population_total).sort_values('Confirmed', ascending=False).dropna()


# In[235]:


combined_expanded


# In[266]:


combined_expanded['incidence_ratio'] = combined_expanded['Confirmed']/combined_expanded['PopTotal']*100000
combined_expanded['mortality_rate'] = combined_expanded['Deaths']/combined_expanded['PopTotal']*100000


# In[267]:


combined_expanded


# In[ ]:





# In[ ]:




