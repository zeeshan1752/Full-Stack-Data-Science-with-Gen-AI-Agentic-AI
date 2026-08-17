# Python Lists

# 1. Introduction

numbers = [10, 20, 30, 40]

print(numbers)


# 2. List Syntax

numbers = [10, 20, 30, 40]
data = [10, 3.14, "Python", True]

print(numbers)
print(data)


# 3. type()

numbers = [10, 20, 30]

print(type(numbers))


# 4. len()

numbers = [10, 20, 30, 40]

print(len(numbers))


# 5. Indexing

numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])


# 6. Negative Indexing

numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])


# 7. Updating List Elements

numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)


# 8. Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1])


# 9. Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


# 10. Nested Indexing

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])


# 11. append()

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# append() takes only one argument

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# numbers.append(40, 50)  # TypeError


# 12. extend()

numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)


# append() vs extend()

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)


# 13. insert()

numbers = [10, 20, 30, 40]

numbers.insert(2, 99)

print(numbers)

# insert() adds the value at the specified index
# Existing elements from that index shift one position to the right


# 14. remove()

numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)

# remove() removes the first occurrence of the specified value
# Elements after the removed value shift one position to the left


# remove() can also remove a nested list

data = [[1, 2, 3], [4, 5, 6], 10, 20]

data.remove([1, 2, 3])

print(data)


# 15. pop()

numbers = [10, 20, 30, 40]

value = numbers.pop()

print(value)
print(numbers)


# pop() using an index

numbers = [10, 20, 30, 40]

value = numbers.pop(1)

print(value)
print(numbers)


# 16. clear()

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# 17. del

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)


# del with slicing

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)


# 18. count()

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))


# 19. index()

numbers = [10, 20, 30, 20]

print(numbers.index(20))


# 20. copy()

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(numbers)
print(new_numbers)


# 21. sort()

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)


# sort() in descending order

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)


# 22. reverse()

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)