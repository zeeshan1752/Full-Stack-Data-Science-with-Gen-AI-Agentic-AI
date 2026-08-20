# Python Dictionary

## 1. Dictionary Introduction & Properties

A **dictionary** is a built-in Python data structure that stores data as **key-value pairs**.

Dictionaries are:

* **Ordered** — preserve insertion order.
* **Mutable** — can be changed after creation.
* **Do not allow duplicate keys**.
* **Allow duplicate values**.
* Keys must be **unique and hashable**.
* Values can be of **any data type**.
* A dictionary can contain **different data types**.
* Dictionaries can contain **nested dictionaries**.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "course": "B.Tech CSE"
}

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21, 'course': 'B.Tech CSE'}
```

## Dictionary Keys

A dictionary key does **not** have to be a string.

Keys must be **hashable**.

Common valid key types:

* `str`
* `int`
* `float`
* `bool`
* `tuple`

```python
data = {
    "name": "Zeeshan",
    1: "One",
    2.5: "Two Point Five",
    (1, 2): "Tuple"
}

print(data)
```

Output:

```text
{'name': 'Zeeshan', 1: 'One', 2.5: 'Two Point Five', (1, 2): 'Tuple'}
```

Quotes are only required when the key is a **string**.

```python
student["name"]   # string key
student[1]        # integer key
student[(1, 2)]   # tuple key
```

Mutable types such as lists cannot be dictionary keys because they are unhashable.

```python
data = {
    [1, 2]: "List"
}
```

Output:

```text
TypeError: unhashable type: 'list'
```

## Dictionary Values

Values can be of any data type.

```python
data = {
    "name": "Zeeshan",
    "age": 21,
    "marks": [80, 90, 85],
    "address": {
        "city": "Lucknow",
        "country": "India"
    }
}

print(data)
```

Output:

```text
{
    'name': 'Zeeshan',
    'age': 21,
    'marks': [80, 90, 85],
    'address': {'city': 'Lucknow', 'country': 'India'}
}
```

---

# 2. Dictionary Methods / Attributes

The following are the main built-in dictionary methods:

| Method         | Description                                          |
| -------------- | ---------------------------------------------------- |
| `clear()`      | Removes all items                                    |
| `copy()`       | Creates a shallow copy                               |
| `fromkeys()`   | Creates a dictionary from given keys                 |
| `get()`        | Returns the value associated with a key              |
| `items()`      | Returns all key-value pairs                          |
| `keys()`       | Returns all keys                                     |
| `pop()`        | Removes a specified key and returns its value        |
| `popitem()`    | Removes and returns the last inserted key-value pair |
| `setdefault()` | Returns a value or inserts a default                 |
| `update()`     | Adds or updates items                                |
| `values()`     | Returns all values                                   |

### `clear()`

Removes all items from the dictionary.

### `copy()`

Creates a **shallow copy** of the dictionary.

### `fromkeys()`

Creates a new dictionary using the given keys and a common value.

### `get()`

Returns the value associated with a key.

If the key does not exist, it returns `None` by default.

A custom default value can also be provided.

### `items()`

Returns a view containing all key-value pairs.

### `keys()`

Returns a view containing all keys.

### `pop()`

Removes the specified key and returns its value.

A default value can be provided if the key does not exist.

### `popitem()`

Removes and returns the **last inserted key-value pair**.

### `setdefault()`

Returns the value of a key if it exists.

If the key does not exist, it adds the key with the specified default value.

### `update()`

Adds new items and updates existing items.

### `values()`

Returns a view containing all values.

### `del`

`del` is a Python statement, **not a dictionary method**.

It can be used to delete a specific key or the entire dictionary.

---

# 3. Creating Dictionaries

## Using `{}`

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21, 'city': 'Lucknow'}
```

## Empty Dictionary

```python
data = {}

print(data)
```

Output:

```text
{}
```

## Using `dict()`

```python
data = dict()

print(data)
```

Output:

```text
{}
```

## Using Keyword Arguments

```python
student = dict(
    name="Zeeshan",
    age=21,
    city="Lucknow"
)

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21, 'city': 'Lucknow'}
```

Keyword arguments become string keys.

## Using a List of Tuples

```python
student = dict([
    ("name", "Zeeshan"),
    ("age", 21)
])

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

## `fromkeys()`

`fromkeys()` creates a new dictionary using the given keys and a common value.

```python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)
```

Output:

```text
{'name': None, 'age': None, 'city': None}
```

A default value can be provided:

```python
student = dict.fromkeys(keys, "Unknown")

print(student)
```

Output:

```text
{'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
```

---

# 4. Accessing Values

## Using `[]`

Use square brackets to access the value associated with a key.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

print(student["name"])
print(student["age"])
```

Output:

```text
Zeeshan
21
```

If the key does not exist, `[]` raises a `KeyError`.

```python
print(student["city"])
```

Output:

```text
KeyError: 'city'
```

## Using `get()`

`get()` returns the value associated with a key.

```python
print(student.get("name"))
```

Output:

```text
Zeeshan
```

If the key does not exist, `get()` returns `None` by default.

```python
print(student.get("city"))
```

Output:

```text
None
```

### `get()` with a Default Value

A custom default value can be provided.

```python
print(student.get("city", "Not Available"))
```

Output:

```text
Not Available
```

The second argument is a **default value**, not another key.

---

# 5. Adding & Updating Items

## Adding an Item

Assign a value to a new key.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

student["city"] = "Lucknow"

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21, 'city': 'Lucknow'}
```

If the key does not exist, a new key-value pair is added.

## Updating an Item

If the key already exists, assigning a new value updates it.

```python
student["age"] = 22

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 22, 'city': 'Lucknow'}
```

## `update()`

`update()` can add new items and update existing items.

```python
student.update({
    "age": 23,
    "city": "Delhi"
})

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 23, 'city': 'Delhi'}
```

If a key already exists, its value is updated.

If a key does not exist, a new key-value pair is added.

---

# 6. Removing Items

## `pop()`

`pop()` removes the specified key and returns its value.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
21
{'name': 'Zeeshan', 'city': 'Lucknow'}
```

### `pop()` with a Default Value

A default value can be provided if the key does not exist.

```python
result = student.pop("marks", "Not Found")

print(result)
```

Output:

```text
Not Found
```

The second argument is simply the **value returned when the key is missing**.

It does not act as another key.

```python
student.pop("marks", "city")
```

If `"marks"` does not exist, `"city"` is returned as a string.

It does **not** remove the `"city"` key.

## `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}

item = student.popitem()

print(item)
print(student)
```

Output:

```text
('city', 'Lucknow')
{'name': 'Zeeshan', 'age': 21}
```

## `del`

`del` is a Python statement, not a dictionary method.

It can delete a specific key.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

del student["age"]

print(student)
```

Output:

```text
{'name': 'Zeeshan'}
```

It can also delete the entire dictionary:

```python
del student
```

## `clear()`

`clear()` removes all items from the dictionary.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

student.clear()

print(student)
```

Output:

```text
{}
```

---

# 7. Checking Keys & Values

## `in`

Use `in` to check whether a key exists.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

## `not in`

Use `not in` to check whether a key does not exist.

```python
print("city" not in student)
```

Output:

```text
True
```

### Important

`in` checks **keys**, not values.

```python
print("name" in student)
print("Zeeshan" in student)
```

Output:

```text
True
False
```

## Checking Values with `values()`

To check whether a value exists, use `values()`.

```python
print("Zeeshan" in student.values())
```

Output:

```text
True
```

## `keys()`

`keys()` returns a view containing all keys.

```python
print(student.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

## `values()`

`values()` returns a view containing all values.

```python
print(student.values())
```

Output:

```text
dict_values(['Zeeshan', 21])
```

## `items()`

`items()` returns a view containing all key-value pairs.

```python
print(student.items())
```

Output:

```text
dict_items([('name', 'Zeeshan'), ('age', 21)])
```

---

# 8. Looping Through a Dictionary

## Loop Through Keys

When a dictionary is directly used in a `for` loop, it iterates through its keys.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

The same can be done using `keys()`:

```python
for key in student.keys():
    print(key)
```

## Loop Through Values

Use `values()` to loop through values.

```python
for value in student.values():
    print(value)
```

Output:

```text
Zeeshan
21
```

## Loop Through Keys and Values

Use `items()` to get both the key and value.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Zeeshan
age 21
```

---

# 9. Dictionary Length & Duplicates

## `len()`

Use `len()` to get the number of key-value pairs in a dictionary.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}

print(len(student))
```

Output:

```text
3
```

## Duplicate Keys

Dictionary keys must be unique.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "name": "Ali"
}

print(student)
```

Output:

```text
{'name': 'Ali', 'age': 21}
```

The later value replaces the earlier value.

## Duplicate Values

Values can be duplicated.

```python
data = {
    "a": 10,
    "b": 10,
    "c": 20
}

print(data)
```

Output:

```text
{'a': 10, 'b': 10, 'c': 20}
```

Only keys must be unique.

---

# 10. Nested Dictionary

A dictionary can contain another dictionary as a value.

```python
students = {
    "student1": {
        "name": "Zeeshan",
        "age": 21
    },
    "student2": {
        "name": "Ali",
        "age": 22
    }
}

print(students)
```

Output:

```text
{
    'student1': {'name': 'Zeeshan', 'age': 21},
    'student2': {'name': 'Ali', 'age': 22}
}
```

## Accessing Nested Values

Use multiple `[]` operations.

```python
print(students["student1"]["name"])
```

Output:

```text
Zeeshan
```

The first `[]` accesses the inner dictionary, and the second `[]` accesses a value inside that dictionary.

---

# 11. Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

## Basic Syntax

```python
{key: value for item in iterable}
```

Example:

```python
numbers = {x: x * x for x in range(1, 6)}

print(numbers)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## With a Condition

```python
numbers = {
    x: x * x
    for x in range(1, 6)
    if x % 2 == 0
}

print(numbers)
```

Output:

```text
{2: 4, 4: 16}
```

---

# 12. Copying a Dictionary

## `copy()`

`copy()` creates a **shallow copy** of the dictionary.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

student_copy = student.copy()

print(student_copy)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

The copied dictionary is a separate dictionary from the original.

## Using `dict()`

A dictionary can also be copied using `dict()`.

```python
student_copy = dict(student)

print(student_copy)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

## Assignment Does Not Create a Copy

Using `=` does not create a new dictionary.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}

student_copy = student

student_copy["age"] = 22

print(student)
print(student_copy)
```

Output:

```text
{'name': 'Zeeshan', 'age': 22}
{'name': 'Zeeshan', 'age': 22}
```

Both variables refer to the **same dictionary**.

---

# 13. Sorting a Dictionary

A dictionary does **not automatically sort** its items.

It preserves the order in which items are inserted.

```python
data = {
    "c": 3,
    "a": 1,
    "b": 2
}

print(data)
```

Output:

```text
{'c': 3, 'a': 1, 'b': 2}
```

## Sorting Using `sorted()`

You can explicitly sort the dictionary items using `sorted()`.

```python
sorted_data = dict(sorted(data.items()))

print(sorted_data)
```

Output:

```text
{'a': 1, 'b': 2, 'c': 3}
```

The dictionary itself does not automatically sort its items.

---

# 14. Important Points / Quick Summary

* A dictionary stores data as **key-value pairs**.
* Keys must be **unique**.
* Values can be duplicated.
* Keys must be **hashable**.
* A key does **not** have to be a string.
* Quotes are required only when the key is a **string**.
* Lists, sets, and dictionaries cannot be used as keys because they are unhashable.
* Values can be of any data type.
* Dictionaries are **mutable**.
* Dictionaries preserve **insertion order**.
* Dictionaries do **not automatically sort** their items.
* Accessing a missing key using `[]` raises `KeyError`.
* `get()` safely accesses a missing key.
* `get()` can accept a custom default value.
* `pop()` removes a specified key and returns its value.
* The second argument of `pop()` is a **default value**, not another key.
* `popitem()` removes the **last inserted** key-value pair.
* `del` is a Python statement, **not a dictionary method**.
* `clear()` removes all items.
* `copy()` creates a **shallow copy**.
* Assignment using `=` does **not** create a copy.
* `update()` can add new items and update existing items.
* `setdefault()` does not overwrite an existing value.
* `keys()` returns a view of the keys.
* `values()` returns a view of the values.
* `items()` returns a view of the key-value pairs.
* `in` checks dictionary **keys** by default.
* Dictionaries can contain lists, tuples, sets, and other dictionaries as **values**.
* Dictionaries can be nested.
* Dictionary comprehensions provide a concise way to create dictionaries.