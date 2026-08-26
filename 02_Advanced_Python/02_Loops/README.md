# Python Loops

Loops are used to **repeat a block of code multiple times**.

Instead of writing the same code again and again, we can use a loop.

For example, without a loop:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Using a loop:

```python
for i in range(1, 6):
    print(i)
```

Both produce:

```text
1
2
3
4
5
```

The loop makes the code shorter, cleaner, and easier to maintain.

---

# Types of Loops

Python has two main types of loops:

1. **`while` loop**
2. **`for` loop**

---

# 1. While Loop

A `while` loop executes a block of code **as long as a condition is `True`**.

## Syntax

```python
while condition:
    statement
```

The condition is checked before every iteration.

If the condition is `True`, the code inside the loop executes.

If the condition becomes `False`, the loop stops.

---

## Basic Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

Here:

* `i = 1` initializes the variable.
* `i <= 5` is the condition.
* `print(i)` prints the current value.
* `i += 1` increases `i` by `1`.

---

# How a While Loop Works

Consider:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

The execution happens like this:

```text
i = 1
1 <= 5 → True → print 1
i = 2

2 <= 5 → True → print 2
i = 3

3 <= 5 → True → print 3
i = 4

4 <= 5 → True → print 4
i = 5

5 <= 5 → True → print 5
i = 6

6 <= 5 → False → Stop
```

The condition is checked before every iteration.

---

# Infinite Loop

If the condition never becomes `False`, the loop will continue forever.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

This is an infinite loop because `i` never changes.

The condition will always remain:

```text
1 <= 5
```

So the loop never stops.

A common solution is to update the variable:

```python
i += 1
```

---

# While Loop With User Input

A `while` loop is useful when you don't know how many times the loop should run.

Example:

```python
number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter another number: "))
```

The loop continues until the user enters `0`.

---

# Practical Example: Countdown

```python
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Done")
```

Output:

```text
5
4
3
2
1
Done
```

---

# Practical Example: Sum of Digits

Suppose the user enters:

```text
12345
```

We can find the sum of its digits using a `while` loop.

```python
n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)
```

Output:

```text
15
```

Because:

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

# Practical Example: Reverse a Number

```python
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)
```

Input:

```text
12345
```

Output:

```text
54321
```

---

# 2. For Loop

A `for` loop is used to iterate over a sequence or repeat a block of code a specific number of times.

## Syntax

```python
for variable in sequence:
    statement
```

The variable takes one value at a time from the sequence.

---

## Basic Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

Here:

* `i` is the loop variable.
* `range(5)` generates numbers from `0` to `4`.
* The loop executes `5` times.

---

# Understanding `range()`

`range()` is commonly used with `for` loops.

There are three common forms.

## `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The `stop` value is **not included**.

---

## `range(start, stop)`

```python
for i in range(2, 7):
    print(i)
```

Output:

```text
2
3
4
5
6
```

It starts at `2` and stops before `7`.

---

## `range(start, stop, step)`

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

Here:

* `start = 2`
* `stop = 11`
* `step = 2`

The value increases by `2` after every iteration.

---

# Counting Backwards

The step can also be negative.

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Looping Through a String

A `for` loop can iterate through each character of a string.

```python
name = "Zee"

for char in name:
    print(char)
```

Output:

```text
Z
e
e
```

Each character is processed one at a time.

---

# Looping Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

The loop visits every item in the list.

---

# Practical Example: Multiplication Table

```python
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

If the user enters `5`:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# Loop Control Statements

Python provides three important statements for controlling loops:

* `break`
* `continue`
* `pass`

These can be used inside both `for` and `while` loops.

---

# `break` in a `for` Loop

`break` is used to **stop the loop immediately**.

As soon as Python encounters `break`, the loop ends.

## Example

```python
for i in range(1, 11):
    if i == 6:
        break

    print(i)
```

Output:

```text
1
2
3
4
5
```

When `i` becomes `6`, `break` stops the entire loop.

The numbers `6` to `10` are never printed.

---

## Example: Find a Number

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Number found")
        break

    print(num)
```

Output:

```text
10
20
Number found
```

Once `30` is found, the loop stops.

---

# `continue` in a `for` Loop

`continue` is used to **skip the current iteration**.

It does not stop the entire loop.

## Example

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

When `i` becomes `3`, Python skips the remaining code for that iteration and moves to the next iteration.

---

## Example: Print Only Odd Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
7
9
```

Here, `continue` skips the even numbers.

---

# `pass` in a `for` Loop

`pass` does **nothing**.

It is used as a placeholder when you want to write the structure of your code but don't want to add the actual logic yet.

## Example

```python
for i in range(5):
    pass
```

The loop runs five times, but nothing is displayed.

---

## `pass` vs `continue`

It is important to understand the difference.

### `pass`

```python
for i in range(1, 6):
    if i == 3:
        pass

    print(i)
```

Output:

```text
1
2
3
4
5
```

`pass` does nothing, so `3` is still printed.

### `continue`

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

`continue` skips the rest of the current iteration.

---

# `break` vs `continue` vs `pass`

| Statement  | What it does                |
| ---------- | --------------------------- |
| `break`    | Stops the entire loop       |
| `continue` | Skips the current iteration |
| `pass`     | Does nothing                |

Think of them like this:

```text
break
  ↓
Stop the loop completely

continue
  ↓
Skip this iteration
Then continue the loop

pass
  ↓
Do nothing
Continue normally
```

---

# For Loop With `else`

Python allows an `else` block with a `for` loop.

The `else` block executes when the loop finishes **normally**, without being stopped by `break`.

## Syntax

```python
for variable in sequence:
    statement
else:
    statement
```

---

## Example

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
3
4
Loop completed
```

The loop completed normally, so the `else` block executed.

---

# `for-else` With `break`

If the loop is stopped using `break`, the `else` block does not execute.

```python
for i in range(5):
    if i == 3:
        break

    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

The loop was terminated by `break`, so the `else` block was skipped.

---

# Practical Example: Searching With `for-else`

A common use of `for-else` is searching for an item.

```python
numbers = [10, 20, 30, 40, 50]

search = 30

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")
```

Output:

```text
Number found
```

If we search for `60`:

```python
numbers = [10, 20, 30, 40, 50]

search = 60

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")
```

Output:

```text
Number not found
```

The logic is:

```text
Number found
     ↓
break
     ↓
else is skipped

Number not found
     ↓
Loop finishes normally
     ↓
else executes
```

---

# Nested Loops

A loop inside another loop is called a **nested loop**.

Example:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

The inner loop runs completely for every iteration of the outer loop.

---

# Understanding Nested Loops

For:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

The execution is:

```text
i = 0
    j = 0 → print 0 0
    j = 1 → print 0 1

i = 1
    j = 0 → print 1 0
    j = 1 → print 1 1

i = 2
    j = 0 → print 2 0
    j = 1 → print 2 1
```

The outer loop runs `3` times.

The inner loop runs `2` times for each outer iteration.

Therefore:

```text
3 × 2 = 6
```

The `print()` statement executes `6` times.

---

# Patterns Using Loops

Patterns are one of the best ways to practice **nested loops**.

A pattern usually consists of:

* Rows
* Columns
* Characters or numbers

For example:

```text
*
* *
* * *
* * * *
* * * * *
```

There are `5` rows.

The number of stars increases by `1` in every row.

---

# Understanding Pattern Logic

Consider:

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()
```

There are two loops:

### Outer loop

```python
for i in range(1, 6):
```

Controls the **rows**.

### Inner loop

```python
for j in range(i):
```

Controls how many stars are printed in each row.

### `print("*", end=" ")`

Prints stars on the same line.

### `print()`

Moves to the next line after the inner loop finishes.

---

# Pattern 1: Increasing Star Pattern

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

Logic:

```text
Row 1 → 1 star
Row 2 → 2 stars
Row 3 → 3 stars
Row 4 → 4 stars
Row 5 → 5 stars
```

---

# Pattern 2: Decreasing Star Pattern

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * *
* * *
* *
*
```

Logic:

```text
Row 1 → 5 stars
Row 2 → 4 stars
Row 3 → 3 stars
Row 4 → 2 stars
Row 5 → 1 star
```

---

# Pattern 3: Number Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Here:

* Outer loop controls rows.
* Inner loop prints numbers from `1` to `i`.

---

# Pattern 4: Repeated Number Pattern

In this pattern, the same number is printed throughout each row.

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")

    print()
```

Output:

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

Notice that the inner loop prints `i` instead of `j`.

---

# Pattern 5: Continuous Number Pattern

Here the numbers continue from one row to the next.

```python
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1

    print()
```

Output:

```text
1
2 3
4 5 6
7 8 9 10
```

The variable `num` is updated after every number.

---

# Pattern 6: Square Pattern

A square has the same number of rows and columns.

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

Here:

```text
Rows    = 5
Columns = 5
```

---

# Pattern 7: Rectangle Pattern

The number of rows and columns can be different.

```python
for i in range(3):
    for j in range(5):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * * *
* * * * *
```

Here:

```text
Rows    = 3
Columns = 5
```

---

# Pattern 8: Right-Aligned Star Pattern

Spaces can be used to move the stars toward the right.

```python
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
```

Output:

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

There are two inner loops:

1. First loop → prints spaces.
2. Second loop → prints stars.

---

# Pattern 9: Pyramid Pattern

A pyramid can be created using spaces and stars.

```python
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

Output:

```text
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

The formulas are:

```text
Spaces = n - i
Stars  = 2 × i - 1
```

---

# How to Approach Pattern Problems

When solving a pattern problem, identify three things.

## 1. Number of Rows

Ask:

> How many lines are there?

Example:

```text
*
* *
* * *
* * * *
* * * * *
```

There are `5` rows.

So:

```python
for i in range(1, 6):
```

---

## 2. Number of Columns

Ask:

> How many characters are printed in each row?

For the increasing pattern:

```text
Row 1 → 1
Row 2 → 2
Row 3 → 3
Row 4 → 4
Row 5 → 5
```

So:

```python
for j in range(i):
```

---

## 3. What Should Be Printed?

Ask:

> Should I print `*`, `i`, `j`, spaces, or another value?

For stars:

```python
print("*", end=" ")
```

For the current row number:

```python
print(i, end=" ")
```

For the current column number:

```python
print(j, end=" ")
```

---

# Pattern Formula Cheat Sheet

For `n = 5`:

## Increasing Pattern

```text
*
* *
* * *
* * * *
* * * * *
```

```python
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")

    print()
```

## Decreasing Pattern

```text
* * * * *
* * * *
* * *
* *
*
```

```python
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()
```

## Square

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

```python
for i in range(n):
    for j in range(n):
        print("*", end=" ")

    print()
```

## Pyramid

```text
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

```python
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

---

# Practical Example: Sum of Numbers

Find the sum of numbers from `1` to `10`.

```python
total = 0

for i in range(1, 11):
    total += i

print(total)
```

Output:

```text
55
```

---

# Practical Example: Factorial

The factorial of `5` is:

```text
5 × 4 × 3 × 2 × 1 = 120
```

Python code:

```python
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```

Output:

```text
120
```

---

# Practical Example: Prime Number

A prime number has exactly two factors:

```text
1 and itself
```

Example:

```text
7 → Prime
10 → Not Prime
```

Using a loop:

```python
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
```

---

# For Loop vs While Loop

| `while` loop                                    | `for` loop                                    |
| ----------------------------------------------- | --------------------------------------------- |
| Repeats while a condition is `True`             | Iterates over a sequence or range             |
| Useful when the number of iterations is unknown | Useful when the number of iterations is known |
| Usually uses a condition                        | Commonly uses `range()` or a sequence         |
| Can easily create an infinite loop              | Less likely to create an infinite loop        |

Example using `while`:

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

Example using `for`:

```python
for i in range(5):
    print(i)
```

Both produce:

```text
0
1
2
3
4
```

---

# Common Loop Mistakes

## 1. Forgetting to update a `while` loop

Incorrect:

```python
i = 1

while i <= 5:
    print(i)
```

This creates an infinite loop.

Correct:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## 2. Incorrect Indentation

Correct:

```python
for i in range(5):
    print(i)
```

Incorrect:

```python
for i in range(5):
print(i)
```

Python uses indentation to determine which statements belong to the loop.

---

## 3. Forgetting That `range()` Excludes the Stop Value

```python
range(1, 5)
```

produces:

```text
1 2 3 4
```

It does not produce `5`.

To include `5`:

```python
range(1, 6)
```

---

# Quick Summary

```text
while
↓
Repeat while a condition is True

for
↓
Iterate over a sequence or range

break
↓
Stop the entire loop

continue
↓
Skip the current iteration

pass
↓
Do nothing / placeholder

for-else
↓
else runs when the for loop finishes normally

nested loop
↓
Loop inside another loop

pattern
↓
Use nested loops to control rows and columns

range()
↓
Generate a sequence of numbers
```

---

# Practice Questions

Try solving these without looking at the solution:

1. Print numbers from `1` to `100`.
2. Print all even numbers from `1` to `50`.
3. Print all odd numbers from `1` to `50`.
4. Print the multiplication table of a number.
5. Find the sum of numbers from `1` to `n`.
6. Find the factorial of a number.
7. Count the number of digits in an integer.
8. Find the sum of digits of an integer.
9. Reverse an integer.
10. Check whether a number is a palindrome.
11. Check whether a number is prime.
12. Print all prime numbers from `1` to `100`.
13. Find the largest digit in a number.
14. Find the smallest digit in a number.
15. Print the Fibonacci series.
16. Create an increasing star pattern.
17. Create a decreasing star pattern.
18. Create a square pattern.
19. Create a rectangle pattern.
20. Create a number pattern.
21. Create a repeated number pattern.
22. Create a continuous number pattern.
23. Create a pyramid pattern.
24. Practice `break` inside a `for` loop.
25. Practice `continue` inside a `for` loop.
26. Practice `pass` inside a `for` loop.
27. Create a `for-else` program to search for a number.
28. Create a `while` loop that keeps asking for input until the user enters `0`.

---

# Conclusion

Loops are one of the most important concepts in Python.

The basic idea is:

```text
Repeat something
      ↓
Use a loop
```

Use a **`while` loop** when repetition depends mainly on a condition.

Use a **`for` loop** when you are iterating over a sequence or know the range of repetition.

Once you understand loops, you can solve many important programming problems such as:

* Patterns
* Factorials
* Prime numbers
* Digit problems
* Multiplication tables
* Searching
* Number series
* Data processing

The best way to become comfortable with loops is to **write and modify small programs repeatedly**.