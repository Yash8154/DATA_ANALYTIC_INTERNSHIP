# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:29:48 2022

@author: Mehta Yash
"""

x=input("enter the city name:")
api="https://api.openweathermap.org/data/2.5/weather?q="+x+"&appid=bf86809d415bca7ec51d8e6a941d1e5b"
import requests
b=requests.get(api)
c=b.json()
d=str(c['coord']['lon'])
e=str(c['coord']['lat'])   
api1="http://api.openweathermap.org/data/2.5/air_pollution?lat="+e+"&lon="+d+"&appid=bf86809d415bca7ec51d8e6a941d1e5b"
f=requests.get(api1)
y=f.json()


#'lon': 72.8333, 'lat': 21.1667