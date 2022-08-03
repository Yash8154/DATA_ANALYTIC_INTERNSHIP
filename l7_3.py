# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:16:31 2022

@author: Mehta Yash
"""

a=open("james_joyce_ulysses.txt",'r')
b=a.read()
import re
c=re.findall("[a-zA-Z]+",b)
d=len(set(c))
print("the no of word is:",len(c))
print("the no.of unique word is:",d)


novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt'
          ]
a=[]

for i in novels:
    b=open(i,encoding="utf8")
    c=b.read()
    import re
    d=re.findall("[a-zA-Z]+",c)
    a.append(len(d))
    
print(a)
    