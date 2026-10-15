# Chi-Square Test

## Introduction

The **Chi-Square Test ($\chi^2$ test)** is a statistical method used primarily to analyse categorical data. It compares observed frequencies with expected frequencies to determine whether the differences are consistent with a specified statistical model.

Categorical data represent groups or categories rather than continuous numerical measurements. Examples include payment methods, product preferences, pass/fail status, education levels, and customer satisfaction categories.

The three main applications of chi-square tests are:

1. **Chi-Square Goodness-of-Fit Test:** Determines whether observed frequencies agree with a specified distribution.
2. **Chi-Square Test of Independence:** Determines whether two categorical variables are associated.
3. **Chi-Square Test of Homogeneity:** Determines whether different populations or groups have the same categorical distribution.

The general formula is:

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

Where:

- $O$ = observed frequency.
- $E$ = expected frequency.
- $\sum$ = sum across all categories or cells.

A large chi-square statistic indicates a greater discrepancy between observed and expected frequencies.

## 1. Categorical Data and Frequencies

Categorical data classify observations into distinct groups.

For example, suppose 100 customers report their preferred payment method.

| Payment Method | Frequency |
|---|---:|
| Cash | 25 |
| Card | 45 |
| UPI | 30 |
| Total | 100 |

The frequency indicates how many observations belong to a category.

The total sample size is:

$$
N=25+45+30=100
$$

Chi-square tests generally use frequency counts rather than percentages alone.

## 2. Observed and Expected Frequencies

### Observed Frequency

The **observed frequency**, represented by $O$, is the actual number of observations recorded in a category.

For example, if 45 customers prefer card payments:

$$
O=45
$$

Observed frequencies are obtained from collected data.

### Expected Frequency

The **expected frequency**, represented by $E$, is the frequency predicted under the null hypothesis.

For example:

$$
E=25.5
$$

An expected frequency can be a decimal because it represents a theoretical expected count, not necessarily an actual count.

The chi-square statistic measures the difference between observed and expected frequencies relative to the expected frequency.

## 3. Understanding the Chi-Square Formula

The formula is:

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

The calculation involves four steps:

1. Subtract the expected frequency from the observed frequency.
2. Square the difference.
3. Divide the squared difference by the expected frequency.
4. Add the contributions from all categories or cells.

### Worked Example

Suppose:

$$
O=30,\qquad E=25
$$

Calculate the difference:

$$
O-E=30-25=5
$$

Square the difference:

$$
(O-E)^2=5^2=25
$$

Divide by the expected frequency:

$$
\frac{25}{25}=1
$$

Therefore, this category contributes $1$ to the total chi-square statistic.

### Why Is the Difference Squared?

The difference $O-E$ can be positive or negative. Squaring prevents positive and negative differences from cancelling each other.

$$
(O-E)^2\geq0
$$

Consequently:

$$
\chi^2\geq0
$$

A chi-square statistic of zero occurs when every observed frequency equals its corresponding expected frequency.

## 4. Hypothesis Testing in Chi-Square Analysis

Every chi-square test involves a null hypothesis and an alternative hypothesis. Their exact meanings depend on the type of test.

### Null Hypothesis ($H_0$)

The **null hypothesis** describes the assumed situation under which expected frequencies are calculated.

Examples include:

- Goodness-of-fit: The population follows the specified categorical distribution.
- Independence: The two categorical variables are independent.
- Homogeneity: The categorical distribution is the same across the populations or groups.

### Alternative Hypothesis ($H_a$)

The **alternative hypothesis** describes a departure from the null hypothesis.

Examples include:

- Goodness-of-fit: The population distribution differs from the specified distribution.
- Independence: The two categorical variables are associated.
- Homogeneity: At least one population or group has a different categorical distribution.

### General Decision Rule

Choose a significance level, commonly:

$$
\alpha=0.05
$$

After calculating the chi-square statistic and its degrees of freedom, obtain the p-value.

- If $p<\alpha$, reject $H_0$.
- If $p\geq\alpha$, fail to reject $H_0$.

Failing to reject the null hypothesis does not prove that it is true.

## 5. Types of Chi-Square Tests

| Test | Research Question |
|---|---|
| Goodness-of-fit | Does one categorical variable follow a specified distribution? |
| Independence | Are two categorical variables associated? |
| Homogeneity | Do different populations have the same categorical distribution? |

Although the calculations for independence and homogeneity are closely related, the research questions and sampling designs differ.

## 6. Chi-Square Goodness-of-Fit Test

The **goodness-of-fit test** determines whether observed frequencies are consistent with a specified theoretical distribution.

Suppose a company expects its customers to choose products according to the following proportions:

| Product | Expected Proportion |
|---|---:|
| A | 0.50 |
| B | 0.30 |
| C | 0.20 |

A sample can be analysed to determine whether the observed product choices are consistent with these proportions.

### Hypotheses

The null hypothesis states that the population category proportions follow the specified distribution.

$$
H_0:\text{The specified distribution is correct}
$$

The alternative hypothesis states that the population distribution differs from the specified distribution.

$$
H_a:\text{The population distribution differs}
$$

More formally, if the specified proportions are $p_1,p_2,\ldots,p_k$, the null hypothesis specifies those category probabilities, while the alternative states that at least one probability differs.

### Expected Frequency Formula

For category $i$:

$$
E_i=Np_i
$$

Where:

- $E_i$ = expected frequency for category $i$.
- $N$ = total sample size.
- $p_i$ = specified probability for category $i$.

### Worked Example: Expected Frequencies

Suppose the sample contains 200 customers.

$$
N=200
$$

For Product A:

$$
E_A=200(0.50)=100
$$

For Product B:

$$
E_B=200(0.30)=60
$$

For Product C:

$$
E_C=200(0.20)=40
$$

The expected frequencies are:

| Product | Expected Proportion | Expected Frequency |
|---|---:|---:|
| A | 0.50 | 100 |
| B | 0.30 | 60 |
| C | 0.20 | 40 |
| Total | 1.00 | 200 |

The expected frequencies must add up to the sample size.

### Python Implementation

```python
import numpy as np

sample_size = 200
expected_proportions = np.array([0.50, 0.30, 0.20])

expected_frequencies = sample_size * expected_proportions

print("Expected frequencies:", expected_frequencies)
print("Total:", expected_frequencies.sum())
```

### Complete Goodness-of-Fit Example

Suppose the observed frequencies are:

| Product | Observed Frequency | Expected Frequency |
|---|---:|---:|
| A | 90 | 100 |
| B | 70 | 60 |
| C | 40 | 40 |
| Total | 200 | 200 |

Calculate the contribution for Product A:

$$
\frac{(90-100)^2}{100}=1
$$

For Product B:

$$
\frac{(70-60)^2}{60}\approx1.6667
$$

For Product C:

$$
\frac{(40-40)^2}{40}=0
$$

Therefore:

$$
\chi^2=1+1.6667+0
$$

$$
\chi^2\approx2.667
$$

### Degrees of Freedom

When the expected proportions are specified in advance and no parameters are estimated from the sample:

$$
df=k-1
$$

Where $k$ is the number of categories.

For three categories:

$$
df=3-1=2
$$

If $m$ independent parameters are estimated from the data to determine the expected probabilities, the degrees of freedom are generally adjusted to:

$$
df=k-1-m
$$

### Python Implementation and Decision

```python
from scipy.stats import chisquare

observed = [90, 70, 40]
expected = [100, 60, 40]

chi2_stat, p_value = chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Chi-square statistic:", chi2_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
```

The statistic is approximately $2.667$, and the p-value is approximately $0.264$.

Because:

$$
0.264>0.05
$$

we fail to reject the null hypothesis. There is insufficient evidence that the observed distribution differs from the specified distribution.

## 7. Chi-Square Test of Independence

The **chi-square test of independence** determines whether two categorical variables are associated in a population.

Examples include:

- Customer type and payment preference.
- Education category and employment category.
- Product preference and customer segment.
- Study method and pass/fail status.

The data are organised in a contingency table.

### Hypotheses

The null hypothesis states that the variables are independent.

$$
H_0:\text{The variables are independent}
$$

The alternative hypothesis states that the variables are associated.

$$
H_a:\text{The variables are associated}
$$

Independence means that knowing the category of one variable does not provide information about the category of the other variable under the population model.

### Contingency Table

Suppose 200 customers are classified by customer type and preferred payment method.

| Customer Type | Cash | Card | UPI | Total |
|---|---:|---:|---:|---:|
| New | 20 | 30 | 50 | 100 |
| Returning | 30 | 40 | 30 | 100 |
| Total | 50 | 70 | 80 | 200 |

Rows represent customer type, columns represent payment method, and the cells contain observed frequencies.

### Expected Frequency Formula

For cell $(i,j)$:

$$
E_{ij}=\frac{R_iC_j}{N}
$$

Where:

- $R_i$ = total for row $i$.
- $C_j$ = total for column $j$.
- $N$ = grand total.
- $E_{ij}$ = expected frequency for the cell.

### Worked Example: Expected Cell Frequency

For new customers who prefer cash:

$$
R_i=100,\qquad C_j=50,\qquad N=200
$$

Therefore:

$$
E=\frac{100(50)}{200}=25
$$

The observed frequency is 20, which is lower than the expected frequency of 25 under independence.

### Complete Expected Frequency Table

| Customer Type | Cash | Card | UPI |
|---|---:|---:|---:|
| New | 25 | 35 | 40 |
| Returning | 25 | 35 | 40 |

For new customers:

$$
E_{\text{Cash}}=\frac{100(50)}{200}=25
$$

$$
E_{\text{Card}}=\frac{100(70)}{200}=35
$$

$$
E_{\text{UPI}}=\frac{100(80)}{200}=40
$$

The returning-customer expected frequencies are the same because their row total is also 100.

### Chi-Square Calculation

For the six cells, the contributions are:

$$
\frac{(20-25)^2}{25}=1
$$

$$
\frac{(30-35)^2}{35}\approx0.7143
$$

$$
\frac{(50-40)^2}{40}=2.5
$$

$$
\frac{(30-25)^2}{25}=1
$$

$$
\frac{(40-35)^2}{35}\approx0.7143
$$

$$
\frac{(30-40)^2}{40}=2.5
$$

Adding the contributions:

$$
\chi^2\approx8.4286
$$

### Degrees of Freedom

For a contingency table:

$$
df=(r-1)(c-1)
$$

Where $r$ is the number of rows and $c$ is the number of columns, excluding the totals.

For a table with two rows and three columns:

$$
df=(2-1)(3-1)=2
$$

### Python Implementation

```python
import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [20, 30, 50],
    [30, 40, 30]
])

chi2_stat, p_value, df, expected = chi2_contingency(
    observed,
    correction=False
)

print("Chi-square statistic:", chi2_stat)
print("Degrees of freedom:", df)
print("P-value:", p_value)

print("\nExpected frequencies:")
print(expected)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("Evidence of an association exists.")
else:
    print("Fail to reject the null hypothesis.")
```

The chi-square statistic is approximately $8.43$, with $df=2$ and $p\approx0.0148$.

Because the p-value is below 0.05, we reject the null hypothesis. There is evidence of an association between customer type and preferred payment method.

**Important:** Association does not establish causation.

## 8. Chi-Square Test of Homogeneity

The **chi-square test of homogeneity** determines whether different populations or groups share the same distribution of a categorical variable.

For example, a researcher may compare transport preferences across three cities:

- Bus.
- Car.
- Metro.

The objective is to determine whether the distribution of transport preferences is the same across the cities.

### Hypotheses

The null hypothesis states that the categorical distribution is the same across all groups.

$$
H_0:\text{All groups have the same distribution}
$$

The alternative hypothesis states that at least one group has a different distribution.

$$
H_a:\text{At least one group has a different distribution}
$$

The expected-frequency formula, chi-square statistic, and degrees-of-freedom formula are the same as those used for a test of independence.

### Independence vs Homogeneity

| Independence | Homogeneity |
|---|---|
| Examines two categorical variables in one population. | Compares a categorical outcome across different populations or groups. |
| Asks whether variables are associated. | Asks whether distributions are the same. |
| Often samples individuals from one population. | Often samples individuals separately from each group or population. |
| Uses a contingency table. | Uses a contingency table. |

The distinction is primarily based on the study design and research question.

## 9. Pearson Residuals and Cell Contributions

A significant overall chi-square test does not identify exactly which cells contribute most to the discrepancy.

The contribution of a cell is:

$$
Contribution_{ij}=\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
$$

A larger contribution indicates that the cell contributes more to the total chi-square statistic.

### Pearson Residual

The Pearson residual standardises the difference between observed and expected frequencies:

$$
r_{ij}=\frac{O_{ij}-E_{ij}}{\sqrt{E_{ij}}}
$$

The chi-square statistic can be expressed as the sum of squared Pearson residuals:

$$
\chi^2=\sum r_{ij}^2
$$

A positive residual indicates that the observed frequency exceeds the expected frequency. A negative residual indicates that the observed frequency is below expectation.

### Python Implementation

```python
import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [20, 30, 50],
    [30, 40, 30]
])

chi2_stat, p_value, df, expected = chi2_contingency(
    observed,
    correction=False
)

pearson_residuals = (
    observed - expected
) / np.sqrt(expected)

cell_contributions = (
    (observed - expected) ** 2
) / expected

print("Pearson residuals:")
print(np.round(pearson_residuals, 3))

print("\nCell contributions:")
print(np.round(cell_contributions, 3))
```

Residual analysis can help identify where discrepancies occur. Formal cell-level conclusions may require adjusted residuals and correction for multiple comparisons.

## 10. Expected Frequency Conditions

The ordinary chi-square approximation works best when expected frequencies are sufficiently large.

A commonly taught guideline is:

$$
E\geq5
$$

This is a practical rule, not a universal requirement for every chi-square analysis. Suitability depends on the test, table dimensions, and distribution of expected counts.

When expected frequencies are very small, consider:

- Collecting more data.
- Combining logically similar categories when scientifically justified.
- Using an exact test where appropriate.
- Using a simulation-based method.
- Choosing a procedure designed for sparse contingency tables.

Do not combine categories merely to satisfy a numerical rule if doing so destroys meaningful information.

### Fisher's Exact Test

Fisher's exact test is particularly useful for small $2\times2$ contingency tables when the chi-square approximation may be unreliable.

```python
from scipy.stats import fisher_exact

observed = [
    [8, 2],
    [1, 9]
]

odds_ratio, p_value = fisher_exact(
    observed,
    alternative="two-sided"
)

print("Odds ratio:", odds_ratio)
print("P-value:", p_value)
```

The exact test calculates probabilities under the null hypothesis rather than relying on the ordinary large-sample chi-square approximation.

## 11. Yates' Continuity Correction

For a $2\times2$ contingency table, Yates' continuity correction is sometimes used to adjust the Pearson chi-square statistic.

$$
\chi_Y^2=\sum\frac{(|O-E|-0.5)^2}{E}
$$

The correction generally makes the test more conservative. Whether it is appropriate depends on the sample size, analysis context, and software method. Fisher's exact test may be preferable for some sparse tables.

In SciPy, the correction is available through `chi2_contingency` for the appropriate $2\times2$ case:

```python
from scipy.stats import chi2_contingency

observed = [
    [70, 30],
    [50, 50]
]

chi2_stat, p_value, df, expected = chi2_contingency(
    observed,
    correction=True
)

print("Corrected chi-square:", chi2_stat)
print("P-value:", p_value)
```

## 12. Effect Size: Cramer's V

A statistically significant chi-square result does not automatically indicate a strong association.

**Cramer's V** measures the strength of association between categorical variables.

$$
V=\sqrt{\frac{\chi^2}{N\min(r-1,c-1)}}
$$

Where:

- $\chi^2$ = Pearson chi-square statistic.
- $N$ = total sample size.
- $r$ = number of rows.
- $c$ = number of columns.

Cramer's V is nonnegative. Its maximum possible value is 1, and 0 indicates no association in the table.

### Worked Example

Suppose:

$$
\chi^2=8.4286
$$

$$
N=200,\qquad r=2,\qquad c=3
$$

First, calculate:

$$
\min(r-1,c-1)=\min(1,2)=1
$$

Then:

$$
V=\sqrt{\frac{8.4286}{200(1)}}
$$

$$
V\approx0.205
$$

This value should be interpreted in the context of the research question, table dimensions, and field of application rather than through universal cut-offs alone.

### Python Implementation

```python
import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [20, 30, 50],
    [30, 40, 30]
])

chi2_stat, p_value, df, expected = chi2_contingency(
    observed,
    correction=False
)

n = observed.sum()
rows, columns = observed.shape

cramers_v = np.sqrt(
    chi2_stat /
    (n * min(rows - 1, columns - 1))
)

print("Chi-square statistic:", chi2_stat)
print("P-value:", p_value)
print("Cramer's V:", cramers_v)
```

### Phi Coefficient

For a $2\times2$ contingency table, the magnitude of the phi coefficient is related to the chi-square statistic by:

$$
|\phi|=\sqrt{\frac{\chi^2}{N}}
$$

Phi and Cramer's V are equivalent in magnitude for a $2\times2$ table. The formula above gives a nonnegative magnitude; a signed phi coefficient depends on the coding and arrangement of the categories.

## 13. Relationship Between Chi-Square and Proportion Tests

For a $2\times2$ table, Pearson's chi-square test and the corresponding two-sided, pooled two-proportion z-test have an important large-sample relationship under equivalent assumptions:

$$
\chi^2=z^2
$$

For example, if the equivalent z-statistic is:

$$
z=2
$$

then:

$$
\chi^2=2^2=4
$$

This relationship connects categorical-data analysis with hypothesis testing for proportions.

## 14. Additional Worked Example: Study Method and Exam Results

Suppose a researcher wants to investigate whether study method is associated with pass/fail status.

| Study Method | Pass | Fail | Total |
|---|---:|---:|---:|
| Method A | 70 | 30 | 100 |
| Method B | 50 | 50 | 100 |
| Total | 120 | 80 | 200 |

### Hypotheses

$$
H_0:\text{Study method and outcome are independent}
$$

$$
H_a:\text{Study method and outcome are associated}
$$

### Expected Frequencies

For Method A and Pass:

$$
E=\frac{100(120)}{200}=60
$$

For Method A and Fail:

$$
E=\frac{100(80)}{200}=40
$$

The expected frequencies for Method B are also 60 for Pass and 40 for Fail.

| Study Method | Pass | Fail |
|---|---:|---:|
| A | 60 | 40 |
| B | 60 | 40 |

### Chi-Square Statistic

$$
\chi^2=
\frac{(70-60)^2}{60}
+\frac{(30-40)^2}{40}
+\frac{(50-60)^2}{60}
+\frac{(50-40)^2}{40}
$$

$$
\chi^2\approx8.333
$$

Degrees of freedom:

$$
df=(2-1)(2-1)=1
$$

The p-value is below 0.05, so the null hypothesis is rejected. There is evidence of an association between study method and pass/fail status.

This observational result does not, by itself, establish that the study method caused the difference in outcomes.

### Python Implementation

```python
import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [70, 30],
    [50, 50]
])

chi2_stat, p_value, df, expected = chi2_contingency(
    observed,
    correction=False
)

print("Chi-square statistic:", chi2_stat)
print("Degrees of freedom:", df)
print("P-value:", p_value)
print("Expected frequencies:")
print(expected)
```

## 15. Chi-Square Distribution and Degrees of Freedom

The chi-square distribution is a probability distribution used to evaluate the chi-square statistic.

It is nonnegative and generally right-skewed for small degrees of freedom. As the degrees of freedom increase, its shape becomes more symmetric.

The standard chi-square tests use the right tail because larger values indicate greater discrepancies between observed and expected frequencies.

### Degrees of Freedom for Goodness-of-Fit

For $k$ categories with specified probabilities:

$$
df=k-1
$$

This accounts for the constraint that the category counts add up to a fixed total.

If parameters are estimated from the same data, an adjustment may be necessary.

### Degrees of Freedom for Contingency Tables

For $r$ rows and $c$ columns, excluding totals:

$$
df=(r-1)(c-1)
$$

For a table with four rows and three columns:

$$
df=(4-1)(3-1)=6
$$

The calculated statistic is evaluated against the chi-square distribution with the appropriate degrees of freedom.

## 16. Complete Goodness-of-Fit Example: Fair Die

Suppose a die is claimed to be fair. Each face should have probability:

$$
p_i=\frac{1}{6}
$$

The hypotheses are:

$$
H_0:p_1=p_2=\cdots=p_6=\frac{1}{6}
$$

$$
H_a:\text{The die does not follow the fair-die distribution}
$$

Suppose the die is rolled 600 times. The expected frequency for each face is:

$$
E=600\left(\frac{1}{6}\right)=100
$$

Observed frequencies:

| Face | Observed | Expected |
|---:|---:|---:|
| 1 | 90 | 100 |
| 2 | 110 | 100 |
| 3 | 95 | 100 |
| 4 | 105 | 100 |
| 5 | 120 | 100 |
| 6 | 80 | 100 |

The individual contributions are:

$$
\frac{(90-100)^2}{100}=1
$$

$$
\frac{(110-100)^2}{100}=1
$$

$$
\frac{(95-100)^2}{100}=0.25
$$

$$
\frac{(105-100)^2}{100}=0.25
$$

$$
\frac{(120-100)^2}{100}=4
$$

$$
\frac{(80-100)^2}{100}=4
$$

Therefore:

$$
\chi^2=1+1+0.25+0.25+4+4
$$

$$
\chi^2=10.5
$$

Degrees of freedom:

$$
df=6-1=5
$$

### Python Implementation

```python
from scipy.stats import chisquare

observed = [90, 110, 95, 105, 120, 80]
expected = [100, 100, 100, 100, 100, 100]

chi2_stat, p_value = chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Chi-square statistic:", chi2_stat)
print("Degrees of freedom:", len(observed) - 1)
print("P-value:", p_value)
```

Use the resulting p-value and chosen significance level to decide whether the observed outcomes provide evidence against the fair-die model.

## 17. Assumptions and Conditions

Before performing a chi-square test, check the following conditions.

### Categorical Frequency Data

The analysis should use meaningful category counts. Continuous measurements should not be inserted directly into a standard categorical chi-square test without an appropriate categorisation or alternative method.

### Independent Observations

Observations should be independent under the intended sampling design. Repeated observations from the same individual or complex survey sampling may require specialised methods.

### Mutually Exclusive Categories

Each observation should be assigned to the appropriate category without being counted multiple times within the same variable's classification.

### Exhaustive Categories

The categories should account for the observations included in the analysis.

### Adequate Expected Frequencies

Expected counts should be sufficient for the chi-square approximation to be reliable. Very small expected counts may call for exact or simulation-based procedures.

### Appropriate Expected Frequencies

For goodness-of-fit, expected counts must follow the specified null distribution. For independence and homogeneity, expected counts are derived from the row and column totals.

## 18. Counts, Percentages, and Survey Data

Chi-square tests are normally calculated using counts.

For example, the following table contains usable frequency data:

| Group | Yes | No |
|---|---:|---:|
| A | 40 | 60 |
| B | 50 | 50 |

If only percentages are available, the sample sizes are needed to reconstruct the frequencies.

Complex survey data may require weights and adjustments for clustering and stratification. Ordinary chi-square formulas should not automatically be applied to complex survey designs.

Expected frequencies must be nonnegative. A zero expected frequency makes the ordinary contribution formula undefined because it requires division by zero; the category specification or statistical method must be reconsidered.

## 19. Sample Size, Significance, and Effect Size

A larger sample can make relatively small discrepancies statistically significant. With a smaller sample, a noticeable difference may not provide sufficient statistical evidence to reject the null hypothesis.

The p-value and effect size answer different questions:

- **P-value:** How incompatible are the observed data with the null hypothesis under the test's assumptions?
- **Effect size:** How strong is the association or discrepancy?
- **Practical importance:** Does the result matter in the real-world context?

For contingency tables, Cramer's V can complement the p-value. A significant result does not automatically imply a strong or practically important association.

## 20. Multiple Comparisons and Follow-Up Analysis

A significant overall chi-square test indicates an overall departure from the null hypothesis. It does not prove that every cell differs from expectation or identify every specific group difference.

Possible follow-up methods include:

- Examining Pearson or adjusted residuals.
- Performing pairwise proportion comparisons with multiplicity adjustment.
- Conducting scientifically planned comparisons.
- Performing category-specific analyses.

When multiple follow-up tests are performed, account for multiple comparisons to reduce the risk of false-positive conclusions.

## 21. Common Mistakes

### Mistake 1: Using percentages without sample sizes

Counts or enough information to reconstruct the counts are needed.

### Mistake 2: Calculating expected frequencies from observed counts alone

Expected frequencies must be derived from the null hypothesis.

### Mistake 3: Assuming expected frequencies must be integers

Expected counts can be decimals.

### Mistake 4: Using incorrect degrees of freedom

For a contingency table:

$$
df=(r-1)(c-1)
$$

For a goodness-of-fit test with fixed specified probabilities:

$$
df=k-1
$$

### Mistake 5: Claiming that association proves causation

A significant test of independence identifies evidence of association, not causation.

### Mistake 6: Ignoring small expected frequencies

The ordinary chi-square approximation may be unreliable with sparse tables.

### Mistake 7: Assuming a significant test identifies every cell difference

The overall statistic measures a combined discrepancy. Follow-up analysis is needed to investigate individual cells.

### Mistake 8: Reporting only the p-value

Include the test type, chi-square statistic, degrees of freedom, p-value, and interpretation. Include effect size where appropriate.

### Mistake 9: Combining categories without justification

Categories should only be combined when doing so is scientifically or substantively meaningful.

## 22. Reporting Chi-Square Results

A report should generally include:

- The test performed.
- The chi-square statistic.
- The degrees of freedom.
- The p-value.
- The statistical decision.
- The interpretation in context.
- An effect size when appropriate.

### Example: Test of Independence

A chi-square test of independence was conducted to examine the association between customer type and preferred payment method. The test produced:

$$
\chi^2(2)\approx8.43
$$

$$
p\approx0.015
$$

At the 5% significance level, the null hypothesis of independence was rejected. The results provide evidence of an association between customer type and preferred payment method. The result does not establish causation.

### Example: Goodness-of-Fit Test

A chi-square goodness-of-fit test was conducted to determine whether observed product choices were consistent with the specified distribution. The test produced:

$$
\chi^2(2)\approx2.67
$$

$$
p\approx0.264
$$

At the 5% significance level, the null hypothesis was not rejected. There was insufficient evidence that the observed product distribution differed from the specified distribution.

This conclusion does not prove that the specified distribution is correct.

## 23. Chi-Square Test Selection Guide

| Research Question | Appropriate Method |
|---|---|
| Does one categorical variable follow specified proportions? | Goodness-of-fit test |
| Are two categorical variables associated? | Test of independence |
| Do multiple populations have the same categorical distribution? | Test of homogeneity |
| Is a small-sample $2\times2$ table being analysed? | Consider Fisher's exact test |
| Are observations from a complex survey? | Consider a survey-adjusted procedure |

Choose the method according to the research question, data collection design, and assumptions.

## 24. Important Formula Summary

### General Chi-Square Statistic

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

### Expected Frequency for Goodness-of-Fit

$$
E_i=Np_i
$$

### Goodness-of-Fit Degrees of Freedom

For fixed specified probabilities:

$$
df=k-1
$$

When $m$ independent parameters are estimated from the data:

$$
df=k-1-m
$$

### Expected Frequency for Contingency Tables

$$
E_{ij}=\frac{R_iC_j}{N}
$$

### Degrees of Freedom for Independence and Homogeneity

$$
df=(r-1)(c-1)
$$

### Pearson Residual

$$
r_{ij}=\frac{O_{ij}-E_{ij}}{\sqrt{E_{ij}}}
$$

### Cramer's V

$$
V=\sqrt{\frac{\chi^2}{N\min(r-1,c-1)}}
$$

### Phi Coefficient Magnitude for a $2\times2$ Table

$$
|\phi|=\sqrt{\frac{\chi^2}{N}}
$$

### Yates' Continuity-Corrected Statistic

$$
\chi_Y^2=\sum\frac{(|O-E|-0.5)^2}{E}
$$

### Relationship to an Equivalent Two-Proportion Test

$$
\chi^2=z^2
$$

This relationship applies to the corresponding two-sided large-sample tests under equivalent assumptions.

## 25. Points to Remember

1. Chi-square tests are primarily used for categorical frequency data.
2. $O$ represents the observed frequency.
3. $E$ represents the expected frequency under the null hypothesis.
4. The chi-square statistic is nonnegative.
5. Large chi-square values indicate greater discrepancies between observed and expected frequencies.
6. Goodness-of-fit compares observed counts with a specified distribution.
7. Independence examines whether two categorical variables are associated.
8. Homogeneity compares categorical distributions across populations or groups.
9. Expected frequencies for goodness-of-fit are calculated using $E_i=Np_i$.
10. Expected frequencies for contingency tables are calculated using $E_{ij}=R_iC_j/N$.
11. Goodness-of-fit degrees of freedom depend on the number of categories and any parameters estimated.
12. Contingency-table degrees of freedom are $(r-1)(c-1)$.
13. A significant independence test indicates association, not causation.
14. Small expected frequencies require special care.
15. Fisher's exact test can be useful for appropriate small $2\times2$ tables.
16. Cramer's V measures association strength in contingency tables.
17. Statistical significance and practical importance are different.
18. Residuals can help identify cells that contribute strongly to the overall discrepancy.
19. Follow-up comparisons may require multiplicity adjustment.
20. Always interpret the result in the context of the original research question.

## 26. Chapter Summary

The chi-square test family provides methods for analysing categorical frequency data.

The central calculation compares observed frequencies with expected frequencies:

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

The goodness-of-fit test compares one categorical variable with a specified distribution. The test of independence examines whether two categorical variables are associated. The test of homogeneity compares categorical distributions across populations or groups.

For contingency tables, expected frequencies are calculated using:

$$
E_{ij}=\frac{R_iC_j}{N}
$$

The degrees of freedom are:

$$
df=(r-1)(c-1)
$$

The calculated statistic is evaluated using the chi-square distribution and the appropriate degrees of freedom. When the p-value is below the significance level, the null hypothesis is rejected.

However, statistical significance does not automatically establish causation or indicate a strong association. Effect sizes, assumptions, expected frequencies, study design, and practical context should also be considered.

The complete workflow is:

**Categorical Data → Observed Frequencies → Expected Frequencies → Chi-Square Statistic → Degrees of Freedom → P-value → Decision → Interpretation**

## 27. Practice Questions

1. What is a chi-square test, and what types of data does it analyse?
2. Explain the difference between observed and expected frequencies.
3. State the formula for the chi-square statistic.
4. What is the purpose of the goodness-of-fit test?
5. A sample contains 300 observations divided into three categories with expected proportions of 0.40, 0.35, and 0.25. Calculate the expected frequencies.
6. Explain the null and alternative hypotheses for a test of independence.
7. A contingency table has four rows and three columns, excluding totals. Calculate the degrees of freedom.
8. What is the difference between independence and homogeneity tests?
9. Why can a significant chi-square result not establish causation?
10. What problems can arise when expected frequencies are very small?
11. Explain Pearson residuals and Cramer's V.
12. When might Fisher's exact test be preferred over the ordinary chi-square approximation?
13. Why should effect size accompany statistical significance when appropriate?
14. What information should be included when reporting a chi-square result?
15. Explain the relationship between Pearson's chi-square test and a two-proportion z-test in an equivalent $2\times2$ setting.

## 28. References and Further Reading

- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [NIST/SEMATECH — e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [Penn State — Statistics Online](https://online.stat.psu.edu/)
- [SciPy — Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [SciPy — `chi2_contingency`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
- [SciPy — `chisquare`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- Agresti, *An Introduction to Categorical Data Analysis*.
- Montgomery and Runger, *Applied Statistics and Probability for Engineers*.

## Related Topics

- Statistics Fundamentals
- Descriptive Statistics
- Probability
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- ANOVA
- Correlation
- Regression Model Evaluation
- Statistics for Machine Learning
