# Recursion

# Basic recursion
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n - 1)

count_down(5)


# Print numbers from 1 to N
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)


# Factorial using recursion
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
print()


# Fibonacci with memoization
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(10))


# Sum of natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))


# Sum of digits
def sum_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))


# Reverse a string
def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))


# Check palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("hello"))


# Power of a number
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))


# GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))


# Count digits
def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))
print(count_digits(0))
print(count_digits(-72))


# Find maximum in a list
def find_max(numbers, index=0):
    if not numbers:
        raise ValueError("The list must not be empty")
    if index == len(numbers) - 1:
        return numbers[index]

    current = numbers[index]
    maximum = find_max(numbers, index + 1)

    return max(current, maximum)

numbers = [10, 50, 20, 80, 30]
print(find_max(numbers))


# Recursive binary search
def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid

    if target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)

    return binary_search(numbers, target, mid + 1, high)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 50, 0, len(numbers) - 1))


# Direct recursion
def direct_recursion(n):
    if n == 0:
        return
    print(n)
    direct_recursion(n - 1)

direct_recursion(3)


# Indirect recursion
def function_a(n):
    if n <= 0:
        return
    print("A:", n)
    function_b(n - 1)

def function_b(n):
    if n <= 0:
        return
    print("B:", n)
    function_a(n - 1)

function_a(3)


# Recursion limit
import sys

print("Current recursion limit:", sys.getrecursionlimit())

# The starting value is platform/environment dependent.
# Do not assume it is always 1000.

# Update the recursion limit carefully.
old_limit = sys.getrecursionlimit()
sys.setrecursionlimit(2000)

print("Updated recursion limit:", sys.getrecursionlimit())

# Restore the original limit for the rest of the session.
sys.setrecursionlimit(old_limit)

print("Restored recursion limit:", sys.getrecursionlimit())


# Demonstrate RecursionError safely
depth = 0

def test_depth():
    global depth
    depth += 1
    test_depth()

try:
    test_depth()
except RecursionError:
    print("RecursionError occurred near depth:", depth)


# Infinite recursion example - do not run
# def infinite_recursion():
#     infinite_recursion()
#
# infinite_recursion()

# Recursive binary search (the list must be sorted)
def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    if target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    return binary_search(numbers, target, mid + 1, high)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 50, 0, len(numbers) - 1))
print(binary_search(numbers, 25, 0, len(numbers) - 1))


# Recursion with nested lists
def print_nested(data):
    for item in data:
        if isinstance(item, list):
            print_nested(item)
        else:
            print(item)

print_nested([1, [2, 3], [4, [5, 6]]])


# Recursion vs iteration: both print numbers from 5 to 1
def count_down_loop(n):
    for number in range(n, 0, -1):
        print(number)

count_down_loop(5)
