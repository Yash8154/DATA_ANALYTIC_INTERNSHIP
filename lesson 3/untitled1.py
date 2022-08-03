# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:35:31 2022

@author: Mehta Yash
"""

table_=[]
while True:
    x=input("enter the number:")
    if(not x):
        print("valid input")
        continue
        
    if(x.isdigit()):
        
        
        print("add again:")
        table_.append(x)


        
    if(x=="DONE"):
        print("thank you")
        break
    
    
    
# Taking multiple inputs from the user
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
    
    
table=[]
while True:
    x=input("enter the number:")
    if(not x):
        print("valid input")
        continue
    if x.isdigit() == False:
        print("add again:")
        
    if(x=="DONE"):
        print("thank you")
        break
    table.append(x)
print(table)

list1=[]
list2=[]

temp=user
reverse=0
while(user>0):
    user=int(input("enter the number:"))
    dig=user%10
    reverse=reverse*10+dig
    user=user//10
if(temp==reverse):
    print("num,is plaindrome")
else:
    print("num,is not palindrome")
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








