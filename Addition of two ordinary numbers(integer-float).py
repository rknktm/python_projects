
#Addition ogf two numbers: While Try-Except
while True:
    try:
      a , b = eval(input("1.Sayi:")) , eval(input("2.Sayi:"))
      print("Girilen sayilarin toplami:",a+b)
      break
    except:
      print("hatali veri girisi,tekrar deneyin...")