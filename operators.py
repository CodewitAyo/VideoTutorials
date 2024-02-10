# This script checks your score and tells you your grade point

score = int(input("Enter your score: "))
if score >= 90:
    Grade = "A"
elif score >= 80:
    Grade = "B"
elif score >= 70:
    Grade = "C"
elif score >= 60:
    Grade = "D"
else:
    Grade = "F"
print("Your grade is: ", Grade)
