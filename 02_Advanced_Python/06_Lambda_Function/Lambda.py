# Lambda Functions

# Lambda Function Basics

def normal_square(x):
    return x * x

print("Normal function:", normal_square(5))

square = lambda x: x * x
print("Lambda:", square(5))

add = lambda a, b: a + b
print("Add:", add(10, 20))

multiply = lambda a, b, c: a * b * c
print("Multiply:", multiply(2, 3, 4))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Condition:", check(10))
print("Condition:", check(7))

# Lambda vs Normal Function

def double_normal(x):
    return x * 2

double_lambda = lambda x: x * 2

print("Normal:", double_normal(10))
print("Lambda:", double_lambda(10))

# Lambda with Collections

numbers = [10, 20, 30, 40]
print(list(map(lambda x: x + 5, numbers)))

values = (1, 2, 3, 4)
print(list(map(lambda x: x * 2, values)))

students_dict = {"A": 80, "B": 95, "C": 70}
print(sorted(students_dict.items(), key=lambda x: x[1]))

# Indexing Using Lambda

students = [
    ("Zeeshan", 85),
    ("Rahul", 70),
    ("Aman", 95)
]

print(sorted(students, key=lambda x: x[0]))
print(sorted(students, key=lambda x: x[1]))

# Nested Indexing

data = [
    ("A", [80, 90]),
    ("B", [70, 85]),
    ("C", [95, 88])
]

print(sorted(data, key=lambda x: x[1][0]))

# Lambda with sorted

numbers = [5, 2, 9, 1, 7]
print(sorted(numbers, key=lambda x: x))

words = ["Python", "AI", "Programming", "Data"]
print(sorted(words, key=lambda x: len(x)))

# map with Normal Function

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))

# map with Lambda

print(list(map(lambda x: x * x, numbers)))

# map with Multiple Iterables

def add(a, b):
    return a + b

a = [1, 2, 3]
b = [10, 20, 30]

print(list(map(add, a, b)))
print(list(map(lambda x, y: x + y, a, b)))

# filter with Normal Function

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(is_even, numbers)))

# filter with Lambda

print(list(filter(lambda x: x % 2 == 0, numbers)))

# filter with Strings

def long_word(word):
    return len(word) > 4

words = ["AI", "Python", "Data", "Programming"]

print(list(filter(long_word, words)))
print(list(filter(lambda word: len(word) > 4, words)))

# filter with Indexed Data

students = [
    ("Aman", 85),
    ("Rahul", 45),
    ("Zeeshan", 90)
]

print(list(filter(lambda x: x[1] >= 50, students)))

# reduce with Normal Function

from functools import reduce

def add_reduce(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]
print(reduce(add_reduce, numbers))

# reduce with Lambda

print(reduce(lambda a, b: a + b, numbers))

# reduce for Product

def multiply_reduce(a, b):
    return a * b

print(reduce(multiply_reduce, numbers))
print(reduce(lambda a, b: a * b, numbers))

# reduce with Initial Value

print(reduce(lambda a, b: a + b, [1, 2, 3], 10))

# reduce for Maximum

def maximum(a, b):
    return a if a > b else b

numbers = [10, 50, 20, 80, 30]

print(reduce(maximum, numbers))
print(reduce(lambda a, b: a if a > b else b, numbers))

# map and filter

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even_numbers)

print(list(squares))

# map, filter and reduce

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even_numbers)
total = reduce(lambda a, b: a + b, squares)

print(total)

# Practical Student Example

students = [
    ("Aman", 85),
    ("Jamshed", 45),
    ("Zeeshan", 90),
    ("Maryam", 35)
]

passed = list(filter(lambda x: x[1] >= 50, students))
marks = list(map(lambda x: x[1], passed))
total = reduce(lambda a, b: a + b, marks, 0)

print("Passed:", passed)
print("Marks:", marks)
print("Total:", total)


# Sorting in Descending Order

words = ["Python", "AI", "Programming", "Data"]
print(sorted(words, key=lambda word: len(word), reverse=True))

# filter with No Matching Items

numbers = [1, 3, 5, 7]
print(list(filter(lambda x: x % 2 == 0, numbers)))

# map with Multiple Iterables of Different Lengths

a = [1, 2, 3, 4]
b = [10, 20]
print(list(map(lambda x, y: x + y, a, b)))

# reduce with an Initial Value for an Empty List

empty_numbers = []
print(reduce(lambda a, b: a + b, empty_numbers, 0))
