# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:17:50 2022

@author: DELL
"""

'''
1. Drop the columns with axis=1;axis=0 is for rows
'''
import pandas as pd

df=pd.read_csv("pokemon.csv")

df=df.drop(["#"],axis=1)

'''
2. The index of Mega Pokemons contained extra and unneeded text. Removed all the text before "Mega"  
'''
df=df['Name'].str.replace(r'.*(?=Mega)', '')
df

'''
3. Some index seems to have duplicates in the front of the name for example, Hoopa is the right name, not HoopaHoopa,replace with sile occurance
'''
df.tail()
import re
df = df["Name"].apply(lambda x: re.sub(r'(HoopaHoopa)(.+)','Hoopa'+r'\2',x))
df.tail()

'''
 4. Filtering pokemons type that Typle 1 and Type 2 contain only combination of Fire and Dragon
'''

df[((df['Type 1']=='Fire') | (df['Type 1']=='Dragon')) & ((df['Type 2']=='Dragon') | (df['Type 2']=='Fire'))].head(3)

'''
 5. Get the First Generation Legendary Pokemons
'''
df_leg =df[df['Legendary']==True]
df_leg_1 = df_leg[df_leg['Generation'] == 1]
df_leg_1 

'''
 6. Make bar graph of the biggest combinations by combining Type 1 and type 2 between the types of Pokemon?
'''

import matplotlib.pyplot as plt
df1 =  pd.read_csv('Pokemon.csv')
df1['Type 1-2'] = df1['Type 1']+ '-' + df1['Type 2']
df2=df1['Type 1-2'].value_counts().head(10)
df2.plot(kind='bar')
plt.title("Total number of Pokemons types")
plt.xlabel("Types of Pokemon")
plt.ylabel("Total count of Pokemons types") 


'''
 7. Make Pie chart for see the Legendary pokemon distribution
 '''
plt.figure(figsize = (12,8))
x= df.Legendary.value_counts()
labels=["Non legendary","Legendary"]
plt.pie(x,labels= labels,autopct= "%1.1f%%")
plt.show() 































































