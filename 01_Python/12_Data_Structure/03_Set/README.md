# Python Set

A **set** is a built-in Python data structure used to store multiple values.

Sets are:

* Unordered
* Mutable
* Do not allow duplicate values
* Can store different data types
* Written using curly braces `{}`

Example:

```python
numbers = {1, 2, 3, 4}
```

## Creating a Set

```python
numbers = {1, 2, 3, 4}
names = {"Alice", "Bob", "Charlie"}
```

To create an empty set, use `set()`:

```python
empty_set = set()
```

`{}` creates an empty dictionary, not a set.

## Duplicate Values

Sets automatically remove duplicate values.

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
# {1, 2, 3, 4}
```

## Accessing Set Items

Sets are unordered, so items cannot be accessed using indexes or slices.

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

The order of items in a set should not be relied upon.

If sorted values are required, use `sorted()`:

```python
numbers = {5, 2, 9, 1, 7}

print(sorted(numbers))
# [1, 2, 5, 7, 9]
```

`sorted()` returns a list, not a set.

## Adding Items

### `add()`

Adds one item to the set.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

### `update()`

Adds multiple items to the set and modifies the original set in place.

```python
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)
# {1, 2, 3, 4, 5, 6}
```

## Removing Items

### `remove()`

Removes a specified item. Raises a `KeyError` if the item does not exist.

```python
numbers = {1, 2, 3}

numbers.remove(2)
```

### `discard()`

Removes a specified item. Does not raise an error if the item does not exist.

```python
numbers = {1, 2, 3}

numbers.discard(5)
```

### `pop()`

Removes and returns an arbitrary item.

```python
numbers = {1, 2, 3}

item = numbers.pop()
```

### `clear()`

Removes all items from the set.

```python
numbers = {1, 2, 3}

numbers.clear()

print(numbers)
# set()
```

### `copy()`

Returns a copy of the set.

```python
numbers = {1, 2, 3}

new_numbers = numbers.copy()

print(new_numbers)
# {1, 2, 3}
```

The copied set is a separate set object.

---

## Set Operations

### `union()`

Returns a new set containing all unique elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)
# {1, 2, 3, 4, 5}
```

The `|` operator can also be used:

```python
print(a | b)
```

### `intersection()`

Returns a new set containing elements common to both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.intersection(b)

print(result)
# {3}
```

The `&` operator can also be used:

```python
print(a & b)
```

### `difference()`

Returns a new set containing elements present in the first set but not in the second.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

result = a.difference(b)

print(result)
# {1, 2}
```

### `difference_update()`

Removes elements of another set from the original set.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)

print(a)
# {1, 2}
```
* `difference()` → returns a new set, original set is unchanged.
* `difference_update()` → modifies the original set in place.

### `symmetric_difference()`

Returns a new set containing elements that are present in either set, but not in both.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)

print(result)
# {1, 2, 4, 5}
```

The `^` operator can also be used:

```python
print(a ^ b)
```

### `symmetric_difference_update()`

Updates the original set with elements that are present in either set, but not in both.

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)

print(a)
# {1, 2, 4, 5}
```
* `symmetric_difference()` → returns a new set, original set is unchanged.
* `symmetric_difference_update()` → modifies the original set in place.

---

## Set Comparison

### `issubset()`

Checks whether all elements of one set are present in another set.

```python
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
# True
```

The `<=` operator can also be used:

```python
print(a <= b)
```

### `issuperset()`

Checks whether a set contains all elements of another set.

```python
a = {1, 2}
b = {1, 2, 3}

print(b.issuperset(a))
# True
```

The `>=` operator can also be used:

```python
print(b >= a)
```

### `isdisjoint()`

Checks whether two sets have no elements in common.

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
# True
```

If even **one element is common**, the sets are **not disjoint**.

## Membership

Use `in` and `not in` to check whether an item exists in a set.

```python
numbers = {1, 2, 3}

print(2 in numbers)
# True

print(5 not in numbers)
# True
```

## Frozenset

A **frozenset** is an immutable version of a set.

Unlike a normal set, a frozenset cannot be changed after it is created.

```python
numbers = frozenset([1, 2, 3, 4])

print(numbers)
# frozenset({1, 2, 3, 4})
```

Frozensets support operations such as:

* `union()`
* `intersection()`
* `difference()`
* `symmetric_difference()`
* `issubset()`
* `issuperset()`
* `isdisjoint()`

Frozensets do not support methods that modify the set, such as:

* `add()`
* `update()`
* `remove()`
* `discard()`
* `pop()`
* `clear()`

A frozenset can be an element of another set because it is immutable.

```python
a = frozenset({1, 2})

b = {a, 3}

print(b)
```

A frozenset can also be used as a dictionary key.

## Set Methods

| Method                          | Description                                                      |
| ------------------------------- | ---------------------------------------------------------------- |
| `add()`                         | Adds one item                                                    |
| `update()`                      | Adds multiple items and modifies the original set                |
| `remove()`                      | Removes an item; raises an error if absent                       |
| `discard()`                     | Removes an item without raising an error                         |
| `pop()`                         | Removes an arbitrary item                                        |
| `clear()`                       | Removes all items                                                |
| `copy()`                        | Returns a copy of the set                                        |
| `union()`                       | Returns a new set containing elements from both sets             |
| `intersection()`                | Returns a new set containing common elements                     |
| `difference()`                  | Returns a new set containing elements in one set but not another |
| `difference_update()`           | Removes elements of another set from the original set            |
| `symmetric_difference()`        | Returns a new set containing elements present in only one set    |
| `symmetric_difference_update()` | Updates the original set with elements present in only one set   |
| `issubset()`                    | Checks whether a set is a subset                                 |
| `issuperset()`                  | Checks whether a set is a superset                               |
| `isdisjoint()`                  | Checks whether sets have no common elements                      |

## Important Points

* Sets do not allow duplicate values.
* Sets are unordered.
* Sets do not support indexing or slicing.
* Sets are mutable.
* Set elements must be **hashable**.
* Lists, dictionaries, and other mutable objects cannot be elements of a set.
* Use `set()` to create an empty set.
* `{}` creates an empty dictionary.
* `sorted()` returns a sorted list, not a set.
* Methods ending with `_update()` modify the original set in place.
* `frozenset` is an immutable version of a set.
* A frozenset can be used as an element of a set and as a dictionary key.
* Sets are useful for removing duplicates and performing mathematical set operations.
