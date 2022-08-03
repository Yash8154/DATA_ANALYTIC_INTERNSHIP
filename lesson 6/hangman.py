# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:48:27 2022

@author: Mehta Yash
"""

import random
dictionary=["reliance","tata","birla","paytm","lifeline","paris","boat","microsoft"]
a=[]
computer=random.choice(dictionary)
length_word=len(computer)
alphabet="abcdefghijklmnopqrstuvwxyz"
for i in computer:
    a.append("_")
print("the guess word of computer has no.of letter is:",length_word)
print("be careful to enter word from alphabet only")
print(a)
tries=1
while tries<10:
    user=input("select any letter:").lower()
    if user not in alphabet:
        print("enter valid alphabet leter:")
    if user in computer:
        print("your pick is correct")
        for x in range(0,length_word):
                if computer[x]==user:
                    a[x]=user
        print(a)
        if '_'not in a:
               print("you won")
               break
    else:
        print("the user is not letter..try again ")
        tries+=1
    if tries==10:
        print("you lose....and computer choice word is..",computer)
        
        
        
        
                    
            
    
