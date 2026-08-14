# Python Number System

## What is a Number System?

A number system is a way of representing numbers using a specific set of digits or symbols.

The commonly used number systems in programming are:

* Binary
* Octal
* Decimal
* Hexadecimal

Each number system has a different **base**.

---

# 1. Binary Number System

Binary is a **base-2** number system.

It uses only two digits:

```text
0 and 1
```

Example:

```text
1010
```

Binary is mainly used by computers because computers work with `0` and `1`.

---

# 2. Octal Number System

Octal is a **base-8** number system.

It uses eight digits:

```text
0 1 2 3 4 5 6 7
```

Example:

```text
25
```

The digits `8` and `9` are not valid in the octal number system.

---

# 3. Decimal Number System

Decimal is a **base-10** number system.

It uses ten digits:

```text
0 1 2 3 4 5 6 7 8 9
```

This is the normal number system that we use in our daily life.

Example:

```text
125
```

---

# 4. Hexadecimal Number System

Hexadecimal is a **base-16** number system.

It uses sixteen symbols:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

The letters represent values from 10 to 15:

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

Example:

```text
2A
```

Hexadecimal is commonly used in programming and computer systems.

---

# Number System Comparison

| Number System | Base | Digits / Symbols |
| ------------- | ---: | ---------------- |
| Binary        |    2 | `0–1`            |
| Octal         |    8 | `0–7`            |
| Decimal       |   10 | `0–9`            |
| Hexadecimal   |   16 | `0–9, A–F`       |

---

# Number System Conversion

In Python, we mainly use these **6 conversions**:

1. Decimal → Binary
2. Binary → Decimal
3. Decimal → Octal
4. Octal → Decimal
5. Decimal → Hexadecimal
6. Hexadecimal → Decimal

These conversions directly match Python's built-in number-system functions.

---

# 1. Decimal → Binary

Python provides the `bin()` function.

### Example 1

```python
bin(10)
```

Output:

```text
0b1010
```

### Example 2

```python
bin(25)
```

Output:

```text
0b11001
```

`0b` indicates that the number is binary.

### Manual Method

To convert decimal to binary:

1. Divide the number by `2`.
2. Write down the remainder.
3. Continue dividing the quotient by `2`.
4. Stop when the quotient becomes `0`.
5. Read the remainders from **bottom to top**.

Example: Convert `10` to binary.

```text
10 ÷ 2 = 5   remainder 0
5  ÷ 2 = 2   remainder 1
2  ÷ 2 = 1   remainder 0
1  ÷ 2 = 0   remainder 1
```

Read from bottom to top:

```text
1010
```

Therefore:

```text
10₁₀ = 1010₂
```

---

# 2. Binary → Decimal

Use the `int()` function with base `2`.

### Example 1

```python
int("1010", 2)
```

Output:

```text
10
```

### Example 2

```python
int("11001", 2)
```

Output:

```text
25
```

### Manual Method

Multiply each binary digit by the corresponding power of `2`.

Example:

```text
1010
```

Starting from the right:

```text
1 × 2³ = 8
0 × 2² = 0
1 × 2¹ = 2
0 × 2⁰ = 0
```

Add the values:

```text
8 + 0 + 2 + 0 = 10
```

Therefore:

```text
1010₂ = 10₁₀
```

---

# 3. Decimal → Octal

Python provides the `oct()` function.

### Example 1

```python
oct(10)
```

Output:

```text
0o12
```

### Example 2

```python
oct(25)
```

Output:

```text
0o31
```

`0o` indicates that the number is octal.

### Manual Method

To convert decimal to octal:

1. Divide the number by `8`.
2. Write down the remainder.
3. Continue dividing the quotient by `8`.
4. Stop when the quotient becomes `0`.
5. Read the remainders from **bottom to top**.

Example: Convert `25` to octal.

```text
25 ÷ 8 = 3   remainder 1
3  ÷ 8 = 0   remainder 3
```

Read from bottom to top:

```text
31
```

Therefore:

```text
25₁₀ = 31₈
```

---

# 4. Octal → Decimal

Use the `int()` function with base `8`.

### Example 1

```python
int("12", 8)
```

Output:

```text
10
```

### Example 2

```python
int("31", 8)
```

Output:

```text
25
```

### Manual Method

Multiply each octal digit by the corresponding power of `8`.

Example:

```text
31
```

```text
3 × 8¹ = 24
1 × 8⁰ = 1
```

Add the values:

```text
24 + 1 = 25
```

Therefore:

```text
31₈ = 25₁₀
```

---

# 5. Decimal → Hexadecimal

Python provides the `hex()` function.

### Example 1

```python
hex(10)
```

Output:

```text
0xa
```

### Example 2

```python
hex(26)
```

Output:

```text
0x1a
```

`0x` indicates that the number is hexadecimal.

### Manual Method

To convert decimal to hexadecimal:

1. Divide the number by `16`.
2. Write down the remainder.
3. Continue dividing the quotient by `16`.
4. Stop when the quotient becomes `0`.
5. Read the remainders from **bottom to top**.
6. Replace values `10–15` with `A–F`.

Example: Convert `26` to hexadecimal.

```text
26 ÷ 16 = 1   remainder 10
1  ÷ 16 = 0   remainder 1
```

Since:

```text
10 = A
```

Read from bottom to top:

```text
1A
```

Therefore:

```text
26₁₀ = 1A₁₆
```

---

# 6. Hexadecimal → Decimal

Use the `int()` function with base `16`.

### Example 1

```python
int("A", 16)
```

Output:

```text
10
```

### Example 2

```python
int("1A", 16)
```

Output:

```text
26
```

### Manual Method

Multiply each hexadecimal digit by the corresponding power of `16`.

Example:

```text
1A
```

Since:

```text
A = 10
```

Calculate:

```text
1 × 16¹ = 16
A × 16⁰ = 10
```

Add the values:

```text
16 + 10 = 26
```

Therefore:

```text
1A₁₆ = 26₁₀
```

---

# Python Number System Functions

| Function         | Conversion            |
| ---------------- | --------------------- |
| `bin()`          | Decimal → Binary      |
| `oct()`          | Decimal → Octal       |
| `hex()`          | Decimal → Hexadecimal |
| `int(value, 2)`  | Binary → Decimal      |
| `int(value, 8)`  | Octal → Decimal       |
| `int(value, 16)` | Hexadecimal → Decimal |

---

# Important Python Prefixes

Python uses special prefixes when displaying binary, octal, and hexadecimal numbers.

```text
0b → Binary
0o → Octal
0x → Hexadecimal
```

Examples:

```python
0b1010
0o12
0xA
```

All three represent the same decimal value:

```text
10
```

---

# Using `int()` with Different Bases

The second argument of `int()` tells Python which number system is being used.

```python
int("1010", 2)
int("12", 8)
int("A", 16)
```

Here:

```text
2  → Binary
8  → Octal
16 → Hexadecimal
```

---

# Manual Verification

Manual conversion is useful to **check or verify** Python's result.

For example:

```python
bin(10)
```

Python gives:

```text
0b1010
```

We can manually verify:

```text
10 ÷ 2 = 5   remainder 0
5  ÷ 2 = 2   remainder 1
2  ÷ 2 = 1   remainder 0
1  ÷ 2 = 0   remainder 1
```

Reading from bottom to top:

```text
1010
```

Python result and manual result are the same.

---

# Important Notes

### 1. These 6 conversions are the main Python conversions

We are focusing on:

```text
Decimal ↔ Binary
Decimal ↔ Octal
Decimal ↔ Hexadecimal
```

These directly match Python's built-in functions.

### 2. Direct Binary ↔ Octal and similar conversions

Conversions such as:

```text
Binary ↔ Octal
Binary ↔ Hexadecimal
Octal ↔ Hexadecimal
```

are **not included here** because Python does not provide separate built-in functions for these direct conversions.

They can still be done by using Decimal as an intermediate value.

For example:

```text
Binary → Decimal → Hexadecimal
```

But they are **not a priority for Data Science**.

### 3. Hexadecimal in programming

Hexadecimal is useful in areas such as:

* Memory addresses
* Hash values
* Colors such as `#FF5733`
* Low-level programming
* Computer systems

---

# Quick Revision

```text
Binary      → Base 2  → 0, 1
Octal       → Base 8  → 0–7
Decimal     → Base 10 → 0–9
Hexadecimal → Base 16 → 0–9, A–F
```

### Main Python Functions

```python
bin()
oct()
hex()
int()
```

### Main Conversions

```text
Decimal → Binary      → bin()
Binary → Decimal      → int(value, 2)

Decimal → Octal       → oct()
Octal → Decimal       → int(value, 8)

Decimal → Hexadecimal → hex()
Hexadecimal → Decimal → int(value, 16)
```

### Remember

> Python provides `bin()`, `oct()`, and `hex()` for converting decimal numbers to other number systems.
> The `int()` function with a base is used to convert binary, octal, and hexadecimal values back to decimal.
