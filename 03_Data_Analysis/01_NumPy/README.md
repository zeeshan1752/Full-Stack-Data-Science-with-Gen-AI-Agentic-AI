# NumPy

NumPy stands for **Numerical Python**. It is a Python library used for numerical calculations and working with arrays.

NumPy is widely used in:

- Data Analysis
- Data Science
- Machine Learning
- Scientific Computing
- Mathematical Operations

---

## 1. Introduction to NumPy

### What is NumPy?

NumPy provides a special data structure called an **array** and many functions for performing numerical operations.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
```

**Output:**

```text
[10 20 30 40]
```

### Why Use NumPy?

Python lists can store numbers, but NumPy arrays are better suited for numerical calculations.

For example:

```python
import numpy as np

marks = np.array([70, 80, 65, 90])

print(marks + 5)
```

**Output:**

```text
[75 85 70 95]
```

Here, `5` is added to every element without using a loop.

**Real-life example:**  
If we have marks of 100 students, NumPy can help us quickly find the average, highest marks, lowest marks, total marks, and filter students based on their marks.

---

## 2. Installing and Importing NumPy

If NumPy is not installed, we can install it using:

```bash
pip install numpy
```

To use NumPy in a Python program:

```python
import numpy as np
```

`np` is the commonly used short name for NumPy.

### Check NumPy Version

We can check the installed NumPy version using `__version__`.

```python
import numpy as np

print(np.__version__)
```

**Output:**

```text
2.x.x
```

The exact version depends on the version installed on the system.

---

## 3. Python List to NumPy Array

A Python list can be converted into a NumPy array using `np.array()`.

```python
import numpy as np

numbers = [10, 20, 30, 40]

arr = np.array(numbers)

print(arr)
print(type(arr))
```

**Output:**

```text
[10 20 30 40]
<class 'numpy.ndarray'>
```

### 1D Array

A one-dimensional array contains values in a single row.

```python
arr = np.array([10, 20, 30, 40])

print(arr)
```

**Output:**

```text
[10 20 30 40]
```

### 2D Array

A two-dimensional array contains rows and columns.

```python
print(arr)
```

**Output:**

```text
[[10 20]
 [30 40]]
```

**Real-life example:**

A 2D array can represent student marks:

```text
          Maths  Science
Student 1   80      75
Student 2   90      85
```

---

## 4. NumPy Array vs Python List

Python lists and NumPy arrays can both store multiple values, but they are mainly used for different purposes.

Python lists are useful for general-purpose collections, while NumPy arrays are more suitable for numerical calculations.

| Feature | Python List | NumPy Array |
|---|---|---|
| **Type of Elements** | Can store different data types | Generally stores elements of the same data type |
| **Performance** | Slower for large numerical operations | Faster for numerical operations |
| **Memory Efficiency** | Uses more memory for numerical data | More memory efficient for numerical data |
| **Operations** | Element-wise numerical operations generally need loops | Supports vectorized operations |
| **Use Case** | General-purpose collection | Numerical and scientific computations |
| **Methods / Functions** | Built-in methods like `append()`, `extend()`, `remove()` | NumPy functions like `np.mean()`, `np.sum()`, `np.dot()` |

### Example: Element-wise Addition

#### Python List

```python
numbers = [10, 20, 30, 40]

result = []

for number in numbers:
    result.append(number + 5)

print(result)
```

**Output:**

```text
[15, 25, 35, 45]
```

With a Python list, we generally use a loop to perform an operation on every element.

#### NumPy Array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

result = numbers + 5

print(result)
```

**Output:**

```text
[15 25 35 45]
```

Here, NumPy performs the operation directly on all elements. This is called a **vectorized operation**.

### Example: Methods and Functions

Python lists have built-in methods:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

**Output:**

```text
[10, 20, 30, 40]
```

NumPy provides many functions for numerical calculations:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(np.mean(numbers))
print(np.sum(numbers))
print(np.max(numbers))
```

**Output:**

```text
25.0
100
40
```

### In Short

- **Python List** → General-purpose collection.
- **NumPy Array** → Numerical calculations and large numerical datasets.
- **List** → Can contain different data types.
- **NumPy Array** → Generally contains elements of the same data type.
- **List** → Element-wise numerical operations generally require a loop or comprehension.
- **NumPy Array** → Supports vectorized operations.
- **NumPy** → Provides many mathematical and statistical functions.

---

## 5. Array Properties

NumPy provides properties to understand the structure of an array.

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

**Output:**

```text
2
(2, 3)
6
int64
```

> The exact `dtype` can vary depending on the system and the way the array is created.

### Important Properties

| Property | Meaning |
|---|---|
| `ndim` | Number of dimensions |
| `shape` | Number of rows and columns |
| `size` | Total number of elements |
| `dtype` | Data type of elements |

For the above array:

```text
ndim  = 2
shape = (2, 3)
size  = 6
```

---

## 6. Creating NumPy Arrays

NumPy provides different functions for creating arrays.

### `np.array()`

Creates an array from a Python list or other sequence.

```python
arr = np.array([1, 2, 3, 4])

print(arr)
```

**Output:**

```text
[1 2 3 4]
```

### `np.zeros()`

Creates an array filled with zeros.

```python
arr = np.zeros(5)

print(arr)
```

**Output:**

```text
[0. 0. 0. 0. 0.]
```

### `np.ones()`

Creates an array filled with ones.

```python
arr = np.ones(4)

print(arr)
```

**Output:**

```text
[1. 1. 1. 1.]
```

### `np.full()`

Creates an array filled with a specified value.

```python
arr = np.full(5, 10)

print(arr)
```

**Output:**

```text
[10 10 10 10 10]
```

### `np.arange()`

Creates values within a given range.

```python
arr = np.arange(1, 6)

print(arr)
```

**Output:**

```text
[1 2 3 4 5]
```

The syntax is:

```python
np.arange(start, stop, step)
```

Example:

```python
arr = np.arange(2, 11, 2)

print(arr)
```

**Output:**

```text
[ 2  4  6  8 10]
```

### `np.linspace()`

Creates a specified number of equally spaced values.

```python
arr = np.linspace(0, 10, 5)

print(arr)
```

**Output:**

```text
[ 0.   2.5  5.   7.5 10. ]
```

### `np.eye()`

Creates an identity matrix.

```python
arr = np.eye(3)

print(arr)
```

**Output:**

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

**Real-life example:**  
Array creation functions are useful when preparing data, creating test data, generating numerical ranges, or creating matrices for calculations.

---

## 7. Array Indexing and Slicing

Indexing is used to access individual elements of an array.

### 1D Indexing

```python
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])
```

**Output:**

```text
10
30
```

### Negative Indexing

Negative indexing starts from the end of the array.

```python
arr = np.array([10, 20, 30, 40])

print(arr[-1])
print(arr[-2])
```

**Output:**

```text
40
30
```

### 2D Indexing

For a 2D array, we use:

```text
array[row, column]
```

Example:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])
print(arr[1, 2])
```

**Output:**

```text
20
60
```

### Slicing

Slicing is used to select multiple elements.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

**Output:**

```text
[20 30 40]
```

### 2D Slicing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 1:3])
```

**Output:**

```text
[[20 30]
 [50 60]]
```

**Real-life example:**  
If an array contains daily sales for a month, slicing can be used to select sales for a particular week.

---

## 8. Array Data Types

NumPy arrays have a data type called `dtype`.

```python
arr = np.array([10, 20, 30])

print(arr.dtype)
```

**Output:**

```text
int64
```

### Specifying Data Type

We can specify the data type while creating the array.

```python
arr = np.array([10, 20, 30], dtype=float)

print(arr)
print(arr.dtype)
```

**Output:**

```text
[10. 20. 30.]
float64
```

### Changing Data Type Using `astype()`

```python
arr = np.array([10, 20, 30])

new_arr = arr.astype(float)

print(new_arr)
```

**Output:**

```text
[10. 20. 30.]
```

---

## 9. Array Operations

NumPy allows us to perform mathematical operations directly on arrays.

### Addition

```python
arr = np.array([10, 20, 30])

print(arr + 5)
```

**Output:**

```text
[15 25 35]
```

### Multiplication

```python
arr = np.array([10, 20, 30])

print(arr * 2)
```

**Output:**

```text
[20 40 60]
```

### Division

```python
arr = np.array([10, 20, 30])

print(arr / 10)
```

**Output:**

```text
[1. 2. 3.]
```

### Operations Between Arrays

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a * b)
```

**Output:**

```text
[11 22 33]
[10 40 90]
```

NumPy performs the operation element by element.

### Comparison Operations

```python
arr = np.array([10, 20, 30, 40])

print(arr > 20)
```

**Output:**

```text
[False False  True  True]
```

---

## 10. Broadcasting

Broadcasting allows NumPy to perform operations between arrays of compatible shapes.

For example:

```python
arr = np.array([10, 20, 30])

print(arr + 5)
```

**Output:**

```text
[15 25 35]
```

Here, `5` is automatically applied to every element.

### Real-life Example

Suppose the prices of three products are:

```python
prices = np.array([500, 700, 1000])

final_prices = prices + 50

print(final_prices)
```

**Output:**

```text
[ 550  750 1050]
```

Here, ₹50 is added to every product price.

---

## 11. Mathematical Functions

NumPy provides many mathematical functions.

### Square Root

```python
arr = np.array([4, 9, 16, 25])

print(np.sqrt(arr))
```

**Output:**

```text
[2. 3. 4. 5.]
```

### Absolute Value

```python
arr = np.array([-10, 20, -30])

print(np.abs(arr))
```

**Output:**

```text
[10 20 30]
```

### Rounding

```python
arr = np.array([2.345, 5.678])

print(np.round(arr, 2))
```

**Output:**

```text
[2.35 5.68]
```

### Power

```python
arr = np.array([2, 3, 4])

print(np.power(arr, 2))
```

**Output:**

```text
[ 4  9 16]
```

### Common Mathematical Functions

- `np.sqrt()`
- `np.abs()`
- `np.round()`
- `np.power()`
- `np.exp()`
- `np.log()`

---

## 12. Statistical and Aggregation Functions

NumPy provides functions to calculate common statistics.

```python
marks = np.array([70, 80, 65, 90, 85])

print(np.sum(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.min(marks))
print(np.max(marks))
print(np.std(marks))
print(np.var(marks))
```

**Output:**

```text
465
78.0
80.0
65
90
8.717797887081348
76.0
```

### Common Statistical Functions

| Function | Purpose |
|---|---|
| `np.sum()` | Finds the total |
| `np.mean()` | Finds the average |
| `np.median()` | Finds the middle value |
| `np.min()` | Finds the smallest value |
| `np.max()` | Finds the largest value |
| `np.std()` | Finds standard deviation |
| `np.var()` | Finds variance |

### `axis`

`axis` is useful when working with 2D arrays.

```python
marks = np.array([
    [80, 70, 90],
    [60, 85, 75]
])

print(np.sum(marks, axis=0))
print(np.sum(marks, axis=1))
```

**Output:**

```text
[140 155 165]
[240 220]
```

- `axis=0` → works column-wise
- `axis=1` → works row-wise

**Real-life example:**

Suppose rows represent students and columns represent subjects:

```text
          Maths  Science  English
Student 1   80      70       90
Student 2   60      85       75
```

`axis=0` can be used to calculate the total for each subject.

`axis=1` can be used to calculate the total for each student.

---

## 13. Boolean Indexing, Masking and Filtering

Boolean indexing is used to select elements based on a condition.

```python
marks = np.array([45, 67, 89, 32, 76])

print(marks >= 50)
```

**Output:**

```text
[False  True  True False  True]
```

The Boolean array is called a **Boolean mask**.

We can use this mask to filter values:

```python
marks = np.array([45, 67, 89, 32, 76])

result = marks[marks >= 50]

print(result)
```

**Output:**

```text
[67 89 76]
```

### Multiple Conditions

```python
marks = np.array([45, 67, 89, 32, 76])

result = marks[(marks >= 50) & (marks <= 80)]

print(result)
```

**Output:**

```text
[67 76]
```

**Real-life example:**  
From a list of student marks, we can select students who scored between 50 and 80.

---

## 14. `np.where()`

`np.where()` is used to select values or find positions based on a condition.

### Find Positions

```python
marks = np.array([40, 65, 80, 35])

print(np.where(marks >= 50))
```

**Output:**

```text
(array([1, 2]),)
```

The positions `1` and `2` contain values greater than or equal to `50`.

### Select Values

`np.where()` can also select one value when the condition is true and another value when it is false.

```python
marks = np.array([40, 65, 80, 35])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)
```

**Output:**

```text
['Fail' 'Pass' 'Pass' 'Fail']
```

**Real-life example:**  
We can classify students as **Pass** or **Fail** based on their marks.

---

## 15. Array Manipulation

Array manipulation means changing the structure or form of an array.

### `reshape()`

Changes the shape of an array without changing its data.

```python
arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print(new_arr)
```

**Output:**

```text
[[1 2 3]
 [4 5 6]]
```

### `flatten()`

Converts a multidimensional array into a 1D array.

```python
arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.flatten())
```

**Output:**

```text
[1 2 3 4]
```

### `ravel()`

Also converts an array into a 1D form.

```python
print(arr.ravel())
```

**Output:**

```text
[1 2 3 4]
```

### Transpose

Transpose changes rows into columns and columns into rows.

```python
print(arr.T)
```

**Output:**

```text
[[1 3]
 [2 4]]
```

---

## 16. Joining and Splitting Arrays

### `np.concatenate()`

Joins arrays together.

```python
a = np.array([1, 2])
b = np.array([3, 4])

result = np.concatenate((a, b))

print(result)
```

**Output:**

```text
[1 2 3 4]
```

### Other Joining Functions

* `np.concatenate()` – Used to join arrays along an existing axis.
* `np.stack()` – Used to join arrays along a **new axis**.
* `np.hstack()` – Used to join arrays **horizontally (column-wise)**.
* `np.vstack()` – Used to join arrays **vertically (row-wise)**.


### `np.split()`

Splits an array into multiple parts.

```python
arr = np.array([1, 2, 3, 4])

result = np.split(arr, 2)

print(result)
```

**Output:**

```text
[array([1, 2]), array([3, 4])]
```

**Real-life example:**  
Joining can combine data collected from two different sources.

Splitting can divide a large dataset into smaller parts for processing.

---

## 17. Sorting and Searching

### `np.sort()`

Sorts an array.

```python
arr = np.array([40, 10, 30, 20])

print(np.sort(arr))
```

**Output:**

```text
[10 20 30 40]
```

### `np.argsort()`

Returns the indexes that would sort the array.

```python
arr = np.array([40, 10, 30, 20])

print(np.argsort(arr))
```

**Output:**

```text
[1 3 2 0]
```

### `np.unique()`

Finds unique values.

```python
arr = np.array([10, 20, 10, 30, 20])

print(np.unique(arr))
```

**Output:**

```text
[10 20 30]
```

### `np.searchsorted()`

Finds the position where a value can be inserted while keeping the array sorted.

```python
arr = np.array([10, 20, 30, 40])

print(np.searchsorted(arr, 25))
```

**Output:**

```text
2
```

---

## 18. Random Numbers and Sampling

NumPy provides functions for generating random values.

### `np.random.rand()`

Generates random floating-point numbers between `0` and `1`.

```python
np.random.seed(10)

print(np.random.rand(3))
```

**Output:**

```text
[0.77132064 0.02075195 0.63364823]
```

### `np.random.randint()`

Generates random integers.

```python
np.random.seed(10)

print(np.random.randint(1, 10, 5))
```

**Output:**

```text
[5 1 2 1 2]
```

### `np.random.choice()`

Selects random values from an array.

```python
np.random.seed(10)

arr = np.array([10, 20, 30, 40, 50])

print(np.random.choice(arr, 3))
```

**Output:**

```text
[20 50 10]
```

### Random Seed

A seed is used when we want the same random results every time.

```python
np.random.seed(10)

print(np.random.randint(1, 10, 5))
```

**Output:**

```text
[5 1 2 1 2]
```

**Real-life example:**  
Random sampling can be used to select a sample of customers from a large customer dataset for a survey.

---

## 19. Linear Algebra

NumPy provides functions for matrix and linear algebra operations.

### Matrix Multiplication

```python
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(a, b)

print(result)
```

**Output:**

```text
[[19 22]
 [43 50]]
```

### Dot Product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print(result)
```

**Output:**

```text
32
```

### Other Linear Algebra Operations

* **Matrix transpose** – `np.transpose()`
* **Matrix inverse** – `np.linalg.inv()`
* **Determinant** – `np.linalg.det()`
* **Eigenvalues** – `np.linalg.eigvals()`
* **Eigenvectors** – `np.linalg.eig()`


**Real-life example:**  
Linear algebra is used in:

- Machine Learning
- Image Processing
- Recommendation Systems
- Scientific Calculations

---

## 20. Logical and Boolean Functions

NumPy provides functions for checking and combining conditions.

### `np.all()`

Checks whether all values satisfy a condition.

```python
arr = np.array([10, 20, 30])

print(np.all(arr > 0))
```

**Output:**

```text
True
```

### `np.any()`

Checks whether at least one value satisfies a condition.

```python
arr = np.array([10, 20, 30])

print(np.any(arr > 25))
```

**Output:**

```text
True
```

### `np.logical_and()`

Performs logical AND between two Boolean arrays.

```python
a = np.array([True, True, False])
b = np.array([True, False, True])

print(np.logical_and(a, b))
```

**Output:**

```text
[ True False False]
```

### Other Logical Functions

- `np.logical_and()`
- `np.logical_or()`
- `np.logical_not()`

---

## 21. Set Operations

NumPy provides functions for performing set-like operations on arrays.

```python
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])
```

### Union

Returns all unique values from both arrays.

```python
print(np.union1d(a, b))
```

**Output:**

```text
[1 2 3 4 5 6]
```

### Intersection

Returns values that are present in both arrays.

```python
print(np.intersect1d(a, b))
```

**Output:**

```text
[3 4]
```

### Difference

Returns values that are present in the first array but not in the second array.

```python
print(np.setdiff1d(a, b))
```

**Output:**

```text
[1 2]
```

**Real-life example:**  
Set operations can be used to compare customer lists.

For example:

- Union → All customers from two lists
- Intersection → Customers common to both lists
- Difference → Customers present in one list but not the other

---

## 22. Handling Missing and Special Values

NumPy provides special values such as `np.nan` and `np.inf`.

### `np.nan`

`np.nan` represents a missing or undefined numerical value.

```python
arr = np.array([10, 20, np.nan, 40])

print(np.isnan(arr))
```

**Output:**

```text
[False False  True False]
```

### `np.inf`

`np.inf` represents infinity.

```python
arr = np.array([10, np.inf, 30])

print(arr)
```

**Output:**

```text
[10. inf 30.]
```

### `np.isfinite()`

Checks whether values are finite.

```python
arr = np.array([10, np.nan, np.inf, 40])

print(np.isfinite(arr))
```

**Output:**

```text
[ True False False  True]
```

### Common Functions

* `np.isnan()` – Used to **check for NaN (Not a Number) values**.
* `np.isinf()` – Used to **check for infinite (`∞` or `-∞`) values**.
* `np.isfinite()` – Used to **check whether values are finite (not NaN or infinity)**.


**Real-life example:**  
When working with real-world datasets, some values may be missing or invalid. These functions help identify such values before analysis.

---

## 23. Copy and View

NumPy arrays can be copied or viewed.

### Copy

A copy creates a separate array. Changes made to the copy do not affect the original array.

```python
arr = np.array([10, 20, 30])

copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)
print(copy_arr)
```

**Output:**

```text
[10 20 30]
[100  20  30]
```

### View

A view shares the same underlying data. Changes made to the view can affect the original array.

```python
arr = np.array([10, 20, 30])

view_arr = arr.view()

view_arr[0] = 100

print(arr)
print(view_arr)
```

**Output:**

```text
[100  20  30]
[100  20  30]
```

### Difference

| Copy | View |
|---|---|
| Creates a separate array | Shares data with the original |
| Changes do not affect the original | Changes can affect the original |
| Uses separate memory | Shares underlying data |

---

## Parameter Tuning and Hyperparameter Tuning

### Parameter Tuning

When NumPy uses the default data type automatically.

**Example:**

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr.dtype)
````

**Output:**

```text
int64
```

### Hyperparameter Tuning

When the user explicitly changes the data type using the `dtype` parameter.

**Example:**

```python
import numpy as np

arr = np.array([10, 20, 30], dtype=float)

print(arr.dtype)
```

**Output:**

```text
float64
```

### Easy Difference

**Default data type selected by NumPy → Parameter**

**Data type explicitly changed by the user → Hyperparameter**

> **Note:** This is a simplified terminology used in this NumPy context. In standard machine learning terminology, parameters are values learned by the model, while hyperparameters are settings chosen by the user.

---

## 25. NumPy in Data Analysis

NumPy is one of the important libraries used in Data Analysis.

A simple data analysis workflow can be:

```text
Collect Data
     ↓
Store Data
     ↓
Convert Data to NumPy Array
     ↓
Clean / Filter Data
     ↓
Perform Calculations
     ↓
Analyse Results
     ↓
Visualise Results
```

### Example: Sales Data

Suppose a shop has the following sales for five days:

```python
import numpy as np

sales = np.array([1200, 1500, 1100, 1800, 2000])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))
```

**Output:**

```text
Total Sales: 7600
Average Sales: 1520.0
Highest Sales: 2000
Lowest Sales: 1100
```

### Real-life Example

The sales data represents:

```text
Monday     → ₹1200
Tuesday    → ₹1500
Wednesday  → ₹1100
Thursday   → ₹1800
Friday     → ₹2000
```

Using NumPy, we can quickly:

- Calculate total sales
- Calculate average sales
- Find the highest sales
- Find the lowest sales
- Filter sales
- Perform mathematical calculations

NumPy is commonly used together with:

- **Pandas** → Working with tabular data
- **Matplotlib** → Data visualisation
- **Scikit-learn** → Machine Learning

---

## 26. Quick Reference

| Task | NumPy Function |
|---|---|
| Create array | `np.array()` |
| Create zeros | `np.zeros()` |
| Create ones | `np.ones()` |
| Create fixed values | `np.full()` |
| Create range | `np.arange()` |
| Create equally spaced values | `np.linspace()` |
| Create identity matrix | `np.eye()` |
| Reshape array | `reshape()` |
| Flatten array | `flatten()` |
| Convert to 1D | `ravel()` |
| Transpose | `.T` |
| Sort values | `np.sort()` |
| Get sorting indexes | `np.argsort()` |
| Get unique values | `np.unique()` |
| Find insertion position | `np.searchsorted()` |
| Find total | `np.sum()` |
| Find average | `np.mean()` |
| Find median | `np.median()` |
| Find minimum | `np.min()` |
| Find maximum | `np.max()` |
| Find standard deviation | `np.std()` |
| Find variance | `np.var()` |
| Filter values | Boolean indexing |
| Conditional selection | `np.where()` |
| Random float | `np.random.rand()` |
| Random integer | `np.random.randint()` |
| Random sample | `np.random.choice()` |
| Combine arrays | `np.concatenate()` |
| Split arrays | `np.split()` |
| Matrix multiplication | `np.matmul()` |
| Dot product | `np.dot()` |
| Union | `np.union1d()` |
| Intersection | `np.intersect1d()` |
| Difference | `np.setdiff1d()` |
| Check NaN | `np.isnan()` |
| Check infinity | `np.isinf()` |
| Check finite values | `np.isfinite()` |
| Create copy | `.copy()` |
| Create view | `.view()` |

---

## Summary

NumPy is an important Python library for numerical calculations and array-based operations.

The main concepts covered are:

1. Introduction to NumPy
2. Installing and importing NumPy
3. Python list to NumPy array
4. NumPy array vs Python list
5. Array properties
6. Creating NumPy arrays
7. Array indexing and slicing
8. Array data types
9. Array operations
10. Broadcasting
11. Mathematical functions
12. Statistical and aggregation functions
13. Boolean indexing, masking and filtering
14. `np.where()`
15. Array manipulation
16. Joining and splitting arrays
17. Sorting and searching
18. Random numbers and sampling
19. Linear algebra
20. Logical and Boolean functions
21. Set operations
22. Handling missing and special values
23. Copy and view
24. Parameters and hyperparameters tuning
25. NumPy in Data Analysis
26. Quick reference