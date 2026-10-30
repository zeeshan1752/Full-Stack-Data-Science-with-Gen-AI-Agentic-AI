# For Loop

for i in range(5):
    print(i)


# range(stop)

for i in range(5):
    print(i)


# range(start, stop)

for i in range(2, 7):
    print(i)


# range(start, stop, step)

for i in range(2, 11, 2):
    print(i)


# Counting Backwards

for i in range(10, 0, -1):
    print(i)


# Looping Through a String

name = "Zee"

for char in name:
    print(char)


# Looping Through a List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# Multiplication Table

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Break

for i in range(1, 11):
    if i == 6:
        break

    print(i)


# Break - Practical Example

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Number found")
        break

    print(num)


# Continue

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# Continue - Print Only Odd Numbers

for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)


# Pass

for i in range(5):
    pass


# Pass vs Continue

for i in range(1, 6):
    if i == 3:
        pass

    print(i)


for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# For-Else

for i in range(5):
    print(i)
else:
    print("Loop completed")


# For-Else With Break

for i in range(5):
    if i == 3:
        break

    print(i)
else:
    print("Loop completed")


# For-Else - Searching

numbers = [10, 20, 30, 40, 50]

search = 30

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")


# Nested For Loop

for i in range(3):
    for j in range(2):
        print(i, j)


# Pattern 1 - Increasing Star Pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()


# Pattern 2 - Decreasing Star Pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()


# Pattern 3 - Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# Pattern 4 - Repeated Number Pattern

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")

    print()


# Pattern 5 - Continuous Number Pattern

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1

    print()


# Pattern 6 - Square Pattern

for i in range(5):
    for j in range(5):
        print("*", end=" ")

    print()


# Pattern 7 - Rectangle Pattern

for i in range(3):
    for j in range(5):
        print("*", end=" ")

    print()


# Pattern 8 - Right-Aligned Star Pattern

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


# Pattern 9 - Pyramid Pattern

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()


# Sum of Numbers

total = 0

for i in range(1, 11):
    total += i

print(total)


# Factorial

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)


# Prime Number

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")