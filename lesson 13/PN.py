# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 21:08:32 2022

@author: Mehta Yash
"""

from selenium import webdriver

from time import sleep

from selenium.webdriver.chrome.service import Service

url = " https://www.sbipensionfunds.com/historical-nav/"




browser = webdriver.Chrome(executable_path=( "C:/Users/Mehta Yash/Chromedriver.exe"))

browser.get(url)

sleep(2)

fromdate=browser.find_element("name","fromdate")

fromdate.send_keys("1-1-2021")

todate=browser.find_element("name","todate")

todate.send_keys("18-7-2022")

search= browser.find_element("name","mysubmit")

search.click()

from bs4 import BeautifulSoup as BS


html_page =  browser.page_source

soup = BS(html_page,"html.parser")

my_tab = soup.find('table',class_="table table-hover table-condensed table-bordered")

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]
N=[]
O=[]

for row in my_tab.findAll('tr'):
    cells = row.findAll('td')
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
    F.append(cells[5].text.strip())
    G.append(cells[6].text.strip())
    H.append(cells[7].text.strip())
    I.append(cells[8].text.strip())
    J.append(cells[9].text.strip())
    K.append(cells[10].text.strip())
    L.append(cells[11].text.strip())
    M.append(cells[12].text.strip())
    N.append(cells[13].text.strip())
    O.append(cells[14].text.strip())


import pandas as pd
df=pd.DataFrame()
mydata = zip(A[::-1],B[::-1],C[::-1],D[::-1],E[::-1],F[::-1],G[::-1],H[::-1],I[::-1],J[::-1],K[::-1],L[::-1],M[::-1],N[::-1],O[::-1])
col = [A[0],B[0],C[0],D[0],E[0],F[0],G[0],H[0],I[0],J[0],K[0],L[0],M[0],N[0],O[0]]
df = pd.DataFrame(mydata, columns=col)
df.to_csv("yp.csv", index = False)
browser.quit()















