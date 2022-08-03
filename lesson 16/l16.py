# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:56:18 2022

@author: Mehta Yash
"""

"""
Database Handling in Python using sqlite - Part 2
"""

import sqlite3
import pandas as pd

'''
Popluate Tables from 
1. cars_data.csv
2. car_names.csv
3. car_makers.csv
'''


# File based database 
# ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'carsdb_.sqlite' )


df = pd.read_csv('car_makers.csv', delimiter=(','))
df.to_sql('car_makers', conn, if_exists='append', index=False)


df = pd.read_csv('cars_data.csv', delimiter=(','))
df.to_sql('cars_data', conn, if_exists='append', index=False)


df = pd.read_csv('car_names.csv', delimiter=(','))
df.to_sql('car_names', conn, if_exists='append', index=False)


c = conn.cursor()


'''
Display how many entries are there in car makers table ?

SELECT 
    COUNT(*) AS total_entry
FROM
    car_makers;
'''
c.execute("""SELECT 
          COUNT(*) AS total_entry 
          FROM car_makers""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_entry"]
print(df)




'''
Display the maximum country code number from car makers table ?

SELECT 
    MAX(car_makers.country) AS max_of_maker
FROM
    car_makers;
'''
c.execute("""SELECT MAX(car_makers.country) AS max_of_maker 
          FROM car_makers""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_of_maker"]
print(df)




'''
Display the minimum country code number  from car makers table ?

SELECT 
    MIN(car_makers.country) AS min_of_maker
FROM
    car_makers;
'''
c.execute("""SELECT MIN(car_makers.country) AS min_of_maker 
          FROM car_makers""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_of_maker"]
print(df)


'''
Popular Aggregate Functions

COUNT()
AVG()
MAX()
MIN()
SUM()
'''



'''
Display the total count of makers from every country  ?

SELECT 
    COUNT(car_makers.car_makersmaker) AS Total_no_of_maker, car_makers.Country
FROM
    car_makers
GROUP BY 
    car_makers.Country;
'''
c.execute("""SELECT COUNT(car_makers.maker) AS Total_no_of_maker , car_makers.Country 
          FROM car_makers 
          GROUP BY car_makers.Country""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Total_no_of_maker", "Country Code"]
df.dropna(inplace = True)
df["Country Code"] = df["Country Code"].astype(int)
print(df)

'''
 1)..Here .astype is similar to type casting but it only appicable when you want whole 
column convert in int data type...it's not applicable for single value for 
single value we use int type typecasting

2)..(.dropna(inplace = True) that use for remove any row which contains null 
     value.
'''


'''
Display count of makers from every country and 
sort them in ascending order of Count of car makers ?


SELECT 
    COUNT(car_makers.maker) AS total_maker, car_makers.Country
FROM
    car_makers
GROUP BY 
    car_makers.Country
ORDER BY 
    COUNT(car_makers.Maker);
'''

c.execute("""SELECT COUNT(car_makers.Maker) AS total_maker, car_makers.Country 
          FROM car_makers 
          GROUP BY car_makers.Country 
          ORDER BY COUNT(car_makers.Maker) DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_maker", "Country"]
print(df) 


'''
ASC   - Ascending is by Default
DESC  - Descending 

'''


'''
SQL DISTINCT basically removes all duplicates
'''

'''
Display all unique Model from the car names table ?


SELECT 
    DISTINCT (car_names.Model)
FROM
    car_names;
'''
c.execute("""SELECT 
          DISTINCT (car_names.Model) 
          FROM car_names""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Model"]
print(df)



'''
Display count of each car maker, 
who have value of Country Code equal to or more than 3  ?

SELECT 
    COUNT(maker) AS total_maker, car_makers.Maker
FROM
    car_makers
WHERE
    car_makers.Country >= 3
GROUP BY 
    car_makers.Maker
ORDER BY
    car_makers.Country;
'''
c.execute("""SELECT COUNT(car_makers.maker) , car_makers.Maker , car_makers.Country
          FROM car_makers 
          WHERE car_makers.Country >= 3 
          GROUP BY car_makers.Maker
          ORDER BY car_makers.Country""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_maker", "Maker", "Country Code"]
print(df)




'''
Find all Reanults (renault) from car names table. 
For each, report the ID, Model, Make and Year. 
Sort output by year.


SELECT 
    car_names.ID, car_names.Model, car_names.Make,  cars_data.Year
FROM 
    car_names, cars_data
WHERE 
    car_names.Model  LIKE '%renault%'
    AND car_names.ID = cars_data.ID
ORDER BY 
    cars_data.Year;
'''

c.execute("""SELECT car_names.ID, car_names.Model, car_names.Make,  cars_data.Year
          FROM car_names, cars_data
          WHERE car_names.Model  LIKE '%renault%'
          AND car_names.ID = cars_data.ID
          ORDER BY cars_data.Year
          """)
df = pd.DataFrame(c.fetchall())
df.columns = ["ID","Model","Make", "Year"]
print(df)



'''
Find all cars produced by Volvo between 1977 and 1981 (inclusive).
Report the name of the car and the year it was produced,
sort output in ascending order by the year.

SELECT 
    car_names.Model, 
    car_names.make,
    cars_data.year
FROM
    car_names,
    cars_data
WHERE
    car_names.Id = cars_data.Id
    AND car_names.model LIKE '%volvo%'
    AND cars_data.year BETWEEN 1977 AND 1981
ORDER BY 
    cars_data.year

'''


c.execute("""SELECT car_names.Model, car_names.make, cars_data.year 
          FROM car_names, cars_data 
          WHERE car_names.Id = cars_data.Id 
          AND car_names.model LIKE '%volvo%'
          AND cars_data.year BETWEEN 1977 AND 1981
          ORDER BY cars_data.year""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Model", "Make","Year"]
print(df)



'''
Find all non-four cylinder cars produced in 1980 that have a better
fuel economy better than 20 MPG and that accelerate to 60 mph faster
than in 15 seconds. 
Report the name of the car and the name of the automaker.

SELECT 
    car_names.Model,
    car_names.make,
    cars_data.year
FROM
    car_names,
    cars_data
    
WHERE car_names.Id = cars_data.Id 
      AND cars_data.Cylinders != 4
      AND cars_data.Year = 1980
      AND cars_data.Accelerate >= 15
      AND cars_data.MPG >= 20
      AND cars_data.Horsepower>60
'''

c.execute("""SELECT car_names.Model, car_names.make, cars_data.year 
          FROM car_names, cars_data 
          WHERE car_names.Id = cars_data.Id 
          AND cars_data.Cylinders != 4 
          AND cars_data.Year = 1980 
          AND cars_data.Accelerate >= 15 
          AND cars_data.MPG >= 20 
          AND cars_data.Horsepower>60""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Model", "Make","Year"]
print(df)




'''
Lets assume that cars which has MPG less than 11 are least fuel efficient
Find all the 8-cylinder least fuel efficient model. 


SELECT 
    car_names.model, 
    cars_data.cylinders, 
    cars_data.MPG
FROM
    cars_data,
    car_names
WHERE
    car_names.Id = cars_data.Id
    AND cars_data.cylinders = 8
    AND cars_data.MPG < 11.0
ORDER BY 
    cars_data.MPG
'''

c.execute("""SELECT car_names.model, cars_data.cylinders, cars_data.MPG
          FROM cars_data, car_names 
          WHERE car_names.Id = cars_data.Id 
          AND cars_data.cylinders = 8
          AND cars_data.MPG < 11.0
          ORDER BY cars_data.MPG
          """)
df = pd.DataFrame(c.fetchall())
df.columns = ["Model", "Cylinders", "MPG"]
print(df)



#Delete the table
c.execute("""DROP TABLE cars_data""")
c.execute("""DROP TABLE car_names""")
c.execute("""DROP TABLE car_makers""")
conn.commit()


conn.close()


'''
FULL SQL STATEMENT  

1.  SELECT
2.  FROM
3.  WHERE
4.  ORDER BY

5.  GROUP BY

6.  HAVING
7.  JOIN
8.  LIMIT

'''


'''
Code Challenges 
1. Bakery
2. csufee
3. enrollment
4. student
5. students
6. zoo
'''
