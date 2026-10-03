# Data Analysis

Data Analysis is the process of collecting, organizing, cleaning, exploring, and understanding data to find useful information and make better decisions.

In real-life projects, data is often incomplete, unorganized, or difficult to understand. Data Analysis helps us convert raw data into meaningful information using Python libraries and different analytical techniques.

For example, an online shopping company can analyze its sales data to find its most popular products, identify monthly sales trends, understand customer behavior, and improve its business decisions.

## Topics and Their Real-Life Applications

### 01. NumPy

NumPy is a Python library used for numerical calculations and working with arrays. It is useful when we need to perform mathematical operations on large amounts of numerical data efficiently.

**When do we use it?**

- When performing calculations on large collections of numbers.
- When working with matrices and multidimensional arrays.
- When calculating averages, minimums, maximums, and standard deviations.
- When preparing numerical data for scientific computing and Machine Learning.

**Real-life example:**

Suppose a company records its daily sales for an entire year. NumPy can help calculate the average daily sales, identify the highest sales value, and perform calculations across the collected data.

### 02. Pandas

Pandas is a Python library used to organize, manipulate, and analyze structured data. It provides Series and DataFrames, which make it easier to work with data arranged in rows and columns.

**When do we use it?**

- When reading data from CSV files, Excel sheets, and other supported sources.
- When selecting specific rows and columns.
- When filtering records based on conditions.
- When grouping data and calculating summaries.
- When combining datasets and preparing reports.

**Real-life example:**

Suppose a company has an Excel file containing thousands of customer orders. Pandas can help identify orders from a particular city, calculate total sales for each product, and find customers who have placed the most orders.

### 03. Matplotlib

Matplotlib is a Python library used to create graphs and charts. It helps us present numerical information visually so that trends and differences are easier to understand.

**When do we use it?**

- When comparing values using bar charts.
- When tracking changes over time using line charts.
- When understanding the distribution of numerical data.
- When creating charts for reports and presentations.

**Real-life example:**

A company wants to understand how its monthly revenue changes throughout the year. A line chart can display revenue month by month, making it easier to identify periods of growth or decline.

### 04. Seaborn

Seaborn is a Python visualization library built on Matplotlib. It provides convenient ways to create statistical charts and understand relationships between variables.

**When do we use it?**

- When comparing distributions across different groups.
- When identifying relationships between numerical variables.
- When creating heatmaps to explore correlations.
- When examining outliers and patterns in datasets.

**Real-life example:**

A housing company wants to study whether house size is related to house price. A scatter plot created with Seaborn can help visualize the relationship and identify unusual properties.

A chart can reveal a pattern, but further analysis is needed before concluding that one variable causes changes in another.

### 05. Exploratory Data Analysis (EDA)

Exploratory Data Analysis is the process of examining a dataset before drawing conclusions or building a model. It helps us understand the structure, quality, distribution, and relationships within the data.

EDA commonly uses Pandas, NumPy, Matplotlib, Seaborn, and statistical techniques.

**When do we use it?**

- When starting work on a new dataset.
- When checking the number of records and available columns.
- When understanding data distributions and relationships.
- When identifying unusual values, patterns, and possible data quality issues.
- When deciding which analytical methods to use next.

**Real-life example:**

Suppose a hospital has patient records containing age, test results, appointment dates, and other information. EDA can help identify missing values, understand age distributions, examine appointment patterns, and discover areas that need further investigation.

EDA helps us understand the data before proceeding with deeper analysis or Machine Learning.

### 06. Data Cleaning

Data Cleaning is the process of identifying and correcting data quality problems. Real-world datasets often contain missing values, duplicate records, inconsistent formats, and incorrect entries.

**When do we use it?**

- When a dataset contains missing information.
- When the same record appears more than once.
- When dates, numbers, or categories use inconsistent formats.
- When values are outside expected ranges.
- When preparing data for reporting, analysis, or Machine Learning.

**Real-life example:**

An online store receives customer information from multiple sources. Some customers may appear more than once, phone numbers may use different formats, and some orders may have missing prices.

Data Cleaning helps resolve these problems according to the project's requirements and makes the dataset more reliable.

Not every unusual value should be deleted or changed. It should first be investigated to determine whether it represents an error or a valid observation.

### 07. Data Visualization

Data Visualization is the process of representing data through charts, graphs, and other visual formats. It helps people understand complex information without having to examine every row of a dataset.

Matplotlib and Seaborn are two tools that can be used for this purpose.

**When do we use it?**

- When presenting findings to managers or clients.
- When comparing products, regions, or business departments.
- When tracking performance over time.
- When communicating trends and unusual observations.
- When building analytical reports and dashboards.

**Real-life example:**

A retail business wants to compare sales across different cities and products. Bar charts can show which products generate more revenue, while line charts can display monthly sales trends.

The purpose is to communicate findings clearly and help people make informed decisions.

### 08. Kaggle

Kaggle is a data science platform that provides datasets, notebooks, learning resources, and competitions. It can be used to practice data analysis on datasets that are more realistic than small, manually created examples.

**When do we use it?**

- When looking for datasets for practice projects.
- When learning from public data science notebooks.
- When applying Pandas and visualization techniques to real datasets.
- When practicing EDA and Data Cleaning.
- When participating in data science competitions, if relevant to the learning goals.

**Real-life example:**

Suppose you want to analyze passenger data, movie ratings, or house prices. You can find a suitable dataset on Kaggle, load it into a Jupyter Notebook, inspect its columns, clean the data, perform EDA, and create visualizations to communicate your findings.

Kaggle is a platform rather than a data analysis technique. The analysis itself is performed using tools such as Pandas, NumPy, Matplotlib, and Seaborn.

## How These Topics Work Together

In a typical data analysis project, these topics are used together rather than independently.

For example, imagine analyzing sales data for an online store.

1. **NumPy:** Perform numerical calculations where needed.
2. **Pandas:** Load the sales dataset and organize its records.
3. **Data Cleaning:** Handle missing values, duplicates, and inconsistent data.
4. **EDA:** Examine sales distributions, product performance, and customer patterns.
5. **Matplotlib and Seaborn:** Create charts to explore and communicate findings.
6. **Data Visualization:** Present the important results in an understandable format.
7. **Kaggle:** Find practice datasets or notebooks to apply the complete workflow.

The exact order can change depending on the dataset and project. For example, you may create visualizations during EDA and discover data quality problems that require additional cleaning.

## Typical Data Analysis Workflow

```text
Raw Dataset
     |
     v
Load and Understand Data
     |
     v
Data Cleaning
     |
     v
Exploratory Data Analysis (EDA)
     |
     v
Data Visualization
     |
     v
Interpret Findings
     |
     v
Report and Decision-Making
```

NumPy and Pandas can support multiple stages, while Matplotlib and Seaborn can be used throughout EDA and reporting.

## Learning Goals

By studying these topics, I aim to:

- Work confidently with structured datasets using Python.
- Identify and handle common data quality problems.
- Explore datasets to discover useful patterns and relationships.
- Create clear and meaningful visualizations.
- Practice with real-world datasets.
- Prepare data for further analysis and Machine Learning.
- Communicate analytical findings in a clear and understandable way.

## Repository Structure

```text
03_Data_Analysis/
│
├── 01_NumPy/
├── 02_Pandas/
├── 03_Matplotlib/
├── 04_Seaborn/
├── 05_EDA/
├── 06_Data_Cleaning/
├── 07_Data_Visualization/
├── 08_Kaggle/
│
└── README.md
```

Each topic folder contains its own learning materials, notes, code examples, and practice exercises. This main README provides an overview of the topics and explains their practical uses.

## Progress

This folder is part of my **Full Stack Data Science with Gen AI & Agentic AI** learning journey. I will continue updating it as I learn new concepts and complete practical exercises.
