# 01 Statistics Fundamentals

Statistics is the foundation for understanding data. It helps us collect, organize, summarize, analyze, interpret, and communicate information so that decisions can be made using evidence.

This folder focuses on the **language and foundations of statistics**. Detailed numerical techniques such as mean, variance, probability, probability distributions, hypothesis testing, ANOVA, and regression are developed in the later folders.

## 1. What is Statistics?

Statistics is the study of data and the methods used to learn from it.

A typical statistical process can be understood as:

```
Data
  ↓
Collect
  ↓
Organize
  ↓
Summarize
  ↓
Analyze
  ↓
Interpret
  ↓
Make a decision
```

For example, a university may collect student marks, attendance, study hours, department, and other information. Statistics helps turn these observations into useful conclusions.

Statistics is therefore not simply about performing calculations. It is also about deciding **which data to collect, how to collect it, which method is appropriate, and what the results actually mean**.

![Types of Statistics](https://media.geeksforgeeks.org/wp-content/uploads/20250222144920592095/stat.webp)

*Source: GeeksforGeeks — Statistics.*

## 2. Descriptive and Inferential Statistics

Statistics is commonly divided into two major branches.

### Descriptive Statistics

Descriptive statistics describes the data that has actually been collected.

Examples include:

- mean
- median
- mode
- variance
- standard deviation
- tables
- graphs

### Inferential Statistics

Inferential statistics uses sample data to make conclusions about a larger population.

Examples include:

- estimation
- confidence intervals
- hypothesis testing
- prediction

The distinction is important:

> **Descriptive statistics tells us what the observed data looks like. Inferential statistics uses data to learn about a wider population.**

## 3. Population and Sample

### Population

A **population** is the complete group that we want to study.

For example, if a university wants to study the average height of all its students, all students in that university form the population.

### Sample

A **sample** is a smaller group selected from the population.

If the university selects 500 students and measures their heights, those 500 students form the sample.

```
Population
┌─────────────────────────────────────┐
│  All students in the university     │
│                                     │
│       ┌──────────────────┐          │
│       │     Sample       │          │
│       │   500 students   │          │
│       └──────────────────┘          │
└─────────────────────────────────────┘
```

A good sample should represent the population reasonably well.

## 4. Parameter and Statistic

These two terms are easy to confuse.

A **parameter** is a numerical value that describes a population.

A **statistic** is a numerical value calculated from a sample.

For example, suppose the average height of every student in a university is 168 cm.

That value is a **population parameter**.

If we select 500 students and calculate their average height as 167.4 cm, 167.4 cm is a **sample statistic**.

A useful memory rule is:

> **Parameter → Population**

> **Statistic → Sample**

### Common Symbols

Population mean is commonly written as:

$$
\mu
$$

Sample mean is commonly written as:

$$
\bar{x}
$$

Here:

- $\mu$ = population mean
- $\bar{x}$ = sample mean

The symbols will become important when we begin numerical statistics.

## 5. Census and Sampling

### Census

A census collects information from every member of the population.

For example, measuring every employee in a company is a census.

### Sampling

Sampling collects information from only a subset of the population.

Sampling is often preferred because a complete census may be expensive, slow, or difficult.

## 6. Sampling Methods

### Simple Random Sampling

Every member has an equal chance of being selected.

For example, randomly selecting 100 student IDs from a list of 5,000 students.

### Systematic Sampling

Select observations at a fixed interval.

For example, after choosing a starting point, select every 10th customer.

### Stratified Sampling

Divide the population into meaningful groups called **strata**, then sample from each group.

For example, a university may divide students by department and sample students from each department.

### Cluster Sampling

Divide the population into clusters, randomly select some clusters, and study the selected clusters.

For example, randomly selecting several schools and surveying students within those schools.

### Convenience Sampling

Select observations because they are easy to access.

For example, asking only nearby students about the opinion of all university students.

Convenience sampling is easy but can introduce substantial bias.

## 7. Sampling Error and Sampling Bias

### Sampling Error

Sampling error is the natural difference between a sample result and the true population value that occurs because we studied a sample rather than the entire population.

Suppose the true population mean is:

$$
\mu=70
$$

and a sample gives:

$$
\bar{x}=72
$$

Then the sample result differs from the population value.

The difference is:

$$
72-70=2
$$

This does not automatically mean that the sampling process was poor. Random samples naturally vary.

### Sampling Bias

Sampling bias is a systematic problem in the way the sample is selected.

For example, asking only gym members about the exercise habits of an entire city is likely to produce a biased sample.

> **Sampling error is random variation; sampling bias is a systematic problem.**

## 8. Data and Variables

A **variable** is a characteristic that can take different values for different observations.

Examples include:

- age
- height
- branch
- salary
- number of products
- satisfaction level

### Qualitative Data

Qualitative data represents categories or qualities.

Examples:

- blood group
- department
- color
- product type

### Quantitative Data

Quantitative data represents numerical quantities.

Examples:

- height
- weight
- income
- number of customers

![Types of Data](https://media.geeksforgeeks.org/wp-content/uploads/20250915162411637111/types_of_data.webp)

*Source: GeeksforGeeks — Data and its Types.*

## 9. Discrete and Continuous Data

### Discrete Data

Discrete data is countable.

Examples:

- number of students
- number of cars
- number of defective products

You can have 5 or 6 cars, but normally not 5.37 cars.

### Continuous Data

Continuous data is measured and can take values within a range.

Examples:

- height
- weight
- temperature
- time

A person's height could be 170 cm, 170.5 cm, or 170.53 cm.

A useful rule is:

> **Count → usually discrete**

> **Measure → usually continuous**

## 10. Levels of Measurement

Measurement levels describe the mathematical meaning of data.

### Nominal

Nominal data consists of categories without a meaningful order.

Examples:

- blood group
- department
- city
- product category

### Ordinal

Ordinal data has a meaningful order, but the difference between categories is not necessarily equal.

Example:

```
Poor < Fair < Good < Excellent
```

We know Excellent is higher than Good, but we cannot automatically say that the difference between Poor and Fair equals the difference between Good and Excellent.

### Interval

Interval data has ordered values with equal intervals, but zero does not represent a complete absence of the quantity.

Temperature in Celsius is a common example.

The difference between 20°C and 30°C is the same as the difference between 30°C and 40°C, but 0°C does not mean "no temperature."

### Ratio

Ratio data has equal intervals and a meaningful zero.

Examples:

- height
- weight
- age
- income
- distance

If one object weighs 20 kg and another weighs 10 kg, the first weighs twice as much.

## 11. Frequency

Frequency tells us how many times a value occurs.

Suppose:

```
Marks = 60, 70, 70, 80, 80, 80
```

The frequencies are:

| Mark | Frequency |
|---:|---:|
| 60 | 1 |
| 70 | 2 |
| 80 | 3 |

The value 80 has the highest frequency.

Detailed frequency distributions and graphs are covered in **02 Descriptive Statistics**.

## 12. Sampling Distribution

A sampling distribution is the probability distribution of a statistic calculated from many possible samples of the same size from a population.

For example, imagine repeatedly selecting samples of 50 students and calculating the sample mean each time.

```
Population
    ↓
Sample 1 → mean
Sample 2 → mean
Sample 3 → mean
Sample 4 → mean
    ↓
Distribution of sample means
```

The sampling distribution becomes important in inferential statistics.

## 13. Standard Error

The **standard error** measures the variability of a sample statistic across repeated samples.

For the sample mean, under the usual independent-sampling setup:

$$
SE(\bar{x})=\frac{\sigma}{\sqrt{n}}
$$

where:

- $SE(\bar{x})$ = standard error of the sample mean
- $\sigma$ = population standard deviation
- $n$ = sample size

If the population standard deviation is 10 and the sample size is 100:

$$
SE(\bar{x})=\frac{10}{\sqrt{100}}
$$

Since:

$$
\sqrt{100}=10
$$

we get:

$$
SE(\bar{x})=\frac{10}{10}=1
$$

Therefore:

$$
\boxed{SE(\bar{x})=1}
$$

This shows why larger samples generally produce more stable estimates of the population mean.

## 14. Outliers

An outlier is an observation that is unusually far from the other observations.

For example:

```
20, 22, 21, 23, 24, 150
```

The value 150 is much larger than the other observations.

An outlier may be:

- a genuine extreme observation
- a measurement error
- a data-entry error
- evidence of an unusual process

An outlier should **not automatically be deleted**. It should first be investigated.

## 15. Notation You Will See Later

| Symbol | Meaning |
|---|---|
| $N$ | Population size |
| $n$ | Sample size |
| $\mu$ | Population mean |
| $\bar{x}$ | Sample mean |
| $\sigma$ | Population standard deviation |
| $s$ | Sample standard deviation |
| $P(A)$ | Probability of event $A$ |
| $SE$ | Standard error |

Defining notation before using formulas is important because the same mathematical symbols appear repeatedly throughout statistics.

## 16. Practical Classification Example

Consider the following variables:

| Variable | Classification |
|---|---|
| Blood group | Qualitative, nominal |
| Satisfaction level | Qualitative, ordinal |
| Temperature in °C | Quantitative, interval |
| Weight in kg | Quantitative, ratio, continuous |
| Number of students | Quantitative, ratio, discrete |
| Student ID | Nominal label |
| Number of website visits | Quantitative, ratio, discrete |
| Height | Quantitative, ratio, continuous |

A variable being written as a number does **not** automatically make it quantitative.

For example:

```
Student ID = 101, 102, 103
```

These numbers are labels, not measurements.

## Points to Remember

- Statistics helps us learn from data.
- Descriptive statistics summarizes observed data.
- Inferential statistics uses samples to learn about populations.
- A population is the complete group being studied.
- A sample is a subset of the population.
- A parameter describes a population.
- A statistic describes a sample.
- Qualitative data represents categories.
- Quantitative data represents numerical quantities.
- Discrete data is countable.
- Continuous data is measurable.
- Nominal data has categories without order.
- Ordinal data has order.
- Interval data has equal intervals but no true zero.
- Ratio data has equal intervals and a meaningful zero.
- Sampling error is natural random variation.
- Sampling bias is a systematic problem.
- Do not confuse numeric labels with quantitative measurements.
- Never remove an outlier automatically; investigate it first.
- Standard error describes the variability of a statistic across repeated samples.

## References

- [GeeksforGeeks — Statistics](https://www.geeksforgeeks.org/maths/introduction-to-statistics/)
- [GeeksforGeeks — Data and its Types](https://www.geeksforgeeks.org/data-analysis/what-is-data/)
- [GeeksforGeeks — Population and Sample](https://www.geeksforgeeks.org/maths/population-and-sample-statistics/)
- [GeeksforGeeks — Methods of Sampling](https://www.geeksforgeeks.org/data-science/methods-of-sampling/)
- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics-2e)
