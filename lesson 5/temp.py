# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:36:14 2022

@author: Mehta Yash
"""

fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
print(celsius)


celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)


d={a:(float(5)/9*(b-32)) for (a,b) in fahrenheit.items()}
print(d)
