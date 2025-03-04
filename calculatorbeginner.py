operator = input("Please chose an operator: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    if num2 == 0:
        print("You can't do division with zero")
    else:
        result = num1 / num2
        print(result)
else:
    print("Please choose a valid operator")