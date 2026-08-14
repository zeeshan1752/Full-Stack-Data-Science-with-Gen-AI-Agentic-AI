# BITWISE OPERATORS - PRACTICE

# 1. Bitwise AND (&)

a = 10
b = 6

print(a & b)


# 2. Bitwise OR (|)

a = 10
b = 6

print(a | b)


# 3. Bitwise XOR (^)

a = 10
b = 6

print(a ^ b)


# 4. Bitwise NOT (~)

a = 10

print(~a)


# 5. Left Shift (<<)

a = 10

print(a << 1)
print(a << 2)


# 6. Right Shift (>>)

a = 10

print(a >> 1)
print(a >> 2)


# 7. Binary Representation

a = 10

print(bin(a))


# 8. Bitwise Operators with Variables

a = 12
b = 5

and_result = a & b
or_result = a | b
xor_result = a ^ b
not_result = ~a
left_shift = a << 1
right_shift = a >> 1

print("AND:", and_result)
print("OR:", or_result)
print("XOR:", xor_result)
print("NOT:", not_result)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)


# 9. Swapping Two Numbers using XOR

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a:", a)
print("b:", b)