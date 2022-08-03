# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:08:11 2022

@author: Mehta Yash
"""

class Book:
    def __init__(self,last_name,first_name,title_name,place_name,publisher_name,year_no):
        self.first=first_name
        self.last=last_name
        self.place=place_name
        self.publisher=publisher_name
        self.title=title_name
        self.year=year_no
    def write_bib_entry(self):
        return self.last \
               + ', ' + self.first \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
beauty=Book("Dubay","Thomas","The Evidential Power of Beauty","San Francisco","Ignatius Press","1999")
pynut=Book("Martelli","Alex","Python in a Nutshell","Sebastopol, CA","O′Reilly","2017")
print(pynut.write_bib_entry())
beauty.year="2021"
print(beauty.write_bib_entry())











