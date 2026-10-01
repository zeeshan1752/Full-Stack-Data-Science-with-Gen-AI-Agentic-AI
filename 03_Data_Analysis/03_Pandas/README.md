# Pandas

Pandas is a Python library used for **data analysis and data manipulation**.

It provides powerful data structures such as:

- Series
- DataFrame

Pandas is commonly used for:

- Reading and writing data
- Cleaning data
- Analysing data
- Filtering data
- Transforming data
- Grouping data
- Merging datasets
- Reshaping data
- Working with dates and time
- Preparing data for Machine Learning


## Topics Covered

- **Basics:** installation, importing Pandas, Series, DataFrames, creating data, and common attributes.
- **Inspecting and importing data:** `head()`, `tail()`, `sample()`, `info()`, `describe()`, CSV and Excel parameter tables, JSON, and SQL.
- **Selecting and changing data:** columns, rows, `loc[]`, `iloc[]`, `at[]`, `iat[]`, Boolean filtering, adding, updating, renaming, inserting, and removing data.
- **Indexes and sorting:** setting, resetting, reindexing, sorting, and removing duplicate data.
- **Cleaning data:** missing values, replacing values, data types, numeric conversion, and string operations.
- **Analysis:** arithmetic, comparisons, descriptive statistics, unique values, ranking, sampling, and applying functions.
- **Grouping and combining:** `groupby()`, aggregation, transformation, filtering, `concat()`, `merge()`, and `join()`.
- **Reshaping:** `pivot()`, `pivot_table()`, `melt()`, and `explode()`.
- **Dates and time series:** date conversion, date ranges, date components, formatting, resampling, rolling calculations, and cumulative operations.
- **Practical data work:** large files, Parquet, NumPy integration, `get_dummies()`, data cleaning, data analysis, and preparing data for Machine Learning.

---
# 1. Introduction to Pandas

## What is Pandas?

**Pandas** is an open-source Python library used for working with structured and tabular data.

It provides easy-to-use data structures and functions for data analysis.

Pandas is built on top of Python and works closely with NumPy.

---

## Why use Pandas?

Pandas helps us to:

* Read data from different file formats
* Store data in tables
* Select rows and columns
* Filter data
* Clean missing values
* Remove duplicate data
* Sort data
* Group data
* Combine multiple datasets
* Reshape data
* Analyse numerical data
* Work with text data
* Work with dates and time
* Prepare data for Machine Learning

---

# 2. Installing Pandas

Pandas can be installed using:

```bash
pip install pandas
```

To install or upgrade Pandas:

```bash
pip install --upgrade pandas
```

---

# 3. Importing Pandas

The commonly used import statement is:

```python
import pandas as pd
```

Here:

```text
pd
```

is the commonly used alias for Pandas.

Example:

```python
import pandas as pd

print(pd.__version__)
```

Output:

```text
3.x.x  # Depends on your installed Pandas version
```

---

# 4. Pandas Data Structures

Pandas mainly provides two important data structures:

1. Series
2. DataFrame

---

# 5. Series

A **Series** is a one-dimensional labelled data structure.

It can contain:

* Numbers
* Strings
* Boolean values
* Dates
* Other Python objects

Example:

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

The left side contains the index and the right side contains the values.

---

## Creating Series with Custom Index

```python
data = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

print(data)
```

Output:

```text
a    10
b    20
c    30
dtype: int64
```

---

## Accessing Series Values

```python
print(data["a"])
```

Output:

```text
10
```

Using position:

```python
print(data.iloc[0])
```

Output:

```text
10
```

---

## Series from Dictionary

```python
data = {
    "Maths": 90,
    "Python": 95,
    "DBMS": 88
}

series = pd.Series(data)

print(series)
```

Output:

```text
Maths     90
Python    95
DBMS      88
dtype: int64
```

---

# 6. DataFrame

A **DataFrame** is a two-dimensional labelled data structure.

It is similar to a table containing:

* Rows
* Columns
* Index

Example:

```python
data = {
    "Name": ["Aman", "Riya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age  Marks
0   Aman   21     85
1   Riya   22     90
2  Rahul   20     78
```

---

## DataFrame Structure

```text
        Name  Age  Marks
0       Aman   21     85
1       Riya   22     90
2      Rahul   20     78
```

---

# 7. Creating DataFrame

## From Dictionary

```python
data = {
    "Name": ["Aman", "Riya"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)
```

---

## From List of Lists

```python
data = [
    ["Aman", 21],
    ["Riya", 22]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age"]
)

print(df)
```

Output:

```text
   Name  Age
0  Aman   21
1  Riya   22
```

---

## From List of Dictionaries

```python
data = [
    {"Name": "Aman", "Age": 21},
    {"Name": "Riya", "Age": 22}
]

df = pd.DataFrame(data)

print(df)
```

Output:

```text
   Name  Age
0  Aman   21
1  Riya   22
```

---

## Creating an Empty DataFrame

```python
df = pd.DataFrame()

print(df)
```

Output:

```text
Empty DataFrame
Columns: []
Index: []
```

---


## Reusable Example DataFrame

Most examples in this README use the following small DataFrame. Using the same data makes it easier to understand what each Pandas method does.

```python
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Arjun", "Sara"],
    "Age": [21, 22, 20, 21, 23, 22],
    "Marks": [85, 92, 78, 88, 95, 76],
    "City": ["Lucknow", "Delhi", "Lucknow", "Mumbai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```text
    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
5   Sara   22     76   Mumbai
```

We will reuse this `df` in many examples below.

# 8. DataFrame Attributes

Some commonly used DataFrame attributes are:

```python
df.shape
df.columns
df.index
df.dtypes
df.size
df.ndim
```

Example:

```python
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
```

Output:

```text
(6, 4)
Index(['Name', 'Age', 'Marks', 'City'], dtype='object')
RangeIndex(start=0, stop=6, step=1)
Name     object
Age       int64
Marks     int64
City     object
dtype: object
```

---

# 9. Viewing Data

## `head()`

Displays the first rows.

```python
df.head()
```

By default, it displays the first 5 rows.

We can specify the number:

```python
df.head(10)
```

---

### Example: `head()`

`df.head()` shows the first 5 rows by default.

```python
print(df.head())
```

Output:

```text
    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
```

So, `head()` means **show the top rows**. `df.head(3)` would show only the first 3 rows.

## `tail()`

Displays the last rows.

```python
df.tail()
```

Example:

```python
df.tail(3)
```

---

### Example: `tail()`

`df.tail()` shows the last 5 rows.

```python
print(df.tail())
```

Output:

```text
    Name  Age  Marks     City
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
5   Sara   22     76   Mumbai
```

So, `tail()` means **show the bottom rows**.

## `sample()`

Returns random rows.

```python
df.sample(5)
```

---

### Example: `sample()`

`sample()` returns random rows, so the exact output can change each time.

```python
print(df.sample(2))
```

Possible output:

```text
    Name  Age  Marks     City
4  Arjun   23     95    Delhi
1   Riya   22     92    Delhi
```

The important point is that the rows are selected randomly.

## `info()`

Displays information about the DataFrame.

```python
df.info()
```

It can show:

* Number of rows
* Columns
* Non-null values
* Data types
* Memory usage

---

### Example: `info()`

```python
df.info()
```

Output:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    6 non-null      object
 1   Age     6 non-null      int64
 2   Marks   6 non-null      int64
 3   City    6 non-null      object
```

`info()` helps us quickly understand the **number of rows, columns, missing values and data types**.

## `describe()`

Provides descriptive statistics.

```python
df.describe()
```

It commonly gives:

* Count
* Mean
* Standard deviation
* Minimum
* Quartiles
* Maximum

---

### Example: `describe()`

```python
print(df.describe())
```

Output:

```text
             Age      Marks
count   6.000000   6.000000
mean   21.500000  85.666667
min    20.000000  76.000000
max    23.000000  95.000000
```

The actual display also contains quartiles and standard deviation. The important idea is that `describe()` gives a quick statistical summary of numeric columns.

### Important Parameter Options

| Method / parameter | Common values | Effect |
|---|---|---|
| `head(n)` / `tail(n)` | `n=5`, `n=10`, any non-negative integer | Number of first or last rows to return; default is `5`. |
| `sample(n=...)` | `n=1`, `n=2`, any valid row count | Number of randomly selected rows. |
| `sample(frac=...)` | `frac=0.1`, `frac=0.5`, `frac=1` | Selects a fraction of rows instead of a fixed count. |
| `sample(random_state=...)` | An integer such as `42` | Makes random sampling reproducible. |
| `describe(include=...)` | `"all"`, `"number"`, or a data type | Controls which columns are summarized. |

# 10. Reading CSV Files

Use `pd.read_csv()` to load a CSV file. Refer to the parameters below instead of memorising separate examples.

| Parameter | Use |
|---|---|
| `sep` | Specify the delimiter, such as `","`, `";"`, or `"	"`. |
| `header` | Choose the row containing column names; use `None` when there is no header. |
| `names` | Provide column names manually. |
| `usecols` | Read only selected columns. |
| `index_col` | Set a column as the DataFrame index. |
| `dtype` | Set data types for columns. |
| `na_values` | Treat selected values as missing values. |
| `nrows` | Read only a specified number of rows. |
| `skiprows` | Skip selected rows. |
| `chunksize` | Read a large file in smaller chunks. |

```python
df = pd.read_csv("data.csv", usecols=["Name", "Age"])
print(df.head())
```

Output depends on the contents of `data.csv`.

---

# 11. Writing CSV Files

Use `df.to_csv()` to save a DataFrame as a CSV file.

| Parameter | Use |
|---|---|
| `index` | Include or exclude the row index; use `False` to exclude it. |
| `columns` | Save only selected columns. |
| `sep` | Choose the delimiter used in the file. |
| `header` | Include column names or provide custom names. |
| `na_rep` | Choose text to write for missing values. |
| `encoding` | Set the file encoding, commonly `"utf-8"`. |

```python
df.to_csv("output.csv", index=False)
```

---

# 12. Reading Excel Files

Use `pd.read_excel()` to load an Excel workbook.

| Parameter | Use |
|---|---|
| `sheet_name` | Select a sheet by name or position; use `None` to read all sheets. |
| `usecols` | Read only selected columns. |
| `header` | Choose the row containing column names; use `None` if there is no header. |
| `skiprows` | Skip rows at the beginning or selected row positions. |
| `dtype` | Set data types for columns where supported. |
| `nrows` | Limit the number of rows to read. |

```python
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
print(df.head())
```

Output depends on the contents of `data.xlsx`.

---

# 13. Writing Excel Files

Use `df.to_excel()` to save a DataFrame as an Excel file.

| Parameter | Use |
|---|---|
| `sheet_name` | Choose the worksheet name. |
| `index` | Include or exclude the DataFrame index. |
| `columns` | Save only selected columns. |
| `header` | Include or customise column names. |
| `na_rep` | Choose text to write for missing values. |

```python
df.to_excel("output.xlsx", sheet_name="Data", index=False)
```

To write multiple sheets, use `pd.ExcelWriter()`.

---

# 14. Reading JSON

JSON data can be read using:

```python
df = pd.read_json("data.json")

print(df)
```

Output:

```text
Output depends on the contents of data.json.
```

---

## Writing JSON

```python
df.to_json("output.json")
```

---

# 15. Reading SQL Data

Pandas can work with SQL databases.

Example:

```python
df = pd.read_sql(
    "SELECT * FROM students",
    connection
)
```

---

# 16. Selecting Columns

Select one column:

```python
df["Name"]
```

Select multiple columns:

```python
df[["Name", "Age"]]
```

---

### Important Selection Notes

| Syntax | Result |
|---|---|
| `df["Name"]` | Returns one column as a Series. |
| `df[["Name", "Age"]]` | Returns selected columns as a DataFrame. |
| `df.loc[:, ["Name", "Age"]]` | Selects columns by their labels. |
| `df.iloc[:, 0:2]` | Selects columns by integer positions; the stop position is excluded. |

# 17. Selecting Rows

Rows can be selected using:

* `loc[]`
* `iloc[]`
* Boolean conditions

---

# 18. `loc[]`

`loc[]` is used mainly for label-based selection.

```python
df.loc[0]
```

Select a particular value:

```python
df.loc[0, "Name"]
```

Select multiple rows:

```python
df.loc[0:2]
```

Select specific rows and columns:

```python
df.loc[0:2, ["Name", "Age"]]
```

---
### Example: `loc[]`

Suppose we want the row whose label is `0`:

```python
print(df.loc[0])
```

Output:

```text
Name         Aman
Age             21
Marks           85
City       Lucknow
Name: 0, dtype: object
```

Selecting one value:

```python
print(df.loc[0, "Name"])
```

Output:

```text
Aman
```

`loc[]` mainly works with **labels**.

# 19. `iloc[]`

`iloc[]` is used for position-based selection.

```python
df.iloc[0]
```

Select a particular value:

```python
df.iloc[0, 1]
```

Select rows:

```python
df.iloc[0:3]
```

Select rows and columns:

```python
df.iloc[0:3, 0:2]
```

---
### Example: `iloc[]`

`iloc[]` selects using row and column positions.

```python
print(df.iloc[0, 1])
```

Output:

```text
21
```

Row `0`, column `1` means the value in the first row and second column.

```python
print(df.iloc[0:3, 0:2])
```

Output:

```text
    Name  Age
0   Aman   21
1   Riya   22
2  Rahul   20
```

`iloc[]` mainly works with **integer positions**.

# 20. `at[]` and `iat[]`

`at[]` is used for fast access to a single value by label.

```python
df.at[0, "Name"]
```

`iat[]` is used for fast access to a single value by position.

```python
df.iat[0, 1]
```

---
### Example: `at[]` and `iat[]`

```python
print(df.at[0, "Name"])
print(df.iat[0, 1])
```

Output:

```text
Aman
21
```

`at[]` uses labels, while `iat[]` uses positions. Both are useful when accessing one value.

# 21. Boolean Indexing

Boolean indexing is used to filter data.

```python
result = df[df["Age"] > 20]

print(result)
```

Output:

```text
    Name  Age  Marks   City
1   Riya   22     92  Delhi
3  Arjun   23     95  Delhi
4   Sara   22     76  Mumbai
```

Multiple conditions:

```python
result = df[
    (df["Age"] > 20) &
    (df["Marks"] > 80)
]
```

OR condition:

```python
result = df[
    (df["Age"] > 20) |
    (df["Marks"] > 80)
]
```

---
### Example: Boolean Indexing

```python
result = df[df["Marks"] > 80]
print(result)
```

Output:

```text
    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
```

The condition `df["Marks"] > 80` creates `True`/`False` values, and Pandas keeps only the rows where the result is `True`.

### Important Boolean Indexing Notes

| Operator / method | Effect |
|---|---|
| `&` | Combines conditions with AND; put each condition in parentheses. |
| `|` | Combines conditions with OR; put each condition in parentheses. |
| `~` | Reverses a Boolean condition. |
| `.isin([...])` | Checks whether values match any value in a collection. |
| `.between(left, right)` | Checks whether values fall within a range; `inclusive` controls boundary handling. |

# 22. `isin()`

`isin()` checks whether values belong to a given collection.

```python
result = df[
    df["City"].isin(["Delhi", "Lucknow"])
]
```

---
### Example: `isin()`

```python
result = df[df["City"].isin(["Delhi", "Lucknow"])]
print(result)
```

Output:

```text
    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
4  Arjun   23     95    Delhi
```

`isin()` checks whether each value belongs to the given list.

# 23. `query()`

The `query()` method can be used to filter rows.

```python
result = df.query("Age > 20")
```

Multiple conditions:

```python
result = df.query(
    "Age > 20 and Marks > 80"
)
```

---
### Example: `query()`

```python
result = df.query("Age > 21")
print(result)
```

Output:

```text
    Name  Age  Marks    City
1   Riya   22     92   Delhi
4  Arjun   23     95   Delhi
5   Sara   22     76  Mumbai
```

`query()` lets us write the filtering condition as a readable string.

# 24. Adding Columns

A new column can be added directly.

```python
df["Salary"] = 30000
```

Column based on another column:

```python
df["Bonus"] = df["Salary"] * 0.10
```

---
### Example: Adding Columns

```python
df["Bonus"] = df["Marks"] + 5
print(df[["Name", "Marks", "Bonus"]])
```

Output:

```text
    Name  Marks  Bonus
0   Aman     85     90
1   Riya     92     97
2  Rahul     78     83
3   Neha     88     93
4  Arjun     95    100
5   Sara     76     81
```

A new column is created by assigning values to `df["Column_Name"]`.

# 25. Updating Columns

```python
df["Age"] = df["Age"] + 1
```

---
### Example: Updating Columns

```python
df["Age"] = df["Age"] + 1
print(df[["Name", "Age"]])
```

Output:

```text
    Name  Age
0   Aman   22
1   Riya   23
2  Rahul   21
3   Neha   22
4  Arjun   24
5   Sara   23
```

Every value in the `Age` column is increased by `1`.

# 26. Renaming Columns

Rename selected columns:

```python
df = df.rename(
    columns={
        "Name": "Student_Name"
    }
)
```

Rename all columns:

```python
df.columns = [
    "Student_Name",
    "Age",
    "Marks",
    "City"
]
```

---
### Example: Renaming Columns

```python
result = df.rename(columns={"Marks": "Score"})
print(result.head(3))
```

Output:

```text
    Name  Age  Score     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
```

Only the column name changes; the data remains the same.

# 27. Removing Columns

Remove one column:

```python
df = df.drop(
    "Age",
    axis=1
)
```

Remove multiple columns:

```python
df = df.drop(
    ["Age", "Marks"],
    axis=1
)
```

`columns=` can also be used:

```python
df = df.drop(
    columns=["Age"]
)
```

---
### Example: Removing Columns

```python
result = df.drop(columns=["Age"])
print(result.head(3))
```

Output:

```text
    Name  Marks     City
0   Aman     85  Lucknow
1   Riya     92    Delhi
2  Rahul     78  Lucknow
```

`axis=1` or `columns=[...]` means we are removing **columns**.

# 28. Removing Rows

Remove a row by index:

```python
df = df.drop(0)
```

Remove multiple rows:

```python
df = df.drop([0, 2])
```

---
### Example: Removing Rows

```python
result = df.drop(0)
print(result.head(3))
```

Output:

```text
    Name  Age  Marks     City
1   Riya   22     92    Delhi
2  Rahul   20     78  Lucknow
3   Neha   21     88   Mumbai
```

Row `0` is removed and the remaining index labels are kept.

# 29. Inserting Columns

A column can be inserted at a specific position.

```python
df.insert(
    1,
    "Country",
    ["India"] * len(df)
)
```

---
### Example: Inserting a Column

```python
result = df.copy()

result.insert(
    1,
    "City",
    result.pop("City")
)

print(result.head(3))
```

Output:

```text
    Name     City  Age  Marks
0   Aman  Lucknow   21     85
1   Riya    Delhi   22     92
2  Rahul  Lucknow   20     78
```

`insert(position, name, values)` places a column at a specific position.

# 30. Reindexing

`reindex()` changes the index or column order.

```python
df = df.reindex(
    [2, 0, 1]
)
```

Column reindexing:

```python
df = df.reindex(
    columns=["Name", "Marks", "Age"]
)
```

---

# 31. Resetting Index

```python
df = df.reset_index()
```

To remove the old index:

```python
df = df.reset_index(drop=True)
```

---

# 32. Sorting Data

Sort by one column:

```python
df.sort_values(
    "Age"
)
```

Descending order:

```python
df.sort_values(
    "Age",
    ascending=False
)
```

Sort by multiple columns:

```python
df.sort_values(
    ["City", "Age"]
)
```

---
### Example: Sorting Data

```python
result = df.sort_values("Marks", ascending=False)
print(result)
```

Output:

```text
    Name  Age  Marks     City
4  Arjun   23     95    Delhi
1   Riya   22     92    Delhi
3   Neha   21     88   Mumbai
0   Aman   21     85  Lucknow
2  Rahul   20     78  Lucknow
5   Sara   22     76   Mumbai
```

`ascending=False` means highest values come first.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `by` | A column name or list of column names | Specifies which column(s) to sort by. |
| `ascending` | `True`, `False`, or a list of booleans | Sorts low-to-high or high-to-low. |
| `na_position` | `"last"`, `"first"` | Places missing values at the end or beginning. |
| `kind` | `"stable"`, `"mergesort"`, `"quicksort"`, `"heapsort"` where supported | Chooses the sorting algorithm. |
| `ignore_index` | `True`, `False` | Resets the result index when enabled. |

# 33. Duplicate Data

Check duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

Duplicates based on selected columns:

```python
df = df.drop_duplicates(
    subset=["Name"]
)
```

---
### Example: Duplicate Data

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Aman"],
    "Marks": [85, 92, 85]
})

print(data.duplicated())
```

Output:

```text
0    False
1    False
2     True
dtype: bool
```

The third row is a duplicate of the first row, so it returns `True`.

# 34. Missing Data

Missing values are common in real-world datasets.

Pandas can represent missing values using values such as:

* `NaN`
* `NaT`
* `pd.NA`
* `None`

---

# 35. Detecting Missing Values

```python
df.isna()
```

or:

```python
df.isnull()
```

Count missing values:

```python
df.isna().sum()
```

---
### Example: Detecting Missing Values

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul"],
    "Marks": [85, None, 78]
})

print(data.isna())
print(data.isna().sum())
```

Output:

```text
    Name  Marks
0  False  False
1  False   True
2  False  False

Name     0
Marks    1
dtype: int64
```

The `Marks` column contains one missing value.

### Important Missing-Value Options

| Method / parameter | Common values | Effect |
|---|---|---|
| `isna()` / `isnull()` | No required parameter | Marks missing values as `True`. |
| `notna()` / `notnull()` | No required parameter | Marks non-missing values as `True`. |
| `sum()` after `isna()` | `df.isna().sum()` | Counts missing values in each column. |

# 36. Dropping Missing Values

Remove rows containing missing values:

```python
df.dropna()
```

Remove columns containing missing values:

```python
df.dropna(axis=1)
```

---
### Example: Dropping Missing Values

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul"],
    "Marks": [85, None, 78]
})

print(data.dropna())
```

Output:

```text
    Name  Marks
0   Aman   85.0
2  Rahul   78.0
```

The row containing the missing value is removed.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `axis` | `0` / `"index"`, `1` / `"columns"` | Checks rows or columns for missing values. |
| `how` | `"any"`, `"all"` | Drops a row/column if any or all selected values are missing. |
| `subset` | A list of column names | Checks missing values only in selected columns. |
| `thresh` | An integer | Requires at least this many non-missing values to keep a row/column. |

# 37. Filling Missing Values

Fill missing values with zero:

```python
df.fillna(0)
```

Fill a column with its mean:

```python
df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)
```

Forward fill:

```python
df.ffill()
```

Backward fill:

```python
df.bfill()
```

---
### Example: Filling Missing Values

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul"],
    "Marks": [85, None, 78]
})

data["Marks"] = data["Marks"].fillna(0)
print(data)
```

Output:

```text
    Name  Marks
0   Aman   85.0
1   Riya    0.0
2  Rahul   78.0
```

`fillna(0)` replaces missing values with `0`.

### Important Parameter Options

| Parameter / method | Common values | Effect |
|---|---|---|
| `value` in `fillna()` | `0`, `"Unknown"`, a dictionary | Replaces missing values with a fixed value or per-column values. |
| `method` in older examples | `"ffill"`, `"bfill"` | Forward-fills or backward-fills missing values; current code can use `.ffill()` or `.bfill()`. |
| `limit` | A positive integer | Limits how many consecutive missing values are filled. |
| `inplace` | `True`, `False` where supported | Requests mutation of the existing object instead of returning a new result. |

# 38. Replacing Values

```python
df["Gender"] = df["Gender"].replace(
    {
        "M": "Male",
        "F": "Female"
    }
)
```

---
### Example: Replacing Values

```python
data = pd.DataFrame({
    "Gender": ["M", "F", "M"]
})

data["Gender"] = data["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

print(data)
```

Output:

```text
   Gender
0    Male
1  Female
2    Male
```

# 39. Data Types

Check data types:

```python
df.dtypes
```

Common data types include:

* Integer
* Float
* Boolean
* String
* Datetime
* Category

---
### Example: Data Types

```python
print(df.dtypes)
```

Output:

```text
Name     object
Age       int64
Marks     int64
City     object
dtype: object
```

`dtypes` tells us the type of data stored in each column.

# 40. Changing Data Types

Use `astype()`:

```python
df["Age"] = df["Age"].astype(int)
```

Convert to string:

```python
df["Name"] = df["Name"].astype(str)
```

---
### Example: `astype()`

```python
data = pd.DataFrame({"Age": ["21", "22", "23"]})

data["Age"] = data["Age"].astype(int)

print(data)
print(data.dtypes)
```

Output:

```text
   Age
0   21
1   22
2   23

Age    int64
dtype: object
```

The values change from strings to integers.

# 41. Numeric Conversion

`to_numeric()` converts values to numeric data.

```python
df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values to missing values.

---
### Example: `to_numeric()`

```python
data = pd.DataFrame({
    "Marks": ["85", "90", "abc"]
})

data["Marks"] = pd.to_numeric(
    data["Marks"],
    errors="coerce"
)

print(data)
```

Output:

```text
   Marks
0   85.0
1   90.0
2    NaN
```

Because `"abc"` is not numeric, `errors="coerce"` converts it to `NaN`.

# 42. String Data

Pandas provides vectorized string operations through `.str`.

```python
df["Name"].str.upper()
```

Convert to lowercase:

```python
df["Name"].str.lower()
```

Remove spaces:

```python
df["Name"].str.strip()
```

Find string length:

```python
df["Name"].str.len()
```

---
### Example: String Operations

```python
print(df["Name"].str.upper())
```

Output:

```text
0     AMAN
1     RIYA
2    RAHUL
3     NEHA
4    ARJUN
5     SARA
Name: Name, dtype: object
```

`.str` lets us apply string operations to an entire Series.

# 43. String Methods

Some commonly used methods are:

```python
.str.upper()
.str.lower()
.str.title()
.str.strip()
.str.replace()
.str.contains()
.str.startswith()
.str.endswith()
.str.split()
.str.len()
.str.find()
```

---
### Example: Common String Methods

```python
print(df["Name"].str.lower())
print(df["Name"].str.len())
```

Output:

```text
0     aman
1     riya
2    rahul
3     neha
4    arjun
5     sara
Name: Name, dtype: object

0    4
1    4
2    5
3    4
4    5
5    4
Name: Name, dtype: int64
```

# 44. Splitting Strings

```python
df["Full_Name"].str.split(" ")
```

Extract first part:

```python
df["Full_Name"].str.split(
    " "
).str[0]
```

---
### Example: Splitting Strings

```python
data = pd.DataFrame({
    "Full_Name": ["Aman Khan", "Riya Sharma"]
})

print(data["Full_Name"].str.split(" "))
print(data["Full_Name"].str.split(" ").str[0])
```

Output:

```text
0       [Aman, Khan]
1    [Riya, Sharma]
Name: Full_Name, dtype: object

0    Aman
1    Riya
Name: Full_Name, dtype: object
```

The first expression creates lists; `.str[0]` gets the first item from each list.

# 45. String Matching

Check whether text contains a value:

```python
df[
    df["Name"].str.contains(
        "Aman",
        na=False
    )
]
```

---
### Example: String Matching

```python
result = df[df["Name"].str.contains("Aman")]
print(result)
```

Output:

```text
   Name  Age  Marks     City
0  Aman   21     85  Lucknow
```

`str.contains()` returns rows where the text contains the specified value.

# 46. Extracting Text

Regular expressions can be used with `.str.extract()`.

```python
df["Email"].str.extract(
    r"(@.*)"
)
```

---

# 47. Vectorized Operations

Pandas performs many operations directly on columns.

```python
df["Total"] = (
    df["Maths"] +
    df["Python"] +
    df["DBMS"]
)
```

This is generally preferred over manually looping through every row.

---
### Example: Vectorized Operation

```python
data = pd.DataFrame({
    "Maths": [80, 90, 70],
    "Python": [85, 95, 75]
})

data["Total"] = data["Maths"] + data["Python"]

print(data)
```

Output:

```text
   Maths  Python  Total
0     80      85    165
1     90      95    185
2     70      75    145
```

Pandas performs the operation on the whole columns without writing a loop.

# 48. Arithmetic Operations

```python
df["Marks"] + 5
df["Marks"] - 5
df["Marks"] * 2
df["Marks"] / 2
```

---
### Example: Arithmetic Operations

```python
print(df["Marks"] + 5)
```

Output:

```text
0     90
1     97
2     83
3     93
4    100
5     81
Name: Marks, dtype: int64
```

The same idea works with `-`, `*`, and `/`.

# 49. Comparison Operations

```python
df["Marks"] > 80
df["Marks"] >= 80
df["Marks"] < 40
df["Marks"] == 90
```

---
### Example: Comparison

```python
print(df["Marks"] > 80)
```

Output:

```text
0     True
1     True
2    False
3     True
4     True
5    False
Name: Marks, dtype: bool
```

The result is a Boolean Series that can be used for filtering.

# 50. Descriptive Statistics

Common functions include:

```python
df["Marks"].sum()
df["Marks"].mean()
df["Marks"].median()
df["Marks"].min()
df["Marks"].max()
df["Marks"].std()
df["Marks"].var()
df["Marks"].count()
```

---
### Example: Descriptive Statistics

```python
print("Sum:", df["Marks"].sum())
print("Mean:", df["Marks"].mean())
print("Minimum:", df["Marks"].min())
print("Maximum:", df["Marks"].max())
```

Output:

```text
Sum: 514
Mean: 85.66666666666667
Minimum: 76
Maximum: 95
```

# 51. `value_counts()`

Counts unique values.

```python
df["City"].value_counts()
```

Percentage:

```python
df["City"].value_counts(
    normalize=True
)
```

---
### Example: `value_counts()`

```python
print(df["City"].value_counts())
```

Output:

```text
City
Lucknow    2
Delhi      2
Mumbai     2
Name: count, dtype: int64
```

It counts how many times each unique value appears.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `normalize` | `True`, `False` | Returns proportions instead of raw counts when `True`. |
| `sort` | `True`, `False` | Sorts results by frequency when `True`. |
| `ascending` | `True`, `False` | Controls the order of the counts. |
| `dropna` | `True`, `False` | Includes or excludes missing values from the counts. |
| `bins` | An integer or bin edges | Groups numeric values into intervals before counting. |

# 52. `unique()` and `nunique()`

Get unique values:

```python
df["City"].unique()
```

Count unique values:

```python
df["City"].nunique()
```

---
### Example: `unique()` and `nunique()`

```python
print(df["City"].unique())
print(df["City"].nunique())
```

Output:

```text
['Lucknow' 'Delhi' 'Mumbai']
3
```

`unique()` returns the unique values, while `nunique()` returns their count.

# 53. Applying Functions

`apply()` can apply a function to values.

```python
def add_bonus(x):
    return x + 5

df["Marks"] = df["Marks"].apply(
    add_bonus
)
```

Using lambda:

```python
df["Marks"] = df["Marks"].apply(
    lambda x: x + 5
)
```

---

# 54. `map()`

`map()` can transform values in a Series.

```python
df["Grade"] = df["Grade"].map(
    {
        "A": "Excellent",
        "B": "Good",
        "C": "Average"
    }
)
```

---
### Example: `map()`

```python
data = pd.DataFrame({
    "Grade": ["A", "B", "C"]
})

data["Result"] = data["Grade"].map({
    "A": "Excellent",
    "B": "Good",
    "C": "Average"
})

print(data)
```

Output:

```text
  Grade     Result
0     A  Excellent
1     B       Good
2     C    Average
```

# 55. GroupBy

`groupby()` follows the idea of:

```text
Split
Apply
Combine
```

Example:

```python
result = df.groupby(
    "Department"
)["Salary"].mean()

print(result)
```

---
### Example: `groupby()`

```python
result = df.groupby("City")["Marks"].mean()
print(result)
```

Output:

```text
City
Delhi      93.5
Lucknow    81.5
Mumbai     82.0
Name: Marks, dtype: float64
```

The rows are grouped by city, and then the average marks are calculated for each group.

### Important GroupBy Options

| Parameter | Common values | Effect |
|---|---|---|
| `by` | A column name or list of columns | Defines the groups. |
| `as_index` | `True`, `False` | Uses group keys as the index or keeps them as columns in supported aggregations. |
| `sort` | `True`, `False` | Sorts group keys or keeps their observed order. |
| `dropna` | `True`, `False` | Controls whether missing group keys are excluded. |
| `observed` | `True`, `False` | Controls whether categorical grouping includes only observed categories; defaults can vary by Pandas version. |

# 56. GroupBy Multiple Columns

```python
result = df.groupby(
    ["Department", "Gender"]
)["Salary"].mean()
```

---
### Example: GroupBy Multiple Columns

```python
data = pd.DataFrame({
    "Department": ["CSE", "CSE", "IT", "IT"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50000, 55000, 45000, 48000]
})

result = data.groupby(
    ["Department", "Gender"]
)["Salary"].mean()

print(result)
```

Output:

```text
Department  Gender
CSE         F         55000.0
            M         50000.0
IT          F         48000.0
            M         45000.0
Name: Salary, dtype: float64
```

# 57. GroupBy Aggregation

Common aggregation functions include:

```python
sum()
mean()
min()
max()
count()
median()
std()
```

Example:

```python
df.groupby("Department")[
    "Salary"
].agg(["mean", "max", "min"])
```

---
### Example: Multiple Aggregations

```python
result = df.groupby("City")["Marks"].agg(["mean", "max", "min"])
print(result)
```

Output:

```text
          mean  max  min
City
Delhi     93.5   95   92
Lucknow   81.5   85   78
Mumbai    82.0   88   76
```

One `groupby()` can calculate several statistics at the same time.

# 58. GroupBy `transform()`

`transform()` returns results aligned with the original DataFrame.

```python
df["Department_Average"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)
```

---
### Example: `transform()`

```python
data = pd.DataFrame({
    "Department": ["CSE", "CSE", "IT", "IT"],
    "Salary": [50000, 60000, 40000, 50000]
})

data["Department_Average"] = (
    data.groupby("Department")["Salary"]
        .transform("mean")
)

print(data)
```

Output:

```text
  Department  Salary  Department_Average
0        CSE   50000             55000.0
1        CSE   60000             55000.0
2         IT   40000             45000.0
3         IT   50000             45000.0
```

Unlike `groupby().mean()`, `transform()` returns values aligned with the original rows.

# 59. Combining DataFrames

Pandas provides several methods for combining datasets:

* `concat()`
* `merge()`
* `join()`
* `merge_ordered()`
* `merge_asof()`

---

# 60. `concat()`

Concatenate DataFrames vertically:

```python
result = pd.concat(
    [df1, df2]
)
```

---

## Concatenate Horizontally

```python
result = pd.concat(
    [df1, df2],
    axis=1
)
```

---

## Ignore Existing Index

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

---
### Example: `concat()`

```python
df1 = pd.DataFrame({"Name": ["Aman", "Riya"]})
df2 = pd.DataFrame({"Name": ["Rahul", "Neha"]})

result = pd.concat([df1, df2], ignore_index=True)
print(result)
```

Output:

```text
    Name
0   Aman
1   Riya
2  Rahul
3   Neha
```

`concat()` combines DataFrames along rows or columns.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `axis` | `0`, `1` | Combines along rows or columns. |
| `ignore_index` | `True`, `False` | Creates a new sequential index along the concatenation axis. |
| `join` | `"outer"`, `"inner"` | Keeps all or only shared labels on the other axis. |
| `keys` | A list of labels | Adds an outer index level to identify each input object. |
| `verify_integrity` | `True`, `False` | Checks for duplicate labels on the concatenation axis. |

# 61. `merge()`

`merge()` combines DataFrames using common keys.

```python
result = pd.merge(
    students,
    marks,
    on="Student_ID"
)
```

---
### Example: `merge()`

```python
students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Aman", "Riya", "Rahul"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [85, 92, 78]
})

result = pd.merge(students, marks, on="Student_ID")
print(result)
```

Output:

```text
   Student_ID   Name  Marks
0           1   Aman     85
1           2   Riya     92
2           3  Rahul     78
```

`merge()` combines data using a common key.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `how` | `"inner"`, `"left"`, `"right"`, `"outer"`, `"cross"` | Chooses the join type. |
| `on` | A column name or list of names | Uses matching column(s) present in both DataFrames as keys. |
| `left_on` / `right_on` | Column names | Uses differently named key columns from each DataFrame. |
| `suffixes` | A pair such as `("_x", "_y")` | Distinguishes overlapping non-key column names. |
| `indicator` | `True`, `False`, or a column name | Adds a column showing whether each row came from the left, right, or both inputs. |
| `validate` | `"one_to_one"`, `"one_to_many"`, `"many_to_one"`, `"many_to_many"` | Checks the expected relationship between merge keys. |

# 62. Types of Merge

## Inner Join

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)
```

## Left Join

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="left"
)
```

## Right Join

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="right"
)
```

## Outer Join

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="outer"
)
```

---

# 63. Merge on Different Column Names

```python
pd.merge(
    df1,
    df2,
    left_on="Student_ID",
    right_on="ID"
)
```

---

# 64. `join()`

`join()` is useful for combining DataFrames using their indexes.

```python
result = df1.join(df2)
```

---
### Example: `join()`

```python
left = pd.DataFrame(
    {"Name": ["Aman", "Riya"]},
    index=[1, 2]
)

right = pd.DataFrame(
    {"Marks": [85, 92]},
    index=[1, 2]
)

result = left.join(right)
print(result)
```

Output:

```text
   Name  Marks
1  Aman     85
2  Riya     92
```

`join()` is commonly used when the DataFrames are aligned by their indexes.

# 65. Reshaping Data

Reshaping changes the structure of a DataFrame.

Important functions include:

* `pivot()`
* `pivot_table()`
* `melt()`
* `explode()`

---

# 66. `pivot()`

```python
result = df.pivot(
    index="Date",
    columns="City",
    values="Sales"
)
```

`pivot()` requires the index/column combination to identify a single value.

---
### Example: `pivot()`

```python
data = pd.DataFrame({
    "Date": ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Sales": [100, 150, 120, 180]
})

result = data.pivot(
    index="Date",
    columns="City",
    values="Sales"
)

print(result)
```

Output:

```text
City        Delhi  Mumbai
Date
2026-01-01    100     150
2026-01-02    120     180
```

`pivot()` changes the shape of the data without aggregating duplicate combinations.

# 67. `pivot_table()`

`pivot_table()` can aggregate duplicate combinations.

```python
result = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Year",
    aggfunc="sum"
)
```

---
### Example: `pivot_table()`

```python
result = pd.pivot_table(
    data,
    values="Sales",
    index="City",
    aggfunc="sum"
)

print(result)
```

Output:

```text
        Sales
City
Delhi     220
Mumbai    330
```

`pivot_table()` is useful when duplicate combinations need to be aggregated.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `values` | A column name or list | Selects values to aggregate. |
| `index` | A column name or list | Defines row groups. |
| `columns` | A column name or list | Defines column groups. |
| `aggfunc` | `"mean"`, `"sum"`, `"count"`, `"min"`, `"max"`, or a function | Chooses how duplicate combinations are aggregated. |
| `fill_value` | `0` or another value | Replaces missing cells in the resulting table. |
| `margins` | `True`, `False` | Adds row/column totals when enabled. |

# 68. `melt()`

`melt()` converts wide data into long format.

```python
result = pd.melt(
    df,
    id_vars=["Name"],
    value_vars=["Maths", "Python"]
)
```

---
### Example: `melt()`

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya"],
    "Maths": [80, 90],
    "Python": [85, 95]
})

result = pd.melt(
    data,
    id_vars=["Name"],
    value_vars=["Maths", "Python"]
)

print(result)
```

Output:

```text
   Name variable  value
0  Aman    Maths     80
1  Riya    Maths     90
2  Aman   Python     85
3  Riya   Python     95
```

`melt()` changes **wide data into long data**.

### Important Parameter Options

| Parameter | Common values | Effect |
|---|---|---|
| `id_vars` | A column name or list | Columns kept as identifier columns. |
| `value_vars` | A column name or list | Columns to unpivot; if omitted, all non-identifier columns are used. |
| `var_name` | A string | Names the column that stores original column names. |
| `value_name` | A string | Names the column that stores the values. |
| `ignore_index` | `True`, `False` | Controls whether the result gets a new sequential index. |

# 69. `explode()`

`explode()` converts list-like values into separate rows.

Example:

```python
df = pd.DataFrame({
    "Name": ["Aman", "Riya"],
    "Skills": [
        ["Python", "SQL"],
        ["Java", "Python"]
    ]
})

result = df.explode("Skills")

print(result)
```

Output:

```text
   Name  Skills
0  Aman  Python
0  Aman     SQL
1  Riya    Java
1  Riya  Python
```

---
### Example: `explode()`

```python
data = pd.DataFrame({
    "Name": ["Aman", "Riya"],
    "Skills": [["Python", "SQL"], ["Java", "Python"]]
})

result = data.explode("Skills")
print(result)
```

Output:

```text
   Name  Skills
0  Aman  Python
0  Aman     SQL
1  Riya    Java
1  Riya  Python
```

Each item in a list becomes a separate row.

# 70. Working with Dates

Pandas provides `to_datetime()` for converting values into datetime objects.

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

---
### Example: `to_datetime()`

```python
data = pd.DataFrame({
    "Date": ["2026-01-01", "2026-02-15"]
})

data["Date"] = pd.to_datetime(data["Date"])

print(data)
print(data.dtypes)
```

Output:

```text
        Date
0 2026-01-01
1 2026-02-15

Date    datetime64[ns]
dtype: object
```

After conversion, Pandas can use datetime-specific operations.

### Important `to_datetime()` Options

| Parameter | Common values | Effect |
|---|---|---|
| `format` | A format such as `"%Y-%m-%d"` | Specifies the expected date format. |
| `errors` | `"raise"`, `"coerce"`, `"ignore"` where supported | Raises errors, converts invalid values to `NaT`, or handles invalid values according to the selected option. |
| `dayfirst` | `True`, `False` | Prefers day-first interpretation for ambiguous dates. |
| `utc` | `True`, `False` | Converts parsed timestamps to UTC when enabled. |

# 71. Creating Date Ranges

```python
dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-10"
)

print(dates)
```

Output:

```text
DatetimeIndex(['2026-01-01', '2026-01-02', '2026-01-03',
               '2026-01-04', '2026-01-05', '2026-01-06',
               '2026-01-07', '2026-01-08', '2026-01-09',
               '2026-01-10'],
              dtype='datetime64[ns]', freq='D')
```

---
### Example: `date_range()`

```python
dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-05"
)

print(dates)
```

Output:

```text
DatetimeIndex(['2026-01-01', '2026-01-02', '2026-01-03',
               '2026-01-04', '2026-01-05'],
              dtype='datetime64[ns]', freq='D')
```

# 72. Date Components

After converting a column to datetime, use `.dt`.

```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
```

Other useful properties:

```python
df["Date"].dt.day_name()
df["Date"].dt.month_name()
df["Date"].dt.dayofweek
df["Date"].dt.quarter
```

---
### Example: Date Components

```python
data = pd.DataFrame({
    "Date": pd.to_datetime(["2026-01-15", "2026-06-20"])
})

print(data["Date"].dt.year)
print(data["Date"].dt.month)
print(data["Date"].dt.day)
```

Output:

```text
0    2026
1    2026
Name: Date, dtype: int32

0    1
1    6
Name: Date, dtype: int32

0    15
1    20
Name: Date, dtype: int32
```

`.dt` gives access to date and time components.

# 73. Date Formatting

```python
df["Date"].dt.strftime(
    "%d-%m-%Y"
)
```

---
### Example: `strftime()`

```python
data = pd.Series(pd.to_datetime(["2026-01-05"]))
print(data.dt.strftime("%d-%m-%Y"))
```

Output:

```text
0    05-01-2026
dtype: object
```

`strftime()` converts datetime values into the requested text format.

# 74. Resampling

Resampling changes the frequency of time-series data.

Monthly sum:

```python
monthly = df.resample(
    "ME"
)["Sales"].sum()
```

Daily mean:

```python
daily = df.resample(
    "D"
)["Sales"].mean()
```

Always check the offset alias supported by your installed Pandas version.

---

### Important Resampling Options

| Parameter | Common values | Effect |
|---|---|---|
| Frequency | `"D"`, `"W"`, `"ME"`, `"h"`, `"min"` | Chooses the target time interval; use frequency aliases supported by your Pandas version. |
| `closed` | `"left"`, `"right"` | Chooses which side of each time interval is included. |
| `label` | `"left"`, `"right"` | Chooses which interval edge labels the result. |
| `origin` | `"start_day"`, `"start"`, `"epoch"` or a timestamp where supported | Controls how bins are anchored. |

# 75. Rolling Window

Rolling operations calculate values over a moving window.

Example:

```python
df["Moving_Average"] = (
    df["Sales"]
    .rolling(3)
    .mean()
)
```

---
### Example: Rolling Average

```python
data = pd.DataFrame({
    "Sales": [10, 20, 30, 40, 50]
})

data["Moving_Average"] = data["Sales"].rolling(3).mean()

print(data)
```

Output:

```text
   Sales  Moving_Average
0     10             NaN
1     20             NaN
2     30            20.0
3     40            30.0
4     50            40.0
```

The first two rows do not have 3 values yet, so their rolling average is `NaN`.

### Important Rolling-Window Options

| Parameter | Common values | Effect |
|---|---|---|
| `window` | An integer such as `3`, or a time offset such as `"7D"` | Defines the number of observations or time span in each window. |
| `min_periods` | An integer | Sets the minimum valid observations required for a result. |
| `center` | `True`, `False` | Labels results at the center of the window or at its right edge. |
| `closed` | `"right"`, `"left"`, `"both"`, `"neither"` where supported | Controls the included window endpoints. |

# 76. Cumulative Operations

Cumulative sum:

```python
df["Sales"].cumsum()
```

Cumulative product:

```python
df["Sales"].cumprod()
```

Cumulative maximum:

```python
df["Sales"].cummax()
```

Cumulative minimum:

```python
df["Sales"].cummin()
```

---
### Example: Cumulative Operations

```python
data = pd.Series([10, 20, 30, 40])

print(data.cumsum())
```

Output:

```text
0     10
1     30
2     60
3    100
dtype: int64
```

Each result contains the running total up to that position.

# 77. Ranking

```python
df["Rank"] = df[
    "Marks"
].rank(
    ascending=False
)
```

---
### Example: Ranking

```python
print(df["Marks"].rank(ascending=False))
```

Output:

```text
0    4.0
1    2.0
2    5.0
3    3.0
4    1.0
5    6.0
Name: Marks, dtype: float64
```

Higher marks receive a better rank when `ascending=False`.

# 78. Sampling

Random sample of rows:

```python
df.sample(5)
```

Sample fraction:

```python
df.sample(
    frac=0.2
)
```

---

# 79. Copying Data

Create an independent copy:

```python
new_df = df.copy()
```

This is useful when we want to modify a DataFrame without changing the original object.

---

# 80. Reading Large Datasets

Large files may not fit comfortably into memory.

CSV files can be read in chunks:

```python
for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    print(chunk.shape)
```

Output:

```text
Example output (one line per chunk):
(10000, 8)
(10000, 8)
...
The final chunk may contain fewer rows. The output depends on the file.
```

This allows data to be processed in smaller portions.

---

### Important Large-File Options

| Parameter | Common values | Effect |
|---|---|---|
| `usecols` | A list of required column names | Reduces memory use by loading only selected columns. |
| `chunksize` | An integer such as `10000` | Returns an iterator that reads a file in chunks. |
| `nrows` | A positive integer | Limits the number of rows read. |
| `dtype` | A type or dictionary of types | Helps avoid unnecessarily large or incorrect data types. |
| `low_memory` | `True`, `False` for `read_csv()` | Controls internal parsing behavior; it does not replace chunked reading for genuinely large files. |

# 81. Parquet Files

Parquet is a column-oriented storage format.

Read:

```python
df = pd.read_parquet(
    "data.parquet"
)
```

Write:

```python
df.to_parquet(
    "output.parquet"
)
```

---

# 82. Working with NumPy

Pandas works closely with NumPy.

Example:

```python
import numpy as np
import pandas as pd

data = np.array([
    [10, 20],
    [30, 40]
])

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    0   1
0  10  20
1  30  40
```

Convert DataFrame to NumPy:

```python
array = df.to_numpy()
```

---

# 83. Conditional Replacement with `where()`

`where()` keeps values where a condition is true and replaces other values.

```python
result = df["Marks"].where(
    df["Marks"] >= 40,
    0
)
```

---
### Example: `where()`

```python
result = df["Marks"].where(df["Marks"] >= 80, 0)
print(result)
```

Output:

```text
0    85
1    92
2     0
3    88
4    95
5     0
Name: Marks, dtype: int64
```

Values meeting the condition are kept; other values become `0`.

# 84. Checking Conditions with `any()` and `all()`

Check whether any value satisfies a condition:

```python
(df["Marks"] > 90).any()
```

Check whether all values satisfy a condition:

```python
(df["Marks"] > 40).all()
```

---

# 85. Working with Rows

Iterating over rows is possible using:

```python
for index, row in df.iterrows():
    print(index, row)
```

Output:

```text
Each row is printed with its index and Series values. Exact output depends on df.
```

Another method:

```python
for row in df.itertuples():
    print(row)
```

Output:

```text
Each row is printed as a named tuple. Exact output depends on df.
```

For most data transformations, vectorized operations are preferred over row-by-row loops.

---

# 86. Applying Functions Row-wise

```python
df["Total"] = df.apply(
    lambda row:
        row["Maths"] + row["Python"],
    axis=1
)
```

Here:

```text
axis=1
```

means the function works row-wise.

---
### Example: Row-wise `apply()`

```python
data = pd.DataFrame({
    "Maths": [80, 90],
    "Python": [85, 95]
})

data["Total"] = data.apply(
    lambda row: row["Maths"] + row["Python"],
    axis=1
)

print(data)
```

Output:

```text
   Maths  Python  Total
0     80      85    165
1     90      95    185
```

`axis=1` means the function receives one row at a time.

# 87. Creating Dummy Variables

Categorical values can be converted into indicator columns using:

```python
result = pd.get_dummies(
    df["Gender"]
)
```

For multiple columns:

```python
result = pd.get_dummies(
    df,
    columns=["Gender"]
)
```

---
### Example: `get_dummies()`

```python
data = pd.Series(["Male", "Female", "Male"], name="Gender")

result = pd.get_dummies(data)
print(result)
```

Output:

```text
   Female   Male
0   False   True
1    True  False
2   False   True
```

Each category becomes a separate indicator column.

### Important `get_dummies()` Options

| Parameter | Common values | Effect |
|---|---|---|
| `columns` | A list of column names | Encodes only the selected columns. |
| `prefix` | A string or dictionary | Adds prefixes to generated column names. |
| `drop_first` | `True`, `False` | Drops the first category column when enabled. |
| `dummy_na` | `True`, `False` | Creates a separate indicator for missing values when enabled. |
| `dtype` | Commonly `bool`, `int`, or another supported dtype | Sets the type of generated indicator columns. |

# 88. Practical Data Cleaning Workflow

A common Pandas data cleaning workflow is:

```text
Read Data
    ↓
Understand Data
    ↓
Check Data Types
    ↓
Check Missing Values
    ↓
Remove Duplicates
    ↓
Clean Columns
    ↓
Convert Data Types
    ↓
Handle Outliers / Invalid Values
    ↓
Transform Data
    ↓
Analyse Data
    ↓
Export Data
```

---

# 89. Practical Example

The following four-row example demonstrates a small, self-contained analysis.

```python
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Age": [21, 22, 20, 21],
    "Marks": [85, 92, 78, 88],
    "City": ["Lucknow", "Delhi", "Lucknow", "Mumbai"],
}
df = pd.DataFrame(data)
```

## Filter students scoring above 80

```python
result = df[df["Marks"] > 80]
print(result)
```

```text
   Name  Age  Marks     City
0  Aman   21     85  Lucknow
1  Riya   22     92    Delhi
3  Neha   21     88   Mumbai
```

## Sort by marks

```python
print(df.sort_values("Marks", ascending=False))
```

Output:

```text
   Name  Age  Marks     City
1  Riya   22     92    Delhi
3  Neha   21     88   Mumbai
0  Aman   21     85  Lucknow
2  Rahul  20     78  Lucknow
```

```text
   Name  Age  Marks     City
1  Riya   22     92    Delhi
3  Neha   21     88   Mumbai
0  Aman   21     85  Lucknow
2  Rahul  20     78  Lucknow
```

## Average and city-level summary

```python
print(df["Marks"].mean())
print(df.groupby("City")["Marks"].mean())
```

Output:

```text
86.0
City
Delhi      92.0
Lucknow    81.5
Mumbai     88.0
Name: Marks, dtype: float64
```

```text
85.75
City
Delhi       92.0
Lucknow     81.5
Mumbai      88.0
Name: Marks, dtype: float64
```
---

# 90. Pandas and Machine Learning

Pandas is frequently used before training a Machine Learning model.

Typical steps include:

```text
Load Dataset
     ↓
Explore Dataset
     ↓
Clean Dataset
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Convert Data Types
     ↓
Encode Categorical Data
     ↓
Select Features
     ↓
Split Data
     ↓
Train Machine Learning Model
```

Example:

```python
X = df[
    ["Age", "Salary"]
]

y = df[
    "Purchased"
]
```

---

# 91. Best Practices

Some useful Pandas practices are:

* Use meaningful column names
* Check `df.info()` after loading data
* Check missing values before analysis
* Check duplicate rows
* Use vectorized operations where possible
* Avoid unnecessary row-by-row loops
* Use `loc[]` and `iloc[]` clearly
* Make explicit copies when needed
* Choose suitable data types
* Use categories for repeated categorical values
* Read only required columns for large files
* Process large datasets in chunks when required
* Keep raw data separate from cleaned data
* Save cleaned datasets in an appropriate format

---

# 92. Performance Considerations

For large datasets:

* Load only required columns
* Use efficient data types
* Use categorical types where suitable
* Process large files in chunks
* Prefer vectorized operations
* Avoid unnecessary copies
* Use appropriate storage formats
* Measure memory usage

For very large datasets, other tools may be more suitable depending on the workload.

---
