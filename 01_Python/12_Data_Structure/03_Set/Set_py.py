# Python Set - Practice

# Creating Sets

numbers = {1, 2, 3, 4}
names = {"Alice", "Bob", "Charlie"}

print(numbers)
print(names)


# Empty Set

empty_set = set()

print(empty_set)


# Duplicate Values

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# Accessing Set Items

numbers = {10, 20, 30}

for number in numbers:
    print(number)


# Sorted Set

numbers = {5, 2, 9, 1, 7}

print(sorted(numbers))


# add()

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)


# update()

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)


# remove()

numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)


# discard()

numbers = {1, 2, 3}

numbers.discard(5)

print(numbers)


# pop()

numbers = {1, 2, 3}

item = numbers.pop()

print(item)
print(numbers)


# clear()

numbers = {1, 2, 3}

numbers.clear()

print(numbers)


# copy()

numbers = {1, 2, 3}

new_numbers = numbers.copy()

print(new_numbers)


# union()

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a | b)


# intersection()

print(a.intersection(b))
print(a & b)


# difference()

print(a.difference(b))
print(a - b)


# difference_update()

a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)

print(a)


# symmetric_difference()

a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))
print(a ^ b)


# symmetric_difference_update()

a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)

print(a)


# issubset()

a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(a <= b)


# issuperset()

print(b.issuperset(a))
print(b >= a)


# isdisjoint()

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))


# Membership

numbers = {1, 2, 3}

print(2 in numbers)
print(5 not in numbers)


# Frozenset

numbers = frozenset([1, 2, 3, 4])

print(numbers)


# Frozenset Operations

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


# Frozenset as Set Element

a = frozenset({1, 2})

b = {a, 3}

print(b)


# Frozenset as Dictionary Key

key = frozenset({1, 2})

data = {key: "value"}

print(data)