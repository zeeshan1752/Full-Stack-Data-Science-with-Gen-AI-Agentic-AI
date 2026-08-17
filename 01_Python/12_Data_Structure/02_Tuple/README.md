# Python Tuple

A **tuple** is a built-in Python data structure used to store multiple values in a single variable.

Tuples are:

* Ordered
* Immutable
* Allow duplicate values
* Can store different data types
* Support indexing and slicing
* Can contain nested data

## Syntax

```python
my_tuple = (value1, value2, value3)
```

Example:

```python
numbers = (10, 20, 30, 40)
```

## Creating Tuples

### Empty Tuple

```python
my_tuple = ()
```

### Single-Element Tuple

A comma is required for a single-element tuple.

```python
number = (10,)

print(type(number))
```

Without the comma, it is not a tuple:

```python
number = (10)

print(type(number))
```

## Accessing Elements

Tuples use indexing starting from `0`.

```python
fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
```

Negative indexing can also be used:

```python
print(fruits[-1])
```

## Slicing

Tuples support slicing just like lists.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
```

## Tuple Length

Use `len()` to find the number of elements.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

## Tuple Methods

Tuples have only **two methods**:

### `count()`

Returns the number of times a value occurs.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

### `index()`

Returns the index of the first occurrence of a value.

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))
```

## Immutability

Tuples cannot be changed after creation.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This gives a `TypeError`.

Tuples do not support methods such as:

```python
append()
remove()
pop()
clear()
```

because these operations modify the tuple.

## Adding Elements

You cannot directly add an element to an existing tuple.

However, you can create a **new tuple** using concatenation:

```python
numbers = (10, 20, 30)

numbers = numbers + (40,)

print(numbers)
```

## Deleting a Tuple

The entire tuple can be deleted using `del`.

**Note:** `del` is **not a tuple method**. It is a Python statement.

```python
numbers = (10, 20, 30)

del numbers
```

Individual elements cannot be deleted from a tuple.

## Tuple Packing and Unpacking

### Packing

Multiple values can be packed into a tuple:

```python
student = "Zeeshan", 21, "CSE"

print(student)
```

### Unpacking

Tuple elements can be assigned to multiple variables:

```python
student = ("Zeeshan", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)
```

## Checking Elements

Use `in` and `not in`:

```python
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("orange" not in fruits)
```

## Looping Through a Tuple

```python
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)
```

## Tuple Operations

### Concatenation

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)
```

### Repetition

```python
numbers = (1, 2)

print(numbers * 3)
```

## Nested Tuple

A tuple can contain another tuple.

```python
numbers = (1, 2, (3, 4), 5)

print(numbers[2])
print(numbers[2][0])
```

## Converting List and Tuple

### List → Tuple

```python
numbers = [10, 20, 30]

numbers = tuple(numbers)

print(numbers)
```

### Tuple → List

```python
numbers = (10, 20, 30)

numbers = list(numbers)

print(numbers)
```

## Tuple vs List

| Feature    | Tuple | List |
| ---------- | ----- | ---- |
| Syntax     | `()`  | `[]` |
| Ordered    | Yes   | Yes  |
| Mutable    | No    | Yes  |
| Duplicates | Yes   | Yes  |
| Indexing   | Yes   | Yes  |
| Slicing    | Yes   | Yes  |
| `append()` | No    | Yes  |
| `remove()` | No    | Yes  |
| `pop()`    | No    | Yes  |
| `count()`  | Yes   | Yes  |
| `index()`  | Yes   | Yes  |

## Important Points

* Tuple = **ordered and immutable collection**
* Uses `()`
* Single-element tuple needs a **comma**
* Supports indexing and slicing
* Has only two methods: `count()` and `index()`
* Cannot use `append()`, `remove()`, `pop()`, or `clear()`
* `del` deletes the entire tuple and is **not a tuple method**
* Tuples support packing and unpacking
* Use a tuple when the stored values should not be changed
