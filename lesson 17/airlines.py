# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:36:30 2022

@author: Mehta Yash
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'airlinesDB.sqlite' )


df1 = pd.read_csv('airlines.csv')
df1.columns =['Id', 'Airline', 'Abbreviation', 'Country']
df1.to_sql('airlines', conn, if_exists='replace', index=False)


df2 = pd.read_csv('flights.csv')
df2.columns = ['Airline', 'FlightNo', 'SourceAirport', 'DestAirport']
df2.to_sql('flights', conn, if_exists='replace', index=False)


df3 = pd.read_csv('airports100.csv')
df3.columns = ['City', 'AirportCode', 'AirportName', 'Country','CountryAbbrev']
df3.to_sql('airports100', conn, if_exists='replace', index=False)


c = conn.cursor()
'''
Find all airlines that have at least one flight out of AXX airport. Report the full name and the abbreviation of each airline.
Report each name only once. Sort the airlines in alphabetical order.
'''

c.execute("""SELECT DISTINCT(airlines.Airline),airlines.Abbreviation
          FROM airlines,flights 
          WHERE airlines.Id=flights.Airline AND flights.SourceAirport LIKE "%AXX%" 
          ORDER BY airlines.Airline
         """)
df = pd.DataFrame(c.fetchall())
df.columns = ["name","abbreviation"]
print(df)


'''
Find all destinations served from the AXX airport by Northwest. 
Report flight number and the full name of the airlne. 
Sort in ascending order by flight number
'''

c.execute("""SELECT flights.FlightNo,airlines.Airline
          FROM airlines,flights 
          WHERE airlines.Id=flights.Airline AND flights.DestAirport LIKE "%AXX%" AND airlines.Abbreviation="Northwest" 
          ORDER BY flights.FlightNo
         """)
df = pd.DataFrame(c.fetchall())
df.columns = ["FlightNo","FullName"]
print(df)


'''
Find all other destinations that are accessible from AHT
flights with exactly one change-over. Report pairs of flight numbers,
airport codes for the final destinations, and full names of the airlines sorted in alphabetical order by the airport code.
'''

c.execute("""SELECT flights.FlightNo,airlines.Airline,flights.DestAirport
          FROM airlines,flights 
          WHERE airlines.Id=flights.Airline AND flights.SourceAirport LIKE "%AHT%" 
          ORDER BY flights.FlightNo
         """)
df = pd.DataFrame(c.fetchall())
df.columns = ["FlightNo","FullName","Destination"]
print(df)



'''
Report all pairs of flightNo served by both Frontier and JetBlue.
Each pair must be reported exactly once.
'''
c.execute("""SELECT flights.FlightNo,airlines.Airline,flights.DestAirport
          FROM airlines,flights 
          WHERE airlines.Id=flights.Airline  AND airlines.Abbreviation="JetBlue" OR airlines.Abbreviation="Frontier"
          ORDER BY flights.FlightNo
         """)
df = pd.DataFrame(c.fetchall())
df.columns = ["FlightNo","AirlineName","Destination"]
print(df)


c.execute(''' DROP TABLE airlines''')
c.execute(''' DROP TABLE flights''')
c.execute(''' DROP TABLE airports100''')


conn.commit()

conn.close()




































































































