            #  CONTINUE

# i=0
# while i<10:
#     if i==5:
#         i+=1
#         continue #alti görmez uste döner
#     print(i)
#     i+=1

            #LIST COMPREHENSION
#liste=[1,2,3,4,5]
#listekare=[i*i for i in liste] #list comprehension
#print(listekare)

# liste=[[1,2,3],[5,6,7]]
# liste2=[ x for i in liste for  x in i]
# print(liste2)

                #FAKTORIYEL BULMA

# while True:
#     i=1
#     sayi=input("bir sayi girin yada cikmak icin q ya basin:")
#     if sayi=="q":
#         break
#     else:
#         faktor=int(sayi)
#         for k in range(1,int(faktor+1)):
#             i=k*i
#         print(i)
            
            
# print("cikma islemi gerceklesiyor")


                #FIBONACCI
# liste=[1,1]
           
# sayi=int(input("bir sayi girin:"))
# for k in range (1,sayi+1):
#     a=liste[k-1]+liste[k]
#     if a<=sayi:
#         liste.append(a)
#     else:
#         break              
# print(liste)
    
            #CARPIM TABLOSU
# for i in range (1,11):
#     print("{} ler Carpim Tablosu".format(i))
#     print("*******************************")
    
#     for k in range(1,11):
#         print("{}*{}={}".format(i,k,i*k))
 
            #INSERT METODU ::: Belirtilen indexe eleman ekler

# liste=[11,23,43,56]
# liste.insert(1,"eco")
# print(liste)

            # POP METODU :::: BELIRTILEN INDEX SILINIR... verilmezse sondaki silinir
# liste=[11,23,43,56]
# # liste.pop()
# # #print(liste)

# help(liste.append)

            #FONKSIYON YAZMA
#örnek-1

# def selam(isim):
#     print("merhaba",isim)
    
# selam("erkan")

#ornek-2
# def selam(isim):
#     print("merhaba",isim)
    
# isim=input("ismi giriniz")
# selam(isim)

#ornek-3
# def faktoriyel(sayi):
#     if sayi==0 or sayi==1:
#         print("{} sayisinin faktoriyeli 1'e esittir".format(sayi))
#     else:
#           f=1
#           for j in range(2,sayi+1):
#                 f *= j
#         print("{} sayisinin faktoriyeli {}'e esittir".format(sayi,f))
        
# sayi=int(input("Bir sayi giriniz: "))
#faktoriyel(sayi) 

#örnek 4
# def faktoriyel(sayi):
#     if sayi==0 or sayi==1:
#          print("{} sayisinin faktoriyeli 1'e esittir".format(sayi))
#     else:
#        i=1
#        f=1
#        while i<=sayi:
#             f*=i
#             i+=1
#        print("{} sayisinin faktoriyeli {}'e esittir".format(sayi,f))
        
# sayi=int(input("Bir sayi giriniz: "))
# faktoriyel(sayi)    

 #örmek 5
 
# def toplam(a,b):
#      return a+b
 
# def carpim(c):
#     return c*c
# rtn=toplam(2,5)
# print(carpim(rtn))   #return, cikan sonucu fonk. calistiran komuta gönder...

# def carp(x):
    
#     return x*x

# def topla(y):
    
#     return 10+y

# def cikart(z):
    
#     return abs(z-2)

# print(cikart(topla(carp(5))))

#ornek-6

# def kayit(ad="none",soyad="none",no="none"):

#      print("Bilgiler:\n","Ad:",ad,"\n","Soyad:",soyad,"\n","No:",no)
    
# kayit("Ali","ak","5")

#örnek-7

# def toplam(*a):    sinirsiz degere karsilik gelir
#     for i in a:
#         t+=i
#     return t

# print(toplam(3,4,5,6,7))

    #global yerel
    

# b=5     #global  global yerele etki eder ama yerelde ayni degisken olmamasi lazim
# def glo_yer():
#    b=10   #yerel    yerel globala etki etmez   #global fonk. önce tanimlanmalidir
#     print(b)
# glo_yer()


# b=5
# def glo():
#     global b   #bu ifade ile globale deger atanabilir
#     b=2
#     print(b)
# glo()
# print(b)

                # LAMBDA 

# liste=[1,2,3,4]
# liste2=[i*2 for i in liste]...........liste de i degerine 2 ile carp ve liste2 ye eleman olarak ekle
# print(liste2)

# toplam=lambda x,y,z:x+y+z
# print(toplam(11,2,3))

# s="python"
# print(s[::-1])

# ters=lambda s:s[::-1]
# kelime=input("kelime girin")
# print(ters(kelime))




