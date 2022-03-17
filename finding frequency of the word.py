# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:07:19 2021
Finding Frequency of a Word in the Text
@author: Erkan Öktem
"""
class Text():
    def __init__(self):
        
      self.liste=list()
      with open("text.txt","r",encoding="utf-8") as file:
           content=file.read()
           simple_content=list(content.split(" "))
           for i in simple_content:
               i=i.strip()
               i=i.strip(",")
               i=i.strip("\n")
               i=i.strip(".")
               i=i.strip("(")
               i=i.strip(").")
               i=i.strip(".[1][2]")
               i=i.lower()
               self.liste.append(i)
    def frequency_word(self,x):
        return self.liste.count(x)
    
    def frequency_all_world(self):
        new_liste=list()
        for i in self.liste:
            if i not in new_liste:
                new_liste.append(i)
                print( f" '{i}' word are there {self.liste.count(i)} times in the text.")
                print("**************************************")
            
                
            
       
                
            

                
            
           

               
words=Text()
#x=input("Enter the word:")
#print(words.frequency_word(x))

words.frequency_all_world()
              