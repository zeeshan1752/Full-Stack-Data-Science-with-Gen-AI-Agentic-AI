# Python Variables

## What is a Variable?

A **variable** is a name used to store data in memory. The value stored in a variable can be changed during program execution.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Zeeshan"
age = 21
height = 5.8
```

---

## Rules for Naming Variables

- Variable names can contain letters, numbers, and underscores (`_`).
- Variable names cannot start with a number.
- Variable names are case-sensitive.
- Do not use Python keywords as variable names.
- Use meaningful variable names.

### Valid Variable Names

```python
name = "Zeeshan"
student_name = "Ali"
age1 = 21
_marks = 95
```

### Invalid Variable Names

```python
1name = "Zeeshan"      # Starts with a number
student-name = "Ali"   # Hyphen is not allowed
class = "Python"       # Keyword
```

---

## Assigning Values

```python
name = "Zeeshan"
age = 21
city = "Lucknow"
```

---

## Multiple Assignment

```python
a = b = c = 100
```

```python
name, age, city = "Zeeshan", 21, "Lucknow"
```

---

## Printing Variables

```python
name = "Zeeshan"
age = 21

print(name)
print(age)
```

---

## Variable Types

```python
name = "Zeeshan"      # String
age = 21              # Integer
height = 5.8          # Float
is_student = True     # Boolean
```

---

## Check Variable Type

```python
name = "Python"

print(type(name))
```

Output

```
<class 'str'>
```

---

## Best Practices

- Use meaningful variable names.
- Follow snake_case naming.
- Avoid single-letter variable names unless required.
- Keep names short and descriptive.

### Good Examples

```python
student_name
mobile_number
total_marks
employee_salary
```

### Avoid

```python
a
x
abc
temp1
```

---

## Summary

In this topic, I learned:

- What is a variable
- Variable naming rules
- Valid and invalid variable names
- Assigning values
- Multiple assignment
- Printing variables
- Data types
- Using the `type()` function

---

## Folder Contents

- `variables.ipynb`
- `task.py`
- `trainer_notes.pdf`