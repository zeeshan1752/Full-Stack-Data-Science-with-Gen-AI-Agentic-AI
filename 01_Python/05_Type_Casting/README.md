# Python Type Casting

## What is Type Casting?

Type casting means converting one data type into another data type.

Python provides built-in functions for type casting:

- `int()` → converts a value to integer
- `float()` → converts a value to float
- `bool()` → converts a value to boolean
- `complex()` → converts a value to complex
- `str()` → converts a value to string

---

# 1. Convert Other Data Types to Integer

The `int()` function is used to convert a value into an integer.

### Syntax

`int(value)`

### Float to Integer

A float can be converted to an integer.

The decimal part is removed.

```python
num = 10.5

print(int(num))
```

Output:

```text
10
```

Another example:

```python
num = -10.8

print(int(num))
```

Output:

```text
-10
```

### String to Integer

A string containing a valid whole number can be converted to an integer.

```python
num = "10"

print(int(num))
print(type(int(num)))
```

Output:

```text
10
<class 'int'>
```

Negative numbers are also possible:

```python
num = "-10"

print(int(num))
```

Output:

```text
-10
```

### String Values That Cannot Be Converted to Integer

A string containing words cannot be converted to an integer.

```python
print(int("ten"))       # ValueError
```

A string containing a decimal number also cannot be directly converted to an integer.

```python
print(int("10.5"))      # ValueError
```

So:

* `int("10")` → works
* `int("-10")` → works
* `int("ten")` → does not work
* `int("10.5")` → does not work

### Boolean to Integer

`True` becomes `1` and `False` becomes `0`.

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

### Complex to Integer

A complex number cannot be directly converted into an integer.

```python
num = 10 + 5j

print(int(num))        # TypeError
```

---

# 2. Convert Other Data Types to Float

The `float()` function is used to convert a value into a floating-point number.

### Syntax

`float(value)`

### Integer to Float

An integer can be converted to a float.

```python
num = 10

print(float(num))
print(type(float(num)))
```

Output:

```text
10.0
<class 'float'>
```

Negative integers are also possible:

```python
num = -10

print(float(num))
```

Output:

```text
-10.0
```

### String to Float

A string containing a valid number can be converted to a float.

```python
num = "10.5"

print(float(num))
print(type(float(num)))
```

Output:

```text
10.5
<class 'float'>
```

An integer value stored as a string can also be converted:

```python
num = "10"

print(float(num))
```

Output:

```text
10.0
```

### String Values That Cannot Be Converted to Float

A string containing words cannot be converted to a float.

```python
print(float("ten"))      # ValueError
```

So:

* `float("10")` → works
* `float("10.5")` → works
* `float("-10.5")` → works
* `float("ten")` → does not work

### Boolean to Float

`True` becomes `1.0` and `False` becomes `0.0`.

```python
print(float(True))
print(float(False))
```

Output:

```text
1.0
0.0
```

### Complex to Float

A complex number cannot be directly converted into a float.

```python
num = 10 + 5j

print(float(num))       # TypeError
```

---

# 3. Convert Other Data Types to Boolean

The `bool()` function is used to convert a value into either `True` or `False`.

### Syntax

`bool(value)`

### Integer to Boolean

`0` becomes `False`.

Any non-zero integer becomes `True`.

```python
print(bool(0))
print(bool(10))
print(bool(-5))
```

Output:

```text
False
True
True
```

### Float to Boolean

`0.0` becomes `False`.

Any non-zero float becomes `True`.

```python
print(bool(0.0))
print(bool(10.5))
print(bool(-2.5))
```

Output:

```text
False
True
True
```

### String to Boolean

An empty string becomes `False`.

A non-empty string becomes `True`.

```python
print(bool(""))
print(bool("Python"))
print(bool("ten"))
```

Output:

```text
False
True
True
```

Even a string containing `"0"` is non-empty, so it becomes `True`.

```python
print(bool("0"))
```

Output:

```text
True
```

### Complex to Boolean

`0j` becomes `False`.

Any non-zero complex number becomes `True`.

```python
print(bool(0j))
print(bool(2 + 3j))
```

Output:

```text
False
True
```

### Important Point

For `bool()`:

* `0` → `False`
* `0.0` → `False`
* `0j` → `False`
* `""` → `False`
* Non-zero numbers → `True`
* Non-empty strings → `True`

---

# 4. Convert Other Data Types to Complex

The `complex()` function is used to convert a value into a complex number.

### Syntax

`complex(value)`

### Integer to Complex

An integer can be converted to a complex number.

```python
num = 10

print(complex(num))
print(type(complex(num)))
```

Output:

```text
(10+0j)
<class 'complex'>
```

`complex()` accepts **maximum 2 arguments**.

### Syntax

`complex(real, imaginary)`

### Examples

`complex(10)`          → Works → `(10+0j)`

`complex(10, 5)`       → Works → `(10+5j)`

`complex(10, 5, 2)`    → TypeError

**Maximum 2 arguments are accepted.**

---

### Float to Complex

A float can be converted to a complex number.

```python
num = 10.5

print(complex(num))
```

Output:

```text
(10.5+0j)
```

### Boolean to Complex

`True` becomes `(1+0j)` and `False` becomes `0j`.

```python
print(complex(True))
print(complex(False))
```

Output:

```text
(1+0j)
0j
```

### String to Complex

A valid string representation of a complex number can be converted into a complex number.

```python
num = "10+5j"

print(complex(num))
```

Output:

```text
(10+5j)
```

A valid real number stored as a string can also be converted:

```python
num = "10"

print(complex(num))
```

Output:

```text
(10+0j)
```

### String Values That Cannot Be Converted to Complex

A string containing an invalid value cannot be converted.

```python
print(complex("ten"))       # ValueError
```

So:

* `complex("10")` → works
* `complex("10+5j")` → works
* `complex("ten")` → does not work

---

# 5. Convert Other Data Types to String

The `str()` function is used to convert a value into a string.

### Syntax

`str(value)`

### Integer to String

An integer can be converted to a string.

```python
num = 10

print(str(num))
print(type(str(num)))
```

Output:

```text
10
<class 'str'>
```

Negative integers can also be converted:

```python
num = -10

print(str(num))
```

Output:

```text
-10
```

### Float to String

A float can be converted to a string.

```python
num = 10.5

print(str(num))
```

Output:

```text
10.5
```

### Boolean to String

A boolean can be converted to a string.

```python
print(str(True))
print(str(False))
```

Output:

```text
True
False
```

### Complex to String

A complex number can be converted to a string.

```python
num = 10 + 5j

print(str(num))
```

Output:

```text
(10+5j)
```
---
### String with Two Arguments

When two arguments are passed to `complex()`, the first argument cannot be a string.

```python
complex(10, 5)       # Works
complex(10.5, 5)     # Works

complex("10", 5)     # TypeError
complex("10+5j", 5)  # TypeError
```
A string is accepted only when it is the first and only argument.

```python
complex("10")        # Works
complex("10+5j")     # Works
```
---
### Important Point

`str()` can convert values of different data types into strings.

* `str(10)` → `"10"`
* `str(10.5)` → `"10.5"`
* `str(True)` → `"True"`
* `str(10 + 5j)` → `"(10+5j)"`

---

# Important Conversion Summary

| From    | To `int`         | To `float`       | To `bool` | To `complex`     | To `str` |
| ------- | ---------------- | ---------------- | --------- | ---------------- | -------- |
| Integer | Yes              | Yes              | Yes       | Yes              | Yes      |
| Float   | Yes              | Yes              | Yes       | Yes              | Yes      |
| Boolean | Yes              | Yes              | Yes       | Yes              | Yes      |
| Complex | No               | No               | Yes       | Yes              | Yes      |
| String  | Depends on value | Depends on value | Yes       | Depends on value | Yes      |

---

# Important Points

1. Type casting means converting one data type into another data type.
2. `int()` is used to convert a value into an integer.
3. `float()` is used to convert a value into a float.
4. `bool()` is used to convert a value into `True` or `False`.
5. `complex()` is used to convert a value into a complex number.
6. `str()` is used to convert a value into a string.
7. The decimal part is removed when a float is converted to an integer.
8. `True` converts to `1` and `False` converts to `0` when converted to integer.
9. `0`, `0.0`, `0j`, and `""` convert to `False`.
10. Non-zero numbers convert to `True`.
11. A non-empty string converts to `True`.
12. A complex number cannot be directly converted to `int` or `float`.
13. A valid numeric string can be converted to `int` or `float`.
14. A valid complex-number string can be converted to `complex()`.
15. Invalid strings can give a `ValueError`.
16. Trying to convert a complex number directly to `int` or `float` gives a `TypeError`.
17. `str()` can convert values of different data types into strings.

---