# Python List

## Introduction

A **list** is a built-in Python data structure used to store multiple values in a single variable.

Lists are:

* Ordered
* Mutable
* Allow duplicate values
* Can store different data types
* Can contain other lists

Example:

```python
numbers = [10, 20, 30, 40]
```

---

# Important Properties of Lists

| Property             | List    |
| -------------------- | ------- |
| Ordered              | Yes     |
| Mutable              | Yes     |
| Duplicates           | Allowed |
| Indexing             | Yes     |
| Negative Indexing    | Yes     |
| Slicing              | Yes     |
| Different Data Types | Yes     |
| Nested Lists         | Yes     |

---

## List Syntax

```python
list_name = [value1, value2, value3]
```

Example:

```python
numbers = [10, 20, 30, 40]
```

A list can contain different data types:

```python
data = [10, 3.14, "Python", True]
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
numbers = [10, 20, 30]

print(type(numbers))
```

Output:

```text
<class 'list'>
```

---

## len()

The `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

---

## Indexing

Each element in a list has an index.

Python uses **zero-based indexing**.

```python
numbers = [10, 20, 30, 40]
```

```text
Value:    10   20   30   40
Index:     0    1    2    3
```

Example:

```python
print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## Negative Indexing

Python also supports negative indexing.

```text
Value:           10    20    30    40
Positive Index:   0     1     2     3
Negative Index:  -4    -3    -2    -1
```

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

---

## Updating List Elements

Lists are **mutable**, which means their elements can be changed.

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:

```text
[10, 25, 30]
```

---

## Slicing

Slicing is used to extract a portion of a list.

### Syntax

```python
list[start:stop:step]
```

The `stop` index is not included.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

### Step

```python
print(numbers[::2])
```

Output:

```text
[10, 30, 50]
```

### Reverse a List Using Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

## Nested Lists

A list can contain other lists. This is called a **nested list**.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Here, the outer list contains three inner lists.

---

## Nested Indexing

Nested indexing is used to access elements inside nested lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
```

Output:

```text
6
```

Explanation:

```text
matrix[1]    → [4, 5, 6]
matrix[1][2] → 6
```

---

# List Methods

## Common List Methods

| Method      | Purpose                                |
| ----------- | -------------------------------------- |
| `append()`  | Adds one element at the end            |
| `extend()`  | Adds multiple elements                 |
| `insert()`  | Adds an element at a specific position |
| `remove()`  | Removes the first matching value       |
| `pop()`     | Removes and returns an element         |
| `clear()`   | Removes all elements                   |
| `count()`   | Counts occurrences of a value          |
| `index()`   | Finds the index of a value             |
| `copy()`    | Creates a copy of the list             |
| `sort()`    | Sorts the list                         |
| `reverse()` | Reverses the list                      |

> **Note:** `del` is included here for learning purposes because it is commonly used with lists, but technically `del` is **not a list method**. It is a Python keyword used to delete objects, elements, slices, or variables.

---

## 1. append()

`append()` adds **one element** to the end of a list.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### Important

`append()` accepts only **one argument**.

Correct:

```python
numbers.append(50)
```

Incorrect:

```python
numbers.append(50, 60)
```

This produces a `TypeError`.

If you want to add multiple elements, use `extend()`.

---

## 2. extend()

`extend()` adds multiple elements to the end of a list.

```python
numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50, 60]
```

### append() vs extend()

```python
numbers = [1, 2, 3]

numbers.append([4, 5])
```

Result:

```text
[1, 2, 3, [4, 5]]
```

Whereas:

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])
```

Result:

```text
[1, 2, 3, 4, 5]
```

---

## 3. insert()

`insert()` adds an element at a specific index.

It adds the new value at the specified index and shifts the existing elements at that index and after it one position to the right (`+1`).

### Syntax

```python
list.insert(index, value)
```

Example:

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

---

## 4. remove()

`remove()` removes the first occurrence of a specified value.

`remove(value)` removes the first occurrence of the specified value, and the elements after it shift one position to the left (`-1`).

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30, 20]
```

If the value does not exist, `remove()` raises a `ValueError`.

---

## 5. pop()

`pop()` removes and returns an element.

Without an index, it removes the last element.

```python
numbers = [10, 20, 30]

x = numbers.pop()

print(x)
print(numbers)
```

Output:

```text
30
[10, 20]
```

You can also specify an index:

```python
numbers = [10, 20, 30]

numbers.pop(1)

print(numbers)
```

Output:

```text
[10, 30]
```

---

## 6. clear()

`clear()` removes all elements from a list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

---

## 7. del

> **Important:** `del` is **not a list method**. It is a Python keyword used to delete elements, slices, or the entire list.

### Delete an Element

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30]
```

### Delete Multiple Elements

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)
```

Output:

```text
[10, 50]
```

### Delete the Entire List

```python
numbers = [10, 20, 30]

del numbers
```

---

## 8. count()

`count()` returns the number of times a value occurs in a list.

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))
```

Output:

```text
3
```

---

## 9. index()

`index()` returns the index of the first occurrence of a value.

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20))
```

Output:

```text
1
```

### Important

`index()` and slicing are different.

```python
numbers.index(30)
```

Finds the position of a value.

```python
numbers[1:3]
```

Extracts a portion of the list.

---

## 10. copy()

`copy()` creates a copy of a list.

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)
```

Output:

```text
[10, 20, 30]
```

The copied list is a separate list.

---

## 11. sort()

`sort()` sorts the elements of a list in ascending order by default.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

For descending order:

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

## 12. reverse()

`reverse()` reverses the order of elements in a list.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

# List Operations

## 1. Membership Operators

The `in` and `not in` operators check whether an element exists in a list.

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

Using `not in`:

```python
print(50 not in numbers)
```

Output:

```text
True
```

---

## 2. List Concatenation

The `+` operator can combine two lists.

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = a + b

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

## 3. List Repetition

The `*` operator can repeat a list.

```python
numbers = [1, 2]

print(numbers * 3)
```

Output:

```text
[1, 2, 1, 2, 1, 2]
```

---

## 4. List Unpacking

List unpacking assigns the elements of a list to multiple variables.

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

The number of variables must normally match the number of elements.

---

# Looping and Built-in Functions with Lists

## 1. Using `for` Loop with a List

A `for` loop can be used to access each element of a list one by one.

```python
numbers = [10, 20, 30, 40]

for value in numbers:
    print(value)
```

Output:

```text
10
20
30
40
```

---

## 2. Using `for i in range()`

`range()` can be used to loop through the **indexes** of a list.

```python
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print(numbers[i])
```

Output:

```text
10
20
30
40
```

Here:

* `len(numbers)` → gives the number of elements.
* `range(len(numbers))` → generates the indexes.
* `numbers[i]` → accesses the element at that index.

You can also use `range()` when you want to modify list elements:

```python
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
```

Output:

```text
[20, 40, 60, 80]
```

---

## 3. Using `enumerate()`

`enumerate()` is used when you want to get both the **index and value** while looping through a list.

### Using `enumerate()` with Two Variables

```python
numbers = [10, 20, 30, 40]

for i, value in enumerate(numbers):
    print(i, value)
```

Output:

```text
0 10
1 20
2 30
3 40
```

Here:

* `i` → index
* `value` → element at that index

### Using `enumerate()` Directly

You can also use `enumerate()` with only one variable:

```python
numbers = [10, 20, 30, 40]

for i in enumerate(numbers):
    print(i)
```

Output:

```text
(0, 10)
(1, 20)
(2, 30)
(3, 40)
```

In this case, `i` contains a **tuple**:

```text
(index, value)
```

For example:

```text
i = (0, 10)
i = (1, 20)
i = (2, 30)
i = (3, 40)
```

To access them separately:

```python
for i, value in enumerate(numbers):
    print(i, value)
```

### `range()` vs `enumerate()`

```text
range()
    → mainly used when you need the index

enumerate()
    → used when you need both index and value
```

Example:

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

```python
for i, value in enumerate(numbers):
    print(i, value)
```

The `enumerate()` approach is generally cleaner when you need both the index and the value.

---

## 4. all()

`all()` returns `True` if **all elements** in an iterable are truthy.

```python
numbers = [1, 2, 3, 4]

print(all(numbers))
```

Output:

```text
True
```

Example with `0`:

```python
numbers = [1, 2, 0, 4]

print(all(numbers))
```

Output:

```text
False
```

Because `0` is considered falsy.

Example with Boolean values:

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

```python
values = [True, False, True]

print(all(values))
```

Output:

```text
False
```

### Important

`all()` returns `False` if **even one element is falsy**.

Common falsy values include:

```text
0
False
None
""
```

---

## 5. any()

`any()` returns `True` if **at least one element** in an iterable is truthy.

```python
numbers = [0, 0, 5, 0]

print(any(numbers))
```

Output:

```text
True
```

Because `5` is truthy.

Example:

```python
numbers = [0, 0, 0, 0]

print(any(numbers))
```

Output:

```text
False
```

Example with Boolean values:

```python
values = [False, False, True]

print(any(values))
```

Output:

```text
True
```

### Important

`any()` returns `True` if **at least one element is truthy**.

---

## `all()` vs `any()`

| Function | Meaning                        | Example                 | Result  |
| -------- | ------------------------------ | ----------------------- | ------- |
| `all()`  | All elements must be truthy    | `[True, True, True]`    | `True`  |
| `all()`  | Even one falsy element         | `[True, False, True]`   | `False` |
| `any()`  | At least one element is truthy | `[False, False, True]`  | `True`  |
| `any()`  | No element is truthy           | `[False, False, False]` | `False` |

### Easy Way to Remember

```text
all() → ALL must be True
any() → ANY one can be True
```

---

# List Comprehension

List comprehension provides a short way to create a new list from an existing sequence.

## Basic Syntax

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

## With Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

List comprehension is especially useful in **Python programming and Data Science**.

---

# Quick Summary

```text
List
│
├── Properties
│   ├── Ordered
│   ├── Mutable
│   ├── Allows duplicates
│   ├── Supports indexing
│   ├── Supports negative indexing
│   ├── Supports slicing
│   ├── Supports different data types
│   └── Supports nested lists
│
├── Basic Operations
│   ├── Indexing
│   ├── Negative Indexing
│   ├── Slicing
│   ├── Nested Indexing
│   ├── Membership (in / not in)
│   ├── Concatenation (+)
│   ├── Repetition (*)
│   └── Unpacking
│
├── List Methods
│   ├── append()
│   ├── extend()
│   ├── insert()
│   ├── remove()
│   ├── pop()
│   ├── clear()
│   ├── count()
│   ├── index()
│   ├── copy()
│   ├── sort()
│   └── reverse()
│
├── List Keyword
│   └── del
│
├── Looping
│   ├── for loop
│   ├── range()
│   └── enumerate()
│
├── Built-in Functions
│   ├── type()
│   ├── len()
│   ├── all()
│   └── any()
│
└── List Comprehension
    ├── Basic comprehension
    └── Comprehension with condition
```

A list is one of the most important Python data structures and is widely used in **Data Science, NumPy, Pandas, Machine Learning, and general Python programming**.
