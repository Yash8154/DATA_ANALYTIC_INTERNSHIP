# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:20:59 2022

@author: Mehta Yash
"""


    
T = int(input("enter:"))

for i in range(T):
    a,b = map(str,input().strip().split())

    try:
        print(int(a)//int(b))
        
    except Exception as e:
        print("Error Code:",e)