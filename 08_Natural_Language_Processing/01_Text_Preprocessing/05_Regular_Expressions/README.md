# 05 Regular Expressions

## 1. Introduction

Regular expressions, also called regex, are patterns used to search, match, extract, split, or replace text. In Python, the built-in `re` module provides regular-expression functionality.

Regex is useful in NLP preprocessing when working with text patterns such as email addresses, numbers, punctuation, repeated spaces, and simple word patterns.

## 2. Learning Objectives

After studying this topic, you should understand how to:

- Use Python's `re` module.
- Match literal characters and character classes.
- Use quantifiers, anchors, and groups.
- Search for and extract patterns.
- Replace text and split strings.
- Apply regular expressions to simple NLP cleaning tasks.

## 3. Importing the Module

Python includes `re`, so it does not need to be installed separately.

```python
import re
```

Use raw strings such as `r"\\d+"` for regex patterns. They help avoid confusion between Python string escapes and regex escapes.

## 4. Common Regex Symbols

| Pattern | Meaning | Example |
|---|---|---|
| `.` | Any character except newline by default | `a.c` matches `abc` |
| `\\d` | A digit | `\\d+` matches `123` |
| `\\w` | A word character (letters, digits, underscore) | `\\w+` |
| `\\s` | Whitespace | `\\s+` |
| `[abc]` | One character from the set | `[aeiou]` |
| `[^abc]` | One character not in the set | `[^0-9]` |
| `+` | One or more repetitions | `a+` |
| `*` | Zero or more repetitions | `ab*` |
| `?` | Zero or one repetition | `colou?r` |
| `{m,n}` | Between m and n repetitions | `\\d{2,4}` |
| `^` | Start of string (or line in multiline mode) | `^Hello` |
| `$` | End of string (or line in multiline mode) | `world$` |
| `\\b` | Word boundary | `\\bcat\\b` |
| `( )` | Capturing group | `(ab)+` |
| `|` | Alternative (OR) | `cat|dog` |

The exact meaning of some symbols depends on flags and context. For example, `\\w` and `\\d` are Unicode-aware for Python string patterns by default.

## 5. Main Functions in Python's `re` Module

| Function | Purpose |
|---|---|
| `re.search()` | Finds the first match anywhere in the string. |
| `re.match()` | Checks for a match at the beginning of the string. |
| `re.fullmatch()` | Checks whether the entire string matches the pattern. |
| `re.findall()` | Returns all non-overlapping matches. |
| `re.finditer()` | Returns an iterator of match objects. |
| `re.sub()` | Replaces matches with another string. |
| `re.split()` | Splits a string using a pattern. |
| `re.compile()` | Compiles a pattern for reuse. |

## 6. Finding Patterns

### Example 1: Extracting Numbers

```python
import re

text = "I have 2 notebooks and 15 pens."

numbers = re.findall(r"\\d+", text)

print(numbers)
```

Output:

```text
['2', '15']
```

### Example 2: Searching for a Word

```python
import re

text = "I am learning Python for NLP."

match = re.search(r"Python", text)

if match:
    print("Found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
else:
    print("No match found.")
```

Output:

```text
Found: Python
Start: 14
End: 20
```

The start index is inclusive and the end index is exclusive.

## 7. Replacing Text with `re.sub()`

```python
import re

text = "Python     is   useful for NLP."

cleaned_text = re.sub(r"\\s+", " ", text).strip()

print(cleaned_text)
```

Output:

```text
Python is useful for NLP.
```

Here, `\\s+` matches one or more whitespace characters and replaces each matching sequence with a single space.

## 8. Extracting Email-Like Patterns

```python
import re

text = "Contact us at support@example.com or team@example.org."

pattern = r"[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print(emails)
```

Output:

```text
['support@example.com', 'team@example.org']
```

This pattern is a practical demonstration, not a complete validator for every valid email address. Use appropriate validation for production systems.

## 9. Regex for Basic NLP Text Cleaning

Regular expressions can remove or replace selected text patterns.

```python
import re
from html import unescape


def clean_text(text):
    # Decode common HTML entities
    text = unescape(text)

    # Remove simple HTML-like tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Replace URLs with a space
    text = re.sub(r"https?://\\S+|www\\.\\S+", " ", text)

    # Normalize repeated whitespace
    text = re.sub(r"\\s+", " ", text).strip()

    return text


raw_text = "<p>Learn NLP at https://example.com   today!</p>"
print(clean_text(raw_text))
```

Output:

```text
Learn NLP at today!
```

**Important:** Regex-based HTML removal is only suitable for simple examples. For complex or malformed HTML, use a dedicated HTML parser such as Beautiful Soup. Cleaning rules should also preserve punctuation, URLs, numbers, or other information when they are meaningful for the task.

## 10. Splitting Text

```python
import re

text = "apple, banana; orange  grape"

items = re.split(r"[,;\\s]+", text.strip())

print(items)
```

Output:

```text
['apple', 'banana', 'orange', 'grape']
```

This splits the text wherever one or more commas, semicolons, or whitespace characters occur.

## 11. Capturing Groups

Groups let you extract parts of a matched pattern.

```python
import re

text = "Date: 2026-10-26"

match = re.search(r"(\\d{4})-(\\d{2})-(\\d{2})", text)

if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Day:", match.group(3))
```

Output:

```text
Year: 2026
Month: 10
Day: 26
```

Group 0 represents the complete match. Groups 1, 2, and 3 represent the captured year, month, and day.

## 12. Using Regex in NLP

Common NLP use cases include:

- Extracting numbers, dates, and simple identifiers.
- Removing or replacing URLs and email addresses.
- Normalizing repeated whitespace.
- Finding selected word patterns.
- Cleaning simple markup.
- Preparing text before tokenization.

Regex is pattern-based and does not understand language meaning. More advanced language tasks may require tokenizers, parsers, or NLP libraries.

## 13. Related Files

- `Regular_Expressions.py` — runnable examples of common regex operations.
- [Text Cleaning and Normalization](../02_Text_Cleaning_and_Normalization/README.md)
- [Tokenization](../03_Tokenization/README.md)

## 14. Key Takeaways

- Regular expressions describe patterns in text.
- Python's built-in `re` module supports searching, extracting, replacing, and splitting.
- Raw strings make regex patterns easier to read.
- Use quantifiers, character classes, anchors, and groups according to the pattern.
- Regex can support NLP cleaning but cannot replace full linguistic analysis.
- Test patterns against representative text before using them on a complete dataset.

## 15. References

- [Python `re` documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
