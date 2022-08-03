# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:22:57 2022

@author: Mehta Yash
"""
#without list comprehension.....

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
list=[]
for i in orders:
    if(i[-1]*i[-2]<100):
        list.append((i[0],i[-1]*i[-2]+10))
    else:
        list.append((i[0],i[-1]*i[-2]))
print(list)

#with list comprehension.....

[(i[0],i[-1]*i[-2]+10) if i[-1]*i[-2]<100 else (i[0],i[-1]*i[-2]) for i in orders]-
