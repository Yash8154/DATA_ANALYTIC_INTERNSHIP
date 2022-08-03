# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:50:25 2022

@author: Mehta Yash
"""


import sqlite3 as sql

import pandas as pd

conn=sql.connect("winedb")

df1=pd.read_csv("wine.csv",delimiter=',')
df1.to_sql("wine",conn,if_exists="replace",index=False)

df2=pd.read_csv("grapes.csv",delimiter=',')
df2.to_sql("grapes",conn,if_exists="replace",index=False)

df3=pd.read_csv("appellations.csv",delimiter=',')
df3.to_sql("appelations",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
Find the grape(s) that grow(s) in the largest number of appellations.
Report grape name, color and the number of appellations it grows in.
'''
c.execute('''SELECT grapes.Grape,grapes.Color,COUNT(wine.Appelation)
          FROM wine,grapes
          WHERE grapes.Grape=wine.Grape
          GROUP BY grapes.Grape
          ORDER BY COUNT(wine.Appelation) DESC LIMIT 1
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRAPES_NAME","COLOR","NO_OF_APPELATIONS"]
print(df)


'''
Find the most popular white grape (i.e., the grape that is used to make the largest number of white wines in the database).
 Report the name of the grape.
'''
c.execute('''SELECT grapes.Grape, COUNT(wine.Appelation)
          FROM wine,grapes
          WHERE grapes.Grape=wine.Grape AND grapes.Color LIKE '%White%'
          GROUP BY grapes.Grape
          ORDER BY COUNT(wine.Appelation) DESC LIMIT 1
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRAPES_NAME","MAX_NO_OF_APPELATIONS"]
print(df)
 


'''
Report the grape with the largest number of high-ranked wines (score of 93 and above).
'''

c.execute('''SELECT grapes.Grape,MAX( wine.Score)
          FROM wine,grapes
          WHERE grapes.Grape=wine.Grape AND wine.Score >=93
          GROUP BY grapes.Grape
          ORDER BY MAX( wine.Score) DESC
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRAPES_NAME","MAX_SCORE"]
print(df)

'''
Report the appellation responsible for the largest number of highranked wines (score of 93 and above).
 Report just the name of the appellation .
'''
 
c.execute('''SELECT grapes.Grape,MAX( wine.Score),wine.Appelation
          FROM wine,grapes
          WHERE grapes.Grape=wine.Grape AND wine.Score >=93
          GROUP BY grapes.Grape
          ORDER BY MAX( wine.Score) DESC
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRAPES_NAME","MAX_SCORE","NAME_OF_APPELATION"]
print(df)


'''
Find the high-ranked wine (score of 93 or above) responsible for highest Price. 
Report the vintage year, winery, wine name, score and the Price (Chronological Order).
'''
c.execute('''SELECT wine.Name,wine.Year,wine.Winery,MAX( wine.Score),wine.Price
          FROM wine
          WHERE  wine.Score >=93
          GROUP BY wine.Grape
          ORDER BY wine.Price
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["WINE_NAME","YEAR","WINERY","MAX_SCORE","PRICE"]
print(df)

'''
Find if there are any 2008 Chardonnays that scored better than any 2007 Syrah. 
report winery, wine name, appellation, score and price.
'''
c.execute("""SELECT 
    wine.Winery,
    wine.Name,
    wine.Appelation,
    wine.Score,
    wine.Price
FROM
    wine
WHERE
	(SELECT wine.Score From wine WHERE wine.Grape LIKE '%Syrah%'
    AND wine.Year LIKE '%2007%') < (SELECT wine.Score From wine WHERE wine.Grape LIKE '%Chardonnay%'
    AND wine.Year LIKE '%2008%')
""")
df = pd.DataFrame(c.fetchall())
if len(df.columns) ==5:
    df.columns = ["Winery","Name","Appelation","Score","Price"]
print(df)


c.execute("""DROP TABLE wine""")          
c.execute("""DROP TABLE grapes""")          
c.execute("""DROP TABLE appelations""")

conn.commit()

conn.close()          
          














































































