# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:34:55 2022

@author: Mehta Yash
"""

import re
b=open("largestcity.txt",'r')
c=b.readlines()
city=[]

for i in c:
    d=re.findall('\s+\D+',i)[0]
    city.append(d.strip())
my_dict={}
cities_postal_data_file=open('postalcode.txt','r')
cities_postal_data=cities_postal_data_file.read()

for j in city:

    regex_exp = '\s'+j+'\s[\d]+\s'
    city_matches =  (re.findall(regex_exp,cities_postal_data)[0:3])
    #covert the city matches list to str
    city_matches_str = "".join(city_matches)
    
    
    my_dict[j] = re.findall(r'[0-9]+', city_matches_str)
    
    
print (my_dict)
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    