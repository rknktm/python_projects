# Equivalent of title fucntion
text =input("Enter any text: ").lower().split(" ")
new =str()
for i in range(len(text)):
    title = text[i][0].upper() + text[i][1:] + " "
    new += title
print(new.lstrip(" "))