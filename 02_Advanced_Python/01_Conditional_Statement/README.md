# Python Conditional Statements

Conditional statements are used to make decisions in a Python program.

They allow the program to execute different blocks of code depending on whether a condition is `True` or `False`.

## Introduction

A condition is an expression that gives either:

* `True`
* `False`

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

Python mainly provides these conditional statements:

* `if`
* `if-else`
* `if-elif-else`
* Nested `if`
* Conditional expression (ternary operator)
* `match-case` for pattern matching

---

## if Statement

The `if` statement executes a block of code only when the given condition is `True`.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```text
You are eligible to vote.
```

### Important Point

Python uses indentation to define the block of code inside an `if` statement.

```python
if age >= 18:
print("Eligible")
```

This gives an `IndentationError`.

Correct:

```python
if age >= 18:
    print("Eligible")
```

---

## if-else Statement

The `if-else` statement is used when there are two possible outcomes.

* If the condition is `True`, the `if` block executes.
* If the condition is `False`, the `else` block executes.

### Syntax

```python
if condition:
    # code when condition is True
else:
    # code when condition is False
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
```

Output:

```text
Not eligible to vote.
```

---

## if-elif-else Statement

The `if-elif-else` statement is used when there are multiple conditions.

* `if` checks the first condition.
* `elif` checks another condition if the previous condition was `False`.
* `else` executes when all conditions are `False`.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

Output:

```text
Grade B
```

### Important Point

Python checks conditions from top to bottom.

As soon as one condition becomes `True`, its block executes and the remaining `elif` and `else` blocks are skipped.

---

## Multiple Conditions

We can combine multiple conditions using logical operators.

### Using `and`

Both conditions must be `True`.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
```

Output:

```text
Entry allowed.
```

### Using `or`

At least one condition must be `True`.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

Output:

```text
Weekend
```

### Using `not`

`not` reverses the Boolean result.

```python
is_raining = False

if not is_raining:
    print("You can go outside.")
```

Output:

```text
You can go outside.
```

---

## Nested if Statement

A nested `if` means using one `if` statement inside another `if` statement.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID is required.")
else:
    print("You are under 18.")
```

Output:

```text
Entry allowed.
```

### Important Point

Nested conditions are useful when one condition depends on another condition.

However, too many nested `if` statements can make code difficult to understand. In such cases, logical operators can sometimes make the code simpler.

---

## Comparing Values in Conditions

Conditional statements commonly use comparison operators.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 21

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

---

## Using Boolean Values

Conditions can directly use Boolean values.

```python
is_logged_in = True

if is_logged_in:
    print("Welcome!")
```

Output:

```text
Welcome!
```

---

## Truthy and Falsy Values

Python treats some values as `False` when used in a condition.

Common falsy values include:

* `False`
* `None`
* `0`
* `0.0`
* `""`
* `[]`
* `()`
* `{}`
* `set()`

Most other values are considered truthy.

### Example

```python
name = ""

if name:
    print("Name is available.")
else:
    print("Name is empty.")
```

Output:

```text
Name is empty.
```

---

## Checking Multiple Values

The `in` operator can be used to check whether a value exists inside a sequence or collection.

### Example

```python
day = "Sunday"

if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")
```

Output:

```text
Weekend
```

---

## Conditional Expression

A conditional expression allows us to write a simple `if-else` in a single line.

It is also called the **ternary operator**.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)
```

Output:

```text
Adult
```

### Another Example

```python
a = 10
b = 20

greater = a if a > b else b

print(greater)
```

Output:

```text
20
```

Use conditional expressions mainly for simple conditions. For complex logic, a normal `if-else` statement is easier to read.

---

## match-case Statement

`match-case` is used for pattern matching.

It is available in **Python 3.10 and later**.

### Syntax

```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default code
```

### Example

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```

Output:

```text
Tuesday
```

The `_` acts as a default case.

### When to Use `match-case`

`match-case` can be useful when the same value needs to be compared against several possible patterns.

For simple conditions involving ranges or comparisons, `if-elif-else` is usually more suitable.

---

## `pass` in Conditional Statements

`pass` is used when a block is required syntactically but we do not want to execute any code yet.

### Example

```python
age = 20

if age >= 18:
    pass
else:
    print("Minor")
```

Output:

```text
```

`pass` does nothing. It is mainly useful as a placeholder while writing or planning code.

---

## Conditions with User Input

Conditional statements are commonly used with `input()`.

Remember that `input()` returns a string by default.

### Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

Example output:

```text
Enter your age: 21
You are eligible to vote.
```

---

## Conditions with Strings

String values can also be compared in conditions.

```python
password = "python123"

if password == "python123":
    print("Correct password.")
else:
    print("Incorrect password.")
```

Output:

```text
Correct password.
```

---

## Conditions with Numbers

Numbers can be checked using comparison operators.

```python
number = 10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

Output:

```text
Positive number
```

---

## Nested Conditions vs Logical Operators

Sometimes nested `if` statements can be replaced with logical operators.

### Nested version

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
```

### Using `and`

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
```

Output:

```text
Entry allowed.
```

Both approaches can work, but the second one is simpler when the conditions are closely related.

---

## Common Mistakes

### Using `=` instead of `==`

Incorrect:

```python
if age = 18:
    print("18")
```

Correct:

```python
if age == 18:
    print("18")
```

`=` is used for assignment, while `==` is used for comparison.

---

### Forgetting the colon

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

### Incorrect indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

### Comparing Different Data Types

```python
age = input("Enter your age: ")

if age >= 18:
    print("Adult")
```

This causes a `TypeError` because `input()` returns a string.

Correct:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
```

---

## Difference Between Conditional Statements

| Statement              | Use                                      |
| ---------------------- | ---------------------------------------- |
| `if`                   | Execute code when a condition is true    |
| `if-else`              | Choose between two possibilities         |
| `if-elif-else`         | Choose between multiple conditions       |
| Nested `if`            | Put one condition inside another         |
| Conditional expression | Write a simple `if-else` in one line     |
| `match-case`           | Match a value against different patterns |

---

## Basic Structure to Remember

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

Only `if` is required.

`elif` and `else` are optional.

A statement can contain multiple `elif` blocks, but only one `else` block can be present, and it must come at the end.

---

## Key Points

* Conditional statements are used for decision-making.
* A condition produces `True` or `False`.
* Python uses indentation to define code blocks.
* `if` checks a condition.
* `else` handles the alternative case.
* `elif` allows multiple conditions.
* Multiple conditions can be combined using `and`, `or`, and `not`.
* `in` can be used to check membership.
* Nested `if` means an `if` statement inside another `if`.
* A conditional expression is a short form of `if-else`.
* `match-case` is available from Python 3.10.
* `pass` can be used as a placeholder.
* `input()` returns a string, so type conversion may be required before numerical comparison.
* Conditions are checked from top to bottom in an `if-elif-else` structure.