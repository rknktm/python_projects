# -*- coding: utf-8 -*-
print("""
Created on Sun Nov 14 21:02:06 2021

MAp Function
@author: Erkan Öktem
""")
#1. Solution
def area(x):
    return x[0]*x[1]
liste=[(3,4),(10,3),(5,6),(1,9)]

print(list(map(area,liste)))


#2.Solution
def area(i):
    return i[0]*i[1]

liste=[(3,4),(10,3),(5,6),(1,9)]
for i in liste:
   print(liste.index(i),".Area=",area(i))