# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:49:28 2022

@author: Mehta Yash
"""

# Memory Allocation in python

a=6
print(id(a)) # which represent address of 'a' in heap
b=6
print(id(b))

c=9
print(type(c))

#c is a reference variable

# Concept of OOPS(Object Oriented Programming language)
'''
OOPS is a philosophy and not a language
It logically group data(variables) and funtions

'''
# Class and Object:
'''
in simple trems class is a main body is a any objcet 
ex:making a radio..in which radio is a objet but 
how we make radio?..so that we need blue print of radio 
this blue print is known as a class
in blue print we mention all chracteristics(variables)
and function of radio

'''
#we need to create class of employee

class Employee:
    #Add your data/variable/chtics
    #Add your methods/functions 
    pass   #denotes a nothing in class

emp_1 = Employee()
#emp_1 is known as a refrence variable..
#memory allocation in stack
#create an object of employee in heap
#stores the address in the reference variable

print(id(emp_1)) #2204057114320

print(emp_1)  #0x000002012C0A96D0 this is same as above address but in hexadecimal
'''                
            Instance/object
            /      \
                    \
            /         \
            /          \
            /           \
          variables     methods

               class
              /     \
            /        \
           /          \ 
         variables    methods
#variables which are shared among all the instance of the class
#class variables should be same for all the instance of the class
'''
class Employee:
    #class variables
    no_of_leaves=0
    def __init__(self,name,age,gender,surname):
        #instance variables
        self.surname=surname
        self.name=name
        self.age=age
        self.gender=gender
        Employee.no_of_leaves+=1
        #print("yash mehta")
        #instance method
    def fullname(self):
        return self.name+" "+self.surname
        
emp_1=Employee("yash",22,"m","mehta") #() call it as funtion calling which i call as 'Constructor'
#print(emp_1)
emp_2=Employee("mahesh",45,"m","shah") # Constructor
#print(emp_2)

print(Employee.no_of_leaves)
print(emp_1.fullname())

'''
concept of inheritance

'''
# we are add employee as a manger and developer

class Developer(Employee):
    pass
class Manager(Employee):
    pass

print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Employee,Developer))

emp_1=Employee()
yash=Developer("yash",22,"m","mehta")
vishal=Manager("mahesh",45,"m","shah")

print(isinstance(emp_1,Manager))
print(isinstance(yash,Developer))
print(isinstance(vishal,Employee))

#multiple inheritance

class A:
    pass
class B:
    pass
class C(A,B):
    pass

#multilevel inheritance

class D:
    pass
class E(D):
    pass
class F(E):
    pass

    
    





























