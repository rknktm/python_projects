# -*- coding: utf-8 -*-
print("""
Created on Sun Nov 14 20:37:51 2021

Finding Factoriyel of given number
@author: Erkan Öktem""")

liste=list()
from functools import reduce
number=int(input("Enter a number: "))
for i in range (1,number+1):
    liste.append(i)
result=reduce (lambda x,y : x*y,liste)
print("Factoriel of the given number is",result)
 

