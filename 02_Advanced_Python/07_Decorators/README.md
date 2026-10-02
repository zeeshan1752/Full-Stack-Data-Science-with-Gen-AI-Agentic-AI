# Decorators in Python

A **decorator** is a function that takes another function, adds some behaviour to it, and returns a function. Decorators let us add reusable behaviour without changing the original function's code.

## 1. Why use decorators?

Decorators are useful for logging, measuring execution time, checking permissions or inputs, and repeating a function call.

## 2. A basic decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
```

Output:

```text
Before the function
Hello!
After the function
```

`@my_decorator` is shorthand for `greet = my_decorator(greet)`.

## 3. Decorator without the `@` syntax

```python
def decorate(func):
    def wrapper():
        print("Starting")
        func()
    return wrapper

def greet():
    print("Hello")

greet = decorate(greet)
greet()
```

Output:

```text
Starting
Hello
```

## 4. Decorators with function arguments

Use `*args` and `**kwargs` in the wrapper when the decorated function may receive positional or keyword arguments.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 4))
```

Output:

```text
Calling add
7
```

Returning `func(*args, **kwargs)` preserves the original function's return value.

## 5. Changing a return value

```python
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def message():
    return "learning python"

print(message())
```

Output:

```text
LEARNING PYTHON
```

This example expects the original function to return a string, because strings provide the `.upper()` method.

## 6. Preserve metadata with `functools.wraps`

Without `@wraps(func)`, attributes such as the function's name and docstring may refer to the wrapper instead of the original function.

```python
from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running function...")
        return func(*args, **kwargs)
    return wrapper

@announce
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(4, 5))
print(multiply.__name__)
print(multiply.__doc__)
```

Output:

```text
Running function...
20
multiply
Return the product of two numbers.
```

## 7. Decorators that accept arguments

A decorator with its own arguments needs an outer function that receives those arguments and returns the actual decorator.

```python
from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
```

Output:

```text
Hi!
Hi!
Hi!
```

This version repeats calls but returns `None`. If the repeated function returns useful values, decide explicitly how those results should be collected and returned.

## 8. Measure execution time

```python
import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Execution time: {elapsed:.6f} seconds")
        return result
    return wrapper

@measure_time
def calculate_sum(limit):
    return sum(range(limit))

print(calculate_sum(10))
```

Example output (the timing varies by computer):

```text
Execution time: 0.000001 seconds
45
```

The measured time is illustrative and will differ between runs and devices.

## 9. Stack multiple decorators

Decorators are applied from the closest decorator to the function outward.

```python
from functools import wraps

def exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

def make_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@exclamation
@make_uppercase
def greeting():
    return "hello"

print(greeting())
```

Output:

```text
HELLO!
```

## 10. Input validation example

```python
from functools import wraps

def require_positive(func):
    @wraps(func)
    def wrapper(number):
        if number <= 0:
            raise ValueError("Number must be positive")
        return func(number)
    return wrapper

@require_positive
def square_root_input(number):
    return number ** 0.5

print(square_root_input(25))
```

Output:

```text
5.0
```

Calling `square_root_input(-5)` raises `ValueError: Number must be positive`.

## 11. Important points

- A decorator receives a function and usually returns a wrapper function.
- Use `@decorator_name` above the function definition to apply a decorator.
- Use `*args` and `**kwargs` to support different arguments.
- Return the wrapped function's result when it should remain available to the caller.
- Use `functools.wraps` to preserve metadata such as `__name__` and `__doc__`.
- A decorator with parameters commonly uses three nested functions: the argument-taking function, the decorator, and the wrapper.
- The wrapper runs when the decorated function is called; the decorator itself is applied when the function is defined.

## 12. Practice questions

1. Create a decorator that prints `Function started` before calling a function.
2. Create a decorator that prints the name of the function being called.
3. Create a decorator that converts a returned string to lowercase.
4. Create a decorator that repeats a function a user-specified number of times.
5. Create a decorator that rejects negative numbers.
6. Apply two decorators to one function and observe the order.
