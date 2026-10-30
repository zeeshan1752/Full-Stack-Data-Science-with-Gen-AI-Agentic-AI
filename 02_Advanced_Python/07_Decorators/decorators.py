# Decorators in Python

# 1. A simple function

def greet():
    print("Hello!")


greet()

# 2. A function that accepts another function

def say_hello():
    print("Hello from the original function!")


def call_function(func):
    func()


call_function(say_hello)

# 3. A basic decorator

def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper


@my_decorator
def greet_user():
    print("Hello, user!")


greet_user()

# 4. Decorator without the @ syntax

def welcome():
    print("Welcome!")


welcome = my_decorator(welcome)
welcome()

# 5. Decorator for a function with arguments

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(3, 4))

# 6. Decorator that returns a value

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_result
def get_message():
    return "learning python"


print(get_message())

# 7. Preserve function metadata with functools.wraps
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

# 8. Decorator with its own argument

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

# 9. Timing a function
import time


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


print(calculate_sum(100_000))

# 10. Stack multiple decorators

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

# 11. Practical example: check a positive number

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

# Uncomment to test the validation error:
# print(square_root_input(-5))
