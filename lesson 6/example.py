# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:44:36 2022

@author: Mehta Yash
"""

# Ques 1-Find all of the numbers from 1-1000 that are divisible by 7

a=[x for x in range (1,1001) if x % 7==0]
print(a)

# Ques 2-Find all of the numbers from 1-1000 that have a 3 in them

b=[x for x in range (1,1001) if '3' in str(x)]
print(b)

# Ques 3-Count the number of spaces in a string

i=0
x=input("enter the word")
for j in x:
    if j==' ':
        i+=1
print(i)

# Ques 4-Remove all of the vowels in a string


string = input("Enter string")
vowels = "aeiou"
remain = []
for i in string:
    if i not in vowels:
        remain.append(i)
c = " ".join(remain)
print(c)

# Ques 5-Find all of the words in a string that are less than 4 letters

x=input("enter the sentence:").split()
d=[i for i in x if len(i)<4]
print(d)

#Ques 6-A list of all consonants in the sentence 'The quick brown fox jumped over the lazy dog'


string = 'The quick brown fox jumped over the lazy dog'
vowels = "aeiou "
a=[]
for i in string:
    if i not in vowels:
        a.append(i)
print(a)

# Ques 7-A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'


string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital = []

for i in string:
    if i==i.upper() and i!=' ':
        capital.append(i)
print(capital) 


# Ques 8-A list of all square numbers formed by squaring the numbers from 1 to 1000.

g=[]
for i in range (1,1001):
    if i*i<1000:
        g.append(i*i)
    else:
        break
print(g)




