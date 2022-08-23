# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:23:52 2022

@author: DELL
"""

import re
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
 Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that 
    particular data. 
'''    

filenames=glob('baby/*.txt')

    
ssa_df_list = []

for file in filenames:
    temp_df = pd.read_csv(file, names = ['names','sex','count'])
    #extract the year from file
    year = int(re.findall('\d\d\d\d', file)[0])
    
    if year > 2010: #we need to collect data from 1880 to 2010 only
        break

    #add a new colum to temp_df with name year and write int(year)
    #adding a new column with default value as year
    #simple is    
    temp_df['year'] = year
    #now append temp_df to ssa_final_df
    ssa_df_list.append(temp_df)

'''
Concatinate all the data to form single dataframe 
    using pandas concat method.
'''
finaldf = pd.concat(ssa_df_list, axis = 0, ignore_index = True)    

'''
 Display the top 5 male and female baby names of 2010.
'''
female=finaldf[(finaldf["sex"]=="F") & (finaldf["year"]==2010)].head() 

male=finaldf[(finaldf["sex"]=="M") & (finaldf["year"]==2010)].head() 

'''
 Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas groupby method).
'''
grouped_multiple = finaldf.groupby(['year', 'sex']).agg({'count': ['sum']})

print(grouped_multiple)    

'''
 Plot the results of the above activity to show total births  by sex and year.
'''
grouped_multiple.plot(kind='bar')

grouped_multiple[0:6].plot(kind='bar')
































































