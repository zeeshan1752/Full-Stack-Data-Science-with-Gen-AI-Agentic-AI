from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

# Load and inspect the raw data
df = pd.read_csv(BASE_DIR / "employee_raw_data.csv")
print("First five rows:\n", df.head())
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values before cleaning:\n", df.isna().sum())
print("Duplicate rows before cleaning:", df.duplicated().sum())

# Standardize column names and text
raw_rows = len(df)
df.columns = (df.columns.str.strip().str.lower()
              .str.replace(r"[^a-z0-9]+", "_", regex=True)
              .str.strip("_"))
df["employee_name"] = df["employee_name"].astype("string").str.strip().str.title()
df["department"] = df["department"].astype("string").str.strip().str.title()
df["email"] = df["email"].astype("string").str.strip().str.lower()

# Convert values to appropriate data types
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["experience"] = pd.to_numeric(df["experience"], errors="coerce")
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

# Remove exact duplicate records
df = df.drop_duplicates().copy()

# Validate age range; mark implausible ages as missing for this example
invalid_age = ~df["age"].between(18, 65) & df["age"].notna()
print("\nImplausible age records:\n", df.loc[invalid_age, ["employee_name", "age"]])
df.loc[invalid_age, "age"] = np.nan

# Handle missing numeric values with medians for this practice dataset
for column in ["age", "salary"]:
    df[column] = df[column].fillna(df[column].median())

# Validate email-like format; this does not confirm the address exists
df["email_valid"] = df["email"].str.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", na=False)

# Create helpful features from existing columns
df["join_year"] = df["join_date"].dt.year
df["years_since_joining"] = (pd.Timestamp("2026-01-01") - df["join_date"]).dt.days / 365.25
df["experience_band"] = pd.cut(df["experience"], bins=[-1, 2, 5, 10, np.inf], labels=["0-2", "3-5", "6-10", "10+"])

# Detect potential salary outliers using the IQR rule
q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[df["salary"].lt(lower_bound) | df["salary"].gt(upper_bound)]
print("\nPotential salary outliers:\n", outliers[["employee_name", "salary"]])

# Check data quality after cleaning
print("\nRows before cleaning:", raw_rows)
print("Rows after cleaning:", len(df))
print("Missing values after cleaning:\n", df.isna().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
df.to_csv(BASE_DIR / "employee_cleaned_data.csv", index=False)
print("\nSaved employee_cleaned_data.csv")

sns.set_theme(palette='deep')

# Histogram and KDE for salary distribution
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["salary"], bins=7, kde=True, color="blue", ax=ax)
ax.set(title="Salary Distribution", xlabel="Salary", ylabel="Employee Count")
fig.tight_layout()
fig.savefig(IMAGE_DIR / "salary_distribution.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Bar chart for average salary by department
fig, ax = plt.subplots(figsize=(8, 5))
df.groupby("department", observed=True)["salary"].mean().sort_values().plot(kind="bar", ax=ax)
ax.set(title="Average Salary by Department", xlabel="Department", ylabel="Average Salary")
ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
fig.savefig(IMAGE_DIR / "average_salary_by_department.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Scatter plot for experience versus salary
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x="experience", y="salary", hue="department", ax=ax)
ax.set(title="Experience vs Salary", xlabel="Years of Experience", ylabel="Salary")
fig.tight_layout()
fig.savefig(IMAGE_DIR / "experience_vs_salary.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Box plot to compare salary distributions and flag potential outliers
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="department", y="salary", ax=ax)
ax.set(title="Salary by Department: Box Plot", xlabel="Department", ylabel="Salary")
ax.tick_params(axis="x", rotation=20)
fig.tight_layout()
fig.savefig(IMAGE_DIR / "salary_box_plot.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Violin plot for distribution shape by department
fig, ax = plt.subplots(figsize=(8, 5))
sns.violinplot(data=df, x="department", y="salary", inner="quartile", ax=ax)
ax.set(title="Salary Distribution by Department", xlabel="Department", ylabel="Salary")
ax.tick_params(axis="x", rotation=20)
fig.tight_layout()
fig.savefig(IMAGE_DIR / "salary_violin_plot.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Correlation heatmap for selected numeric variables
fig, ax = plt.subplots(figsize=(8, 6))
corr = df[["age", "experience", "salary", "performance_rating"]].corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", center=0, cmap="coolwarm", ax=ax)
ax.set_title("Correlation Heatmap")
fig.tight_layout()
fig.savefig(IMAGE_DIR / "correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Pair plot for multiple numeric variables
pair_grid = sns.pairplot(df[["age", "experience", "salary", "performance_rating"]], corner=True, diag_kws={"color": "blue"})
pair_grid.fig.suptitle("Pair Plot of Numeric Variables", y=1.02)
pair_grid.savefig(IMAGE_DIR / "pair_plot.png", dpi=150, bbox_inches="tight")
plt.close("all")

# Two plots in one figure using subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df["salary"], bins=7, kde=True, color="blue", ax=axes[0])
axes[0].set_title("Salary Distribution")
df.groupby("department", observed=True)["salary"].mean().plot(kind="bar", ax=axes[1])
axes[1].set_title("Mean Salary by Department")
axes[1].tick_params(axis="x", rotation=30)
fig.tight_layout()
fig.savefig(IMAGE_DIR / "combined_subplots.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Saved charts to:", IMAGE_DIR)
