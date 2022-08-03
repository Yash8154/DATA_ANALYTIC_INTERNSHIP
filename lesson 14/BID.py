# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:38:10 2022

@author: Mehta Yash
"""

import mysql.connector

conn = mysql.connector.connect(user='hpmehta75',password='lifeokyash1799',host='db4free.net',database='yashmehta8799')

c = conn.cursor()

#.cursor is necessary to write because it is used for executing query in database



''' c.execute("""CREATE TABLE TABLE_NAME(
            COLUMN_NAME-DATA_TYPE-NULL/NOT_NULL-KEY
            )""")

---->if you write null correspond to any column no record assined
    but you give no null then record assinged

---->if you do not assinged any key then repeated record consider ex:if you assingned same 
       roll number then it will consider but in reality same roll number is not possible
---->so assinged 'primary_key' to avoid this

'''

c.execute("""CREATE TABLE BID_(
        no INTEGER,
        items TEXT,
        quantity INTEGER,
        departmemt_name TEXT,
        start_dt DATE,
        start_time TIME,
        end_date DATE ,
        end_time TIME
        )"""
        )

conn.commit()


c.execute("INSERT INTO BID_ VALUES('2139881','CORN FLAKES','170','MINISTRY OF DEFENCE','2022-04-28','15:44:00','2022-04-30','16:00:00')")
c.execute("INSERT INTO BID_ VALUES('2129504','Package No. 4 - Atal Tinkering Lab OF NITI AAYOG ...','1','Niti Aayog - National Institution For Transforming India atal innovation mission Sansad Marg Atal Tinkering Lab','2022-04-27','15:07','2022-04-30','16:00')")
c.execute("INSERT INTO BID_ VALUES('2139814','Aerated Water','900','Ministry Of Defence Department Of Military Affairs *********** Indian Army','2022-04-28','15:21','2022-04-30','16:00')")
c.execute("INSERT INTO BID_ VALUES('2137065','Desktop Computers','4','Ministry Of Textiles','2022-04-27','15:38','2022-04-30','16:00')")
c.execute("INSERT INTO BID_ VALUES('2129535','Package No.3 ATAL TINKERING LAB OF NITI AAYOG M...','1','Niti Aayog - National Institution For Transforming India atal innovation mission Sansad Marg Atal Tinkering Lab','2022-04-27','15:04','2022-04-30','16:00')")
c.execute("INSERT INTO BID_ VALUES('2129568','Package No.2: ATAL TINKERING LAB OF NITI AAYOG R… ','1','Niti Aayog - National Institution For Transforming India atal innovation mission Sansad Marg Atal Tinkering Lab','2022-04-27','15:02','2022-04-30','16:00')")
c.execute("INSERT INTO BID_ VALUES('2131389','Digital Signature Certificate','2','Ministry Of Railways','2022-04-25','17:02','2022-04-30','17:00')")
c.execute("INSERT INTO BID_ VALUES('2137405','Dextrose','500','Ministry Of Railways','2022-04-27','16:36','2022-04-30','17:00')")
c.execute("INSERT INTO BID_ VALUES('2126289','Portable Single Operated Rectifier Type Dc Arc Wel...','4','Ministry Of Railways','2022-04-25','13:02','2022-04-30','17:00')")
c.execute("INSERT INTO BID_ VALUES('2137422','Revolving Chair','15','Ministry Of Textiles Delhi Office Of Development Commissioner For Handlooms','2022-04-27','17:02','2022-04-30','17:00')")

conn.commit()




c.execute("SELECT * FROM BID_")
from pandas import DataFrame
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["BID NO","ITEMS","QUANTITY REQUIRED INTEGER", "DEPARTMENT NAME AND ADDRESS","START DATE","START TIME","END DATE","END TIME"]
print(df)


c.execute("DROP Table BID_")
conn.commit()

conn.close()




























































































