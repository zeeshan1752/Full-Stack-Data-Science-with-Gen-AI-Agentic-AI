# SWAPPING - PRACTICE

# 1. Swapping using Multiple Assignment

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# 2. Swapping using a Temporary Variable

a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)


# 3. Swapping using Addition and Subtraction

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a)
print(b)