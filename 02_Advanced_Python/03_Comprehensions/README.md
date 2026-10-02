# Comprehensions

Comprehensions provide a short and simple way to create new collections from existing iterables.

Python provides different types of comprehensions:

- List Comprehension
- Dictionary Comprehension
- Set Comprehension

---

## 1. List Comprehension

List comprehension is used to create a new list in a single line of code.

### Syntax

```python
[expression for item in iterable]
```

### Basic Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### List Comprehension with Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

### List Comprehension with `if-else`

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
```

**Output:**

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Remember the difference:**

- `if` after the `for` filters items. Only items that satisfy the condition are included.
- `if-else` before the `for` expression chooses a value for every item. It does not filter items out.

### Working with Strings

```python
words = ["python", "java", "html"]

uppercase = [word.upper() for word in words]

print(uppercase)
```

**Output:**

```text
['PYTHON', 'JAVA', 'HTML']
```

### Multiple `for` Loops

List comprehensions can contain more than one `for` loop.

```python
numbers = [1, 2, 3]
letters = ["A", "B"]

result = [(number, letter) for number in numbers for letter in letters]

print(result)
```

**Output:**

```text
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]
```

### Nested List Comprehension

Nested list comprehension can be used to work with nested lists.

```python
matrix = [[1, 2], [3, 4], [5, 6]]

result = [number for row in matrix for number in row]

print(result)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

---

## 2. Dictionary Comprehension

Dictionary comprehension is used to create a new dictionary in a single line of code.

### Syntax

```python
{key_expression: value_expression for item in iterable}
```

### Basic Example

```python
numbers = [1, 2, 3, 4, 5]

squares = {x: x ** 2 for x in numbers}

print(squares)
```

**Output:**

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Dictionary Comprehension with Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {x: x ** 2 for x in numbers if x % 2 == 0}

print(even_numbers)
```

**Output:**

```text
{2: 4, 4: 16, 6: 36}
```

### Dictionary Comprehension with `if-else`

```python
numbers = [1, 2, 3, 4, 5]

result = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}

print(result)
```

**Output:**

```text
{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}
```

### Creating a Dictionary from Two Lists

```python
keys = ["name", "age", "city"]
values = ["Zeeshan", 22, "Lucknow"]

person = {keys[i]: values[i] for i in range(len(keys))}

print(person)
```

**Output:**

```text
{'name': 'Zeeshan', 'age': 22, 'city': 'Lucknow'}
```

`zip(keys, values)` pairs items by position. It stops when the shorter iterable ends, so make sure both lists have the expected matching items.

### Using `items()`

Dictionary comprehension can be used with the `items()` method.

```python
prices = {"apple": 100, "banana": 50, "orange": 80}

new_prices = {key: value * 2 for key, value in prices.items()}

print(new_prices)
```

**Output:**

```text
{'apple': 200, 'banana': 100, 'orange': 160}
```

### Filtering a Dictionary

```python
marks = {"Python": 85, "Java": 65, "SQL": 90, "HTML": 55}

passed = {subject: mark for subject, mark in marks.items() if mark >= 60}

print(passed)
```

**Output:**

```text
{'Python': 85, 'Java': 65, 'SQL': 90}
```

---

## 3. Set Comprehension

Set comprehension is used to create a new set in a single line of code.

### Syntax

```python
{expression for item in iterable}
```

### Basic Example

```python
numbers = [1, 2, 3, 4, 5]

squares = {x ** 2 for x in numbers}

print(squares)
```

**Output:**

```text
{1, 4, 9, 16, 25}
```

> The order of elements in a set is not guaranteed.

### Set Comprehension with Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {x for x in numbers if x % 2 == 0}

print(even_numbers)
```

**Output:**

```text
{2, 4, 6}
```

### Set Comprehension with `if-else`

```python
numbers = [1, 2, 3, 4, 5]

result = {"Even" if x % 2 == 0 else "Odd" for x in numbers}

print(result)
```

**Output:**

```text
{'Even', 'Odd'}
```

> A set stores only unique values, so duplicate results are automatically removed.

### Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique_numbers = {x for x in numbers}

print(unique_numbers)
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

---

## 4. Nested Comprehensions

Comprehensions can also be nested inside other comprehensions.

### Nested List Comprehension

```python
matrix = [[1, 2], [3, 4], [5, 6]]

result = [[x * 2 for x in row] for row in matrix]

print(result)
```

**Output:**

```text
[[2, 4], [6, 8], [10, 12]]
```

### Nested Dictionary Comprehension

```python
numbers = [1, 2, 3]

result = {
    x: {y: x * y for y in numbers}
    for x in numbers
}

print(result)
```

**Output:**

```text
{1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
```

---

## 5. Comprehension vs Traditional Loop

The same task can be written using a traditional `for` loop or a comprehension.

### Using a Traditional Loop

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### Using List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

Comprehension can make simple collection-building operations shorter and easier to read.

---

## 6. Difference Between Comprehensions

| Type                     | Creates    | Syntax                              |
| ------------------------ | ---------- | ----------------------------------- |
| List Comprehension       | List       | `[expression for item in iterable]` |
| Dictionary Comprehension | Dictionary | `{key_expression: value_expression for item in iterable}` |
| Set Comprehension        | Set        | `{expression for item in iterable}` |

### List Comprehension

```python
squares = [x ** 2 for x in range(1, 6)]
```

### Dictionary Comprehension

```python
squares = {x: x ** 2 for x in range(1, 6)}
```

### Set Comprehension

```python
squares = {x ** 2 for x in range(1, 6)}
```

---

## 7. Advantages of Comprehensions

* Makes code shorter and cleaner.
* Useful for creating collections.
* Can include conditions.
* Useful for transforming data.
* Can replace simple `for` loops.
* Makes many collection operations easier to write.

---

## Summary

### List Comprehension

Used to create a list:

```python
[expression for item in iterable]
```

### Dictionary Comprehension

Used to create a dictionary:

```python
{key_expression: value_expression for item in iterable}
```

### Set Comprehension

Used to create a set:

```python
{expression for item in iterable}
```

Comprehensions are useful when creating or transforming collections in a concise and readable way.

---

## 8. Points to Remember

- List comprehension creates a **list** and uses square brackets `[]`.
- Dictionary comprehension creates a **dictionary** using key-value pairs.
- Set comprehension creates a **set** and automatically removes duplicate values.
- `if` can be used to filter values in a comprehension.
- `if-else` can be used to choose between two values.
- The expression comes before the `for` in a comprehension.
- Multiple `for` loops can be used in a comprehension.
- Nested comprehensions are possible, but avoid making them unnecessarily complex.
- Set elements do not have a guaranteed order.
- Dictionary comprehensions require both a **key** and a **value**.
- Comprehensions are best suited for simple and readable operations.
- A normal `for` loop is often better when the logic becomes complex.
- Comprehensions can make code shorter, but shorter code is not always better code.