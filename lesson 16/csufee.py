# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:15:58 2022

@author: Mehta Yash
"""

import sqlite3 as sql

import pandas as pd

conn=sql.connect("csufeedb")

df=pd.read_csv("csufee.csv",delimiter=(','))

df.to_sql("csufee",conn,if_exists="replace",index=False)

c=conn.cursor()

'''
 Display How many entries are there in csufee table ?
 '''
c.execute('''SELECT COUNT(*) FROM csufee ''')
df=pd.DataFrame(c.fetchall())
df.columns=["No.of.records"]
print(df)

'''
Display average number of CampusFee from campus 2,  from csufee table ?
'''

c.execute('''SELECT csufee.Campus,AVG(csufee.CampusFee) FROM csufee
          WHERE Campus=2 
          GROUP BY (csufee.Campus)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=['CAMPUS',"AVG_FEE_OF_C-2"]
print(df)

'''
Display the maximum campus code number from csufee table ?
'''
c.execute('''SELECT MAX(csufee.Campus) FROM csufee
        
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=[' MAX_CAMPUS']
print(df)

'''
 Display the minimum campus code number  from csufee table ?
 '''
c.execute('''SELECT MIN(csufee.Campus) FROM csufee
        
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=[' MIN_CAMPUS']
print(df)
 
'''
Display count number of totalcsufee_AYs from every campus  ?
'''
c.execute('''SELECT csufee.Campus,COUNT(csufee.CampusFee) FROM csufee
            GROUP BY (csufee.Campus)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=['CAMPUS','TOTAL_FEES_STR.']
print(df)


'''
 Display the maximum campus fee from csufee table ?
'''
c.execute('''SELECT csufee.Campus,MAX(csufee.CampusFee) FROM csufee
           
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=['CAMPUS','MAX_FEES_STR.']
print(df)
 
'''
  Display the minimum campus code from csufee table ?
  '''

c.execute('''SELECT MIN(csufee.Campus) FROM csufee
           
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=['MIN_CAMPUS']
print(df)

'''
 Display count of totalcsufee_AYs from every campus and sort them in ascending order from csufee table ?
 '''
 
c.execute('''SELECT csufee.Campus,SUM(csufee.CampusFee) FROM csufee
           GROUP BY csufee.Campus 
           ORDER BY SUM(csufee.CampusFee)
          ''')
df=pd.DataFrame(c.fetchall())
df.columns=['Campus','Total_Fee']
print(df)


'''
 Display totalcsufee_AY column from csufee table without duplicates ?
 '''

c.execute("""SELECT DISTINCT(CampusFee) FROM csufee;""")
df = pd.DataFrame(c.fetchall())
df.columns = ["CampusFee"]
print(df)

'''
 Display count of each car totalcsufee_AY , who have value of campus equal to or more than 3  ?
 '''
c.execute("""SELECT campus,COUNT(*) AS totalcsufee_AY FROM csufee WHERE campus>=3 Group BY Campus;""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Campus","totalcsufee_AY"]
print(df) 


c.execute('''DROP TABLE csufee''')
conn.commit()
conn.close()






























































































































































































































