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
- Data visualization

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

---

## Accessing Series Values

```python
print(data["a"])
```

Using position:

```python
print(data.iloc[0])
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

---

## Creating an Empty DataFrame

```python
df = pd.DataFrame()

print(df)
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

# 10. Reading Data

Pandas can read data from many sources.

Common functions include:

```python
pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_html()
pd.read_sql()
```

Pandas also supports many other storage formats such as Parquet, Feather, HDF5 and others.

---

# 11. Reading CSV Files

CSV stands for **Comma-Separated Values**.

Example:

```python
data = pd.read_csv("data.csv")

print(data)
```

---

## Reading CSV with a Different Separator

```python
data = pd.read_csv(
    "data.csv",
    sep=";"
)
```

---

## Reading Selected Columns

```python
data = pd.read_csv(
    "data.csv",
    usecols=["Name", "Age"]
)
```

---

## Reading CSV with Index Column

```python
data = pd.read_csv(
    "data.csv",
    index_col="Name"
)
```

---

## Handling Missing Values While Reading

```python
data = pd.read_csv(
    "data.csv",
    na_values=["NA", "N/A", "?"]
)
```

---

# 12. Writing CSV Files

Use:

```python
df.to_csv("output.csv")
```

To avoid writing the index:

```python
df.to_csv(
    "output.csv",
    index=False
)
```

---

# 13. Reading Excel Files

Pandas can read Excel files using:

```python
df = pd.read_excel("data.xlsx")
```

We can specify a sheet:

```python
df = pd.read_excel(
    "data.xlsx",
    sheet_name="Sheet1"
)
```

---

# 14. Writing Excel Files

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

Multiple sheets can be written using `ExcelWriter`.

```python
with pd.ExcelWriter("output.xlsx") as writer:
    df.to_excel(
        writer,
        sheet_name="Data",
        index=False
    )
```

---

# 15. Reading JSON

JSON data can be read using:

```python
df = pd.read_json("data.json")

print(df)
```

---

## Writing JSON

```python
df.to_json("output.json")
```

---

# 16. Reading HTML Tables

Pandas can extract tables from HTML pages.

```python
tables = pd.read_html("https://example.com")
```

This returns a list of DataFrames.

---

# 17. Reading SQL Data

Pandas can work with SQL databases.

Example:

```python
df = pd.read_sql(
    "SELECT * FROM students",
    connection
)
```

---

# 18. Selecting Columns

Select one column:

```python
df["Name"]
```

Select multiple columns:

```python
df[["Name", "Age"]]
```

---

# 19. Selecting Rows

Rows can be selected using:

* `loc[]`
* `iloc[]`
* Boolean conditions

---

# 20. `loc[]`

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

# 21. `iloc[]`

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

# 22. `at[]` and `iat[]`

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

# 23. Boolean Indexing

Boolean indexing is used to filter data.

```python
result = df[df["Age"] > 20]

print(result)
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

# 24. `isin()`

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

# 25. `query()`

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

# 26. Adding Columns

A new column can be added directly.

```python
df["Salary"] = [25000, 30000, 28000]
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

# 27. Updating Columns

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

# 28. Renaming Columns

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
    "Marks"
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

# 29. Removing Columns

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

# 30. Removing Rows

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

# 31. Inserting Columns

A column can be inserted at a specific position.

```python
df.insert(
    1,
    "City",
    ["Delhi", "Lucknow", "Mumbai"]
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

# 32. Reindexing

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

# 33. Indexing

Every Series and DataFrame has an index.

```python
print(df.index)
```

Set a column as index:

```python
df = df.set_index("Name")
```

---

# 34. Resetting Index

```python
df = df.reset_index()
```

To remove the old index:

```python
df = df.reset_index(drop=True)
```

---

# 35. Sorting Data

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

# 36. Sorting by Index

```python
df.sort_index()
```

Descending:

```python
df.sort_index(
    ascending=False
)
```

---

# 37. Duplicate Data

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

# 38. Missing Data

Missing values are common in real-world datasets.

Pandas can represent missing values using values such as:

* `NaN`
* `NaT`
* `pd.NA`
* `None`

---

# 39. Detecting Missing Values

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

# 40. Dropping Missing Values

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

# 41. Filling Missing Values

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

# 42. Replacing Values

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

# 43. Data Types

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

# 44. Changing Data Types

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

# 45. Numeric Conversion

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

# 46. String Data

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

# 47. String Methods

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

# 48. Splitting Strings

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

# 49. String Matching

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

# 50. Extracting Text

Regular expressions can be used with `.str.extract()`.

```python
df["Email"].str.extract(
    r"(@.*)"
)
```

---

# 51. Vectorized Operations

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

# 52. Arithmetic Operations

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

# 53. Comparison Operations

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

# 54. Descriptive Statistics

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

# 55. `value_counts()`

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

# 56. `unique()` and `nunique()`

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

# 57. `idxmax()` and `idxmin()`

Find the index of the maximum value:

```python
df["Marks"].idxmax()
```

Find the index of the minimum value:

```python
df["Marks"].idxmin()
```

---
### Example: `idxmax()` and `idxmin()`

```python
print(df["Marks"].idxmax())
print(df["Marks"].idxmin())
```

Output:

```text
4
5
```

Index `4` contains the highest marks (`95`), while index `5` contains the lowest (`76`).

# 58. Applying Functions

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

# 59. `map()`

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

# 60. `applymap()` / Element-wise Operations

For element-wise transformations across a DataFrame, use the current pandas element-wise APIs appropriate to the installed version.

Example:

```python
df.map(
    lambda x: x
)
```

Always check the installed Pandas version when working with APIs that have changed between releases.

---

# 61. GroupBy

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

# 62. GroupBy Multiple Columns

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

# 63. GroupBy Aggregation

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

# 64. Named Aggregation

```python
result = df.groupby(
    "Department"
).agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max")
)
```

---

# 65. GroupBy `transform()`

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

# 66. GroupBy `filter()`

Groups can be filtered based on a condition.

```python
result = df.groupby(
    "Department"
).filter(
    lambda group: len(group) > 2
)
```

---

# 67. GroupBy `apply()`

A custom function can be applied to each group.

```python
result = df.groupby(
    "Department"
).apply(
    lambda group: group["Salary"].mean()
)
```

---

# 68. Combining DataFrames

Pandas provides several methods for combining datasets:

* `concat()`
* `merge()`
* `join()`
* `merge_ordered()`
* `merge_asof()`

---

# 69. `concat()`

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

# 70. `merge()`

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

# 71. Types of Merge

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

# 72. Merge on Different Column Names

```python
pd.merge(
    df1,
    df2,
    left_on="Student_ID",
    right_on="ID"
)
```

---

# 73. `join()`

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

# 74. Comparing DataFrames

Pandas provides `compare()` for finding differences.

```python
df1.compare(df2)
```

---

# 75. Reshaping Data

Reshaping changes the structure of a DataFrame.

Important functions include:

* `pivot()`
* `pivot_table()`
* `melt()`
* `stack()`
* `unstack()`
* `explode()`
* `crosstab()`
* `cut()`
* `factorize()`

---

# 76. `pivot()`

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

# 77. `pivot_table()`

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

# 78. `melt()`

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

# 79. `stack()` and `unstack()`

`stack()` moves columns into the index.

```python
result = df.stack()
```

`unstack()` moves an index level into columns.

```python
result = df.unstack()
```

---

# 80. `explode()`

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

# 81. `crosstab()`

`crosstab()` creates a frequency table.

```python
result = pd.crosstab(
    df["Gender"],
    df["Department"]
)
```

---
### Example: `crosstab()`

```python
result = pd.crosstab(df["City"], df["Age"])
print(result)
```

Output:

```text
Age      20  21  22  23
City
Delhi     0   0   1   1
Lucknow   1   1   0   0
Mumbai    0   1   1   0
```

`crosstab()` creates a frequency table showing how often combinations occur.

# 82. `cut()`

`cut()` converts numerical values into intervals.

```python
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 50, 100]
)
```

---
### Example: `cut()`

```python
data = pd.DataFrame({"Age": [17, 21, 35, 60]})

data["Age_Group"] = pd.cut(
    data["Age"],
    bins=[0, 18, 30, 50, 100]
)

print(data)
```

Output:

```text
   Age    Age_Group
0   17    (0, 18]
1   21   (18, 30]
2   35   (30, 50]
3   60  (50, 100]
```

`cut()` converts continuous numeric values into intervals.

# 83. `qcut()`

`qcut()` divides data into quantiles.

```python
df["Group"] = pd.qcut(
    df["Marks"],
    4
)
```

---
### Example: `qcut()`

```python
data = pd.DataFrame({
    "Marks": [40, 50, 60, 70, 80, 90, 100, 30]
})

data["Group"] = pd.qcut(data["Marks"], 4)
print(data)
```

Output:

```text
   Marks          Group
0     40   (29.999, 47.5]
1     50     (47.5, 65.0]
2     60     (47.5, 65.0]
3     70     (65.0, 77.5]
4     80    (77.5, 92.5]
5     90    (77.5, 92.5]
6    100   (92.5, 100.0]
7     30   (29.999, 47.5]
```

The exact interval representation can vary slightly with Pandas versions, but the idea is to divide values into quantile-based groups.

# 84. `factorize()`

`factorize()` converts values into integer codes.

```python
codes, uniques = pd.factorize(
    df["City"]
)
```

---
### Example: `factorize()`

```python
codes, uniques = pd.factorize(df["City"])

print(codes)
print(uniques)
```

Output:

```text
[0 1 0 2 1 2]
Index(['Lucknow', 'Delhi', 'Mumbai'], dtype='object')
```

Each unique category receives an integer code.

# 85. Categorical Data

Categorical data is useful when a column contains a limited number of repeated categories.

Example:

```python
df["Department"] = df[
    "Department"
].astype("category")
```

Check categories:

```python
df["Department"].cat.categories
```

---

# 86. Working with Categories

Add categories:

```python
df["Department"] = (
    df["Department"]
    .cat.add_categories(["Other"])
)
```

Rename categories:

```python
df["Department"] = (
    df["Department"]
    .cat.rename_categories({
        "CSE": "Computer Science"
    })
)
```

---

# 87. Ordered Categories

```python
from pandas.api.types import CategoricalDtype

dtype = CategoricalDtype(
    categories=[
        "Low",
        "Medium",
        "High"
    ],
    ordered=True
)

df["Priority"] = df[
    "Priority"
].astype(dtype)
```

---

# 88. Working with Dates

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

# 89. Creating Date Ranges

```python
dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-10"
)

print(dates)
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

# 90. Date Components

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

# 91. Date Formatting

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

# 92. Time Series

Pandas provides strong support for time-series data.

A datetime column can be used as an index:

```python
df = df.set_index("Date")
```

---

# 93. Resampling

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

# 94. Time Zones

Pandas supports timezone-aware datetime values.

Example:

```python
dates = pd.to_datetime(
    ["2026-01-01 10:00"]
)

dates = dates.tz_localize(
    "Asia/Kolkata"
)
```

---

# 95. Timedelta

A `Timedelta` represents a duration.

```python
duration = pd.Timedelta(
    days=5
)

print(duration)
```

Difference between dates:

```python
df["Duration"] = (
    df["End_Date"] -
    df["Start_Date"]
)
```

---
### Example: `Timedelta`

```python
duration = pd.Timedelta(days=5)
print(duration)
```

Output:

```text
5 days 00:00:00
```

A `Timedelta` represents a duration rather than a calendar date.

# 96. Rolling Window

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

# 97. Expanding Window

An expanding window uses all observations available up to the current row.

```python
df["Cumulative_Average"] = (
    df["Sales"]
    .expanding()
    .mean()
)
```

---
### Example: Expanding Average

```python
data = pd.DataFrame({
    "Sales": [10, 20, 30, 40]
})

data["Average"] = data["Sales"].expanding().mean()

print(data)
```

Output:

```text
   Sales  Average
0     10     10.0
1     20     15.0
2     30     20.0
3     40     25.0
```

The calculation uses all values available up to the current row.

# 98. Exponentially Weighted Window

An exponentially weighted calculation gives more weight to recent observations.

```python
df["EWMA"] = (
    df["Sales"]
    .ewm(span=3)
    .mean()
)
```

---

# 99. Cumulative Operations

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

# 100. Ranking

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

# 101. Sampling

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

# 102. Memory Usage

Check DataFrame memory usage:

```python
df.memory_usage(
    deep=True
)
```

Total memory:

```python
df.memory_usage(
    deep=True
).sum()
```

---
### Example: Memory Usage

```python
print(df.memory_usage(deep=True))
```

Output will look similar to:

```text
Index    ...
Name     ...
Age      ...
Marks    ...
City     ...
dtype: int64
```

The exact byte values depend on the Python/Pandas environment, but the method shows how much memory each column uses.

# 103. Copying Data

Create an independent copy:

```python
new_df = df.copy()
```

This is useful when we want to modify a DataFrame without changing the original object.

---

# 104. Views and Copy-on-Write

Pandas has behaviour around views, copies and assignment.

A safe and clear approach when creating an independent DataFrame is:

```python
new_df = df.copy()
```

Modern Pandas also uses **Copy-on-Write** mechanisms. Code that relies on accidental view behaviour should be avoided.

---

# 105. MultiIndex

A MultiIndex allows multiple levels of indexes.

Example:

```python
df = df.set_index(
    ["Department", "Name"]
)
```

Accessing a level:

```python
df.index
```

---
### Example: MultiIndex

```python
data = pd.DataFrame({
    "Department": ["CSE", "CSE", "IT"],
    "Name": ["Aman", "Riya", "Rahul"],
    "Marks": [85, 92, 78]
})

data = data.set_index(["Department", "Name"])
print(data)
```

Output:

```text
                    Marks
Department Name
CSE        Aman        85
           Riya        92
IT         Rahul       78
```

Two columns are now used together as a hierarchical index.

# 106. MultiIndex Selection

```python
df.loc[
    ("CSE", "Aman")
]
```

MultiIndex is useful for hierarchical data.

---

# 107. Duplicate Labels

Pandas indexes can contain duplicate labels.

Check duplicate index values:

```python
df.index.duplicated()
```

Duplicate column labels can also be checked using:

```python
df.columns.duplicated()
```

---

# 108. Nullable Data Types

Pandas provides nullable data types for values such as integers and booleans.

Example:

```python
df["Age"] = df[
    "Age"
].astype("Int64")
```

Nullable boolean:

```python
df["Active"] = df[
    "Active"
].astype("boolean")
```

---
### Example: Nullable Integer

```python
data = pd.Series([21, None, 23], dtype="Int64")

print(data)
print(data.dtype)
```

Output:

```text
0      21
1    <NA>
2      23
dtype: Int64
Int64
```

The capital `I` in `Int64` represents Pandas' nullable integer type.

# 109. Pandas Plotting

Pandas can create plots using Matplotlib.

Example:

```python
df["Sales"].plot()

import matplotlib.pyplot as plt

plt.show()
```

Bar chart:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)
```

Common plot types include:

* Line
* Bar
* Barh
* Histogram
* Box
* Area
* Pie
* Scatter

---

# 110. Styling DataFrames

Pandas provides the `Styler` object for displaying formatted tables.

Example:

```python
df.style
```

Format values:

```python
df.style.format(
    {
        "Salary": "₹{:,.0f}"
    }
)
```

---

# 111. Conditional Styling

Example:

```python
df.style.highlight_max()
```

Highlight minimum:

```python
df.style.highlight_min()
```

---

# 112. Exporting Styled Data

Styled DataFrames can also be exported to supported formats.

Example:

```python
styled = df.style.highlight_max()
```

The final export method depends on the required output format.

---

# 113. Evaluation with `eval()`

Pandas provides expression evaluation tools for some DataFrame operations.

Example:

```python
df.eval(
    "Total = Maths + Python"
)
```

---

# 114. Querying with `query()`

Example:

```python
result = df.query(
    "Marks > 80"
)
```

This can make some filtering expressions easier to read.

---

# 115. Reading Large Datasets

Large files may not fit comfortably into memory.

CSV files can be read in chunks:

```python
for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    print(chunk.shape)
```

This allows data to be processed in smaller portions.

---

# 116. Selecting Required Columns

When working with large data, reading only required columns can reduce unnecessary memory usage.

```python
df = pd.read_csv(
    "large_file.csv",
    usecols=["Name", "Age", "Marks"]
)
```

---

# 117. Efficient Data Types

Choosing suitable data types can reduce memory usage.

For example:

```python
df["Age"] = df[
    "Age"
].astype("Int64")
```

Categorical columns can also reduce memory usage when the number of unique values is small:

```python
df["City"] = df[
    "City"
].astype("category")
```

---

# 118. Sparse Data

Pandas supports sparse data structures for datasets containing many repeated or missing values.

Example:

```python
sparse = pd.arrays.SparseArray(
    [0, 0, 1, 0, 0]
)

print(sparse)
```

Sparse data can be useful when most values are empty or zero.

---

# 119. Parquet Files

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

# 120. Feather Files

Read:

```python
df = pd.read_feather(
    "data.feather"
)
```

Write:

```python
df.to_feather(
    "output.feather"
)
```

---

# 121. Pickle

Pandas objects can be serialized using Pickle.

Write:

```python
df.to_pickle(
    "data.pkl"
)
```

Read:

```python
df = pd.read_pickle(
    "data.pkl"
)
```

Only load pickle files from trusted sources.

---

# 122. HDF5

Pandas can work with HDF5 files when the required HDF5/PyTables dependencies are available.

Write:

```python
df.to_hdf(
    "data.h5",
    key="data"
)
```

Read:

```python
df = pd.read_hdf(
    "data.h5",
    key="data"
)
```

---

# 123. Clipboard

Pandas can read tabular data from the system clipboard in supported environments.

```python
df = pd.read_clipboard()
```

---

# 124. Working with NumPy

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

Convert DataFrame to NumPy:

```python
array = df.to_numpy()
```

---

# 125. DataFrame to Dictionary

```python
data = df.to_dict()
```

Other orientations can be used:

```python
df.to_dict(
    orient="records"
)
```

---
### Example: DataFrame to Dictionary

```python
data = df[["Name", "Marks"]].head(2)
print(data.to_dict(orient="records"))
```

Output:

```text
[{'Name': 'Aman', 'Marks': 85}, {'Name': 'Riya', 'Marks': 92}]
```

`orient="records"` creates a list containing one dictionary for each row.

# 126. DataFrame to List

```python
data = df.values.tolist()
```

A NumPy-based approach is:

```python
data = df.to_numpy().tolist()
```

---
### Example: DataFrame to List

```python
data = df[["Name", "Marks"]].head(2)
print(data.to_numpy().tolist())
```

Output:

```text
[['Aman', 85], ['Riya', 92]]
```

# 127. DataFrame to CSV String

```python
csv_data = df.to_csv(
    index=False
)

print(csv_data)
```

---
### Example: DataFrame to CSV String

```python
data = df[["Name", "Marks"]].head(2)

csv_data = data.to_csv(index=False)
print(csv_data)
```

Output:

```text
Name,Marks
Aman,85
Riya,92
```

Instead of saving to a file, `to_csv()` can return the CSV content as a string.

# 128. `get()` Method

`get()` can safely retrieve a column.

```python
column = df.get(
    "Name"
)
```

A default value can be supplied:

```python
column = df.get(
    "Address",
    "Not Available"
)
```

---
### Example: `get()`

```python
print(df.get("Name").head(2))
print(df.get("Address", "Not Available"))
```

Output:

```text
0    Aman
1    Riya
Name: Name, dtype: object

Not Available
```

`get()` is useful when a column may not exist because a default value can be supplied.

# 129. Conditional Replacement with `where()`

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

# 130. `mask()`

`mask()` is the opposite style of conditional replacement.

```python
result = df["Marks"].mask(
    df["Marks"] < 40,
    0
)
```

---
### Example: `mask()`

```python
result = df["Marks"].mask(df["Marks"] < 80, 0)
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

Here, values matching the condition (`Marks < 80`) are replaced.

# 131. Checking Conditions with `any()` and `all()`

Check whether any value satisfies a condition:

```python
(df["Marks"] > 90).any()
```

Check whether all values satisfy a condition:

```python
(df["Marks"] > 40).all()
```

---

# 132. `where()` with DataFrame

Conditions can also be applied to an entire DataFrame.

```python
result = df.where(
    df > 0
)
```

---

# 133. Working with Rows

Iterating over rows is possible using:

```python
for index, row in df.iterrows():
    print(index, row)
```

Another method:

```python
for row in df.itertuples():
    print(row)
```

For most data transformations, vectorized operations are preferred over row-by-row loops.

---

# 134. Applying Functions Row-wise

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

# 135. Working with Index Alignment

Pandas aligns Series and DataFrames using their labels.

Example:

```python
s1 = pd.Series(
    [10, 20],
    index=["A", "B"]
)

s2 = pd.Series(
    [30, 40],
    index=["B", "C"]
)

print(s1 + s2)
```

The result is aligned using the index labels.

---

# 136. Mathematical Operations with Alignment

```python
df["Total"] = (
    df["Maths"] +
    df["Python"]
)
```

Pandas aligns values based on labels rather than only relying on their physical position.

---

# 137. `combine_first()`

`combine_first()` can use non-missing values from another object.

```python
result = df1.combine_first(
    df2
)
```

---

# 138. `merge_ordered()`

`merge_ordered()` is useful for combining ordered data.

```python
result = pd.merge_ordered(
    df1,
    df2,
    on="Date"
)
```

---

# 139. `merge_asof()`

`merge_asof()` performs a nearest-key style merge, commonly useful with ordered time-series data.

```python
result = pd.merge_asof(
    df1,
    df2,
    on="Time"
)
```

The input data should be appropriately sorted for the operation.

---

# 140. Creating Dummy Variables

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

# 141. One-Hot Encoding

One-hot encoding creates separate columns for categories.

Example:

```text
Gender
Male
Female
Male
```

can become:

```text
Female  Male
0       1
1       0
0       1
```

This is commonly used while preparing categorical data for Machine Learning.

---
### Example: One-Hot Encoding

```text
Original:

Gender
Male
Female
Male

After encoding:

   Female  Male
0   False  True
1    True  False
2   False  True
```

The categorical values are represented using separate columns.

# 142. `from_dummies()`

Indicator columns can be converted back to categorical representation using:

```python
pd.from_dummies(
    dummy_data
)
```

---

# 143. Practical Data Cleaning Workflow

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

# 144. Practical Example

Suppose we have student data:

```python
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Age": [21, 22, 20, 21],
    "Marks": [85, 92, 78, 88],
    "City": [
        "Lucknow",
        "Delhi",
        "Lucknow",
        "Mumbai"
    ]
}

df = pd.DataFrame(data)

print(df)
```

---

## Filtering Students

```python
result = df[
    df["Marks"] > 80
]

print(result)
```

---

### Example Output

```text
    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
```

Only students with marks greater than `80` are included.

## Sorting Students

```python
result = df.sort_values(
    "Marks",
    ascending=False
)

print(result)
```

---

### Example Output

```text
    Name  Age  Marks     City
4  Arjun   23     95    Delhi
1   Riya   22     92    Delhi
3   Neha   21     88   Mumbai
0   Aman   21     85  Lucknow
2  Rahul   20     78  Lucknow
5   Sara   22     76  Mumbai
```

## Average Marks

```python
average = df["Marks"].mean()

print(average)
```

---

### Example Output

```text
85.66666666666667
```

## City-wise Average Marks

```python
result = df.groupby(
    "City"
)["Marks"].mean()

print(result)
```

---
### Example: Complete Small Analysis

Using the student DataFrame above:

```python
print("Average marks:", df["Marks"].mean())
print()
print(df[df["Marks"] > 80])
```

Output:

```text
Average marks: 85.66666666666667

    Name  Age  Marks     City
0   Aman   21     85  Lucknow
1   Riya   22     92    Delhi
3   Neha   21     88   Mumbai
4  Arjun   23     95    Delhi
```

This shows the typical pattern: **create/load data → inspect → filter → calculate**.

# 145. Practical Data Analysis Workflow

Pandas is often used with:

```text
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
Machine Learning
```

Pandas is commonly used as the data preparation and analysis layer before visualization or Machine Learning.

---

# 146. Commonly Used Pandas Functions

```python
pd.Series()
pd.DataFrame()

pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_html()
pd.read_sql()

pd.concat()
pd.merge()
pd.crosstab()
pd.pivot_table()

pd.to_datetime()
pd.to_numeric()
pd.cut()
pd.qcut()
pd.factorize()
pd.get_dummies()
```

---

# 147. Common DataFrame Methods

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.index
df.dtypes

df.loc[]
df.iloc[]
df.at[]
df.iat[]

df.sort_values()
df.sort_index()

df.drop()
df.dropna()
df.fillna()
df.replace()

df.rename()
df.reset_index()
df.set_index()

df.drop_duplicates()
df.value_counts()
df.apply()
df.map()
df.groupby()

df.pivot()
df.melt()
df.stack()
df.unstack()
df.explode()

df.join()
df.compare()

df.sample()
df.copy()
df.memory_usage()
```

---

# 148. Important Pandas Concepts

The important concepts to remember are:

* Series
* DataFrame
* Index
* Columns
* Data Types
* Selection
* Boolean Indexing
* Missing Data
* Duplicate Data
* Sorting
* Filtering
* GroupBy
* Aggregation
* Merge
* Join
* Concatenation
* Reshaping
* Pivot Tables
* Text Processing
* Categorical Data
* DateTime
* Time Series
* Timedelta
* Rolling Windows
* Expanding Windows
* MultiIndex
* Data Visualization
* File Input/Output
* Performance
* Memory Management

---

# 149. Pandas and Machine Learning

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

# 150. Best Practices

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

# 151. Performance Considerations

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

# 152. Pandas with Matplotlib

Pandas can directly create visualizations using Matplotlib.

Example:

```python
import matplotlib.pyplot as plt

df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.show()
```

---

# 153. Pandas with NumPy

Pandas and NumPy are commonly used together.

```python
import numpy as np
import pandas as pd

data = np.arange(1, 11)

df = pd.DataFrame({
    "Numbers": data
})

print(df)
```

---

# 154. Summary

Pandas is one of the most important Python libraries for data analysis.

In this guide, we covered:

* Introduction to Pandas
* Installation
* Importing Pandas
* Series
* DataFrame
* Creating DataFrames
* DataFrame attributes
* Viewing data
* CSV files
* Excel files
* JSON files
* HTML tables
* SQL data
* Selecting rows and columns
* `loc[]`
* `iloc[]`
* `at[]`
* `iat[]`
* Boolean indexing
* `isin()`
* `query()`
* Adding columns
* Updating columns
* Renaming columns
* Dropping rows and columns
* Reindexing
* Setting and resetting index
* Sorting
* Duplicate data
* Missing data
* Filling missing values
* Replacing values
* Data types
* Numeric conversion
* String operations
* Vectorized operations
* Descriptive statistics
* `value_counts()`
* `unique()`
* `nunique()`
* `apply()`
* `map()`
* GroupBy
* Aggregation
* Transformation
* Filtering groups
* Concatenation
* Merge
* Join
* Comparing DataFrames
* Pivot
* Pivot table
* Melt
* Stack and unstack
* Explode
* Crosstab
* Cut and qcut
* Factorize
* Categorical data
* Date and time
* Time series
* Resampling
* Time zones
* Timedelta
* Rolling windows
* Expanding windows
* Exponentially weighted windows
* Cumulative operations
* Ranking
* Sampling
* Memory usage
* Copying
* Copy-on-Write
* MultiIndex
* Duplicate labels
* Nullable data types
* Pandas plotting
* DataFrame styling
* `eval()`
* Large dataset handling
* Sparse data
* Parquet
* Feather
* Pickle
* HDF5
* Clipboard
* NumPy integration
* Conditional operations
* SQL-style merging
* One-hot encoding
* Data cleaning
* Data analysis workflow
* Machine Learning data preparation
* Performance considerations
* Best practices

Pandas provides the tools required to load, clean, transform, analyse and prepare structured data for visualization and Machine Learning.
