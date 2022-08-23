# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 14:50:47 2022

@author: DELL
"""

'''
Encoding of the dataset is in Windows 1252 so it should be specified while loading it
'''
import pandas as pd

df=pd.read_csv("thanksgiving.csv", encoding="Windows 1252")


'''
# Fetching the columns name for further reference
'''
column_name=df.columns.tolist()
print(column_name)

'''
 # Initializing a code number for each column name
'''
column_number=[]
for i in range(65):
    column_number.append(i)
print(column_number)    

'''
# Storing the column name with their codes for further reference
'''
columns_names_code_mapping = dict(zip(column_number, column_name))

'''
# Initializing the dataframe with the codes of the column
'''
df.columns = column_number


'''
# Fetching the data of the people who perform thanksgiving.
'''
thanksgiving_perform=df[df[1]=='Yes']

'''
#check for missing values
'''
df.isnull().any(axis = 0)

'''
# Filling out the nan values with 'Missing' keyword
'''
df=df.fillna("Missing")


'''

# Analysing for the state/region, area  and income based what is consumed in thankgiving dinner

'''
region_based = df.groupby(64)
print (region_based.groups)
print (region_based.size())


area=df.groupby(60)
print(area.groups)
print(area.size())

income=df.groupby(63)
print(income.groups)
print(income.size())

'''

# Analysis of the sauces prefered by each incomes group people
'''
sauce_type_per_income_group = df.groupby(8)[63].value_counts()

print (sauce_type_per_income_group)

'''

#What is your gender? convert column to numeric values. 
#We’ll assign 0 to Male, and 1 to Female. 

'''
def gender_filter(value):
    if value == "Male":
        value = 0
    elif value == "Female":
        value = 1

    return value

df[62] = df[62].apply(gender_filter)
print (df[62].value_counts())

'''
#income cleanup
'''
import re
df[63] = df[63].replace(['Prefer not to answer', 'Missing'],['0','0'])

regex = re.compile("\d+\W*\d+")

'''
# A function to be passed in .apply() method for filtering out the salaries
'''

def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)

'''
# Using the apply method to filter the income column

'''

df[63] = df[63].apply(income_filter)

'''
# Fetching the average incomes for each type sauces

'''


income_by_sauce_type = df.groupby(8)[63]

print (income_by_sauce_type.groups)

avg_income_by_sauce_type = income_by_sauce_type.mean()

print (avg_income_by_sauce_type)

'''
# Visualizing the average income of the various sauces

'''
import matplotlib.pyplot as plt

avg_income_by_sauce_type.plot.bar()









































