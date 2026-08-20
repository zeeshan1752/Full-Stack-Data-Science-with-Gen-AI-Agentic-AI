# PYTHON RANGE

# Creating a range
numbers = range(5)
print(numbers)
print(type(numbers))

# Converting range to list
print(list(range(5)))

# range(stop)
for i in range(5):
    print(i)

# range(start, stop)
for i in range(1, 6):
    print(i)

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)

# Negative step
for i in range(5, 0, -1):
    print(i)

# Reverse sequence
print(list(range(10, 0, -2)))

# Empty range
print(list(range(5, 5)))
print(list(range(5, 1)))
print(list(range(1, 5, -1)))

# Step cannot be zero

# print(range(1, 5, 0))

# range accepts integers

print(list(range(1, 6)))

# print(range(1.5, 5))

# Length of range
numbers = range(1, 10)
print(len(numbers))

# Indexing
numbers = range(10)
print(numbers[2])
print(numbers[5])

# Negative indexing
print(numbers[-1])
print(numbers[-2])

# Slicing
numbers = range(10)
print(numbers[2:7])
print(list(numbers[2:7]))
print(list(numbers[1:8:2]))

# Membership
print(5 in range(1, 10))
print(10 in range(1, 10))
print(6 in range(0, 11, 2))
print(7 in range(0, 11, 2))

# Range attributes
numbers = range(2, 10, 2)
print(numbers.start)
print(numbers.stop)
print(numbers.step)

# Reversed range
numbers = range(1, 6)
for i in reversed(numbers):
    print(i)
print(list(reversed(range(1, 6))))

# Range equality
print(range(0) == range(2, 1, 3))
print(range(0, 3, 2) == range(0, 4, 2))

# Range is immutable

numbers = range(5)

# numbers[0] = 10

# Convert to list to modify
numbers = list(range(5))
numbers[0] = 10
print(numbers)

# Large range
numbers = range(1000000000)
print(numbers.start)
print(numbers.stop)

# Common examples

# Even numbers
for i in range(2, 11, 2):
    print(i)

# Odd numbers
for i in range(1, 10, 2):
    print(i)

# Countdown
for i in range(10, 0, -1):
    print(i)

# Multiplication table
num = 5
for i in range(1, 11):
    print(num * i)

# Using range with len()
names = ["Ali", "Zaid", "Sara"]
for i in range(len(names)):
    print(i, names[i])

# Converting range to tuple
numbers = tuple(range(5))
print(numbers)

# Checking the type
numbers = range(5)
print(type(numbers))