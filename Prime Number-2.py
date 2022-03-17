
print("""*************************
ASAL SAYI BULMA PROGRAMI
**************************""")
while True:
    sayi=input("bir sayi girin: ")
    if sayi=="1":
        print("Sayi asal degildir")
    elif sayi=="2":
        print("Sayi asaldir")
    elif sayi=="q":
        print("cikiliyor")
        break
    else:
        i=2
        liste=[]
        sayi=int(sayi)
        while i<sayi:
            if sayi % i == 0:
                liste.append(i)
                i+=1
            else:
                i+=1
                
        if len(liste)==0:
            print("Girilen Sayi Asaldir")
           
        else:
            print("Girilen SAyi Asal degildir")
          
               
    
