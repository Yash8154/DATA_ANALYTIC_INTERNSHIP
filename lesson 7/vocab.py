# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:58:11 2021

@author: Ria
"""
import re

novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt'
          ]

    
length_of_unique_word_in_files=[]
novels_wordlist=[]

#for finding Length of Unique Words
for novelname in novels:
    
    #Opning Each Novel Text File
    fopen=open(novelname,encoding="utf8")
    fread=fopen.read()
    
    #Finding Starting and Ending Position to Read File
    result=re.search(r'START OF',fread)
    startindex=fread.find('\n',result.end())
    result=re.search(r'END OF',fread)
   
    #Substituting Every Non Character in Text File with Space Character
    stringline=re.sub(r"[^a-zA-Z]+", ' ',fread)
    
    #Strip to remove space and split to read individual Word
    temp =stringline.strip().split()
    novels_wordlist.append(temp)
    
    #Finding Length of Unique Word in temp
    lengthofuniquewords=len(set(temp))
    
    #Adding Length of Unique Words in Each Novel to list
    length_of_unique_word_in_files.append(lengthofuniquewords)
    
    fopen.close()

#Finding Total Number of Words in Best Novel
#wordlength_of_best_novel=len()
#Finding Maximium Length in list
max_index=length_of_unique_word_in_files.index(max(length_of_unique_word_in_files))
#Finding List of All Words of Best Novel
best_novel=novels_wordlist[max_index] 
#Finding Name of Best Novel by Measuring Maximium Unique Words
best_novel_name=novels[max_index]

#Assigning Best Novels Complete Word List to Variable best and variable y
best=set(best_novel)
total_words_of_all_novel=set(best_novel)

for novel in novels_wordlist:
    if best_novel!=novel:
        #Finding Unique Words in Best Novels by Comparing with All Novels
        best=set(best)-set(novel)
    
    #Adding Words of All Novels into one(Neglecting the Commom Words by using Set Intersection )
    total_words_of_all_novel=set(total_words_of_all_novel) & set(novel)

#Append Unique Word of Best Novel in Text File        
fopen=open("Unique_Word_File.txt","w")
for word in list(best):
    fopen.write(word)
    fopen.write("\n")
fopen.close()

print("Name of Best Novel( Having Maximium Unique Word ) :",best_novel_name)
print("\nTotal Number of Words in Best Novel : ",len(best_novel))
print("\nNo of Unique Words Best Novel Individually Have : ",max(length_of_unique_word_in_files))
print("\nNo of Unique Words of Best Novel by Comparing with All Novels :",len(best))
print("\nNo of Words Common in All Files :",len(total_words_of_all_novel))
