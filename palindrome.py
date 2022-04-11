text = input("Text :")
text2 = text.lower()
palindrome = [i  for i in text2 if i.isalnum()]
if "".join(palindrome) == "".join(palindrome[::-1]) :
  print(f"{text} is a palindrome")
else:
  print(f" {text} is not a palindrome")