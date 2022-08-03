# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:23:24 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("studentsdb")

df=pd.read_csv("students.csv")

df.to_sql("st",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
Display all columns data of all the rows from the students table ?

'''
c.execute('''SELECT * FROM st ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Display last name and first name of all the students from the students table ?
'''
c.execute('''SELECT LastName,FirstName FROM st ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname"]
print(df)

'''
Display first name of all the students from the students table ?
'''
c.execute('''SELECT FirstName FROM st ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Firstname"]
print(df)

'''
Select all students, that have Grade 1  from the students table ?
'''
c.execute('''SELECT * FROM st WHERE Grade=1 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all students, that have Grade 0 from the students table ?
'''
c.execute('''SELECT * FROM st WHERE Grade=0 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the students, that have not Grade 0 from the students table ?

'''
c.execute('''SELECT * FROM st WHERE Grade !=0 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the students for whom the Grade is less than 4 from the students table ?

'''
c.execute('''SELECT * FROM st WHERE Grade <4 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all students whose FirstName contains at least one e character from the students table ?
'''
c.execute('''SELECT * FROM st WHERE FirstName LIKE '%e%' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all students whose LastName ends with ‘a’  from the students table ?
'''
c.execute('''SELECT * FROM st WHERE LastName LIKE '%a' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)


'''
Select all students whose FirstName is exactly five characters long from the students table ?
'''
c.execute('''SELECT * FROM st WHERE FirstName LIKE '_____' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select only those students  from the students table ? 
that: have a FirstName exactly five characters long, have a Grade more than 2
'''
c.execute('''SELECT * FROM st WHERE FirstName LIKE '_____' AND Grade>2 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select students that have Grade 1,and all the students that have classroom 102 from the students table ?
'''
c.execute('''SELECT * FROM st WHERE Grade=1 AND Classroom=102 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the students whose Classroom is any of these: 101, 108, 102, 105, 107 from the students table ?
'''
c.execute('''SELECT * FROM st WHERE Classroom IN (101,108,102,105,107) ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the FirstName that are not 5 characters long  from the students table ?
'''
c.execute('''SELECT * FROM st WHERE FirstName NOT LIKE '_____' ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the students where Grade is null?
'''

c.execute('''SELECT * FROM st WHERE Grade IS NULL ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Select all the students where Grade is between 1 to 5?

'''

c.execute('''SELECT * FROM st WHERE Grade BETWEEN 1 AND 5 ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

'''
Sort all the students according to their Classroom.
'''
c.execute('''SELECT * FROM st ORDER BY Classroom ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LastName","Firstname","Grade","Class"]
print(df)

c.execute("""DROP TABLE st""")

conn.commit()

conn.close()




















































































































































































