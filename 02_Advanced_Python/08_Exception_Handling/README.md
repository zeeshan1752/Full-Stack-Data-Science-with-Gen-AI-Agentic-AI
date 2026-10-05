# Exception Handling in Python

Exception handling is used to handle errors that occur while a Python program is running. Instead of allowing the program to stop suddenly, we can detect the exception and respond to it properly.

## 1. What is an Error?

An error is a problem in a program that prevents the program from working as expected.

There are three common categories:

### Syntax / Compiler Error

A syntax error happens when Python code does not follow the correct syntax.

```python
print("Hello"
```

Output:

```text
SyntaxError: '(' was never closed
```

The program cannot start until the syntax is corrected.

### Logical Error

A logical error happens when the program runs, but the logic or calculation is wrong.

```python
a = 10
b = 5

result = a - b
print(result)
```

Output:

```text
5
```

If the intention was to add the numbers, the program runs without an error, but the result is logically wrong.

### Runtime Error

A runtime error occurs while the program is running.

```python
a = 10
b = 0

print(a / b)
```

Output:

```text
ZeroDivisionError: division by zero
```

Runtime errors are commonly handled using exception handling.

---

## 2. What is an Exception?

An exception is an event that occurs during program execution and interrupts the normal flow of the program.

Examples:

- Dividing by zero
- Entering text where an integer is expected
- Accessing an invalid list index
- Accessing a dictionary key that does not exist
- Opening a file that does not exist

Example:

```python
num = int("abc")
```

Output:

```text
ValueError: invalid literal for int()
```

---

## 3. Error vs Exception

| Error | Exception |
|---|---|
| General problem in a program | An event raised during execution |
| Can include syntax and logical problems | Usually refers to runtime problems |
| Logical errors may not raise an exception | Exceptions can often be handled |
| Example: wrong formula | Example: ZeroDivisionError |

---

## 4. Why is Exception Handling Required?

Without exception handling:

```python
num = int(input("Enter a number: "))
print(10 / num)

print("Program completed")
```

If the user enters `0`, the program stops before reaching the last line.

With exception handling:

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program completed")
```

Output when input is `0`:

```text
Cannot divide by zero
Program completed
```

Exception handling allows the program to respond to unexpected situations gracefully.

---

# 5. try Block

The `try` block contains code that may cause an exception.

```python
try:
    result = 10 / 0
```

An exception should normally be handled using an `except` block.

---

# 6. except Block

The `except` block handles an exception.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

# 7. Basic try-except

```python
try:
    num = int(input("Enter a number: "))
    print("Number:", num)
except ValueError:
    print("Please enter a valid integer")
```

Input:

```text
abc
```

Output:

```text
Please enter a valid integer
```

The program does not terminate with a traceback.

---

# 8. except Exception as e

A very common pattern is:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except Exception as e:
    print("An error occurred:", e)
```

Here:

- `Exception` is the base class for most normal exceptions.
- `as e` stores the exception object in the variable `e`.
- `e` can be printed to see the actual error message.

Input:

```text
0
```

Output:

```text
An error occurred: division by zero
```

Another example:

```python
try:
    num = int("hello")
except Exception as e:
    print("Error:", e)
```

Output:

```text
Error: invalid literal for int() with base 10: 'hello'
```

### Why use `as e`?

It helps us inspect the actual exception message.

```python
except Exception as e:
    print(type(e))
    print(e)
```

---

# 9. `except:` vs `except Exception:` vs `except Exception as e`

### Catch everything

```python
try:
    ...
except:
    print("Something went wrong")
```

This is broad and usually not preferred because it can also catch exceptions such as `KeyboardInterrupt`.

### Catch normal application exceptions

```python
try:
    ...
except Exception:
    print("Something went wrong")
```

### Catch and inspect the error

```python
try:
    ...
except Exception as e:
    print("Error:", e)
```

For debugging and learning, `except Exception as e` is very useful.

For production code, catching a specific exception is usually better when you know what can happen.

---

# 10. Catching Specific Exceptions

Instead of catching every exception, catch the expected exception.

```python
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")
```

Input:

```text
abc
```

Output:

```text
Please enter a valid number
```

Input:

```text
0
```

Output:

```text
Number cannot be zero
```

---

# 11. Multiple except Blocks

A single `try` block can have multiple `except` blocks.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ValueError:
    print("Please enter integers only")

except ZeroDivisionError:
    print("Second number cannot be zero")
```

Only the matching exception handler is executed.

---

# 12. else Block

The `else` block runs only when the `try` block completes without an exception.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", num)
```

Input:

```text
25
```

Output:

```text
Valid number: 25
```

If the input is invalid, `else` does not execute.

---

# 13. finally Block

The `finally` block executes whether an exception occurs or not.

```python
try:
    print("Opening resource")
    result = 10 / 0
except ZeroDivisionError:
    print("An error occurred")
finally:
    print("Closing resource")
```

Output:

```text
Opening resource
An error occurred
Closing resource
```

`finally` is commonly used for cleanup operations.

Examples:

- Closing a file
- Closing a database connection
- Releasing a resource
- Cleaning temporary data

---

# 14. try-except-else-finally

All four blocks can be used together.

```python
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
```

Input:

```text
10
```

Output:

```text
Result: 10.0
Program execution completed
```

Input:

```text
0
```

Output:

```text
Number cannot be zero
Program execution completed
```

---

# 15. Common Built-in Exceptions

## ZeroDivisionError

Occurs when dividing by zero.

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError: division by zero
```

## ValueError

Occurs when a function receives a value of the correct type but an invalid value.

```python
int("abc")
```

Output:

```text
ValueError
```

## TypeError

Occurs when an operation is performed on incompatible types.

```python
print("10" + 5)
```

Output:

```text
TypeError
```

## NameError

Occurs when a variable or name is not defined.

```python
print(age)
```

Output:

```text
NameError
```

## IndexError

Occurs when an invalid list index is accessed.

```python
numbers = [10, 20, 30]
print(numbers[5])
```

Output:

```text
IndexError
```

## KeyError

Occurs when a dictionary key does not exist.

```python
student = {"name": "Zee"}
print(student["age"])
```

Output:

```text
KeyError
```

## FileNotFoundError

Occurs when a requested file does not exist.

```python
file = open("abc.txt")
```

Output:

```text
FileNotFoundError
```

## AttributeError

Occurs when an object does not have the requested attribute or method.

```python
number = 10
number.append(20)
```

Output:

```text
AttributeError
```

---

# 16. Raising Exceptions with `raise`

The `raise` keyword is used to manually raise an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```text
ValueError: Age cannot be negative
```

Another example:

```python
marks = 150

if marks > 100:
    raise ValueError("Marks cannot be greater than 100")
```

`raise` is useful when we want to enforce our own rules.

---

# 17. Custom Exceptions

We can create our own exception classes.

```python
class InvalidAgeError(Exception):
    pass
```

Use it:

```python
age = 15

if age < 18:
    raise InvalidAgeError("Age must be 18 or above")
```

Output:

```text
InvalidAgeError: Age must be 18 or above
```

Custom exceptions are useful in larger applications where normal built-in exceptions are not descriptive enough.

---

# 18. Exception Hierarchy

Python exceptions are organized in a hierarchy.

```text
BaseException
│
├── SystemExit
├── KeyboardInterrupt
│
└── Exception
    │
    ├── ArithmeticError
    │   └── ZeroDivisionError
    │
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── IndexError
    ├── KeyError
    ├── FileNotFoundError
    └── AttributeError
```

Most application-level exceptions inherit from `Exception`.

---

# 19. File Handling Example

Without handling:

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

If `data.txt` does not exist:

```text
FileNotFoundError
```

Using exception handling:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("File not found:", e)
finally:
    print("File operation completed")
```

---

# 20. Database Example

Exception handling is especially useful with databases.

A typical database workflow is:

```text
Open database connection
        ↓
Perform database operation
        ↓
If error → handle exception
        ↓
Close database connection
```

Example structure:

```python
connection = None

try:
    print("Connecting to database")

    # Database operations
    print("Executing query")

except Exception as e:
    print("Database error:", e)

finally:
    if connection is not None:
        connection.close()
    print("Database connection closed")
```

Why `finally`?

Even if a database query fails, the connection or other resources should be cleaned up.

---

# 21. Practical Example: User Input

```python
while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        break

    except ValueError as e:
        print("Invalid input:", e)
```

Input:

```text
hello
```

Output:

```text
Invalid input: invalid literal for int() with base 10: 'hello'
```

Input:

```text
25
```

Output:

```text
You entered: 25
```

---

# 22. Best Practices

1. Catch specific exceptions whenever possible.
2. Use `as e` when you need the exception message.
3. Keep the `try` block focused and small.
4. Use `finally` for cleanup operations.
5. Use `else` for code that should run only when no exception occurs.
6. Do not silently ignore exceptions.
7. Give meaningful error messages.
8. Use `raise` when invalid data should be rejected.
9. Use custom exceptions for application-specific errors.
10. Do not use a broad `except` when a specific exception can be handled.

---

# 23. Common Mistakes

### Mistake 1: Empty except block

```python
try:
    x = 10 / 0
except:
    pass
```

This hides the error and makes debugging difficult.

### Mistake 2: Catching everything unnecessarily

```python
try:
    important_operation()
except Exception:
    pass
```

The program may continue, but the actual problem is hidden.

### Mistake 3: Putting too much code inside try

Avoid:

```python
try:
    # 100 lines of code
    ...
except Exception as e:
    ...
```

Keep the risky operation focused.

### Mistake 4: Using the wrong exception

If you know the operation can raise `ValueError`, handle `ValueError` instead of blindly catching everything.

---

# 24. Points to Remember

- `try` → contains code that may cause an exception.
- `except` → handles the exception.
- `except Exception as e` → catches a normal exception and stores it in `e`.
- `else` → runs when no exception occurs.
- `finally` → runs whether an exception occurs or not.
- `raise` → manually raises an exception.
- Custom exceptions → allow us to create application-specific errors.
- Exception handling prevents unexpected program termination.
- Specific exception handling is preferred over a generic `except`.
- `finally` is useful for cleanup such as closing files and database connections.
- Logical errors usually do not raise Python exceptions.
- Syntax errors must be fixed before normal execution can begin.

---

# 25. Quick Syntax Reference

```python
try:
    # risky code

except SpecificException as e:
    # handle error

else:
    # runs when no exception occurs

finally:
    # cleanup
```

Not every block is mandatory.

Common combinations:

```python
try:
    ...
except:
    ...
```

```python
try:
    ...
except:
    ...
finally:
    ...
```

```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

---

# Summary

Exception handling allows Python programs to handle unexpected situations in a controlled way.

The most important concepts are:

```text
try
  ↓
Run risky code
  ↓
Exception?
  ├── Yes → except
  └── No  → else
  ↓
finally
  ↓
Cleanup / continue program
```

The main syntax to remember is:

```python
try:
    risky_code()

except Exception as e:
    print("Error:", e)

else:
    print("No error occurred")

finally:
    print("Cleanup completed")
```
