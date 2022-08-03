# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:56:14 2022

@author: Mehta Yash
"""

'''
1. Remove the dollar signs in the AnnualSalary field 
and assign it as a float
'''
import pandas as pd

import numpy as np

df=pd.read_csv("Baltimore.csv")

df["AnnualSalary"]=df["AnnualSalary"].astype(str)

df["AnnualSalary"]=df["AnnualSalary"].apply(lambda x : x.replace('$',""))

df["AnnualSalary"]=df["AnnualSalary"].astype(float)


'''
 Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
'''

df.groupby(df["JobTitle"]).AnnualSalary.agg(['sum','mean','max','count','min'])


'''
How many employees are there for each JobRoles and Graph it
'''

df['JobTitle'].value_counts()[0:5].plot(kind = 'bar')

'''
List All the Agency ID and Agency Name
'''
a=df[["AgencyID","Agency"]]
a.drop_duplicates(inplace=True)
print(a)


'''
Find all the missing Gross data in the dataset
'''

df["GrossPay"].isnull().sum()






































