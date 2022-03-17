print("""********************
      Geometrik Sekil Bulucu
      **********************""")
s=input("Ucgen mi Dortgen mi:")

if s.capitalize()=="Dortgen":
   d1=int(input("1.Kenari girin"))
   d2=int(input("2.Kenari girin"))
   d3=int(input("3.Kenari girin"))
   d4=int(input("4.Kenari girin"))
   if d1==d2 and d3==d4 and d2==d3:
       print("sekliniz karedir")
       
   elif d1==d2 and d3==d4 or d1==d3 and d2==d4 or d1==d4 and d2==d3: 
       print("sekliniz dikdotgendir")
   else:
       print("dortgendir")

    
elif s.capitalize()=="Ucgen":
    d1=int(input("1.Kenari girin"))
    d2=int(input("2.Kenari girin"))
    d3=int(input("3.Kenari girin"))
    if d1+d2>d3 and abs(d1-d2)< d3 or d2+d3>d1 and abs(d2-d3)< d1 or d1+d3>d2 and abs(d1-d3)< d2:
        if d1==d2 and d1!=d3 or d2==d3 and d2!=d1 or d3==d1 and d3!=d2:
            print("ikizkenar")
        elif d1==d2 and d1==d3:
            print("eskenar")
        else:
            print("cesitkenar")
    else:
        
        print("bu bir ucgen degildir")
else:
    print("Hatali Giris")
    
