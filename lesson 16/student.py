# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:49:59 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("stdb")

df=pd.read_csv("student.csv",delimiter=',')

df.to_sql("st1",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
 Display How many students are there in student table ?
 
'''
c.execute('''SELECT COUNT(*)
           FROM st1
          
          ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["No.of.Entries"]
print(df)

'''
 Display the average grade of students from student table ?
'''
c.execute('''SELECT AVG(st1.Grade)
            FROM st1
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["AVG_GRADE"]
print(df)

'''
Display the maximum grade from student table ?
'''

c.execute('''SELECT MAX(st1.Grade)
            FROM st1
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["MAX_GRADE"]
print(df)

'''
Display the minimum grade from student table ?
'''

c.execute('''SELECT MIN(st1.Grade)
            FROM st1
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["MIN_GRADE"]
print(df)

'''
 Display the count of students for each grade from student table ?
'''

c.execute('''SELECT COUNT(st1.StFirstName) ,st1.Grade
            FROM st1
            GROUP BY st1.Grade
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_ST","Grade"]
print(df)

'''
 Display average grade for classroom 101 or 102 from student table ?
'''
c.execute('''SELECT st1.Classroom ,AVG(st1.Grade)
            FROM st1
           WHERE Classroom=101 OR Classroom=102
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOOM","AVG_Grade"]
print(df)

'''
 Display the maximum grade of each classroom from student table ?
'''
c.execute('''SELECT st1.Classroom ,MAX(st1.Grade)
            FROM st1
           GROUP BY st1.classroom
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOM","MAX_Grade"]
print(df)


'''
 Display the minimum grade of each classroom from student table ?
'''
c.execute('''SELECT st1.Classroom ,MIN(st1.Grade)
            FROM st1
           GROUP BY st1.classroom
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOM","MIN_Grade"]
print(df)

'''
 Display count of every classroom from student table and sort them by count ?
'''
c.execute('''SELECT st1.Classroom
            FROM st1
            GROUP BY st1.Classroom
          ORDER BY st1.Classroom
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOM"]
print(df)


'''
 Display average grade for each classroom from student table in descending order ?
'''
c.execute('''SELECT st1.Classroom,AVG(st1.Grade)
            FROM st1
            GROUP BY st1.Classroom
          ORDER BY AVG(st1.Grade) DESC
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOM","AVG_GRADE"]
print(df)

'''
 Display the maximum grade of each classroom from student table and sort them by maximum grade ?
'''
c.execute('''SELECT st1.Classroom,MAX(st1.Grade)
            FROM st1
            GROUP BY st1.Classroom
          ORDER BY MAX(st1.Grade) DESC
           
           ''') 
df=pd.DataFrame(c.fetchall())
df.columns=["CALSSROOM","MAX_GRADE"]
print(df)


'''
 Display the grade, Firstname, Secondname and classroom of top 3 students according to their grade from student table ?
'''
c.execute('''SELECT st1.StFirstName,st1.StLastName,st1.Classroom,MAX(st1.Grade)
          FROM st1
          GROUP BY st1.Classroom
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["F.N","L.N","C.R","Grade"]
print(df)



c.execute('''DROP TABLE st1''')
conn.commit()
conn.close()































































































































































































