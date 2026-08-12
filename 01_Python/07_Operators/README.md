# Python Operators

## What are Operators?

Operators are special symbols or keywords used to **perform operations on values and variables**.

For example:

```python
num1 = 10
num2 = 5

print(num1 + num2)
```

Output:

```text
15
```

Here, `+` is an operator used for addition.

Python has different types of operators.

---

# Types of Operators

The basic operators covered here are:

1. Arithmetic Operators
2. Assignment Operators
3. Relational Operators
4. Logical Operators
5. Unary Operators

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform **mathematical operations**.

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

---

## Addition `+`

The `+` operator is used to add two values.

```python
num1 = 10
num2 = 5

print(num1 + num2)
```

Output:

```text
15
```

---

## Subtraction `-`

The `-` operator is used to subtract one value from another.

```python
num1 = 10
num2 = 5

print(num1 - num2)
```

Output:

```text
5
```

---

## Multiplication `*`

The `*` operator is used to multiply two values.

```python
num1 = 10
num2 = 5

print(num1 * num2)
```

Output:

```text
50
```

---

## Division `/`

The `/` operator is used for division.

```python
num1 = 10
num2 = 5

print(num1 / num2)
```

Output:

```text
2.0
```

> **Note:** The `/` operator returns the division result as a floating-point value.

---

## Floor Division `//`

The `//` operator is used for floor division.

It returns the quotient after removing the decimal part by flooring the result.

```python
print(10 // 3)
```

Output:

```text
3
```

Another example:

```python
print(7 // 2)
```

Output:

```text
3
```

---

## Modulus `%`

The `%` operator returns the **remainder** after division.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 ÷ 3 = 3 remainder 1
```

So:

```python
10 % 3
```

gives:

```text
1
```

---

## Exponentiation `**`

The `**` operator is used to calculate the power of a number.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

Another example:

```python
print(5 ** 2)
```

Output:

```text
25
```

---

# 2. Assignment Operators

Assignment operators are used to **assign or update values in variables**.

The basic assignment operator is:

```python
=
```

### Basic Assignment

```python
num = 10

print(num)
```

Output:

```text
10
```

Here, `10` is assigned to the variable `num`.

---

## Arithmetic Assignment Operators

Arithmetic assignment operators are formed by taking an **arithmetic operator and adding `=`**.

### Pattern

```text
Arithmetic Operator + =
```

For example:

```text
+  →  +=
-  →  -=
*  →  *=
/  →  /=
// →  //=
%  →  %=
** →  **=
```

---

## Assignment Operators Table

| Operator | Meaning                 | Same As      |
| -------- | ----------------------- | ------------ |
| `=`      | Assignment              | `a = 10`     |
| `+=`     | Add and assign          | `a = a + 5`  |
| `-=`     | Subtract and assign     | `a = a - 5`  |
| `*=`     | Multiply and assign     | `a = a * 5`  |
| `/=`     | Divide and assign       | `a = a / 5`  |
| `//=`    | Floor divide and assign | `a = a // 5` |
| `%=`     | Modulus and assign      | `a = a % 5`  |
| `**=`    | Power and assign        | `a = a ** 5` |

---

## `+=`

```python
num = 10

num += 5

print(num)
```

Output:

```text
15
```

It is the same as:

```python
num = num + 5
```

---

## `-=`

```python
num = 10

num -= 3

print(num)
```

Output:

```text
7
```

It is the same as:

```python
num = num - 3
```

---

## `*=`

```python
num = 10

num *= 2

print(num)
```

Output:

```text
20
```

It is the same as:

```python
num = num * 2
```

---

## `/=`

```python
num = 10

num /= 2

print(num)
```

Output:

```text
5.0
```

It is the same as:

```python
num = num / 2
```

---

## `//=`

```python
num = 10

num //= 3

print(num)
```

Output:

```text
3
```

It is the same as:

```python
num = num // 3
```

---

## `%=`

```python
num = 10

num %= 3

print(num)
```

Output:

```text
1
```

It is the same as:

```python
num = num % 3
```

---

## `**=`

```python
num = 2

num **= 3

print(num)
```

Output:

```text
8
```

It is the same as:

```python
num = num ** 3
```

---

# 3. Relational Operators

Relational operators are also called **comparison operators**.

They are used to **compare two values**.

The result of a comparison is either:

```text
True
```

or

```text
False
```

### Relational Operators

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `5 == 5` |
| `!=`     | Not equal to             | `5 != 3` |
| `>`      | Greater than             | `5 > 3`  |
| `<`      | Less than                | `3 < 5`  |
| `>=`     | Greater than or equal to | `5 >= 5` |
| `<=`     | Less than or equal to    | `3 <= 5` |

---

## Equal to `==`

```python
print(10 == 10)
```

Output:

```text
True
```

```python
print(10 == 5)
```

Output:

```text
False
```

> `=` is used for assignment, while `==` is used for comparison.

---

## Not Equal to `!=`

```python
print(10 != 5)
```

Output:

```text
True
```

```python
print(10 != 10)
```

Output:

```text
False
```

---

## Greater Than `>`

```python
print(10 > 5)
```

Output:

```text
True
```

---

## Less Than `<`

```python
print(5 < 10)
```

Output:

```text
True
```

---

## Greater Than or Equal to `>=`

```python
print(10 >= 10)
```

Output:

```text
True
```

It is also `True` when the left value is greater:

```python
print(10 >= 5)
```

Output:

```text
True
```

---

## Less Than or Equal to `<=`

```python
print(5 <= 5)
```

Output:

```text
True
```

It is also `True` when the left value is smaller:

```python
print(5 <= 10)
```

Output:

```text
True
```

---

# 4. Logical Operators

Logical operators are used to **combine or modify conditions**.

Python has three basic logical operators:

* `and`
* `or`
* `not`

---

## `and` Operator

The `and` operator returns `True` only when **both conditions are True**.

### Truth Table

| Condition 1 | Condition 2 | Result |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | False  |
| False       | True        | False  |
| False       | False       | False  |

### Example

```python
print(10 > 5 and 10 < 20)
```

Output:

```text
True
```

Both conditions are True.

Another example:

```python
print(10 > 5 and 10 > 20)
```

Output:

```text
False
```

The first condition is True, but the second condition is False.

Therefore, the result is False.

---

## `or` Operator

The `or` operator returns `True` when **at least one condition is True**.

### Truth Table

| Condition 1 | Condition 2 | Result |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | True   |
| False       | True        | True   |
| False       | False       | False  |

### Example

```python
print(10 > 5 or 10 > 20)
```

Output:

```text
True
```

The first condition is True, so the overall result is True.

Another example:

```python
print(10 < 5 or 10 > 20)
```

Output:

```text
False
```

Both conditions are False.

---

## `not` Operator

The `not` operator reverses the Boolean result.

### Truth Table

| Condition | `not` Condition |
| --------- | --------------- |
| True      | False           |
| False     | True            |

### Example

```python
print(not True)
```

Output:

```text
False
```

Another example:

```python
print(not False)
```

Output:

```text
True
```

Using a comparison:

```python
print(not (10 > 5))
```

Output:

```text
False
```

Because:

```text
10 > 5
```

is True, and `not` changes True to False.

---

# 5. Unary Operator

A unary operator is an operator that works with **only one operand**.

For example:

```python
num = 10

print(-num)
```

Output:

```text
-10
```

Here:

* `-` is the unary operator.
* `num` is the only operand.

---

## Why Do We Use Unary Operators?

Unary operators are mainly used when we want to **represent or change the sign of a value**.

### Unary Plus `+`

The unary `+` represents a positive value.

```python
num = 10

print(+num)
```

Output:

```text
10
```

### Unary Minus `-`

The unary `-` changes the sign of a value.

```python
num = 10

print(-num)
```

Output:

```text
-10
```

If the value is already negative:

```python
num = -10

print(-num)
```

Output:

```text
10
```

So, unary minus changes the sign of the value.

---

## Unary vs Binary Operators

The same symbol can sometimes work as a unary or binary operator depending on how it is used.

### Unary

```python
-num
```

Here `-` works on one operand.

### Binary

```python
num1 - num2
```

Here `-` works between two operands.

So:

```text
Unary operator  → works on one operand
Binary operator → works on two operands
```

---

# Quick Revision

```python
# Arithmetic Operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

# Assignment Operators
num = 10
num += 5
num -= 2
num *= 2
num /= 2
num //= 2
num %= 2
num **= 2

# Relational Operators
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(5 < 10)
print(10 >= 10)
print(5 <= 10)

# Logical Operators
print(True and True)
print(True or False)
print(not True)

# Unary Operators
num = 10
print(+num)
print(-num)
```

---

# Important Points

* Operators are used to perform operations on values and variables.
* Arithmetic operators are used for mathematical calculations.
* `//` performs floor division.
* `%` gives the remainder.
* `**` is used for exponentiation.
* `=` is the basic assignment operator.
* Arithmetic assignment operators are formed by adding `=` with an arithmetic operator.
* Relational operators compare two values and return `True` or `False`.
* `and` returns `True` only when both conditions are True.
* `or` returns `True` when at least one condition is True.
* `not` reverses the Boolean result.
* A unary operator works with only one operand.
* Unary `+` represents a positive value.
* Unary `-` changes the sign of a value.
* `=` and `==` have different purposes:

  * `=` → Assignment
  * `==` → Comparison

---

# Summary

Operators are an important part of Python because they allow us to perform calculations, assign and update values, compare values, combine conditions, and work with the sign of a value.

The main operators covered in this topic are **Arithmetic, Assignment, Relational, Logical, and Unary operators**.
