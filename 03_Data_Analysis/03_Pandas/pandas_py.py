# Pandas Introduction and Importing Pandas

import pandas as pd
from pathlib import Path

print(pd.__version__)


# Creating a Series

data = [10, 20, 30, 40, 50]

series = pd.Series(data)

print(series)


# Creating a Series with Custom Index

marks = [85, 90, 78, 92]

students = ["Aman", "Rahul", "Zoya", "Ali"]

series = pd.Series(marks, index=students)

print(series)


# Accessing Series Elements

print(series["Aman"])
print(series.iloc[1])


# Creating a DataFrame

data = {
    "Name": ["Aman", "Rahul", "Zoya", "Ali"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)


# DataFrame Properties

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)


# Viewing Data

print(df.head())
print(df.tail())
print(df.head(2))
print(df.tail(2))


# Selecting a Column

print(df["Name"])
print(df["Marks"])


# Selecting Multiple Columns

print(df[["Name", "Marks"]])


# Selecting Rows using iloc

print(df.iloc[0])
print(df.iloc[1:3])


# Selecting Rows and Columns using iloc

print(df.iloc[0:3, 0:2])


# Selecting Rows using loc

print(df.loc[0])
print(df.loc[1:3, ["Name", "Marks"]])


# Adding a New Column

df["Result"] = ["Pass", "Pass", "Pass", "Pass"]

print(df)


# Updating a Column

df["Marks"] = df["Marks"] + 5

print(df)


# Filtering Data

print(df[df["Marks"] > 85])


# Multiple Conditions

print(df[(df["Marks"] > 80) & (df["Age"] > 19)])


# Sorting Data

print(df.sort_values("Marks"))

print(df.sort_values("Marks", ascending=False))


# Handling Missing Values

data = {
    "Name": ["Aman", "Rahul", "Zoya", "Ali"],
    "Marks": [85, None, 92, 88]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.dropna())

print(df.fillna(0))


# Renaming Columns

df = df.rename(columns={"Marks": "Score"})

print(df)


# Basic Statistical Functions

data = {
    "Marks": [85, 78, 92, 88, 75]
}

df = pd.DataFrame(data)

print(df["Marks"].mean())
print(df["Marks"].sum())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].median())


# Reading a CSV File

df = pd.read_csv(Path(__file__).with_name("students.csv"))

print(df)


# Writing DataFrame to CSV

df.to_csv(Path(__file__).with_name("students_output.csv"), index=False)


# GroupBy

data = {
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
    "Marks": [85, 90, 78, 82, 88]
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Marks"].mean())


# Value Counts

data = ["CSE", "ECE", "CSE", "ME", "CSE", "ECE"]

series = pd.Series(data)

print(series.value_counts())


# Applying a Function

df = pd.DataFrame({
    "Marks": [45, 67, 89, 32, 76]
})

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(df)