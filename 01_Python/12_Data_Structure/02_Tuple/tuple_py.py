# Python Tuple

# Creating a Tuple

numbers = (10, 20, 30, 40)
print(numbers)


# Empty Tuple

empty_tuple = ()
print(empty_tuple)


# Single-Element Tuple

single = (10,)
print(single)
print(type(single))


# Tuple Without Parentheses

values = 10, 20, 30
print(values)


# Tuple Type

print(type(numbers))


# Tuple Length

print(len(numbers))


# Accessing Tuple Elements

print(numbers[0])
print(numbers[2])


# Negative Indexing

print(numbers[-1])
print(numbers[-2])


# Tuple Slicing

print(numbers[1:3])
print(numbers[:3])
print(numbers[::2])


# Tuple Methods - count()

values = (10, 20, 10, 30, 10)
print(values.count(10))


# Tuple Methods - index()

values = (10, 20, 30, 20)
print(values.index(20))


# Checking Elements

fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("orange" not in fruits)


# Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)


# Tuple Repetition

numbers = (1, 2)
print(numbers * 3)


# Tuple Packing

student = "Zeeshan", 21, "CSE"
print(student)


# Tuple Unpacking

student = ("Zeeshan", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)


# Nested Tuple

numbers = (1, 2, (3, 4), 5)

print(numbers[2])
print(numbers[2][0])


# Looping Through a Tuple

fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)


# Tuple to List

numbers = (10, 20, 30)

numbers = list(numbers)
print(numbers)


# List to Tuple

numbers = [10, 20, 30]

numbers = tuple(numbers)
print(numbers)


# Deleting a Tuple

numbers = (10, 20, 30)

del numbers