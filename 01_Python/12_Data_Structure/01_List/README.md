# Python List

## Introduction

A **list** is a built-in Python data structure used to store multiple values in a single variable.

Lists are:

- Ordered
- Mutable
- Allow duplicate values
- Can store different data types
- Can contain other lists

Example:

numbers = `[10, 20, 30, 40]`

---

## List Syntax

```python
list_name = [value1, value2, value3]
````

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

### Reverse a List

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

- `insert()` adds an element at a specific index.

- `insert()`adds the new value at the specified index and shifts the existing elements at that index and after it one position to the right `(+1)`.

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

- `remove()` removes the first occurrence of a specified value.

- `remove(value)` removes the first occurrence of the specified value and then the elements after it shift one position to the left `(-1)`.

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

`del` is a Python keyword used to delete elements, slices, or the entire list.

### Delete an element

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30]
```

### Delete multiple elements

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)
```

Output:

```text
[10, 50]
```

### Delete the entire list

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

# List Comprehension

List comprehension provides a short way to create a new list from an existing sequence.

### Basic Syntax

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

### With Condition

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

# Common List Methods

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

---

# Quick Summary

```text
List
│
├── Ordered
├── Mutable
├── Allows duplicates
├── Supports indexing
├── Supports negative indexing
├── Supports slicing
├── Supports nested lists
│
├── append()
├── extend()
├── insert()
├── remove()
├── pop()
├── clear()
├── del
├── count()
├── index()
├── copy()
├── sort()
└── reverse()
```

A list is one of the most important Python data structures and is widely used in **Data Science, NumPy, Pandas, Machine Learning, and general Python programming**.