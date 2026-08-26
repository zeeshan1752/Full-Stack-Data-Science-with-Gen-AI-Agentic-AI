# Python Conditional Statements

# Introduction

age = 20

print(age >= 18)


# if Statement

age = 20

if age >= 18:
    print("You are eligible to vote.")


# if-else Statement

age = 16

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


# if-elif-else Statement

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Multiple Conditions - and

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")


# Multiple Conditions - or

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# Multiple Conditions - not

is_raining = False

if not is_raining:
    print("You can go outside.")


# Nested if Statement

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID is required.")
else:
    print("You are under 18.")


# Comparison Operators

age = 21

if age >= 18:
    print("Adult")


# Boolean Values

is_logged_in = True

if is_logged_in:
    print("Welcome!")


# Truthy and Falsy Values

name = ""

if name:
    print("Name is available.")
else:
    print("Name is empty.")


# Checking Multiple Values using in

day = "Sunday"

if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")


# Conditional Expression / Ternary Operator

age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)


# Conditional Expression Example

a = 10
b = 20

greater = a if a > b else b

print(greater)


# match-case Statement

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# pass in Conditional Statement

age = 20

if age >= 18:
    pass
else:
    print("Minor")


# Conditional Statement with User Input

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Conditional Statement with Strings

password = "python123"

if password == "python123":
    print("Correct password.")
else:
    print("Incorrect password.")


# Positive, Negative or Zero

number = 10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# Nested if vs Logical Operator

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")


# Basic Structure

# if condition:
#     # code
#     pass

# elif another_condition:
#     # code
#     pass

# else:
#     # code
#     pass