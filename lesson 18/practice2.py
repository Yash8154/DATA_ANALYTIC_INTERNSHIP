# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:37:20 2022

@author: Mehta Yash
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'practice2DB' )


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



df8 = pd.read_csv('csufee.csv')
df8.to_sql('csufees', conn, if_exists='replace', index=False)





df11 = pd.read_csv('list.csv')
df11.to_sql('list', conn, if_exists='replace', index=False)


df12 = pd.read_csv('teachers.csv')
df12.to_sql('teachers', conn, if_exists='replace', index=False)

df13 = pd.read_csv('appellations.csv')
df13.to_sql('appellations', conn, if_exists='replace', index=False)


df14 = pd.read_csv('grapes.csv')
df14.to_sql('grapes', conn, if_exists='replace', index=False)


df15 = pd.read_csv('wine.csv')
df15.to_sql('wine', conn, if_exists='replace', index=False)

df16 = pd.read_csv('car_names.csv')
df16.to_sql('car_names', conn, if_exists='replace', index=False)


df17 = pd.read_csv('cars_data.csv')
df17.to_sql('cars_data', conn, if_exists='replace', index=False)

df18 = pd.read_csv('car_makers.csv')
df18.to_sql('car_makers', conn, if_exists='replace', index=False)

df19 = pd.read_csv('bakery1.csv',delimiter=";")
df19.to_sql('goods', conn, if_exists='replace', index=False)

c = conn.cursor()

'''
Select all flights whose airline number is 3 from ?
'''
c.execute('''SELECT * FROM flights WHERE flights.Airline=3''')
df=pd.DataFrame(c.fetchall())
df.columns=["AIR_LINE_NO","FLIGHT_NO","S_AIRPORT","D_AIRPORT"]
print(df)

'''
Display count of every Food from bakery table ?
'''
c.execute('''SELECT COUNT(goods.Food) 
          FROM goods 
        ''')
df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_FOOD"]
print(df)

'''
Display How many entries are there in car_makers table ?
'''
c.execute('''SELECT COUNT(car_makers.Maker) 
          FROM car_makers 
          
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["NO_OF_MAKER"]
print(df)

'''
Display average number of car_makers from country 2 ?
'''
c.execute('''SELECT AVG(car_makers.Maker) 
          FROM car_makers 
          WHERE car_makers.Country=2
         
          
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["AVG_MAKER"]
print(df)

'''
Display the total price of Each Flavour ?
'''

c.execute('''SELECT    goods.Flavor,SUM(goods.Price) 
          FROM goods 
         GROUP BY goods.Flavor
         
          
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["FLAVOR","TOTAL_PRICE"]
print(df)


'''
Display the maximum country code number ?
'''
c.execute('''SELECT    MAX(car_makers.Country)
          FROM  car_makers
        
         
          
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["MAX_C_CODE"]
print(df)


'''
Display the minimum country code number   ?
'''

c.execute('''SELECT    MIN(car_makers.Country)
          FROM  car_makers
        
         
          
          ''')

df=pd.DataFrame(c.fetchall())
df.columns=["MIN_C_CODE"]
print(df)

'''
Display average price for Cake or Eclair?
'''
c.execute('''SELECT    goods.Food,AVG(goods.Price)
          FROM  goods
        WHERE goods.Food LIKE '%Eclair%' OR goods.Food LIKE '%Cake%'
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["FOOD","AVG_PRICE"]
print(df)

'''
Display the maximum price of each Food
'''

c.execute('''SELECT    goods.Food,MAX(goods.Price)
          FROM  goods
       GROUP BY  goods.Food
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["FOOD","MAX_PRICE"]
print(df)

'''
Display the minimum price of each Flavour ?
'''

c.execute('''SELECT    goods.Flavor,MIN(goods.Price)
          FROM  goods
       GROUP BY  goods.Flavor
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["FLAVOR","MIN_PRICE"]
print(df)

'''
Display count of each Food, 
   which have Chocolate Flavour , 
   also arrange food's name in alphabetical order
'''
   
c.execute('''SELECT    goods.Food,COUNT(goods.Food)
          FROM  goods
          WHERE goods.Flavor LIKE '%Chocolate%'
       GROUP BY  goods.Food
       ORDER BY goods.Food
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["FOOD","NO_OF_VARIETY"]
print(df)

'''
Find all non-four cylinder cars produced in 1980 that have a better
 fuel economy better 
than 20 MPG and that accelerate to 60 mph faster
than in 15 seconds.
'''
c.execute('''SELECT   car_names.Model
          FROM  car_names,cars_data
          WHERE car_names.Id=cars_data.Id AND cars_data.Year=1980 AND cars_data.MPG>20 AND cars_data.Accelerate<=15 AND cars_data.Cylinders!=4
    
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["MODEL_NAME"]
print(df)

'''
Find all cars produced by Volvo between 1977 and 1981 (inclusive).

Report the name of the car and the year it was produced,
sort output
 in ascending order by the year.
'''
c.execute('''SELECT   car_names.Model,cars_data.Year
          FROM  car_names,cars_data
          WHERE car_names.Id=cars_data.Id AND cars_data.Year BETWEEN 1977 AND 1981 AND car_names.Model LIKE '%Volvo%' 
          GROUP BY cars_data.Year
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["MODEL_NAME","YEAR"]
print(df)

'''
Display average grade for each classroom from students table in descending order ?
'''

c.execute('''SELECT   list.Classroom,AVG(list.Grade)
          FROM  list
         
          GROUP BY  list.Classroom
          ORDER BY  list.Classroom
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["C_ROOM","AVG_GRADE"]
print(df)

'''
Display the maximum grade of each classroom from students table and sort them by maximum grade ?
'''

c.execute('''SELECT   list.Classroom,MAX(list.Grade)
          FROM  list
         
          GROUP BY  list.Classroom
          ORDER BY  MAX(list.Grade)
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["C_ROOM","MAX_GRADE"]
print(df)

'''
Display the grade, Firstname, Secondname and classroom of top 3 students according to their grade 
'''
c.execute('''SELECT   list.FirstName,list.LastName, list.Classroom,list.Grade
          FROM  list
         
         
          ORDER BY  list.Grade DESC LIMIT 3
        ''')

df=pd.DataFrame(c.fetchall())
df.columns=["F_NAME","L_NAME","C_ROOM","GRADE"]
print(df)


conn.close()


































































































































