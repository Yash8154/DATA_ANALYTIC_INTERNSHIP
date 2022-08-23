# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:02:26 2022

@author: DELL
"""

'''
1. Handle the missing values for Price column
'''

import pandas as pd

df=pd.read_csv("Automobile.csv")

df['price']=df['price'].fillna(df['price'].mean())

'''
 2. Get the values from Price column into a numpy.ndarray
'''
 
array_price=df['price'].values

'''
 3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
'''
min_price=df['price'].min()
max_price=df['price'].max()
avg_price=df['price'].mean() 
std_price=df['price'].std()

'''
 4. Make a pie chart for all car makers
'''
import matplotlib.pyplot as plt

car_maker_name=df["make"].value_counts()

maker_name=car_maker_name.index[0:5]

no_of_car=car_maker_name.values[0:5]

apart=(0,0,0,0.1,0.1)

plt.pie(no_of_car,explode=apart,labels=maker_name,autopct='%.2f%%')

plt.show()








































































