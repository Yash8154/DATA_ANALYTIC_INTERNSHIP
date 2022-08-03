# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:23:07 2022

@author: Mehta Yash
"""
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
          [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
          [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
          [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

out=[]
for i in orders:
    temp=[]
    for j in i[1:]:
        temp.append(j[1]*j[2])
    out.append([i[0],sum(temp)])
print(out)
        


    

a=[1,2,3,4,5]
sum(a)
orders[2][1][1]
orders[1:]