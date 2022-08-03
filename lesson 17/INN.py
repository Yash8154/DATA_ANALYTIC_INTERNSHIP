# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:52:02 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("inndb")

df1=pd.read_csv("Rooms.csv",delimiter=',')

df1.to_sql("Rooms",conn,if_exists="replace",index=False)
df1.columns=["RoomId","roomName","beds","bedType","maxOccupancy","basePrice","decor"]

df2=pd.read_csv("Reservations.csv",delimiter=',')

df2.to_sql("Reservations",conn,if_exists="replace",index=False)
df2.columns=["Code","Room","CheckIn","CheckOut","Rate","LastName","FirstName","Adults","Kids"]

c=conn.cursor()

'''
Find all modern rooms with a base price below $160 and two beds.Report room names and codes in alphabetical order by the code.
'''

c.execute('''SELECT Rooms.roomName,Rooms.RoomId
          FROM Rooms
          WHERE Rooms.basePrice<160 AND Rooms.beds=2 AND Rooms.decor LIKE '%modern%'
          ORDER BY Rooms.RoomId
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["ROOM_NAME","ROOM_ID"]
print(df)


'''
Find all July reservations for the ’Convoke and sanguine’ room. For each reservation
report the last name of the person who reserved it, checkin and checkout dates, the total number of people staying and the daily rate.
Output reservations in chronological order.
'''

c.execute('''SELECT Reservations.LastName,Reservations.CheckIn,Reservations.CheckOut,Reservations.Adults+Reservations.Kids,Reservations.Rate
          FROM Rooms,Reservations
          WHERE Rooms.RoomId=Reservations.Room AND Reservations.CheckIn LIKE '%JUL%' AND Rooms.roomName LIKE '%Convoke%'
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["LAST_NAME","CHECK_IN","CHECK_OUT","TOTAL_PERSON","RATE"]
print(df)


'''
Find all rooms occupied on February 6, 2010. 
Report full name of the room, the check-in and checkout dates of the reservation. 
Sort output in alphabetical order by room name.
'''

c.execute('''SELECT Rooms.roomName,Reservations.CheckIn,Reservations.CheckOut
          FROM Rooms,Reservations
          WHERE Rooms.RoomId=Reservations.Room AND Reservations.CheckIn  LIKE '%06-FEB-10%' 
         
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["ROOM_NAME","CHECK_IN","CHECK_OUT"]
print(df)

'''
For each stay of GRANT KNERIEN in the hotel, calculate the total amount of money, he paid.
 Report reservation code, checkin and checkout dates, room name (full) and the total amount of money the stay cost.
Sort output in chronological order by the day of arrival.
'''
c.execute('''SELECT   Reservations.Code,Rooms.roomName,Reservations.CheckIn,Reservations.CheckOut,SUM(Reservations.Rate)
          FROM Rooms,Reservations
          WHERE Rooms.RoomId=Reservations.Room AND Reservations.FirstName  LIKE '%GRANT%' AND   Reservations.LastName  LIKE '%KNERIEN%'
         GROUP BY  Rooms.roomName
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","ROOM_NAME","CHECK_IN","CHECK_OUT","TOTAL_AMOUNT"]
print(df)

'''
For each reservation that starts on December 31, 2010 report the room name, nightly rate 
and the total amount of money paid.
 Sort output in descending order by the number of nights stayed.
 '''
c.execute('''SELECT   Reservations.Code,Rooms.roomName,SUM(Reservations.Rate)
          FROM Rooms,Reservations
          WHERE Rooms.RoomId=Reservations.Room AND Reservations.CheckIn  LIKE '%31-DEC-10%' 
         GROUP BY  Rooms.roomName
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=["Code","ROOM_NAME","TOTAL_AMOUNT"]
print(df)
 
c.execute('''DROP TABLE Rooms''')
c.execute('''DROP TABLE Reservations''')
conn.commit()
conn.close()











































































































































































