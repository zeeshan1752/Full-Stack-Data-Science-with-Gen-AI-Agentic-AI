# Python Strings

## What is a String?

A string is a collection of characters written inside quotes.

In Python, we can create strings using:

- Single quotes: `'Hello'`
- Double quotes: `"Hello"`
- Triple single quotes: `'''Hello'''`
- Triple double quotes: `"""Hello"""`

```python
name = "Zeeshan"
message = 'Hello Python'
```

---

## String Declaration

### 1. Syntax

```python
variable_name = "value"
```

### 2. Example

```python
name = "Zeeshan"
course = "Python"
city = "Lucknow"

print(name)
print(course)
print(city)
```

**Output:**

```text
Zeeshan
Python
Lucknow
```

### 3. Checking the Data Type

We can use `type()` to check the data type of a string.

```python
name = "Zeeshan"

print(type(name))
```

**Output:**

```text
<class 'str'>
```

---

## Types of Quotes

### 1. Single Quotes

```python
name = 'Zeeshan'
```

### 2. Double Quotes

```python
name = "Zeeshan"
```

Both are commonly used for single-line strings.

### 3. Triple Quotes

Triple quotes are mainly used for multiline strings.

They can be written using:

- `''' '''`
- `""" """`

```python
message = """Hello
My name is Zeeshan
I am learning Python"""

print(message)
```

**Output:**

```text
Hello
My name is Zeeshan
I am learning Python
```

Triple quotes can also be used for a single line:

```python
message = """Hello Python"""
```

---

## Escape Characters

Escape characters are used to represent special characters inside a string.

They start with a backslash (`\`).

| Escape Character | Meaning |
|---|---|
| `\'` | Single quote |
| `\"` | Double quote |
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\b` | Backspace |
| `\r` | Carriage return |
| `\ooo` | Octal value |

### 1. New Line

```python
print("Hello\nWorld")
```

**Output:**

```text
Hello
World
```

### 2. Tab

```python
print("Name\tAge")
```

**Output:**

```text
Name    Age
```

---

## Raw Strings

A raw string treats backslashes as normal characters.

We use `r` before the string.

### 1. Example

```python
path = r"C:\Users\Zeeshan\Documents"

print(path)
```

**Output:**

```text
C:\Users\Zeeshan\Documents
```

Raw strings are commonly useful for file paths and regular expressions.

---

## String Concatenation

String concatenation means joining two or more strings.

The `+` operator is used for concatenation.

### 1. Syntax

```python
string1 + string2
```

### 2. Example

```python
first_name = "Zeeshan"
last_name = "Jamshed"

full_name = first_name + " " + last_name

print(full_name)
```

**Output:**

```text
Zeeshan Jamshed
```

Here, `" "` adds a space between the two strings.

### 3. Concatenating Different Data Types

We cannot directly concatenate a string and an integer.

```python
age = 21

print("Age: " + age)
```

This gives a `TypeError`.

We can use `str()` to convert the integer into a string.

```python
age = 21

print("Age: " + str(age))
```

**Output:**

```text
Age: 21
```

---

## String Repetition

The `*` operator can be used to repeat a string.

### 1. Example

```python
text = "Python "

print(text * 3)
```

**Output:**

```text
Python Python Python
```

---

## Length of a String

The `len()` function returns the number of characters in a string.

### 1. Example

```python
text = "Python"

print(len(text))
```

**Output:**

```text
6
```

Spaces are also counted.

```python
text = "Hi Python"

print(len(text))
```

**Output:**

```text
9
```

---

## Minimum and Maximum Character

`min()` returns the smallest character according to character ordering.

`max()` returns the largest character.

### 1. Example

```python
text = "python"

print(min(text))
print(max(text))
```

**Output:**

```text
h
y
```

---

## Membership Operators

### 1. `in`

Checks whether a character or substring is present in a string.

```python
text = "Python Programming"

print("Python" in text)
```

**Output:**

```text
True
```

### 2. `not in`

Checks whether a character or substring is not present.

```python
text = "Python Programming"

print("Java" not in text)
```

**Output:**

```text
True
```

String membership is case-sensitive.

```python
print("python" in "Python")
```

**Output:**

```text
False
```

---

# String Indexing and Slicing

## String Index

Every character in a string has a position called an index.

Python uses **zero-based indexing**, so the first character has index `0`.

For example:

```python
text = "Python"
```

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Forward Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Backward Index | -6 | -5 | -4 | -3 | -2 | -1 |

---

## Indexing

Indexing is used to access one character from a string.

### 1. Syntax

```python
string[index]
```

### 2. Forward Indexing

Forward indexing starts from the left side.

```python
text = "Python"

print(text[0])
print(text[3])
print(text[5])
```

**Output:**

```text
P
h
n
```

### 3. Backward Indexing

Backward indexing starts from the right side.

The last character has index `-1`.

```python
text = "Python"

print(text[-1])
print(text[-2])
print(text[-6])
```

**Output:**

```text
n
o
P
```

### 4. IndexError

If we try to access an index which does not exist, Python gives an `IndexError`.

```python
text = "Python"

print(text[10])
```

**Error:**

```text
IndexError: string index out of range
```

For `"Python"`, valid forward indexes are:

```text
0  1  2  3  4  5
```

---

## String Slicing

Slicing is used to get a part of a string.

### 1. Syntax

```python
string[start:stop]
```

- `start` → starting index, included
- `stop` → ending index, excluded
- Last included index is `stop - 1`

### 2. Example

```python
text = "Python"

print(text[0:3])
```

**Output:**

```text
Pyt
```

Index `3` is not included.

### 3. Stop Value Outside the Range

The `stop` value can be greater than the length of the string.

Python simply stops at the end.

```python
text = "Python"

print(text[0:100])
```

**Output:**

```text
Python
```

---

## Slicing from the Beginning

If `start` is not given, Python starts from index `0`.

### 1. Example

```python
text = "Python"

print(text[:3])
```

**Output:**

```text
Pyt
```

---

## Slicing till the End

If `stop` is not given, Python continues till the end.

### 1. Example

```python
text = "Python"

print(text[2:])
```

**Output:**

```text
thon
```

---

## Complete String using Slicing

`[:]` can be used to get the complete string.

### 1. Example

```python
text = "Python"

print(text[:])
```

**Output:**

```text
Python
```

---

## Slicing with Step

We can use a third value called `step`.

### 1. Syntax

```python
string[start:stop:step]
```

The `step` tells Python how many positions to move at a time.

### 2. Positive Step

A positive step moves from left to right.

```python
text = "Python"

print(text[0:6:2])
```

**Output:**

```text
Pto
```

### 3. Negative Step

A negative step moves from right to left.

```python
text = "Python"

print(text[5:1:-1])
```

**Output:**

```text
noht
```

---

## Reverse a String

We can reverse a string using `[::-1]`.

### 1. Example

```python
text = "Python"

print(text[::-1])
```

**Output:**

```text
nohtyP
```

Here:

- Start is omitted.
- Stop is omitted.
- Step is `-1`.
- `-1` moves from right to left.

### 2. Slicing Direction Rule

With a positive step:

```text
start < stop → output
start > stop → ''
```

With a negative step:

```text
start > stop → output
start < stop → ''
```

---

# String Case Methods

## `upper()`

Converts letters into uppercase.

### 1. Example

```python
text = "hello world"

print(text.upper())
```

**Output:**

```text
HELLO WORLD
```

---

## `lower()`

Converts letters into lowercase.

### 1. Example

```python
text = "HELLO WORLD"

print(text.lower())
```

**Output:**

```text
hello world
```

---

## `capitalize()`

Converts the first character to uppercase and the remaining characters to lowercase.

### 1. Example

```python
text = "hello WORLD"

print(text.capitalize())
```

**Output:**

```text
Hello world
```

---

## `title()`

Converts the first character of each word to uppercase.

### 1. Example

```python
text = "python programming language"

print(text.title())
```

**Output:**

```text
Python Programming Language
```

---

## `swapcase()`

Changes uppercase characters to lowercase and lowercase characters to uppercase.

### 1. Example

```python
text = "Python Programming"

print(text.swapcase())
```

**Output:**

```text
pYTHON pROGRAMMING
```

---

## `casefold()`

Converts a string into a form suitable for case-insensitive comparison.

### 1. Example

```python
text = "Python"

print(text.casefold())
```

**Output:**

```text
python
```

---

# String Checking Methods

## `isupper()`

Checks whether the string is uppercase.

Returns `True` or `False`.

### 1. Example

```python
print("PYTHON".isupper())
print("Python".isupper())
```

**Output:**

```text
True
False
```

---

## `islower()`

Checks whether the string is lowercase.

### 1. Example

```python
print("python".islower())
print("Python".islower())
```

**Output:**

```text
True
False
```

---

## `istitle()`

Checks whether the string is in title case.

### 1. Example

```python
print("Python Programming".istitle())
print("python programming".istitle())
```

**Output:**

```text
True
False
```

---

## `isalpha()`

Returns `True` if all characters are alphabetic.

### 1. Example

```python
print("Python".isalpha())
print("Python123".isalpha())
```

**Output:**

```text
True
False
```

---

## `isalnum()`

Returns `True` if all characters are letters or numbers.

### 1. Example

```python
print("Python123".isalnum())
print("Python 123".isalnum())
```

**Output:**

```text
True
False
```

A space is not an alphanumeric character.

---

## `isdigit()`

Returns `True` if all characters are digits.

### 1. Example

```python
print("12345".isdigit())
print("123a".isdigit())
```

**Output:**

```text
True
False
```

---

## `isdecimal()`

Returns `True` if all characters are decimal characters.

### 1. Example

```python
print("12345".isdecimal())
print("12.5".isdecimal())
```

**Output:**

```text
True
False
```

---

## `isnumeric()`

Returns `True` if all characters are numeric.

### 1. Example

```python
print("12345".isnumeric())
```

**Output:**

```text
True
```

---

## `isspace()`

Returns `True` if the string contains only whitespace characters such as spaces, tabs, or newlines.

### 1. Example

```python
print("   ".isspace())
print("Hello".isspace())
```

**Output:**

```text
True
False
```

---

## `isprintable()`

Checks whether all characters in the string are printable.

### 1. Example

```python
print("Hello".isprintable())
print("Hello\nWorld".isprintable())
```

**Output:**

```text
True
False
```

---

## `isidentifier()`

Checks whether a string is a valid Python identifier.

### 1. Example

```python
print("student_name".isidentifier())
print("student-name".isidentifier())
print("123student".isidentifier())
```

**Output:**

```text
True
False
False
```

---

# Searching and Checking Strings

## `startswith()`

Checks whether a string starts with a particular substring.

### 1. Example

```python
text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))
```

**Output:**

```text
True
False
```

---

## `endswith()`

Checks whether a string ends with a particular substring.

### 1. Example

```python
text = "Python Programming"

print(text.endswith("Programming"))
print(text.endswith("Python"))
```

**Output:**

```text
True
False
```

### 2. Checking Multiple Endings

```python
filename = "report.pdf"

print(filename.endswith((".pdf", ".docx", ".txt")))
```

**Output:**

```text
True
```

---

## `find()`

Returns the index of the first occurrence of a substring.

If the substring is not found, it returns `-1`.

### 1. Example

```python
text = "Python Programming"

print(text.find("Program"))
print(text.find("Java"))
```

**Output:**

```text
7
-1
```

---

## `rfind()`

Returns the index of the last occurrence.

### 1. Example

```python
text = "Python Programming Python"

print(text.rfind("Python"))
```

**Output:**

```text
19
```

---

## `index()`

Returns the index of the first occurrence.

If the substring is not found, it raises a `ValueError`.

### 1. Example

```python
text = "Python Programming"

print(text.index("Program"))
```

**Output:**

```text
7
```

---

## `rindex()`

Returns the index of the last occurrence.

If the substring is not found, it raises a `ValueError`.

### 1. Example

```python
text = "Python Python"

print(text.rindex("Python"))
```

**Output:**

```text
7
```

### 2. `find()` vs `index()`

| Method | If Found | If Not Found |
|---|---|---|
| `find()` | Returns index | Returns `-1` |
| `index()` | Returns index | Raises `ValueError` |

---

## `count()`

Counts how many times a character or substring occurs.

### 1. Example

```python
text = "banana"

print(text.count("a"))
print(text.count("na"))
```

**Output:**

```text
3
2
```

We can also specify the starting position.

```python
text = "banana"

print(text.count("a", 2))
```

**Output:**

```text
2
```

---

## `replace()`

Replaces one substring with another.

### 1. Example

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

**Output:**

```text
I like Python
```

### 2. Limiting Replacements

```python
text = "apple apple apple"

print(text.replace("apple", "mango", 2))
```

**Output:**

```text
mango mango apple
```

`replace()` returns a new string. It does not change the original string.

---

# Splitting and Joining

## `split()`

Splits a string and returns a list.

By default, whitespace is used as the separator.

### 1. Example

```python
text = "Python is easy"

print(text.split())
```

**Output:**

```text
['Python', 'is', 'easy']
```

### 2. Using a Separator

```python
text = "apple,banana,mango"

print(text.split(","))
```

**Output:**

```text
['apple', 'banana', 'mango']
```

### 3. Limiting Splits

```python
text = "one-two-three-four"

print(text.split("-", 2))
```

**Output:**

```text
['one', 'two', 'three-four']
```

---

## `rsplit()`

`rsplit()` splits the string from the right side.

### 1. Example

```python
text = "one-two-three-four"

print(text.rsplit("-", 2))
```

**Output:**

```text
['one-two', 'three', 'four']
```

### 2. Difference

```text
split()  → splits from the left
rsplit() → splits from the right
```

---

## `splitlines()`

Splits a multiline string into a list of lines.

### 1. Example

```python
text = "Python\nJava\nC++"

print(text.splitlines())
```

**Output:**

```text
['Python', 'Java', 'C++']
```

---

## `join()`

`join()` combines elements of an iterable into one string.

The separator is written before `.join()`.

### 1. Example

```python
words = ["Python", "is", "easy"]

print(" ".join(words))
```

**Output:**

```text
Python is easy
```

### 2. Different Separators

```python
words = ["Python", "Java", "C++"]

print(", ".join(words))
print(" - ".join(words))
```

**Output:**

```text
Python, Java, C++
Python - Java - C++
```

---

## `partition()`

`partition()` divides a string into a 3-item tuple:

```text
(before separator, separator, after separator)
```

### 1. Example

```python
text = "name=Zeeshan"

print(text.partition("="))
```

**Output:**

```text
('name', '=', 'Zeeshan')
```

---

## `rpartition()`

`rpartition()` partitions the string at the last occurrence of the separator.

### 1. Example

```python
text = "folder/subfolder/file.txt"

print(text.rpartition("/"))
```

**Output:**

```text
('folder/subfolder', '/', 'file.txt')
```

---

# Whitespace and Formatting

## `strip()`

Removes whitespace from both the beginning and the end.

### 1. Example

```python
text = "   Python   "

print(text.strip())
```

**Output:**

```text
Python
```

---

## `lstrip()`

Removes whitespace from the beginning.

### 1. Example

```python
text = "   Python   "

print(text.lstrip())
```

**Output:**

```text
Python   
```

---

## `rstrip()`

Removes whitespace from the end.

### 1. Example

```python
text = "   Python   "

print(text.rstrip())
```

**Output:**

```text
   Python
```

These methods do not remove spaces from the middle.

---

## `strip()` with Specific Characters

We can also provide characters to remove from both ends.

### 1. Example

```python
text = "###Python###"

print(text.strip("#"))
```

**Output:**

```text
Python
```

> `strip()` treats the argument as a set of characters, not as one exact substring.

---

## `ljust()`

Left-aligns the string within the given width.

### 1. Example

```python
text = "Python"

print(text.ljust(10, "-"))
```

**Output:**

```text
Python----
```

---

## `rjust()`

Right-aligns the string within the given width.

### 1. Example

```python
text = "Python"

print(text.rjust(10, "-"))
```

**Output:**

```text
----Python
```

---

## `center()`

Centers the string within the given width.

### 1. Example

```python
text = "Python"

print(text.center(10, "-"))
```

**Output:**

```text
--Python--
```

The width represents the total length of the resulting string.

---

## `expandtabs()`

Replaces tab characters with spaces according to the specified tab size.

### 1. Example

```python
text = "Name\tAge"

print(text.expandtabs(10))
```

**Output:**

```text
Name      Age
```

---

## `zfill()`

Adds zeros to the left until the string reaches the given width.

### 1. Example

```python
number = "42"

print(number.zfill(5))
```

**Output:**

```text
00042
```

---

# String Immutability

## 1. What is Immutability?

Strings are **immutable** in Python.

This means we cannot directly change an individual character of a string.

```python
text = "Python"

text[0] = "J"
```

**Error:**

```text
TypeError: 'str' object does not support item assignment
```

## 2. String Methods Return a New String

String methods generally return a new string instead of changing the original string.

```python
text = "python"

text.upper()

print(text)
```

**Output:**

```text
python
```

To store the changed value:

```python
text = "python"

text = text.upper()

print(text)
```

**Output:**

```text
PYTHON
```

---

# String Methods Quick Reference

| Method | Purpose |
|---|---|
| `capitalize()` | Capitalizes the first character |
| `casefold()` | Converts to casefolded form |
| `center()` | Centers the string |
| `count()` | Counts occurrences |
| `endswith()` | Checks the ending |
| `expandtabs()` | Replaces tabs with spaces |
| `find()` | Finds first occurrence, returns `-1` if absent |
| `index()` | Finds first occurrence, raises `ValueError` if absent |
| `isalnum()` | Checks letters and numbers |
| `isalpha()` | Checks letters only |
| `isdecimal()` | Checks decimal characters |
| `isdigit()` | Checks digits |
| `isidentifier()` | Checks valid Python identifier |
| `islower()` | Checks lowercase |
| `isnumeric()` | Checks numeric characters |
| `isprintable()` | Checks printable characters |
| `isspace()` | Checks whitespace |
| `istitle()` | Checks title case |
| `isupper()` | Checks uppercase |
| `join()` | Joins iterable elements |
| `ljust()` | Left-aligns text |
| `lower()` | Converts to lowercase |
| `lstrip()` | Removes leading whitespace |
| `partition()` | Splits around first separator |
| `replace()` | Replaces substrings |
| `rfind()` | Finds last occurrence |
| `rindex()` | Finds last occurrence |
| `rjust()` | Right-aligns text |
| `rpartition()` | Splits around last separator |
| `rsplit()` | Splits from the right |
| `rstrip()` | Removes trailing whitespace |
| `split()` | Splits string into a list |
| `splitlines()` | Splits string into lines |
| `startswith()` | Checks the beginning |
| `strip()` | Removes characters from both ends |
| `swapcase()` | Swaps letter cases |
| `title()` | Converts to title case |
| `upper()` | Converts to uppercase |
| `zfill()` | Adds zeros to the left |

---

# String Operations Quick Reference

| Operation | Purpose |
|---|---|
| `s + s2` | Concatenates strings |
| `s * n` | Repeats a string |
| `s[index]` | Accesses one character |
| `s[start:stop]` | Slices a string |
| `s[start:stop:step]` | Slices with a step |
| `x in s` | Checks membership |
| `x not in s` | Checks absence |
| `len(s)` | Returns string length |
| `min(s)` | Returns smallest character |
| `max(s)` | Returns largest character |

---

# Important Differences

## `find()` vs `index()`

```text
find()  → returns -1 if not found
index() → raises ValueError if not found
```

## `find()` vs `rfind()`

```text
find()  → finds the first occurrence
rfind() → finds the last occurrence
```

## `split()` vs `rsplit()`

```text
split()  → splits from the left
rsplit() → splits from the right
```

## `strip()` vs `lstrip()` vs `rstrip()`

```text
strip()  → removes from both sides
lstrip() → removes from the left
rstrip() → removes from the right
```

## `upper()` vs `isupper()`

```text
upper()   → converts to uppercase
isupper() → checks whether the string is uppercase
```

## `lower()` vs `islower()`

```text
lower()   → converts to lowercase
islower() → checks whether the string is lowercase
```

## `replace()` vs `strip()`

```text
replace() → replaces text anywhere in the string
strip()   → removes characters from the ends
```

---

# Important Points to Remember

### 1. Basic String Concepts

- A string is a collection of characters.
- Strings can be created using single quotes, double quotes, or triple quotes.
- Triple quotes are useful for multiline strings.
- Strings are represented by the `str` data type.
- Strings are immutable in Python.

### 2. Indexing and Slicing

- Python uses zero-based indexing.
- Forward indexing starts from `0`.
- Backward indexing starts from `-1`.
- Indexing is used to access one character.
- An invalid index raises `IndexError`.
- Slicing is used to access a part of a string.
- Slicing uses `[start:stop]`.
- The `start` index is included.
- The `stop` index is excluded.
- The last included index is `stop - 1`.
- An out-of-range stop value in slicing does not raise an error.
- `[:]` represents the complete string.
- A third value can be used as `step`.
- A positive step moves from left to right.
- A negative step moves from right to left.
- `[::-1]` is commonly used to reverse a string.

### 3. String Operations

- `+` is used for concatenation.
- `*` is used for repetition.
- `len()` returns the number of characters.
- `min()` returns the smallest character.
- `max()` returns the largest character.
- `in` checks whether a value is present.
- `not in` checks whether a value is absent.
- `str()` can convert another data type into a string.

### 4. String Methods

- Methods beginning with `is` generally return `True` or `False`.
- `find()` returns `-1` when the substring is not found.
- `index()` raises `ValueError` when the substring is not found.
- `split()` returns a list.
- `join()` returns a string.
- `strip()`, `lstrip()`, and `rstrip()` work on the ends of a string.
- String methods generally return a new string instead of changing the original string.
```
