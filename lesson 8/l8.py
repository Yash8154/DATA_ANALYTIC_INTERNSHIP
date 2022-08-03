# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:23:36 2022

@author: Mehta Yash
"""

"""
TOPIC:Exception Handling in Python

this topic is generally used in internet connectivity

"""
#version 1:
try:
    x=int(input("enter your age :"))
except Exception:
    print("non integer value...try again")
else:
    print("your age is",x)
finally:
    print("program ended")
    
#version 2:
    
try:
    x=int(input("enter your age :"))
else:
    print("your age is",x)
except Exception:
    print("non integer value...try again")

finally:
    print("program ended")

# diff. b\w 1 and 2 is we follow squence of version 1

while(True):
    try:
        x=int(input("enter your age :"))
        if(x>=18):
            print("you are adult")
        else:
            print("you are not adult")
    except Exception:
        print("non integer value...try again")
    else:
        print("your age is",x)
    finally:
        print("program ended")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    