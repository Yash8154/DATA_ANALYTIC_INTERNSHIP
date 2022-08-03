# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:21:47 2022

@author: Mehta Yash
"""


user=input("enter the numbers:").split(" ")

list1=[]
list2=[]

for i in user:
    list1.append(i)
for j in list1:
    if j == j[::-1]:
        list2.append(True)
    else:
        list2.append(False)
        
if True in list2:
    print("atleast one no..is palindrome")
else:
    print("Not found any palindrome no..")
    
#solution.................................................

user = input('>').split(" ")  # splitting the inputs with spaces by 'split'

# Assigning lists
list1 = []  # for user input
list2 = []  # for the output


for i in user:
    list1.append(i)  # appending the inputs into list1

# Checking for the symmetry
for i in list1:
    if i == i[::-1]:
        list2.append(True)
    else:
        list2.append(False)

# Printing outputs
if True in list2:
    print("True")
else:
    print("False")
