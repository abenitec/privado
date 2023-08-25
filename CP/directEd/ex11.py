#Boolean Logic + Logical Operators

#take integer input from user and store it in variable x.
x = int(input("What's x? "))
#take integer input from user and store it in variable x.
y = int(input("What's y? "))

#if x greater or lesser to y it print x is not equal to y
if x < y or x > y:
    print("x is not equal to y")
#if x has same value to y it prints x is equal to y
else:
    print("x is equal to y")

#take integer input from the user and store it in variable score  
score = int(input("Score: "))


if score >= 90 and score <= 100:  # If the score is between 90 and 100 (inclusive)
    print("Grade: A")  # Print "Grade: A"
elif score >=80 and score < 90:  # Otherwise, if the score is between 80 and 89 (inclusive)
    print("Grade: B")  # Print "Grade: B"
elif score >=70 and score < 80:  # Otherwise, if the score is between 70 and 79 (inclusive)
    print("Grade: C")  # Print "Grade: C"
elif score >=60 and score < 70:  # Otherwise, if the score is between 60 and 69 (inclusive)
    print("Grade: D")  # Print "Grade: D"
else:  # Otherwise (if the score is less than 60 or greater than 100)
    print("Grade: F")  # Print "Grade: F"

#take integer input from the user(1 or 2) and store it in isStudent 
isStudent = int(input("Are you a student? Press 1 for yes, 2 for no: "))

if not(isStudent == 1 or isStudent == 2):  # If the input is neither 1 nor 2
    print("I don't understand")  # Print "I don't understand"
elif isStudent == 1:  # If the input is 1
    print("Aha! You are a Student!")  # Print "Aha! You are a Student!"
else:  # If the input is 2
    print("Only Students can use this program, Bye!")  # Print "Only Students can use this program, Bye!"