# Descriptive Statistics

Descriptive statistics is the branch of statistics concerned with **organising, summarising, analysing, and presenting observed data** in a meaningful form.

In Data Science, datasets may contain thousands or millions of observations. Examining every observation individually is often impractical. Descriptive statistics helps us understand the centre, spread, distribution, and unusual values in a dataset before performing further analysis or building machine learning models.

For example, before developing a house-price prediction model, we should understand the typical house price, the variation in prices, the presence of unusually expensive properties, and the distributions of numerical features.

This chapter covers the major descriptive statistical measures, their mathematical foundations, worked examples, and practical implementation using Python, NumPy, pandas, and Matplotlib.

---

## 1. Introduction to Descriptive Statistics

Descriptive statistics summarises the data we have observed. It helps us understand the characteristics of a dataset without, by itself, making conclusions about an entire population or establishing causal relationships.

For example, suppose a dataset contains examination scores from 1,000 students. We can calculate the mean, median, minimum, maximum, standard deviation, and percentiles to understand their performance.

A typical descriptive analysis follows this process:

**Raw Data → Data Organisation → Statistical Summaries → Visualisation → Interpretation**

### 1.1 Main Categories of Descriptive Statistics

| Category | Purpose | Important Measures |
|---|---|---|
| Central tendency | Describes the centre of the data | Mean, median, mode |
| Dispersion | Describes the spread of observations | Range, variance, standard deviation, IQR |
| Position | Describes the relative position of observations | Quartiles, percentiles, deciles |
| Distribution shape | Describes the shape and asymmetry of data | Skewness, kurtosis |
| Frequency | Describes how often values occur | Frequency, relative frequency |

A good descriptive analysis examines both **central tendency and dispersion**. Two datasets can have the same mean but very different amounts of variability.

## 2. Frequency Distribution

A frequency distribution organises data by showing how often each value or category occurs. It makes large datasets easier to understand.

Consider the following examination scores:

`72, 45, 81, 63, 55, 90, 38, 76, 63, 50`

Arranging them in ascending order gives:

`38, 45, 50, 55, 63, 63, 72, 76, 81, 90`

### 2.1 Frequency

Frequency is the number of times a particular value or category appears.

Consider the data:

`10, 20, 20, 30, 20, 40, 30, 20`

| Value | Frequency |
|---:|---:|
| 10 | 1 |
| 20 | 4 |
| 30 | 2 |
| 40 | 1 |
| **Total** | **8** |

The value 20 occurs four times.

### 2.2 Relative Frequency

Relative frequency represents the proportion of observations belonging to a particular value or category.

$$
\text{Relative Frequency}=\frac{f}{n}
$$

Here, \(f\) represents the frequency of a value and \(n\) represents the total number of observations.

For the value 20:

$$
\text{Relative Frequency}=\frac{4}{8}=0.5
$$

Therefore, 50% of the observations have the value 20.

The percentage frequency is calculated as:

$$
\text{Percentage Frequency}=\frac{f}{n}\times100
$$

### 2.3 Grouped Frequency Distribution

When numerical data contains many distinct values, observations can be grouped into intervals.

| Score Interval | Frequency |
|---|---:|
| 0–10 | 2 |
| 11–20 | 5 |
| 21–30 | 9 |
| 31–40 | 12 |
| 41–50 | 7 |

Each interval is called a **class interval**. Grouping makes large datasets easier to summarise, although it reduces information about individual observations.

For approximately equal-width classes:

$$
\text{Class Width}\approx\frac{\text{Range}}{\text{Number of Classes}}
$$

The exact class width depends on the class boundaries and interval convention used.

## 3. Measures of Central Tendency

Measures of central tendency describe the centre or typical value of a dataset. The three principal measures are the mean, median, and mode.

### 3.1 Arithmetic Mean

The arithmetic mean is the sum of all observations divided by the number of observations.

For a population:

$$
\mu=\frac{\sum_{i=1}^{N}x_i}{N}
$$

For a sample:

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

Here:

- \(x_i\) is an individual observation.
- \(N\) is the population size.
- \(n\) is the sample size.
- \(\mu\) is the population mean.
- \(\bar{x}\) is the sample mean.

**Worked example**

Consider the observations:

`10, 20, 30, 40, 50`

First, calculate their sum:

$$
10+20+30+40+50=150
$$

There are five observations.

$$
\bar{x}=\frac{150}{5}=30
$$

**Answer:** The mean is 30.

The mean uses every observation, making it useful for summarising numerical data. However, it is sensitive to extreme values.

For example, if 500 is added to the original dataset:

$$
\bar{x}=\frac{10+20+30+40+50+500}{6}
$$

$$
\bar{x}\approx108.33
$$

One extreme observation has substantially increased the mean.

### 3.2 Weighted Mean

A weighted mean is used when different observations contribute unequally to the result.

$$
\bar{x}_w=\frac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}
$$

Here, \(x_i\) is an observation and \(w_i\) is its weight.

**Worked example**

A student's assessment results are:

| Assessment | Score | Weight |
|---|---:|---:|
| Assignment | 80 | 2 |
| Midterm | 70 | 3 |
| Final examination | 90 | 5 |

Calculate the weighted total:

$$
80(2)+70(3)+90(5)=820
$$

Calculate the sum of weights:

$$
2+3+5=10
$$

Therefore:

$$
\bar{x}_w=\frac{820}{10}=82
$$

**Answer:** The weighted mean is 82.

Weighted means are useful for calculating weighted grades, aggregating observations with different importance, and summarising grouped data when appropriate weights are available.

### 3.3 Median

The median is the middle value after the observations have been arranged in ascending or descending order.

For an odd number of observations:

`10, 20, 30, 40, 50`

The median is 30.

For an even number of observations, take the average of the two middle values.

`10, 20, 30, 40, 50, 60`

$$
\text{Median}=\frac{30+40}{2}=35
$$

The median is generally less affected by extreme values than the mean. It is particularly useful for skewed distributions, such as income and house prices.

### 3.4 Mode

The mode is the value or category that occurs most frequently.

Example:

`10, 20, 20, 30, 20, 40`

The mode is 20 because it appears three times.

A dataset can be:

- **Unimodal:** one mode.
- **Bimodal:** two modes.
- **Multimodal:** more than two modes.
- **Without a unique mode:** no value occurs more frequently than the others.

The mode is useful for categorical data, such as the most common payment method, product category, or customer segment.

### 3.5 Comparison of Mean, Median, and Mode

| Measure | Meaning | Sensitivity to Extreme Values | Common Use |
|---|---|---|---|
| Mean | Arithmetic average | High | Numerical data |
| Median | Middle ordered value | Low | Skewed numerical data |
| Mode | Most frequent value or category | Depends on the data | Numerical and categorical data |

For a roughly symmetric distribution without strong outliers, the mean may be a useful measure of centre. For strongly skewed data, the median may provide a more representative summary.

## 4. Measures of Dispersion

Dispersion describes how widely observations are spread out.

Consider two datasets:

- Dataset A: `48, 49, 50, 51, 52`
- Dataset B: `10, 30, 50, 70, 90`

Both have a mean of 50, but Dataset B has much greater variability.

Important measures of dispersion include range, variance, standard deviation, and interquartile range.

### 4.1 Range

The range is the difference between the maximum and minimum values.

$$
R=x_{\max}-x_{\min}
$$

Example:

`12, 15, 20, 27, 30`

$$
R=30-12=18
$$

**Answer:** The range is 18.

The range is simple to calculate but depends only on the two extreme observations.

### 4.2 Variance

Variance measures the average squared deviation from the mean. The population and sample formulas differ.

**Population variance**

$$
\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

**Sample variance**

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Here, \(\mu\) is the population mean and \(\bar{x}\) is the sample mean.

Squaring deviations prevents positive and negative differences from cancelling each other.

**Worked example: Sample variance**

Consider:

`2, 4, 6`

First, calculate the mean:

$$
\bar{x}=\frac{2+4+6}{3}=4
$$

Calculate the deviations and their squares:

| Observation | Deviation | Squared Deviation |
|---:|---:|---:|
| 2 | -2 | 4 |
| 4 | 0 | 0 |
| 6 | 2 | 4 |
| **Total** | | **8** |

Because the observations are treated as a sample, divide by \(n-1\):

$$
s^2=\frac{8}{3-1}=\frac{8}{2}=4
$$

**Answer:** The sample variance is 4.

### 4.3 Population Variance vs Sample Variance

Use population variance when the dataset represents the entire population of interest. Use sample variance when observations are a sample used to estimate population variability.

The sample variance formula uses \(n-1\), known as **Bessel's correction**, to provide an unbiased estimate of population variance under the usual random-sampling assumptions.

| Feature | Population Variance | Sample Variance |
|---|---|---|
| Denominator | \(N\) | \(n-1\) |
| Mean used | Population mean, \(\mu\) | Sample mean, \(\bar{x}\) |
| Symbol | \(\sigma^2\) | \(s^2\) |

### 4.4 Standard Deviation

Standard deviation is the square root of variance.

**Population standard deviation**

$$
\sigma=\sqrt{\sigma^2}
$$

**Sample standard deviation**

$$
s=\sqrt{s^2}
$$

From the previous example:

$$
s=\sqrt{4}=2
$$

**Answer:** The sample standard deviation is 2.

Standard deviation is expressed in the same units as the original observations. For example, if data is measured in kilograms, variance is measured in squared kilograms, whereas standard deviation is measured in kilograms.

A larger standard deviation generally indicates greater spread around the mean.

## 5. Quartiles, Percentiles, and Deciles

These measures describe the relative position of observations within an ordered dataset.

### 5.1 Quartiles

Quartiles divide ordered data into four approximately equal parts.

- \(Q_1\): First quartile, approximately the 25th percentile.
- \(Q_2\): Second quartile, the median or 50th percentile.
- \(Q_3\): Third quartile, approximately the 75th percentile.

The precise quartile values depend on the calculation method used by a textbook or software package.

### 5.2 Percentiles

The \(p\)th percentile is a value below which approximately \(p\%\) of observations fall, according to the selected percentile convention.

Examples include:

- 25th percentile: approximately \(Q_1\).
- 50th percentile: median.
- 75th percentile: approximately \(Q_3\).
- 90th percentile: a value marking the 90th percentile position.

**Percentile is not the same as percentage.** A student at the 90th percentile has a relative position in a score distribution; this does not necessarily mean that the student scored 90 marks out of 100.

### 5.3 Deciles

Deciles divide ordered data into ten approximately equal parts. The deciles \(D_1\) through \(D_9\) correspond approximately to the 10th through 90th percentiles.

Quartiles, percentiles, and deciles are useful for analysing customer spending, salary distributions, examination rankings, and other relative positions.

## 6. Interquartile Range (IQR)

The interquartile range measures the spread of the middle 50% of observations.

$$
IQR=Q_3-Q_1
$$

Suppose:

$$
Q_1=20,\qquad Q_3=50
$$

Then:

$$
IQR=50-20=30
$$

**Answer:** The interquartile range is 30.

The IQR is generally less affected by extreme observations than the range or standard deviation because it uses the first and third quartiles rather than the minimum and maximum.

## 7. Five-Number Summary and Box Plot

The five-number summary provides a compact description of a dataset.

It contains:

1. Minimum
2. First quartile (\(Q_1\))
3. Median (\(Q_2\))
4. Third quartile (\(Q_3\))
5. Maximum

Example:

| Measure | Value |
|---|---:|
| Minimum | 10 |
| \(Q_1\) | 20 |
| Median | 35 |
| \(Q_3\) | 50 |
| Maximum | 80 |

A **box plot** visualises the median, quartiles, spread, and potential outliers. The box extends from \(Q_1\) to \(Q_3\), with a line marking the median.

### 7.1 IQR Rule for Potential Outliers

A commonly used convention identifies potential outliers using the following fences.

**Lower fence**

$$
Q_1-1.5(IQR)
$$

**Upper fence**

$$
Q_3+1.5(IQR)
$$

An observation below the lower fence or above the upper fence is flagged as a potential outlier.

These fences do not prove that an observation is incorrect. Box plots commonly display observations outside the fences separately, with whiskers extending to the most extreme observations within the fences.

## 8. Outliers and Their Effects

An outlier is an observation that lies unusually far from the rest of the data.

Example:

`10, 12, 13, 14, 15, 100`

The value 100 is substantially larger than the other observations.

Outliers may result from:

- Data-entry or measurement errors.
- Rare events.
- Unusual but genuine behaviour.
- Differences between groups.
- Changes in the data-generating process.

Outliers can strongly affect:

- Mean
- Range
- Variance
- Standard deviation

The median and IQR are generally more resistant to extreme values.

In Data Science, investigate outliers before removing them. An unusually expensive house might be a data error, but it could also represent a genuine luxury property. Removing valid observations without justification can introduce bias into an analysis or model.

## 9. Coefficient of Variation (CV)

The coefficient of variation measures variability relative to the mean.

For a sample with a non-zero mean:

$$
CV=\frac{s}{\bar{x}}\times100\%
$$

For a population with a non-zero mean:

$$
CV=\frac{\sigma}{\mu}\times100\%
$$

Suppose the sample mean is 50 and the sample standard deviation is 5.

$$
CV=\frac{5}{50}\times100\%=10\%
$$

**Answer:** The coefficient of variation is 10%.

CV can help compare relative variability across datasets measured on suitable ratio scales. It should be interpreted carefully when the mean is zero, close to zero, negative, or when the measurement scale lacks a meaningful zero.

## 10. Distribution Shape

Understanding distribution shape helps identify asymmetry, unusual tails, and patterns that may not be apparent from the mean or standard deviation alone.

### 10.1 Skewness

Skewness describes the asymmetry of a distribution.

**Symmetric distribution**

A distribution is approximately symmetric when its left and right sides have similar shapes. For a symmetric, unimodal distribution, the mean and median are often close. In an ideal normal distribution, the mean, median, and mode are equal.

**Right-skewed distribution**

A right-skewed distribution has a longer tail towards larger values. The mean is often greater than the median because large observations pull the mean to the right.

Examples may include income, house prices, and customer spending.

**Left-skewed distribution**

A left-skewed distribution has a longer tail towards smaller values. The mean is often less than the median because small observations pull the mean to the left.

The relationship between the mean and median is only a clue to skewness. A histogram or another distribution plot should also be examined.

### 10.2 Kurtosis

Kurtosis describes aspects of a distribution's shape and tail behaviour.

Common classifications include:

- **Mesokurtic:** kurtosis similar to the normal distribution under the selected definition.
- **Leptokurtic:** higher kurtosis than the normal distribution, commonly associated with heavier tails.
- **Platykurtic:** lower kurtosis than the normal distribution, commonly associated with lighter tails.

Kurtosis should not be interpreted only as peak height. Tail behaviour is an important part of its interpretation.

For Data Science, use distribution plots and investigate extreme observations rather than relying on a single shape statistic.

## 11. Choosing the Right Descriptive Measure

The appropriate measure depends on the type of data, its distribution, and the purpose of the analysis.

| Situation | Useful Measure |
|---|---|
| Numerical data without strong outliers | Mean and standard deviation |
| Strongly skewed numerical data | Median and IQR |
| Most common category | Mode |
| Quick measure of total spread | Range |
| Spread around the mean | Variance and standard deviation |
| Spread of the middle 50% | IQR |
| Relative position in a distribution | Percentiles |
| Compact summary of centre and spread | Five-number summary |
| Relative variability on suitable ratio scales | Coefficient of variation |

No single measure is best for every dataset. It is often useful to report more than one measure to understand the data more completely.

## 12. Visualising Descriptive Statistics

Visualisation helps reveal patterns that a numerical summary might hide.

### 12.1 Histogram

A histogram groups numerical observations into bins and displays their frequencies. It helps reveal concentration, spread, skewness, gaps, and possible multiple peaks.

### 12.2 Bar Chart

A bar chart compares values across categories, such as customer counts by region or product category.

### 12.3 Box Plot

A box plot summarises the median, quartiles, and potential outliers. It is particularly useful for comparing numerical distributions across groups.

### 12.4 Choosing a Visualisation

| Data or Question | Suitable Visualisation |
|---|---|
| Distribution of a numerical feature | Histogram |
| Compare categorical counts | Bar chart |
| Compare spread across groups | Box plot |
| Change over time | Line graph |
| Relationship between two numerical variables | Scatter plot |

Scatter plots are useful during Exploratory Data Analysis (EDA). Detailed study of relationships between numerical variables belongs in the Correlation folder.

## 13. Descriptive Statistics with Python

Python libraries make descriptive analysis easier to perform, reproduce, and apply to real datasets.

### 13.1 Using NumPy

NumPy provides functions for calculating the mean, median, variance, and standard deviation.

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))

print("Population variance:", np.var(data, ddof=0))
print("Sample variance:", np.var(data, ddof=1))

print("Population standard deviation:", np.std(data, ddof=0))
print("Sample standard deviation:", np.std(data, ddof=1))
```

Expected output:

```text
Mean: 30.0
Median: 30.0
Population variance: 200.0
Sample variance: 250.0
Population standard deviation: 14.142135623730951
Sample standard deviation: 15.811388300841896
```

**Important:** NumPy uses `ddof=0` by default, which divides by \(n\). Setting `ddof=1` divides by \(n-1\), giving the usual sample variance and sample standard deviation.

### 13.2 Calculating Percentiles and IQR

```python
import numpy as np

data = np.array([10, 12, 15, 18, 20, 22, 25, 30])

q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
q3 = np.percentile(data, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("IQR:", iqr)
```

Percentile results can depend on the selected calculation method. When comparing results with a textbook or another software package, use consistent conventions.

### 13.3 Using pandas

pandas is especially useful for analysing tabular datasets.

```python
import pandas as pd

df = pd.DataFrame({
    "Marks": [45, 55, 60, 70, 80, 90],
    "Study_Hours": [1, 2, 2, 3, 4, 5]
})

print(df.describe())
```

The `describe()` method provides numerical summaries, including count, mean, standard deviation, minimum, quartiles, and maximum.

Individual statistics can also be calculated:

```python
print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Standard deviation:", df["Marks"].std())
print("Minimum:", df["Marks"].min())
print("Maximum:", df["Marks"].max())
print("75th percentile:", df["Marks"].quantile(0.75))
```

By default, pandas uses sample standard deviation for a Series, equivalent to `ddof=1`.

For categorical columns, `describe()` reports different summaries, such as the number of non-missing observations, unique values, most frequent value, and its frequency.

## 14. Descriptive Statistics in Exploratory Data Analysis (EDA)

Exploratory Data Analysis is the process of examining a dataset to understand its structure, quality, patterns, and unusual observations before building a model.

Descriptive statistics is an important part of EDA.

A practical initial workflow is:

1. Inspect the dataset's rows, columns, and data types.
2. Check the number of missing values.
3. Calculate descriptive statistics for numerical columns.
4. Examine categorical frequencies.
5. Plot numerical distributions.
6. Investigate potential outliers.
7. Decide whether further cleaning or transformation is justified.

### 14.1 Practical Python Example

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Inspect the dataset
print(df.head())
print("Dataset shape:", df.shape)
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Summarise numerical columns
print(df.describe())

# Visualise a numerical feature
df["feature_name"].hist()

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Feature")
plt.show()
```

Replace `"data.csv"` and `"feature_name"` with the actual file name and column name.

Descriptive statistics can identify unusual ranges, highly skewed variables, possible data-entry problems, and differences in scale. However, they do not automatically determine how missing values or outliers should be treated. Those decisions require context and validation.

## 15. Feature Scaling: Connection to Machine Learning

Standardisation and min-max scaling are feature-scaling techniques used to change the scale of numerical features. They connect descriptive statistics with machine learning preprocessing.

### 15.1 Standardisation

Standardisation converts a value into a z-score by subtracting the mean and dividing by the standard deviation.

$$
z=\frac{x-\mu}{\sigma}
$$

Here, \(x\) is the observation, \(\mu\) is the mean, and \(\sigma\) is the standard deviation under the population convention.

A standardised value indicates how many standard deviations an observation lies from the mean.

### 15.2 Min-Max Scaling

Min-max scaling transforms values to a chosen range, commonly 0 to 1.

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

The formula requires \(x_{\max}\ne x_{\min}\).

### 15.3 Python Implementation

```python
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = np.array([[10], [20], [30], [40], [50]])

standard_scaler = StandardScaler()
standardised = standard_scaler.fit_transform(data)

minmax_scaler = MinMaxScaler()
normalised = minmax_scaler.fit_transform(data)

print("Standardised values:")
print(standardised)

print("Min-max scaled values:")
print(normalised)
```

Standardisation and min-max scaling are different operations. The appropriate method depends on the feature, algorithm, and data distribution.

**Important for machine learning:** fit the scaler on training data only, then use the fitted scaler to transform validation or test data. Fitting it on the complete dataset before splitting can leak information from the test set into training.

## 16. Common Mistakes in Descriptive Statistics

### 16.1 Using the Mean Without Checking Outliers

The mean can be misleading when extreme observations are present. Examine the median and distribution as well.

### 16.2 Confusing Variance and Standard Deviation

Variance is expressed in squared units, while standard deviation is expressed in the original units.

### 16.3 Using the Wrong Variance Formula

Population variance divides by \(N\). The usual sample variance estimator divides by \(n-1\).

### 16.4 Assuming Every Outlier Is an Error

Outliers can represent valid and important observations. Investigate their source before deciding how to handle them.

### 16.5 Confusing Percentile and Percentage

The 90th percentile describes relative position in a distribution. It does not mean a score of 90%.

### 16.6 Assuming the Mean Describes Every Dataset Well

For strongly skewed data, the median and IQR may provide a more useful summary.

### 16.7 Ignoring Missing Values

Statistics calculated after missing observations have been excluded may describe a different set of observations than expected. Always understand how missing values are handled.

### 16.8 Fitting a Scaler Before Splitting the Dataset

Fitting a scaler on both training and test data can cause data leakage. Fit preprocessing steps using training data only.

## 17. Points to Remember

1. Descriptive statistics summarises observed data.
2. Mean, median, and mode measure central tendency.
3. Range, variance, standard deviation, and IQR measure dispersion.
4. The mean is sensitive to extreme observations.
5. The median is generally more resistant to outliers.
6. Sample variance commonly uses \(n-1\) in the denominator.
7. Standard deviation is the square root of variance.
8. Quartiles divide ordered data into four approximately equal parts.
9. Percentiles describe relative position within a dataset.
10. The five-number summary contains the minimum, \(Q_1\), median, \(Q_3\), and maximum.
11. Box plots help compare distributions and flag potential outliers.
12. Skewness describes asymmetry; kurtosis describes aspects of distribution shape and tail behaviour.
13. NumPy's `ddof` determines the variance and standard-deviation denominator convention.
14. pandas `describe()` is useful for initial numerical summaries.
15. EDA should include numerical summaries, visualisation, and data-quality checks.
16. Outliers should be investigated rather than automatically deleted.
17. Standardisation and min-max scaling are different techniques.
18. Fit preprocessing transformations on training data only when evaluating predictive models.

## 18. Important Formula Summary

**Arithmetic mean**

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

**Weighted mean**

$$
\bar{x}_w=\frac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}
$$

**Relative frequency**

$$
\text{Relative Frequency}=\frac{f}{n}
$$

**Percentage frequency**

$$
\text{Percentage Frequency}=\frac{f}{n}\times100
$$

**Range**

$$
R=x_{\max}-x_{\min}
$$

**Population variance**

$$
\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

**Sample variance**

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

**Population standard deviation**

$$
\sigma=\sqrt{\sigma^2}
$$

**Sample standard deviation**

$$
s=\sqrt{s^2}
$$

**Interquartile range**

$$
IQR=Q_3-Q_1
$$

**Lower IQR fence**

$$
Q_1-1.5(IQR)
$$

**Upper IQR fence**

$$
Q_3+1.5(IQR)
$$

**Sample coefficient of variation**

$$
CV=\frac{s}{\bar{x}}\times100\%
$$

**Z-score standardisation**

$$
z=\frac{x-\mu}{\sigma}
$$

**Min-max scaling**

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

## 19. Chapter Summary

Descriptive statistics provides the foundation for understanding a dataset before applying advanced statistical methods or machine learning algorithms.

Measures of central tendency describe the centre of the data, while measures of dispersion describe its variability. Quartiles, percentiles, and the five-number summary explain relative position and spread. Skewness and kurtosis provide additional information about distribution shape.

In practical Data Science, these concepts are applied with Python, NumPy, pandas, and visualisation libraries to explore datasets, identify unusual observations, understand feature distributions, and guide further investigation.

Descriptive statistics does not replace data cleaning, inferential statistics, or model evaluation. Instead, it provides the understanding needed to apply those methods appropriately.

## 20. References and Further Reading

### GeeksforGeeks

- [Descriptive Statistics](https://www.geeksforgeeks.org/maths/descriptive-statistics/)
- [Mean, Median and Mode](https://www.geeksforgeeks.org/maths/mean-median-mode/)

### OpenStax

- [Measures of the Spread of the Data](https://openstax.org/books/introductory-statistics-2e/pages/2-7-measures-of-the-spread-of-the-data)
- [Box Plots](https://openstax.org/books/introductory-statistics-2e/pages/2-4-box-plots)
- [Histograms and Frequency Graphs](https://openstax.org/books/introductory-statistics-2e/pages/2-2-histograms-frequency-polygons-and-time-series-graphs)
- [Skewness and the Mean, Median, and Mode](https://openstax.org/books/introductory-statistics-2e/pages/2-6-skewness-and-the-mean-median-and-mode)

### Python Libraries

- [NumPy — Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [pandas — Descriptive Statistics](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics)
- [Matplotlib — Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [scikit-learn — Preprocessing Data](https://scikit-learn.org/stable/modules/preprocessing.html)

### Related Topics in This Repository

- Statistics Fundamentals
- Probability
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- ANOVA
- Chi-Square Test
- Correlation
- Regression
- Regression Model Evaluation
- Bias and Variance
- Statistics for Machine Learning
