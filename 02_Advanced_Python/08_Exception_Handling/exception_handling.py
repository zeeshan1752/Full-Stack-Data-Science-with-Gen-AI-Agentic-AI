# Exception Handling in Python

# Basic try-except
try:
    num = int(input("Enter a number: "))
    print("Number:", num)
except ValueError:
    print("Please enter a valid integer")


# Handling ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Exception as e
try:
    num = int("hello")
except Exception as e:
    print("Error:", e)


# Multiple except blocks
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter integers only")
except ZeroDivisionError:
    print("Second number cannot be zero")


# else block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", num)


# finally block
try:
    print("Opening resource")
    result = 10 / 0
except ZeroDivisionError:
    print("An error occurred")
finally:
    print("Closing resource")


# try-except-else-finally
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Number cannot be zero")
else:
    print("Result:", result)
finally:
    print("Program execution completed")


# Common exceptions
examples = [
    "ZeroDivisionError: 10 / 0",
    "ValueError: int('abc')",
    "TypeError: '10' + 5",
    "NameError: print(unknown_variable)",
    "IndexError: [10, 20][5]",
    "KeyError: {'name': 'Zee'}['age']",
]

for example in examples:
    print(example)


# File handling
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("File not found:", e)
finally:
    print("File operation completed")


# raise
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Custom validation error:", e)


# Custom exception
class InvalidAgeError(Exception):
    pass


try:
    age = 15
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
except InvalidAgeError as e:
    print("Custom exception:", e)


# Database-style example
connection = None

try:
    print("Connecting to database")
    print("Executing query")
except Exception as e:
    print("Database error:", e)
finally:
    if connection is not None:
        connection.close()
    print("Database connection closed")
