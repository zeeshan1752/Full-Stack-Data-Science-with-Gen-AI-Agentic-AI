# Recursion

Recursion is a programming technique in which a function or method calls itself to solve a problem.

A recursive solution normally contains two important parts:

```text
1. Base Case
   → Stops the recursion.

2. Recursive Case
   → Calls the same function again with a smaller or simpler problem.
```

## 1. What is Recursion?

A function that calls itself is using recursion.

```python
def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)

count_down(5)
```

Output:

```text
5
4
3
2
1
```

Here:

```text
count_down() → Function
Recursion    → Technique being used
```

Recursion itself is not a function or a method. A function or method can use recursion.

## 2. Basic Structure of Recursion

```python
def function_name(value):

    if stopping_condition:
        return

    # Some work

    function_name(smaller_value)
```

There are two important parts.

### Base Case

The condition that stops recursion.

```python
if n == 0:
    return
```

### Recursive Case

The function calls itself.

```python
function_name(n - 1)
```

## 3. Simple Recursion Example

```python
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

Output:

```text
1
2
3
4
5
```

If the `print()` statement is before the recursive call:

```python
def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n - 1)

print_numbers(5)
```

Output:

```text
5
4
3
2
1
```

This shows that the position of code relative to the recursive call affects the output.

## 4. How Recursion Works Internally

Consider:

```python
def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)

count_down(3)
```

The calls happen like this:

```text
count_down(3)
    ↓
count_down(2)
    ↓
count_down(1)
    ↓
count_down(0)
```

When `n == 0`, the base case is reached.

Then the function calls start returning.

```text
Calling:
3 → 2 → 1 → 0

Returning:
0 → 1 → 2 → 3
```

## 5. Call Stack

Python uses a **call stack** to keep track of active function calls.

For:

```python
def test(n):
    if n == 0:
        return

    print(n)
    test(n - 1)

test(3)
```

Conceptually, the stack grows like:

```text
test(3)
test(2)
test(1)
test(0)
```

Then:

```text
test(0) → returns
test(1) → returns
test(2) → returns
test(3) → returns
```

Each function call creates a **stack frame** containing information needed for that call.

## 6. Base Case

The base case tells recursion when to stop.

```python
def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)
```

The base case is:

```python
if n == 0:
    return
```

## 7. Missing Base Case

```python
def test(n):
    print(n)
    test(n - 1)

test(5)
```

There is no condition that stops the function.

Eventually Python raises:

```text
RecursionError: maximum recursion depth exceeded
```

## 8. Incorrect Base Case

```python
def count_down(n):
    if n == 10:
        return

    print(n)
    count_down(n - 1)

count_down(5)
```

Starting from `5`, the value moves away from `10`, so the base case is never reached.

Eventually:

```text
RecursionError: maximum recursion depth exceeded
```

A base case must be reachable.

## 9. Recursive Case

The recursive case is where the function calls itself.

```python
def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)
```

Here:

```python
count_down(n - 1)
```

is the recursive case.

The problem becomes smaller:

```text
5 → 4 → 3 → 2 → 1 → 0
```

## 10. Factorial Using Recursion

Factorial:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Recursive definition:

```text
n! = n × (n - 1)!
0! = 1
```

Python:

```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

Execution:

```text
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1 × factorial(0)
= 120
```

## 11. Factorial with an Incorrect Base Case

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(0))
```

The base case `n == 1` is never reached when starting with `0`.

The recursive calls continue into negative numbers until Python raises `RecursionError`.

## 12. Fibonacci Using Recursion

Fibonacci sequence:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Recursive formula:

```text
F(n) = F(n - 1) + F(n - 2)

F(0) = 0
F(1) = 1
```

```python
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```

Output:

```text
8
```

Generate a sequence:

```python
for i in range(10):
    print(fibonacci(i), end=" ")
```

Output:

```text
0 1 1 2 3 5 8 13 21 34
```

## 13. Why Basic Recursive Fibonacci is Slow

For:

```python
fibonacci(5)
```

many values are calculated repeatedly.

Conceptually:

```text
                fib(5)
               /      \
           fib(4)     fib(3)
           /   \       /   \
       fib(3) fib(2) fib(2) fib(1)
```

`fib(3)` and `fib(2)` are calculated multiple times.

Basic recursive Fibonacci has approximately:

```text
Time: O(2^n)
Space: O(n)
```

## 14. Fibonacci with Memoization

Memoization stores already calculated results.

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]

print(fibonacci(10))
```

Output:

```text
55
```

This avoids repeated calculations.

Approximate complexity:

```text
Time: O(n)
Space: O(n)
```

## 15. Sum of Natural Numbers

This example expects a non-negative integer.

```python
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))
```

Output:

```text
15
```

## 16. Sum of Digits

```python
def sum_digits(n):
    n = abs(n)

    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))
```

Output:

```text
10
```

The values become:

```text
1234
123
12
1
0
```

## 17. Reverse a String

```python
def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))
```

Output:

```text
nohtyP
```

## 18. Check Palindrome Using Recursion

```python
def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("hello"))
```

Output:

```text
True
False
```

## 19. Power of a Number

This version expects a non-negative integer exponent.

```python
def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 5))
```

Output:

```text
32
```

## 20. GCD Using Recursion

```python
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

print(gcd(48, 18))
```

Output:

```text
6
```

Flow:

```text
gcd(48, 18)
gcd(18, 12)
gcd(12, 6)
gcd(6, 0)
```

## 21. Count Digits

```python
def count_digits(n):
    n = abs(n)

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)

print(count_digits(12345))
print(count_digits(0))
print(count_digits(-72))
```

Output:

```text
5
1
2
```

The function treats `0` as a one-digit number and ignores the minus sign for negative integers.

## 22. Find Maximum in a List

```python
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
```

Output:

```text
80
```

## 23. Recursive Binary Search

Binary search works only when the list is sorted. It repeatedly checks the middle item and searches only the half that can contain the target.

```python
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
```

Output:

```text
4
-1
```

The first output is the index of `50`. The value `-1` means the target was not found.

## 24. Recursion with Lists

```python
def print_list(numbers, index=0):
    if index == len(numbers):
        return

    print(numbers[index])
    print_list(numbers, index + 1)

numbers = [10, 20, 30, 40]

print_list(numbers)
```

Output:

```text
10
20
30
40
```

## 25. Recursion with Nested Lists

```python
def print_nested(data):
    for item in data:

        if isinstance(item, list):
            print_nested(item)
        else:
            print(item)

data = [1, [2, 3], [4, [5, 6]]]

print_nested(data)
```

Output:

```text
1
2
3
4
5
6
```

This type of recursion is useful for nested or tree-like structures.

## 26. Direct Recursion

When a function directly calls itself:

```python
def test(n):
    if n == 0:
        return

    print(n)
    test(n - 1)
```

This is **direct recursion**.

## 27. Indirect Recursion

One function calls another function, which eventually calls the first function.

```python
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
```

Output:

```text
A: 3
B: 2
A: 1
```

## 28. Tail Recursion

A recursive function is tail recursive when the recursive call is the final operation.

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

Python does **not** perform tail-call optimization.

Therefore, tail recursion does not remove Python's recursion-depth limitation.

## 29. Recursion Limit in Python

Python has a recursion-depth limit to prevent extremely deep recursion from continuously consuming the call stack.

The limit is **not one universal number for every platform or Python installation**.

It can vary depending on factors such as:

- Operating system
- Python implementation
- Python version
- Build/environment
- Available C stack

Therefore, do **not** assume that the recursion limit is always exactly `1000`.

The correct way is to check the value in the Python environment you are using.

### Check the Current Recursion Limit

```python
import sys

limit = sys.getrecursionlimit()

print("Recursion limit:", limit)
```

Example output on one environment may be:

```text
Recursion limit: 1000
```

Another environment can report a different value.

The number printed by your own Python installation is the value you should use for that environment.

### Platform Note

There is no reliable rule such as:

```text
Windows → exactly X
Linux   → exactly Y
macOS   → exactly Z
```

The Python documentation/API does not define one fixed platform-specific recursion limit for all installations.

The limit should be treated as **environment-dependent**.

If you are working on:

```text
Windows
Linux
macOS
WSL
Docker
Jupyter
Anaconda/Conda
```

check it directly:

```python
import sys

print(sys.getrecursionlimit())
```

This is more reliable than memorizing a platform number.

## 30. Change the Recursion Limit

Python provides:

```python
sys.setrecursionlimit()
```

Example:

```python
import sys

print("Before:", sys.getrecursionlimit())

sys.setrecursionlimit(2000)

print("After:", sys.getrecursionlimit())
```

Possible output:

```text
Before: 1000
After: 2000
```

The `Before` value depends on your environment.

### Important Warning

Increasing the recursion limit does **not** fix infinite recursion.

For example:

```python
import sys

sys.setrecursionlimit(100000)

def test():
    test()

test()
```

This is still infinite recursion.

A very high limit can increase the risk of excessive stack/memory usage and may crash the Python process.

Only change the limit when you have a valid reason and understand the depth required by your program.

## 31. Demonstrating the Limit

We can create a recursive function that counts how deep it can go before Python raises `RecursionError`.

```python
import sys

print("Configured recursion limit:", sys.getrecursionlimit())

depth = 0

def test():
    global depth

    depth += 1
    test()

try:
    test()
except RecursionError:
    print("RecursionError occurred near depth:", depth)
```

The exact depth reached is **not guaranteed to equal the configured recursion limit**.

For example, if:

```text
sys.getrecursionlimit() = 1000
```

the observed depth may be somewhat lower or otherwise differ depending on the environment and how the recursion is executed.

This example is only for understanding the concept.

## 32. RecursionError

When Python reaches its recursion-depth protection, it raises:

```text
RecursionError
```

Example:

```python
def infinite_recursion():
    infinite_recursion()

infinite_recursion()
```

Eventually:

```text
RecursionError: maximum recursion depth exceeded
```

The problem is not simply that recursion was used.

The problem is that the recursive calls never stop.

## 33. Common Causes of RecursionError

### Missing Base Case

```python
def test(n):
    test(n - 1)

test(5)
```

### Base Case Cannot Be Reached

```python
def test(n):
    if n == 10:
        return

    test(n - 1)

test(5)
```

### Argument Does Not Change

```python
def test(n):
    if n == 0:
        return

    test(n)

test(5)
```

Here `n` remains `5`.

Correct:

```python
def test(n):
    if n == 0:
        return

    test(n - 1)

test(5)
```

## 34. Recursion vs Iteration

The same problem can often be solved using recursion or a loop.

### Recursion

```python
def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)

count_down(5)
```

### Iteration

```python
for i in range(5, 0, -1):
    print(i)
```

Both produce:

```text
5
4
3
2
1
```

| Feature | Recursion | Iteration |
|---|---|---|
| Main technique | Function calls itself | Loop repeats |
| Uses recursive call stack | Yes | No recursive call stack |
| Stopping mechanism | Base case | Loop condition |
| Memory for repeated calls | Can be higher | Usually lower |
| Useful for | Trees, DFS, divide-and-conquer, backtracking | Simple repetition and linear processing |

## 35. Time and Space Complexity

### Factorial

```text
Time: O(n)
Space: O(n)
```

The space is `O(n)` because of the recursive call stack.

### Basic Fibonacci

```text
Time: O(2^n) approximately
Space: O(n)
```

Repeated calculations make the basic recursive version slow.

### Binary Search

```text
Time: O(log n)
Space: O(log n)
```

The search space is divided approximately in half at every recursive call.

## 36. Common Recursion Mistakes

### Forgetting the base case

```python
def test(n):
    print(n)
    test(n - 1)
```

### Not changing the argument

```python
def test(n):
    if n == 0:
        return

    test(n)
```

### Moving away from the base case

```python
def test(n):
    if n == 10:
        return

    test(n - 1)
```

Starting from `5` moves away from `10`.

### Incorrect return

Incorrect:

```python
def factorial(n):
    if n == 0:
        return 1

    factorial(n - 1)
```

Correct:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

## 37. Important Rules to Remember

```text
1. Identify the base case.
2. Make sure the base case is reachable.
3. Make the problem smaller in every recursive call.
4. Return the recursive result when required.
5. Understand the call stack.
6. Consider time complexity.
7. Consider space complexity.
8. Check the recursion limit when recursion may become deep.
9. Do not increase the limit just to hide an infinite-recursion bug.
10. Use iteration when recursion does not provide a clear advantage.
```

A simple way to remember recursion:

```text
Problem
   ↓
Smaller Problem
   ↓
Smaller Problem
   ↓
Base Case
   ↓
Return
   ↑
Return
   ↑
Return
   ↑
Final Answer
```
