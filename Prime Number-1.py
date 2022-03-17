
def asal_mi(sayi):
    if sayi==1:
        return False
    if sayi==2:
        return True
    else:
        for i in range(3,sayi):
            
            if sayi % i==0:
                return False
        return True
    
while True:
    sayi=input("bir sayi girin:")
    if sayi=="q":
        break
    else:
        sayi=int(sayi)
        if asal_mi(sayi):
            print(sayi, "Asaldir")
        else:
            print(sayi,"asal degildir")
        
        

