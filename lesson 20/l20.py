# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:09:13 2022

@author: DELL
"""

list1 = [1,2,3,4,5,6,7,8,9,10]

list1*10

list1 = [0]*10

list2 = []
for item in list1:
    list2.append (item*10)
    
[item*10 for item in list1]

list1 = [1,2,3,4,5,6,7,8,9,10]

import numpy as np

x = np.array(list1)

#df.values -> ndarray

x.shape
x.ndim

y = 10 #scaler value

y = np.array(y)
y.shape
y.ndim

y = [10] #1D

y = np.array(y)

y.shape
y.ndim

y = [[10]] #2D

y = np.array(y)
y.shape
y.ndim

list1 = [1,2,3,4,5,6,7,8,9]

x = np.array(list1)
x = x.reshape(3,3)

x = np.arange(5, dtype = np.int32)


np.ones((3,4), dtype = np.int8)

np.zeros((2,4))


import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.scatter(x,y)
plt.plot(x,y)


x =  np.arange(20)
y = [item**3 for item in x] 

plt.scatter(x,y)

plt.plot(x,y)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
branchnames = ('CSE', 'ECE', 'IT', 'EE')
sizes = [10, 5, 5, 2]
apart = (0.2, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')


plt.pie(sizes, explode=apart ,labels=branchnames, autopct='%.2f%%')

plt.show()







































































