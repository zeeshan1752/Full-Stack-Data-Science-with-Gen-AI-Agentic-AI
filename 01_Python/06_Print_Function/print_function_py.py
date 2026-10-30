# Python Print Function Practice

# Basic print
print("Hello World")

# Printing text
print("Hello Python")
print("I am learning Python")

# Printing a number
print(100)
print(25.5)

# Printing text and number
age = 21
print("My age is", age)

# Printing calculated value
num1 = 3
num2 = 6
add = num1 + num2

print("The sum of num1 and num2 is", add)

# Code optimization using one print
print("Hello", "My name is Zeeshan", "I am learning Python")

# Format method
print("The sum of {} and {} is {}.".format(num1, num2, add))

# F-string
print(f"The sum of {num1} and {num2} is {add}.")

# Using end
print("Hello", end=" ")
print("World")

print("Hello", end="...")
print("World")

# Using sep
print("Python", "Java", "C++", sep="-")
print(10, 20, 30, sep=",")

# Using sep and end together
print("Python", "Java", "C++", sep=" | ", end=" Done")