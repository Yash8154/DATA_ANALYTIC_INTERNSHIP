# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 18:06:20 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("practicedb")

df1 = pd.read_csv('airlines.csv')
df1.columns =['Id', 'Airline', 'Abbreviation', 'Country']
df1.to_sql('airlines', conn, if_exists='replace', index=False)


df2 = pd.read_csv('flights.csv')
df2.columns = ['Airline', 'FlightNo', 'SourceAirport', 'DestAirport']
df2.to_sql('flights', conn, if_exists='replace', index=False)


df3 = pd.read_csv('airports100.csv')
df3.columns = ['City', 'AirportCode', 'AirportName', 'Country','CountryAbbrev']
df3.to_sql('airports100', conn, if_exists='replace', index=False)


df4 = pd.read_csv('Reservations.csv')
df4.to_sql('reservations', conn, if_exists='replace', index=False)


df6 = pd.read_csv('Rooms.csv')
df6.to_sql('room', conn, if_exists='replace', index=False)


df7 = pd.read_csv('csufee.csv')
df7.to_sql('csufees', conn, if_exists='replace', index=False)

df8 = pd.read_csv('list.csv')
df8.to_sql('list', conn, if_exists='replace', index=False)


df9 = pd.read_csv('teachers.csv')
df9.to_sql('teachers', conn, if_exists='replace', index=False)

df10 = pd.read_csv('appellations.csv')
df10.to_sql('appellations', conn, if_exists='replace', index=False)


df11 = pd.read_csv('grapes.csv')
df11.to_sql('grapes', conn, if_exists='replace', index=False)


df12 = pd.read_csv('wine.csv')
df12.to_sql('wine', conn, if_exists='replace', index=False)

df13 = pd.read_csv('car_names.csv')
df13.to_sql('car_names', conn, if_exists='replace', index=False)


df14 = pd.read_csv('cars_data.csv')
df14.to_sql('cars_data', conn, if_exists='replace', index=False)

df15 = pd.read_csv('car_makers.csv')
df15.to_sql('cars_makers', conn, if_exists='replace', index=False)

c=conn.cursor()

'''
Given a student’s last name, find the student’s grade, 
classroom .
'''
c.execute('''SELECT list.Grade,list.Classroom
          FROM list
          WHERE list.LastName LIKE '%BEAN%'
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["GRADE","CLASS_ROOM"]
print(df)

'''
'Given a student’s last name, find the bus route the student takes
'''
c.execute('''SELECT list.Bus
          FROM list
          WHERE list.LastName LIKE '%BEAN%'
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["BUS"]
print(df)

'''
Find all students at a specified grade level
'''
c.execute('''SELECT list.LastName,list.FirstName
          FROM list
          WHERE list.Grade=6 
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["L_NAME","F_NAME"]
print(df)

'''
For each entry found, print the last name, first name, grade, classroom 
'''
c.execute('''SELECT *
          FROM list
          
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["L_NAME","F_NAME","GRADE","C_ROOM","BUS"]
print(df)


'''
Display the total number of students for each bus routes
'''
c.execute('''SELECT COUNT(list.FirstName),list.Bus
          FROM list
          GROUP BY list.Bus
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_ST","BUS_NO"]
print(df)

'''
Display the total number of students for each grades
'''




c.execute('''SELECT COUNT(list.FirstName),list.Grade
          FROM list
          GROUP BY list.Grade
          
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_ST","GRADE"]
print(df)


'''
'Find all cars produced by Volvo between 1977 and 1981 (inclusive)
'''

c.execute('''SELECT car_names.Model,car_names.Make,cars_data.Year
          FROM car_names,cars_data
          WHERE car_names.Id=cars_data.Id AND cars_data.Year BETWEEN 1977 AND 1981 AND car_names.Model LIKE '%volvo%'
          ''')
          
df=pd.DataFrame(c.fetchall())
df.columns=["MODEL","MAKER","YEAR"]
print(df)

'''
Display all columns data of all the rows from the flights table ?
'''
c.execute('''SELECT *
          FROM flights
          ''')
          
df=pd.DataFrame(c.fetchall())
df.columns=["AIRLINE","F-NO","S-AIRPORT","D-AIRPORT"]
print(df)

'''
Display source and destination airport  from flights table ?
'''
c.execute("""SELECT 
    flights.SourceAirport,
    flights.DestAirport
FROM
    flights;""")

df = pd.DataFrame(c.fetchall())
if len(df.columns) ==2:
    df.columns = ["SourceAirport","DestAirport"]
print(df)


'''
Select all flights whose airline number is 3 or 5 from flights table ?
'''
c.execute("""SELECT 
    flights.DestAirport, flights.Airline
FROM
    flights
WHERE
    flights.Airline IN (3 , 5); """)
df = pd.DataFrame(c.fetchall())
if len(df.columns) ==2:
    df.columns = ["DestAirport","Airline"]
print(df)


'''
Display  all airline code  from flights table ?
'''
c.execute("""SELECT 
    DISTINCT(flights.Airline)
FROM
    flights;""")
    
df = pd.DataFrame(c.fetchall())
if len(df.columns) ==1:
    df.columns = ["Airline"]
print(df)


'''
Select all flights whose airline number is 3 from flights table ?
'''
c.execute("""SELECT 
    flights.DestAirport, flights.Airline
FROM
    flights
WHERE
    flights.Airline = 3;""")
    
df = pd.DataFrame(c.fetchall())
if len(df.columns) ==2:
    df.columns = ["DestAirport","Airline"]
print(df)


conn.close()






























































































































