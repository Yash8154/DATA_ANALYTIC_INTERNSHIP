# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:19:44 2022

@author: Mehta Yash
"""
list1=[]
d=open("romeo.txt",'r')
e=d.readlines()
for i in e:
    list1.append(i.split())
name={}
for j in list1:
    for k in j:
        if k not in name:
            name[k]=1
        else:
            name[k]+=1
print(str(name))






