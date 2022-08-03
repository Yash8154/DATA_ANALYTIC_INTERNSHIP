# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:50:52 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("zoodb")

df=pd.read_csv("zoo.csv")

df.to_sql("zoo",conn,if_exists="append",index=False)

c=conn.cursor()

'''
Display all columns data of all the rows from the zoo table ?
'''
c.execute('''SELECT * FROM zoo''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Display animal name and water needed of all the animals from the zoo table ?
'''
c.execute('''SELECT animal,water_need FROM zoo''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","water_need"]
print(df)

'''
 Display animal name of all the animals from the zoo table ?

'''
c.execute('''SELECT animal FROM zoo''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal"]
print(df)

'''
Select all animals, that are elephants  from the zoo table ?

'''
c.execute('''SELECT * FROM zoo WHERE animal='elephant' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
  Select all animals, that are zebra’s from the zoo table ?
 '''
c.execute('''SELECT * FROM zoo WHERE animal='zebra' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
 Select all the animals, that are not zebras from the zoo table ?
 '''

c.execute('''SELECT * FROM zoo WHERE animal !='zebra' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
 Select all the animals for whom the water needed is less than 300 from the zoo table ?
 '''
c.execute('''SELECT * FROM zoo WHERE water_need<300 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)
 
'''
  Select all animals whose name contains at least one e character from the zoo table ?

'''
c.execute('''SELECT * FROM zoo WHERE animal LIKE '%e%' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all animals whose name ends with 'roo' from the zoo table ?
'''
c.execute('''SELECT * FROM zoo WHERE animal LIKE '%roo' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all animals whose species name is exactly five characters long from the zoo table ?
'''

c.execute('''SELECT * FROM zoo WHERE animal LIKE '_____' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select only those animals  from the zoo table ? that:
have a name exactly five characters long
are not tigers
have a water_need more than 200
'''

c.execute('''SELECT * FROM zoo WHERE animal LIKE '_____' AND animal !='tiger' AND water_need>200 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select animals that are lions, plus all the animals that have less than 300 water_need  from the zoo table ?
'''
c.execute('''SELECT * FROM zoo WHERE  animal LIKE 'lion' OR water_need<300 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all the animals whose unique id is any of these: 1001, 1008, 1012, 1015, 1018 from the zoo table ?
'''
c.execute('''SELECT * FROM zoo WHERE uniq_id IN (1001,1008,1012,1015,1018) ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all the animals that are not 5 characters long  from the zoo table ?
'''
c.execute('''SELECT * FROM zoo WHERE animal LIKE '_____'  ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all the animals where water_need is null?
'''
c.execute('''SELECT * 
          FROM zoo WHERE water_need IS NULL ; ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Select all the animals where water_need is between 200 to 500?
'''
c.execute('''SELECT * FROM zoo WHERE water_need BETWEEN 200 AND 500  ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

'''
Sort all the animals according to their water needs.
'''
c.execute('''SELECT * FROM zoo  ORDER BY water_need   ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Animal","uniq_id","water_need"]
print(df)

c.execute("DROP TABLE zoo")

conn.commit()

conn.close()













































































































































































