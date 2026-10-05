# Descriptive Statistics

Descriptive Statistics is the branch of statistics used to **collect, organize, summarize, and present data** in a meaningful way.

It helps us understand the important characteristics of a dataset without making conclusions about a larger population.

---

## 1. Introduction to Descriptive Statistics

### What is Descriptive Statistics?

Descriptive Statistics provides a compact summary of data using:

- Numerical measures
- Tables
- Frequency distributions
- Graphs and charts

For example, suppose the marks of five students are: **45, 60, 72, 72, 91**

Instead of looking at all five values repeatedly, we can summarize them using:

- Mean
- Median
- Mode
- Range
- Variance
- Standard deviation
- Quartiles

The purpose is to make the dataset easier to understand.

### Descriptive Statistics vs Inferential Statistics

| Descriptive Statistics | Inferential Statistics |
|---|---|
| Summarizes observed data | Makes conclusions about a population |
| Uses tables, graphs and summary measures | Uses estimation, confidence intervals and hypothesis tests |
| Describes what the data looks like | Uses sample data to learn about a wider population |
| Example: average marks of a class | Example: estimating the average marks of all students in a university |

---

## 2. Main Parts of Descriptive Statistics

Descriptive Statistics can be broadly organized into:

1. Measures of Central Tendency
2. Measures of Dispersion
3. Measures of Position
4. Measures of Shape
5. Frequency Distributions
6. Data Visualization

### Overview diagram

![Descriptive Statistics overview](https://media.geeksforgeeks.org/wp-content/uploads/20250508115106881109/descriptive_statistics.webp)

**Image source:** GeeksforGeeks — Descriptive Statistics

[Open the original GeeksforGeeks article](https://www.geeksforgeeks.org/maths/descriptive-statistics/)

# 3. Measures of Central Tendency

A measure of central tendency attempts to represent the **center or typical value** of a dataset.

The three basic measures are:

- Mean
- Median
- Mode

---

## 3.1 Mean

The **mean** is the arithmetic average of a dataset.

### Formula

For a dataset: **x₁, x₂, x₃, ..., xₙ**

the arithmetic mean is:

**Formula:** **x̄ = Σx / n**

where:

- `x̄` = mean
- `Σx` = sum of all observations
- `n` = number of observations

### Example

For example, consider the dataset **10, 20, 30, 40, 50**.

The sum is **150**.

Number of observations:

There are **5 observations**.

Therefore, **Mean = 150 / 5 = 30**.

### Important property

The mean uses **every observation** in the dataset.

This makes it useful, but it also means the mean can be strongly affected by extreme values.

Example:

10, 20, 30, 40, 1000

The value `1000` pulls the mean upward.

### Python

```python
data = [10, 20, 30, 40, 50]

mean = sum(data) / len(data)

print(mean)
```

Output:

30.0

---

## 3.2 Weighted Mean

Sometimes every observation does not have equal importance.

A weighted mean assigns a weight to each value.

### Formula

**Weighted Mean = Σ(wx) / Σw**

where:

- `x` = observation
- `w` = weight

### Example

Suppose a student's marks are:

| Subject | Marks | Weight |
|---|---:|---:|
| Mathematics | 80 | 4 |
| Statistics | 70 | 3 |
| Python | 90 | 2 |

Weighted Mean
= (80×4 + 70×3 + 90×2) / (4+3+2)
= (320 + 210 + 180) / 9
= 710 / 9
= 78.89

Weighted mean is useful when different observations contribute differently.

---

## 3.3 Median

The **median** is the middle value after the data is arranged in ascending or descending order.

### Odd number of observations

Example: **5, 8, 12, 15, 20**

There are five values.

The middle value is: **12**

So:

**Median = 12**

### Even number of observations

Example: **5, 8, 12, 15, 20, 25**

The two middle values are: **12** and **15**

Therefore:

**Median = (12 + 15) / 2 = 13.5**

### Why median is useful

Median is less affected by extreme values than the mean.

Example:

For example, consider **20, 22, 25, 27, 1000**.

The mean becomes very large because of `1000`, while the median remains:

The median remains **25**.

This makes the median useful for data such as:

- House prices
- Salaries
- Income
- Property values

where extreme observations may occur.

---

## 3.4 Mode

The **mode** is the value that occurs most frequently.

Example:

For example, **2, 3, 3, 4, 5, 3, 6** has 3 as its most frequent value.

`3` occurs three times.

Therefore:

Therefore, **Mode = 3**.

### Types of mode

**Unimodal**

One mode:

Example: **1, 2, 2, 3, 4** has one mode, 2.

**Mode = `2`**

**Bimodal**

Two modes:

Example: **1, 2, 2, 3, 3, 4** has two modes, 2 and 3.

Modes = `2, 3`

**Multimodal**

More than two modes.

### No mode

If every value occurs only once, there is no mode.

---

# 4. Comparing Mean, Median and Mode

Consider: **10, 20, 20, 30, 40**

Mean: **(10 + 20 + 20 + 30 + 40) / 5 = 24**

Median: **20**

Mode: **20**

Therefore:

The results are:

- Mean = 24
- Median = 20
- Mode = 20

Each measure describes the center from a different perspective.

---

# 5. Measures of Dispersion

Central tendency tells us where the center is.

But two datasets can have the same mean while having very different amounts of spread.

Example:

For example:

- Dataset A: **48, 49, 50, 51, 52**
- Dataset B: **10, 30, 50, 70, 90**

Both have mean:

Both have a mean of **50**.

But Dataset B is much more spread out.

Measures of dispersion help us describe this spread.

Important measures include:

- Range
- Variance
- Standard deviation
- Mean absolute deviation
- Quartile deviation
- Interquartile range

---

# 6. Range

Range is the difference between the maximum and minimum values.

### Formula

**Formula:** **Range = Maximum − Minimum**

Example:

For example, consider **10, 15, 20, 25, 40**.

Therefore, **Range = 40 − 10 = 30**.

### Advantage

Very easy to calculate.

### Limitation

Range depends only on the minimum and maximum values.

---

# 7. Variance

Variance measures how far observations tend to spread from the mean using **squared deviations**.

For a population:

**Population variance:** **σ² = Σ(x − μ)² / N**

For a sample:

**Sample variance:** **s² = Σ(x − x̄)² / (n − 1)**

The distinction between population and sample variance will become important when studying inferential statistics.

### Step-by-step idea

Consider **2, 4, 6**.

Mean: **4**

The deviations from the mean are **−2, 0, and 2**.

The squared deviations are **4, 0, and 4**.


**Population variance = **(4 + 0 + 4) / 3 = 8 / 3 ≈ 2.67**.**

Variance is expressed in **squared units**.

---

# 8. Standard Deviation

Standard deviation is the square root of variance.

### Population standard deviation

**Population standard deviation:** **σ = √σ²**

### Sample standard deviation

**Sample standard deviation:** **s = √s²**

For the population example above:

If variance is approximately **2.67**, the standard deviation is **√2.67 ≈ 1.63**.

### Interpretation

A small standard deviation generally means observations are relatively close to the mean.

A large standard deviation generally means observations are more spread out.

Standard deviation is widely used in:

- Data Science
- Machine Learning
- Finance
- Quality control
- Scientific research

---

# 9. Mean Absolute Deviation

Mean Absolute Deviation (MAD) measures the average absolute distance of observations from a chosen central value.

For deviations from the mean:

**Formula:** **MAD = Σ|x − x̄| / n**

Example:

Consider **3, 5, 7, 9, 11**.

Mean:

The mean is **7**.

Absolute deviations:

The absolute deviations are **4, 2, 0, 2, 4**.

MAD:

**MAD = **(4 + 2 + 0 + 2 + 4) / 5 = 2.4**.**

---

# 10. Quartiles

Quartiles divide ordered data into four parts.

The main quartiles are:

- Q1 — first quartile
- Q2 — second quartile
- Q3 — third quartile

### Q1

Approximately 25% of observations lie below Q1.

### Q2

Q2 is the median.

Approximately 50% of observations lie below Q2.

### Q3

Approximately 75% of observations lie below Q3.

---

# 11. Interquartile Range (IQR)

The Interquartile Range describes the spread of the **middle 50%** of the data.

### Formula

**Formula:** **IQR = Q3 − Q1**

Example:

Suppose **Q1 = 20** and **Q3 = 50**.

Therefore:

Therefore, **IQR = 50 − 20 = 30**.

IQR is useful because it is less affected by extreme values than the range.

---

# 12. Quartile Deviation

Quartile deviation is also called the semi-interquartile range.

### Formula

**Formula:** **Quartile Deviation = (Q3 − Q1) / 2**

It represents half of the IQR.

---

# 13. Percentiles

Percentiles divide ordered data into 100 parts.

For example:

- 25th percentile ≈ Q1
- 50th percentile = median / Q2
- 75th percentile ≈ Q3

If a student's score is at the 90th percentile, the score is higher than approximately 90% of the observations in the reference dataset.

Percentiles are widely used for:

- Exam results
- Entrance tests
- Ranking
- Height and weight charts
- Performance analysis

---

# 14. Five-Number Summary

The five-number summary contains:

1. Minimum
2. Q1
3. Median
4. Q3
5. Maximum

Example:

For example, a five-number summary may be:

- Minimum = 10
- Q1 = 20
- Median = 30
- Q3 = 40
- Maximum = 60

These five values provide a compact description of the distribution.

The five-number summary is especially important for **box plots**.

---

# 15. Frequency Distribution

A frequency distribution shows how often values occur.

Example:

| Marks | Frequency |
|---:|---:|
| 50 | 2 |
| 60 | 3 |
| 70 | 5 |
| 80 | 4 |

Frequency tells us the number of observations belonging to a value or category.

### Relative frequency

**Formula:** **Relative Frequency = Frequency / Total Frequency**

It can also be expressed as a percentage.

### Cumulative frequency

Cumulative frequency is the running total of frequencies.

---

# 16. Graphical Descriptive Statistics

Graphs can reveal patterns that are difficult to see in raw numbers.

Important graphs include:

- Bar chart
- Histogram
- Pie chart
- Box plot
- Dot plot
- Stem-and-leaf plot
- Frequency polygon

---

## 16.1 Bar Chart

A bar chart is commonly used for categorical data.

Example:

**Product A → 20
Product B → 35
Product C → 25**

The categories are represented by separate bars.

---

## 16.2 Histogram

A histogram is used to visualize the distribution of numerical data.

Unlike a typical categorical bar chart, histogram bars represent **continuous or numerical intervals** and normally touch each other.

Example intervals:

For example, histogram intervals can be **0–10, 10–20, 20–30, and 30–40**.

Histograms help identify:

- Center
- Spread
- Shape
- Peaks
- Gaps
- Possible outliers

---

## 16.3 Box Plot

A box plot summarizes data using the five-number summary.

It shows:

- Minimum / lower whisker
- Q1
- Median
- Q3
- Maximum / upper whisker

It can also help identify potential outliers using rules such as the 1.5 × IQR rule.

---

## 16.4 Pie Chart

A pie chart displays parts of a whole.

For example:

**Python = 40%
Java = 30%
C++ = 20%
Other = 10%**

All categories together represent 100%.

Pie charts are most useful when there are only a small number of meaningful categories.

---

# 17. Distribution Shape

Descriptive statistics also helps us understand the shape of a distribution.

Important concepts:

- Symmetry
- Skewness
- Kurtosis

---

## 17.1 Symmetric Distribution

A distribution is approximately symmetric when its left and right sides have similar shapes.

In a perfectly symmetric unimodal distribution:

For a perfectly symmetric unimodal distribution, **Mean ≈ Median ≈ Mode**.

---

## 17.2 Right-Skewed Distribution

A right-skewed distribution has a longer tail toward larger values.

Often:

A common pattern in right-skewed data is **Mean > Median**.

Income and house-price datasets can sometimes show right-skewed behavior.

---

## 17.3 Left-Skewed Distribution

A left-skewed distribution has a longer tail toward smaller values.

Often:

A common pattern in left-skewed data is **Mean < Median**.

The relationship depends on the actual distribution, so mean and median should not be used as the only evidence of skewness.

---

# 18. Kurtosis

Kurtosis describes aspects of the shape and tail behavior of a distribution.

Common terms include:

- Mesokurtic
- Leptokurtic
- Platykurtic

In practical data analysis, kurtosis should be interpreted carefully and in context rather than simply treating it as a universal "peakness" score.

Detailed distribution theory will be covered further in later Statistics folders.

---

# 19. Choosing the Right Measure

Different datasets require different summaries.

| Situation | Useful measure |
|---|---|
| General numerical data | Mean + standard deviation |
| Data with strong outliers | Median + IQR |
| Most common category/value | Mode |
| Quick overall spread | Range |
| Spread around the mean | Standard deviation |
| Middle 50% spread | IQR |
| Position within a distribution | Percentile |
| Five-number summary | Box plot |

There is no single measure that is always best.

---

# 20. Effect of Outliers

An outlier is an observation that is unusually far from the rest of the data.

Consider: **20, 21, 22, 23, 24**.

Mean: **22**

Now add an extreme observation: **20, 21, 22, 23, 24, 100**.

The mean changes substantially.

The median changes much less.

This illustrates why: **Mean + Standard Deviation** and **Median + IQR** can lead to different interpretations.

---

# 21. Manual Calculation vs Python

Learning the manual calculation is important because it explains what Python libraries are doing internally.

For example:

```python
import statistics

data = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
```

Output:

Mean: 30
Median: 30
Mode: 10

The mode example above is intentionally included to demonstrate an important point: when all values occur once, Python's `statistics.mode()` returns the first mode according to its API behavior. In such cases, you should understand the dataset and library behavior rather than blindly interpreting the result as a uniquely occurring mode.

For broader analysis, libraries such as NumPy, pandas, and SciPy provide additional statistical functionality.

---

# 22. A Complete Worked Example

Consider the dataset:

**12, 15, 15, 18, 20, 22, 25, 25, 25, 30**

### Number of observations

**n = 10**

### Mean

**Mean = (12 + 15 + 15 + 18 + 20 + 22 + 25 + 25 + 25 + 30) / 10**  
&nbsp;&nbsp;&nbsp;&nbsp;**= 207 / 10**  
&nbsp;&nbsp;&nbsp;&nbsp;**= 20.7**

### Median

There are **10 observations**.

The middle positions are **5 and 6**:

**20 and 22**

**Median = (20 + 22) / 2 = 21**

### Mode

The value **`25`** occurs three times.

**Mode = 25**

### Range

**Range = 30 − 12 = 18**

This small example demonstrates how multiple descriptive measures provide different views of the same dataset.

---

# 23. Python Libraries for Descriptive Statistics

### Python `statistics`

Useful for basic statistical calculations.

```python
import statistics
```

### NumPy

Useful for numerical computing and array-based statistics.

```python
import numpy as np
```

### pandas

Useful for working with structured datasets.

```python
import pandas as pd
```

Example:

```python
import pandas as pd

data = pd.Series([10, 20, 20, 30, 40])

print(data.mean())
print(data.median())
print(data.mode())
print(data.std())
print(data.var())
```

---

# 24. Descriptive Statistics in Data Science

Descriptive statistics is one of the first steps in data analysis.

A typical workflow can be:

**Workflow:**

Raw Dataset → Understand Variables → Clean Data → Descriptive Statistics → Visualize Data → Identify Patterns → Further Statistical / ML Analysis

Before building a Machine Learning model, we often need to understand:

- Typical values
- Data spread
- Missing values
- Extreme values
- Distribution shape
- Relationships between variables

This is why descriptive statistics is an important foundation for Data Science and Machine Learning.

---

# 25. Points to Remember

- Descriptive statistics summarizes and presents observed data.
- Mean is the arithmetic average.
- Median is the middle value after sorting.
- Mode is the most frequently occurring value.
- Mean can be sensitive to extreme values.
- Median is generally more resistant to extreme values.
- Range = maximum − minimum.
- Variance measures squared spread around the mean.
- Standard deviation is the square root of variance.
- **IQR = Q3 − Q1**.
- Q2 is the median.
- Percentiles describe relative position in ordered data.
- The five-number summary consists of minimum, Q1, median, Q3, and maximum.
- Frequency tells how often observations occur.
- Histograms are useful for numerical distributions.
- Bar charts are commonly used for categorical comparisons.
- Box plots summarize distribution using quartiles and help inspect possible outliers.
- Mean and standard deviation are often useful for roughly symmetric numerical data.
- Median and IQR are often useful when distributions are skewed or contain strong outliers.
- Always understand whether you are describing a population or a sample before choosing the appropriate variance or standard deviation formula.

---

# 26. References / Further Reading

The explanations in this folder are written in our own words. The following sources are useful for deeper study and cross-checking concepts.

### GeeksforGeeks

- [Descriptive Statistics](https://www.geeksforgeeks.org/maths/descriptive-statistics/)
- [Mean, Median and Mode](https://www.geeksforgeeks.org/maths/mean-median-mode/)
- [Descriptive Statistics Practice Questions](https://www.geeksforgeeks.org/maths/descriptive-statistics-practice-questions/)

### Khan Academy

- [Summarizing Quantitative Data](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)
- [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)

### NIST / SEMATECH

- [e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)

### Further topics

The following topics will be developed further in the upcoming Statistics folders:

- Probability
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- ANOVA
- Correlation
- Regression
