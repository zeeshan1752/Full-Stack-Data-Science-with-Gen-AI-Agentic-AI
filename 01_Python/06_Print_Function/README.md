# Python Print Function

## What is the `print()` Function?

The `print()` function is a built-in Python function used to **display output on the screen**.

It can be used to display:

* Text
* Numbers
* Variables
* Calculated values
* Multiple values together

### Basic Syntax

```python
print(value)
```

### Example

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

## When Do We Use `print()`?

If we want to display something as output, we use the `print()` function.

For a single statement, we can directly write the statement without using multiple `print()` functions.

For example:

```python
print("Hello")
```

When we have multiple values or results to display, we can also combine them into a single `print()` statement.

Example:

```python
name = "Zeeshan"
age = 21

print(name, age)
```

Output:

```text
Zeeshan 21
```

Using one `print()` statement can sometimes make the code shorter and reduce unnecessary output statements.

---

# Printing Text

We can use `print()` to display text.

Text is written inside quotes.

```python
print("Hello Python")
print("I am learning Python")
```

Output:

```text
Hello Python
I am learning Python
```

Both single and double quotes can be used:

```python
print("Hello")
print('Hello')
```

---

# Printing Numbers

We can also print numbers directly.

```python
print(10)
print(25.5)
```

Output:

```text
10
25.5
```

We do not need quotes when printing numbers.

```python
print(10)
```

Here `10` is treated as a number.

```python
print("10")
```

Here `10` is treated as text.

---

# Printing Text and Numbers Together

We can print text and numbers together by separating them with a comma.

```python
age = 21

print("My age is", age)
```

Output:

```text
My age is 21
```

---

# Printing Calculated Values

We can also print the result of a calculation.

Example:

```python
num1 = 3
num2 = 6
add = num1 + num2

print("The sum of num1 and num2 is", add)
```

Output:

```text
The sum of num1 and num2 is 9
```

Here:

* `num1` contains `3`
* `num2` contains `6`
* `add` contains the result of `num1 + num2`
* `print()` displays the text and result together

---

# Code Optimization Using `print()`

Code optimization means improving the code so that it is simpler and more efficient.

Sometimes, we use multiple `print()` statements when a single `print()` statement can do the same work.

### Multiple `print()` Statements

```python
print("Hello")
print("My name is Zeeshan")
print("I am learning Python")
```

### Single `print()` Statement

```python
print("Hello", "My name is Zeeshan", "I am learning Python")
```

The second example uses only one `print()` function.

### Another Example

Instead of:

```python
num1 = 3
num2 = 6

print("Number 1 is", num1)
print("Number 2 is", num2)
print("The sum is", num1 + num2)
```

We can write:

```python
num1 = 3
num2 = 6

print("Number 1 is", num1, "Number 2 is", num2, "The sum is", num1 + num2)
```

This reduces the number of `print()` calls.

> **Note:** Reducing unnecessary `print()` calls can make code shorter and cleaner. It is not correct to assume that every `print()` always consumes exactly 1 KB of memory. The actual memory usage depends on Python's implementation and runtime.

---

# Format Method

The `format()` method can be used to insert values into a string.

### Syntax

```python
"{}".format(value)
```

### Example

```python
num1 = 3
num2 = 6
add = num1 + num2

print("The sum of {} and {} is {}.".format(num1, num2, add))
```

Output:

```text
The sum of 3 and 6 is 9.
```

Another Example

```python
name = "Zeeshan"
age = 21

print("My name is {} and I am {} years old".format(name, age))
```

Output:

```text
My name is Zeeshan and I am 21 years old
```

The `{}` acts as a placeholder for the values.

---

# F-String

F-string is another simple way to insert variables inside a string.

An `f` or `F` is written before the string.

### Syntax

```python
f"text {variable}"
```

### Example

```python
num1 = 3
num2 = 6
add = num1 + num2

print(f"The sum of {num1} and {num2} is {add}.")
```

Output:

```text
The sum of 3 and 6 is 9.
```

Another example:

```python
name = "Zeeshan"
age = 21

print(f"My name is {name} and I am {age} years old")
```

Output:

```text
My name is Zeeshan and I am 21 years old
```

F-strings are generally easier to read when we have multiple variables.

---

# `end` Parameter

By default, `print()` moves to a new line after printing.

Example:

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

The `end` parameter can change what is printed at the end.

### Example

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Here, instead of moving to a new line, the first `print()` ends with a space.

### Another Example

```python
print("Hello", end="...")
print("World")
```

Output:

```text
Hello...World
```

### Default Value of `end`

The default value of `end` is:

```python
end="\n"
```

`\n` means a new line.

Therefore:

```python
print("Hello")
```

is similar to:

```python
print("Hello", end="\n")
```

---

# `sep` Parameter

The `sep` parameter is used to specify the separator between multiple values in `print()`.

By default, `print()` uses a space as the separator.

### Example

```python
print("Python", "Java", "C++")
```

Output:

```text
Python Java C++
```

Here, the default separator is a space.

### Using `sep`

```python
print("Python", "Java", "C++", sep="-")
```

Output:

```text
Python-Java-C++
```

Another example:

```python
print(10, 20, 30, sep=",")
```

Output:

```text
10,20,30
```

### Default Value of `sep`

The default value is:

```python
sep=" "
```

So:

```python
print("Python", "Java")
```

is similar to:

```python
print("Python", "Java", sep=" ")
```

---

# Difference Between `sep` and `end`

| Parameter | Purpose                                                |
| --------- | ------------------------------------------------------ |
| `sep`     | Defines what comes **between multiple values**         |
| `end`     | Defines what comes **after the complete print output** |

### Example

```python
print("Python", "Java", "C++", sep=" | ", end=" Done")
```

Output:

```text
Python | Java | C++ Done
```

Here:

* `sep=" | "` is used between the values.
* `end=" Done"` is added at the end.

---

# Important Points

* `print()` is a built-in Python function.
* It is mainly used to display output.
* It can print text, numbers, variables, and calculated values.
* Multiple values can be printed using commas.
* `format()` can be used to insert values into strings.
* F-strings can also be used to insert variables into strings.
* `end` controls what is printed after the output.
* `sep` controls what is printed between multiple values.
* The default value of `end` is `"\n"`.
* The default value of `sep` is `" "`.
* Reducing unnecessary `print()` calls can make code shorter and cleaner.
* `print()` has runtime and memory overhead, but its memory usage should not be treated as a fixed 1 KB.

---

# Quick Revision

```python
# Basic print
print("Hello World")

# Printing a number
print(100)

# Printing text and number
age = 21
print("My age is", age)

# Printing calculated value
num1 = 3
num2 = 6
add = num1 + num2

print("The sum of num1 and num2 is", add)

# Using format()
print("The sum is {}".format(add))

# Using f-string
print(f"The sum is {add}")

# Using end
print("Hello", end=" ")
print("World")

# Using sep
print("Python", "Java", "C++", sep=" | ")
```

---

## Summary

The `print()` function is one of the most basic and important functions in Python. It is used to display output on the screen. We can use it with text, numbers, variables, and calculated values.

We can also control the output using parameters like `sep` and `end`. For inserting variables into text, `format()` and f-strings provide useful ways to create readable output.
