# Descriptive Statistics

Descriptive statistics is the branch of statistics concerned with **organising, summarising, analysing, and presenting observed data** in a meaningful form.

In Data Science, datasets may contain thousands or millions of rows. Examining every observation individually is often impractical. Descriptive statistics helps us understand the centre, spread, distribution, and unusual values of a dataset before making further decisions.

For example, before building a machine learning model to predict house prices, we should understand the average price, the median price, the variation in prices, the presence of unusually expensive houses, and the distribution of important numerical features.

This chapter covers the statistical concepts most useful for Data Science, with mathematical formulas, worked examples, Python implementation, and practical connections to Exploratory Data Analysis (EDA).

---

## 1. What Is Descriptive Statistics?

Descriptive statistics summarises the data we have observed. It helps us understand what the dataset contains without, by itself, making conclusions about an entire population or proving why a pattern exists.

Suppose we have the examination scores of 1,000 students. Instead of examining every score individually, we can calculate the mean, median, minimum, maximum, standard deviation, and percentiles. We can also use graphs to understand the distribution of scores.

A typical descriptive analysis follows this process:

**Raw Data → Data Organisation → Statistical Summaries → Visualisation → Interpretation**

In Data Science, descriptive statistics is one of the first steps in understanding a dataset.

## 2. Main Categories of Descriptive Statistics

Descriptive measures can be organised into four main categories.

| Category | Purpose | Important Measures |
|---|---|---|
| Central tendency | Describes the centre of the data | Mean, median, mode |
| Dispersion | Describes the spread of the data | Range, variance, standard deviation, IQR |
| Position | Describes the relative position of observations | Quartiles, percentiles, deciles |
| Shape | Describes the distribution's characteristics | Skewness, kurtosis |

Frequency distributions and graphs are also important because they help us organise and interpret data.

A good descriptive analysis usually examines both **central tendency and dispersion**. Two datasets can have the same mean but very different levels of variability.

## 3. Organising Data and Frequency Distribution

Consider the following examination scores:

`72, 45, 81, 63, 55, 90, 38, 76, 63, 50`

Arranging the observations in ascending order gives:

`38, 45, 50, 55, 63, 63, 72, 76, 81, 90`

The ordered data makes it easier to identify the minimum, maximum, median, and repeated values.

### 3.1 Frequency

Frequency is the number of times a particular value or category occurs.

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

### 3.2 Relative Frequency

Relative frequency represents the proportion of observations belonging to a particular value or category.

$$
\text{Relative Frequency}=\frac{f}{n}
$$

Here, \(f\) is the frequency and \(n\) is the total number of observations.

For the value 20:

$$
\text{Relative Frequency}=\frac{4}{8}=0.5
$$

The percentage frequency is:

$$
\text{Percentage Frequency}=\frac{f}{n}\times100
$$

Therefore, the value 20 represents 50% of the observations.

### 3.3 Grouped Frequency Distribution

When numerical data contains many distinct values, it may be useful to group the observations into intervals.

| Score Interval | Frequency |
|---|---:|
| 0–10 | 2 |
| 11–20 | 5 |
| 21–30 | 9 |
| 31–40 | 12 |
| 41–50 | 7 |

Each interval is called a **class interval**. Grouped frequency distributions summarise large datasets, although they lose some detail about individual observations.

For continuous class boundaries, class width can be calculated as:

$$
\text{Class Width}=\frac{\text{Range}}{\text{Number of Classes}}
$$

The exact width convention depends on the class boundaries used.

## 4. Measures of Central Tendency

Measures of central tendency describe the centre or typical value of a dataset. The three fundamental measures are the mean, median, and mode.

The appropriate measure depends on the type of data, its distribution, and the presence of outliers.

### 4.1 Arithmetic Mean

The arithmetic mean is the sum of all observations divided by the number of observations.

For a population:

$$
\mu=\frac{\sum_{i=1}^{N}x_i}{N}
$$

For a sample:

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

Here, \(x_i\) represents an observation, \(N\) is the population size, and \(n\) is the sample size.

**Example**

Consider the observations:

`10, 20, 30, 40, 50`

First, calculate the sum:

$$
10+20+30+40+50=150
$$

There are five observations, so:

$$
\bar{x}=\frac{150}{5}=30
$$

The mean is 30.

The mean uses every observation, which makes it useful for summarising numerical data. However, it can be strongly affected by extreme values.

For example, adding 500 to the original dataset changes the mean to:

$$
\bar{x}=\frac{10+20+30+40+50+500}{6}
$$

$$
\bar{x}\approx108.33
$$

One extreme observation substantially increases the mean.

### 4.2 Weighted Mean

A weighted mean is used when different observations contribute unequally to the result.

$$
\bar{x}_w=\frac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}
$$

Here, \(x_i\) is an observation and \(w_i\) is its weight.

**Example**

A student's assessment scores are:

| Assessment | Score | Weight |
|---|---:|---:|
| Assignment | 80 | 2 |
| Midterm | 70 | 3 |
| Final examination | 90 | 5 |

The weighted total is:

$$
80(2)+70(3)+90(5)=820
$$

The total weight is:

$$
2+3+5=10
$$

Therefore:

$$
\bar{x}_w=\frac{820}{10}=82
$$

The weighted mean is 82.

Weighted means are useful when calculating weighted averages, combining observations with different levels of importance, or summarising grouped data when the appropriate weights are known.

### 4.3 Median

The median is the middle value after observations are arranged in ascending or descending order.

For an odd number of observations, the median is the single middle value.

Example:

`10, 20, 30, 40, 50`

The median is 30.

For an even number of observations, the median is the average of the two middle values.

Example:

`10, 20, 30, 40, 50, 60`

$$
\text{Median}=\frac{30+40}{2}=35
$$

The median is less affected by extreme values than the mean. It is especially useful when a numerical dataset is strongly skewed or contains large outliers.

### 4.4 Mode

The mode is the value or category that occurs most frequently.

Example:

`10, 20, 20, 30, 20, 40`

The mode is 20 because it occurs three times.

A dataset may be:

- **Unimodal:** one mode.
- **Bimodal:** two modes.
- **Multimodal:** more than two modes.
- **Without a unique mode:** no value occurs more frequently than the others.

The mode is particularly useful for categorical data, such as the most common product category, payment method, or customer segment.

### 4.5 Comparison of Mean, Median, and Mode

| Measure | What It Represents | Sensitivity to Extreme Values |
|---|---|---|
| Mean | Arithmetic average | High |
| Median | Middle ordered value | Low |
| Mode | Most frequent value or category | Depends on the data |

For a roughly symmetric distribution without strong outliers, the mean may be a useful measure of centre. For strongly skewed data, the median may provide a more representative summary.

## 5. Measures of Dispersion

Dispersion describes how far observations are spread out from one another or from a central value.

Consider two datasets:

- Dataset A: `48, 49, 50, 51, 52`
- Dataset B: `10, 30, 50, 70, 90`

Both have a mean of 50, but Dataset B has much greater spread.

Important measures of dispersion include range, variance, standard deviation, interquartile range, and coefficient of variation.

### 5.1 Range

The range is the difference between the maximum and minimum values.

$$
R=x_{\max}-x_{\min}
$$

Example:

`12, 15, 20, 27, 30`

$$
R=30-12=18
$$

The range is 18.

The range is simple to calculate, but it depends only on the two extreme observations and ignores the distribution of the remaining values.

### 5.2 Variance

Variance measures the average squared deviation from the mean. The population and sample formulas are different.

**Population variance**

$$
\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

**Sample variance**

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Here, \(\mu\) is the population mean and \(\bar{x}\) is the sample mean.

Squaring the deviations prevents positive and negative differences from cancelling one another.

**Worked example: sample variance**

Consider:

`2, 4, 6`

First, calculate the mean:

$$
\bar{x}=\frac{2+4+6}{3}=4
$$

Next, calculate and square the deviations:

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

The sample variance is 4.

### 5.3 Population vs Sample Variance

Use population variance when the dataset represents the entire population of interest. Use sample variance when the observations are a sample used to estimate population variability.

The sample variance formula uses \(n-1\), known as **Bessel's correction**, to produce an unbiased estimate of population variance under the usual random-sampling assumptions.

| Feature | Population Variance | Sample Variance |
|---|---|---|
| Formula denominator | \(N\) | \(n-1\) |
| Mean used | Population mean \(\mu\) | Sample mean \(\bar{x}\) |
| Symbol | \(\sigma^2\) | \(s^2\) |

### 5.4 Standard Deviation

Standard deviation is the square root of variance.

**Population standard deviation**

$$
\sigma=\sqrt{\sigma^2}
$$

**Sample standard deviation**

$$
s=\sqrt{s^2}
$$

In the previous example:

$$
s=\sqrt{4}=2
$$

The sample standard deviation is 2.

Unlike variance, standard deviation is expressed in the same units as the original observations. For example, if the data is measured in kilograms, variance is measured in square kilograms, while standard deviation is measured in kilograms.

A larger standard deviation indicates greater spread around the mean, although its interpretation depends on the context and distribution of the data.

## 6. Quartiles, Percentiles, and Deciles

These measures describe the relative position of observations within an ordered dataset.

### 6.1 Quartiles

Quartiles divide ordered data into four parts.

- \(Q_1\), the first quartile, represents approximately the 25th percentile.
- \(Q_2\), the second quartile, is the median.
- \(Q_3\), the third quartile, represents approximately the 75th percentile.

The exact numerical values can vary depending on the quartile calculation method used by a textbook or software package.

### 6.2 Percentiles

The \(p\)th percentile is a value below which approximately \(p\%\) of observations fall, according to the selected percentile convention.

For example:

- 25th percentile: approximately \(Q_1\).
- 50th percentile: median.
- 75th percentile: approximately \(Q_3\).
- 90th percentile: a value marking the 90th percentile position.

A percentile is not the same as a percentage score. A student at the 90th percentile has a relative position in the score distribution; it does not necessarily mean that the student obtained 90 marks out of 100.

### 6.3 Deciles

Deciles divide ordered data into ten parts. The deciles \(D_1\) through \(D_9\) correspond approximately to the 10th through 90th percentiles.

Quartiles, percentiles, and deciles are useful for understanding rankings, customer spending levels, salary distributions, and the relative position of observations.

## 7. Interquartile Range (IQR)

The interquartile range measures the spread of the middle 50% of the data.

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

The interquartile range is 30.

Because it uses the first and third quartiles rather than the extreme values, the IQR is generally less affected by outliers than the range or standard deviation.

## 8. Five-Number Summary and Box Plot

The five-number summary gives a compact description of a dataset.

It consists of:

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

A **box plot** visualises quartiles, the median, spread, and possible outliers.

The box extends from \(Q_1\) to \(Q_3\), with the median marked inside it. The interquartile range is the width of the box on a horizontal box plot.

### 8.1 IQR Rule for Potential Outliers

A commonly used rule identifies observations outside the following fences as potential outliers:

**Lower fence**

$$
Q_1-1.5(IQR)
$$

**Upper fence**

$$
Q_3+1.5(IQR)
$$

An observation below the lower fence or above the upper fence is flagged as a potential outlier.

These fences are a statistical convention, not proof that an observation is incorrect. Some box-plot implementations draw whiskers only to the most extreme observations within the fences and display observations outside them separately.

## 9. Outliers and Their Effects

An outlier is an observation that is unusually distant from the rest of the data.

Example:

`10, 12, 13, 14, 15, 100`

The value 100 is much larger than the other observations.

Outliers can occur because of data-entry errors, measurement errors, rare events, unusual but genuine behaviour, or differences between groups.

Outliers may strongly affect:

- Mean
- Range
- Variance
- Standard deviation

They generally have less influence on:

- Median
- Interquartile range

In Data Science, investigate outliers before removing them. An unusual house price might be a data error, but it might also represent a genuine luxury property. Removing valid observations without understanding them can introduce bias into an analysis or model.

## 10. Coefficient of Variation (CV)

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

The coefficient of variation is 10%.

CV can help compare relative variability between datasets measured on comparable ratio scales, even when their means or units differ. It should be interpreted carefully when the mean is zero, close to zero, negative, or when the measurement scale does not have a meaningful zero.

## 11. Distribution Shape: Skewness

Skewness describes the asymmetry of a distribution.

### 11.1 Symmetric Distribution

A distribution is approximately symmetric when its left and right sides have similar shapes.

For a symmetric, unimodal distribution, the mean and median are often close to each other. They are also equal to the mode in some idealised distributions, such as a perfectly symmetric normal distribution.

### 11.2 Right-Skewed Distribution

A right-skewed distribution has a longer tail toward larger values.

The mean is often greater than the median because large observations pull the mean to the right.

Examples can include income, house prices, and customer spending.

### 11.3 Left-Skewed Distribution

A left-skewed distribution has a longer tail toward smaller values.

The mean is often less than the median because small observations pull the mean to the left.

The relationship between mean and median is a useful clue, but it is not sufficient on its own to establish skewness. A histogram or another distribution plot should also be examined.

## 12. Kurtosis

Kurtosis describes aspects of a distribution's tail behaviour and shape.

Common classifications include:

- **Mesokurtic:** kurtosis similar to the normal distribution under the selected definition.
- **Leptokurtic:** higher kurtosis than the normal distribution, often associated with heavier tails.
- **Platykurtic:** lower kurtosis than the normal distribution, often associated with lighter tails.

Kurtosis is frequently misunderstood as a measure of peak height alone. In statistical analysis, tail behaviour is an important part of its interpretation.

For Data Science, the practical lesson is to examine distribution plots and investigate extreme observations rather than relying only on a single shape statistic. Detailed distribution theory belongs in the Probability Distributions section.

## 13. Choosing the Right Descriptive Measure

Different datasets require different summaries.

| Situation | Useful Measure |
|---|---|
| General numerical data without strong outliers | Mean and standard deviation |
| Strongly skewed data | Median and IQR |
| Most common category | Mode |
| Quick measure of total spread | Range |
| Spread around the mean | Variance and standard deviation |
| Spread of the middle 50% | IQR |
| Relative position in a distribution | Percentile |
| Compact summary of centre and spread | Five-number summary |
| Relative variability between suitable datasets | Coefficient of variation |

No single measure is always best. The choice should reflect the data type, distribution, and purpose of the analysis.

## 14. Visualising Descriptive Statistics

Visualisation makes patterns easier to recognise and helps identify issues that a numerical summary might hide.

### 14.1 Histogram

A histogram displays the distribution of numerical data by grouping values into bins. It helps reveal concentration, spread, skewness, gaps, and possible multiple peaks.

### 14.2 Bar Chart

A bar chart compares values across categories, such as the number of customers in each region or the frequency of each product type.

### 14.3 Box Plot

A box plot summarises the median, quartiles, and potential outliers. It is especially useful for comparing numerical distributions across groups.

### 14.4 Choosing a Visualisation

| Data or Question | Suitable Visualisation |
|---|---|
| Distribution of a numerical feature | Histogram |
| Compare categorical counts | Bar chart |
| Compare spread across groups | Box plot |
| Change over time | Line graph |
| Relationship between two numerical variables | Scatter plot |

The scatter plot is useful during EDA, but the strength and direction of relationships between numerical variables are studied more directly in the Correlation folder.

## 15. Descriptive Statistics with Python

Python libraries make descriptive analysis easier to reproduce and apply to real datasets.

### 15.1 Using NumPy

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

The correct setting depends on whether you intend to describe the complete population or estimate variability from a sample.

### 15.2 Calculating Percentiles and IQR

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

NumPy's percentile results depend on the chosen percentile method. If you are comparing results with a textbook or another library, ensure that the same convention is being used.

### 15.3 Using pandas

pandas is especially useful when working with tabular datasets.

```python
import pandas as pd

df = pd.DataFrame({
    "Marks": [45, 55, 60, 70, 80, 90],
    "Study_Hours": [1, 2, 2, 3, 4, 5]
})

print(df.describe())
```

The `describe()` method provides descriptive summaries of numerical columns, including count, mean, standard deviation, minimum, quartiles, and maximum.

Individual statistics can also be calculated:

```python
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].std())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].quantile(0.75))
```

By default, pandas uses sample standard deviation for a Series, equivalent to `ddof=1`.

For categorical columns, `describe()` reports different information, such as the number of non-missing observations, unique values, most frequent value, and its frequency.

## 16. Descriptive Statistics in Exploratory Data Analysis (EDA)

Exploratory Data Analysis is the process of examining a dataset to understand its structure, quality, patterns, and unusual observations before building a model.

Descriptive statistics is an important part of EDA.

A practical initial workflow is:

1. Inspect the dataset's rows, columns, and data types.
2. Check the number of missing values.
3. Calculate descriptive statistics for numerical columns.
4. Examine categorical frequencies.
5. Plot numerical distributions.
6. Investigate potential outliers.
7. Decide whether further data cleaning or transformation is justified.

Example:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Inspect the dataset
print(df.head())
print(df.shape)
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Summarise numerical columns
print(df.describe())

# Visualise one numerical feature
df["feature_name"].hist()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Feature")
plt.show()
```

Replace `"data.csv"` and `"feature_name"` with the actual file name and column name.

Descriptive statistics can help identify unusual ranges, highly skewed variables, possible data-entry problems, and differences in scale. However, the statistics do not automatically determine how missing values or outliers should be treated. Those decisions require context and validation.

## 17. Standardisation and Normalisation: A Machine Learning Preview

Standardisation and normalisation are feature-scaling techniques used to change the scale of numerical features. They are related to descriptive analysis because they depend on understanding the range, mean, and standard deviation of the data.

### 17.1 Standardisation

Standardisation converts a value into a z-score by subtracting the mean and dividing by the standard deviation.

$$
z=\frac{x-\mu}{\sigma}
$$

When applied to a sample, the sample mean and sample standard deviation may be used according to the chosen convention.

A standardised value indicates how far an observation lies from the mean in standard-deviation units.

### 17.2 Min-Max Normalisation

Min-max scaling transforms values to a chosen range, commonly 0 to 1.

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

This formula requires \(x_{\max}\ne x_{\min}\).

### 17.3 Python Example

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

data = np.array([[10], [20], [30], [40], [50]])

standard_scaler = StandardScaler()
standardised = standard_scaler.fit_transform(data)

minmax_scaler = MinMaxScaler()
normalised = minmax_scaler.fit_transform(data)

print("Standardised values:")
print(standardised)

print("Normalised values:")
print(normalised)
```

Standardisation and min-max scaling are not the same operation. The appropriate technique depends on the feature, the algorithm, and the data distribution.

**Important for machine learning:** fit the scaler on the training data and then use that fitted scaler to transform validation or test data. Fitting it on the complete dataset before splitting can leak information from the test set into training. Detailed feature-scaling workflows can be developed further in the Machine Learning section of the repository.

## 18. Common Mistakes in Descriptive Statistics

### Mistake 1: Using the Mean Without Checking Outliers

The mean may be misleading when a dataset contains extreme values. Examine the median and distribution as well.

### Mistake 2: Confusing Variance and Standard Deviation

Variance is expressed in squared units. Standard deviation is expressed in the original units.

### Mistake 3: Using the Wrong Variance Formula

Population variance divides by \(N\). The usual sample variance estimator divides by \(n-1\).

### Mistake 4: Assuming Every Outlier Is an Error

Outliers can represent valid and important observations. Investigate their source before deciding how to handle them.

### Mistake 5: Confusing Percentile and Percentage

The 90th percentile describes relative position in a distribution. It does not mean a score of 90%.

### Mistake 6: Assuming the Mean Describes Every Dataset Well

For strongly skewed data, the median and IQR may provide a more useful summary.

### Mistake 7: Ignoring Missing Values

A statistic calculated after missing observations have been excluded may describe a different set of observations than expected. Always understand how missing values are handled.

### Mistake 8: Fitting a Scaler Before Splitting the Dataset

In predictive modelling, fitting a scaler on both training and test data can cause data leakage. Fit preprocessing steps using training data only.

## 19. Points to Remember

1. Descriptive statistics summarises observed data.
2. Mean, median, and mode measure central tendency.
3. Range, variance, standard deviation, and IQR measure dispersion.
4. The mean is sensitive to extreme observations.
5. The median is generally more resistant to outliers.
6. Sample variance commonly uses \(n-1\) in the denominator.
7. Standard deviation is the square root of variance.
8. Quartiles divide ordered data into four parts.
9. Percentiles describe relative position in a dataset.
10. The five-number summary contains the minimum, \(Q_1\), median, \(Q_3\), and maximum.
11. Box plots help compare distributions and flag potential outliers.
12. Skewness describes asymmetry; kurtosis describes aspects of distribution shape and tail behaviour.
13. pandas `describe()` is useful for initial numerical summaries.
14. NumPy's `ddof` determines the variance and standard-deviation denominator convention.
15. EDA should include numerical summaries, visualisation, and checks for data quality.
16. Outliers should be investigated rather than automatically deleted.
17. Standardisation and normalisation are different feature-scaling techniques.
18. Preprocessing must be fitted on training data only when evaluating a predictive model.

## 20. Important Formula Summary

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

**Coefficient of variation for a sample**

$$
CV=\frac{s}{\bar{x}}\times100\%
$$

**Z-score standardisation**

$$
z=\frac{x-\mu}{\sigma}
$$

**Min-max normalisation**

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

## 21. Chapter Summary

Descriptive statistics provides the foundation for understanding a dataset before applying more advanced statistical methods or machine learning algorithms.

Measures of central tendency describe the centre of the data, while measures of dispersion describe its variability. Quartiles, percentiles, and the five-number summary help explain relative position and spread. Skewness and kurtosis provide additional information about distribution shape.

In practical Data Science, these concepts are used alongside Python, NumPy, pandas, and visualisation libraries to perform initial data exploration. The results help identify unusual values, understand feature distributions, and guide further investigation.

Descriptive statistics does not replace data cleaning, inferential statistics, or model evaluation. Instead, it provides the understanding needed to use those methods appropriately.

## 22. References and Further Reading

The following resources provide additional explanations and examples.

### GeeksforGeeks

- [Descriptive Statistics](https://www.geeksforgeeks.org/maths/descriptive-statistics/)
- [Mean, Median and Mode](https://www.geeksforgeeks.org/maths/mean-median-mode/)

### OpenStax

- [Measures of the Spread of the Data](https://openstax.org/books/introductory-statistics-2e/pages/2-7-measures-of-the-spread-of-the-data)
- [Box Plots](https://openstax.org/books/introductory-statistics-2e/pages/2-4-box-plots)
- [Histograms, Frequency Polygons, and Time Series Graphs](https://openstax.org/books/introductory-statistics-2e/pages/2-2-histograms-frequency-polygons-and-time-series-graphs)
- [Skewness and the Mean, Median, and Mode](https://openstax.org/books/introductory-statistics-2e/pages/2-6-skewness-and-the-mean-median-and-mode)

### Python Libraries

- [NumPy — Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [pandas — Descriptive Statistics](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics)
- [Matplotlib — Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [scikit-learn — Preprocessing Data](https://scikit-learn.org/stable/modules/preprocessing.html)

### Related Topics in This Repository

- Probability
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- ANOVA
- Correlation
- Regression
- Regression Model Evaluation
- Statistics for Machine Learning
