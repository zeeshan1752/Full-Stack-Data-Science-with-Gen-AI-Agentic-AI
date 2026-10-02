# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw employee data
employee = pd.read_excel("employee_raw_data.xlsx")
print(employee.head())
print("Shape:", employee.shape)

# Check missing values and duplicates
print(employee.isnull().sum())
print("Duplicate rows:", employee.duplicated().sum())

# Clean text and numeric-like columns
clean_data = employee.copy()

for column in ["Name", "Domain", "Location"]:
    clean_data[column] = clean_data[column].astype("string").str.replace(r"\W+", "", regex=True)
    clean_data.loc[employee[column].isna(), column] = pd.NA

for column in ["Age", "Salary", "Exp"]:
    clean_data[column] = clean_data[column].astype("string").str.extract(r"(\d+)", expand=False)
    clean_data[column] = pd.to_numeric(clean_data[column], errors="coerce")

# Treat missing values with median/mode as an example
for column in ["Age", "Salary", "Exp"]:
    if clean_data[column].notna().any():
        clean_data[column] = clean_data[column].fillna(clean_data[column].median())

for column in ["Name", "Domain", "Location"]:
    if clean_data[column].notna().any():
        clean_data[column] = clean_data[column].fillna(clean_data[column].mode().iloc[0])

# Variable identification
X = clean_data[["Name", "Domain", "Age", "Location", "Exp"]]
y = clean_data[["Salary"]]

# Univariate analysis
print(clean_data[["Age", "Salary", "Exp"]].describe())
sns.histplot(data=clean_data, x="Salary", kde=True)
plt.title("Salary Distribution")
plt.tight_layout()
plt.show()

# Bivariate analysis
sns.scatterplot(data=clean_data, x="Exp", y="Salary", hue="Domain")
plt.title("Experience vs Salary")
plt.tight_layout()
plt.show()

# Outlier detection using IQR
for column in ["Age", "Salary", "Exp"]:
    q1 = clean_data[column].quantile(0.25)
    q3 = clean_data[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = clean_data[(clean_data[column] < lower_bound) | (clean_data[column] > upper_bound)]
    print(f"{column}: {len(outliers)} possible outlier(s)")

# Feature creation
clean_data["Experience_Level"] = pd.cut(
    clean_data["Exp"],
    bins=[-float("inf"), 2, 5, float("inf")],
    labels=["Beginner", "Intermediate", "Experienced"]
)

# Save cleaned data
clean_data.to_csv("employee_cleaned_data_from_script.csv", index=False)
print("Saved employee_cleaned_data_from_script.csv")
