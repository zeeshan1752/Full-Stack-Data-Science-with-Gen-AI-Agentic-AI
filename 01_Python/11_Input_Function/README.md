# Python `input()` Function

The `input()` function is used to **take input from the user** during program execution.

It allows the user to enter a value through the keyboard.

---

## What is `input()`?

`input()` is a **built-in Python function**.

It pauses the program and waits for the user to enter something.

### Syntax

```python
input()
```

Example:

```python
name = input()

print(name)
```

If the user enters:

```text
Zeeshan
```

Output:

```text
Zeeshan
```

---

# Taking Input with a Message

We can display a message inside `input()` to tell the user what they need to enter.

### Syntax

```python
input("message")
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

Output:

```text
Enter your name: Zeeshan
Zeeshan
```

The message inside `input()` is called the **prompt**.

---

# Storing Input in a Variable

Usually, we store the value entered by the user in a variable.

```python
name = input("Enter your name: ")
```

Here:

* `input()` takes input from the user.
* `"Enter your name: "` is the prompt.
* `name` stores the entered value.

Example:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)
```

---

# Important Point: `input()` Always Returns a String

This is one of the most important things to remember.

By default, `input()` returns the user's input as a **string (`str`)**.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
21
```

Output:

```text
<class 'str'>
```

Even though `21` looks like a number, Python treats it as a string.

---

# Why Does `input()` Return a String?

User input is received as text.

For example:

```python
age = input("Enter your age: ")
```

If the user enters:

```text
21
```

Python receives it as:

```python
"21"
```

Not:

```python
21
```

The quotes indicate that it is a string.

---

# Taking Integer Input

If we want to perform mathematical operations on the input, we need to convert the string into an integer.

We can use `int()`.

### Syntax

```python
int(input())
```

Example:

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

If the user enters:

```text
21
```

Output:

```text
21
<class 'int'>
```

---

# Taking Float Input

For decimal values, we can use `float()`.

### Syntax

```python
float(input())
```

Example:

```python
price = float(input("Enter the price: "))

print(price)
print(type(price))
```

If the user enters:

```text
99.50
```

Output:

```text
99.5
<class 'float'>
```

---

# Taking Boolean Input

`input()` itself does not automatically convert text into `True` or `False`.

For example:

```python
value = input("Enter True or False: ")

print(type(value))
```

If the user enters:

```text
True
```

The value is still:

```python
"True"
```

and its type is:

```text
str
```

For beginners, boolean input should be handled using proper conversion logic instead of directly using `bool(input())`.

### Important

This is **not** a reliable way to take boolean input:

```python
value = bool(input())
```

Because:

```python
bool("False")
```

returns:

```text
True
```

Any non-empty string is considered `True`.

---

# Input and Type Conversion

Since `input()` returns a string, we often combine it with type conversion functions.

| Required Data Type | Example          |
| ------------------ | ---------------- |
| String             | `input()`        |
| Integer            | `int(input())`   |
| Float              | `float(input())` |

Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

---

# Input for Mathematical Operations

If we directly take numbers using `input()`, Python treats them as strings.

Example:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

If the user enters:

```text
10
20
```

Output:

```text
1020
```

Why?

Because:

```python
"10" + "20"
```

means **string concatenation**.

---

## Correct Way

Convert the input into integers.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Output:

```text
30
```

---

# Taking Multiple Inputs

There are different ways to take multiple values from the user.

## Method 1: Separate `input()` Statements

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

This is the easiest method for beginners.

---

## Method 2: Multiple Values in One Line

We can use `split()` to take multiple inputs from one line.

```python
a, b = input("Enter two numbers: ").split()
```

If the user enters:

```text
10 20
```

Then:

```python
a = "10"
b = "20"
```

Both values are strings.

To convert them into integers:

```python
a, b = map(int, input("Enter two numbers: ").split())
```

Now:

```python
a = 10
b = 20
```

and both are integers.

---

# `input()` with `split()`

`split()` separates a string into multiple parts.

Example:

```python
data = input("Enter your name and city: ").split()

print(data)
```

Input:

```text
Zeeshan Hyderabad
```

Output:

```text
['Zeeshan', 'Hyderabad']
```

---

# `input()` with `map()`

`map()` can be used to apply a conversion function to multiple inputs.

Example:

```python
a, b, c = map(int, input("Enter three numbers: ").split())

print(a)
print(b)
print(c)
```

Input:

```text
10 20 30
```

Output:

```text
10
20
30
```

Here:

```python
map(int, ...)
```

converts each input value into an integer.

---

# Input with Different Data Types

Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)
```

Example input:

```text
Enter your name: Zeeshan
Enter your age: 21
Enter your height: 5.8
```

Output:

```text
Name: Zeeshan
Age: 21
Height: 5.8
```

---

# `input()` and the `print()` Function

Both functions are commonly used together.

### `input()`

Used to **take data from the user**.

### `print()`

Used to **display data to the user**.

Example:

```python
name = input("Enter your name: ")

print("Hello", name)
```

Input:

```text
Zeeshan
```

Output:

```text
Hello Zeeshan
```

---

# Input and Variables

`input()` is commonly used when we want the user to provide a value that will be stored in a variable.

Example:

```python
name = input("Enter your name: ")
```

The flow is:

```text
User
  ↓
input()
  ↓
Value received as string
  ↓
Variable
```

Example:

```python
name = input("Enter your name: ")
```

---

# Common Mistake

### Incorrect

```python
age = input("Enter your age: ")

print(age + 5)
```

This causes an error because `age` is a string.

Python cannot directly add:

```python
"21" + 5
```

### Correct

```python
age = int(input("Enter your age: "))

print(age + 5)
```

Output:

```text
26
```

---

# Input Conversion Flow

When we use:

```python
age = int(input("Enter your age: "))
```

The process is:

```text
User enters 21
       ↓
input()
       ↓
"21" (string)
       ↓
int()
       ↓
21 (integer)
       ↓
age
```

Similarly:

```python
price = float(input("Enter price: "))
```

Flow:

```text
User enters 99.50
       ↓
input()
       ↓
"99.50" (string)
       ↓
float()
       ↓
99.5 (float)
       ↓
price
```

---

# Important Functions Used with `input()`

| Function  | Purpose                               | Example                     |
| --------- | ------------------------------------- | --------------------------- |
| `input()` | Takes input as string                 | `input()`                   |
| `int()`   | Converts to integer                   | `int(input())`              |
| `float()` | Converts to float                     | `float(input())`            |
| `str()`   | Converts to string                    | `str(value)`                |
| `split()` | Splits input into parts               | `input().split()`           |
| `map()`   | Applies conversion to multiple values | `map(int, input().split())` |

---

# Real Example

Let's create a simple program that takes two numbers and calculates their sum.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum:", sum)
```

Example:

```text
Enter first number: 25
Enter second number: 15
Sum: 40
```

---

# Important Points to Remember

1. `input()` is a **built-in Python function**.
2. It is used to **take input from the user**.
3. `input()` returns the entered value as a **string**.
4. Use `int()` when an integer is required.
5. Use `float()` when a decimal number is required.
6. Use `split()` to separate multiple values entered in one line.
7. Use `map()` when the same conversion needs to be applied to multiple values.
8. `input()` is commonly used with variables.
9. For mathematical operations, convert numeric input into the required numeric type.
10. Do not use `bool(input())` directly for normal `True`/`False` input because any non-empty string becomes `True`.

---

# Quick Revision

```python
# String input
name = input("Enter your name: ")

# Integer input
age = int(input("Enter your age: "))

# Float input
price = float(input("Enter price: "))

# Multiple string inputs
a, b = input("Enter two values: ").split()

# Multiple integer inputs
a, b = map(int, input("Enter two numbers: ").split())
```

### Main Rule

```text
input() → always returns string
```

For numbers:

```text
int(input())   → integer
float(input()) → float
```

---

# Summary

The `input()` function is used whenever a Python program needs to **receive information from the user**.

The most important concept is:

```python
input()
```

always gives the entered value as a **string**.

Therefore, when taking numeric input, we usually use type conversion:

```python
int(input())
```

or:

```python
float(input())
```

Understanding `input()` is important because it is used in many beginner-level Python programs and helps us create programs that can interact with users.