# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:57:42 2022

@author: Mehta Yash
"""

'''Table list and teachers'''

import sqlite3 as sql

import pandas as pd

conn=sql.connect("Practice3db")

df1=pd.read_csv("list.csv",delimiter=',')

df1.to_sql("list",conn,if_exists="replace",index=False)


df2=pd.read_csv("teachers.csv",delimiter=',')

df2.to_sql("teachers",conn,if_exists="replace",index=False)

c=conn.cursor()


#Q 1  Given a student’s last name, find the student’s grade, classroom and teacher.

c.execute('''SELECT list.Grade,list.Classroom,teachers.LastName,teachers.FirstName
          FROM list,teachers
          WHERE list.Classroom=teachers.Classroom
           AND
           list.LastName LIKE '%BEX%'
           ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRADE","C-ROOM","T-LASTNAME","T-FIRSTNAME"]
print(df)           


#Q 2  Given a student’s last name, find the bus route the student takes

c.execute('''SELECT list.Bus
          FROM list
          WHERE  list.LastName LIKE '%BEX%'
          
          
           ''')
df=pd.DataFrame(c.fetchall())
df.columns=["BUS"]
print(df)           


#Given a bus route, find all students who take it

c.execute('''SELECT list.FirstName,list.LastName
          FROM list
          WHERE  list.Bus=53
          
          
           ''')
df=pd.DataFrame(c.fetchall())
df.columns=["F-NAME","L-NAME"]
print(df)           


c.execute('''DROP TABLE list''')
c.execute('''DROP TABLE teachers''')
conn.commit()
conn.close()


'''Tables  campuses and csufees'''

import sqlite3
import pandas as pd
conn = sqlite3.connect ('practice3db.sqlite' )

campuses = pd.read_csv('campuses.csv', delimiter=(','))
campuses.to_sql('campuses', conn, if_exists='replace', index=False)

csufees = pd.read_csv('csufee.csv', delimiter=(','))
csufees.to_sql('csufees', conn, if_exists='replace', index=False)

disciplines = pd.read_csv('disciplines.csv', delimiter=(','))
disciplines.to_sql('disciplines', conn, if_exists='replace', index=False)

discipline_name = pd.read_csv('discipline_name.csv', delimiter=(','))
discipline_name.to_sql('discipline_name', conn, if_exists='replace', index=False)


enrollments = pd.read_csv('enrollments.csv', delimiter=(','))
enrollments.to_sql('enrollments', conn, if_exists='replace', index=False)




c = conn.cursor()


#Q 5 Report all campuses from Los Angeles county. Output the full name of campus in alphabetical order.

c.execute('''SELECT campuses.Campus
          FROM campuses
          WHERE campuses.County LIKE '%Los Angeles%'
          ORDER BY campuses.Campus
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["CAMPUS_NAME"]
print(df)


#Q 6 
#-- For each year between 1994 and 2004 (inclusive) report the number of
#-- students who enrolled for undergraduate from California Maritime Academy Output
#-- the year,no. of enrollments for each year.

c.execute('''SELECT SUM(disciplines.Undergraduate)
          FROM campuses,disciplines
          WHERE campuses.Id=disciplines.Campus
          AND disciplines.Year BETWEEN 1994 AND 2004
          AND campuses.Campus LIKE '%California  Maritime Academy%'
          
          GROUP BY disciplines.Year
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_UG_ENROLLMENTS"]
print(df)


#Q 7 
#-- Report undergraduate and graduate enrollments (as two numbers) in
#-- ’Mathematics’, ’Engineering’ and ’Computer'.

c.execute("""SELECT 
    discipline_name.Name, 
    SUM(disciplines.Undergraduate),
    SUM(disciplines.Graduate)
FROM
    discipline_name,
    disciplines
WHERE
    discipline_name.Name IN ('Mathematics' , 'Engineering', 'Computer and Info. Sciences') 
    GROUP BY discipline_name.Name;""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Name","total Undergraduate","total Graduate"]
print(df)


#Q 8
#-- Report graduate enrollments in 2004 
#-- Report only one row from each university  
#-- the number of graduate students.

c.execute('''SELECT campuses.Campus,SUM(disciplines.Undergraduate)
          FROM campuses,disciplines
          WHERE campuses.Id=disciplines.Campus
          AND disciplines.Year = 2004
        
          
          GROUP BY campuses.Campus
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NAME_OF_UNIVERSITY","NO_OF_UG_ENROLLMENTS"]
print(df)



#Q 9
#-- Find all  campuses where graduate enrollment in 2004
#-- was at least double than undergraduate enrollment. 
#-- Report campus names and discipline id. 
#-- Sort output by campus name in alphabetical order.
c.execute("""SELECT 
    discipline_name.Id, 
    campuses.campus
FROM
    discipline_name,
    campuses,
    disciplines
WHERE
    disciplines.Campus = campuses.Id
    AND disciplines.Graduate >= 2*disciplines.Undergraduate
	AND disciplines.year = 2004 ORDER BY campuses.campus;""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Id","campus"]
print(df)


#Q 10
#-- Report the total amount of money collected from student fees at ’Fresno State
#-- University’ for each year between 2002 and 2004 inclusively,. Output the year.
c.execute("""SELECT 
    SUM(csufees.campusfee) AS total_amount, csufees.year
FROM
    csufees,
    campuses
WHERE
    csufees.year IN (2002 ,2003, 2004)
        AND campuses.campus LIKE '%Fresno State University%'
        GROUP BY csufees.year ;""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_amount","year"]
print(df)


#Q 11
#-- Find all campuses where enrollment in 2004 ,
#-- was higher than the 2004 enrollment in ’San Jose State University’.
#-- Report the name of campus.


c.execute('''SELECT campuses.Campus
          FROM campuses,enrollments
          WHERE campuses.Id=enrollments.Campus
          AND (enrollments.TotalEnrollment_AY  AND campuses.Campus NOT LIKE '%San Jose State University%')>(enrollments.TotalEnrollment_AY AND campuses.Campus LIKE '%San Jose State University%')
        AND enrollments.Year=2004
          
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NAME_OF_UNIVERSITY"]
print(df)


c.execute("""DROP TABLE campuses""")
c.execute("""DROP TABLE csufees""")
c.execute("""DROP TABLE disciplines""")
c.execute("""DROP TABLE discipline_name""")
c.execute("""DROP TABLE enrollments""")

conn.commit()

conn.close()







































































































































