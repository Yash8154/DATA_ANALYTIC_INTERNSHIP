# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:54:36 2022

@author: Mehta Yash
"""

"""
Database Handling in Python using sqlite - Part 1
"""

'''
1. Connect to the Database
2. Cursor ( bridge )
3. Execute SQL Statements
4. Process the results
5. Close the connection
'''


import sqlite3
import pandas as pd

'''
Create a Database and Use it

CREATE DATABASE carsdb;
USE carsdb;
'''

# File based database 
# ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'carsdb.sqlite' )


# creating cursor
c = conn.cursor()



'''
Create a Table carMakers 

CREATE TABLE carMakers(
    Maker VARCHAR(20),
    FullName VARCHAR (30),
    Country int(3)
    );
'''
'''
varchar ()
int(3)  
bigint
float   
'''

# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE carMakers(
          Maker  TEXT,
          FullName TEXT,
          Country int(3)
          )"""
          )
conn.commit()



'''
Insert Data into the carMakers Table

INSERT INTO carMakers(Maker,FullName,Country) 
VALUES ('amc','American Motor Company',1);

INSERT INTO carMakers(Maker,FullName,Country) 
VALUES ('volkswagen','Volkswagen',2);

INSERT INTO carMakers(Maker,FullName,Country) 
VALUES ('bmw','BMW',2);

INSERT INTO carMakers(Maker,FullName,Country) 
VALUES ('gm','General Motors',1);

INSERT INTO carMakers(Maker,FullName,Country) 
VALUES ('chrysler','Chrysler',1);
'''


c.execute("""INSERT INTO carMakers VALUES ('amc','American Motor Company',1)""")
c.execute("""INSERT INTO carMakers VALUES ('volkswagen','Volkswagen',2)""")
c.execute("""INSERT INTO carMakers VALUES ('bmw','BMW',2)""")
c.execute("""INSERT INTO carMakers VALUES ('gm','General Motors',1)""")
c.execute("""INSERT INTO carMakers VALUES ('chrysler','Chrysler',1)""")
conn.commit()



'''
SELECT * 
FROM carMakers;
'''

c.execute("""SELECT * 
          FROM carMakers""")




# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns two or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of all tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("""SELECT * 
          FROM carMakers""")



df = pd.DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Maker","FullName","Country"]
df.to_csv("car.csv", index=False)
print(df)


#Delete the table
c.execute("""DROP TABLE carMakers""")
conn.commit()


# closing the connection 
conn.close()


#print ( c.fetchone()) 





'''
Popluate Table from carMakers.csv 
'''

import sqlite3
import pandas as pd

# File based database 
# ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'carsdb.sqlite' )


df = pd.read_csv('carMakers.csv', delimiter=(';'))
df.to_sql('carMakers', conn,  if_exists='replace', index=False)     
c = conn.cursor()
print(c.description)

'''
Display all columns data of all the rows from the carmakers table ?

SELECT * 
FROM carMakers;
'''
c.execute("""SELECT * 
          FROM carMakers""")
print(c.description)
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



    

'''
Display car makers and their country code from carMakers table ?

SELECT Maker, Country 
FROM carMakers;
'''
c.execute("""SELECT Maker, Country 
          FROM carMakers""")
df = pd.DataFrame(c.fetchall()) 
df.columns = ["Maker", "Country"]
print(df)




'''
Display fullName of all car makers from carMakers table ?

SELECT FullName FROM carMakers;
'''
c.execute("""SELECT FullName 
          FROM carMakers""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FullName"]
print(df)



'''
Select all car makers name who has country code 4 from carMakers table ?


SELECT Maker, FullName , Country
FROM carMakers 
WHERE country = 4;
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country = 4""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)


'''
0   == Missing Country
1   == USA              ( America )
2   == Germany          ( Europe  )
3   == France           ( Europe  )
4   == Japan            ( Asia    )
5   == Italy            ( Europe  )
6   == Sweden           ( Europe  )
7   == United Kingdom   ( Europe  )
8   == Korea            ( Asia    )
'''




'''
Operator 	Description 	
    = 	    Equal 	
    !=      Not Equal
    > 	    Greater than 	
    < 	    Less than 	
    >= 	    Greater than or equal 	
    <= 	    Less than or equal 	
    <> 	    Not equal 
    BETWEEN Between a certain range 	
    LIKE 	Search for a pattern 	
    IN 	    To specify multiple possible values for a column
'''


'''
Select all car makers name who has country code 2 and 5 from carMakers table ?

SELECT Maker, FullName , Country 
FROM carMakers 
WHERE country IN (2,5);
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country IN (2,5)""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name who does not have  country code 2 and 5 from carMakers table ?

SELECT Maker, FullName , Country
FROM carMakers 
WHERE country !=2 AND 5;
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country !=2 AND 5""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name whose country code is greater than 2 from carMakers table ?

SELECT Maker, FullName , Country 
FROM carMakers 
WHERE country >2;
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country >2""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name whose name contains first letter as h from carMakers table ?

SELECT Maker, FullName , Country
FROM carMakers 
WHERE maker LIKE "h%";
'''
c.execute("""SELECT Maker, FullName , Country 
          FROM carMakers 
          WHERE maker LIKE 'h%'""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)


'''
Select all car makers name whose fullName ends with da from carMakers table ?

SELECT Maker, FullName , Country 
FROM carMakers 
WHERE FullName LIKE "%da";
'''
c.execute("""SELECT Maker, FullName , Country 
          FROM carMakers 
          WHERE FullName LIKE '%da'""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name whose name exactly 4 characters from carMakers table ?

SELECT Maker, FullName , Country 
FROM carMakers 
WHERE maker LIKE "____";
'''
c.execute("""SELECT Maker, FullName , Country  
          FROM carMakers 
          WHERE maker LIKE '____'""")
df = pd.DataFrame(c.fetchall()) 
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)


'''
-- AND returns every row where all the conditions are true.
-- OR returns every row where at least one of the conditions is true.
'''


'''
Select all car makers name who has country code 2 or whose name ends with en from carMakers table ?

SELECT Maker, FullName , Country
FROM carMakers 
WHERE country = 2 OR maker LIKE '%en';
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country = 2 OR maker LIKE '%en'""")
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)




'''
Select all car makers name whose country code are 2,3,4,5 from carMakers table ?

SELECT Maker, FullName , Country
FROM carMakers 
WHERE country IN (2,3,4,5);
'''
c.execute("""SELECT Maker, FullName , Country
          FROM carMakers 
          WHERE country IN (2,3,4,5)""")
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all the car makers that are not 4 characters long from carMakers table ?

SELECT Maker, FullName , Country
FROM carMakers 
WHERE maker NOT LIKE '____';
'''
c.execute("""SELECT Maker, FullName , Country 
          FROM carMakers 
          WHERE maker NOT LIKE '____'""")
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name where country code is null?

SELECT Maker, FullName , Country  
FROM carMakers 
WHERE country LIKE 'NULL';
'''
c.execute("""SELECT Maker, FullName , Country 
          FROM carMakers 
          WHERE country LIKE NULL""")
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
Select all car makers name whose country code between 2 and 5 from carMakers table ?

SELECT Maker, FullName , Country 
FROM carMakers 
WHERE country BETWEEN 2 AND 5;
'''
c.execute("""SELECT Maker, FullName , Country 
          FROM carMakers 
          WHERE country BETWEEN 2 AND 5""")
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



'''
sort car makers table with their country code?

SELECT * 
FROM carMakers 
ORDER BY country ASC;
'''
c.execute("""SELECT * 
          FROM carMakers 
          ORDER BY country ASC""") #DESC for descending
df = pd.DataFrame(c.fetchall())
if(len(df.columns==4)):
    df.columns = ["Maker","FullName","Country"]
print(df)



#Delete the table
c.execute("""DROP TABLE carMakers""")
conn.commit()


conn.close()


'''
FULL SQL STATEMENT  

1.  SELECT
2.  FROM
3.  WHERE
4.  ORDER BY

5.  HAVING
6.  GROUP BY
7.  JOIN
8.  LIMIT

'''




'''
Code Challenges 
1. bakery
2. flights
3. reservations
4. students
5. zoo
'''
