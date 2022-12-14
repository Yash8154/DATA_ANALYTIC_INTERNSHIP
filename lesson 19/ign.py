# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:23:43 2022

@author: Mehta Yash
"""
"""
  Problem Statement:
   Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4. We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.


        
"""



import pandas as pd

df=pd.read_csv("ign.csv")


'''
 Let's say we want to find games released for the Xbox One 
 that have a score of more than 7.
'''
a=df[(df["platform"]=="Xbox One") & (df["score"]>7)] 
b=a["title"]
print(b)

'''
 review distribution for the Xbox One
'''
x=df["platform"]=="Xbox One" 
y=df[x]
z=y["score_phrase"]
z.hist(bins=20, grid=False, xrot=90)

'''
review distribution for the PlayStation 4
'''
a=df["platform"]=="PlayStation 4"
b=df[a]
c=b["score_phrase"]
c.hist(bins=20,grid=False,xrot=90)







































































