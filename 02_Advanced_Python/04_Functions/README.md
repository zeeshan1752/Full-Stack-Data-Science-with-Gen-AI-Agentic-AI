# Functions

A function is a block of reusable code that performs a specific task.

Functions help us:

* Avoid repeating the same code.
* Make programs easier to understand.
* Make code easier to test and debug.
* Divide a large program into smaller parts.

## 1. Defining a Function

A function is defined using the `def` keyword.

### Example

```python
def greet():
    print("Hello")
```

Here:

* `def` is used to define a function.
* `greet` is the function name.
* `()` contains parameters, if any.
* The indented code is the function body.

The function does not execute when it is only defined.

We need to call it.

```python
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
```

## 2. Calling a Function

Calling a function means executing the code inside the function.

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output:

```text
Welcome to Python
```

If we call a function that does not exist:

```python
welcome_user()
```

Error:

```text
NameError: name 'welcome_user' is not defined
```

The error occurs because Python cannot find a function named `welcome_user`.

## 3. Function Syntax

Basic syntax:

```python
def function_name(parameters):
    # function body
    statements
```

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

The colon `:` is required after the function definition.

Incorrect:

```python
def add(a, b)
    print(a + b)
```

Error:

```text
SyntaxError: expected ':'
```

## 4. Function with No Arguments

A function does not always need arguments.

```python
def message():
    print("Learning Python")

message()
```

Output:

```text
Learning Python
```

## 5. Function with Arguments

Arguments allow us to send data to a function.

```python
def greet(name):
    print("Hello", name)

greet("Zee")
```

Output:

```text
Hello Zee
```

If the required argument is not provided:

```python
def greet(name):
    print("Hello", name)

greet()
```

Error:

```text
TypeError: greet() missing 1 required positional argument: 'name'
```

The function requires `name`, but no value was passed.

## 6. Function with Return Value

A function can return a value using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The returned value can be stored in a variable.

### `print()` vs `return`

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

`print()` displays the value but does not return it.

With `return`:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

## 7. `return` Statement

`return` sends a value back to the place where the function was called.

```python
def square(number):
    return number * number

answer = square(5)

print(answer)
```

Output:

```text
25
```

A function can return multiple values.

```python
def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)
```

Output:

```text
15
5
50
```

## 8. Actual Arguments and Formal Parameters

The variables written inside the function definition are called **formal parameters**.

The actual values passed while calling the function are called **actual arguments**.

```python
def add(a, b):
    print(a + b)
```

Here:

```text
a and b → Formal Parameters
```

When we call:

```python
add(10, 20)
```

Here:

```text
10 and 20 → Actual Arguments
```

Complete example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

## 9. Types of Arguments

Python supports different ways of passing arguments to functions.

The main types are:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments (`*args`)
5. Keyword Variable-Length Arguments (`**kwargs`)

## 10. Positional Arguments

In positional arguments, values are passed according to their position.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Zee", 22)
```

Output:

```text
Name: Zee
Age: 22
```

Here:

```text
"Zee" → name
22     → age
```

The position decides which parameter receives the value.

### Changing the position

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(22, "Zee")
```

Output:

```text
Name: 22
Age: Zee
```

Python does not automatically understand that `22` should be the age. It assigns values according to position.

### Too many positional arguments

```python
def student(name, age):
    print(name, age)

student("Zee", 22, "CSE")
```

Error:

```text
TypeError: student() takes 2 positional arguments but 3 were given
```

The function accepts only two parameters, but three arguments were provided.

### Missing positional argument

```python
def student(name, age):
    print(name, age)

student("Zee")
```

Error:

```text
TypeError: student() missing 1 required positional argument: 'age'
```

## 11. Keyword Arguments

In keyword arguments, we explicitly specify the parameter name.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Zee")
```

Output:

```text
Name: Zee
Age: 22
```

The order does not matter when keyword arguments are used.

```python
student(name="Zee", age=22)
```

and:

```python
student(age=22, name="Zee")
```

Both produce the same result.

### Incorrect keyword name

```python
def student(name, age):
    print(name, age)

student(username="Zee", age=22)
```

Error:

```text
TypeError: student() got an unexpected keyword argument 'username'
```

The function has a parameter named `name`, not `username`.

### Mixing positional and keyword arguments

This is valid:

```python
def student(name, age):
    print(name, age)

student("Zee", age=22)
```

Output:

```text
Zee 22
```

But this is invalid:

```python
student(name="Zee", 22)
```

Error:

```text
SyntaxError: positional argument follows keyword argument
```

Once a keyword argument is used, a positional argument cannot come after it.

## 12. Default Arguments

A default argument has a default value.

```python
def greet(name="User"):
    print("Hello", name)

greet()
```

Output:

```text
Hello User
```

If we provide a value, the default value is replaced.

```python
greet("Zee")
```

Output:

```text
Hello Zee
```

### Example

```python
def student(name, course="CSE"):
    print("Name:", name)
    print("Course:", course)

student("Zee")
```

Output:

```text
Name: Zee
Course: CSE
```

We can also provide another course:

```python
student("Zee", "Data Science")
```

Output:

```text
Name: Zee
Course: Data Science
```

### Error with default and non-default parameters

Incorrect:

```python
def student(course="CSE", name):
    print(course, name)
```

Error:

```text
SyntaxError: non-default argument follows default argument
```

A parameter without a default value must come before a parameter with a default value.

Correct:

```python
def student(name, course="CSE"):
    print(name, course)
```

## 13. Variable-Length Arguments - `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def add(*args):
    print(args)

add(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

Inside the function, `args` is a tuple.

### Example

```python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30, 40))
```

Output:

```text
30
100
```

The name does not have to be `args`.

```python
def add(*numbers):
    print(numbers)
```

`*args` means:

```text
Multiple positional arguments → tuple
```

### Passing a list with `*`

```python
numbers = [10, 20, 30]

def add(*args):
    print(args)

add(*numbers)
```

Output:

```text
(10, 20, 30)
```

Here `*numbers` unpacks the list and passes its elements as separate positional arguments.

## 14. Keyword Variable-Length Arguments - `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def student(**details):
    print(details)

student(name="Zee", age=22, course="CSE")
```

Output:

```text
{'name': 'Zee', 'age': 22, 'course': 'CSE'}
```

Inside the function, `kwargs` is a dictionary.

### Example

```python
def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Zee", age=22, course="CSE")
```

Output:

```text
name : Zee
age : 22
course : CSE
```

`**kwargs` means:

```text
Multiple keyword arguments → dictionary
```

### Passing a dictionary with `**`

```python
details = {
    "name": "Zee",
    "age": 22
}

def student(**kwargs):
    print(kwargs)

student(**details)
```

Output:

```text
{'name': 'Zee', 'age': 22}
```

### Wrong use of `**kwargs`

```python
def student(**kwargs):
    print(kwargs)

student("Zee")
```

Error:

```text
TypeError: student() takes 0 positional arguments but 1 was given
```

`**kwargs` accepts keyword arguments, not normal positional arguments.

## 15. `*args` vs `**kwargs`

| Feature   | `*args`              | `**kwargs`        |
| --------- | -------------------- | ----------------- |
| Accepts   | Positional arguments | Keyword arguments |
| Stored as | Tuple                | Dictionary        |
| Example   | `fun(10, 20)`        | `fun(a=10, b=20)` |
| Symbol    | `*`                  | `**`              |

Example:

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, name="Zee", age=22)
```

Output:

```text
(10, 20)
{'name': 'Zee', 'age': 22}
```

## 16. Scope of Variables

The **scope** of a variable means the part of the program where that variable can be accessed.

Python mainly follows the **LEGB rule** when looking for a variable.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches in this order:

```text
Local → Enclosing → Global → Built-in
```

## 17. Local Scope

A variable created inside a function is normally a local variable.

```python
def test():
    x = 10
    print(x)

test()
```

Output:

```text
10
```

`x` exists inside the function.

Trying to access it outside:

```python
def test():
    x = 10

test()

print(x)
```

Error:

```text
NameError: name 'x' is not defined
```

The variable `x` has local scope.

## 18. Global Scope

A variable created outside a function has global scope.

```python
x = 10

def test():
    print(x)

test()
```

Output:

```text
10
```

The function can read the global variable.

### Local variable with the same name

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Output:

```text
20
10
```

The `x` inside the function is a different local variable.

## 19. `global` Keyword

The `global` keyword allows us to modify a global variable from inside a function.

```python
count = 10

def change():
    global count
    count = 20

change()

print(count)
```

Output:

```text
20
```

Without `global`:

```python
count = 10

def change():
    count = 20

change()

print(count)
```

Output:

```text
10
```

Here, `count = 20` creates a new local variable instead of changing the global variable.

### Error when modifying a global variable incorrectly

```python
count = 10

def change():
    print(count)
    count = 20

change()
```

Error:

```text
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

Python treats `count` as local because it is assigned inside the function.

Correct:

```python
count = 10

def change():
    global count
    print(count)
    count = 20

change()
```

## 20. `globals()` Function

`globals()` returns a dictionary containing the current global symbol table.

Example:

```python
name = "Zee"
age = 22

print(globals()["name"])
print(globals()["age"])
```

Output:

```text
Zee
22
```

We can also modify a global variable through the dictionary.

```python
x = 10

globals()["x"] = 50

print(x)
```

Output:

```text
50
```

`globals()` and `global` are different:

```text
global  → keyword
globals() → built-in function
```

## 21. Local vs Global Variables

```python
x = 100

def test():
    y = 200
    print(x)
    print(y)

test()
```

Output:

```text
100
200
```

Here:

```text
x → Global variable
y → Local variable
```

`x` can be accessed outside the function.

`y` cannot normally be accessed outside the function.

## 22. Enclosing Scope

An enclosing variable exists in an outer function when another function is defined inside it.

```python
def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()
```

Output:

```text
10
```

Here `x` is not local to `inner()`, but it exists in the enclosing `outer()` function.

## 23. `nonlocal` Keyword

The `nonlocal` keyword is used to modify a variable from an enclosing function.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
```

Output:

```text
20
```

Without `nonlocal`, assigning `x` inside `inner()` would create a new local variable.

## 24. Built-in Scope

Python already provides many built-in names.

Examples:

```python
print()
len()
sum()
max()
min()
type()
int()
str()
list()
```

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

These names are available without defining them ourselves.

## 25. Pass by Value and Pass by Reference

In some programming languages, arguments are described as being passed by value or passed by reference.

Python is better described as using **object reference / call by sharing**.

The function receives a reference to the same object.

The result depends on whether the object is mutable or immutable.

## 26. Immutable Objects

Examples of immutable objects:

```text
int
float
str
tuple
bool
```

Example:

```python
def change_value(x):
    x = x + 10
    print("Inside:", x)

num = 20

change_value(num)

print("Outside:", num)
```

Output:

```text
Inside: 30
Outside: 20
```

The original integer does not change because integers are immutable.

The assignment:

```python
x = x + 10
```

creates a new integer object and makes `x` refer to it.

## 27. Mutable Objects

Examples of mutable objects:

```text
list
dict
set
```

Example:

```python
def add_item(items):
    items.append(40)

numbers = [10, 20, 30]

add_item(numbers)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

The list changed because lists are mutable.

The function and the outside variable refer to the same list object.

## 28. Mutable vs Immutable

### Immutable example

```python
def change(x):
    x = 50

number = 10

change(number)

print(number)
```

Output:

```text
10
```

### Mutable example

```python
def change(items):
    items.append(50)

numbers = [10, 20]

change(numbers)

print(numbers)
```

Output:

```text
[10, 20, 50]
```

The important point is:

```text
Python does not simply behave as "pass by value"
or
"pass by reference".

Python passes object references to functions.
```

Whether the original object appears to change depends on whether the object is mutable and whether the function mutates it.

## 29. Nested Functions

A function defined inside another function is called a nested function.

```python
def outer():

    def inner():
        print("Inside inner function")

    inner()

outer()
```

Output:

```text
Inside inner function
```

The `inner()` function is defined inside `outer()`.

## 30. Recursion

A function calling itself is called recursion.

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

The condition:

```python
if n == 0:
    return
```

is important because it stops the recursion.

Without a stopping condition:

```python
def test():
    test()

test()
```

Python keeps calling the function until it reaches the recursion limit.

Error:

```text
RecursionError: maximum recursion depth exceeded
```

## 31. Function with Multiple Types of Arguments

A function can use different argument types together.

```python
def student(name, age=18, *subjects, **details):
    print("Name:", name)
    print("Age:", age)
    print("Subjects:", subjects)
    print("Details:", details)

student(
    "Zee",
    22,
    "Python",
    "SQL",
    city="Lucknow",
    course="CSE"
)
```

Output:

```text
Name: Zee
Age: 22
Subjects: ('Python', 'SQL')
Details: {'city': 'Lucknow', 'course': 'CSE'}
```

This combines:

```text
name       → normal parameter
age        → default parameter
*subjects  → variable-length positional arguments
**details  → variable-length keyword arguments
```

## 32. Common Function Mistakes

### Forgetting the colon

Incorrect:

```python
def greet()
    print("Hello")
```

Error:

```text
SyntaxError: expected ':'
```

Correct:

```python
def greet():
    print("Hello")
```

### Forgetting parentheses while calling

Defining:

```python
def greet():
    print("Hello")
```

Writing:

```python
greet
```

does not call the function.

Correct:

```python
greet()
```

### Wrong number of arguments

```python
def add(a, b):
    return a + b

add(10)
```

Error:

```text
TypeError: add() missing 1 required positional argument: 'b'
```

### Too many arguments

```python
def add(a, b):
    return a + b

add(10, 20, 30)
```

Error:

```text
TypeError: add() takes 2 positional arguments but 3 were given
```

### Wrong keyword

```python
def student(name, age):
    print(name, age)

student(username="Zee", age=22)
```

Error:

```text
TypeError: student() got an unexpected keyword argument 'username'
```

### Using a local variable outside its scope

```python
def test():
    value = 100

test()

print(value)
```

Error:

```text
NameError: name 'value' is not defined
```

### Using a variable before assigning it

```python
def test():
    print(value)
    value = 10

test()
```

Error:

```text
UnboundLocalError: cannot access local variable 'value' where it is not associated with a value
```

## 33. Function Practice Examples

### Example 1: Check Even or Odd

```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))
```

Output:

```text
Even
Odd
```

### Example 2: Find Maximum

```python
def find_max(a, b):
    if a > b:
        return a
    return b

print(find_max(10, 20))
```

Output:

```text
20
```

### Example 3: Calculate Factorial

```python
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
```

Output:

```text
120
```

### Example 4: Sum Using `*args`

```python
def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result

print(total(10, 20))
print(total(10, 20, 30, 40))
```

Output:

```text
30
100
```

### Example 5: Student Details Using `**kwargs`

```python
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(
    name="Zee",
    age=22,
    course="CSE"
)
```

Output:

```text
name : Zee
age : 22
course : CSE
```



## 35. Keyword-Only Parameters

A keyword-only parameter must be passed using its parameter name. Put it after `*` or after `*args` in the function definition.

```python
def show_profile(name, *, city):
    print("Name:", name)
    print("City:", city)

show_profile("Zee", city="Hyderabad")
```

Output:

```text
Name: Zee
City: Hyderabad
```

Calling `show_profile("Zee", "Hyderabad")` would raise a `TypeError` because `city` is keyword-only.

## 36. Functions Are Objects

In Python, a function can be assigned to another variable. The variable can then be used to call the same function.

```python
def greet():
    print("Hello")

hello = greet
hello()
```

Output:

```text
Hello
```

Notice that `greet` is assigned without parentheses. Writing `greet()` would call the function immediately and assign its return value instead.

## 37. Passing a Function as an Argument

A function can receive another function as an argument. This is useful when we want to reuse an operation.

```python
def square(number):
    return number * number

def apply_function(function, value):
    return function(value)

print(apply_function(square, 5))
```

Output:

```text
25
```

## 38. Returning a Function

A function can return another function. The returned function can be stored in a variable and called later.

```python
def make_greeter():
    def greet():
        return "Hello from the returned function"

    return greet

greeter = make_greeter()
print(greeter())
```

Output:

```text
Hello from the returned function
```

## 39. Function Docstrings

A docstring is a string written as the first statement inside a function. It describes the function and can be accessed using `function_name.__doc__`.

```python
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(4, 5))
print(multiply.__doc__)
```

Output:

```text
20
Return the product of two numbers.
```

## 40. Finding a Maximum with `*args`

This example accepts any number of values. It returns `None` when no values are provided.

```python
def find_maximum(*numbers):
    if not numbers:
        return None

    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number

    return maximum

print(find_maximum(10, 50, 20, 80, 30))
print(find_maximum())
```

Output:

```text
80
None
```

# Python Functions — Points to Remember

## 1. Function Basics

| Term | Meaning |
|---|---|
| `def` | Used to define a function. |
| `()` | Used to define parameters or call a function. |
| `return` | Sends a value back from a function. |
| **Docstring** | Describes what a function does. |

## 2. Arguments and Parameters

| Term | Meaning |
|---|---|
| **Actual Arguments** | Values passed during a function call. |
| **Formal Parameters** | Variables that receive values in a function definition. |
| **Positional Arguments** | Values matched according to their position. |
| **Keyword Arguments** | Values matched using parameter names. |
| **Default Arguments** | Parameters that have default values. |
| **Keyword-only Parameter** | A parameter that must be passed using its parameter name. |
| `*args` | Accepts multiple positional arguments and stores them as a tuple. |
| `**kwargs` | Accepts multiple keyword arguments and stores them as a dictionary. |

## 3. Variables and Scope

| Term | Meaning |
|---|---|
| **Local Variable** | Available within its local scope. |
| **Global Variable** | Defined outside functions. |
| `global` | Used to modify a global variable inside a function. |
| `globals()` | Returns the global symbol table as a dictionary. |
| `nonlocal` | Used to modify a variable from an enclosing scope. |
| **LEGB Rule** | The order Python follows when looking up a name: Local → Enclosing → Global → Built-in. |

## 4. Other Important Concepts

| Term | Meaning |
|---|---|
| **Mutable** | Can be changed after creation. |
| **Immutable** | Cannot be changed after creation. |
| **Recursion** | A function calling itself. |
| **Function as an Object** | A function can be assigned to a variable, passed as an argument, or returned from another function. |

## Quick Revision

- `def` → Define a function
- `return` → Return a value
- `*args` → Multiple positional arguments (tuple)
- `**kwargs` → Multiple keyword arguments (dictionary)
- `global` → Refer to or modify a global variable
- `nonlocal` → Refer to or modify a variable in an enclosing scope
- `globals()` → Access the global symbol table
- `LEGB` → Local → Enclosing → Global → Built-in
- Recursion → A function calling itself
- Docstring → Describe a function
