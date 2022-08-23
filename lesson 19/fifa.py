# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:30:58 2022

@author: DELL
"""
'''
 1. read the data which is seprated by ;
'''
import pandas as pd

import matplotlib.pyplot as plt 

df=pd.read_csv("FIFA-21.csv",sep=";")

'''
 2. get the info of top 10 oldest players in FIFA-21
'''
old=df.sort_values('age',ascending=False)[['name', 'nationality','age', 'nationality','team']].head(10) 

'''
 3. get the info of top 10 players in FIFA 2021
'''
df.sort_values('hits',ascending=False)[['name', 'nationality','age', 'nationality','team']].head(10) 
 
'''
4. plot the bar graph of top 10 countries in FIFA-21
'''
plt.style.use('dark_background') 
df['nationality'].value_counts().head(10).plot.bar()
plt.title('players from top 10 countries in FIFA-21')
plt.xlabel('countries')
plt.ylabel('total players')
plt.show()


'''
  5. plot the pie graph of top 5 teams in FIFA-21
'''
team=df['team'].value_counts()
topteam = team.index[0:5]
count = team.values[0:5]
plt.pie(count, labels=topteam, autopct='%.2f%%')
plt.title('popular teams in FIFA-21')
plt.show()









































































