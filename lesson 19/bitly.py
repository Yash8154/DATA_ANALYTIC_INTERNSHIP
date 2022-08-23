# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 21:57:57 2022

@author: DELL
"""
import pandas as pd

import numpy as np

json_df=pd.read_json("bitly.json",lines=True)

'''
  Replace the 'nan' values with 'Missing' and ' ' values with 'Unknown' keywords
'''
json_df.isnull().any(axis=0)  

json_df = json_df.replace([np.nan, "Missing"], [" ", "Unknown"])
'''
 Print top 10 most frequent time-zones from the Dataset 
 '''
 
json_df_tz = json_df['tz'].value_counts().head(10)


'''
Count the number of occurrence for each time-zone
'''
tz_count = json_df['tz'].value_counts()

'''
 Plot a bar Graph to show the frequency of top 10 time-zones.
'''
import matplotlib.pyplot as plt

json_df_tz.plot.bar() 

'''
  From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
'''
  
tokens_df = json_df['a'].str.split(n = 1, expand = True).add_prefix("Token_")

# Fetching the frequency of the browser capability
tokens_frequency = tokens_df['Token_0'].value_counts()



# Plotting bar graph for top 5 browser capability
tokens_frequency.head().plot.bar()

# Filling the missing values in the token parts with mising string
tokens_df = tokens_df.replace(np.nan, 'Missing')

# Classifying as windows os and non-windows os

# Initializing the os column as Not windows
tokens_df["os"] = 'Not Windows'

# Applying the conditions to find the windows os user and initializing their os column as Windows
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"





















































































