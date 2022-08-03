# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:15:39 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("bakerydb")

df=pd.read_csv("bakery.csv",delimiter=(";"))

df.to_sql("bakeryshop",conn,if_exists='replace',index=False)

c=conn.cursor()

'''
 Display all columns data of all the rows from the bakery table ?
 '''
c.execute('''SELECT * FROM bakeryshop''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Display goods and their price code from bakery table ?
 '''
c.execute('''SELECT Food,Price FROM bakeryshop''')
df=pd.DataFrame(c.fetchall())
df.columns=['Food','Price']
print(df)

'''
  Display all goods from bakery table ?
  '''
c.execute('''SELECT Food FROM bakeryshop''')
df=pd.DataFrame(c.fetchall())
df.columns=['Food']
print(df)

'''
 Select all goods whose price is 3.25 from bakery table
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price=3.25''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods whose price is 3.25 or 8.95 from bakery table 
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price=3.25 OR Price=8.95''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
Select all goods who price is not 3.25 or 8.95 from bakery table ?
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price !=3.25 AND  Price !=8.95''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods whose price is greater than 3 from bakery table ?
 '''
c.execute('''SELECT * FROM bakeryshop WHERE Price >3 ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods names where first letter c from bakery table ?
 '''
c.execute('''SELECT * FROM bakeryshop WHERE Food LIKE 'c%' ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

 
'''
 Select all goods whose food name ends  with rt from bakery table ?
 '''
c.execute('''SELECT * FROM bakeryshop WHERE Food LIKE '%rt' ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods names which having   exactly 4 characters from bakery table
'''
c.execute('''SELECT * FROM bakeryshop WHERE Food LIKE '____' ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods names   who has price greater than 3 or who ends with ke from bakery table 
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price>3 OR Food LIKE '%ke' ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods whose price are 3.25,8.95,3.75 from bakery table ?
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price IN (3.25,8.95,3.75) ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all the goods names that are not 4 characters long from bakery table ?
'''
c.execute('''SELECT * FROM bakeryshop WHERE  Food NOT LIKE '____' ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
Select all goods where price is null?
'''
c.execute('''SELECT * FROM bakeryshop WHERE Price LIKE NULL ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Select all goods whose price code between 3.25 and 8.95 from bakery table ?
 '''
c.execute('''SELECT * FROM bakeryshop WHERE Price BETWEEN 3.25 and 8.95 ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

'''
 Sort bakery table with their price code?
 '''
c.execute('''SELECT * FROM bakeryshop ORDER BY Price ASC ''')
df=pd.DataFrame(c.fetchall())
df.columns=['ID','Flavor','Food','Price']
print(df)

c.execute("DROP TABLE bakeryshop")

conn.commit()

conn.close()

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
