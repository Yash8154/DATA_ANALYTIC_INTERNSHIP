# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:34:23 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("reservationdb")

df=pd.read_csv("reservations.csv")

df.to_sql("reservation",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
Display all columns data of all the rows from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Display FirstName and LastName of all the guests from the RESERVATIONS table ?
'''
c.execute('''SELECT FirstName,LastName FROM reservation''')
df=pd.DataFrame(c.fetchall())
df.columns=["FirstName","LastName"]
print(df)

'''
Display first name of all the guests from the RESERVATIONS table ?
'''
c.execute('''SELECT FirstName FROM reservation''')
df=pd.DataFrame(c.fetchall())
df.columns=["FirstName"]
print(df)

'''
 Select all guests, that have Adults 2 from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation WHERE Adults=2''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
 Select all guests, that have Childs 1 from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation WHERE Childs=1''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
 Select all the guests, that have not Adults 0 from the RESERVATIONS table 
'''
c.execute('''SELECT * FROM reservation WHERE Adults !=0''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
 Select all the guests for whom Rate is more than 150.0 from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation WHERE Rate > 150''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
 Select all guests whose FirstName contains at least one a character from the RESERVATIONS table ?
'''
c.execute("""SELECT *
          FROM reservation
          WHERE FirstName LIKE "%a%" """)
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select all guests whose LastName starts with ‘m’  from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation WHERE LastName LIKE "m%"''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select all guests whose FirstName is exactly five characters long from the RESERVATIONS table ?

'''
c.execute('''SELECT * FROM reservation WHERE FirstName LIKE "_____"''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select only those guests from the RESERVATIONS table that: have a FirstName exactly five characters long, have a Adults more than 2
'''
c.execute('''SELECT * FROM reservation WHERE FirstName LIKE "_____" OR Adults>2''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select guests that have 2 Adults with Room Rent 250.0 from the RESERVATIONS table ?
'''
c.execute('''SELECT * FROM reservation WHERE Rate=250 AND Adults=2''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select all the guests whose CheckIn is any of these: 01-jan-10, 01-feb-10, 01-mar-10, 01-apr-10, 01-may-10 from the RESERVATIONS table ?
'''
c.execute("""SELECT *
        FROM reservation
        WHERE CheckIn IN ("01-JAN-10", "01-FEB-10", "01-MAR-10", "01-APR-10", "01-MAY-10");""")

df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select all the CheckIn that are not in jan month from the RESERVATIONS table ?
'''
c.execute("""SELECT *
        FROM reservation
        WHERE CheckIn NOT LIKE "%JAN%";""")
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)


'''
Select all the guests where Rate is between 200 to 250?
'''
c.execute('''SELECT * FROM reservation WHERE Rate BETWEEN 200 AND 250''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Select all the guests where CheckOut is null?

'''

c.execute('''SELECT * FROM reservation WHERE CheckOut is NULL''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

'''
Sort all the guests according to their Rate.

'''
c.execute("""SELECT * 
        FROM reservation
        ORDER BY Rate ASC;""")
df=pd.DataFrame(c.fetchall())
        
df.columns=["Code","Room","CheckIN","CheckOut","Rate","FirstName","LastName","Adults","Child"]
print(df)

c.execute("DROP TABLE reservation")

conn.commit()

conn.close()
















































































































