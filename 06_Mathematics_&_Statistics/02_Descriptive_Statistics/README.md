# 02 — Descriptive Statistics

Descriptive statistics is the branch of statistics concerned with **organising, summarising, and presenting observed data** in a meaningful form.

Raw data can contain hundreds, thousands, or millions of observations. Looking at every individual value does not always make the overall pattern easy to understand. Descriptive statistics reduces a large collection of observations into useful summaries such as measures of central tendency, measures of dispersion, position measures, frequency distributions, and graphical representations.

This chapter develops these ideas step by step. The emphasis is on understanding what each measure means, how it is calculated, when it is useful, and how its value should be interpreted.

---

## 1. What Is Descriptive Statistics?

Descriptive statistics summarises the characteristics of a dataset without making a general conclusion about an unknown population beyond the data being described.

Suppose the daily sales of a shop for 30 days are available. Instead of listing all 30 values, we can calculate:

- Mean sales
- Median sales
- Minimum and maximum sales
- Range
- Variance
- Standard deviation
- Quartiles
- Percentiles
- Frequency distributions

We can also represent the data using:

- Tables
- Bar charts
- Histograms
- Pie charts
- Box plots
- Line graphs
- Scatter plots

A useful way to think about descriptive statistics is:

```
Raw Data
   ↓
Organise
   ↓
Summarise
   ↓
Calculate Statistics
   ↓
Visualise
   ↓
Interpret the Dataset
```

Descriptive statistics does not by itself establish why a pattern exists. Its purpose is to make the observed data easier to understand.

---

## 2. Types of Descriptive Measures

Descriptive measures can be grouped into several important categories.

### Measures of Central Tendency

These describe the centre or typical value of a dataset.

The main measures are:

- Mean
- Median
- Mode

### Measures of Dispersion

These describe how spread out the observations are.

The main measures are:

- Range
- Variance
- Standard deviation
- Interquartile range
- Coefficient of variation

### Measures of Position

These describe where an observation lies relative to the rest of the dataset.

Important examples are:

- Quartiles
- Percentiles
- Deciles

### Measures of Shape

These describe characteristics such as:

- Skewness
- Kurtosis

A complete descriptive analysis usually considers both the **centre** and the **spread**, rather than relying on a single statistic.

---

## 3. Organising Raw Data

Consider the following examination scores:

```
72, 45, 81, 63, 55, 90, 38, 76, 63, 50
```

The raw values are difficult to compare quickly.

We can first arrange them in ascending order:

```
38, 45, 50, 55, 63, 63, 72, 76, 81, 90
```

This simple step makes several properties easier to identify.

For example:

- Minimum = 38
- Maximum = 90
- Repeated value = 63
- Number of observations = 10

Organising data is often the first step before calculating descriptive statistics.

---

## 4. Frequency Distribution

A **frequency distribution** records how often each value or category occurs.

Consider:

```
10, 20, 20, 30, 20, 40, 30, 20
```

The frequency distribution is:

| Value | Frequency |
|---:|---:|
| 10 | 1 |
| 20 | 4 |
| 30 | 2 |
| 40 | 1 |

The total frequency is:

$$
1 + 4 + 2 + 1 = 8
$$

Therefore, there are 8 observations.

### Relative Frequency

Relative frequency expresses a frequency as a proportion of the total.

$$
R = \frac{f}{n}
$$

where:

- $f$ = frequency of a value or category
- $n$ = total number of observations

For the value 20:

$$
R = \frac{4}{8}
$$

$$
R = 0.5
$$

As a percentage:

$$
0.5 \times 100 = 50\%
$$

Therefore, 20 represents **50% of the observations**.

---

## 5. Grouped Frequency Distribution

When a dataset contains many different numerical values, listing every individual value may not be useful. We can group observations into intervals.

Suppose examination scores are:

```
0–10
11–20
21–30
31–40
41–50
```

A grouped frequency table might be:

| Score Interval | Frequency |
|---|---:|
| 0–10 | 2 |
| 11–20 | 5 |
| 21–30 | 9 |
| 31–40 | 12 |
| 41–50 | 7 |

The intervals are called **class intervals**.

### Class Width

A class width describes the size of an interval.

For continuous class boundaries, a common calculation is:

$$
\text{Class Width} = \frac{\text{Maximum Value} - \text{Minimum Value}}{\text{Number of Classes}}
$$

The exact convention can vary depending on how class boundaries are defined.

Grouped distributions are useful because they provide a compact summary of large numerical datasets.

---

## 6. Measures of Central Tendency

Measures of central tendency attempt to describe the central or typical value of a dataset.

The three basic measures are:

1. Mean
2. Median
3. Mode

No single measure is always best. The appropriate choice depends on the data and its distribution.

---

# 7. Arithmetic Mean

The **arithmetic mean** is commonly called the average.

For a sample:

$$
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}
$$

where:

- $\bar{x}$ = sample mean
- $x_i$ = the $i$th observation
- $n$ = number of observations
- $\sum$ = summation

### Worked Example

Consider:

```
10, 20, 30, 40, 50
```

Step 1: Add all observations.

$$
10 + 20 + 30 + 40 + 50 = 150
$$

Step 2: Count the observations.

$$
n = 5
$$

Step 3: Apply the formula.

$$
\bar{x} = \frac{150}{5}
$$

Therefore:

$$
\boxed{\bar{x}=30}
$$

The mean is **30**.

### Important Property

The arithmetic mean uses every observation. Therefore, an extremely large or extremely small value can strongly affect it.

Consider:

```
10, 20, 30, 40, 50
```

The mean is:

$$
\bar{x}=30
$$

Now add an extreme value of 500:

```
10, 20, 30, 40, 50, 500
```

The new mean becomes:

$$
\bar{x} = \frac{650}{6}
$$

$$
\boxed{\bar{x}\approx108.33}
$$

The mean moved from 30 to approximately 108.33 because of one extreme observation.

This is why the mean should be interpreted carefully when the dataset contains strong outliers.

---

# 8. Weighted Mean

A **weighted mean** is used when different observations contribute unequally to the final result.

The formula is:

$$
\bar{x}_w = \frac{\sum_{i=1}^{n}w_i x_i}{\sum_{i=1}^{n}w_i}
$$

where:

- $x_i$ = observation
- $w_i$ = weight assigned to the observation

### Worked Example

Suppose a student's final result is based on:

| Assessment | Score | Weight |
|---|---:|---:|
| Assignment | 80 | 2 |
| Midterm | 70 | 3 |
| Final Exam | 90 | 5 |

Calculate the weighted score.

First:

$$
80(2)=160
$$

$$
70(3)=210
$$

$$
90(5)=450
$$

Therefore:

$$
\sum w_i x_i = 160+210+450=820
$$

The total weight is:

$$
\sum w_i = 2+3+5=10
$$

Thus:

$$
\bar{x}_w=\frac{820}{10}
$$

$$
\boxed{\bar{x}_w=82}
$$

The weighted mean is **82**.

---

# 9. Median

The **median** is the middle value after the observations are arranged in ascending or descending order.

The median is particularly useful when the dataset contains extreme values because it is less affected by outliers than the mean.

### Case 1: Odd Number of Observations

Consider:

```
10, 20, 30, 40, 50
```

There are 5 observations.

The middle observation is:

$$
30
$$

Therefore:

$$
\boxed{\text{Median}=30}
$$

### Case 2: Even Number of Observations

Consider:

```
10, 20, 30, 40, 50, 60
```

There are 6 observations.

The two middle observations are:

$$
30 \quad \text{and} \quad 40
$$

The median is their average:

$$
\text{Median}=\frac{30+40}{2}
$$

$$
\boxed{\text{Median}=35}
$$

### Why Sorting Is Important

Consider:

```
50, 10, 40, 20, 30
```

The values must first be sorted:

```
10, 20, 30, 40, 50
```

The middle value is 30.

Therefore:

$$
\boxed{\text{Median}=30}
$$

---

# 10. Mode

The **mode** is the value or category that occurs most frequently.

Consider:

```
10, 20, 20, 30, 20, 40
```

The frequencies are:

| Value | Frequency |
|---:|---:|
| 10 | 1 |
| 20 | 3 |
| 30 | 1 |
| 40 | 1 |

The highest frequency is 3.

Therefore:

$$
\boxed{\text{Mode}=20}
$$

### Possible Cases

A dataset can be:

- **Unimodal** — one mode
- **Bimodal** — two modes
- **Multimodal** — more than two modes
- **Without a unique mode** — no value occurs more frequently than the others

For categorical data, the mode is often particularly useful because categories may not have meaningful numerical averages.

---

# 11. Mean, Median, and Mode Comparison

Consider a roughly symmetric dataset:

```
10, 20, 30, 40, 50
```

Here:

$$
\text{Mean}=30
$$

$$
\text{Median}=30
$$

There is no unique mode.

Now consider:

```
10, 20, 20, 20, 30, 100
```

The mean is:

$$
\bar{x}=\frac{200}{6}
$$

$$
\bar{x}\approx33.33
$$

The median is:

$$
\text{Median}=\frac{20+20}{2}=20
$$

The mode is:

$$
\boxed{\text{Mode}=20}
$$

The extreme value 100 pulls the mean upward, while the median remains near the centre of the majority of observations.

### General Interpretation

| Measure | Main Idea | Sensitivity to Outliers |
|---|---|---|
| Mean | Arithmetic average | High |
| Median | Middle ordered value | Low |
| Mode | Most frequent value | Generally low |

For a strongly skewed numerical dataset, the median may provide a more representative description of the centre than the mean.

---

# 12. Measures of Dispersion

Knowing the centre of a dataset is not enough.

Consider two datasets:

```
A: 48, 49, 50, 51, 52

B: 10, 30, 50, 70, 90
```

Both have mean 50.

However, the observations in dataset B are much more spread out.

Therefore, descriptive analysis should consider both:

- **Central tendency**
- **Dispersion**

Important measures of dispersion include:

- Range
- Variance
- Standard deviation
- Interquartile range
- Coefficient of variation

---

# 13. Range

The **range** is the difference between the largest and smallest values.

$$
R = x_{\max} - x_{\min}
$$

### Worked Example

Consider:

```
12, 15, 20, 27, 30
```

The maximum is:

$$
x_{\max}=30
$$

The minimum is:

$$
x_{\min}=12
$$

Therefore:

$$
R=30-12
$$

$$
\boxed{R=18}
$$

The range is 18.

### Limitation of Range

The range uses only two observations:

- Minimum
- Maximum

It ignores all values between them.

Therefore, two datasets can have the same range while having very different internal distributions.

---

# 14. Variance

Variance measures the average squared deviation of observations from their mean.

For a population:

$$
\sigma^2 = \frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

For a sample:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

where:

- $\sigma^2$ = population variance
- $s^2$ = sample variance
- $x_i$ = observation
- $\mu$ = population mean
- $\bar{x}$ = sample mean
- $N$ = population size
- $n$ = sample size

### Why Square the Deviations?

If we simply added deviations from the mean, positive and negative deviations would cancel.

For example:

```
-10, -5, 0, 5, 10
```

The sum is:

$$
-10-5+0+5+10=0
$$

Squaring makes every deviation non-negative:

```
100, 25, 0, 25, 100
```

This allows us to measure the magnitude of dispersion.

### Worked Sample Example

Consider:

```
2, 4, 6
```

Step 1: Calculate the sample mean.

$$
\bar{x}=\frac{2+4+6}{3}
$$

$$
\bar{x}=4
$$

Step 2: Calculate deviations.

| $x_i$ | $x_i-\bar{x}$ |
|---:|---:|
| 2 | -2 |
| 4 | 0 |
| 6 | 2 |

Step 3: Square the deviations.

| $x_i$ | $x_i-\bar{x}$ | $(x_i-\bar{x})^2$ |
|---:|---:|---:|
| 2 | -2 | 4 |
| 4 | 0 | 0 |
| 6 | 2 | 4 |

Step 4: Add squared deviations.

$$
4+0+4=8
$$

Step 5: Because these three observations are being treated as a sample, divide by $n-1$.

$$
s^2=\frac{8}{3-1}
$$

$$
s^2=\frac{8}{2}
$$

Therefore:

$$
\boxed{s^2=4}
$$

---

# 15. Standard Deviation

Standard deviation is the square root of variance.

For a population:

$$
\sigma = \sqrt{\sigma^2}
$$

For a sample:

$$
s = \sqrt{s^2}
$$

Using the previous example:

$$
s^2=4
$$

Therefore:

$$
s=\sqrt{4}
$$

$$
\boxed{s=2}
$$

Standard deviation is expressed in the **same units as the original variable**, unlike variance.

For example, if the observations represent kilograms:

- Variance is expressed in $\text{kg}^2$.
- Standard deviation is expressed in kg.

A larger standard deviation indicates greater spread around the mean, while a smaller standard deviation indicates that observations tend to be closer to the mean.

---

# 16. Population vs Sample Variance

A common source of confusion is the denominator.

### Population Variance

When the entire population is being described:

$$
\sigma^2 = \frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

### Sample Variance

When the observations represent a sample used to estimate population variability:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

The use of $n-1$ in the sample variance formula is known as **Bessel's correction**.

It provides an unbiased estimator of the population variance under the standard assumptions of random sampling and finite population variance.

---

# 17. Interquartile Range

The **interquartile range (IQR)** measures the spread of the middle 50% of the observations.

It is defined as:

$$
IQR = Q_3-Q_1
$$

where:

- $Q_1$ = first quartile
- $Q_3$ = third quartile

The IQR is less affected by extreme observations than the range.

### Example

Suppose:

$$
Q_1=20
$$

and:

$$
Q_3=50
$$

Then:

$$
IQR=50-20
$$

$$
\boxed{IQR=30}
$$

The middle 50% of the data spans 30 units.

---

# 18. Quartiles

Quartiles divide ordered data into four parts.

The main quartiles are:

- $Q_1$ — first quartile
- $Q_2$ — second quartile
- $Q_3$ — third quartile

### First Quartile

$Q_1$ is the value below which approximately 25% of the observations fall.

### Second Quartile

$Q_2$ is the median.

Approximately 50% of observations lie below it.

### Third Quartile

$Q_3$ is the value below which approximately 75% of observations fall.

A useful representation is:

```
Minimum      Q1          Q2          Q3       Maximum
   |----------|-----------|-----------|----------|
       25%         25%         25%         25%
```

Different software packages may use different interpolation conventions when calculating quartiles, especially for small datasets. Therefore, the exact numerical value can depend on the chosen method.

---

# 19. Percentiles

A **percentile** describes the position of an observation relative to the rest of the data.

The $p$th percentile is a value below which approximately $p\%$ of observations fall.

Examples:

- 25th percentile ≈ $Q_1$
- 50th percentile = median
- 75th percentile ≈ $Q_3$

Suppose a student is at the 90th percentile in an examination.

This means approximately 90% of the observations are at or below that student's position, depending on the percentile convention used.

A percentile does **not** mean that the student scored 90%.

For example:

- Score = 90 marks
- Percentile = 90th percentile

These are different concepts.

---

# 20. Deciles

Deciles divide ordered data into ten parts.

They are commonly represented as:

$$
D_1,D_2,\ldots,D_9
$$

where:

- $D_1$ corresponds approximately to the 10th percentile.
- $D_5$ corresponds approximately to the 50th percentile.
- $D_9$ corresponds approximately to the 90th percentile.

Like quartiles and percentiles, the exact calculation can depend on the selected statistical convention.

---

# 21. Five-Number Summary

The **five-number summary** consists of:

1. Minimum
2. First quartile ($Q_1$)
3. Median ($Q_2$)
4. Third quartile ($Q_3$)
5. Maximum

It provides a compact description of both centre and spread.

For example:

| Measure | Value |
|---|---:|
| Minimum | 10 |
| $Q_1$ | 20 |
| Median | 35 |
| $Q_3$ | 50 |
| Maximum | 80 |

These five values are particularly useful when constructing and interpreting a box plot.

---

# 22. Box Plot

A **box plot** represents the five-number summary visually.

A typical box plot contains:

- Lower whisker
- First quartile
- Median
- Third quartile
- Upper whisker

The box itself represents the interquartile range.

Conceptually:

```
Minimum       Q1          Median          Q3       Maximum
   |-----------[===========|===============]----------|
               <---- IQR ---->
```

Box plots are useful for comparing distributions across groups because they show:

- Centre
- Spread
- Possible outliers
- Differences between groups

### Outlier Rule Based on IQR

A common rule identifies possible outliers using:

$$
\text{Lower Fence}=Q_1-1.5(IQR)
$$

$$
\text{Upper Fence}=Q_3+1.5(IQR)
$$

Observations outside these fences are commonly flagged as possible outliers.

This rule is a convention for identifying potential outliers; it does not automatically mean that such observations are errors.

---

# 23. Outliers

An **outlier** is an observation that is unusually distant from the rest of the data.

Consider:

```
10, 12, 13, 14, 15, 100
```

The value 100 is much larger than the other observations.

Outliers may occur because of:

- Measurement error
- Data entry error
- Unusual but genuine behaviour
- Rare events
- Different populations or subgroups

An outlier should not automatically be deleted.

A better approach is to investigate why it exists.

### Effect on Descriptive Measures

Outliers can strongly affect:

- Mean
- Variance
- Standard deviation
- Range

They generally have less influence on:

- Median
- IQR

This difference is one reason robust measures are useful for skewed datasets.

---

# 24. Coefficient of Variation

The **coefficient of variation (CV)** measures relative variability.

It is commonly defined as:

$$
CV = \frac{s}{\bar{x}}\times100
$$

for a sample, where:

- $s$ = sample standard deviation
- $\bar{x}$ = sample mean

### Worked Example

Suppose:

$$
\bar{x}=50
$$

and:

$$
s=5
$$

Then:

$$
CV=\frac{5}{50}\times100
$$

$$
CV=10\%
$$

Therefore:

$$
\boxed{CV=10\%}
$$

The coefficient of variation is useful when comparing relative variability between datasets with different scales or means.

It should be used carefully when the mean is zero or very close to zero, because the ratio becomes unstable or undefined.

---

# 25. Skewness

**Skewness** describes the asymmetry of a distribution.

A perfectly symmetric distribution has approximately equal left and right sides around its centre.

### Positive Skewness

A positively skewed distribution has a longer tail toward larger values.

```
Frequency
   ^
   |       ███
   |     █████
   |   ███████
   | ███████
   +-------------------->
              Long right tail
```

For many positively skewed distributions:

$$
\text{Mean} > \text{Median}
$$

### Negative Skewness

A negatively skewed distribution has a longer tail toward smaller values.

For many negatively skewed distributions:

$$
\text{Mean} < \text{Median}
$$

### Important Note

The relationship between mean and median is a useful descriptive clue, but it should not be treated as a universal mathematical rule for every distribution.

---

# 26. Kurtosis

**Kurtosis** describes aspects of the shape of a distribution, particularly the behaviour of its tails relative to a reference distribution.

Three common descriptive terms are:

- Mesokurtic
- Leptokurtic
- Platykurtic

In statistical software, kurtosis may be reported using different conventions, including **excess kurtosis**.

Because conventions differ, the definition and reference value should always be checked before interpreting a numerical kurtosis value.

The important practical idea is that kurtosis is related to the distribution's tail behaviour and the occurrence of extreme observations.

---

# 27. Measures of Shape

Descriptive analysis can therefore examine three broad characteristics:

### Centre

Where the observations are concentrated.

Examples:

- Mean
- Median
- Mode

### Spread

How far observations vary around the centre.

Examples:

- Range
- Variance
- Standard deviation
- IQR

### Shape

How the distribution is arranged.

Examples:

- Skewness
- Kurtosis

A good descriptive summary considers these characteristics together.

---

# 28. Data Visualisation

Numerical summaries are important, but visualisations often reveal patterns that are difficult to see from a table of values.

The appropriate graph depends on the type of variable and the question being asked.

### Bar Chart

A bar chart is commonly used for categorical data.

Example:

```
Department    Students

CSE           █████████████
ECE           ████████
ME            █████
```

The bars represent categories and their frequencies.

### Histogram

A histogram is used to represent the distribution of numerical data using intervals.

Unlike a standard bar chart, the horizontal axis represents numerical intervals.

### Box Plot

A box plot summarises the distribution using quartiles, median, and possible outliers.

### Scatter Plot

A scatter plot represents the relationship between two numerical variables.

For example:

- Study hours
- Examination score

Each point represents one observation.

### Line Graph

A line graph is commonly used when observations are ordered over time.

For example:

```
Month → Sales
Jan   → 100
Feb   → 120
Mar   → 135
Apr   → 150
```

The graph helps show the direction and pattern of change.

---

# 29. Histogram vs Bar Chart

These two graphs are often confused.

| Feature | Histogram | Bar Chart |
|---|---|---|
| Typical data | Numerical | Categorical |
| Horizontal axis | Numerical intervals | Categories |
| Bars | Usually touch | Usually separated |
| Purpose | Show distribution | Compare categories |

For example:

- Age distribution → Histogram
- Number of students by branch → Bar chart

Choosing the wrong graph can make the data difficult to interpret.

---

# 30. Central Tendency and Distribution Shape

The relationship between mean and median can provide useful information about distribution shape.

### Approximately Symmetric Distribution

The mean and median may be close:

$$
\text{Mean} \approx \text{Median}
$$

### Positively Skewed Distribution

The mean is often pulled toward the longer right tail:

$$
\text{Mean} > \text{Median}
$$

### Negatively Skewed Distribution

The mean is often pulled toward the longer left tail:

$$
\text{Mean} < \text{Median}
$$

These are useful descriptive patterns, not universal laws.

---

# 31. Worked Example — Complete Descriptive Summary

Consider the dataset:

```
4, 5, 6, 6, 7, 8, 10, 12, 15, 20
```

There are:

$$
n=10
$$

observations.

### Step 1: Mean

First calculate the sum:

$$
4+5+6+6+7+8+10+12+15+20=93
$$

Therefore:

$$
\bar{x}=\frac{93}{10}
$$

$$
\boxed{\bar{x}=9.3}
$$

### Step 2: Median

There are 10 observations, so take the average of the 5th and 6th values.

The 5th value is 7.

The 6th value is 8.

Therefore:

$$
\text{Median}=\frac{7+8}{2}
$$

$$
\boxed{\text{Median}=7.5}
$$

### Step 3: Mode

The value 6 occurs twice.

All other values occur once.

Therefore:

$$
\boxed{\text{Mode}=6}
$$

### Step 4: Range

Maximum:

$$
x_{\max}=20
$$

Minimum:

$$
x_{\min}=4
$$

Therefore:

$$
R=20-4
$$

$$
\boxed{R=16}
$$

### Step 5: Interpretation

The mean is 9.3, while the median is 7.5.

The mean is larger because the higher values, particularly 15 and 20, pull the arithmetic average upward.

This suggests that the distribution has some right-side skewness.

A complete analysis would continue with quartiles, IQR, standard deviation, and a visualisation before drawing a stronger conclusion about the distribution.

---

# 32. Comparing Two Datasets

Consider:

```
Dataset A:
48, 49, 50, 51, 52

Dataset B:
10, 30, 50, 70, 90
```

### Mean of Dataset A

$$
\bar{x}_A=\frac{48+49+50+51+52}{5}
$$

$$
\boxed{\bar{x}_A=50}
$$

### Mean of Dataset B

$$
\bar{x}_B=\frac{10+30+50+70+90}{5}
$$

$$
\boxed{\bar{x}_B=50}
$$

The means are identical.

However, Dataset B is much more spread out.

Therefore:

> **A measure of centre alone is not enough to describe a dataset.**

We also need a measure of dispersion such as standard deviation or IQR.

This is one of the most important ideas in descriptive statistics.

---

# 33. Choosing the Appropriate Measure

The choice of descriptive statistic depends on the data.

### For Nominal Data

Useful measure:

- Mode
- Frequency
- Proportion

### For Ordinal Data

Useful measures may include:

- Median
- Mode
- Percentiles
- Frequencies

### For Numerical Data

Useful measures may include:

- Mean
- Median
- Range
- Variance
- Standard deviation
- Quartiles
- IQR

For strongly skewed numerical data, the **median and IQR** can provide a more robust summary than the mean and standard deviation.

---

# 34. Common Mistakes

### Mistake 1: Calculating the Mean Without Inspecting the Data

The mean can be strongly affected by outliers.

### Mistake 2: Confusing Median and Mean

The mean is an arithmetic average, while the median is the middle ordered value.

### Mistake 3: Forgetting to Sort Before Finding the Median

The median depends on the ordered position of observations.

### Mistake 4: Treating Variance and Standard Deviation as the Same

Standard deviation is the square root of variance.

### Mistake 5: Ignoring Units

Variance has squared units, while standard deviation has the original units.

### Mistake 6: Removing Outliers Automatically

An outlier may be a genuine observation.

### Mistake 7: Confusing Percentile With Percentage

A 90th percentile position is not the same thing as scoring 90%.

### Mistake 8: Using a Bar Chart for a Numerical Distribution

A histogram is generally more appropriate for continuous numerical distributions.

### Mistake 9: Reporting Only the Mean

A mean without information about spread can hide important differences between datasets.

---

# 35. Points to Remember

1. Descriptive statistics summarises observed data.
2. The mean is the arithmetic average.
3. The median is the middle ordered value.
4. The mode is the most frequently occurring value or category.
5. The mean is sensitive to extreme observations.
6. The median is generally more resistant to outliers.
7. Range is the difference between maximum and minimum.
8. Variance measures squared deviation from the mean.
9. Standard deviation is the square root of variance.
10. Sample variance uses $n-1$ in the denominator.
11. IQR measures the spread of the middle 50% of observations.
12. Quartiles divide ordered data into four parts.
13. Percentiles describe relative position in a dataset.
14. The five-number summary contains minimum, $Q_1$, median, $Q_3$, and maximum.
15. A box plot is based on the five-number summary.
16. Outliers should be investigated rather than automatically removed.
17. Skewness describes asymmetry.
18. Kurtosis describes aspects of tail behaviour and distribution shape.
19. A measure of central tendency should usually be considered together with a measure of dispersion.
20. The correct visualisation depends on the type and structure of the data.

---

# 36. Important Formula Summary

### Arithmetic Mean

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

### Weighted Mean

$$
\bar{x}_w=\frac{\sum_{i=1}^{n}w_i x_i}{\sum_{i=1}^{n}w_i}
$$

### Range

$$
R=x_{\max}-x_{\min}
$$

### Population Variance

$$
\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

### Sample Variance

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

### Population Standard Deviation

$$
\sigma=\sqrt{\sigma^2}
$$

### Sample Standard Deviation

$$
s=\sqrt{s^2}
$$

### Interquartile Range

$$
IQR=Q_3-Q_1
$$

### Lower IQR Fence

$$
Q_1-1.5(IQR)
$$

### Upper IQR Fence

$$
Q_3+1.5(IQR)
$$

### Coefficient of Variation

$$
CV=\frac{s}{\bar{x}}\times100
$$

### Relative Frequency

$$
R=\frac{f}{n}
$$

### Percentage

$$
P=\frac{f}{n}\times100
$$

---

# 37. Quick Concept Comparison

| Concept | What It Describes |
|---|---|
| Mean | Arithmetic centre |
| Median | Middle ordered value |
| Mode | Most frequent value |
| Range | Total distance between minimum and maximum |
| Variance | Average squared dispersion |
| Standard Deviation | Typical spread measured in original units |
| Quartiles | Positions dividing ordered data into four parts |
| IQR | Spread of middle 50% |
| Percentile | Relative position |
| Skewness | Asymmetry |
| Kurtosis | Tail and shape characteristics |
| Frequency | Number of occurrences |
| Relative Frequency | Proportion of occurrences |
| Five-Number Summary | Compact distribution summary |
| Box Plot | Visual summary of centre, spread, and possible outliers |

---

# 38. Chapter Summary

Descriptive statistics provides the tools needed to turn raw observations into an understandable summary.

The first question is often **where the centre of the data lies**, which leads to the mean, median, and mode. The next question is **how much the observations vary**, which leads to range, variance, standard deviation, and IQR. We can then study **where observations lie relative to one another** using quartiles and percentiles and examine the **shape of the distribution** using skewness and kurtosis.

Visualisation complements numerical summaries. Histograms show numerical distributions, bar charts compare categories, box plots summarise distributions using quartiles, and scatter plots display pairs of numerical observations.

The most important principle is that **no single descriptive statistic completely describes a dataset**. A meaningful summary usually combines measures of centre, spread, position, and shape with an appropriate visual representation.

---

# 39. References

1. Standard introductory statistics material covering descriptive statistics, measures of central tendency, dispersion, position, and distribution shape.
2. Open educational resources for statistics and data analysis.
3. Course notes and classroom material used for the Mathematics & Statistics section of this repository.
