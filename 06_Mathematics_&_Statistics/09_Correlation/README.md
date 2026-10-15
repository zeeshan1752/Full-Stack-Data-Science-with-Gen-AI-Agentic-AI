# Correlation

## Introduction

**Correlation** is a statistical method used to describe the strength and direction of association between two variables. It helps us understand whether two variables tend to change together.

For example, correlation can help us study the relationships between:

- Study hours and examination marks.
- Advertising expenditure and sales.
- Temperature and cold-drink sales.
- Height and weight.

Correlation is useful in Statistics, Data Science, Machine Learning, and exploratory data analysis. However, **correlation does not by itself establish causation**.

The main concepts covered in this chapter include covariance, Pearson correlation, Spearman rank correlation, correlation matrices, outliers, significance testing, confidence intervals, partial correlation, and practical Python implementation.

## 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain correlation and its importance.
2. Distinguish positive, negative, and near-zero correlation.
3. Understand paired observations and scatter plots.
4. Explain covariance and its relationship with correlation.
5. Calculate and interpret Pearson's correlation coefficient.
6. Understand the limitations of correlation.
7. Calculate Spearman's rank correlation coefficient.
8. Distinguish linear and monotonic relationships.
9. Construct and interpret a correlation matrix.
10. Understand outliers, confounding variables, and correlation versus causation.
11. Perform significance testing for Pearson correlation.
12. Understand confidence intervals and partial correlation.
13. Calculate correlation using Python, NumPy, pandas, and SciPy.

## 2. What Is Correlation?

Suppose two variables are represented by \(X\) and \(Y\). For each observation, we record a pair of values:

$$
(x_i,y_i)
$$

Correlation describes how these paired values vary together.

If larger values of \(X\) tend to occur with larger values of \(Y\), the relationship is positive.

If larger values of \(X\) tend to occur with smaller values of \(Y\), the relationship is negative.

If there is no clear linear pattern, Pearson correlation may be close to zero.

### Example

Suppose the following observations record study hours and examination marks.

| Student | Study Hours (\(X\)) | Marks (\(Y\)) |
|---|---:|---:|
| A | 1 | 42 |
| B | 2 | 48 |
| C | 3 | 55 |
| D | 4 | 63 |
| E | 5 | 70 |

As study hours increase, marks also tend to increase. This suggests a positive association.

## 3. Paired Data

Correlation requires **paired observations**. Each value of \(X\) must correspond to the correct value of \(Y\).

For \(n\) observations:

$$
(X,Y)=\{(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n)\}
$$

For example, temperature and cold-drink sales recorded on the same day form a pair.

| Day | Temperature (\(X\)) | Sales (\(Y\)) |
|---|---:|---:|
| 1 | 25 | 80 |
| 2 | 27 | 95 |
| 3 | 30 | 120 |
| 4 | 32 | 145 |
| 5 | 35 | 170 |

Incorrectly matching observations can produce a meaningless correlation. Always verify the pairing before calculating a coefficient.

## 4. Scatter Plot

A **scatter plot** represents each paired observation as a point on a graph.

The horizontal axis generally represents \(X\), and the vertical axis represents \(Y\).

A scatter plot helps us identify:

- Direction and strength of association.
- Linear and nonlinear patterns.
- Clusters and subgroups.
- Outliers and unusual observations.
- Whether Pearson correlation is appropriate.

A numerical coefficient should be interpreted alongside a scatter plot whenever possible.

## 5. Direction of Correlation

### 5.1 Positive Correlation

In positive correlation, both variables tend to increase together.

$$
X\uparrow\Rightarrow Y\uparrow
$$

The correlation coefficient is positive:

$$
r>0
$$

Examples include study hours and marks, or temperature and cold-drink sales.

### 5.2 Negative Correlation

In negative correlation, one variable tends to decrease as the other increases.

$$
X\uparrow\Rightarrow Y\downarrow
$$

The correlation coefficient is negative:

$$
r<0
$$

Examples include price and quantity demanded, or speed and travel time for a fixed distance under comparable conditions.

### 5.3 Zero or Near-Zero Linear Correlation

When there is little or no linear association:

$$
r\approx0
$$

However, a correlation near zero does not prove that the variables are unrelated. A strong nonlinear relationship may exist even when Pearson correlation is close to zero.

For example:

$$
Y=X^2
$$

This produces a U-shaped pattern. If the data are symmetric around zero, the positive and negative parts can cancel when measuring linear association.

## 6. Strength of Correlation

Pearson's correlation coefficient lies between \(-1\) and \(1\).

$$
-1\leq r\leq1
$$

- Values close to \(+1\) indicate strong positive linear association.
- Values close to \(-1\) indicate strong negative linear association.
- Values close to \(0\) indicate weak or no linear association.

A commonly used rough interpretation is:

| Absolute Correlation | Description |
|---|---|
| 0.00–0.19 | Very weak |
| 0.20–0.39 | Weak |
| 0.40–0.59 | Moderate |
| 0.60–0.79 | Strong |
| 0.80–1.00 | Very strong |

These are guidelines, not universal rules. The meaning of a correlation depends on the field, measurement quality, sample size, and purpose of the analysis.

### Perfect Correlation

Perfect positive correlation occurs when all points lie exactly on an increasing straight line.

$$
r=1
$$

Perfect negative correlation occurs when all points lie exactly on a decreasing straight line.

$$
r=-1
$$

Both represent perfect linear association in the observed data.

## 7. Correlation Coefficient

A correlation coefficient is a numerical measure of association.

The most widely used coefficient for linear association between two quantitative variables is **Pearson's correlation coefficient**.

For a sample, it is represented by \(r\). The corresponding population parameter is represented by \(\rho\).

$$
-1\leq r\leq1
$$

Where:

- \(r\) = sample correlation coefficient.
- \(\rho\) = population correlation coefficient.

The sample coefficient estimates the population correlation.

## 8. Covariance

Before understanding Pearson correlation, it is useful to understand **covariance**.

Covariance describes whether two variables tend to vary together.

The sample covariance is:

$$
s_{XY}=
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}
$$

Where:

- \(x_i\) = \(i\)th observation of \(X\).
- \(y_i\) = \(i\)th observation of \(Y\).
- \(\bar{x}\) = sample mean of \(X\).
- \(\bar{y}\) = sample mean of \(Y\).
- \(n\) = number of paired observations.
- \(s_{XY}\) = sample covariance.

### Understanding the Sign of Covariance

The product of deviations is:

$$
(x_i-\bar{x})(y_i-\bar{y})
$$

| Deviation of \(X\) | Deviation of \(Y\) | Product |
|---|---|---|
| Positive | Positive | Positive |
| Negative | Negative | Positive |
| Positive | Negative | Negative |
| Negative | Positive | Negative |

When both variables tend to be above or below their means together, covariance tends to be positive.

When one variable tends to be above its mean while the other is below, covariance tends to be negative.

### Worked Example: Covariance

Consider the following data.

| \(X\) | \(Y\) |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 8 |

Calculate the means:

$$
\bar{x}=\frac{1+2+3+4}{4}=2.5
$$

$$
\bar{y}=\frac{2+4+5+8}{4}=4.75
$$

Calculate the deviations and their products.

| \(X\) | \(Y\) | \(X-\bar{x}\) | \(Y-\bar{y}\) | Product |
|---:|---:|---:|---:|---:|
| 1 | 2 | -1.5 | -2.75 | 4.125 |
| 2 | 4 | -0.5 | -0.75 | 0.375 |
| 3 | 5 | 0.5 | 0.25 | 0.125 |
| 4 | 8 | 1.5 | 3.25 | 4.875 |

Sum the products:

$$
\sum(X-\bar{x})(Y-\bar{y})=9.5
$$

Divide by \(n-1\):

$$
s_{XY}=\frac{9.5}{4-1}
$$

$$
s_{XY}\approx3.167
$$

The positive covariance indicates that the two variables tend to increase together.

### Python Implementation

```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 5, 8])

covariance_matrix = np.cov(x, y)
sample_covariance = covariance_matrix[0, 1]

print("Sample covariance:", sample_covariance)
```

## 9. Why Covariance Alone Is Not Enough

Covariance has a limitation: its numerical magnitude depends on the units of measurement.

For example, measuring height in metres instead of centimetres changes the numerical covariance.

Correlation addresses this limitation by standardising covariance using the standard deviations of both variables.

## 10. Pearson Correlation Coefficient

Pearson's correlation coefficient measures the strength and direction of the **linear relationship** between two quantitative variables.

The sample formula is:

$$
r=
\frac{\sum(X-\bar{X})(Y-\bar{Y})}
{\sqrt{\sum(X-\bar{X})^2}\sqrt{\sum(Y-\bar{Y})^2}}
$$

An equivalent formula is:

$$
r=\frac{s_{XY}}{s_Xs_Y}
$$

Where \(s_X\) and \(s_Y\) are the sample standard deviations.

Because covariance is divided by the product of the standard deviations, correlation is unitless.

### Worked Example: Pearson Correlation

Using the previous dataset:

| \(X\) | \(Y\) |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 8 |

The means are:

$$
\bar{x}=2.5,\qquad\bar{y}=4.75
$$

The required sums are:

$$
\sum(X-\bar{x})(Y-\bar{y})=9.5
$$

$$
\sum(X-\bar{x})^2=5
$$

$$
\sum(Y-\bar{y})^2=18.75
$$

Substitute into the formula:

$$
r=\frac{9.5}{\sqrt{5}\sqrt{18.75}}
$$

$$
r=\frac{9.5}{\sqrt{93.75}}
$$

$$
r\approx0.981
$$

The data show a very strong positive linear association.

### Shortcut Formula

Pearson correlation can also be calculated from summary totals:

$$
r=
\frac{n\sum xy-(\sum x)(\sum y)}
{\sqrt{[n\sum x^2-(\sum x)^2][n\sum y^2-(\sum y)^2]}}
$$

This form is useful for manual calculations when the required sums are already available.

### Python Implementation

```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 5, 8])

r = np.corrcoef(x, y)[0, 1]

print("Pearson correlation:", r)
```

## 11. Interpretation of Pearson's \(r\)

Suppose:

$$
r=0.85
$$

This indicates a strong positive linear association.

It does not mean that:

- \(Y\) increases by exactly 0.85 units when \(X\) increases by one unit.
- 85% of observations follow a particular pattern.
- \(X\) causes \(Y\).
- The relationship is necessarily perfect.

Similarly:

$$
r=-0.72
$$

indicates a strong negative linear association.

Always report both the direction and magnitude of the coefficient.

## 12. Standardised Interpretation of Correlation

A z-score expresses an observation in standard-deviation units.

For \(X\):

$$
z_x=\frac{x-\bar{x}}{s_X}
$$

For \(Y\):

$$
z_y=\frac{y-\bar{y}}{s_Y}
$$

Sample correlation can be expressed as:

$$
r=\frac{1}{n-1}\sum_{i=1}^{n}z_{x_i}z_{y_i}
$$

This demonstrates that correlation measures how the standardised deviations of two variables move together.

## 13. Geometric Interpretation

Consider the centred vectors:

$$
\mathbf{x}_c=(x_1-\bar{x},\ldots,x_n-\bar{x})
$$

$$
\mathbf{y}_c=(y_1-\bar{y},\ldots,y_n-\bar{y})
$$

Pearson correlation is related to the cosine of the angle \(\theta\) between these vectors:

$$
r=\cos(\theta)
$$

Therefore:

- If \(\theta=0^\circ\), then \(r=1\).
- If \(\theta=90^\circ\), then \(r=0\).
- If \(\theta=180^\circ\), then \(r=-1\).

This gives a geometric interpretation of perfect positive, zero, and perfect negative linear correlation.

## 14. Properties of Pearson Correlation

### Bounded

$$
-1\leq r\leq1
$$

### Unitless

Correlation has no physical unit.

### Symmetric

$$
r_{XY}=r_{YX}
$$

The correlation between \(X\) and \(Y\) is the same as the correlation between \(Y\) and \(X\).

### Measures Linear Association

Pearson correlation measures linear association, not every possible type of relationship.

### Sensitive to Outliers

Extreme observations can substantially change the coefficient.

### Invariant to Positive Linear Changes of Scale and Location

Suppose:

$$
X'=a+bX
$$

$$
Y'=c+dY
$$

When \(b>0\) and \(d>0\):

$$
r_{X'Y'}=r_{XY}
$$

If one variable is multiplied by a negative number, the correlation direction reverses. For example:

$$
r_{X,-Y}=-r_{XY}
$$

## 15. Correlation Is Not Causation

One of the most important principles in Statistics is:

**Correlation does not imply causation.**

Suppose ice-cream sales and swimming activity are positively correlated. This does not prove that buying ice cream causes people to swim.

A third variable, such as temperature, may influence both:

Temperature → Ice-cream sales

Temperature → Swimming activity

Temperature is a possible **confounding variable**.

Correlation identifies association. Establishing causation requires an appropriate study design and additional assumptions or analysis.

## 16. Correlation Does Not Mean Perfect Prediction

Suppose:

$$
r=0.80
$$

This indicates a strong positive linear association, but individual observations may still vary considerably around the overall trend.

Correlation is not itself a complete predictive model.

### Coefficient of Determination

The square of Pearson correlation is:

$$
R^2=r^2
$$

For example, if:

$$
r=0.80
$$

then:

$$
R^2=(0.80)^2=0.64
$$

In simple linear regression with an intercept, \(R^2=0.64\) means that 64% of the observed sample variation in \(Y\) is accounted for by the fitted linear model.

It does not mean that 64% of \(Y\) is caused by \(X\).

## 17. Outliers and Correlation

An **outlier** is an observation that is unusually far from the rest of the data.

Pearson correlation depends on deviations from the means, so an extreme observation can strongly influence its value.

Before removing an outlier:

1. Visualise the data.
2. Investigate unusual observations.
3. Check for data-entry or measurement errors.
4. Determine whether the observation is valid.
5. Compare results with and without the observation when scientifically appropriate.

An outlier may represent an error, a valid rare observation, or a different subgroup. It should not automatically be deleted.

## 18. Nonlinear Relationships

Pearson correlation may fail to describe a strong nonlinear relationship.

For example:

$$
Y=X^2
$$

produces a U-shaped pattern. If the data are symmetric around zero, Pearson correlation can be close to zero even though the variables have a clear relationship.

Therefore:

**A correlation near zero does not prove that two variables are unrelated.** It indicates little or no linear association.

| Scatter-Plot Pattern | Typical Pearson \(r\) |
|---|---:|
| Strong upward straight-line pattern | Close to \(+1\) |
| Moderate upward trend | Positive |
| No clear linear trend | Close to \(0\) |
| Moderate downward trend | Negative |
| Strong downward straight-line pattern | Close to \(-1\) |
| Strong curved pattern | May be close to \(0\) |

## 19. Spearman Rank Correlation

**Spearman's rank correlation** measures the strength and direction of a monotonic relationship.

It is represented by:

$$
\rho_s
$$

A monotonic relationship means that the variables generally move in one direction together, although the rate of change need not be constant.

Spearman correlation is useful for ordinal data, ranked observations, and relationships that are monotonic but not necessarily linear.

### Pearson vs Spearman

| Feature | Pearson | Spearman |
|---|---|---|
| Main purpose | Linear association | Monotonic association |
| Data used | Original values | Ranks |
| Appropriate for ordinal data | Not generally the first choice | Yes |
| Sensitivity to outliers | Often more sensitive | Often less sensitive, but not immune |
| Requires a straight-line relationship | Measures linear association | No |
| Symbol | \(r\) | \(\rho_s\) |

The choice should depend on the data and research question, not on which coefficient produces the larger result.

## 20. Spearman Correlation Without Tied Ranks

When there are no tied ranks, Spearman correlation can be calculated using:

$$
\rho_s=1-\frac{6\sum d_i^2}{n(n^2-1)}
$$

Where:

- \(d_i\) = difference between the ranks of \(X_i\) and \(Y_i\).
- \(n\) = number of paired observations.

### Worked Example

Suppose five students have the following examination ranks.

| Student | Rank in Exam 1 | Rank in Exam 2 |
|---|---:|---:|
| A | 1 | 2 |
| B | 2 | 1 |
| C | 3 | 3 |
| D | 4 | 5 |
| E | 5 | 4 |

Calculate the rank differences:

$$
d_i=R_{Xi}-R_{Yi}
$$

| Student | \(R_X\) | \(R_Y\) | \(d\) | \(d^2\) |
|---|---:|---:|---:|---:|
| A | 1 | 2 | -1 | 1 |
| B | 2 | 1 | 1 | 1 |
| C | 3 | 3 | 0 | 0 |
| D | 4 | 5 | -1 | 1 |
| E | 5 | 4 | 1 | 1 |

Therefore:

$$
\sum d_i^2=4,\qquad n=5
$$

Substitute into the formula:

$$
\rho_s=1-\frac{6(4)}{5(5^2-1)}
$$

$$
\rho_s=1-\frac{24}{120}
$$

$$
\rho_s=0.80
$$

The ranks show a strong positive monotonic association.

### Spearman Correlation With Ties

When equal values occur, assign **average ranks**.

For example, if two observations occupy ranks 2 and 3 but have equal values, each receives:

$$
\frac{2+3}{2}=2.5
$$

The simple \(d_i^2\) formula assumes there are no tied ranks. In practice, software calculates Spearman correlation by ranking the observations and computing Pearson correlation on the resulting ranks.

$$
\rho_s = \mathrm{Corr}(\mathrm{rank}(X), \mathrm{rank}(Y))
$$

### Python Implementation

```python
from scipy.stats import spearmanr

x = [1, 2, 3, 4, 5]
y = [2, 1, 3, 5, 4]

rho, p_value = spearmanr(x, y)

print("Spearman correlation:", rho)
print("P-value:", p_value)
```

## 21. Monotonic vs Linear Relationships

A linear relationship follows an approximately straight-line pattern.

A monotonic relationship means that one variable generally increases or decreases as the other changes, but the rate of change can vary.

For example:

$$
Y=\log(X)
$$

is nonlinear but increasing for positive \(X\).

Spearman correlation can describe the monotonic direction even when the relationship is not a straight line.

## 22. Covariance vs Correlation

| Feature | Covariance | Correlation |
|---|---|---|
| Indicates direction | Yes | Yes |
| Standardised measure of strength | No | Yes |
| Unitless | No | Yes |
| Range | Unbounded | \([-1,1]\) |
| Depends on measurement units | Yes | No, under positive linear changes of scale |

The relationship is:

$$
r=\frac{s_{XY}}{s_Xs_Y}
$$

Correlation can therefore be understood as **standardised covariance**.

## 23. Correlation Matrix

When more than two variables are available, a **correlation matrix** summarises their pairwise correlations.

Suppose a dataset contains study hours, attendance, and marks.

| | Study Hours | Attendance | Marks |
|---|---:|---:|---:|
| Study Hours | 1.00 | 0.45 | 0.78 |
| Attendance | 0.45 | 1.00 | 0.62 |
| Marks | 0.78 | 0.62 | 1.00 |

The diagonal values are always 1 because each variable has perfect correlation with itself.

$$
r_{XX}=1
$$

The matrix is symmetric:

$$
r_{XY}=r_{YX}
$$

For example, a correlation of 0.78 between study hours and marks indicates a strong positive linear association.

Pairwise correlations do not automatically reveal causal relationships.

### Python Implementation

```python
import pandas as pd

df = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7],
    "attendance": [60, 65, 70, 75, 85, 90],
    "marks": [45, 50, 54, 61, 65, 70]
})

correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)
```

## 24. Correlation Heatmap

A correlation heatmap visualises the correlation matrix using colours. It can make strong positive and negative relationships easier to identify.

### Python Implementation

```python
import matplotlib.pyplot as plt

correlation_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(7, 5))

image = plt.imshow(
    correlation_matrix,
    vmin=-1,
    vmax=1,
    aspect="auto"
)

plt.colorbar(image, label="Correlation")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation_matrix.index)),
    correlation_matrix.index
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
```

A heatmap helps identify variable pairs that move together, but it does not establish causation.

## 25. Partial Correlation

A **partial correlation** measures the association between two variables after statistically controlling for another variable.

For three variables \(X\), \(Y\), and \(Z\):

$$
r_{XY\cdot Z}=
\frac{r_{XY}-r_{XZ}r_{YZ}}
{\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}}
$$

Where:

- \(r_{XY}\) = correlation between \(X\) and \(Y\).
- \(r_{XZ}\) = correlation between \(X\) and \(Z\).
- \(r_{YZ}\) = correlation between \(Y\) and \(Z\).

Partial correlation helps examine whether an association remains after accounting for a third variable. It does not, by itself, prove causation.

## 26. Testing the Significance of Pearson Correlation

A sample correlation may differ from zero due to sampling variability. A significance test can assess whether the data provide evidence that the population correlation differs from zero.

For a two-sided test:

$$
H_0:\rho=0
$$

$$
H_1:\rho\neq0
$$

Under the standard assumptions for the classical Pearson correlation test, the test statistic is:

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
$$

The degrees of freedom are:

$$
df=n-2
$$

### Worked Example

Suppose:

$$
r=0.70,\qquad n=20
$$

The hypotheses are:

$$
H_0:\rho=0
$$

$$
H_1:\rho\neq0
$$

Calculate the test statistic:

$$
t=\frac{0.70\sqrt{20-2}}{\sqrt{1-0.70^2}}
$$

$$
t=\frac{0.70\sqrt{18}}{\sqrt{0.51}}
$$

$$
t\approx4.16
$$

Degrees of freedom:

$$
df=20-2=18
$$

The p-value can then be obtained from the \(t\)-distribution.

### Python Implementation

```python
from scipy.stats import pearsonr

x = [1, 2, 3, 4, 5, 6]
y = [2, 3, 5, 4, 6, 8]

r, p_value = pearsonr(x, y)

print("Pearson correlation:", r)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
```

The p-value tests the null hypothesis; the correlation coefficient describes the observed association.

## 27. Statistical Significance vs Practical Importance

A statistically significant correlation may still be small in practical terms.

With a very large sample, even a modest correlation can produce a small p-value.

Distinguish three concepts:

- **Statistical significance:** Evidence that the population correlation differs from the null value.
- **Strength of association:** The magnitude of the correlation.
- **Practical importance:** Whether the relationship matters in the real-world context.

The p-value and the coefficient answer different questions.

## 28. Confidence Interval for Correlation

A confidence interval describes uncertainty around an estimated population correlation.

A commonly used approximate method is **Fisher's z transformation**:

$$
z'=\frac{1}{2}\ln\left(\frac{1+r}{1-r}\right)
$$

Its approximate standard error is:

$$
SE_{z'}=\frac{1}{\sqrt{n-3}}
$$

For a confidence level associated with critical value \(z_{\alpha/2}\), the interval on the transformed scale is:

$$
z'\pm z_{\alpha/2}SE_{z'}
$$

Transform the lower and upper limits back to the correlation scale using:

$$
r=\frac{e^{2z'}-1}{e^{2z'}+1}
$$

This is an approximate procedure and is most appropriate under the assumptions of the method. Special handling is needed for correlations exactly equal to \(-1\) or \(1\).

## 29. Assumptions for Pearson Correlation

### Quantitative Variables

The variables should generally be quantitative, with meaningful numerical differences.

### Paired Observations

Each observation of \(X\) must correspond to the correct observation of \(Y\).

### Independence

Observations should generally be independent for standard inferential procedures.

### Approximately Linear Relationship

Pearson correlation measures linear association. A scatter plot should be checked for curvature or other patterns.

### Outliers

Extreme observations can strongly influence the coefficient.

### Distributional Conditions

Classical significance tests and confidence procedures may require stronger distributional assumptions, particularly for small samples.

## 30. Independence vs Zero Correlation

It is important to distinguish **uncorrelated** from **independent**.

If two variables are independent and have finite variances, their covariance is zero and their Pearson correlation is zero when both variances are positive.

However, the reverse is not generally true.

$$
\text{Independence}\Rightarrow\text{Zero Correlation}
$$

under the stated conditions, but:

$$
\text{Zero Correlation}\nRightarrow\text{Independence}
$$

A nonlinear relationship may exist even when Pearson correlation is zero.

## 31. Restriction of Range

Correlation can be affected when the observed data cover only a narrow range of one variable.

For example, if a study includes only students whose aptitude scores fall within a very narrow interval, the observed correlation between aptitude and academic performance may differ from the correlation in a broader student population.

This is called **restriction of range**.

The sample's range and selection process should therefore be considered when interpreting a correlation.

## 32. Aggregated Data

Correlation calculated from group averages can differ substantially from correlation calculated from individual observations.

For example, a relationship between average income and average education across cities does not automatically describe the relationship between income and education for individuals.

Always consider the level at which the data were collected.

## 33. Correlation and Data Quality

Real datasets may contain missing values, duplicates, or measurement errors.

### Missing Values

Before calculating correlation, decide how missing observations should be handled. In a correlation matrix, different variable pairs may use different numbers of observations.

```python
correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)
```

Check the effective sample size when interpreting correlations, especially when missingness is substantial.

### Duplicate Observations

Duplicate records can give particular observations extra weight and change the correlation.

### Measurement Error

Measurement error can weaken an observed association. A genuinely related pair of variables may appear less strongly correlated when measurements contain substantial noise.

Data cleaning and validation should precede the final analysis.

## 34. Common Mistakes in Correlation

### Mistake 1: Claiming that correlation proves causation

Incorrect: “Study hours cause higher marks because \(r=0.80\).”

Better: “Study hours and marks show a strong positive linear association.”

### Mistake 2: Ignoring the sign

A value of \(r=-0.85\) indicates a strong negative association, not a positive one.

### Mistake 3: Treating \(r=0\) as proof of no relationship

A nonlinear relationship may still exist.

### Mistake 4: Ignoring outliers

One unusual observation can substantially change Pearson correlation.

### Mistake 5: Calculating correlation without visualising the data

A coefficient can hide curvature, clusters, or outliers.

### Mistake 6: Confusing correlation with slope

Correlation describes strength and direction. Regression slope describes the expected change in the fitted response for a one-unit change in the predictor.

### Mistake 7: Automatically choosing Pearson

The appropriate coefficient depends on variable types, data patterns, and the research question.

### Mistake 8: Reporting statistical significance without context

Include the coefficient, sample size, and an appropriate interpretation. Report uncertainty when relevant.

## 35. Correlation Does Not Give the Regression Slope

Suppose:

$$
r=0.80
$$

This describes a strong positive linear association. It does not tell us how many units \(Y\) changes when \(X\) increases by one unit.

The regression equation is:

$$
\hat{Y}=a+bX
$$

Where:

- \(a\) = intercept.
- \(b\) = regression slope.

Correlation and regression are related but answer different questions.

## 36. Complete Correlation Analysis

A good correlation analysis follows these steps.

1. **Identify the variables.** Determine which two variables are being compared.
2. **Verify pairing.** Ensure that each \(X\) observation matches the correct \(Y\) observation.
3. **Visualise the data.** Create a scatter plot.
4. **Examine the pattern.** Check linearity, direction, clusters, and outliers.
5. **Select the coefficient.** Use Pearson for linear association and Spearman for appropriate rank or monotonic relationships.
6. **Calculate the coefficient.** Compute \(r\) or \(\rho_s\).
7. **Assess uncertainty.** Use a p-value or confidence interval when inferential analysis is required.
8. **Interpret the result.** State the direction and strength in context.
9. **Avoid causal claims.** Do not interpret association as causation without a suitable causal design and analysis.

## 37. Complete Worked Example: Study Hours and Marks

Suppose the following data record weekly study hours and examination marks.

| Student | Study Hours (\(X\)) | Marks (\(Y\)) |
|---|---:|---:|
| 1 | 2 | 45 |
| 2 | 3 | 50 |
| 3 | 4 | 54 |
| 4 | 5 | 61 |
| 5 | 6 | 65 |
| 6 | 7 | 70 |

### Step 1: Calculate the Means

$$
\bar{x}=\frac{2+3+4+5+6+7}{6}=4.5
$$

$$
\bar{y}=\frac{45+50+54+61+65+70}{6}=57.5
$$

### Step 2: Calculate Deviations

| \(X\) | \(Y\) | \(X-\bar{x}\) | \(Y-\bar{y}\) |
|---:|---:|---:|---:|
| 2 | 45 | -2.5 | -12.5 |
| 3 | 50 | -1.5 | -7.5 |
| 4 | 54 | -0.5 | -3.5 |
| 5 | 61 | 0.5 | 3.5 |
| 6 | 65 | 1.5 | 7.5 |
| 7 | 70 | 2.5 | 12.5 |

### Step 3: Calculate the Cross-Products

$$
\sum(X-\bar{x})(Y-\bar{y})=88.5
$$

### Step 4: Calculate Squared Deviations

$$
\sum(X-\bar{x})^2=17.5
$$

$$
\sum(Y-\bar{y})^2=445.5
$$

### Step 5: Calculate Pearson Correlation

$$
r=\frac{88.5}{\sqrt{17.5}\sqrt{445.5}}
$$

$$
r\approx0.999
$$

The data show an extremely strong positive linear association between study hours and marks. This does not establish that study hours cause higher marks.

### Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

study_hours = np.array([2, 3, 4, 5, 6, 7])
marks = np.array([45, 50, 54, 61, 65, 70])

pearson_r, pearson_p = pearsonr(study_hours, marks)
spearman_rho, spearman_p = spearmanr(study_hours, marks)

print("Pearson correlation:", pearson_r)
print("Pearson p-value:", pearson_p)

print("Spearman correlation:", spearman_rho)
print("Spearman p-value:", spearman_p)

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.show()
```

## 38. Correlation Using pandas

For a DataFrame, pandas can calculate the correlation between two columns or construct a complete correlation matrix.

```python
import pandas as pd

df = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7],
    "marks": [45, 50, 54, 61, 65, 70]
})

print("Pearson correlation:")
print(df["study_hours"].corr(df["marks"]))

print("\nCorrelation matrix:")
print(df.corr(numeric_only=True))

print("\nSpearman correlation:")
print(
    df["study_hours"].corr(
        df["marks"],
        method="spearman"
    )
)
```

The default correlation method in pandas is Pearson. Spearman can be selected with `method="spearman"`.

## 39. Visualising Correlation

A scatter plot helps verify whether the numerical coefficient represents the observed data pattern.

```python
import matplotlib.pyplot as plt

plt.scatter(df["study_hours"], df["marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.tight_layout()
plt.show()
```

Inspect the graph for outliers, clusters, and nonlinear patterns before interpreting the coefficient.

## 40. Formula Summary

### Sample Covariance

$$
s_{XY}=\frac{\sum(X-\bar{X})(Y-\bar{Y})}{n-1}
$$

### Pearson Correlation

$$
r=
\frac{\sum(X-\bar{X})(Y-\bar{Y})}
{\sqrt{\sum(X-\bar{X})^2\sum(Y-\bar{Y})^2}}
$$

### Pearson Correlation Using Covariance

$$
r=\frac{s_{XY}}{s_Xs_Y}
$$

### Shortcut Pearson Formula

$$
r=
\frac{n\sum xy-(\sum x)(\sum y)}
{\sqrt{[n\sum x^2-(\sum x)^2][n\sum y^2-(\sum y)^2]}}
$$

### Range of Correlation

$$
-1\leq r\leq1
$$

### Coefficient of Determination

$$
R^2=r^2
$$

### Spearman Correlation Without Ties

$$
\rho_s=1-\frac{6\sum d_i^2}{n(n^2-1)}
$$

### Pearson Correlation Test Statistic

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
$$

$$
df=n-2
$$

### Fisher's z Transformation

$$
z'=\frac{1}{2}\ln\left(\frac{1+r}{1-r}\right)
$$

### Standard Error on Fisher's z Scale

$$
SE_{z'}=\frac{1}{\sqrt{n-3}}
$$

### Partial Correlation

$$
r_{XY\cdot Z}=
\frac{r_{XY}-r_{XZ}r_{YZ}}
{\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}}
$$

## 41. Quick Concept Comparison

| Concept | Main Purpose |
|---|---|
| Covariance | Describes the direction of joint variation |
| Pearson correlation | Measures the strength and direction of linear association |
| Spearman correlation | Measures the strength and direction of monotonic rank association |
| Scatter plot | Visualises the relationship between paired variables |
| Correlation matrix | Summarises pairwise correlations |
| Partial correlation | Measures association after controlling for another variable |
| \(R^2\) | In simple linear regression, describes the proportion of sample variation accounted for by the fitted linear model |

## 42. Points to Remember

1. Correlation measures association between variables.
2. Pearson correlation measures linear association.
3. Pearson correlation lies between \(-1\) and \(1\).
4. Positive correlation means the variables tend to increase together.
5. Negative correlation means one variable tends to decrease as the other increases.
6. A correlation near zero does not rule out a nonlinear relationship.
7. Covariance depends on measurement units; correlation is unitless.
8. Correlation is symmetric: \(r_{XY}=r_{YX}\).
9. Pearson correlation is sensitive to outliers.
10. A scatter plot should normally accompany correlation analysis.
11. Spearman correlation uses ranks and is useful for monotonic relationships.
12. Correlation does not prove causation.
13. Statistical significance and practical importance are different.
14. A correlation matrix is symmetric with ones on the diagonal.
15. The sample correlation \(r\) estimates the population correlation \(\rho\).
16. Choose the coefficient according to the data and research question.

## 43. Chapter Summary

Correlation provides a numerical description of how two variables move together.

Covariance describes the direction of joint variation. Pearson correlation standardises covariance to measure the strength and direction of linear association:

$$
r=\frac{s_{XY}}{s_Xs_Y}
$$

Pearson correlation lies between \(-1\) and \(1\). Its sign indicates direction, and its magnitude describes the strength of linear association.

Scatter plots are essential because curvature, clusters, and outliers can make a coefficient misleading when viewed alone. Spearman rank correlation is useful when ranks or monotonic relationships are more appropriate.

Correlation also connects with covariance, standardisation, hypothesis testing, confidence intervals, and regression. Nevertheless, correlation is not causation.

A sound correlation analysis combines:

**Correct Pairing + Visualisation + Appropriate Coefficient + Careful Interpretation**

## 44. References and Further Reading

- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [Penn State — Statistics Online](https://online.stat.psu.edu/)
- [NIST/SEMATECH — e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [SciPy — Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [SciPy — `pearsonr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)
- [SciPy — `spearmanr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)
- [pandas — Correlation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [NumPy — `corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
- GeeksforGeeks — Educational articles on correlation and covariance.

## Related Topics

- Statistics Fundamentals
- Descriptive Statistics
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- ANOVA
- Chi-Square Test
- Regression
- Regression Model Evaluation
- Statistics for Machine Learning

**Repository location:** `09_Correlation/README.md`
