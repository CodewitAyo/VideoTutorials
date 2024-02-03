num1 = float(input("Enter first number: "))
operator = input("Enter your operators(+,-,*,/): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2
else:
    print("Incorrect syntax")

print(result)

