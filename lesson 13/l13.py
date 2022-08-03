# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:55:56 2022

@author: Mehta Yash
"""

#case 01
#Kerala Results

from selenium import webdriver

from time import sleep

from selenium.webdriver.chrome.service import Service

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"




browser = webdriver.Chrome(service= Service( "C://Users//Mehta Yash//Chromedriver.exe"))

browser.get(url)

sleep(2)

school_code = browser.find_element("name","treg")

school_code.send_keys('2000')

sleep(2)


get_school_result = browser.find_element("name","bsubmit")

get_school_result.click()

sleep(30)


"""html_page = browser.page_source


from bs4 import BeautifulSoup as BS


soup = BS(html_page)
features="html.parser"""

browser.quit()





#case 02
#We do the scrapping using Selenium

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

browser = webdriver.Chrome(service= Service( "C://Users//Mehta Yash//Chromedriver.exe"))

browser.get(wiki)

right_table = browser.find_elements("name",'wikitable')

A = []
B = []
C = []
D = []
E = []
F = []

for row in right_table.find_element('tr'):
    cells = row.find_element('td')
    states = row.find_element('th')
    
    #if it is first row, th(count) = 7, td(count) = 0
    #for rest of rows, th(count) = 1, td(count) = 6
    
    if len(cells) == 6:
        A.append(cells[1].text.strip())
        B.append(states[0].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
        
import pandas as pd


df = pd.DataFrame()

df['State_UT'] = B
df['Admin_Cap'] = A
df['Legis_Cap'] = C
df['Judi_Cap'] = D
df['Year'] = E
df['Formar_Cap'] = F




