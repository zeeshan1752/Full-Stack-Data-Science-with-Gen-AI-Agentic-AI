# Data Structures — README

## Data Type vs Data Structure

### Data Type

A **data type** defines the type of a value.

Examples:

```text
int
float
str
bool
```

Example:

```python
age = 21
```

Here, `21` is an **integer (`int`) data type**.

### Data Structure

A **data structure** is a collection of data types organized and stored in a particular way.

```text
Data Structure → Collection of data types
```

Example:

```python
marks = [85, 90, 88]
```

Here, `marks` is a **list**, which is a data structure containing integer values.

---

# Data Representation

## Scalar

A **scalar** is a single value.

```text
5
```

Example:

```python
x = 5
```

```text
Scalar → Single value
```

---

## Vector

A **vector** is a collection of scalar elements.

```text
Vector → Collection of scalar elements
```

### Horizontal Vector

A horizontal vector contains scalar elements arranged horizontally.

```text
[10  20  30]
```

### Vertical Vector

A vertical vector contains scalar elements arranged vertically.

```text
[10]
[20]
[30]
```

---

## Matrix

A **matrix** is a collection of horizontal and vertical vectors arranged in rows and columns.

```text
Matrix → Collection of horizontal and vertical vectors
```

Example:

```text
[1  2  3]
[4  5  6]
[7  8  9]
```

A matrix has **2 dimensions**:

```text
Rows × Columns

3 × 3
```

---

## Tensor

A **tensor** is a collection of matrices and can represent data in more than two dimensions.

```text
Tensor → Collection of matrices
```

Example:

```text
Matrix 1          Matrix 2

[1  2]            [5  6]
[3  4]            [7  8]
```

These two matrices together form a tensor.

In **PyTorch**:

```python
import torch

x = torch.tensor([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(x.shape)
```

Output:

```text
torch.Size([2, 2, 2])
```

---

## Table

A **table** is a collection of matrices used to organize data into rows and columns.

```text
Table → Collection of matrices
```

Example:

```text
        Name     Age     Marks

        Ali      20      85
        Sara     21      90
        John     22      88
```

In practical data science, tables are commonly represented using **Pandas DataFrames**.

---

# Data Structure Hierarchy

A simple way to remember the concepts:

```text
Scalar
   ↓
Vector
   ↓
Matrix
   ↓
Tensor
```

And conceptually:

```text
Scalar
  ↓
Vector → Collection of scalar elements
  ↓
Matrix → Collection of horizontal & vertical vectors
  ↓
Tensor → Collection of matrices
```

For data organization:

```text
Data Type
    ↓
Data Structure
    ↓
Collection of Data Types
```

---

# Python Data Structures

Python provides several built-in data structures for storing and organizing data.

### List

A **list** is an ordered and mutable collection that allows duplicate values.

```python
numbers = [10, 20, 30, 20]
```

### Tuple

A **tuple** is an ordered and immutable collection that allows duplicate values.

```python
numbers = (10, 20, 30, 20)
```

### Set

A **set** is an unordered collection of unique values.

```python
numbers = {10, 20, 30}
```

### Dictionary

A **dictionary** stores data in key-value pairs.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}
```

### Range

A **range** represents a sequence of numbers.

```python
numbers = range(1, 6)
```

Output when converted to a list:

```python
[1, 2, 3, 4, 5]
```

---

## Quick Summary

| Concept               | Definition                                             |
| --------------------- | ------------------------------------------------------ |
| **Data Type**         | Defines the type of a value                            |
| **Data Structure**    | Collection of data types organized in a particular way |
| **Scalar**            | Single value                                           |
| **Vector**            | Collection of scalar elements                          |
| **Horizontal Vector** | Scalar elements arranged horizontally                  |
| **Vertical Vector**   | Scalar elements arranged vertically                    |
| **Matrix**            | Collection of horizontal and vertical vectors          |
| **Tensor**            | Collection of matrices                                 |
| **Table**             | Collection of matrices used to organize data           |
| **List**              | Ordered, mutable collection                            |
| **Tuple**             | Ordered, immutable collection                          |
| **Set**               | Unordered collection of unique values                  |
| **Dictionary**        | Collection of key-value pairs                          |
| **Range**             | Sequence of numbers                                    |
