# Python Swapping

Swapping means **exchanging the values of two variables**.

For example:

```python
a = 10
b = 20
```

After swapping:

```python
a = 20
b = 10
```

Python provides a very simple way to swap values using **multiple assignment**.

---

## 1. Swapping using Multiple Assignment

This is the **recommended and most Pythonic way**.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

Python handles the exchange directly without creating a temporary variable.

### Why use this?

* Simple
* Easy to read
* No extra variable required
* Commonly used in Python

---

## 2. Swapping using a Temporary Variable

We can also use a third variable to store one value temporarily.

```python
a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)
```

Output:

```text
20
10
```

### Working

Initially:

```text
a = 10
b = 20
```

Store `a` in `temp`:

```text
temp = 10
```

Put `b` into `a`:

```text
a = 20
```

Put `temp` into `b`:

```text
b = 10
```

Final result:

```text
a = 20
b = 10
```

---

## 3. Swapping using Arithmetic Operators

Swapping can also be done using addition and subtraction.

```python
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a)
print(b)
```

Output:

```text
20
10
```

### Working

Initially:

```text
a = 10
b = 20
```

After:

```text
a = a + b
```

```text
a = 30
b = 20
```

Then:

```text
b = a - b
```

```text
a = 30
b = 10
```

Then:

```text
a = a - b
```

```text
a = 20
b = 10
```

### Note

This method is mainly useful for understanding the logic. It is **not normally preferred in Python**.

---

## 4. Swapping using XOR

Two integer values can also be swapped using the **XOR (`^`) bitwise operator**.

```python
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)
```

Output:

```text
20
10
```

### How it works

The XOR operation has these important properties:

```text
a ^ a = 0
a ^ 0 = a
```

Using these properties, the values can be exchanged without a temporary variable.

### Note

This method works with integers and is mainly useful for understanding **bitwise operations**.

In normal Python code, use:

```python
a, b = b, a
```

instead.

---

# Comparison of Swapping Methods

| Method                  | Extra Variable | Recommended in Python | Important                   |
| ----------------------- | -------------- | --------------------- | --------------------------- |
| Multiple Assignment     | No             | Yes                   | ⭐ Most important           |
| Temporary Variable      | Yes            | Yes                   | Basic programming concept   |
| Addition/Subtraction    | No             | No                    | Conceptual                  |
| XOR                     | No             | No                    | Useful for bitwise learning |

---

# Most Important Method

For Python, remember this:

```python
a, b = b, a
```

This is the **standard Python way to swap two variables**.

---

# Practice Examples

## Example 1: Swap Two Numbers

```python
a = 5
b = 10

a, b = b, a

print(a)
print(b)
```

Output:

```text
10
5
```

## Example 2: Swap User Input Values

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
```

---

# Key Points

* Swapping means **exchanging the values of two variables**.
* Python supports swapping using **multiple assignment**.
* `a, b = b, a` is the **preferred Python method**.
* A temporary variable can also be used.
* Arithmetic and XOR methods are mainly useful for understanding programming concepts.
* XOR swapping works with **integers**.
* In Python, there is usually **no reason to use complicated swapping methods** when multiple assignment is available.
