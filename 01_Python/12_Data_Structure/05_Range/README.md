# Python `range()` — README

## Introduction

`range()` is a built-in Python function used to generate a sequence of integers.

It is commonly used with `for` loops.

```python
range(start, stop, step)
```

* `start` → starting value
* `stop` → ending limit (**not included**)
* `step` → difference between values

---

## Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### `range(stop)`

Starts from `0` and uses a step of `1`.

```python
range(5)
```

Values:

```text
0 1 2 3 4
```

### `range(start, stop)`

```python
range(2, 7)
```

Values:

```text
2 3 4 5 6
```

### `range(start, stop, step)`

```python
range(2, 10, 2)
```

Values:

```text
2 4 6 8
```

---

## Important Rule: `stop` Is Excluded

The `stop` value is never included.

```python
print(list(range(1, 5)))
```

Output:

```text
[1, 2, 3, 4]
```

So:

```text
start → included
stop  → excluded
```

---

## Type of `range()`

`range()` returns a `range` object.

```python
numbers = range(5)

print(type(numbers))
```

Output:

```text
<class 'range'>
```

It does not immediately create a list containing all the numbers.

---

## Converting `range()` to a List

Use `list()` to convert it into a list.

```python
numbers = list(range(5))

print(numbers)
```

Output:

```text
[0, 1, 2, 3, 4]
```

You can also convert it to other sequence types:

```python
tuple(range(5))
```

Output:

```text
(0, 1, 2, 3, 4)
```

---

## Using `range()` with `for` Loop

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### Starting from a Specific Number

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## `step`

`step` determines how much the value changes each time.

```python
list(range(0, 11, 2))
```

Output:

```text
[0, 2, 4, 6, 8, 10]
```

Here:

```text
start = 0
stop  = 11
step  = 2
```

### Default Step

If `step` is not provided, it is `1`.

```python
list(range(2, 6))
```

Output:

```text
[2, 3, 4, 5]
```

This is equivalent to:

```python
list(range(2, 6, 1))
```

---

## Negative Step

A negative `step` moves backwards.

```python
list(range(5, 0, -1))
```

Output:

```text
[5, 4, 3, 2, 1]
```

### Reverse Sequence

```python
list(range(10, 0, -2))
```

Output:

```text
[10, 8, 6, 4, 2]
```

For a negative step:

```text
start > stop
```

is normally required to produce values.

---

## Positive vs Negative Step

### Positive Step

```python
list(range(1, 6, 1))
```

Output:

```text
[1, 2, 3, 4, 5]
```

The sequence moves upward.

### Negative Step

```python
list(range(5, 0, -1))
```

Output:

```text
[5, 4, 3, 2, 1]
```

The sequence moves downward.

---

## Empty Range

A range can contain no values.

```python
list(range(5, 5))
```

Output:

```text
[]
```

Because `start` and `stop` are equal.

A positive step also cannot move toward a smaller `stop`:

```python
list(range(5, 1, 1))
```

Output:

```text
[]
```

Similarly, a negative step cannot move toward a larger `stop`:

```python
list(range(1, 5, -1))
```

Output:

```text
[]
```

---

## Step Cannot Be Zero

`step` cannot be `0`.

```python
range(1, 5, 0)
```

Output:

```text
ValueError: range() arg 3 must not be zero
```

---

## `range()` Accepts Integers

`range()` works with integer values.

```python
range(1, 5)
```

But floating-point values are not allowed:

```python
range(1.5, 5)
```

Output:

```text
TypeError
```

For decimal values, other approaches are needed.

---

## `len()` with `range()`

`len()` returns the number of values in the range.

```python
print(len(range(1, 10)))
```

Output:

```text
9
```

Another example:

```python
print(len(range(0, 20, 2)))
```

Output:

```text
10
```

---

## Indexing

A `range` object supports indexing.

```python
numbers = range(10)

print(numbers[2])
```

Output:

```text
2
```

Another example:

```python
numbers = range(2, 10)

print(numbers[3])
```

Output:

```text
5
```

Indexing starts from `0`.

---

## Negative Indexing

Negative indexes can also be used.

```python
numbers = range(10)

print(numbers[-1])
```

Output:

```text
9
```

```python
print(numbers[-2])
```

Output:

```text
8
```

---

## Slicing

A `range` object supports slicing.

```python
numbers = range(10)

print(numbers[2:7])
```

Output:

```text
range(2, 7)
```

Convert it to a list to see the values:

```python
print(list(numbers[2:7]))
```

Output:

```text
[2, 3, 4, 5, 6]
```

Slicing can also have a step:

```python
print(list(range(10)[1:8:2]))
```

Output:

```text
[1, 3, 5, 7]
```

---

## Membership with `in`

You can check whether a value exists in a range.

```python
print(5 in range(1, 10))
```

Output:

```text
True
```

```python
print(10 in range(1, 10))
```

Output:

```text
False
```

This also works with stepped ranges:

```python
print(6 in range(0, 11, 2))
```

Output:

```text
True
```

```python
print(7 in range(0, 11, 2))
```

Output:

```text
False
```

---

## `.start`, `.stop`, and `.step`

A `range` object has three useful attributes.

```python
numbers = range(2, 10, 2)

print(numbers.start)
print(numbers.stop)
print(numbers.step)
```

Output:

```text
2
10
2
```

They represent:

```text
start → 2
stop  → 10
step  → 2
```

These attributes are read-only.

---

## `reversed()` with `range()`

`reversed()` can be used to iterate through a range backwards.

```python
numbers = range(1, 6)

for i in reversed(numbers):
    print(i)
```

Output:

```text
5
4
3
2
1
```

You can also convert it to a list:

```python
print(list(reversed(range(1, 6))))
```

Output:

```text
[5, 4, 3, 2, 1]
```

---

## Range Equality

Two ranges can be equal if they represent the same sequence of values, even if their `start`, `stop`, and `step` are different.

```python
print(range(0) == range(2, 1, 3))
```

Output:

```text
True
```

For non-empty ranges:

```python
print(range(0, 3, 2) == range(0, 4, 2))
```

Output:

```text
True
```

Both represent:

```text
0 2
```

---

## Range Is Immutable

A `range` object cannot be modified after it is created.

```python
numbers = range(5)

numbers[0] = 10
```

Output:

```text
TypeError
```

You cannot directly change individual values.

If you need to modify the values, convert the range to a list:

```python
numbers = list(range(5))

numbers[0] = 10

print(numbers)
```

Output:

```text
[10, 1, 2, 3, 4]
```

---

## Memory Efficiency

`range()` is memory-efficient because it does not store every number as a separate list element.

```python
numbers = range(1000000000)
```

This creates a range object without creating a list containing one billion integers.

If you do this:

```python
numbers = list(range(1000000000))
```

Python has to create and store all those values in memory.

Therefore, `range()` is especially useful for large sequences and loops.

---

## Large Ranges

`range()` can represent very large integer ranges.

```python
numbers = range(1000000000000)

print(numbers.start)
print(numbers.stop)
```

Output:

```text
0
1000000000000
```

The range object itself remains memory-efficient.

---

## Common Patterns

### Print Numbers

```python
for i in range(1, 6):
    print(i)
```

### Print Even Numbers

```python
for i in range(2, 11, 2):
    print(i)
```

### Print Odd Numbers

```python
for i in range(1, 10, 2):
    print(i)
```

### Countdown

```python
for i in range(10, 0, -1):
    print(i)
```

### Multiplication Table

```python
num = 5

for i in range(1, 11):
    print(num * i)
```

Output:

```text
5
10
15
20
25
30
35
40
45
50
```

### Iterating Through a List Using Index

```python
names = ["Ali", "Zaid", "Sara"]

for i in range(len(names)):
    print(i, names[i])
```

Output:

```text
0 Ali
1 Zaid
2 Sara
```

---

## Common Mistakes

### Forgetting That `stop` Is Excluded

```python
list(range(1, 5))
```

Output:

```text
[1, 2, 3, 4]
```

Not:

```text
[1, 2, 3, 4, 5]
```

### Using the Wrong Step Direction

```python
list(range(1, 10, -1))
```

Output:

```text
[]
```

Use:

```python
list(range(10, 1, -1))
```

Output:

```text
[10, 9, 8, 7, 6, 5, 4, 3, 2]
```

### Using `0` as Step

```python
range(1, 10, 0)
```

This raises a `ValueError`.

### Expecting a List

```python
numbers = range(5)

print(numbers)
```

Output:

```text
range(0, 5)
```

Use:

```python
print(list(numbers))
```

Output:

```text
[0, 1, 2, 3, 4]
```

### Using Floats

```python
range(1.0, 5.0)
```

This raises a `TypeError`.

---

## Quick Reference

| Expression         | Values           |
| ------------------ | ---------------- |
| `range(5)`         | `0, 1, 2, 3, 4`  |
| `range(2, 6)`      | `2, 3, 4, 5`     |
| `range(2, 10, 2)`  | `2, 4, 6, 8`     |
| `range(5, 0, -1)`  | `5, 4, 3, 2, 1`  |
| `range(10, 0, -2)` | `10, 8, 6, 4, 2` |
| `range(5, 5)`      | empty            |
| `range(5, 1)`      | empty            |
| `range(1, 5, -1)`  | empty            |

---

## Key Points

* `range()` is a built-in Python function.
* It generates a sequence of integers.
* `range(stop)` starts from `0`.
* `start` is included.
* `stop` is excluded.
* Default `step` is `1`.
* `step` cannot be `0`.
* A negative `step` moves backwards.
* `range()` accepts integers, not floats.
* `range()` returns a `range` object.
* Use `list(range(...))` to convert it to a list.
* `range` supports indexing and slicing.
* `range` supports `in` membership checking.
* `.start`, `.stop`, and `.step` give its parameters.
* `range` objects are immutable.
* `range()` is memory-efficient because it does not store all values as a list.
* `range()` is most commonly used with `for` loops.