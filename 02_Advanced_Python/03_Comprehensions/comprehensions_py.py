# List, Dictionary and Set Comprehension

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)

# List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# List Comprehension with if-else
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)

# Working with Strings
words = ["python", "java", "html"]
uppercase = [word.upper() for word in words]
print(uppercase)

# Multiple for Loops
numbers = [1, 2, 3]
letters = ["A", "B"]
result = [(number, letter) for number in numbers for letter in letters]
print(result)

# Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
result = [number for row in matrix for number in row]
print(result)

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x: x ** 2 for x in numbers}
print(squares)

# Dictionary Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_numbers)

# Dictionary Comprehension with if-else
numbers = [1, 2, 3, 4, 5]
result = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print(result)

# Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Zeeshan", 22, "Lucknow"]
person = {key: value for key, value in zip(keys, values)}
print(person)

# Using items()
prices = {"apple": 100, "banana": 50, "orange": 80}
new_prices = {key: value * 2 for key, value in prices.items()}
print(new_prices)

# Filtering a Dictionary
marks = {"Python": 85, "Java": 65, "SQL": 90, "HTML": 55}
passed = {subject: mark for subject, mark in marks.items() if mark >= 60}
print(passed)

# Set Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x ** 2 for x in numbers}
print(squares)

# Set Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)

# Set Comprehension with if-else
numbers = [1, 2, 3, 4, 5]
result = {"Even" if x % 2 == 0 else "Odd" for x in numbers}
print(result)

# Removing Duplicates
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)

# Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
result = [[x * 2 for x in row] for row in matrix]
print(result)

# Nested Dictionary Comprehension
numbers = [1, 2, 3]
result = {
    x: {y: x * y for y in numbers}
    for x in numbers
}
print(result)
