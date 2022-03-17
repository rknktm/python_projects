# -*- coding: utf-8 -*-
print("""
Created on Sun Nov 14 21:52:53 2021

Addition of the Even numbers from the list
@author: Erkan Öktem
""")
from functools import reduce
liste=list()
while True:
    number=input("Enter the number or for Quit Press q:")
    if number=="q":
        break
    else:
        liste.append(int(number))

print(liste)
a=list(filter(lambda x:x%2==0,liste))
print("Even Numbers in the list are",a)
print("Addition of the even numbers is",reduce(lambda x,y:x+y,a))
