from xmlrpc.client import boolean


def my_hex(n):
  """ Pozitif ve Negatif sayilarin hex degerini bulur
  """
  if type(n) == float or type(n) == str:
    return f"TypeError: {type(n)} object cannot be interpreted as an integer"
  if type(n)  == int :
    if n >= 0:
        dicto = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"10"}
        if n >=0 and n <=16:
          return "0x"+dicto[n]
        else:
          digit = "0x"
          liste = []
          while True:
            r = n%16
            n = int(n/16)
            liste.append(dicto[r])
            if n == 0:
              break
          for i in liste[::-1]:
            digit += str(i)
          return digit
    else: 
      return "-" + my_hex(-n)
  if type(n)  == bool:
    if n == True:
      return my_hex(1)
    else:
      return my_hex(0)

print(my_hex(12.5))