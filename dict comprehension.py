#Counting letters in a given text

#solution-1

text = input("Text:").lower().split(" ")
dicto ={}
count =0
for word in text:
  for letter in word:
    if letter in dicto.keys():
      dicto[letter] += 1
    else:
      dicto[letter]=1
print(dicto)


#solution-2

def my_dicto():
  txt = input("Text:").lower()
  dicto = {v:txt.count(v)  for v in set(txt) if v.isalpha()}
  return dicto
print(my_dicto())

#Using of dict compherension

#d = {k:v for k, v in iterable}
# {k: v for k, v in blahs if not int(k[-1]) % 2}


