# 02 Descriptive Statistics

Descriptive Statistics is the branch of statistics used to **organize, summarize, and present observed data**.

After learning the vocabulary of statistics in `01 Statistics Fundamentals`, we can now work with actual numerical data.

Suppose the marks of five students are:

$$
45,\ 60,\ 72,\ 72,\ 91
$$

Looking at the individual observations tells us something, but descriptive statistics allows us to summarize the dataset using measures such as the mean, median, mode, range, variance, standard deviation, quartiles, and percentiles.

![Descriptive Statistics](https://media.geeksforgeeks.org/wp-content/uploads/20250508115106881109/descriptive_statistics.webp)

*Source: GeeksforGeeks — Descriptive Statistics.*

## 1. Descriptive vs Inferential Statistics

| Descriptive Statistics | Inferential Statistics |
|---|---|
| Describes observed data | Uses sample data to learn about a population |
| Uses tables, graphs, and summary measures | Uses estimation and statistical tests |
| Answers "What does this data look like?" | Answers "What can we conclude beyond this sample?" |

This folder focuses on **describing the data we have**.

## 2. Measures of Central Tendency

Central tendency describes a typical or central value in a dataset.

The three basic measures are:

- Mean
- Median
- Mode

## 3. Mean

The mean is the arithmetic average.

For observations $x_1,x_2,\ldots,x_n$:

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

Here:

- $\bar{x}$ = sample mean
- $x_i$ = the $i$th observation
- $n$ = number of observations
- $\sum$ = sum of the observations

### Worked Example

Consider:

$$
10,\ 20,\ 30,\ 40,\ 50
$$

First add the observations:

$$
10+20+30+40+50=150
$$

There are:

$$
n=5
$$

Now substitute into the formula:

$$
\bar{x}=\frac{150}{5}
$$

Therefore:

$$
\boxed{\bar{x}=30}
$$

The mean is 30.

The mean uses every observation, which makes it useful but also makes it sensitive to extreme values.

### Effect of an Outlier

Consider:

$$
10,\ 20,\ 30,\ 40,\ 1000
$$

The sum is:

$$
10+20+30+40+1000=1100
$$

Therefore:

$$
\bar{x}=\frac{1100}{5}=220
$$

The value 1000 has pulled the mean far away from most of the observations.

## 4. Weighted Mean

Sometimes observations do not have equal importance.

The weighted mean is:

$$
\bar{x}_w=
\frac{\sum w_ix_i}{\sum w_i}
$$

where:

- $x_i$ = value
- $w_i$ = weight assigned to that value

### Worked Example

Suppose marks are:

| Subject | Marks | Weight |
|---|---:|---:|
| Mathematics | 80 | 3 |
| Statistics | 70 | 2 |
| Python | 90 | 1 |

Calculate the weighted mean.

First calculate each value multiplied by its weight:

$$
80\times3=240
$$

$$
70\times2=140
$$

$$
90\times1=90
$$

Add them:

$$
240+140+90=470
$$

Add the weights:

$$
3+2+1=6
$$

Now:

$$
\bar{x}_w=\frac{470}{6}
$$

$$
\bar{x}_w\approx78.33
$$

Therefore:

$$
\boxed{\bar{x}_w\approx78.33}
$$

## 5. Median

The median is the middle value after arranging the data in ascending or descending order.

### Odd Number of Observations

For an odd number of observations, the middle observation is the median.

Consider:

$$
10,\ 20,\ 30,\ 40,\ 50
$$

The middle value is:

$$
\boxed{30}
$$

### Even Number of Observations

When there are an even number of observations, the median is the average of the two middle values.

Consider:

$$
10,\ 20,\ 30,\ 40
$$

The two middle values are 20 and 30.

Therefore:

$$
Median=\frac{20+30}{2}
$$

$$
=\frac{50}{2}
$$

$$
\boxed{25}
$$

The median is generally less affected by extreme values than the mean.

## 6. Mode

The mode is the value that occurs most frequently.

Consider:

$$
10,\ 20,\ 20,\ 30,\ 40
$$

The value 20 occurs twice.

Therefore:

$$
\boxed{Mode=20}
$$

A dataset can have:

- one mode
- two modes
- multiple modes
- no mode

Mode is especially useful for categorical data.

## 7. Range

Range is the difference between the maximum and minimum values.

$$
Range=Maximum-Minimum
$$

Consider:

$$
10,\ 20,\ 30,\ 40,\ 50
$$

Maximum:

$$
50
$$

Minimum:

$$
10
$$

Therefore:

$$
Range=50-10
$$

$$
\boxed{Range=40}
$$

Range is simple, but it uses only two observations and can be strongly affected by extreme values.

## 8. Quartiles

Quartiles divide ordered data into four parts.

The important quartiles are:

- $Q_1$ = first quartile, approximately the 25th percentile
- $Q_2$ = second quartile, the median
- $Q_3$ = third quartile, approximately the 75th percentile

For a dataset, quartiles help us understand where observations lie within the distribution.

## 9. Interquartile Range

The interquartile range measures the spread of the middle 50% of the data.

The formula is:

$$
IQR=Q_3-Q_1
$$

Here:

- $Q_1$ = first quartile
- $Q_3$ = third quartile

### Worked Example

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

The IQR is less sensitive to extreme observations than the range.

## 10. Percentiles

A percentile describes the relative position of a value in an ordered dataset.

For example, being at the 90th percentile means the value is at or above roughly 90% of the observations, depending on the percentile convention being used.

Percentiles are commonly used for:

- examination scores
- growth measurements
- salaries
- performance rankings

Different software and textbooks may use different percentile interpolation conventions, so the method should always be stated when exact numerical results matter.

## 11. Five-Number Summary

The five-number summary contains:

1. Minimum
2. $Q_1$
3. Median
4. $Q_3$
5. Maximum

For example:

$$
10,\ 20,\ 30,\ 40,\ 50
$$

The five-number summary is:

| Measure | Value |
|---|---:|
| Minimum | 10 |
| $Q_1$ | depends on the quartile convention |
| Median | 30 |
| $Q_3$ | depends on the quartile convention |
| Maximum | 50 |

The exact quartiles can depend on the method used.

## 12. Variance

Variance measures the average squared deviation from the mean.

For a population:

$$
\sigma^2=
\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

For a sample:

$$
s^2=
\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Here:

- $\sigma^2$ = population variance
- $s^2$ = sample variance
- $N$ = population size
- $n$ = sample size
- $\mu$ = population mean
- $\bar{x}$ = sample mean

The denominator differs because sample variance uses $n-1$ for the usual unbiased estimator of population variance under the standard random-sampling assumptions.

### Worked Example: Population Variance

Consider:

$$
2,\ 4,\ 6
$$

First calculate the mean:

$$
\mu=\frac{2+4+6}{3}
$$

$$
\mu=\frac{12}{3}=4
$$

Now calculate deviations:

$$
2-4=-2
$$

$$
4-4=0
$$

$$
6-4=2
$$

Square the deviations:

$$
(-2)^2=4
$$

$$
0^2=0
$$

$$
2^2=4
$$

Add them:

$$
4+0+4=8
$$

Divide by the population size:

$$
\sigma^2=\frac{8}{3}
$$

Therefore:

$$
\boxed{\sigma^2=\frac83\approx2.67}
$$

## 13. Standard Deviation

Standard deviation is the square root of variance.

For a population:

$$
\sigma=\sqrt{\sigma^2}
$$

For a sample:

$$
s=\sqrt{s^2}
$$

Using the previous population variance:

$$
\sigma^2=\frac83
$$

Therefore:

$$
\sigma=\sqrt{\frac83}
$$

$$
\boxed{\sigma\approx1.63}
$$

Standard deviation is expressed in the **same units as the original data**, unlike variance.

## 14. Mean Absolute Deviation

Mean Absolute Deviation, or MAD, measures the average absolute distance from a chosen center, often the mean.

Using the mean:

$$
MAD=\frac{\sum |x_i-\bar{x}|}{n}
$$

The absolute value removes negative signs while preserving the size of the deviation.

### Example

For:

$$
2,\ 4,\ 6
$$

the mean is:

$$
\bar{x}=4
$$

Absolute deviations:

$$
|2-4|=2
$$

$$
|4-4|=0
$$

$$
|6-4|=2
$$

Therefore:

$$
MAD=\frac{2+0+2}{3}
$$

$$
\boxed{MAD=\frac43\approx1.33}
$$

## 15. Frequency Distribution

A frequency distribution records how often values or intervals occur.

For example:

| Marks | Frequency |
|---|---:|
| 0–20 | 3 |
| 21–40 | 7 |
| 41–60 | 12 |
| 61–80 | 8 |
| 81–100 | 5 |

This gives a compact view of the dataset.

## 16. Histogram

A histogram represents the distribution of numerical data using adjacent intervals called bins.

Histograms are useful for understanding:

- concentration
- spread
- skewness
- gaps
- possible outliers

A histogram differs from a bar chart because histogram bars represent numerical intervals and are typically adjacent.

## 17. Bar Chart

A bar chart is commonly used for categorical data.

For example:

| Department | Students |
|---|---:|
| CSE | 120 |
| ECE | 80 |
| ME | 60 |

The categories are separate groups, so the bars represent categories rather than continuous numerical intervals.

## 18. Box Plot

A box plot summarizes a distribution using the five-number summary.

It shows:

- minimum or lower whisker
- $Q_1$
- median
- $Q_3$
- maximum or upper whisker
- possible outliers

A common rule for identifying potential outliers is:

$$
Lower\ Fence=Q_1-1.5(IQR)
$$

$$
Upper\ Fence=Q_3+1.5(IQR)
$$

Observations outside these fences are commonly flagged as potential outliers.

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
IQR=50-20=30
$$

Lower fence:

$$
20-1.5(30)
$$

$$
=20-45
$$

$$
\boxed{-25}
$$

Upper fence:

$$
50+1.5(30)
$$

$$
=50+45
$$

$$
\boxed{95}
$$

Values below -25 or above 95 would be flagged by this rule.

## 19. Skewness

Skewness describes the asymmetry of a distribution.

### Positive Skew

A distribution with a longer right tail is positively skewed.

### Negative Skew

A distribution with a longer left tail is negatively skewed.

### Symmetric Distribution

A symmetric distribution has approximately balanced tails around its center.

![Types of Skewness](https://assets.mbrenndoerfer.com/notebooks/2_probability_fundamentals_files/skewness-distribution-examples.png)

*Source: Michael Brenndoerfer — Distributions with Different Skewness.*

The image compares negative skewness, zero skewness (symmetric distribution), and positive skewness. A positive skew has a longer right tail, while a negative skew has a longer left tail.

Skewness helps us understand whether the mean and median may differ substantially.

## 20. Kurtosis

Kurtosis describes aspects of the shape of a distribution, particularly tail heaviness relative to a reference distribution.

In practical data analysis, kurtosis is useful when investigating whether a distribution has unusually heavy or light tails.

Terms often encountered include:

- mesokurtic
- leptokurtic
- platykurtic

The precise definition of kurtosis depends on the convention being used, so software documentation and the chosen statistical definition should be checked when reporting exact values.

## 21. Standardization

Standardization converts an observation into a z-score.

The formula is:

$$
z=\frac{x-\mu}{\sigma}
$$

Here:

- $x$ = observation
- $\mu$ = population mean
- $\sigma$ = population standard deviation

For a sample-based calculation, corresponding sample quantities may be used.

### Worked Example

Suppose:

$$
x=80
$$

$$
\mu=70
$$

$$
\sigma=5
$$

Substitute:

$$
z=\frac{80-70}{5}
$$

$$
=\frac{10}{5}
$$

$$
\boxed{z=2}
$$

The observation is 2 standard deviations above the mean.

Standardization is especially useful when variables are measured on different scales.

## 22. Normalization

Normalization rescales data into a specified range.

A common min-max normalization formula is:

$$
x'=\frac{x-x_{min}}{x_{max}-x_{min}}
$$

To scale into the range $[0,1]$:

Suppose:

$$
x=70,\quad x_{min}=50,\quad x_{max}=100
$$

Then:

$$
x'=\frac{70-50}{100-50}
$$

$$
=\frac{20}{50}
$$

$$
\boxed{x'=0.4}
$$

Normalization and standardization are different techniques and should not be treated as interchangeable.

## 23. Choosing the Right Measure

A useful practical guide is:

| Data situation | Useful measures |
|---|---|
| Roughly symmetric numerical data | Mean and standard deviation |
| Skewed numerical data | Median and IQR |
| Strong outliers | Median and IQR |
| Categorical data | Mode and frequency |
| Need relative position | Percentiles |
| Need spread of middle 50% | IQR |

The correct choice depends on the shape and purpose of the analysis.

## 24. Descriptive Statistics in Data Science

A common workflow is:

```
Raw Dataset
    ↓
Understand Variables
    ↓
Clean Data
    ↓
Descriptive Statistics
    ↓
Inspect Distribution
    ↓
Identify Patterns / Outliers
    ↓
Further Statistical or ML Analysis
```

Before building a Machine Learning model, we often need to understand typical values, spread, missing values, extreme values, and distribution shape.

## Points to Remember

- Mean is the arithmetic average.
- Median is the middle value after sorting.
- Mode is the most frequently occurring value.
- Mean is sensitive to extreme values.
- Median is generally more resistant to extreme values.
- Range = maximum − minimum.
- Variance measures squared deviation from the mean.
- Standard deviation is the square root of variance.
- Population and sample variance use different denominators.
- $IQR=Q_3-Q_1$.
- $Q_2$ is the median.
- Percentiles describe relative position.
- The five-number summary contains minimum, $Q_1$, median, $Q_3$, and maximum.
- Histograms are useful for numerical distributions.
- Bar charts are useful for categorical comparisons.
- Box plots summarize distribution and help identify potential outliers.
- Skewness describes asymmetry.
- Kurtosis describes aspects of tail behaviour.
- Standardization produces z-scores.
- Normalization rescales values, often to $[0,1]$.
- Always understand whether you are describing a population or a sample before choosing a formula.

## References

- [GeeksforGeeks — Measures of Central Tendency and Dispersion](https://www.geeksforgeeks.org/maths/measures-of-central-tendency-and-dispersion/)
- [GeeksforGeeks — Descriptive Statistics](https://www.geeksforgeeks.org/maths/descriptive-statistics/)
- [Khan Academy — Summarizing Quantitative Data](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
