student_age = int(input("How old are you? "))
if student_age >= 18:
    print("Congrats! You are old enough to vote!")
elif student_age <= 10:
    print("Try again in 8 years.")
else:
    print("Ineligible to vote.")


 student_age1 = int(input("How old are you? "))
if student_age1 < 18:
    if student_age1 > 7 and student_age1 < 12:
        print("You are in elementary school!")
