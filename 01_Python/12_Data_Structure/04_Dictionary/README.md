# Python Dictionary

## Introduction

A **dictionary** is a built-in Python data structure that stores data as **key-value pairs**.

Dictionaries are:

* Ordered — preserve insertion order
* Mutable
* Do not allow duplicate keys
* Allow duplicate values
* Keys must be unique and hashable
* Values can be of any data type
* Can contain different data types
* Can contain nested dictionaries

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

## Creating a Dictionary

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

### Empty Dictionary

```python
data = {}
print(data)
```

Output:

```text
{}
```

### Using `dict()`

```python
data = dict()
print(data)
```

Output:

```text
{}
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

Mutable types such as lists cannot be dictionary keys:

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

## Accessing Dictionary Values

### Using `[]`

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

### Using `get()`

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

A custom default value can also be provided:

```python
print(student.get("city", "Not Available"))
```

Output:

```text
Not Available
```

The second argument is a **default value**, not another key.

## Adding Items

Assign a value to a new key:

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

## Updating Items

If the key already exists, assigning a new value updates it.

```python
student["age"] = 22

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 22, 'city': 'Lucknow'}
```

### `update()`

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

## Removing Items

### `pop()`

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

A default value can be provided if the key does not exist:

```python
result = student.pop("marks", "Not Found")

print(result)
```

Output:

```text
Not Found
```

The second argument is simply the **value returned when the key is missing**.

It does not act as another key:

```python
student.pop("marks", "city")
```

Here, `"city"` is returned as a string if `"marks"` does not exist. It does **not** remove `"city"`.

### `popitem()`

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

### `del`

`del` is a Python statement, **not a dictionary method**.

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

### `clear()`

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

## Dictionary Methods

### `keys()`

Returns a view containing all keys.

```python
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}

print(student.keys())
```

Output:

```text
dict_keys(['name', 'age', 'city'])
```

### `values()`

Returns a view containing all values.

```python
print(student.values())
```

Output:

```text
dict_values(['Zeeshan', 21, 'Lucknow'])
```

### `items()`

Returns a view containing all key-value pairs.

```python
print(student.items())
```

Output:

```text
dict_items([('name', 'Zeeshan'), ('age', 21), ('city', 'Lucknow')])
```

### `get()`

Returns the value associated with a key, or a default value if the key does not exist.

```python
print(student.get("name"))
```

Output:

```text
Zeeshan
```

### `update()`

Adds new items or updates existing items.

```python
student.update({"age": 22})

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 22, 'city': 'Lucknow'}
```

### `pop()`

Removes a specified key and returns its value.

```python
student.pop("age")

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'city': 'Lucknow'}
```

### `popitem()`

Removes and returns the last inserted key-value pair.

```python
student.popitem()

print(student)
```

Output:

```text
{'name': 'Zeeshan'}
```

### `clear()`

Removes all items.

```python
student.clear()

print(student)
```

Output:

```text
{}
```

### `copy()`

Creates a **shallow copy** of the dictionary.

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

### `setdefault()`

Returns the value of a key if it exists.

If the key does not exist, it adds the key with the specified default value.

```python
student = {
    "name": "Zeeshan"
}

student.setdefault("age", 21)

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

If the key already exists, its value is not changed:

```python
student.setdefault("age", 25)

print(student)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

## Checking if a Key Exists

Use `in`:

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

Use `not in`:

```python
print("city" not in student)
```

Output:

```text
True
```

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

To check values:

```python
print("Zeeshan" in student.values())
```

Output:

```text
True
```

## Looping Through a Dictionary

### Loop Through Keys

```python
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

### Loop Through Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Zeeshan
21
```

### Loop Through Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Zeeshan
age 21
```

## Dictionary Length

Use `len()` to get the number of key-value pairs.

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

## Nested Dictionary

A dictionary can contain another dictionary.

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

Access nested values:

```python
print(students["student1"]["name"])
```

Output:

```text
Zeeshan
```

## Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

```python
numbers = {x: x * x for x in range(1, 6)}

print(numbers)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

With a condition:

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

## Creating a Dictionary with `dict()`

### Using Keyword Arguments

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

### Using a List of Tuples

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

Creates a new dictionary using the given keys and a common value.

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

## Copying a Dictionary

### Using `copy()`

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

`copy()` creates a **shallow copy**.

### Using `dict()`

```python
student_copy = dict(student)

print(student_copy)
```

Output:

```text
{'name': 'Zeeshan', 'age': 21}
```

### Assignment Does Not Create a Copy

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

## Sorting a Dictionary

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

You can explicitly sort the items using `sorted()`:

```python
sorted_data = dict(sorted(data.items()))

print(sorted_data)
```

Output:

```text
{'a': 1, 'b': 2, 'c': 3}
```

## Dictionary Methods Summary

| Method         | Description                                   |
| -------------- | --------------------------------------------- |
| `clear()`      | Removes all items                             |
| `copy()`       | Returns a shallow copy                        |
| `fromkeys()`   | Creates a dictionary from keys                |
| `get()`        | Returns a value or default value              |
| `items()`      | Returns key-value pairs                       |
| `keys()`       | Returns all keys                              |
| `pop()`        | Removes a specified key and returns its value |
| `popitem()`    | Removes the last inserted key-value pair      |
| `setdefault()` | Returns a value or inserts a default          |
| `update()`     | Adds or updates items                         |
| `values()`     | Returns all values                            |

## Important Points

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
* `get()` safely accesses a missing key and can accept a default value.
* `pop()` removes a key and returns its value.
* The second argument of `pop()` is a **default value**, not another key.
* `popitem()` removes the **last inserted** key-value pair.
* `del` is a Python statement, **not a dictionary method**.
* `copy()` creates a **shallow copy**.
* Assignment with `=` does not create a copy.
* `update()` can add new items and update existing items.
* `setdefault()` does not overwrite an existing value.
* Dictionaries can contain lists, tuples, sets, and other dictionaries as **values**.
* Dictionaries can be nested.
