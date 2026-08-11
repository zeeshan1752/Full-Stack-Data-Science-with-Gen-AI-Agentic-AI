# Python Strings

## What is a String?

A string is a collection of characters written inside quotes.

In Python, we can use:

- Single quotes: `'Hello'`
- Double quotes: `"Hello"`
- Triple single quotes: `'''Hello'''`
- Triple double quotes: `"""Hello"""`

---

## String Declaration

A string is declared by storing text inside a variable.

### Syntax

```python
variable_name = "value"
````

### Examples

```python
name = "Zeeshan"
course = "Python"
city = "Lucknow"
```

We can check the data type using the `type()` function.

```python
name = "Zeeshan"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

## Types of String Quotes

### Single Quotes

We can use single quotes to declare a string.

```python
name = 'Zeeshan'
```

### Double Quotes

We can also use double quotes to declare a string.

```python
name = "Zeeshan"
```

Both single and double quotes are commonly used for single-line strings.

---

## Triple Quotes

Triple quotes are used when we want to write **multiple lines of text** or a string that contains more than one line.

We can use:

* Triple single quotes: `''' '''`
* Triple double quotes: `""" """`

### Example using Triple Single Quotes

```python
message = '''Hello
My name is Zeeshan
I am learning Python'''
```

### Example using Triple Double Quotes

```python
message = """Hello
My name is Zeeshan
I am learning Python"""
```

Triple quotes can also be used for a single line.

```python
message = """Hello Python"""
```

### Use of Triple Quotes

Triple quotes are useful when:

* The string contains multiple lines.
* We want to preserve line breaks.
* We need to write a long text in multiple lines.

---

# String Concatenation

String concatenation means **joining two or more strings together**.

The `+` operator is used to concatenate strings.

### Syntax

```python
string1 + string2
```
Example

```python
first_name = "Zeeshan"
last_name = "Jamshed"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Zeeshan Jamshed
```

Here, `" "` is used to add a space between the two strings.

### Another Example

```python
first_name = "Hello"
last_name = "Python"

print(first_name + " " + last_name)
```

Output:

```text
Hello Python
```

### Important

We can concatenate strings using the `+` operator.

```python
name = "Python"
version = "3"

print(name + version)
```

Output:

```text
Python3
```

We cannot directly concatenate a string with an integer.

```python
age = 21

print("Age: " + age)
```

This gives a `TypeError`.

We can convert the integer into a string using `str()`.

```python
age = 21

print("Age: " + str(age))
```

Output:

```text
Age: 21
```

# String Index

Every character in a string has a position called an **index**.

Python uses **zero-based indexing**, which means the first character starts from index `0`.

Example:

```python
name = "Python"
```

| Character      | P  | y  | t  | h  | o  | n  |
| -------------- | -- | -- | -- | -- | -- | -- |
| Forward Index  | 0  | 1  | 2  | 3  | 4  | 5  |
| Backward Index | -6 | -5 | -4 | -3 | -2 | -1 |

---

# Indexing

Indexing is used to access a single character from a string.

### Syntax

```python
string[index]
```

### Example

```python
name = "Python"

print(name[0])
print(name[1])
print(name[2])
```

Output:

```text
P
y
t
```

---

## Forward Index

Forward indexing starts from the **left side**.

The first character has index `0`.

```text
P   y   t   h   o   n
0   1   2   3   4   5
```

### Example

Forward indexing is useful when we want to access characters by counting from the beginning of the string.

```python
name = "Python"

print(name[0])
print(name[3])
print(name[5])
```

Output:

```text
P
h
n
```

---

## Backward Index

Backward indexing starts from the **right side**.

The last character has index `-1`.

```text
P    y    t    h    o    n
-6   -5   -4   -3   -2   -1
```

### Example

Backward indexing is useful when we want to access characters by counting from the end of the string.

```python
name = "Python"

print(name[-1])
print(name[-2])
print(name[-6])
```

Output:

```text
n
o
P
```

---

## Example for both:

We can use both positive and negative indexes to access characters.

```python
name = "Python"

# Forward indexing
print(name[0])
print(name[5])

# Backward indexing
print(name[-1])
print(name[-6])
```

Output:

```text
P
n
n
P
```

## IndexError

When we try to access an index that does not exist in a string, Python gives an `IndexError`.

### Example

```python
name = "Python"
print(name[10])
```
Output:

```text
IndexError: string index out of range
```

Here, the valid forward indexes are 0 to 5, so index 10 does not exist.

* In indexing, the index must be within the valid range.

```text
Python → 0  1  2  3  4  5
```

Using an index outside this range gives an IndexError.

---

# String Slicing

String slicing is used to get a **part of a string**.

### Syntax

```python
string[start:stop]
```
* start = starting index, included.
* stop = ending position, not included.
* The actual last included index is **stop - 1**.
* start < stop  → output
* start > stop  → ''


### Example

```python
name = "Python"
print(name[0:3])
```

Output:

```text
Pyt
```

Here:

* `0` is the starting index.
* `3` is the stopping index.
* Index `3` is not included.

---
### Important: Stop Can Be Out of Range

In slicing, the `stop` value can be greater than the length of the string.

Python does not give an error. It simply stops at the end of the string.

### Example

```python
name = "Python"
```

The valid indexes are:

```text
P   y   t   h   o   n
0   1   2   3   4   5
```

But we can use a stop value greater than the range:
```python
print(name[0:100])
```
Output:

```text
Python
```

* Even though 100 is outside the index range, Python prints the string up to the end.

---
## Forward Slicing

Forward slicing uses positive indexes and moves from **left to right**.

Example:

```text
P   y   t   h   o   n
0   1   2   3   4   5
```

### Example

Forward slicing is useful when we want to get a part of a string from the beginning or by using positive indexes.

```python
name = "Python"
print(name[0:3])
print(name[1:5])
```

Output:

```text
Pyt
ytho
```

---

## Backward Slicing

Backward slicing uses negative indexes and works from the **right side**.

Example:

```text
P    y    t    h    o    n
-6   -5   -4   -3   -2   -1
```

### Example

Backward slicing is useful when we want to get a part of a string by using negative indexes.

```python
name = "Python"

print(name[-4:-1])
print(name[-5:-2])
```

Output:

```text
tho
yth
```

The stop index is not included.

---

## Example for Both

We can use both positive and negative indexes for slicing.

```python
name = "Python"

# Forward slicing
print(name[1:5])

# Backward slicing
print(name[-5:-1])
```

Output:

```text
ytho
ytho
```
---

# Using Positive and Negative Indexes Together in Slicing

Negative indexes can be mentally converted to their equivalent positive indexes to understand the direction of slicing.

With the default step `(+1)`:

- If `start < stop` → characters are returned.
- If `start > stop` → empty string (`''`) is returned.

### Examples

    text[4:10]     # works
    text[10:4]     # ''

### Negative Index Example

If `-4` is equivalent to positive index `6`:

    text[-4:10]    # same direction as 6:10
    text[-4:2]     # same direction as 6:2 → ''

If `-4` is used as the stop index:

    text[2:-4]     # same as text[2:6] → works
    text[10:-4]    # same as text[10:6] → ''

> Note: Python does not actually convert the negative index into a positive index. We can do this mentally to understand the slicing direction easily.

---

## Slicing from the Beginning

If we do not give the start index, Python starts from index `0`.

### Syntax

```python
string[:stop]
```

### Example

```python
name = "Python"

print(name[:3])
```

Output:

```text
Pyt
```

---

## Slicing till the End

If we do not give the stop index, Python takes the string till the end.

### Syntax

```python
string[start:]
```

### Example

```python
name = "Python"

print(name[2:])
```

Output:

```text
thon
```

---

## Complete String using Slicing

We can use `[:]` to get the complete string.

```python
name = "Python"

print(name[:])
```

Output:

```text
Python
```

---

# String Slicing with Step

We can also give a third value called `step`.

### Syntax

```python
string[start:stop:step]
```

The `step` tells Python how many positions to move at a time.

### Example

```python
name = "Python"

print(name[0:6:2])
```

Output:

```text
Pto
```

Here, Python takes every second character.

---
### Slicing Direction Rule

Normal slicing:

- `start < stop` → output
- `start > stop` → `''`

Step slicing with a positive step (`+1`):

- `start < stop` → output
- `start > stop` → `''`

Step slicing with a negative step (`-1`):

- `start > stop` → output
- `start < stop` → `''`
- In the negative step, the last value is `stop + 1`.

---

## Reverse a String

We can reverse a string by using a negative step.

```python
name = "Python"

print(name[::-1])
```

Output:

```text
nohtyP
```

Here:

* Start is not given.
* Stop is not given.
* Step is `-1`.
* `-1` moves from right to left.

---

# Important Points

1. A string is a collection of characters.
2. Strings can be written using single quotes or double quotes.
3. Triple quotes can be used to write strings in multiple lines.
4. Python uses zero-based indexing.
5. Forward indexing starts from `0`.
6. Backward indexing starts from `-1`.
7. Forward indexing moves from left to right.
8. Backward indexing moves from right to left.
9. Indexing is used to access a single character.
10. If an index is outside the valid range, Python gives an `IndexError`.
11. Slicing is used to access a part of a string.
12. The syntax for slicing is `[start:stop]`.
13. The `start` index is included in slicing.
14. The `stop` index is not included in slicing.
15. If `stop = n`, the last included index is `n-1`.
16. The `stop` value can be greater than the string's index range.
17. An out-of-range `stop` value in slicing does not give an error.
18. When `stop` is out of range, Python prints up to the end of the string.
19. Positive indexes are used for forward indexing and slicing.
20. Negative indexes are used for backward indexing and slicing.
21. Slicing can be done from the beginning using `[:stop]`.
22. Slicing can be done till the end using `[start:]`.
23. `[:]` can be used to get the complete string.
24. A third value called `step` can be used in slicing.
25. The syntax for slicing with step is `[start:stop:step]`.
26. The `step` is used to skip characters.
27. A positive step moves from left to right.
28. A negative step moves from right to left.
29. `[::-1]` is commonly used to reverse a string.
30. Strings are immutable, so individual characters of a string cannot be changed directly.
31. String concatenation means joining two or more strings together.
32. The `+` operator is used for string concatenation.
33. A space can be added while concatenating by using `" "`.
34. A string cannot be directly concatenated with an integer or another different data type.
35. The `str()` function can be used to convert another data type into a string before concatenation.
36. Concatenating a string with an incompatible data type directly can give a `TypeError`.

---
