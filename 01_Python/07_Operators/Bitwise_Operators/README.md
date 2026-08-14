# Bitwise Operators in Python

## What are Bitwise Operators?

Bitwise operators are used to perform operations on the **individual bits (0 and 1)** of an integer.

Example:

```python
a = 5
```

Binary representation of `5`:

```text
5 = 0101
```

Python provides the following bitwise operators:

| Operator    | Name                     | Symbol |
| ----------- | ------------------------ | ------ |
| AND         | Bitwise AND              | `&`    |
| OR          | Bitwise OR               | `\|`   |
| XOR         | Bitwise XOR              | `^`    |
| Complement  | Bitwise NOT / Complement | `~`    |
| Left Shift  | Left Shift               | `<<`   |
| Right Shift | Right Shift              | `>>`   |

---

# 1. Bitwise AND (`&`)

The AND operator compares each bit of two numbers.

### Rule

* `1 & 1` → `1`
* Otherwise → `0`

### Example

```text
  5 = 0101
  3 = 0011
      ----
5 & 3 = 0001
```

Therefore:

```python
5 & 3
```

Output:

```text
1
```

### Truth Table

| A | B | A & B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 0     |
| 1 | 0 | 0     |
| 1 | 1 | 1     |

---

# 2. Bitwise OR (`|`)

The OR operator compares each bit of two numbers.

### Rule

* If **at least one bit is `1`**, the result is `1`.
* Only `0 | 0` gives `0`.

### Example

```text
  5 = 0101
  3 = 0011
      ----
5 | 3 = 0111
```

Therefore:

```python
5 | 3
```

Output:

```text
7
```

### Truth Table

| A | B | A | B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 1     |

---

# 3. Bitwise XOR (`^`)

XOR means **Exclusive OR**.

### Rule

* Different bits → `1`
* Same bits → `0`

### Example

```text
  5 = 0101
  3 = 0011
      ----
5 ^ 3 = 0110
```

Therefore:

```python
5 ^ 3
```

Output:

```text
6
```

### Truth Table

| A | B | A ^ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

---

# 4. Bitwise Complement (`~`)

The complement operator changes every bit:

```text
0 → 1
1 → 0
```

It is also called **Bitwise NOT**.

The operator used in Python is:

```python
~
```

### Important Rule

For an integer:

```text
1's complement + 1 = 2's complement
```

And Python's complement operation follows:

```text
~n = -(n + 1)
```

### Example

```python
~5
```

We can understand it using binary representation:

```text
5 = 0101
```

1's complement:

```text
1010
```

Add `1`:

```text
1010
+   1
-----
1011
```

The result represents `-6`.

Therefore:

```python
~5
```

Output:

```text
-6
```

### Shortcut

```text
~5 = -(5 + 1)
   = -6
```

Similarly:

```text
~10 = -11
~20 = -21
```

---

# 5. Left Shift (`<<`)

The left shift operator shifts the bits towards the **left**.

Syntax:

```python
number << positions
```

### Example

```text
5 = 0101
```

Shift left by 1:

```text
0101 << 1
= 1010
```

`1010` is `10`.

Therefore:

```python
5 << 1
```

Output:

```text
10
```

### Important Rule

Each left shift by one position generally **multiplies the number by 2**.

```text
5 << 1 = 10
5 << 2 = 20
5 << 3 = 40
```

Formula:

```text
n << k = n × 2^k
```

---

# 6. Right Shift (`>>`)

The right shift operator shifts the bits towards the **right**.

Syntax:

```python
number >> positions
```

### Example

```text
20 = 10100
```

Shift right by 1:

```text
10100 >> 1
= 01010
```

`01010` is `10`.

Therefore:

```python
20 >> 1
```

Output:

```text
10
```

### Important Rule

For positive integers, each right shift by one position generally **divides the number by 2** and keeps the integer result.

```text
20 >> 1 = 10
20 >> 2 = 5
20 >> 3 = 2
```

Formula:

```text
n >> k = n // 2^k
```

---

# Quick Summary

| Operator | Name        | Main Rule                    |
| -------- | ----------- | ---------------------------- |
| `&`      | AND         | Both bits must be `1`        |
| `\|`     | OR          | At least one bit must be `1` |
| `^`      | XOR         | Different bits → `1`         |
| `~`      | Complement  | `~n = -(n + 1)`              |
| `<<`     | Left Shift  | Multiply by `2^k`            |
| `>>`     | Right Shift | Integer divide by `2^k`      |

## Important Points to Remember

### AND

```text
1 & 1 = 1
```

### OR

```text
0 | 0 = 0
```

### XOR

```text
Same → 0
Different → 1
```

### Complement

```text
1's complement + 1 = 2's complement

~n = -(n + 1)
```

### Left Shift

```text
n << k = n × 2^k
```

### Right Shift

```text
n >> k = n // 2^k
```

These operators work at the **bit level**, so understanding binary numbers is important before using bitwise operators.
