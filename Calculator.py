print("""Menu \n*********************""")
print ("1-Addition\n2-Substraction\n3-Division\n4-Multipication")
while True:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    n=int(input("What would you like to perform:"))
    if n ==1:
        print(f"Addition of two numbers ===> {a}+{b} =",a+b)
        break
    if n ==2:
        print(f"Substraction of two numbers ===> {a}-{b} =",a-b)
        break
    if n ==3:
        print(f"Division of two numbers ===> {a}/{b} =",a/b)
        break
    if n ==4:
        print(f"Multipication of two numbers ===> {a}*{b} =",a*b)
        break
    else:
        print("Please enter a valid number.")
        
