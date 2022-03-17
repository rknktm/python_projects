print("""Hesap MAkinasi Programi\n*********************************""")
print ("1-Toplama\n 2-Cikarma\n 3-Bolme\n 4-CArpma")

a=int(input("1.sayiyi girin:"))
b=int(input("2.sayiyi girin:"))
islem=int(input("isleminizi secin:"))
if islem ==1:
    print("toplam=",a+b)
if islem ==2:
    print("cikarma=",a-b)
if islem ==3:
    print("bolme=",a/b)
if islem ==4:
    print("Carpma=",a*b)
else:
    print("gecerli bir islem secin")