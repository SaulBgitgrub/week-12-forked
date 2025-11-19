# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a == b)   # False. Checks equality
print(a != b)   # True. Checks if it is not equal to another value
print(a > b)    # False. Checks if greater than another value
print(a < b)    # True. Checks if less than another value.
print(a >= b)   # False. Checks if greater than or equal to.
print(a <= b)   # True. Checks for less than or equal to.


#predict the output of the following comparisons:
10 > 5 #Output true
7 == 2 * 3 + 1 #Outpuit true
8 != 8 #Output false
4 <= 2 + 2 #Output True

# Write 3 examples that result in True and 3 that result in False.
10 > 6 #Output true
8 == 2 * 3 + 2 #Output true
9 != 2 #Output true

5 > 6 #Output false
10 != 10 #Output false
5 == 8 - 1 #Output false

# Create a simple grade-checking condition:
score = int(input("What is your score? "))
#Make this program for all grading spectrums
# IF the score is between 90 - 100 .. you got an A
# If the score is between 80 - 89... you got a B
# IF the score is between 70 - 79 .. you got a C
# IF the score is between 60 - 69 .. you got a D
# IF the score is < 60 .. you got an F
if score >= 90 and score <= 100:
    print("You got an A")
elif score >= 80 and score < 90:
    print("You got an B")
elif score >= 70 and score < 80:
    print("You got an C")
elif score >= 60 and score < 70:
    print("You got an D")
elif score < 60:
    print("You got an F")
if score >= 60:
    print("You passed the test")
else:
    print("You didn't pass")


# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
# # The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

#1. Student Score
Score2 = int(input("What is your score: "))
if Score2 <= 100 and Score2 >= 60:
    print("You passed the test")
elif Score2 > 100:
    print("You failed the test")

#2. Ask for password
password = input("What is your password ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is invalid.")
