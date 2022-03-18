
#Addition ogf two numbers: While Try-Except
while True:
    try:
      a , b = eval(input("First Number:")) , eval(input("Second Number:"))
      print(f"Addition of two entered numbers {a} + {b} =",a+b)
      break
    except:
      print("Value Error, please try again.")