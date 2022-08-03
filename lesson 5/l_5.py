# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:36:06 2022

@author: Mehta Yash
"""

#LECTURE 5  functional programming ..................................

list1=[10,20,30,40]
for i in list1:
    print(i*i)
    
[i*i  for i in list1]


def squarevalue(x):
    return(x*x)
    
print(list(map(squarevalue,list1)))

list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    if(i%2==0):
        list2.append("TRUE")
    else:
        list2.append("FALSE")
print(list2)

#...now using DEFINE funtion.....

def iseven(x):
    if(x%2==0):
        print(True)
    else:
        print(False)
        
#....now using map funtion.......

print(list(map(iseven, list1)))

"""
in above list we get trure or false value
but if we get only even value then...
i can use "FILTER FUNTION"
"""
print(list(filter(iseven,list1)))

# now using lambda....

print(list(map(lambda x : x%2==0, list1)))

#PYTHON IS A PARTIAL FUNCTIONAL PROGRAMMING LANGUAGE
list1 = [1,2,3,4,5]
​
def iseven(x):
  return (x % 2 == 0)
​
print  (list(map(iseven, list1)))
​
print  (list(map(lambda x:x % 2 == 0, list1)))
​
​
print  (list(filter(iseven, list1)))

#.....reduce funtion......

list1=[1,2,3,4,5,6]
def fadd(x,y):
    return(x+y)
import functools
print(functools.reduce(fadd,list1))


list1=[1,2,3,4,5,6]
def fadd(x,y):
    return(x*y)
import functools
print(functools.reduce(fadd,list1))

# using lambda.....

list1=[1,2,3,4,5,6]
def fadd(x,y):
    return(x*y)
import functools
print(functools.reduce(lambda x,y:x*y,list1))

# dictionary data structure......
student={
            'name':'yash',
            'chem':'87',
            'math':'76',
            'phy':'80'
}

#in dictionary we use sub dictionary
student={
            'name':'yash',
            'chem':{'mt-1':'40' , 'mt-2':'37'},
            'math':'76',
            'phy':'80'
}
student['chem']
student['chem']['mt-2']

#tuple.....

divmod(45,7)
type(divmod(45,7))
x, y=divmod(45,7)











​
 
  










      






















