# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:44:59 2022

@author: DELL
"""

'''
 1.Author's Books having Maximum rating: 4.9 
 '''
import pandas as pd

df=pd.read_csv("bestsellers with categories.csv")

a=df[df["User Rating"]==4.9]

b=a.groupby(["Author"]).size().reset_index(name="Count")

'''
  2.plot the bar graph of most expensive books by seaborn
'''
import seaborn as sns

x= df.groupby("Name").Price.mean().sort_values(ascending= False).head(5)
sns.barplot(x.values,x.index)



yash=[2,4,6,7,2,5,20,65]
a=[0,0,0,0]
for i in yash:
    if i >5:
        a[0]+=1
    elif i>10:
        a[1]+=1
    elif i>15:
        a[2]+=1
    elif i>20:
        a[3]+=1


'''
  3.group the user rating data in 4 cateogeory and plot the bar graph
'''
import matplotlib.pyplot as plt
popularity = [0,0,0,0]
for i in df["User Rating"]:
    if i >= 4.8:
        popularity[0] += 1
    elif i >= 4.5:
        popularity[1] += 1
    elif i >= 4.0:
        popularity[2] += 1
    else:
        popularity[3] += 1
x = ['Extremely Popular(4.8, 4.9)','Very Popular(4.4 - 4.7)','Fairly Popular(4.0 - 4.3)','Popular (- 3.9)']
plt.bar(x, popularity, color = "green")  
plt.show()

'''
4.Top rated books (Revieved by at least 50000 people)
'''
top_rating = df.groupby(['Name', 'Author', 'Genre'], as_index=False)[['User Rating', 'Reviews']].mean()
top_rating = top_rating[top_rating['Reviews']>50000]
top_rating = top_rating.sort_values('Reviews', ascending=False).head()
top_rating


'''
5.How many are fiction and non fiction Show both in numbers adn Graphically using a Pie Chart
'''
df["Genre"].value_counts()
pie_1 = df.drop_duplicates('Name').sort_values('Reviews',ascending=False)['Genre'].head(10).value_counts()
plt.pie(pie_1,explode = [0,0.15],labels=['Fiction','Non Fiction'],autopct='%.1f%%',shadow=True,startangle=0)
plt.title('Genre Pie Chart for the top 10 Bestselling Books on Amazon (2009-2019)',y=0)



'''
 6.get the number of count by year wise of fiction and nonofiction genre and merge both
'''
year = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
num_fic= []
for i in year:
    fic = df[(df["Year"] == i) & (df["Genre"] == "Fiction")]
    num_fic.append(len(fic))
df_fict = pd.DataFrame({"Year": year,"numberofFiction": num_fic})

year = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
num_nonfic= []
for i in year:
    nonfic = df[(df["Year"] == i) & (df["Genre"] == "Non Fiction")]
    num_nonfic.append(len(nonfic))
df_nonfict = pd.DataFrame({"Year": year,"numberofNonFiction": num_nonfic})

pd.merge(df_fict,df_nonfict)


















































