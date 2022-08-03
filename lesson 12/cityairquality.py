# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:06:00 2022

@author: Mehta Yash
"""

x=input("enter the city name:")
api1="http://api.openweathermap.org/geo/1.0/direct?q="+x+"&appid=bf86809d415bca7ec51d8e6a941d1e5b"
import requests
a=requests.get(api1)
c=a.json()
d=c['lat']
e=c['lon']