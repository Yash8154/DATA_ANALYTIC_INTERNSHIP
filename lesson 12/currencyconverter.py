# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:00:53 2022

@author: Mehta Yash
"""

api1="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=5dd2af13197cfa5ace63"
import requests
b=requests.get(api1)
c=b.json()


