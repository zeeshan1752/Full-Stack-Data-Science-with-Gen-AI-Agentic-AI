# Lambda Functions in Python

Lambda functions are small anonymous functions used mainly for short expressions. This folder covers lambda functions and their use with `map()`, `filter()`, `reduce()`, `sorted()`, and indexing.

# 1. Lambda Function Basics

## What is a Lambda Function?

A lambda function is an anonymous function created using the `lambda` keyword.

Normal function:

```python
def square(x):
    return x * x

print(square(5))
```

Output:

```text
25
```



Lambda version:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```



## Syntax

```python
# Syntax: lambda arguments: expression
```



The expression is automatically returned.

## Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(10, 20))

multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))
```

Output:

```text
30
24
```



## Lambda with Conditional Expression

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

Output:

```text
Even
Odd
```



# 2. Lambda vs Normal Function

Normal function:

```python
def square(x):
    return x * x
```



Lambda:

```python
square = lambda x: x * x
```



Use lambda mainly for short expressions. Use `def` when the logic is complex or needs multiple statements.

## Passing Lambda as an Argument

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * x, numbers))

print(result)
```

Output:

```text
[1, 4, 9, 16]
```



# 3. Lambda with Collections

## Lambda with List

```python
numbers = [10, 20, 30, 40]

print(list(map(lambda x: x + 5, numbers)))
```

Output:

```text
[15, 25, 35, 45]
```



## Lambda with Tuple

```python
values = (1, 2, 3, 4)

print(list(map(lambda x: x * 2, values)))
```

Output:

```text
[2, 4, 6, 8]
```



## Lambda with Dictionary

```python
students = {
    "A": 80,
    "B": 95,
    "C": 70
}

print(sorted(students.items(), key=lambda x: x[1]))
```

Output:

```text
[('C', 70), ('A', 80), ('B', 95)]
```



# 4. Indexing Using Lambda

Lambda is useful for accessing elements by index, especially with tuples and lists.

## First Index

```python
students = [
    ("Zeeshan", 85),
    ("Rahul", 70),
    ("Aman", 95)
]

print(sorted(students, key=lambda x: x[0]))
```

Output:

```text
[('Aman', 95), ('Rahul', 70), ('Zeeshan', 85)]
```



`x[0]` accesses the first element.

## Second Index

```python
print(sorted(students, key=lambda x: x[1]))
```

Output:

```text
[('Rahul', 70), ('Zeeshan', 85), ('Aman', 95)]
```



`x[1]` accesses the second element.

## Nested Indexing

```python
data = [
    ("A", [80, 90]),
    ("B", [70, 85]),
    ("C", [95, 88])
]

print(sorted(data, key=lambda x: x[1][0]))
```

Output:

```text
[('B', [70, 85]), ('A', [80, 90]), ('C', [95, 88])]
```



`x[1][0]` means the second element, then its first element.

# 5. Lambda with `sorted()`

## Sort Numbers

```python
numbers = [5, 2, 9, 1, 7]

print(sorted(numbers, key=lambda x: x))
```

Output:

```text
[1, 2, 5, 7, 9]
```



## Sort Strings by Length

```python
words = ["Python", "AI", "Programming", "Data"]

print(sorted(words, key=lambda x: len(x)))
```

Output:

```text
['AI', 'Data', 'Python', 'Programming']
```



# 6. `map()`

`map()` applies a function to items and returns an iterator in Python 3. Convert it to a list with `list()` to see all results.

Syntax:



## `map()` with Normal Function

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

print(list(map(square, numbers)))
```

Output:

```text
[1, 4, 9, 16, 25]
```



## `map()` with Lambda

```python
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * x, numbers)))
```

Output:

```text
[1, 4, 9, 16, 25]
```



## `map()` with Multiple Iterables

Normal function:

```python
def add(a, b):
    return a + b

a = [1, 2, 3]
b = [10, 20, 30]

print(list(map(add, a, b)))
```

Output:

```text
[11, 22, 33]
```



Lambda:

```python
print(list(map(lambda x, y: x + y, a, b)))
```

Output:

```text
[11, 22, 33]
```



# 7. `filter()`

`filter()` selects items for which a function returns a truthy value and returns an iterator in Python 3. Convert it to a list to see all results.

Syntax:



## `filter()` with Normal Function

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

print(list(filter(is_even, numbers)))
```

Output:

```text
[2, 4, 6]
```



## `filter()` with Lambda

```python
print(list(filter(lambda x: x % 2 == 0, numbers)))
```

Output:

```text
[2, 4, 6]
```



## `filter()` with Strings

Normal function:

```python
def long_word(word):
    return len(word) > 4

words = ["AI", "Python", "Data", "Programming"]

print(list(filter(long_word, words)))
```

Output:

```text
['Python', 'Programming']
```



Lambda:

```python
print(list(filter(lambda word: len(word) > 4, words)))
```

Output:

```text
['Python', 'Programming']
```



## `filter()` with Indexed Data

```python
students = [
    ("Aman", 85),
    ("Rahul", 45),
    ("Zeeshan", 90)
]

print(list(filter(lambda x: x[1] >= 50, students)))
```

Output:

```text
[('Aman', 85), ('Zeeshan', 90)]
```



# 8. `reduce()`

`reduce()` repeatedly combines elements into a single result.

It must be imported from `functools`:

```python
from functools import reduce
```



Syntax:



## `reduce()` with Normal Function

```python
from functools import reduce

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

print(reduce(add, numbers))
```

Output:

```text
15
```



Calculation:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

## `reduce()` with Lambda

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

print(reduce(lambda a, b: a + b, numbers))
```

Output:

```text
15
```



## `reduce()` for Product

Normal function:

```python
def multiply(a, b):
    return a * b

print(reduce(multiply, numbers))
```

Output:

```text
120
```



Lambda:

```python
print(reduce(lambda a, b: a * b, numbers))
```

Output:

```text
120
```



## `reduce()` with Initial Value

```python
print(reduce(lambda a, b: a + b, [1, 2, 3], 10))
```

Output:

```text
16
```



Result:

```text
16
```

## `reduce()` for Maximum

Normal function:

```python
def maximum(a, b):
    return a if a > b else b

numbers = [10, 50, 20, 80, 30]

print(reduce(maximum, numbers))
```

Output:

```text
80
```



Lambda:

```python
print(reduce(lambda a, b: a if a > b else b, numbers))
```

Output:

```text
80
```



# 9. Combining `map()`, `filter()` and `reduce()`

## `map()` + `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even_numbers)

print(list(squares))
```

Output:

```text
[4, 16, 36]
```



## `filter()` + `map()`

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(
    map(
        lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)
```

Output:

```text
[4, 16, 36]
```



## `map()` + `filter()` + `reduce()`

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even_numbers)
total = reduce(lambda a, b: a + b, squares)

print(total)
```

Output:

```text
56
```



# 10. Practical Example - Student Records

```python
from functools import reduce

students = [
    ("Aman", 85),
    ("Rahul", 45),
    ("Zeeshan", 90),
    ("Riya", 35)
]

passed = list(filter(lambda x: x[1] >= 50, students))
marks = list(map(lambda x: x[1], passed))
total = reduce(lambda a, b: a + b, marks, 0)

print("Passed:", passed)
print("Marks:", marks)
print("Total:", total)
```

Output:

```text
Passed: [('Aman', 85), ('Zeeshan', 90)]
Marks: [85, 90]
Total: 175
```



# 11. Common Errors and Mistakes

## Multiple Statements in Lambda

Lambda is designed for a single expression.

For complex logic, use a normal `def` function.

## Forgetting the Expression

Incorrect:

```python
# lambda x:
```



A lambda needs an expression after `:`.

## Confusing `map()` and `filter()`

- `map()` transforms elements.
- `filter()` selects elements.

## Forgetting the `reduce()` Import

Correct:

```python
from functools import reduce
```



# 12. When to Use Lambda

Lambda is useful when:

- The operation is short.
- The function is needed only once.
- It is passed to `map()`, `filter()`, or `sorted()`.

Use a normal function when:

- The logic is complex.
- Multiple statements are needed.
- The function needs a meaningful name.
- A normal function is easier to read.

# 13. Final Summary

- `lambda` creates a small anonymous function.
- A lambda contains a single expression.
- The expression is automatically returned.
- Lambda can have multiple arguments.
- `lambda x: x[0]` accesses the first indexed element.
- `lambda x: x[1]` accesses the second indexed element.
- `map()` transforms elements.
- `filter()` selects elements.
- `reduce()` combines elements into a final result.
- `reduce()` is imported from `functools`.
- `map()`, `filter()`, and `reduce()` can work with both normal functions and lambda functions.

## 14. Useful Edge Cases

These examples cover reverse sorting, filtering when no items match, `map()` with different iterable lengths, and `reduce()` with an empty list.

### 1. Sorting in Reverse Order

```python
words = ["Python", "AI", "Programming", "Data"]

print(sorted(words, key=lambda word: len(word), reverse=True))
```

**Output:**

```text
['Programming', 'Python', 'Data', 'AI']
```

**Explanation:** `key=lambda word: len(word)` sorts words by length. `reverse=True` sorts them from longest to shortest.

### 2. Filtering When No Items Match

```python
numbers = [1, 3, 5, 7]

print(list(filter(lambda x: x % 2 == 0, numbers)))
```

**Output:**

```text
[]
```

**Explanation:** All numbers are odd, so none satisfies the even-number condition. Therefore, `filter()` returns an empty list.

### 3. Using `map()` with Different Iterable Lengths

```python
a = [1, 2, 3, 4]
b = [10, 20]

print(list(map(lambda x, y: x + y, a, b)))
```

**Output:**

```text
[11, 22]
```

**Explanation:** When `map()` receives multiple iterables, it stops when the shortest iterable is exhausted. Here, only two pairs are available:

- `1 + 10 = 11`
- `2 + 20 = 22`

### 4. Using `reduce()` with an Empty List

```python
from functools import reduce

empty_numbers = []

print(reduce(lambda a, b: a + b, empty_numbers, 0))
```

**Output:**

```text
0
```

**Explanation:** The initial value `0` allows `reduce()` to return a result even when the iterable is empty. Without an initial value, `reduce()` raises a `TypeError` for an empty iterable.

## Important Notes

- A `lambda` function contains a single expression, not multiple statements.
- The result of a lambda expression is returned automatically.
- `map()` transforms items, while `filter()` selects items based on a condition.
- `reduce()` combines items into a single result and must be imported from `functools`.
- Use an initial value with `reduce()` when the iterable might be empty.
- `sorted(numbers)` is sufficient for sorting ordinary numbers in ascending order. Using `key=lambda x: x` is valid but unnecessary.
- When `map()` receives multiple iterables, it stops at the shortest one.
- Prefer `def` when a function needs multiple statements or a descriptive, reusable name.
