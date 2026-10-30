# 1. Basic input

name = input()

print(name)


# 2. Input with a message

name = input("Enter your name: ")

print(name)


# 3. Storing input in variables

name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)


# 4. Input always returns a string

age = input("Enter your age: ")

print(age)
print(type(age))


# 5. Taking integer input

age = int(input("Enter your age: "))

print(age)
print(type(age))


# 6. Taking float input

price = float(input("Enter the price: "))

print(price)
print(type(price))


# 7. Taking boolean input

value = input("Enter True or False: ")

print(value)
print(type(value))


# 8. Boolean input using bool()

value = bool(input("Enter something: "))

print(value)
print(type(value))

# Note:
# bool("False") gives True because "False" is a non-empty string.


# 9. Input and type conversion

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(name)
print(age)
print(height)


# 10. Input for mathematical operations

a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)


# 11. Correct way to perform mathematical operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)


# 12. Taking multiple inputs using separate input statements

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name)
print(age)


# 13. Multiple inputs in one line using split()

a, b = input("Enter two values: ").split()

print(a)
print(b)


# 14. Multiple integer inputs using split() and map()

a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)


# 15. Input with split()

data = input("Enter your name and city: ").split()

print(data)


# 16. Input with map()

a, b, c = map(int, input("Enter three numbers: ").split())

print(a)
print(b)
print(c)


# 17. Input with different data types

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)