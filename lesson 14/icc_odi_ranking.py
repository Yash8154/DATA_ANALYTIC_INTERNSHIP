# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:06:20 2022

@author: Mehta Yash
"""

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

import requests

from bs4 import BeautifulSoup

source=requests.get(url).text

soup=BeautifulSoup(source,"html.parser")

ranking_table=soup.find('table',class_="table")
E=[]
A=[]
B=[]
C=[]
D=[]

for row in ranking_table.findAll ("tr"):
    a=row.findAll('td')
    if len(a)==5:
        E.append(a[0].text.strip())
        A.append(a[1].text.strip())
        B.append(a[2].text.strip())
        C.append(a[3].text.strip())
        D.append(a[4].text.strip())
        
import pandas as pd

df=pd.DataFrame()
df["Ranking"]=E
df["Team"]=A
df["Matches"]=B
df["Points"]=C
df["Ratings"]=D

df.to_csv("odi_rankings.csv",index=False)

df1 = pd.DataFrame(zip(E,A,B,C,D), columns = ['Ranking','Team','Matches','Points','Ratings'])

import sqlite3 as sq

conn=sq.connect("ODI_Ranking.db")

df.to_sql("Rtable",conn)

#reading the data from table

rconn = sq.connect('ODI_Ranking.db')

new_df = pd.read_sql('SELECT * FROM Rtable' , rconn)



a=pd.read_sql('SELECT * FROM Rtable WHERE Ranking == 3' , rconn)


new_df1 = pd.read_sql_table('SELECT * FROM Rtable' , rconn)





















































