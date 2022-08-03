# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:10:15 2022

@author: Mehta Yash
"""
import re
a=open("phonebook1.txt",'r')

for i in a:
    if(re.search('^[J]\w+\s[Neu]+\s\d{3}\-\d{4}',i)):
        print(i)        