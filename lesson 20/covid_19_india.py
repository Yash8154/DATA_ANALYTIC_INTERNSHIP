# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:01:19 2022

@author: DELL
"""

'''
 1. display first 5 rows from COVID-19 dataset also print the dataset info
'''
import pandas as pd

df=pd.read_csv("covid_19_india.csv") 

df.head()

print(df.info())

'''
 2. get the latest number of confirmed, deaths, recovered and active cases of covid 19 statewise
'''
df['Active'] = df['Confirmed'] -df['Deaths'] - df['Cured']
result = df.groupby('State/UnionTerritory')['Confirmed', 'Deaths', 'Cured', 'Active'].sum().reset_index()
print(result) 
 

'''
  3. list states with no cases of covid 19 cured
'''
cured = df.groupby('State/UnionTerritory')['Confirmed', 'Deaths', 'Cured', 'Active'].sum().reset_index()
result = cured[cured['Cured']==0][['State/UnionTerritory', 'Confirmed', 'Deaths', 'Cured','Active']]
print(result)


'''
  4. make a pie chart for top 5 state of covid 19 deathwise
'''
import matplotlib.pyplot as plt
series = df.groupby("State/UnionTerritory")["Deaths"].sum().sort_values(ascending=False)
topState = series.index[0:5]
Count = series.values[0:5]
plt.pie(Count, labels=topState, autopct='%.2f%%')
plt.show()






















































