# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:03:50 2022

@author: Mehta Yash
"""

shopping_list=[]
print("wlcome to this app.")
print("user instruction:")
print("you add new item by clicking add")
print("if you write DONE then adding item stop and shopping list is created")
while(True):
    user=input("add item:")
    if(not user):
        print("please add anything you want")
        continue
    if(user=='DONE'):
        print("THANKS FOR USING THIS APP:")
        
        break
        
    shopping_list.append(user)
print("here is your list:")        
for i in shopping_list:
    
    print(i)
    
    
    
    
    
    