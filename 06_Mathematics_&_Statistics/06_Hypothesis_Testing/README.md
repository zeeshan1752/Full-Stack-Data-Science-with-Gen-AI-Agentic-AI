# Hypothesis Testing

## Introduction to Hypothesis Testing

**Hypothesis testing** is a statistical method used to evaluate claims about a population using sample data. It is an important part of inferential statistics and is widely used in data analysis, machine learning experiments, business analytics, and scientific research.

For example, a company claims that its average delivery time is 30 minutes. By collecting a sample of delivery times, we can evaluate whether the available evidence provides a reason to question that claim.

Hypothesis testing does not prove a claim with absolute certainty. Instead, it provides a systematic method for making decisions under uncertainty.

### What This Chapter Covers

- Statistical hypotheses and test direction
- Null and alternative hypotheses
- Significance level and p-value
- Test statistics and critical values
- Type I and Type II errors
- Statistical power
- Z-tests and t-tests
- One-proportion z-test
- Test selection and assumptions
- Statistical versus practical significance
- Reporting and interpreting results using Python

---

## 1. What Is a Statistical Hypothesis?

A **statistical hypothesis** is a statement about a population parameter or probability distribution.

Examples include:

- The population mean is 50.
- The population proportion is 0.40.
- The average delivery time is greater than 30 minutes.
- The average scores of two groups are different.

Common symbols include:

| Symbol | Meaning |
|---|---|
| $\mu$ | Population mean |
| $p$ | Population proportion |
| $\sigma$ | Population standard deviation |
| $\mu_0$ | Hypothesised population mean |
| $p_0$ | Hypothesised population proportion |
| $\alpha$ | Significance level |
| $\beta$ | Probability of a Type II error |

A statistical hypothesis is evaluated using sample evidence and an appropriate probability model.

## 2. Null and Alternative Hypotheses

Hypothesis testing generally involves two competing statements.

### 2.1 Null Hypothesis

The **null hypothesis**, denoted by $H_0$, is the reference claim evaluated using sample evidence.

For example:

$$
H_0:\mu=50
$$

This states that the population mean equals 50.

### 2.2 Alternative Hypothesis

The **alternative hypothesis**, denoted by $H_a$ or $H_1$, represents the difference or effect being investigated.

The research question determines the direction of the alternative hypothesis.

| Test type | Alternative hypothesis | Meaning |
|---|---|---|
| Two-tailed | $H_a:\mu\ne\mu_0$ | The mean is different |
| Right-tailed | $H_a:\mu>\mu_0$ | The mean is greater |
| Left-tailed | $H_a:\mu<\mu_0$ | The mean is smaller |

For example, if a company claims that average delivery time is 30 minutes and we want to investigate whether it differs from the claim:

$$
H_0:\mu=30
$$

$$
H_a:\mu\ne30
$$

The hypotheses and test direction should be chosen before examining the results. Choosing a direction after seeing the data can increase the risk of misleading conclusions.

### One-Tailed vs Two-Tailed Tests

A **one-tailed test** investigates a difference in one specified direction. A **two-tailed test** investigates a difference in either direction.

For a two-tailed test, evidence in either extreme of the reference distribution may lead to rejection of the null hypothesis.

## 3. Steps in Hypothesis Testing

A hypothesis test generally follows these steps:

1. Define the research question and population parameter.
2. State the null and alternative hypotheses.
3. Choose the significance level $\alpha$.
4. Select an appropriate statistical test.
5. Check the assumptions of the test.
6. Calculate the test statistic.
7. Obtain the p-value or compare the statistic with a critical value.
8. Make the statistical decision.
9. Interpret the result in the original context.

The decision alone is not the complete analysis. The result should also be interpreted in terms of the estimated effect, uncertainty, and practical importance.

## 4. Significance Level

The **significance level**, denoted by $\alpha$, is the threshold used to determine whether the evidence is sufficiently strong to reject the null hypothesis.

Common significance levels are:

$$
\alpha=0.10
$$

$$
\alpha=0.05
$$

$$
\alpha=0.01
$$

A significance level of 0.05 corresponds to a 5% long-run probability of rejecting a true null hypothesis when the testing procedure and its assumptions hold.

A smaller significance level generally requires stronger evidence to reject $H_0$.

The significance level should normally be selected before interpreting the test result.

## 5. Test Statistic

A **test statistic** measures how far the observed sample result is from the value expected under the null hypothesis, relative to its standard error.

A general structure is:

$$
\text{Test Statistic}=
\frac{\text{Observed Estimate}-\text{Null Value}}
{\text{Standard Error}}
$$

The exact formula depends on the statistical test.

Common test statistics include:

| Statistic | Common application |
|---|---|
| Z-statistic | Z-tests |
| t-statistic | T-tests |
| F-statistic | ANOVA and other F-tests |
| Chi-square statistic | Tests involving categorical counts and other applications |

Detailed ANOVA and Chi-Square procedures are covered in their dedicated repository folders.

## 6. P-Value

The **p-value** is the probability, assuming the null hypothesis is true, of obtaining a test statistic as extreme as or more extreme than the observed result in the direction specified by the alternative hypothesis.

The standard decision rule is:

$$
p\le\alpha
\quad\Rightarrow\quad
\text{Reject }H_0
$$

$$
p>\alpha
\quad\Rightarrow\quad
\text{Fail to reject }H_0
$$

### Worked Example

Suppose the p-value is 0.03 and the significance level is 0.05.

$$
p=0.03,\qquad\alpha=0.05
$$

Since the p-value is smaller than the significance level, we reject the null hypothesis.

Now suppose the p-value is 0.08.

$$
p=0.08,\qquad\alpha=0.05
$$

We fail to reject the null hypothesis because the p-value exceeds the significance level.

**Important:** A p-value is not the probability that the null hypothesis is true. Failing to reject $H_0$ does not prove that it is true.

A p-value also does not measure the size or practical importance of an effect.

## 7. Critical Value and Rejection Region

A **critical value** is a threshold determined by the significance level and the relevant probability distribution.

The **rejection region** contains the test-statistic values for which the null hypothesis is rejected.

For a two-tailed z-test at a significance level of 0.05, the standard Normal critical values are approximately:

$$
z=-1.96
$$

$$
z=1.96
$$

The null hypothesis is rejected when the observed z-statistic is below -1.96 or above 1.96.

For a two-tailed test:

$$
|z|>1.96
\quad\Rightarrow\quad
\text{Reject }H_0
$$

The p-value method and critical-value method produce the same decision when applied consistently to the same test.

## 8. Type I and Type II Errors

Because hypothesis testing uses sample data, an incorrect decision is possible.

| Error | Meaning | Probability |
|---|---|---|
| Type I error | Rejecting a true $H_0$ | $\alpha$ |
| Type II error | Failing to reject a false $H_0$ | $\beta$ |

### 8.1 Type I Error

A **Type I error** occurs when we reject the null hypothesis even though it is true.

For example, a test concludes that a new process changes the average delivery time when, in reality, there is no such change.

The probability of a Type I error is controlled by the significance level under the test's assumptions.

### 8.2 Type II Error

A **Type II error** occurs when we fail to reject the null hypothesis even though it is false.

For example, a test fails to detect a genuine improvement in delivery time.

The probability of a Type II error is denoted by $\beta$.

### 8.3 Statistical Power

**Statistical power** is the probability of correctly rejecting a false null hypothesis.

$$
\text{Power}=1-\beta
$$

Power generally increases with:

- A larger sample size.
- A larger true effect.
- Lower variability.
- A higher significance level, assuming other factors remain unchanged.

A test with low power may fail to detect a meaningful effect even when that effect exists.

## 9. Z-Test

A **z-test** uses the standard Normal distribution to evaluate a hypothesis.

For a one-sample population mean with a known population standard deviation:

$$
z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
$$

where:

- $\bar{x}$ is the sample mean.
- $\mu_0$ is the mean specified under the null hypothesis.
- $\sigma$ is the known population standard deviation.
- $n$ is the sample size.

### Worked Example

Suppose a sample has the following values:

- Sample mean = 52
- Hypothesised population mean = 50
- Known population standard deviation = 10
- Sample size = 100

The hypotheses for a two-tailed test are:

$$
H_0:\mu=50
$$

$$
H_a:\mu\ne50
$$

Calculate the test statistic:

$$
z=\frac{52-50}{10/\sqrt{100}}
$$

$$
z=\frac{2}{1}=2
$$

For a two-tailed test at $\alpha=0.05$, the critical values are approximately -1.96 and 1.96.

Since $z=2$ exceeds 1.96, we reject $H_0$.

The sample provides statistically significant evidence that the population mean differs from 50, subject to the test assumptions.

A one-sample z-test for a mean is appropriate when the population standard deviation is known and the sampling conditions support the Normal reference distribution.

## 10. T-Test

A **t-test** is commonly used to test hypotheses about population means when the population standard deviation is unknown.

### 10.1 One-Sample T-Test

A one-sample t-test compares a sample mean with a hypothesised population mean.

$$
t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}
$$

The degrees of freedom are:

$$
df=n-1
$$

Here, $s$ is the sample standard deviation.

### 10.2 Independent Two-Sample T-Test

An independent two-sample t-test compares the means of two independent groups.

Welch's t-test is often a suitable default because it does not require equal population variances.

### 10.3 Paired T-Test

A paired t-test is used when observations are naturally paired, such as measurements taken from the same individuals before and after a treatment.

First, calculate the difference for each pair. Then test whether the population mean difference equals zero.

### Python Implementation: Welch's T-Test

```python
from scipy import stats

group_a = [72, 75, 78, 74, 77]
group_b = [80, 82, 79, 85, 81]

t_statistic, p_value = stats.ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

alpha = 0.05

print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value <= alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
```

This test evaluates whether the two population means differ using a two-sided alternative by default.

The conclusion should also consider the estimated difference, effect size, data quality, and assumptions.

## 11. One-Proportion Z-Test

A **one-proportion z-test** evaluates a hypothesis about a population proportion.

For the null hypothesis $H_0:p=p_0$, the test statistic is:

$$
z=\frac{\hat{p}-p_0}
{\sqrt{p_0(1-p_0)/n}}
$$

where:

- $\hat{p}$ is the observed sample proportion.
- $p_0$ is the proportion specified under the null hypothesis.
- $n$ is the sample size.

The null proportion $p_0$ is used to calculate the standard error under the null hypothesis.

The Normal approximation requires suitable sample-size conditions. If the sample is small or the approximation is unsuitable, an exact binomial test may be preferable.

### Python Implementation

```python
from statsmodels.stats.proportion import proportions_ztest

successes = 60
observations = 100
hypothesised_proportion = 0.50

z_statistic, p_value = proportions_ztest(
    count=successes,
    nobs=observations,
    value=hypothesised_proportion
)

print("Z-statistic:", z_statistic)
print("P-value:", p_value)
```

The default alternative is two-sided. Install Statsmodels if necessary:

```bash
pip install statsmodels
```

## 12. Choosing the Appropriate Statistical Test

The correct test depends on the research question, the type of data, the sampling design, and the assumptions.

| Research question | Common test |
|---|---|
| Is a population mean different from a specified value when the population SD is known? | One-sample z-test |
| Is a population mean different from a specified value when the population SD is unknown? | One-sample t-test |
| Do two independent population means differ? | Independent two-sample t-test, often Welch's |
| Did the mean change between paired measurements? | Paired t-test |
| Does a population proportion differ from a specified value? | One-proportion z-test, when its conditions hold |
| Do three or more population means differ? | ANOVA |
| Are two categorical variables associated? | Chi-Square test of independence |

ANOVA is covered in `07_ANOVA`, while Chi-Square methods are covered in `08_Chi_Square_Test`. Their detailed theory and calculations should remain in those folders.

## 13. Assumptions of Hypothesis Testing

The assumptions depend on the selected test. Important considerations include:

**Random sampling:** The sample should represent the population of interest.

**Independence:** Observations should satisfy the independence conditions required by the test. Paired tests explicitly account for pairing.

**Distributional conditions:** Small-sample t-tests commonly rely on the relevant population or difference distribution being approximately Normal. Large-sample methods may rely on suitable approximations.

**Outliers:** Extreme observations can substantially affect means and test statistics.

**Equal variances:** Some pooled two-sample procedures assume equal population variances. Welch's t-test does not require this assumption.

**Proportion approximation:** A proportion z-test requires conditions that make the Normal approximation reasonable.

If assumptions are not satisfied, consider an appropriate alternative rather than automatically applying the same test.

## 14. Statistical Significance vs Practical Significance

**Statistical significance** indicates that the data provide evidence against the null hypothesis under the selected procedure.

**Practical significance** concerns whether the observed difference is meaningful in the real-world context.

For example, a very large dataset may produce a small p-value for a difference of only a few seconds in delivery time. That difference might not be important for the business.

Conversely, a potentially meaningful difference may not be statistically significant in a small sample.

A complete interpretation should consider:

- The estimated difference.
- The effect size.
- The p-value.
- The confidence interval or other measure of uncertainty.
- The sample size.
- The practical context.

A statistically significant result is not automatically an important result.

## 15. Common Mistakes

1. **Treating the p-value as the probability that $H_0$ is true.** It is calculated under the assumption that the null hypothesis is true.
2. **Accepting the null hypothesis merely because the result is not significant.** The correct wording is “fail to reject the null hypothesis.”
3. **Choosing a one-tailed test after seeing the results.** The test direction should be selected in advance.
4. **Ignoring assumptions or data quality.** A test cannot compensate for a poor sampling design.
5. **Confusing statistical significance with practical importance.** A small p-value does not measure the size of an effect.
6. **Using a z-test for a population mean when the population standard deviation is unknown without justification.** A t-test is commonly used in that situation.
7. **Reporting only whether a result is significant.** Include the test statistic, p-value, and contextual conclusion.
8. **Performing many tests without considering multiple comparisons.** Repeated testing can increase the risk of false-positive findings.
9. **Ignoring effect size and uncertainty.** A p-value alone is not a complete summary of the result.

## 16. Reporting Hypothesis Test Results

A useful report identifies the test, hypotheses, test statistic, degrees of freedom when applicable, p-value, significance level, decision, and contextual conclusion.

For example:

> A one-sample t-test was conducted to examine whether the population mean differs from 50. The test produced a t-statistic of 2.50 with 35 degrees of freedom. At the 5% significance level, the null hypothesis was rejected, providing evidence that the population mean differs from 50.

This is an illustrative reporting example. In an actual analysis, report the values produced by the data rather than copying these example values.

Where relevant, also report an effect size and confidence interval to describe the magnitude and uncertainty of the result.

## 17. Formula Summary

### One-Sample Z-Test for a Mean

$$
z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
$$

### One-Sample T-Test

$$
t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}
$$

### Degrees of Freedom for a One-Sample T-Test

$$
df=n-1
$$

### One-Proportion Z-Test

$$
z=\frac{\hat{p}-p_0}
{\sqrt{p_0(1-p_0)/n}}
$$

### Statistical Power

$$
\text{Power}=1-\beta
$$

### Hypothesis Test Decision Rules

$$
p\le\alpha
\quad\Rightarrow\quad
\text{Reject }H_0
$$

$$
p>\alpha
\quad\Rightarrow\quad
\text{Fail to reject }H_0
$$

---

## 18. Key Points to Remember

1. Hypothesis testing evaluates population claims using sample evidence.
2. The null hypothesis is the reference claim; the alternative defines the departure being investigated.
3. The significance level should be chosen before interpreting the test result.
4. A p-value measures how extreme the observed evidence is under the null hypothesis.
5. Reject $H_0$ when $p\le\alpha$ under the standard decision rule.
6. Failing to reject $H_0$ does not establish that it is true.
7. Type I and Type II errors describe different kinds of incorrect decisions.
8. Statistical power is the probability of correctly rejecting a false null hypothesis.
9. Select the test according to the research question, data structure, and assumptions.
10. Statistical significance does not automatically imply practical importance.
11. Report the result in context and consider effect size and uncertainty.
12. ANOVA and Chi-Square procedures have dedicated chapters in this repository.

## 19. Practice Questions

1. Define a statistical hypothesis.
2. Explain the difference between the null and alternative hypotheses.
3. What is the significance level?
4. Explain the meaning of a p-value.
5. Differentiate between one-tailed and two-tailed tests.
6. Explain Type I and Type II errors.
7. What is statistical power?
8. When is a one-sample z-test appropriate?
9. Differentiate between independent and paired t-tests.
10. Why is Welch's t-test often used for independent groups?
11. Why should a statistically significant result also be evaluated for practical significance?
12. Why should the test direction be selected before examining the results?

## 20. References

- NIST/SEMATECH, [e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- SciPy, [Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- Statsmodels, [Official Documentation](https://www.statsmodels.org/stable/index.html)
- Penn State, [STAT 500: Applied Statistics](https://online.stat.psu.edu/stat500/)

### Related Topics in This Repository

- `03_Probability`
- `04_Probability_Distributions`
- `05_Inferential_Statistics`
- `07_ANOVA`
- `08_Chi_Square_Test`
- `09_Correlation`
- `10_Regression`
- `11_Regression_Model_Evaluation`
