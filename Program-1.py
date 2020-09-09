num1 = int(input("Enter the first number\n"))
operator = input("Enter the operator \n")
num2 = int(input("Enter the second number\n"))

if "+" in operator:
   print(num1+num2)

elif "*" in operator:
    print(num1*num2)
elif "/" in operator:
    print(num1/num2)
elif "-" in operator:
    print(num1-num2)

