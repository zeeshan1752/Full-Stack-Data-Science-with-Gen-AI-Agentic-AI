# Python Data Types

Data types tell Python what kind of value a variable is storing.

For example, a variable can store a whole number, decimal number, `True` or `False`, a complex number, or text.

In this topic, we will learn the following basic data types:

- Integer (`int`)
- Float (`float`)
- Boolean (`bool`)
- Complex (`complex`)
- String (`str`)

We will also learn:

- `type()` function
- `id()` function

---

# 1. Integer

An integer is a **whole number** without a decimal point.

It can be:

- Positive
- Negative
- Zero

### Examples

```python
age = 21
marks = 95
temperature = -5
count = 0
````

### Checking the Type

We can use the `type()` function to check the data type.

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

### Important Point

The data type of an integer is:

```text
int
```

---

# 2. Float

A float is a number that contains a **decimal point**.

It is used when we need to store decimal values.

### Examples

```python
price = 99.50
height = 5.8
temperature = -2.5
```

### More Examples

```python
x = 10.0
y = 3.14
z = -7.25
```

Even `10.0` is a float because it contains a decimal point.

### Checking the Type

```python
price = 99.50

print(type(price))
```

Output:

```text
<class 'float'>
```

### Scientific Notation

Python also supports scientific notation for floating-point numbers.

```python
x = 2e3
y = 5.5e2
```

Here:

```text
2e3 = 2 × 10³ = 2000.0

5.5e2 = 5.5 × 10² = 550.0
```

### Important Point

The data type of a float is:

```text
float
```

---

# 3. Boolean

Boolean is a data type that has only two values:

* `True`
* `False`

Boolean values are mainly used when we want to represent whether something is true or false.

### Examples

```python
is_student = True
is_logged_in = False
```

### Boolean with Comparison

Comparison operations return a Boolean value.

```python
age = 21

print(age > 18)
print(age == 21)
```

Output:

```text
True
True
```

Another example:

```python
age = 15

print(age >= 18)
```

Output:

```text
False
```

### Checking the Type

```python
is_student = True

print(type(is_student))
```

Output:

```text
<class 'bool'>
```

### Important Point

The data type of Boolean is:

```text
bool
```

### Note

`True` and `False` must start with a capital letter.

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

---

# 4. Complex

A complex number contains two parts:

1. Real part
2. Imaginary part

The imaginary part is represented using `j` or `J`.

Python accepts both lowercase `j` and uppercase `J`.

---

## Format

```text
real + imaginaryj
```

For example:

```text
3 + 4j
```

Here:

```text
3 = Real part
4j = Imaginary part
```

---

## Syntax

```python
variable = real + imaginaryj
```

Example:

```python
x = 3 + 4j
```

Both `j` and `J` are accepted:

```python
x = 3 + 4j
y = 3 + 4J
```

Both are valid complex numbers.

---

## Example 1

```python
x = 3 + 4j

print(x)
```

Output:

```text
(3+4j)
```

Here:

```text
Real part = 3
Imaginary part = 4
```

---

## Example 2

```python
y = 5 - 2J

print(y)
```

Output:

```text
(5-2j)
```

Here:

```text
Real part = 5
Imaginary part = -2
```

Notice that Python displays the imaginary part using lowercase `j`, even if we write `J`.

---

## Checking the Type

```python
x = 3 + 4j

print(type(x))
```

Output:

```text
<class 'complex'>
```

### Important Point

The data type of a complex number is:

```text
complex
```

---

## Getting Real and Imaginary Parts

Python provides `.real` and `.imag` to get the real and imaginary parts of a complex number.

```python
x = 3 + 4j

print(x.real)
print(x.imag)
```

Output:

```text
3.0
4.0
```

Notice that the values are displayed as floats.

---

# 5. String

A string is used to store **text or a sequence of characters**.

The data type of a string is:

```text
str
```

Examples:

```text
"Hello"
"Python"
"Zeeshan"
"123"
```

A string can contain:

* Letters
* Numbers
* Spaces
* Special characters

> String definition, creation, indexing, slicing, methods, and other string concepts are covered separately in the **String** topic.

---

# `type()` Function

The `type()` function is used to check the **data type of a value or object**.

## Syntax

```python
type(object)
```

### Example

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

---

## More Examples

```python
x = 10
y = 10.5
z = True
a = 3 + 4j
b = "Python"

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'complex'>
<class 'str'>
```

---

## Why Do We Use `type()`?

We use `type()` when we want to know what type of data a variable or value contains.

For example:

```python
name = "Python"

print(type(name))
```

Output:

```text
<class 'str'>
```

So, `name` contains a string value.

---

# `id()` Function

The `id()` function returns the **identity of an object**.

In simple words, it gives a unique identification number for an object during its lifetime.

## Syntax

```python
id(object)
```

---

## Example

```python
x = 10

print(id(x))
```

Output will be a number similar to:

```text
140732123456789
```

The exact number can be different on different systems and different Python runs.

---

## Another Example

```python
name = "Python"

print(id(name))
```

This will return the identity number of the object referred to by `name`.

---

## Using `id()` with Two Variables

```python
x = 10
y = x

print(id(x))
print(id(y))
```

Both will normally show the same ID because both variables refer to the same object.

Example output:

```text
140732123456789
140732123456789
```

---

# Difference Between `type()` and `id()`

| Function | Purpose                           |
| -------- | --------------------------------- |
| `type()` | Tells the data type of an object  |
| `id()`   | Returns the identity of an object |

### Example

```python
x = 25

print(type(x))
print(id(x))
```

Output:

```text
<class 'int'>
140732123456789
```

The ID number shown above is only an example. Your output can be different.

---

# Quick Summary of Data Types

| Data Type | Python Type | Example    |
| --------- | ----------- | ---------- |
| Integer   | `int`       | `10`       |
| Float     | `float`     | `10.5`     |
| Boolean   | `bool`      | `True`     |
| Complex   | `complex`   | `3 + 4j`   |
| String    | `str`       | `"Python"` |

---

# Basic Example

We can store different types of values in different variables.

```python
age = 21
height = 5.8
is_student = True
number = 3 + 4j
name = "Python"

print(age)
print(height)
print(is_student)
print(number)
print(name)
```

We can also check their types:

```python
print(type(age))
print(type(height))
print(type(is_student))
print(type(number))
print(type(name))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'complex'>
<class 'str'>
```

---

# Important Points

* `int` is used for whole numbers.
* `float` is used for decimal numbers.
* `bool` has only two values: `True` and `False`.
* `complex` contains a real part and an imaginary part.
* Both `j` and `J` are accepted for complex numbers.
* `str` is used to store text.
* `type()` is used to check the data type of an object.
* `id()` returns the identity of an object.
* The exact value returned by `id()` can be different on different systems or Python runs.
* Python is a **dynamically typed language**, so we do not need to specify the data type while creating a variable.

---

# Final Example

```python
# Integer
age = 21

# Float
height = 5.8

# Boolean
is_student = True

# Complex
number = 3 + 4j

# String
name = "Python"

# Checking data types
print(type(age))
print(type(height))
print(type(is_student))
print(type(number))
print(type(name))

# Checking object identity
print(id(age))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'complex'>
<class 'str'>
140732123456789
```

> The `id()` value will be different depending on the system and Python run.