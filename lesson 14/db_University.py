# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:58:34 2022

@author: Mehta Yash
"""

import sqlite3 as sq

conn=sq.connect("db_university.db")

a=conn.cursor()

a.execute("""CREATE TABLE STUDENT_LIST (
    
    Name TEXT,
    Age INTEGER,
    Roll_No_ INTEGER,
    Branch TEXT
    )""" )

conn.commit()

a.execute("INSERT INTO STUDENT_LIST VALUES('Yash','22','23','Mechanical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Harsh','21','25','Chemical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Monil','22','26','Chemical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Parth','23','21','BSC_Math') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Dhruval','23','24','Electrical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Nish','22','29','Physics') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Vivek','22','33','Mechanical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Vishal','20','63','Mechanical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Urvish','19','13','Mechanical') ")
a.execute("INSERT INTO STUDENT_LIST VALUES('Sohan','27','3','Biology') ")

conn.commit()

a.execute("SELECT * FROM STUDENT_LIST")

from pandas import DataFrame

df = DataFrame(a.fetchall())
df.columns = ["Name","Age","Roll_No","Branch"]
df.to_csv('db_University.csv')

conn.close()

