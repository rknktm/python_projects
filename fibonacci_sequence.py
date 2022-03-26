# ddition of even numbers  till 100  in fibonacci squence
# first try:

liste = [1,1]
i = 1
while True:
  next = liste[i]+liste[i-1]
  i +=1
  if next > 100 :
    break
  else:
    liste.append(next)
toplam =0
for i in liste:
  if i%2 ==0:
    toplam += i
print(toplam)


# second try:

def my_fibo():
  liste = [1,1]
  while True:
    next = sum(liste[:-1])+1  
    if next > 100 :
      break
    else:
      liste.append(next)
  return  sum([ i for i in liste if not i%2])
print(my_fibo())




