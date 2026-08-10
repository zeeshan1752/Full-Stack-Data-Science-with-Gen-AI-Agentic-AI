# Python Variables

## What is a Variable?

A **variable** is a name that refers to a value stored in memory.

In simple words, a variable gives a name to a value so that we can use that value later in our program.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Zeeshan"
age = 21
height = 5.8
```

Here:

* `name` is a variable.
* `"Zeeshan"` is the value.
* `age` is a variable.
* `21` is the value.
* `height` is a variable.
* `5.8` is the value.

---

# How Variables Work in Python

When we write:

```python
age = 21
```

Python creates the value `21` in memory and the name `age` refers to that value.

We can think of it like this:

```text
age ───────► 21
```

The variable name is used to access the value.

```python
age = 21

print(age)
```

Output:

```text
21
```

### Important Point

A variable is not exactly a box that permanently stores a value.

In Python, a variable name **refers to an object**.

For example:

```python
age = 21
```

The name `age` refers to the integer object `21`.

---

# Creating a Variable

A variable is created when we assign a value to a name.

```python
name = "Zeeshan"
age = 21
city = "Lucknow"
```

There is no separate declaration required before creating a variable.

For example, we do not need to write:

```python
int age
```

Instead, we simply write:

```python
age = 21
```

---

# Variable Assignment

The `=` operator is called the **assignment operator**.

It assigns a value to a variable.

```python
name = "Zeeshan"
age = 21
```

The right side is evaluated first, and then the result is assigned to the variable on the left.

```python
x = 10 + 5
```

Here:

```text
10 + 5 → 15
```

So:

```text
x → 15
```

---

# Reassigning a Variable

A variable can be assigned a new value.

```python
age = 21

age = 22

print(age)
```

Output:

```text
22
```

The variable `age` first referred to `21` and later referred to `22`.

```text
age ───► 21

age ───► 22
```

The old value is no longer referred to by `age`.

---

# Variables Can Change Their Value

Python allows us to assign different values to the same variable.

```python
value = 10
print(value)

value = 20
print(value)

value = 30
print(value)
```

Output:

```text
10
20
30
```

This is why we call it a **variable** — its assigned value can change.

---

# Python is Dynamically Typed

Python is a **dynamically typed language**.

This means we do not have to specify the type of a variable when creating it.

```python
value = 10
```

Later, we can assign another kind of value to the same variable:

```python
value = "Python"
```

And later:

```python
value = 5.8
```

Python automatically understands the type of the current value.

### Example

```python
value = 10
print(value)

value = "Hello"
print(value)
```

Output:

```text
10
Hello
```

The variable name is the same, but the value it refers to has changed.

---

# Variable Name vs Value

Consider:

```python
name = "Zeeshan"
```

There are two different things here:

```text
name       → variable name
"Zeeshan"  → value
```

The variable `name` refers to the value `"Zeeshan"`.

---

# Variable Naming Rules

Python has some rules for naming variables.

### 1. Variable names can contain letters

```python
name = "Zeeshan"
```

### 2. Variable names can contain numbers

```python
student1 = "Ali"
```

But a variable name **cannot start with a number**.

```python
1student = "Ali"    # Invalid
```

### 3. Underscore is allowed

```python
student_name = "Ali"
```

### 4. Spaces are not allowed

```python
student name = "Ali"    # Invalid
```

Use an underscore instead:

```python
student_name = "Ali"
```

### 5. Hyphen is not allowed

```python
student-name = "Ali"    # Invalid
```

Use:

```python
student_name = "Ali"
```

### 6. Variable names are case-sensitive

These are different variables:

```python
name = "Ali"
Name = "Zeeshan"
NAME = "Ahmed"
```

Python treats:

```text
name
Name
NAME
```

as three different names.

### 7. Python keywords cannot be used as variable names

For example:

```python
class = "Python"    # Invalid
```

`class` is a Python keyword.

---

# Valid Variable Names

```python
name = "Zeeshan"
age = 21
student_name = "Ali"
student1 = "Ahmed"
_marks = 95
total_marks = 450
mobile_number = 9876543210
```

---

# Invalid Variable Names

```python
1name = "Zeeshan"        # Cannot start with a number
student-name = "Ali"    # Hyphen is not allowed
student name = "Ali"    # Space is not allowed
class = "Python"        # Keyword cannot be used
```

---

# Meaningful Variable Names

Variable names should clearly tell us what the value represents.

### Good

```python
student_name = "Zeeshan"
total_marks = 450
mobile_number = 9876543210
employee_salary = 50000
```

### Not Good

```python
x = "Zeeshan"
a = 450
m = 9876543210
s = 50000
```

Meaningful names make code easier to understand.

---

# Python Naming Convention

Python commonly uses **snake_case** for variable names.

In snake_case, words are written in lowercase and separated using underscores.

### Examples

```python
student_name
total_marks
mobile_number
date_of_birth
employee_salary
```

Avoid unnecessary capital letters in normal variable names.

```python
studentName
StudentName
```

The common Python style is:

```python
student_name
```

---

# Assigning Different Values

A variable can hold different kinds of values.

```python
name = "Zeeshan"
age = 21
height = 5.8
is_student = True
```

The detailed study of these value types is covered separately in the **Data Types** topic.

---

# Printing Variables

We can use the `print()` function to display the value of a variable.

```python
name = "Zeeshan"
age = 21

print(name)
print(age)
```

Output:

```text
Zeeshan
21
```

---

# Printing Text and Variables Together

We can pass multiple values to `print()`.

```python
name = "Zeeshan"
age = 21

print("Name:", name)
print("Age:", age)
```

Output:

```text
Name: Zeeshan
Age: 21
```

---

# Using Variables in Calculations

Variables can be used in expressions and calculations.

```python
a = 10
b = 20

total = a + b

print(total)
```

Output:

```text
30
```

Another example:

```python
price = 100
quantity = 3

total = price * quantity

print(total)
```

Output:

```text
300
```

---

# Assigning the Result of an Expression

We can assign the result of an expression to a variable.

```python
a = 10
b = 20

result = a + b
```

Here:

```text
a + b → 30
```

So:

```text
result → 30
```

---

# Multiple Assignment

Python allows us to assign values to multiple variables in one line.

```python
name, age, city = "Zeeshan", 21, "Lucknow"
```

This is similar to:

```python
name = "Zeeshan"
age = 21
city = "Lucknow"
```

---

# Assigning the Same Value to Multiple Variables

We can assign the same value to multiple variables.

```python
a = b = c = 100
```

Now:

```text
a → 100
b → 100
c → 100
```

Example:

```python
x = y = z = 0

print(x)
print(y)
print(z)
```

Output:

```text
0
0
0
```

---

# Unpacking Values into Variables

Python allows us to assign multiple values to multiple variables.

```python
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

Here:

```text
a → 10
b → 20
c → 30
```

The number of variables should normally match the number of values.

---

# Swapping Variables

Python provides an easy way to swap two variables.

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

We do not need a third variable.

Without Python's multiple assignment, we may use:

```python
temp = a
a = b
b = temp
```

But Python allows the shorter method:

```python
a, b = b, a
```

---

# Checking the Type of a Variable

The `type()` function can be used to check the type of the value referred to by a variable.

```python
name = "Python"

print(type(name))
```

Output:

```text
<class 'str'>
```

Another example:

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

Detailed information about data types is covered in the **Data Types** topic.

---

# Variable and Object

In Python, a variable name refers to an object.

For example:

```python
age = 21
```

We can think of it as:

```text
age ─────► 21
```

If we do:

```python
age = 25
```

then:

```text
age ─────► 25
```

The name `age` now refers to the new value.

This is an important concept because Python variables are better understood as **names or references to objects**, rather than simple boxes containing values.

---

# Multiple Variables Can Refer to the Same Object

Two or more variables can refer to the same object.

```python
a = 100
b = a
```

Now both names refer to the value `100`.

```text
a ───► 100
b ───► 100
```

Example:

```python
a = 100
b = a

print(a)
print(b)
```

Output:

```text
100
100
```

---

# The `id()` Function

The `id()` function returns the identity of an object.

Example:

```python
a = 100

print(id(a))
```

The exact number can be different on different systems or runs.

We can compare the identity of two variables:

```python
a = 100
b = a

print(id(a))
print(id(b))
```

Both names refer to the same object in this example, so their identity is the same.

---

# Variable Reassignment and Object References

Consider:

```python
a = 10
b = a
```

Both names refer to `10`.

```text
a ───► 10
b ───► 10
```

Now:

```python
a = 20
```

The name `a` is changed to refer to `20`.

```text
a ───► 20
b ───► 10
```

Changing `a` does not automatically change `b`.

Example:

```python
a = 10
b = a

a = 20

print(a)
print(b)
```

Output:

```text
20
10
```

---

# Variables and Memory

When Python runs a program, objects are created in memory.

Variable names are used to refer to these objects.

For example:

```python
name = "Python"
```

We can think of it as:

```text
name ─────► "Python"
```

If we later write:

```python
name = "Java"
```

the name now refers to another object:

```text
name ─────► "Java"
```

Python manages memory automatically. We normally do not need to manually allocate or free memory for variables.

---

# Deleting a Variable

The `del` keyword can be used to remove a variable name.

```python
age = 21

del age
```

After this, trying to use `age` will cause an error because the name no longer exists.

```python
print(age)
```

This gives a `NameError`.

### Example

```python
name = "Zeeshan"

del name

print(name)
```

Output:

```text
NameError
```

`del` removes the name/reference. Python's memory management decides when an object can actually be removed from memory.

---

# Checking Whether a Variable Exists

Python does not provide a simple `exists()` function for variables.

Inside a normal program, we usually avoid checking this by designing the code properly.

For global names, `globals()` can be used in some situations:

```python
name = "Zeeshan"

print("name" in globals())
```

Output:

```text
True
```

This is not normally required for beginner programs.

---

# Constants in Python

Python does not have a strict constant variable system like some other languages.

However, we use **UPPERCASE names** to show that a value should not normally be changed.

Example:

```python
PI = 3.14159
MAX_USERS = 100
COMPANY_NAME = "ABC"
```

These are treated as constants by convention.

Python still allows us to change them:

```python
PI = 3.14
```

So uppercase is mainly a way to tell other programmers:

> This value is intended to remain unchanged.

---

# Local and Global Variables

Variables can have different scopes.

## Local Variable

A variable created inside a function is normally a local variable.

```python
def show_name():
    name = "Zeeshan"
    print(name)
```

Here, `name` is local to the function.

## Global Variable

A variable created outside functions is normally a global variable.

```python
name = "Zeeshan"

def show_name():
    print(name)
```

Here, `name` is defined outside the function.

Scope is covered in more detail in the **Functions** topic.

---

# Variable vs Function

A **variable** and a **function** are different things.

### Variable

A variable is a name that refers to a value/object.

```python
name = "Zeeshan"
age = 21
```

Here:

```text
name → "Zeeshan"
age  → 21
```

### Function

A function is a reusable block of code that performs a particular task.

```python
def greet():
    print("Hello")
```

Here, `greet` is the name of a function.

We can call the function:

```python
greet()
```

Output:

```text
Hello
```

### Main Difference

| Variable                  | Function                  |
| ------------------------- | ------------------------- |
| Refers to a value/object  | Represents reusable code  |
| Stores/references data    | Performs a task           |
| Example: `age = 21`       | Example: `def greet():`   |
| Used directly by its name | Usually called using `()` |

### Example Together

```python
name = "Zeeshan"

def greet():
    print("Hello", name)

greet()
```

Here:

* `name` is a variable.
* `greet` is a function.
* `greet()` calls the function.
* The function uses the variable `name`.

---

# Common Mistakes with Variables

## 1. Starting a Variable Name with a Number

```python
1name = "Zeeshan"
```

This is invalid.

Correct:

```python
name1 = "Zeeshan"
```

---

## 2. Using Spaces

```python
student name = "Zeeshan"
```

This is invalid.

Correct:

```python
student_name = "Zeeshan"
```

---

## 3. Using a Keyword

```python
class = "Python"
```

This is invalid because `class` is a Python keyword.

---

## 4. Using an Undefined Variable

```python
print(name)
```

If `name` has not been created before, Python gives a `NameError`.

Correct:

```python
name = "Zeeshan"
print(name)
```

---

## 5. Confusing `=` and `==`

`=` is used for assignment.

```python
age = 21
```

`==` is used to compare two values.

```python
age == 21
```

Example:

```python
age = 21

print(age == 21)
```

Output:

```text
True
```

---

# Best Practices for Variables

* Use meaningful variable names.
* Follow the `snake_case` naming style.
* Use lowercase names for normal variables.
* Use uppercase names for constants by convention.
* Avoid unnecessary single-letter names.
* Do not use Python keywords as variable names.
* Keep variable names clear and easy to understand.
* Avoid very long and confusing variable names.
* Use names that describe the purpose of the value.

### Good Examples

```python
student_name = "Zeeshan"
total_marks = 450
mobile_number = 9876543210
employee_salary = 50000
date_of_birth = "01-01-2000"
```

### Avoid

```python
a = "Zeeshan"
x = 450
abc = 9876543210
temp1 = 50000
```

These names do not clearly explain what the values represent.

---

# Quick Examples

### Basic Variable

```python
name = "Zeeshan"
```

### Multiple Variables

```python
name = "Zeeshan"
age = 21
city = "Lucknow"
```

### Multiple Assignment

```python
a, b, c = 10, 20, 30
```

### Same Value

```python
a = b = c = 100
```

### Reassignment

```python
age = 21
age = 22
```

### Calculation

```python
price = 100
quantity = 5

total = price * quantity
```

### Swapping

```python
a = 10
b = 20

a, b = b, a
```

### Checking Type

```python
value = 100

print(type(value))
```

### Checking Object Identity

```python
value = 100

print(id(value))
```

### Deleting a Variable

```python
name = "Zeeshan"

del name
```

---

# Important Points to Remember

* A variable is a name that refers to an object/value.
* Variables are created using assignment.
* The `=` operator is used for assignment.
* Python does not require variable declarations.
* Python is dynamically typed.
* A variable can be reassigned.
* Variable names are case-sensitive.
* Variable names cannot start with a number.
* Spaces and hyphens are not allowed in variable names.
* Python keywords cannot be used as variable names.
* Multiple variables can be assigned in one line.
* The same value can be assigned to multiple variables.
* Python supports unpacking values into variables.
* Python allows easy swapping of variables.
* `type()` can be used to check the type of the value.
* `id()` can be used to check the identity of an object.
* `del` can remove a variable name.
* Uppercase names are commonly used for constants by convention.
* Variables and functions are different concepts.

---

# Summary

In this topic, I learned:

* What a variable is
* How variables work in Python
* Creating variables
* Variable assignment
* Reassigning variables
* Dynamic typing
* Variable names and values
* Variable naming rules
* Valid and invalid variable names
* Python naming conventions
* Meaningful variable names
* Printing variables
* Using variables in calculations
* Multiple assignment
* Assigning the same value to multiple variables
* Unpacking values
* Swapping variables
* Variables and objects
* Multiple variables referring to the same object
* The `id()` function
* Variables and memory
* Deleting variables using `del`
* Constants in Python
* Local and global variables
* Difference between a variable and a function
* Common mistakes with variables
* Best practices for naming variables

---
