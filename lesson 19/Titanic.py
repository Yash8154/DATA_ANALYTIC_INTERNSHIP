# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 17:27:22 2022

@author: Mehta Yash
"""

import pandas as pd

df=pd.read_csv("titanic.csv")

# How many people survived the disaster ?
a=df["Survived"].value_counts()[1]
print(a,"People survived during titanic disaster")

# How many people died ?
b=df["Survived"].value_counts()[0]
print(b,"People died during titanic disaster")

# Calculate the survival rates as proportions (percentage)

a=df["Survived"].value_counts(normalize=True)[1]
print(str(round(float(a)*100,2))+("% people survived"))

b=df["Survived"].value_counts(normalize=True)[0]
print(str(round(float(b)*100,3))+("% people died"))


# Males that survived vs males that passed away

a=df["Survived"][df["Sex"]=="male"].value_counts(normalize=True)[1]
b=df["Survived"][df["Sex"]=="male"].value_counts(normalize=True)[0]
print(str(round(float(a)*100,2)) +("% male survived"))
print(str(round(float(b)*100,2)) +("% male died"))

# Females that survived vs males that passed away

a=df["Survived"][df["Sex"]=="female"].value_counts(normalize=True)[1]
b=df["Survived"][df["Sex"]=="female"].value_counts(normalize=True)[0]
print(str(round(float(a)*100,3)) +("% female survived"))
print(str(round(float(b)*100,3)) +("% female died"))

"""
Does age play a role?
Since it's probable that children were saved first."""

def filter_data(value):
    if value <= 18:
        return 1
    else:
        return 0


df['Child'] = df['Age'].apply(filter_data)
c =  df['Survived'][df['Child'] == 1].value_counts(normalize=True)[1]
print ("Child Survived : "+str(round(c*100, 2))+"%")


'''
Adults percentage rate is slightly less than 50 % compare to 
children so..yaa age role matter during rescue operation

'''



































































