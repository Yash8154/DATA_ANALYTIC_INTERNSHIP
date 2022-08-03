# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:13:18 2022

@author: Mehta Yash
"""


import sqlite3 as sql

import pandas as pd

conn=sql.connect("bakery1db")

df=pd.read_csv("bakery1.csv",delimiter=(";"))

df.to_sql("bakery1",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
 Display How many Chocolate Flavoured Foods are there in bakery table ?
 '''
c.execute("""SELECT COUNT(bakery1.Flavor) FROM bakery1 WHERE Flavor='Apple' """)
df=pd.DataFrame(c.fetchall())
df.columns=["No.Of_Choclate_Flavor"]
print(df)


'''
Display the total price of Foods which are Apple Flavoured from bakery table ?
'''
c.execute('''SELECT bakery1.Flavor,SUM(bakery1.price) FROM bakery1 WHERE Flavor='Apple'  
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor","Total_Price"]
print(df)

'''
Display average amount of cake Flavoured Foods from bakery table ?
'''
c.execute('''SELECT bakery1.Food,AVG(bakery1.price) FROM bakery1 WHERE Food='Cake'  
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","AVG.PRICE"]
print(df)

'''
Display the maximum price from bakery table ?

'''

c.execute('''SELECT MAX(bakery1.price) FROM bakery1
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["MAX.PRICE"]
print(df)

'''
Display the minimum price from bakery table ?

'''

c.execute('''SELECT MIN(bakery1.price) FROM bakery1
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["MIN.PRICE"]
print(df)

'''
Display count of every Food from bakery table ?
'''

c.execute('''SELECT bakery1.Food, COUNT(bakery1.Food) FROM bakery1
         GROUP BY bakery1.Food
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","No.Food"]
print(df)


'''
Display the total price of Each Flavour from bakery table  ?
'''
c.execute('''SELECT bakery1.Flavor, SUM(bakery1.Price) FROM bakery1
         GROUP BY bakery1.FLavor
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor","Total_Price"]
print(df)


'''
Display average price for Cake or Eclair from bakery table ?

'''
c.execute('''SELECT bakery1.Food, AVG(bakery1.Price) FROM bakery1
         WHERE Food='Cake ' OR Food='Eclair'
         GROUP BY bakery1.Food
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","Avg_Price"]
print(df)

'''
Display the maximum price of each Food from bakery table ?

'''
c.execute('''SELECT bakery1.Food, MAX(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","MAX_Price"]
print(df)

'''
Display the minimum price of each Flavour from bakery table ?
'''

c.execute('''SELECT bakery1.Food, MIN(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","MIN_Price"]
print(df)

'''
Display count of every Food from bakery table and sort them by count ?
'''

c.execute('''SELECT bakery1.Food , COUNT(bakery1.Food) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY COUNT(bakery1.Food)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","NO.OF>ITEMS"]
print(df)


'''
Display the total price of each Flavour from bakery table and sort them by price ?
'''
c.execute('''SELECT bakery1.Flavor , SUM(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Flavor ORDER BY SUM(bakery1.Price)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor","Total_Price"]
print(df)

'''
Display average price for each Food from bakery table and sort them by average price ?
'''
c.execute('''SELECT bakery1.Food , AVG(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY AVG(bakery1.Price)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","AVG_Price"]
print(df)

'''
Display the maximum price of each Food from bakery table and sort them by maximum price ?

'''

c.execute('''SELECT bakery1.Food , MAX(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY MAX(bakery1.Price)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","MAX_Price"]
print(df)

'''
Display the minimum price of each Flavour from bakery table and sort them by minimum price ?
'''

c.execute('''SELECT bakery1.Flavor , MIN(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Flavor ORDER BY MIN(bakery1.Price)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor","MIN_Price"]
print(df)

'''
Display count of every Food from bakery table in descending order ?
'''
c.execute('''SELECT bakery1.Food , COUNT(bakery1.Food) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY COUNT(bakery1.Food) DESC
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","NO>OF>Flavours"]
print(df)

'''
Display the total price of each Flavour from bakery table in descending order ?

'''
c.execute('''SELECT bakery1.Flavor , SUM(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Flavor ORDER BY SUM(bakery1.Price) DESC
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor","TOTAL_PRICE"]
print(df)

'''
Display average price for each Food from bakery table in descending order ?
'''

c.execute('''SELECT bakery1.Food , AVG(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY AVG(bakery1.Price) DESC
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","AVG_PRICE"]
print(df)



'''
Display the maximum price for each food from bakery table in descending order ?

'''
c.execute('''SELECT bakery1.Food , MAX(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY MAX(bakery1.Price) DESC
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","AVG_PRICE"]
print(df)

'''
Display the minimum price for each food from bakery table in descending order ?

'''
c.execute('''SELECT bakery1.Food , MIN(bakery1.Price) FROM bakery1
        
         GROUP BY bakery1.Food ORDER BY MIN(bakery1.Price) DESC
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","MIN_PRICE"]
print(df)

'''
Display Flavour column from bakery table without duplicates ?
'''
c.execute('''SELECT bakery1.Flavor FROM bakery1
        
         GROUP BY bakery1.Flavor ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Flavor"]
print(df)


'''
Display count of each Food, which have Chocolate Flavour , also arrange food's name in alphabetical order ?

'''

c.execute('''SELECT bakery1.Food,bakery1.Flavor FROM bakery1
        WHERE Flavor='Chocolate'
        GROUP BY bakery1.Food
        ORDER BY bakery1.Food
         ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Food","Flavor"]
print(df)


c.execute('''DROP TABLE bakery1''')

conn.commit()

conn.close()






































































































































































