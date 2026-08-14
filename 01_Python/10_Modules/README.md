# Python Modules

## Function vs Module vs Package vs Framework

Before learning the `math` module, it is important to understand four basic terms:

* Function
* Module
* Package
* Framework

These terms are related to how Python code is written, organized, reused, and used to build applications.

---

# 1. Function

## What is a Function?

A **function** is a block of reusable code that is created to perform a specific task.

Instead of writing the same code again and again, we can put that code inside a function and call the function whenever we need it.

### Example

```python
def add(a, b):
    return a + b

print(add(10, 5))
print(add(20, 30))
```

Output:

```text
15
50
```

Here:

```text
add() → Function
a, b  → Parameters
10, 5 → Arguments
return → Sends the result back
```

The same function can be used multiple times with different values.

### Another Example

Python already provides many built-in functions:

```python
print("Hello")
input("Enter your name: ")
len("Python")
```

Here:

* `print()` → Function
* `input()` → Function
* `len()` → Function

A function mainly focuses on **performing a particular task**.

---

# 2. Module

## What is a Module?

A **module** is a Python file containing reusable Python code.

A module normally has a `.py` extension.

A module can contain:

* Functions
* Variables
* Classes
* Statements

For example:

```text
calculator.py
```

can contain:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Now another Python file can use these functions by importing the module.

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

Here:

```text
calculator.py → Module
add()          → Function
subtract()     → Function
```

So, a module can contain **multiple functions and other reusable code**.

---

## Why Do We Use Modules?

Modules help us:

* Organize code
* Reuse code
* Avoid writing the same code again
* Divide a large program into smaller files
* Make code easier to maintain

Instead of having one huge Python file:

```text
big_program.py
```

we can divide the code into different modules:

```text
calculator.py
user.py
database.py
validation.py
```

Each module can handle a different part of the program.

---

# 3. Package

## What is a Package?

A **package** is used to organize related Python modules together.

Think of it as a folder that contains related Python modules.

For example:

```text
calculator/
│
├── __init__.py
├── basic.py
├── scientific.py
└── conversion.py
```

Here:

```text
calculator → Package
basic.py → Module
scientific.py → Module
conversion.py → Module
```

The modules inside the package can contain functions.

For example:

```text
Package
   ↓
Modules
   ↓
Functions
```

A package is useful when a project contains many related modules.

---

## Example

Suppose we create a package called `calculator`.

```text
calculator/
│
├── __init__.py
├── addition.py
└── subtraction.py
```

`addition.py`:

```python
def add(a, b):
    return a + b
```

`subtraction.py`:

```python
def subtract(a, b):
    return a - b
```

We can use these modules from the package in another program.

```python
from calculator.addition import add

print(add(10, 5))
```

Output:

```text
15
```

---

# 4. Framework

## What is a Framework?

A **framework** is a larger software structure that provides tools, rules, and a basic structure for building applications.

A framework helps developers build applications without creating everything from the beginning.

For example, if we want to build a web application, we don't necessarily have to create everything ourselves.

A web framework can provide things like:

* URL handling
* Request and response handling
* Database support
* Authentication
* Application structure
* Security features

### Examples of Python Frameworks

**Django**

Used for building web applications.

**Flask**

A lightweight web framework for Python.

**FastAPI**

Commonly used for building APIs and modern web applications.

---

# Function vs Module vs Package vs Framework

| Concept       | What is it?                                   | Main purpose                | Example  |
| ------------- | --------------------------------------------- | --------------------------- | -------- |
| **Function**  | Reusable block of code                        | Perform a specific task     | `sqrt()` |
| **Module**    | Python `.py` file containing reusable code    | Organize and reuse code     | `math`   |
| **Package**   | Collection/organization of related modules    | Organize larger codebases   | `numpy`  |
| **Framework** | Structure and tools for building applications | Build complete applications | Django   |

### Simple Example to Understand

Imagine you are building a house:

```text
Function
   ↓
One specific task

Module
   ↓
A file containing related code

Package
   ↓
A collection of related modules

Framework
   ↓
A complete structure for building an application
```

> These are different concepts. They are not strict levels where every framework contains packages, every package contains modules, and every module contains functions. This is only a simple way to understand their general purpose.

---

# Math Module

Now we will look at one of Python's built-in modules: the **`math` module**.

## What is the Math Module?

The `math` module is a **built-in Python module** that provides mathematical functions and constants.

Python already provides this module, so we don't need to install it separately.

We only need to import it before using it.

```python
import math
```

---

# Why Do We Use `import`?

Python does not automatically make every module available in our program.

The `import` statement tells Python:

> "I want to use this module in my program."

For example:

```python
import math
```

Now Python makes the `math` module available to our program.

We can use its functions:

```python
print(math.sqrt(25))
```

Output:

```text
5.0
```

### Without `import`

If we try:

```python
print(math.sqrt(25))
```

without importing `math`, Python does not know what `math` is.

So we first write:

```python
import math
```

and then use:

```python
math.sqrt(25)
```

---

# Understanding `math.sqrt()`

Look at this:

```python
math.sqrt(25)
```

It has two important parts:

```text
math.sqrt(25)
│    │
│    └── Function
│
└─────── Module
```

So:

```text
math → Module
sqrt → Function
25   → Argument
```

The `sqrt()` function belongs to the `math` module.

---

# Functions in the Math Module

The `math` module contains **many mathematical functions and constants**.

We will not learn all of them now.

For now, we will focus on four basic functions:

1. `sqrt()`
2. `pow()`
3. `floor()`
4. `ceil()`

Some other functions available in the `math` module are:

```text
factorial()
gcd()
lcm()
sin()
cos()
tan()
log()
exp()
```

We will study other functions later when they are required.

---

# 1. `sqrt()`

## What is `sqrt()`?

`sqrt()` is used to find the **square root** of a number.

### Example

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

Because:

```text
√25 = 5
```

Another example:

```python
print(math.sqrt(16))
print(math.sqrt(100))
print(math.sqrt(49))
```

Output:

```text
4.0
10.0
7.0
```

---

# 2. `pow()`

## What is `pow()`?

`pow()` is used to calculate the **power** of a number.

It takes two main values:

```text
pow(base, exponent)
```

### Example

```python
import math

print(math.pow(2, 3))
```

Output:

```text
8.0
```

Because:

```text
2³ = 2 × 2 × 2 = 8
```

Another example:

```python
print(math.pow(5, 2))
```

Output:

```text
25.0
```

Because:

```text
5² = 25
```

---

# 3. `floor()`

## What is `floor()`?

`floor()` returns the **largest integer that is less than or equal to the given number**.

In simple words:

> `floor()` moves the value downward.

### Example

```python
import math

print(math.floor(4.8))
```

Output:

```text
4
```

Another example:

```python
print(math.floor(7.9))
print(math.floor(7.1))
print(math.floor(7.0))
```

Output:

```text
7
7
7
```

### Important

`floor()` is not simply "remove the decimal."

For negative numbers:

```python
print(math.floor(-4.2))
```

Output:

```text
-5
```

Because `-5` is the largest integer that is less than or equal to `-4.2`.

---

# 4. `ceil()`

## What is `ceil()`?

`ceil()` returns the **smallest integer that is greater than or equal to the given number**.

In simple words:

> `ceil()` moves the value upward.

### Example

```python
import math

print(math.ceil(4.2))
```

Output:

```text
5
```

Another example:

```python
print(math.ceil(7.1))
print(math.ceil(7.9))
print(math.ceil(7.0))
```

Output:

```text
8
8
7
```

For negative numbers:

```python
print(math.ceil(-4.2))
```

Output:

```text
-4
```

---

# `floor()` vs `ceil()`

| Function  | Meaning        |      Example | Result |
| --------- | -------------- | -----------: | -----: |
| `floor()` | Moves downward | `floor(4.8)` |    `4` |
| `ceil()`  | Moves upward   |  `ceil(4.2)` |    `5` |

Simple way to remember:

```text
floor → ↓
ceil  → ↑
```

---

# Different Ways to Import the Math Module

Python provides different ways to import code from a module.

We will learn four common forms:

```python
import math
```

```python
import math as m
```

```python
from math import sqrt
```

```python
from math import *
```

---

# 1. `import math`

This imports the `math` module.

```python
import math
```

We then access its functions using:

```text
module.function()
```

### Example

```python
import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.floor(4.8))
print(math.ceil(4.2))
```

Here we use:

```text
math.sqrt()
math.pow()
math.floor()
math.ceil()
```

This is one of the clearest and most commonly recommended ways to use a module.

---

# 2. `import math as m`

## What is `as`?

`as` is used to give a **different name or alias** to an imported module.

Example:

```python
import math as m
```

Here:

```text
math → Original module name
m    → Alias
```

Now instead of writing:

```python
math.sqrt(25)
```

we can write:

```python
m.sqrt(25)
```

### Example

```python
import math as m

print(m.sqrt(25))
print(m.pow(2, 3))
print(m.floor(4.8))
print(m.ceil(4.2))
```

The output is the same.

The only difference is that we are using `m` as the name of the module.

---

# 3. `from math import`

`from ... import ...` allows us to import **specific functions or objects** from a module.

### Example

```python
from math import sqrt
```

Now we can directly use:

```python
print(sqrt(25))
```

We don't need:

```python
math.sqrt(25)
```

because `sqrt` itself has been imported.

### Multiple Functions

We can import multiple functions:

```python
from math import sqrt, pow, floor, ceil

print(sqrt(25))
print(pow(2, 3))
print(floor(4.8))
print(ceil(4.2))
```

---

# 4. `from math import *`

The `*` means **all available names** from the module.

```python
from math import *
```

Now we can directly use functions from the `math` module.

### Example

```python
from math import *

print(sqrt(25))
print(pow(2, 3))
print(floor(4.8))
print(ceil(4.2))
```

We don't need to write:

```python
math.sqrt()
math.pow()
```

because the names have been imported directly.

### Important Note

Although this syntax works, it is generally **not recommended in larger programs**.

For example:

```python
from math import *
```

can make it difficult to know where a particular function came from.

For normal code, these are usually clearer:

```python
import math
```

or:

```python
from math import sqrt
```

---

# Import Methods Comparison

| Syntax                  | What happens                 | How we use `sqrt()` |
| ----------------------- | ---------------------------- | ------------------- |
| `import math`           | Imports the module           | `math.sqrt(25)`     |
| `import math as m`      | Imports module with an alias | `m.sqrt(25)`        |
| `from math import sqrt` | Imports only `sqrt()`        | `sqrt(25)`          |
| `from math import *`    | Imports all available names  | `sqrt(25)`          |

---

# Overall Structure

You can understand everything we learned like this:

```text
Python
│
├── Function
│   └── Performs a specific task
│
├── Module
│   └── Contains reusable code
│
├── Package
│   └── Organizes related modules
│
└── Framework
    └── Provides structure for building applications
```

And for the `math` module:

```text
math
│
├── sqrt()
├── pow()
├── floor()
├── ceil()
│
└── Many other functions
    ├── factorial()
    ├── gcd()
    ├── lcm()
    ├── sin()
    ├── cos()
    ├── tan()
    └── ...
```

---

# Key Points

* A **function** performs a specific task.
* A **module** is a Python file containing reusable code.
* A **package** organizes related modules.
* A **framework** provides a structure for building applications.
* `math` is a built-in Python module.
* We use `import` to make a module available in our program.
* `as` is used to create an alias for an imported module.
* `from ... import ...` allows us to import specific items.
* `from math import *` imports all available names from the module.
* `sqrt()` finds the square root.
* `pow()` calculates a power.
* `floor()` moves a value downward to the nearest integer.
* `ceil()` moves a value upward to the nearest integer.
* The `math` module has many more functions that we can learn later.