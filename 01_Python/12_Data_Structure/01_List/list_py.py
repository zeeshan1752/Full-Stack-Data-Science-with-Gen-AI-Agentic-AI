# Python Lists

# Creating Lists
numbers = [10, 20, 30, 40]
data = [10, 3.14, "Python", True]

print(numbers)
print(data)

# type()
print(type(numbers))

# len()
print(len(numbers))

# Indexing
print(numbers[0])
print(numbers[2])

# Negative Indexing
print(numbers[-1])
print(numbers[-2])

# Updating List Elements
numbers[1] = 25
print(numbers)

# Slicing
print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1])

# Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Nested Indexing
print(matrix[1][2])

# append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# extend()
numbers.extend([50, 60])
print(numbers)

# append() vs extend()
a = [1, 2, 3]
a.append([4, 5])
print(a)

b = [1, 2, 3]
b.extend([4, 5])
print(b)

# insert()
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

# remove()
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)

# pop()
numbers = [10, 20, 30]
value = numbers.pop()
print(value)
print(numbers)

numbers = [10, 20, 30]
value = numbers.pop(1)
print(value)
print(numbers)

# clear()
numbers = [10, 20, 30]
numbers.clear()
print(numbers)

# del
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)

numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)

# count()
numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))

# index()
numbers = [10, 20, 30, 20]
print(numbers.index(20))

# copy()
numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)

# sort()
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# reverse()
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

# Membership Operators
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)

# List Concatenation
a = [1, 2, 3]
b = [4, 5, 6]

result = a + b
print(result)

# List Repetition
numbers = [1, 2]
print(numbers * 3)

# List Unpacking
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# for Loop
numbers = [10, 20, 30, 40]

for value in numbers:
    print(value)

# for Loop with range()
for i in range(len(numbers)):
    print(i, numbers[i])

# Modifying a List Using range()
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# enumerate()
numbers = [10, 20, 30, 40]

for i, value in enumerate(numbers):
    print(i, value)

# enumerate() with One Variable
for i in enumerate(numbers):
    print(i)

# all()
numbers = [1, 2, 3, 4]
print(all(numbers))

numbers = [1, 2, 0, 4]
print(all(numbers))

# any()
numbers = [0, 0, 5, 0]
print(any(numbers))

numbers = [0, 0, 0, 0]
print(any(numbers))

# all() vs any()
values = [True, True, True]
print(all(values))
print(any(values))

values = [True, False, True]
print(all(values))
print(any(values))

# List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]
print(squares)

# List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)