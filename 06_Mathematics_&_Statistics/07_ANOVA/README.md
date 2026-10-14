# Analysis of Variance (ANOVA)

## 1. Introduction

ANOVA stands for **Analysis of Variance**. It is a statistical method used to determine whether there is sufficient evidence that the means of three or more populations differ.

Although ANOVA compares means, it uses variation to perform the comparison.

It examines two sources of variation:

1. **Between-group variation:** Differences between the group means.
2. **Within-group variation:** Differences between observations belonging to the same group.

If the variation between groups is large relative to the variation within groups, ANOVA may provide evidence that not all population means are equal.

ANOVA is useful in data analysis, business analytics, experimental analysis, and machine learning experiments.

For example, a data scientist may use ANOVA to compare the average performance of three different experimental conditions.

## 2. One-Way ANOVA

One-way ANOVA examines the effect of **one categorical factor** on a quantitative response variable.

For example:

| Variable | Example |
|---|---|
| Factor | Teaching method |
| Factor levels | Method A, Method B, Method C |
| Response variable | Examination score |

The factor divides the observations into groups, and ANOVA compares their population means.

## 3. Hypotheses of ANOVA

Suppose there are \(k\) independent groups.

The null hypothesis states that all population means are equal:

$H_0: \mu_1 = \mu_2 = \cdots = \mu_k$

The alternative hypothesis states that at least one population mean differs:

$H_a: \text{At least one population mean differs}$

A significant ANOVA result does not mean that every group differs from every other group. It indicates evidence that the population means are not all equal.

## 4. Understanding Variation

ANOVA divides total variation into between-group and within-group components.

The fundamental relationship is:

$SS_T = SS_B + SS_W$

Where:

- \(SS_T\) = total sum of squares.
- \(SS_B\) = between-group sum of squares.
- \(SS_W\) = within-group sum of squares.

### 4.1 Grand Mean

The grand mean is the mean of all observations combined.

$\bar{x}_{grand} = \frac{\sum_{i=1}^{k} n_i\bar{x}_i}{N}$

Where:

- \(n_i\) = number of observations in group \(i\).
- \(\bar{x}_i\) = mean of group \(i\).
- \(N\) = total number of observations.

$N = \sum_{i=1}^{k} n_i$

### 4.2 Total Sum of Squares

The total sum of squares measures the variation of all observations around the grand mean.

$SS_T = \sum_{i=1}^{N}(x_i-\bar{x}_{grand})^2$

### 4.3 Between-Group Sum of Squares

This measures how far the group means are from the grand mean.

$SS_B = \sum_{i=1}^{k}n_i(\bar{x}_i-\bar{x}_{grand})^2$

### 4.4 Within-Group Sum of Squares

This measures how far individual observations are from their respective group means.

$SS_W = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(x_{ij}-\bar{x}_i)^2$

Where \(x_{ij}\) represents observation \(j\) in group \(i\).

## 5. Worked Example: Calculating Sums of Squares

Consider the following data:

| Group A | Group B | Group C |
|---:|---:|---:|
| 10 | 16 | 22 |
| 12 | 18 | 24 |
| 14 | 20 | 26 |

### Step 1: Calculate the group means

For Group A:

$\bar{x}_A = \frac{10+12+14}{3} = 12$

For Group B:

$\bar{x}_B = \frac{16+18+20}{3} = 18$

For Group C:

$\bar{x}_C = \frac{22+24+26}{3} = 24$

### Step 2: Calculate the grand mean

There are \(N=9\) observations.

$\bar{x}_{grand} = \frac{10+12+14+16+18+20+22+24+26}{9}$

$\boxed{\bar{x}_{grand}=18}$

### Step 3: Calculate the between-group sum of squares

$SS_B = 3(12-18)^2 + 3(18-18)^2 + 3(24-18)^2$

$SS_B = 3(36) + 3(0) + 3(36)$

$SS_B = 108 + 0 + 108$

**Answer:**

$\boxed{SS_B=216}$

### Step 4: Calculate the within-group sum of squares

For Group A:

$SS_A = (10-12)^2+(12-12)^2+(14-12)^2$

$SS_A = 4+0+4=8$

For Group B:

$SS_B^{(within)} = (16-18)^2+(18-18)^2+(20-18)^2$

$SS_B^{(within)} = 4+0+4=8$

For Group C:

$SS_C = (22-24)^2+(24-24)^2+(26-24)^2$

$SS_C = 4+0+4=8$

Therefore:

$SS_W = 8+8+8$

**Answer:**

$\boxed{SS_W=24}$

### Step 5: Calculate the total sum of squares

$SS_T = SS_B + SS_W$

$SS_T = 216+24$

**Answer:**

$\boxed{SS_T=240}$

The sum-of-squares decomposition is verified.

## 6. Degrees of Freedom

Degrees of freedom are used to calculate the mean squares.

| Source | Formula |
|---|---|
| Between groups | `df_B = k - 1` |
| Within groups | `df_W = N - k` |
| Total | `df_T = N - 1` |

For the worked example, \(k=3\) and \(N=9\).

Between-group degrees of freedom:

$df_B = 3-1 = 2$

Within-group degrees of freedom:

$df_W = 9-3 = 6$

Total degrees of freedom:

$df_T = 9-1 = 8$

The relationship is:

$df_T = df_B + df_W$

$8 = 2+6$

## 7. Mean Squares

A mean square is calculated by dividing a sum of squares by its corresponding degrees of freedom.

Between-group mean square:

$MS_B = \frac{SS_B}{df_B}$

Within-group mean square:

$MS_W = \frac{SS_W}{df_W}$

Using the worked example:

$MS_B = \frac{216}{2} = 108$

$MS_W = \frac{24}{6} = 4$

## 8. F-Statistic

The F-statistic compares between-group variation with within-group variation.

$F = \frac{MS_B}{MS_W}$

Using the previous results:

$F = \frac{108}{4}$

**Answer:**

$\boxed{F=27}$

A large F-statistic indicates that the variation between group means is large relative to the variation within groups. The final statistical decision depends on the F-distribution and the corresponding degrees of freedom.

## 9. ANOVA Table

The ANOVA table summarises the main calculations.

| Source | Sum of Squares | df | Mean Square | F |
|---|---:|---:|---:|---:|
| Between groups | 216 | 2 | 108 | 27 |
| Within groups | 24 | 6 | 4 | — |
| Total | 240 | 8 | — | — |

The F-statistic is calculated as:

$F = \frac{MS_B}{MS_W}$

The p-value is obtained from the F-distribution using:

- Numerator degrees of freedom: \(df_B\)
- Denominator degrees of freedom: \(df_W\)

## 10. Decision Using the p-Value

The significance level is commonly set to \(\alpha=0.05\), although the appropriate level depends on the analysis.

| Condition | Decision |
|---|---|
| \(p \leq \alpha\) | Reject the null hypothesis |
| \(p > \alpha\) | Fail to reject the null hypothesis |

For example, if \(p=0.003\) and \(\alpha=0.05\), reject the null hypothesis. There is statistical evidence that not all population means are equal.

If \(p=0.27\) and \(\alpha=0.05\), fail to reject the null hypothesis. There is insufficient evidence to conclude that the population means differ.

**Important:** Failing to reject the null hypothesis does not prove that all population means are identical.

## 11. Assumptions of One-Way ANOVA

Classical one-way ANOVA relies on three main assumptions.

### 11.1 Independence

Observations should be independent according to the study design. Repeated observations from the same individual may require a different analysis.

### 11.2 Normality

The errors within each group should be approximately normally distributed. Severe skewness and extreme outliers can affect the analysis, particularly with small samples.

### 11.3 Homogeneity of Variance

The population variances should be reasonably equal.

$\sigma_1^2 = \sigma_2^2 = \cdots = \sigma_k^2$

Box plots and residual plots can help identify unusual spread, outliers, and other patterns.

**Levene's test** can assess evidence against equal variances. Its result should be considered alongside the study design, sample sizes, and graphical diagnostics.

## 12. Welch's ANOVA

Welch's ANOVA is an alternative when the assumption of equal population variances is questionable.

| Classical One-Way ANOVA | Welch's ANOVA |
|---|---|
| Assumes equal population variances | Does not require equal population variances |
| Uses the standard ANOVA F-test | Uses an adjusted test statistic and degrees of freedom |
| Suitable when its assumptions are reasonable | Useful when variances differ, particularly with unequal group sizes |

Unequal group sizes alone do not invalidate classical ANOVA. The decision should consider the variance pattern and study design.

## 13. Post-Hoc Tests

A significant ANOVA identifies an overall difference but does not identify which groups differ.

Post-hoc tests perform follow-up comparisons while accounting for multiple testing.

**Tukey's Honestly Significant Difference (HSD)** is a common method for comparing all pairs of group means.

For equal group sizes, the critical difference is:

$HSD = q_{\alpha,k,df_W}\sqrt{\frac{MS_W}{n}}$

Where:

- \(q\) = critical value from the studentized-range distribution.
- \(\alpha\) = significance level.
- \(k\) = number of groups.
- \(df_W\) = within-group degrees of freedom.
- \(MS_W\) = within-group mean square.
- \(n\) = observations per group.

Tukey's procedure is useful when the goal is to compare all group pairs. Other procedures may be appropriate for different comparison objectives.

## 14. Effect Size in ANOVA

Statistical significance does not indicate how large or practically important a group effect is. Effect sizes help quantify its magnitude.

### 14.1 Eta Squared

Eta squared measures the proportion of total variation associated with group differences in a one-way ANOVA.

$\eta^2 = \frac{SS_B}{SS_T}$

For the worked example:

$\eta^2 = \frac{216}{240}$

$\boxed{\eta^2=0.90}$

The between-group sum of squares accounts for 90% of the total sum of squares in this sample.

### 14.2 Omega Squared

Omega squared is a less upward-biased estimate of the population effect size.

$\omega^2 = \frac{SS_B-(k-1)MS_W}{SS_T+MS_W}$

Using the worked example:

$\omega^2 = \frac{216-(3-1)(4)}{240+4}$

$\omega^2 = \frac{208}{244}$

$\boxed{\omega^2 \approx 0.852}$

Effect-size interpretation should consider the subject area and practical context rather than relying on a universal threshold.

## 15. ANOVA in Python

Python libraries such as SciPy, pandas, and statsmodels can perform ANOVA calculations.

### 15.1 Using SciPy

```python
from scipy.stats import f_oneway

group_a = [10, 12, 14]
group_b = [16, 18, 20]
group_c = [22, 24, 26]

f_statistic, p_value = f_oneway(
    group_a,
    group_b,
    group_c
)

print("F-statistic:", f_statistic)
print("p-value:", p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothesis.")
    print("At least one population mean differs.")
else:
    print("Fail to reject the null hypothesis.")
    print("Insufficient evidence of different means.")
```

### 15.2 Using Statsmodels

Statsmodels provides an ANOVA table through an ordinary least-squares model.

```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.DataFrame({
    "score": [
        10, 12, 14,
        16, 18, 20,
        22, 24, 26
    ],
    "group": [
        "A", "A", "A",
        "B", "B", "B",
        "C", "C", "C"
    ]
})

model = ols("score ~ C(group)", data=df).fit()

anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
```

Here, `C(group)` tells statsmodels to treat the group variable as categorical.

### 15.3 Tukey HSD in Python

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

result = pairwise_tukeyhsd(
    endog=df["score"],
    groups=df["group"],
    alpha=0.05
)

print(result)
```

Tukey HSD identifies which pairs of group means differ significantly while accounting for multiple comparisons.

## 16. Choosing an Appropriate Analysis

| Situation | Appropriate approach |
|---|---|
| Compare means across independent groups when equal-variance assumptions are reasonable | One-way ANOVA |
| Compare independent group means when variances are unequal | Welch's ANOVA |
| Identify which group pairs differ | Appropriate post-hoc procedure, such as Tukey HSD |
| Compare two independent group means | Appropriate two-sample t-test |
| Analyse repeated measurements from the same subjects | A method designed for repeated or paired data |

The choice of statistical method should follow the study design, response variable, and assumptions.

## 17. Points to Remember

1. ANOVA stands for Analysis of Variance.
2. One-way ANOVA compares population means across independent groups.
3. The null hypothesis states that all population means are equal.
4. The alternative states that at least one population mean differs.
5. Total variation is divided into between-group and within-group variation.
6. The central identity is `SS_T = SS_B + SS_W`.
7. The F-statistic is `F = MS_B / MS_W`.
8. The standard ANOVA F-test uses the right tail of the F-distribution.
9. A significant ANOVA does not identify which groups differ.
10. Post-hoc tests can be used for follow-up comparisons.
11. Independence, normality of errors, and equal variances are important assumptions.
12. Welch's ANOVA is useful when equal variances are questionable.
13. Effect sizes describe the magnitude of group differences.
14. SciPy and statsmodels can perform ANOVA in Python.
15. Statistical significance and practical importance are not the same.

## 18. Formula Summary

### Grand Mean

$\bar{x}_{grand} = \frac{\sum_{i=1}^{k}n_i\bar{x}_i}{N}$

### Total Sum of Squares

$SS_T = \sum_{i=1}^{N}(x_i-\bar{x}_{grand})^2$

### Between-Group Sum of Squares

$SS_B = \sum_{i=1}^{k}n_i(\bar{x}_i-\bar{x}_{grand})^2$

### Within-Group Sum of Squares

$SS_W = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(x_{ij}-\bar{x}_i)^2$

### Sum-of-Squares Identity

$SS_T = SS_B + SS_W$

### Degrees of Freedom

$df_B = k-1$

$df_W = N-k$

$df_T = N-1$

### Mean Squares

$MS_B = \frac{SS_B}{df_B}$

$MS_W = \frac{SS_W}{df_W}$

### F-Statistic

$F = \frac{MS_B}{MS_W}$

### Eta Squared

$\eta^2 = \frac{SS_B}{SS_T}$

### Omega Squared

$\omega^2 = \frac{SS_B-(k-1)MS_W}{SS_T+MS_W}$

## 19. Practice Questions

1. What is ANOVA, and why is it used?
2. Write the null and alternative hypotheses for a one-way ANOVA.
3. Explain between-group and within-group variation.
4. Calculate the grand mean for groups with unequal sample sizes.
5. Explain the relationship between total, between-group, and within-group sums of squares.
6. Calculate the degrees of freedom for an ANOVA with four groups and 40 observations.
7. What does a large F-statistic indicate?
8. Why does a significant ANOVA not identify the exact groups that differ?
9. Explain the assumptions of classical one-way ANOVA.
10. When should Welch's ANOVA be considered?
11. What is the purpose of Tukey HSD?
12. Calculate eta squared from given sums of squares.
13. Perform a one-way ANOVA using SciPy.
14. Generate an ANOVA table using statsmodels.

## 20. References

- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [NIST/SEMATECH — e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [Penn State — STAT Online](https://online.stat.psu.edu/)
- [SciPy — `f_oneway`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)
- [Statsmodels — ANOVA](https://www.statsmodels.org/stable/anova.html)
- [Statsmodels — Tukey HSD](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html)
