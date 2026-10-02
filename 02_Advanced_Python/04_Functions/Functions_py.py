# Functions

# Defining and calling a function
def greet():
    print("Hello, welcome to Python")

greet()


# Function syntax
def add(a, b):
    print(a + b)

add(10, 20)


# Function with no arguments
def message():
    print("Learning Python functions")

message()


# Function with arguments
def greet_user(name):
    print("Hello", name)

greet_user("Zee")


# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)


# return statement
def square(number):
    return number * number

answer = square(5)
print(answer)


# print vs return
def add_using_print(a, b):
    print(a + b)

result = add_using_print(10, 20)
print(result)


def add_using_return(a, b):
    return a + b

result = add_using_return(10, 20)
print(result)


# Actual arguments and formal parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Zee", 22)

# name and age -> formal parameters
# "Zee" and 22 -> actual arguments


# Positional arguments
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Zee", 22)

# Error example:
# student_info("Zee")
# TypeError: student_info() missing 1 required positional argument: 'age'

# Error example:
# student_info("Zee", 22, "CSE")
# TypeError: student_info() takes 2 positional arguments but 3 were given


# Keyword arguments
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)

student_details(age=22, name="Zee")

# Error example:
# student_details(username="Zee", age=22)
# TypeError: student_details() got an unexpected keyword argument 'username'

# Error example:
# student_details(name="Zee", 22)
# SyntaxError: positional argument follows keyword argument


# Default arguments
def greet_with_default(name="User"):
    print("Hello", name)

greet_with_default()
greet_with_default("Zee")


def student_course(name, course="CSE"):
    print("Name:", name)
    print("Course:", course)

student_course("Zee")
student_course("Zee", "Data Science")

# Error example:
# def invalid_default(course="CSE", name):
#     print(course, name)
# SyntaxError: non-default argument follows default argument


# Variable-length arguments - *args
def add_many(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_many(10, 20))
print(add_many(10, 20, 30, 40))


def show_args(*args):
    print(args)
    print(type(args))

show_args(10, 20, 30)


# Unpacking with *args
numbers = [10, 20, 30]

def show_numbers(*args):
    print(args)

show_numbers(*numbers)


# Keyword variable-length arguments - **kwargs
def show_details(**details):
    print(details)

show_details(name="Zee", age=22, course="CSE")


def print_details(**details):
    for key, value in details.items():
        print(key, ":", value)

print_details(name="Zee", age=22, course="CSE")


# Unpacking with **kwargs
details = {
    "name": "Zee",
    "age": 22
}

def student_kwargs(**kwargs):
    print(kwargs)

student_kwargs(**details)


# *args vs **kwargs
def example(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example(10, 20, name="Zee", age=22)

# Error example:
# def only_kwargs(**kwargs):
#     print(kwargs)
#
# only_kwargs("Zee")
# TypeError: only_kwargs() takes 0 positional arguments but 1 was given


# Combining different argument types
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


# Local scope
def local_example():
    value = 100
    print(value)

local_example()

# Error example:
# print(value)
# NameError: name 'value' is not defined


# Global scope
x = 10

def global_read():
    print(x)

global_read()
print(x)


# Local and global variables with the same name
x = 10

def local_global_example():
    x = 20
    print("Inside:", x)

local_global_example()
print("Outside:", x)


# global keyword
count = 10

def change_count():
    global count
    count = 20

change_count()
print(count)


# Error example without global
count = 10

def wrong_change():
    count = 20

wrong_change()
print(count)


# global keyword error
number = 10

def wrong_global_usage():
    # print(number)
    # number = 20
    pass

# If the print and assignment above are uncommented together:
# UnboundLocalError: cannot access local variable 'number'
# where it is not associated with a value


# globals() function
name = "Zee"
age = 22

print(globals()["name"])
print(globals()["age"])


# Modifying a global variable using globals()
score = 10

globals()["score"] = 50

print(score)


# Scope of variables - LEGB
value = "global"

def outer():
    value = "enclosing"

    def inner():
        value = "local"
        print(value)

    inner()

outer()


# Enclosing scope
def outer_function():
    message = "Hello from outer"

    def inner_function():
        print(message)

    inner_function()

outer_function()


# nonlocal keyword
def outer_function():
    value = 10

    def inner_function():
        nonlocal value
        value = 20

    inner_function()
    print(value)

outer_function()


# Built-in scope
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(max(numbers))


# Pass by object reference with immutable object
def change_number(number):
    number = number + 10
    print("Inside:", number)

number = 20

change_number(number)

print("Outside:", number)


# Pass by object reference with mutable object
def add_item(items):
    items.append(40)

numbers = [10, 20, 30]

add_item(numbers)

print(numbers)


# Mutable vs immutable
def change_immutable(value):
    value = 50

number = 10

change_immutable(number)

print(number)


def change_mutable(items):
    items.append(50)

numbers = [10, 20]

change_mutable(numbers)

print(numbers)


# Nested functions
def outer():
    def inner():
        print("Inside inner function")

    inner()

outer()


# Recursion from a function
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)


# Common function errors

# Missing argument:
# def add(a, b):
#     return a + b
#
# add(10)
# TypeError: add() missing 1 required positional argument: 'b'


# Too many arguments:
# add(10, 20, 30)
# TypeError: add() takes 2 positional arguments but 3 were given


# Unexpected keyword:
# add(first=10, second=20)
# TypeError: add() got an unexpected keyword argument 'first'


# NameError:
# unknown_function()
# NameError: name 'unknown_function' is not defined


# Function with multiple return values
def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)


# Practical example - even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))


# Practical example - find maximum
def find_max(a, b):
    if a > b:
        return a

    return b

print(find_max(10, 20))


# Practical example - factorial using a function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))


# Practical example - sum using *args
def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result

print(total(10, 20))
print(total(10, 20, 30, 40))


# Practical example - student details using **kwargs
def student_details_practical(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details_practical(
    name="Zee",
    age=22,
    course="CSE"
)

# Keyword-only parameters
def show_profile(name, *, city):
    print("Name:", name)
    print("City:", city)

show_profile("Zee", city="Hyderabad")


# Function as an object
def say_hello():
    print("Hello from a function object")

hello = say_hello
hello()


# Passing a function as an argument
def square(number):
    return number * number

def apply_function(function, value):
    return function(value)

print(apply_function(square, 5))


# Returning a function
def make_greeter():
    def greet():
        return "Hello from the returned function"

    return greet

greeter = make_greeter()
print(greeter())


# Function docstring
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(4, 5))
print(multiply.__doc__)


# Practical example - maximum using *args
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
