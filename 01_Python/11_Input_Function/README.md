# Python Strings & String Manipulation

Strings are used to store and work with **text** in Python.

---

## 1. Creating a String

A string is a sequence of characters written inside single or double quotes.

```python
name = "Zeeshan"
city = 'Lucknow'

print(name)
print(city)
```

Both of these are valid:

```python
"Hello"
'Hello'
```

---

## 2. String Indexing

Each character in a string has an **index**.

The index starts from `0`.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[5])
```

Output:

```text
P
y
n
```

### Negative Indexing

Negative indexes start from the end.

```python
text = "Python"

print(text[-1])
print(text[-2])
```

Output:

```text
n
o
```

### Index Positions

```text
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

---

# 3. String Slicing

Slicing is used to extract a part of a string.

### Syntax

```python
string[start:end]
```

The `end` index is **not included**.

```python
text = "Python"

print(text[0:3])
print(text[2:5])
```

Output:

```text
Pyt
tho
```

### Using Step

```python
text = "Python"

print(text[0:6:2])
```

Output:

```text
Pto
```

### Reverse a String

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

# 4. Finding the Length of a String

The `len()` function returns the number of characters.

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Spaces are also counted.

```python
text = "Hello World"

print(len(text))
```

Output:

```text
11
```

---

# 5. String Concatenation

Concatenation means joining strings using `+`.

```python
first_name = "Zeeshan"
last_name = "Khan"

name = first_name + " " + last_name

print(name)
```

Output:

```text
Zeeshan Khan
```

---

# 6. String Repetition

The `*` operator can repeat a string.

```python
text = "Python "

print(text * 3)
```

Output:

```text
Python Python Python
```

---

# 7. Membership Operators

We can check whether a character or word exists in a string.

### `in`

```python
text = "Python"

print("P" in text)
print("Java" in text)
```

Output:

```text
True
False
```

### `not in`

```python
text = "Python"

print("Java" not in text)
```

Output:

```text
True
```

---

# 8. Changing String Case

### `upper()`

Converts the string to uppercase.

```python
text = "hello"

print(text.upper())
```

Output:

```text
HELLO
```

### `lower()`

Converts the string to lowercase.

```python
text = "HELLO"

print(text.lower())
```

Output:

```text
hello
```

### `capitalize()`

Converts the first character to uppercase.

```python
text = "hello world"

print(text.capitalize())
```

Output:

```text
Hello world
```

### `title()`

Capitalizes the first character of each word.

```python
text = "hello world"

print(text.title())
```

Output:

```text
Hello World
```

### `swapcase()`

Changes uppercase characters to lowercase and lowercase characters to uppercase.

```python
text = "Hello World"

print(text.swapcase())
```

Output:

```text
hELLO wORLD
```

### `isupper()`

Checks whether all alphabetic characters in the string are uppercase.

Returns `True` or `False`.

```python
text = "HELLO"
print(text.isupper())
```

Output:

```text
True
```

### `islower()`

Checks whether all alphabetic characters in the string are lowercase.

Returns `True` or `False`.

```python
text = "hello"
print(text.islower())
```

Output:

```text
True
```

---

# 9. Removing Spaces

### `strip()`

Removes spaces from both sides.

```python
text = "  Hello  "

print(text.strip())
```

Output:

```text
Hello
```

### `lstrip()`

Removes spaces from the left side.

```python
text = "  Hello"

print(text.lstrip())
```

### `rstrip()`

Removes spaces from the right side.

```python
text = "Hello  "

print(text.rstrip())
```

---

# 10. Replacing Text

The `replace()` method replaces one part of a string with another.

### Syntax

```python
string.replace(old, new)
```

Example:

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

We can also specify the number of replacements.

```python
text = "apple apple apple"

print(text.replace("apple", "mango", 2))
```

Output:

```text
mango mango apple
```

---

# 11. Searching in a String

### `find()`

Returns the index of the first occurrence.

```python
text = "Hello World"

print(text.find("World"))
```

Output:

```text
6
```

If the text is not found, `find()` returns `-1`.

```python
print(text.find("Python"))
```

Output:

```text
-1
```

### `index()`

Also returns the position of the text.

```python
text = "Hello World"

print(text.index("World"))
```

**Difference:**

```text
find()  → returns -1 if not found
index() → gives an error if not found
```

---

# 12. Counting Characters or Words

The `count()` method counts how many times something appears.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

Example:

```python
text = "hello hello"

print(text.count("hello"))
```

Output:

```text
2
```

---

# 13. Checking the Beginning and Ending

### `startswith()`

Checks whether a string starts with specific text.

```python
text = "Python Programming"

print(text.startswith("Python"))
```

Output:

```text
True
```

### `endswith()`

Checks whether a string ends with specific text.

```python
text = "Python Programming"

print(text.endswith("Programming"))
```

Output:

```text
True
```

---

# 14. Checking String Content

### `isalpha()`

Checks whether all characters are alphabets.

```python
text = "Python"

print(text.isalpha())
```

Output:

```text
True
```

### `isdigit()`

Checks whether all characters are digits.

```python
text = "12345"

print(text.isdigit())
```

Output:

```text
True
```

### `isalnum()`

Checks whether all characters are alphabets or numbers.

```python
text = "Python123"

print(text.isalnum())
```

Output:

```text
True
```

### `isspace()`

Checks whether all characters are whitespace.

```python
text = "   "

print(text.isspace())
```

Output:

```text
True
```

---

# 15. Splitting a String

The `split()` method divides a string into parts and returns a **list**.

```python
text = "Python is easy"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

By default, `split()` separates values using whitespace.

### Splitting Using a Specific Character

```python
text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

---

# 16. Joining Strings

The `join()` method joins elements into a single string.

```python
words = ["Python", "is", "easy"]

text = " ".join(words)

print(text)
```

Output:

```text
Python is easy
```

Another example:

```python
words = ["Python", "Java", "C++"]

text = ", ".join(words)

print(text)
```

Output:

```text
Python, Java, C++
```

### Remember

```text
split() → String → List

join()  → List → String
```

---

# 17. Escape Characters

Escape characters are used to represent special characters.

### New Line `\n`

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab `\t`

```python
print("Hello\tWorld")
```

### Single Quote `\'`

```python
print('It\'s Python')
```

### Double Quote `\"`

```python
print("He said \"Hello\"")
```

---

# 18. f-Strings

f-strings are used to insert variables into strings.

```python
name = "Zeeshan"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Zeeshan and I am 21 years old.
```

---

# 19. String Immutability

Strings are **immutable**.

This means we cannot directly change an individual character.

❌ Incorrect:

```python
name = "Python"

name[0] = "J"
```

Instead, create a new string.

```python
name = "Python"

name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

String methods also return a **new string**.

```python
text = "hello"

new_text = text.upper()

print(text)
print(new_text)
```

Output:

```text
hello
HELLO
```

---

# 20. Taking String Input

The `input()` function is used to take input from the user during program execution. 

### Basic Syntax

```python
input()
```

Example:

```python
name = input()

print(name)
```

### Input with a Prompt

We can display a message inside `input()`.

```python
name = input("Enter your name: ")

print(name)
```

The message inside `input()` is called the **prompt**. 

---

# 21. Important: `input()` Returns a String

By default, `input()` always returns the user's input as a **string**. 

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
21
```

Python receives:

```python
"21"
```

not:

```python
21
```

This is important when working with numbers.

---

# 22. Type Conversion with `input()`

If we need a number, we can convert the input.

### Integer

```python
age = int(input("Enter your age: "))
```

### Float

```python
price = float(input("Enter the price: "))
```

The basic pattern is:

```text
input()        → string
int(input())   → integer
float(input()) → float
```



---

# 23. Input for Mathematical Operations

If we take numbers directly using `input()`, they are strings.

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Because Python is doing:

```python
"10" + "20"
```

which is string concatenation.

### Correct Way

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Output:

```text
30
```



---

# 24. Taking Multiple Inputs

### Separate Inputs

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

This is the simplest approach.

### Multiple Values in One Line

Use `split()`:

```python
a, b = input("Enter two values: ").split()
```

If the user enters:

```text
10 20
```

then:

```python
a = "10"
b = "20"
```

Both are strings.

### Multiple Integer Inputs

Use `map()` with `split()`:

```python
a, b = map(int, input("Enter two numbers: ").split())
```

Now:

```python
a = 10
b = 20
```



---

# 25. `input()` with `split()`

`split()` is especially useful when taking multiple values from the user.

```python
data = input("Enter your name and city: ").split()

print(data)
```

Input:

```text
Zeeshan Hyderabad
```

Output:

```text
['Zeeshan', 'Hyderabad']
```

---

# 26. `input()` with `map()`

`map()` applies a conversion function to multiple values.

```python
a, b, c = map(int, input("Enter three numbers: ").split())

print(a)
print(b)
print(c)
```

Input:

```text
10 20 30
```

Output:

```text
10
20
30
```

Here:

```python
map(int, ...)
```

converts each input value into an integer. 

---

# 27. Boolean Input

`input()` does not automatically convert text into `True` or `False`.

```python
value = input("Enter True or False: ")

print(type(value))
```

If the user enters:

```text
True
```

the value is:

```python
"True"
```

which is still a string.

### Important

Do not normally use:

```python
value = bool(input())
```

For example:

```python
bool("False")
```

returns:

```text
True
```

because any non-empty string is considered `True`. 

---

# 28. Common String Methods — Quick Reference

| Method         | Purpose                         |
| -------------- | ------------------------------- |
| `upper()`      | Converts to uppercase           |
| `lower()`      | Converts to lowercase           |
| `capitalize()` | Capitalizes first character     |
| `title()`      | Capitalizes each word           |
| `swapcase()`   | Changes uppercase ↔ lowercase   |
| `strip()`      | Removes spaces from both sides  |
| `lstrip()`     | Removes left-side spaces        |
| `rstrip()`     | Removes right-side spaces       |
| `replace()`    | Replaces text                   |
| `find()`       | Finds position of text          |
| `index()`      | Finds position; error if absent |
| `count()`      | Counts occurrences              |
| `startswith()` | Checks beginning                |
| `endswith()`   | Checks ending                   |
| `split()`      | Converts string into a list     |
| `join()`       | Joins elements into a string    |
| `isalpha()`    | Checks alphabets                |
| `isdigit()`    | Checks digits                   |
| `isalnum()`    | Checks alphabets/numbers        |
| `isspace()`    | Checks whitespace               |

---

# 29. Important Functions Used with Input

| Function  | Purpose                               | Example                     |
| --------- | ------------------------------------- | --------------------------- |
| `input()` | Takes input as string                 | `input()`                   |
| `int()`   | Converts to integer                   | `int(input())`              |
| `float()` | Converts to float                     | `float(input())`            |
| `str()`   | Converts to string                    | `str(value)`                |
| `split()` | Splits input                          | `input().split()`           |
| `map()`   | Applies conversion to multiple values | `map(int, input().split())` |



---

# 30. Quick Revision

### String Basics

```python
text = "Python"

text[0]       # Indexing
text[0:3]     # Slicing
text[::-1]    # Reverse
len(text)     # Length
```

### String Operations

```python
"Hello" + " World"   # Concatenation
"Hi " * 3            # Repetition
"Py" in "Python"     # Membership
```

### Case Methods

| Method | Purpose |
|---|---|
| `upper()` | Converts to uppercase |
| `lower()` | Converts to lowercase |
| `capitalize()` | Capitalizes first character |
| `title()` | Capitalizes each word |
| `swapcase()` | Swaps uppercase and lowercase |
| `isupper()` | Checks if string is uppercase |
| `islower()` | Checks if string is lowercase |

---
### Input

```python
name = input("Enter name: ")

age = int(input("Enter age: "))

price = float(input("Enter price: "))

a, b = input().split()

x, y = map(int, input().split())
```

---

# 31. Main Rules to Remember

```text
String → sequence of characters

Index → starts from 0

Negative index → starts from -1

Slicing → [start:end]

len() → returns number of characters

Strings → immutable

input() → always returns a string

int(input()) → integer input

float(input()) → decimal input

split() → string to list

join() → list/sequence to string

map() → applies a function to multiple values
```
