number = float(input("Enter in a number: "))
if number % 2 == 0:
    answer = "even"
elif number % 2 == 1:
    answer = "odd"
else:
    answer = "invalid"
    print("incorrect syntax")
print(number, "is an ", answer, " number")
