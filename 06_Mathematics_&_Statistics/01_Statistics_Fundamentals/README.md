# 01 Statistics Fundamentals

Statistics is one of the foundations of Data Science, Machine Learning, Artificial Intelligence, experimentation, and data-driven decision making.

This folder builds the **fundamental statistical vocabulary and concepts** needed before moving to Descriptive Statistics, Probability, Probability Distributions, Inferential Statistics, Hypothesis Testing, ANOVA, Correlation & Regression, and Machine Learning.

> **Scope:** This folder focuses on concepts and foundations. Detailed calculations such as mean/median/mode, variance, standard deviation, probability rules, distributions, hypothesis tests, ANOVA, and regression are covered in the later Statistics folders.

---

## Folder Structure

```text
01_Statistics_Fundamentals/
│
├── README.md
└── Statistics_Fundamentals.ipynb
```

---

# 1. What is Statistics?

**Statistics** is the discipline of collecting, organizing, summarizing, analyzing, interpreting, and communicating data so that useful conclusions can be made.

A simple way to remember the idea is:

```text
Raw Data
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

For example, suppose a college wants to understand student performance. It may collect marks, attendance, branch, study hours, and other information. Statistics helps convert these observations into useful information such as average marks, variation in marks, relationships between variables, and evidence for decisions.

Statistics is not simply "doing calculations." A major goal is understanding what the numbers mean and whether the conclusion is justified by the data.

**Reference:** [GeeksforGeeks – Statistics: The Foundation of Data Science & Analytics](https://www.geeksforgeeks.org/data-science/statistics-the-foundation-of-data-science/)

---

# 2. Why Do We Need Statistics?

Real-world data is usually too large, messy, or variable to understand just by looking at individual observations.

Statistics helps us:

- summarize large datasets
- compare groups
- identify patterns and trends
- quantify variation
- estimate unknown population characteristics
- measure uncertainty
- test claims
- support decisions
- communicate evidence clearly

### Example

Imagine an e-commerce company has 10 million orders. Looking at every order individually is not useful for a manager.

Statistics can answer questions such as:

- What is the average order value?
- Which category sells the most?
- How much do order values vary?
- What percentage of customers return products?
- Is a new recommendation system improving conversion?

These questions lead into descriptive and inferential statistics.

---

# 3. Statistics in Data Science

Statistics provides the foundation for understanding data before and after machine-learning models are built.

```text
Data
  ↓
Statistics
  ↓
Understanding the data
  ↓
Feature engineering / modeling
  ↓
Model evaluation
  ↓
Decision
```

Statistics appears in:

- Exploratory Data Analysis (EDA)
- sampling
- A/B testing
- confidence intervals
- hypothesis testing
- feature analysis
- model evaluation
- uncertainty estimation
- experiment design
- anomaly detection

The important distinction for this repository is:

> **Statistics & Mathematics** = mathematical/statistical foundations.
>
> **Machine Learning** = practical model implementation and applied workflows.

---

# 4. Two Major Types of Statistics

Statistics is commonly divided into **Descriptive Statistics** and **Inferential Statistics**.

![Types of Statistics](https://media.geeksforgeeks.org/wp-content/uploads/20250222144920592095/stat.webp)

*Image source: GeeksforGeeks, [Statistics: The Foundation of Data Science & Analytics](https://www.geeksforgeeks.org/data-science/statistics-the-foundation-of-data-science/).* 

## 4.1 Descriptive Statistics

Descriptive statistics describes the data that has actually been collected.

Common tools include:

- tables
- frequency distributions
- charts
- mean
- median
- mode
- range
- variance
- standard deviation

Example:

**Marks = [60, 70, 72, 80, 88]**

Saying that the average mark is 74 is a **descriptive** statement about these observations.

## 4.2 Inferential Statistics

Inferential statistics uses sample data to make statements or decisions about a larger population.

Examples include:

- estimating a population mean
- confidence intervals
- hypothesis testing
- predicting population behavior from a sample

Example:

A university has 50,000 students. We survey 500 students and use their responses to estimate the opinion of the entire student population.

**Reference:** [OpenStax – Definitions of Statistics, Probability, and Key Terms](https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms)

---

# 5. Population

A **population** is the complete set of individuals, objects, events, or observations that a study is interested in.

The population does not always mean "all people in the world." It depends on the research question.

### Examples

| Research question | Population |
|---|---|
| Average marks of a class | All students in that class |
| Customer satisfaction for a company | All relevant customers |
| Average height of students in a university | All students in that university |
| Spam detection | All emails relevant to the problem |
| Average response time of a server | All relevant server requests |

Population size is commonly represented by **N**.

![Population and Sample](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220302154028/Group-13.jpg)

*Image source: GeeksforGeeks, [Population vs Sample in Statistics](https://www.geeksforgeeks.org/maths/population-and-sample-statistics/).* 

---

# 6. Sample

A **sample** is a subset of the population selected for analysis.

We use samples because studying an entire population may be:

- expensive
- time-consuming
- geographically difficult
- technically impossible
- destructive in some experiments

Sample size is commonly represented by **n**.

### Example

Population:

> All 50,000 students of a university.

Sample:

> 500 students selected for a survey.

The objective is to use the sample to learn something about the population.

**Reference:** [GeeksforGeeks – Population vs Sample in Statistics](https://www.geeksforgeeks.org/maths/population-and-sample-statistics/)

---

# 7. Population vs Sample

| Population | Sample |
|---|---|
| Entire group of interest | Subset of the population |
| Usually denoted by N | Usually denoted by n |
| Describes the complete group | Used to represent the group |
| Parameter describes it | Statistic describes it |
| Often expensive/impractical to measure completely | Usually cheaper and faster |

### Easy memory trick

**POPULATION = ALL**
**SAMPLE     = SOME**

---

# 8. Parameter

A **parameter** is a numerical value that describes a characteristic of a population.

Examples:

- population mean: **μ**
- population standard deviation: **σ**
- population proportion: often **p**

Suppose the average height of **every** student in a university is 168.4 cm. That 168.4 cm is a population parameter.

The important point is that a parameter describes the **population**, not merely a sample.

---

# 9. Statistic

A **statistic** is a numerical value calculated from sample data.

Examples:

- sample mean: **x̄**
- sample standard deviation: **s**
- sample proportion: often **p̂**

If we randomly select 500 students and calculate their average height as 167.9 cm, then 167.9 cm is a sample statistic.

The statistic can be used to estimate the unknown population parameter.

```text
Population
    ↓
Parameter (usually unknown)
    ↑
    │ estimate
    │
Statistic
    ↑
Sample
```

**Reference:** [GeeksforGeeks – Population vs Sample in Statistics](https://www.geeksforgeeks.org/maths/population-and-sample-statistics/)

---

# 10. Parameter vs Statistic

| Parameter | Statistic |
|---|---|
| Describes a population | Describes a sample |
| Population quantity | Sample quantity |
| Often unknown | Calculated from observed data |
| μ, σ, p are common symbols | x̄, s, p̂ are common symbols |
| Can be estimated using a statistic | Used to estimate a parameter |

### Example

Suppose:

**Population = all 20,000 employees**
**Sample = 500 employees**

If the true average salary of all 20,000 employees is μ, that is a parameter.

If the average salary of the 500 sampled employees is x̄, that is a statistic.

---

# 11. Census vs Sample Survey

## Census

A **census** collects information from every member of the population.

Example:

> Collecting information from every student in a college.

Advantages:

- complete population information
- no sampling error from selecting a subset

Disadvantages:

- expensive
- time-consuming
- difficult for very large populations

## Sample Survey

A **sample survey** collects information from only a subset of the population.

Advantages:

- faster
- cheaper
- practical for large populations

Disadvantages:

- sampling error can occur
- poor sampling can create bias

---

# 12. Data

**Data** are observations, measurements, records, or values collected for analysis.

Examples:

**Age = 22
Height = 170.5 cm
City = Lucknow
Marks = 87
Department = CSE**

A single value is often called a **datum**, while multiple observations are called **data**.

OpenStax explains that data are the actual values of variables collected from a population or sample.

**Reference:** [OpenStax – Data, Sampling, and Variation](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)

---

# 13. Variable

A **variable** is a characteristic or measurement that can take different values for different observations.

Examples:

- age
- height
- weight
- marks
- city
- department
- number of purchases

If `X = marks`, then different students may have different values of X.

**Student A → X = 78
Student B → X = 91
Student C → X = 65**

The variable is **marks**; the individual values are the observations.

---

# 14. Independent and Dependent Variables

These terms are especially important when studying relationships between variables.

## Independent Variable

The variable that is changed, controlled, or used as a predictor.

## Dependent Variable

The outcome that is measured.

### Example

Suppose we study whether study hours affect exam marks.

```text
Study Hours ─────────→ Exam Marks
(independent)          (dependent)
```

Here:

- **Study hours = independent variable**
- **Exam marks = dependent variable**

> Remember: correlation or association alone does not automatically prove causation.

---

# 15. Qualitative Data

**Qualitative data** describes categories, qualities, or characteristics rather than a measured numerical amount.

It is also commonly called **categorical data**.

Examples:

- blood group
- department
- city
- eye color
- product category
- operating system

Example:

**Department = CSE
Department = ECE
Department = Mechanical**

These are categories.

---

# 16. Quantitative Data

**Quantitative data** represents quantities that can be expressed numerically.

Examples:

- age
- height
- weight
- salary
- number of products
- temperature
- marks

Quantitative data is commonly divided into:

```text
Quantitative Data
├── Discrete
└── Continuous
```

---

# 17. Discrete Data

**Discrete data** consists of countable values.

Examples:

- number of students
- number of cars
- number of emails
- number of defects
- number of children

For example:

**Number of students = 45**

You can have 45 students, but normally not 45.37 students.

---

# 18. Continuous Data

**Continuous data** can take any value within a range, depending on measurement precision.

Examples:

- height
- weight
- temperature
- time
- distance
- voltage

Example:

**Height = 170 cm
Height = 170.2 cm
Height = 170.27 cm**

The measurement can become more precise depending on the measuring instrument.

---

# 19. Qualitative vs Quantitative

![Types of Data](https://media.geeksforgeeks.org/wp-content/uploads/20260818105623706789/types_of_data.webp)

*Image source: GeeksforGeeks, [Statistics: The Foundation of Data Science & Analytics](https://www.geeksforgeeks.org/data-science/statistics-the-foundation-of-data-science/).* 

| Qualitative | Quantitative |
|---|---|
| Describes categories | Represents quantities |
| Usually categorical | Numerical |
| Example: color | Example: height |
| Example: department | Example: marks |
| Often summarized using counts/proportions | Often summarized using numerical measures |

**Reference:** [OpenStax – Data, Sampling, and Variation](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)

---

# 20. Nominal Data

**Nominal data** consists of categories with no meaningful ranking.

Examples:

- blood group: A, B, AB, O
- color: red, blue, green
- operating system: Windows, Linux, macOS
- city: Lucknow, Hyderabad, Delhi

If we encode:

**Windows = 1
Linux   = 2
macOS   = 3**

the numbers are only labels. `3` is not "greater" than `1` in a statistical sense.

For nominal data, common summaries include:

- frequency counts
- proportions/percentages
- mode

---

# 21. Ordinal Data

**Ordinal data** has categories that have a meaningful order or ranking, but the distance between adjacent categories is not necessarily equal.

Examples:

**Poor < Fair < Good < Excellent**

or

**Beginner < Intermediate < Advanced**

We know the order, but we cannot assume that the difference between Poor and Fair is the same as the difference between Good and Excellent.

Common summaries include:

- frequency
- percentages
- mode
- median/rank-based summaries where appropriate

---

# 22. Interval Data

**Interval data** has ordered values and meaningful, equal differences between values, but it does not have a meaningful absolute zero.

A standard example is temperature in Celsius.

The difference between 10°C and 20°C is the same size as the difference between 30°C and 40°C: both differences are 10 degrees.

However:

> 40°C is not meaningfully "twice as hot" as 20°C.

This is because 0°C does not represent the complete absence of temperature.

---

# 23. Ratio Data

**Ratio data** has:

1. categories/order where relevant
2. meaningful differences
3. equal intervals
4. a true zero

Examples:

- height
- weight
- age
- distance
- income
- reaction time
- number of items

For ratio data, statements such as "20 kg is twice 10 kg" are meaningful because zero kg represents the absence of weight.

---

# 24. Four Levels of Measurement

![Four Levels of Measurement](https://media.geeksforgeeks.org/wp-content/uploads/20251206123755209876/the_four_level_of_measu.webp)

*Image source: GeeksforGeeks, [Statistics: The Foundation of Data Science & Analytics](https://www.geeksforgeeks.org/data-science/statistics-the-foundation-of-data-science/).* 

| Level | Ordered? | Equal intervals? | True zero? | Example |
|---|---:|---:|---:|---|
| Nominal | No | No | No | Blood group |
| Ordinal | Yes | Not guaranteed | No | Satisfaction level |
| Interval | Yes | Yes | No | Celsius temperature |
| Ratio | Yes | Yes | Yes | Weight |

A useful way to remember the hierarchy:

```text
Nominal
   ↓ + order
Ordinal
   ↓ + equal intervals
Interval
   ↓ + true zero
Ratio
```

**References:**

- [OpenStax – Levels of Measurement](https://openstax.org/books/introductory-statistics-2e/pages/1-3-frequency-frequency-tables-and-levels-of-measurement)
- [GeeksforGeeks – Scales of Measurement](https://www.geeksforgeeks.org/data-science/scales-of-measurement-in-business-statistics/)

---

# 25. Univariate, Bivariate, and Multivariate Data

Another way to classify data is by the number of variables being studied.

## Univariate

One variable.

Example:

> Heights of 100 students.

## Bivariate

Two variables.

Example:

> Study hours and exam marks.

## Multivariate

More than two variables.

Example:

> Age, study hours, attendance, sleep hours, and exam marks.

![Types of Statistical Data](https://media.geeksforgeeks.org/wp-content/uploads/20231116153056/Types-of-Statistical-Data-copy.webp)

*Image source: GeeksforGeeks, [Types of Statistical Data](https://www.geeksforgeeks.org/data-analysis/types-of-statistical-data/).* 

---

# 26. Cross-Sectional Data

**Cross-sectional data** records observations for multiple subjects at approximately one point in time or one defined period.

Example:

A survey of 1,000 students conducted in October 2026 containing:

- age
- branch
- marks
- attendance

Each row represents a different student.

---

# 27. Time-Series Data

**Time-series data** records observations over time.

Example:

```text
Month       Sales
January     1200
February    1350
March       1280
April       1500
```

The order of observations matters because time is part of the data.

Time-series analysis will be studied in more detail later.

---

# 28. Primary Data

**Primary data** is collected directly by the researcher or organization for the current study.

Examples:

- conducting your own survey
- interviewing customers
- measuring temperature yourself
- running an experiment
- collecting application logs for a specific study

Advantages:

- collected for a specific purpose
- researcher controls the collection process

Disadvantages:

- can be expensive
- takes time
- requires planning

---

# 29. Secondary Data

**Secondary data** is data that was previously collected by another person, organization, or system and is reused for analysis.

Examples:

- government datasets
- public research datasets
- company reports
- Kaggle datasets
- historical databases
- published survey results

Before using secondary data, check:

- source
- collection method
- date
- definitions
- missing values
- possible bias
- licensing/usage conditions

---

# 30. Observation

An **observation** is one recorded instance or row of data.

Example dataset:

| Student | Age | Marks |
|---|---:|---:|
| A | 20 | 78 |
| B | 21 | 85 |
| C | 20 | 91 |

Each row is an observation.

The dataset contains 3 observations.

---

# 31. Frequency

**Frequency** means the number of times a value or category occurs.

Example:

```text
Marks = [60, 70, 70, 80, 80, 80]
```

Frequency:

| Marks | Frequency |
|---:|---:|
| 60 | 1 |
| 70 | 2 |
| 80 | 3 |

Frequency tables and distributions are covered more deeply in the Descriptive Statistics folder.

**Reference:** [OpenStax – Frequency, Frequency Tables, and Levels of Measurement](https://openstax.org/books/introductory-statistics-2e/pages/1-3-frequency-frequency-tables-and-levels-of-measurement)

---

# 32. Frequency Distribution

A **frequency distribution** organizes values into categories or intervals and records how often observations fall into them.

For example:

| Marks range | Frequency |
|---|---:|
| 0–39 | 2 |
| 40–59 | 5 |
| 60–79 | 12 |
| 80–100 | 8 |

This makes a large set of observations easier to understand.

---

# 33. Sampling

**Sampling** is the process of selecting a subset of a population for study.

A good sample should provide useful information about the population it represents.

The choice of sampling method affects the quality of conclusions.

OpenStax describes simple random, stratified, cluster, and systematic sampling as common random sampling methods.

**Reference:** [OpenStax – Data, Sampling, and Variation](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)

---

# 34. Simple Random Sampling

In **simple random sampling**, individuals are selected randomly so that each member has an appropriate chance of selection and each sample of the required size is equally likely under the standard SRS definition.

Example:

**Population = 1,000 students
Sample size = 100**

Use a random selection process to choose 100 students.

Advantages:

- conceptually simple
- reduces researcher selection preference

Limitation:

- requires a suitable sampling frame

---

# 35. Systematic Sampling

In **systematic sampling**, we select observations at regular intervals after choosing a starting point.

Example:

```text
Population list = 1, 2, 3, ... 1000
Sampling interval = 10
Starting point = 7

Selected = 7, 17, 27, 37, ...
```

This is easy to implement, but the ordering of the population list should be considered because periodic patterns can introduce problems.

---

# 36. Stratified Sampling

In **stratified sampling**, the population is divided into meaningful subgroups called **strata**, and samples are taken from the strata.

Example:

```text
University
├── CSE
├── ECE
├── Mechanical
└── Civil
```

If we want every branch represented, we can sample students from each branch.

The groups should be defined using a characteristic relevant to the study.

---

# 37. Cluster Sampling

In **cluster sampling**, the population is divided into groups called clusters, and some clusters are randomly selected for study.

Example:

```text
City
├── School A
├── School B
├── School C
├── School D
└── School E
```

Instead of selecting students from every school, we might randomly select several schools and study students within the selected schools.

Cluster sampling can reduce logistical cost, but clusters should be considered carefully because observations within a cluster may be more similar to one another.

---

# 38. Convenience Sampling

**Convenience sampling** selects people or observations that are easiest to access.

Example:

> Asking only people currently sitting in your classroom about the opinion of all university students.

It is easy, but it can be biased because the people who are easiest to reach may not represent the entire population.

Convenience sampling is **not** the same as random sampling.

---

# 39. Sampling Bias

**Sampling bias** occurs when the sampling process systematically makes some members of the target population more or less likely to be included, leading to a sample that does not adequately represent the population.

Example:

Suppose a university wants to know whether students like online classes, but the survey is sent only to students who voluntarily signed up for an online-learning club.

The respondents may have unusually positive opinions about online learning.

Potential result:

```text
Biased sample
     ↓
Biased statistic
     ↓
Poor inference about population
```

**Reference:** [OpenStax – Data, Sampling, and Variation](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)

---

# 40. Sampling Error

**Sampling error** is the natural difference between a sample-based result and the corresponding population value caused by studying a sample rather than the entire population.

Even a well-designed random sample will generally not have exactly the same mean as the population.

Example:

**Population mean = 70.0
Sample mean     = 71.4**

The difference does not automatically mean the sample was badly collected. Some variation is expected from sampling.

This is different from **sampling bias**.

**Sampling error → random variation
Sampling bias  → systematic problem in selection**

---

# 41. Data Bias and Other Sources of Error

Not every problem comes from the sampling process.

Possible sources include:

- selection bias
- non-response bias
- measurement error
- response bias
- interviewer effects
- poorly worded questions
- data-entry errors
- missing data
- survivorship bias

A statistically sophisticated analysis cannot completely fix fundamentally poor data collection.

---

# 42. Outlier – Basic Introduction

An **outlier** is an observation that is unusually far from the general pattern of the data.

Example:

**12, 13, 14, 15, 16, 17, 95**

The value `95` looks unusual compared with the other observations.

An outlier may be caused by:

- measurement error
- data-entry error
- unusual but genuine observation
- rare event
- different population/process

Do **not** automatically delete an outlier. First investigate why it exists.

Detailed outlier detection will be covered later in Descriptive Statistics / EDA.

---

# 43. Statistical Notation – Basic Symbols

| Symbol | Meaning |
|---|---|
| N | Population size |
| n | Sample size |
| μ | Population mean |
| x̄ | Sample mean |
| σ | Population standard deviation |
| s | Sample standard deviation |
| p | Population proportion |
| p̂ | Sample proportion |
| Σ | Summation |
| X | A variable/random quantity or observation, depending on context |

### Important

Symbols can vary slightly between textbooks, so always read the definition being used in the particular context.

---

# 44. One Complete Example

Suppose a university has **10,000 students** and wants to estimate average daily study time.

### Step 1 – Population

All 10,000 students.

### Step 2 – Sample

Randomly select 500 students.

### Step 3 – Variable

Daily study time in hours.

### Step 4 – Data type

Quantitative and continuous.

### Step 5 – Parameter

The true average study time of all 10,000 students, μ.

### Step 6 – Statistic

The average study time calculated from the 500 sampled students, x̄.

### Step 7 – Inference

Use the sample statistic to estimate the population parameter.

This single example connects many of the fundamental terms together.

---

# 45. Quick Classification Practice

Classify each variable.

| Variable | Classification |
|---|---|
| Blood group | Qualitative, nominal |
| Satisfaction: Poor/Fair/Good/Excellent | Qualitative, ordinal |
| Temperature in °C | Quantitative, interval |
| Weight in kg | Quantitative, ratio, continuous |
| Number of children | Quantitative, ratio, discrete |
| Student ID | Nominal label, even though numeric-looking |
| Number of website visits | Quantitative, ratio, discrete |
| Height | Quantitative, ratio, continuous |

### Important lesson

A variable being written using numbers does **not** automatically make it quantitative in the meaningful mathematical sense.

For example:

**Student ID = 101, 102, 103**

The ID numbers are labels. Student 103 is not "more" of a student than student 101.

---


# 46. Points to Remember

1. Statistics is about learning from data.
2. Descriptive statistics summarizes observed data.
3. Inferential statistics uses sample data to learn about a population.
4. Population means the complete target group.
5. Sample means a subset of the population.
6. A parameter describes a population.
7. A statistic describes a sample.
8. Qualitative data represents categories.
9. Quantitative data represents quantities.
10. Discrete data is countable.
11. Continuous data is measurable over a range.
12. Nominal data has categories without order.
13. Ordinal data has order but not necessarily equal gaps.
14. Interval data has equal intervals but no true zero.
15. Ratio data has equal intervals and a true zero.
16. Sampling method affects the quality of inference.
17. Sampling error is expected random variation from using a sample.
18. Sampling bias is a systematic problem in how the sample is selected.
19. Do not confuse numeric labels with quantitative measurements.
20. Never remove an outlier automatically; investigate it first.

---

# 47. Recommended Learning Order After This Folder

```text
01 Statistics Fundamentals
        ↓
02 Descriptive Statistics
        ↓
03 Probability
        ↓
04 Probability Distributions
        ↓
05 Inferential Statistics
        ↓
06 Hypothesis Testing
        ↓
07 ANOVA
        ↓
08 Correlation & Regression
        ↓
09 ...
```

This order keeps the concepts connected instead of learning formulas without understanding the underlying terminology.

---

# 48. References & Further Reading

### GeeksforGeeks

- [Statistics: The Foundation of Data Science & Analytics](https://www.geeksforgeeks.org/data-science/statistics-the-foundation-of-data-science/)
- [Population vs Sample in Statistics](https://www.geeksforgeeks.org/maths/population-and-sample-statistics/)
- [Types of Statistical Data](https://www.geeksforgeeks.org/data-analysis/types-of-statistical-data/)
- [Data Types in Statistics](https://www.geeksforgeeks.org/maths/data-types-in-statistics/)
- [Methods of Sampling](https://www.geeksforgeeks.org/data-science/methods-of-sampling/)
- [Scales of Measurement in Business Statistics](https://www.geeksforgeeks.org/data-science/scales-of-measurement-in-business-statistics/)
- [Introduction to Statistics](https://www.geeksforgeeks.org/maths/introduction-to-statistics/)

### OpenStax

- [Introductory Statistics – Chapter 1](https://openstax.org/books/introductory-statistics-2e/pages/1-introduction)
- [Definitions of Statistics, Probability, and Key Terms](https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms)
- [Data, Sampling, and Variation](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)
- [Frequency, Frequency Tables, and Levels of Measurement](https://openstax.org/books/introductory-statistics-2e/pages/1-3-frequency-frequency-tables-and-levels-of-measurement)

### Other useful references

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [CASRAI – Levels of Measurement](https://www.casrai.org/guides/levels-of-measurement-nominal-ordinal-interval-ratio)

> **Image attribution:** The diagrams embedded in this README are linked from GeeksforGeeks pages. The images remain the property of their respective copyright holders. The source article is linked directly beside each image. Check the source site's terms/licensing before redistributing the images outside this personal learning repository.

---

## Next Folder

➡️ **02 Descriptive Statistics**

There we will move from terminology into actual statistical summaries and calculations such as:

- mean
- weighted mean
- median
- mode
- range
- variance
- standard deviation
- quartiles
- percentiles
- IQR
- skewness
- kurtosis
- frequency distributions
- histograms
- box plots
- and practical Python examples.
