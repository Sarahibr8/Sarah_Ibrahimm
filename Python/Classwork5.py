# Classwork 1 — Pass or fail
#
# Task:
#   Ask the user for a test score (0 to 100).
#   If the score is 50 or above, print "Pass".
#   Otherwise, print "Fail".

# Write your code below:

score = int(input("Enter your score(0-100):"))
if score >= 50:
    print("Pass")
else:
    print("Fail")

# Classwork 2 — Even or odd
#
# Task:
#   Ask the user for a number.
#   Print "<number> is even" or "<number> is odd".
#
# Hint: a number is even if (number % 2 == 0).

# Write your code below:

number = int(input("Enter your number:"))
if number %2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is old")

# Classwork 3 — Largest of three
#
# Task:
#   Ask the user for THREE numbers.
#   Print the largest one. (Don't use the built-in max() function — use if/elif/else.)
#
# Example:
#   First:  10
#   Second: 25
#   Third:  17
#   The largest is 25

# Write your code below:

number1 = int(input("First number:"))
number2 = int(input("Second number:"))
number3 = int(input("Third number:"))

if number1 >= number2 and number1 >= number3:
    print(f"The Largest is{number1}")
elif number2 >= number1 and number2 >= number3:
    print(f"The largest is {number2}")
else:
    print(f"The largest is {number3}")

# Classwork 4 — Letter grade
#
# Task:
#   Ask the user for a numeric mark (0 to 100), then print the letter grade:
#       90+      → A
#       80-89    → B
#       70-79    → C
#       60-69    → D
#       below 60 → F
#
#   Use if / elif / else.

# Write your code below:
marks = int(input("Enter your mark (0-100):"))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# Homework 3 — Login check
#
# Task:
#   The correct username is "admin" and password is "1234".
#
#   Ask the user for a username AND a password.
#   - If BOTH match, print "Login successful".
#   - If username matches but password does not, print "Wrong password".
#   - Otherwise, print "Unknown user".
#
#   Use AND, OR, and nested if statements as needed.

# Write your code below:
username = input("Enter your username")
password = input("Enter your password")

if username == "admin" and password == "1234":
    print("Login successful")

elif username == "admin" and password != "1234":
    print("Wrong password")

else:
    print("Unknown user")

# Homework 4 — Triangle classification
#
# Task:
#   Ask the user for the lengths of three sides of a triangle (a, b, c).
#   Decide what kind of triangle it is:
#     - If all three are equal → "Equilateral"
#     - If exactly two are equal → "Isosceles"
#     - Otherwise → "Scalene"
#
#   Print the result.

# Write your code below:
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third sid: "))

if side1 == side2 and side2 == side3:
    print("Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
else:
    print("Scalene")
