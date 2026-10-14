# Hypothesis Testing

Hypothesis testing is a statistical method used to evaluate claims about a population using sample data. It is an important part of inferential statistics and is widely used in data analysis, machine learning experiments, business analytics, and scientific research.

For example, a company may claim that its average delivery time is 30 minutes. By collecting a sample of delivery times, we can evaluate whether the available evidence provides a reason to question that claim.

Hypothesis testing does not prove a claim with absolute certainty. Instead, it provides a systematic method for making decisions under uncertainty.

## 1. What Is a Statistical Hypothesis?

A **statistical hypothesis** is a statement about a population parameter or probability distribution.

Examples include:

- The population mean is 50.
- The population proportion is 0.40.
- The average delivery time is greater than 30 minutes.
- The average scores of two groups are different.

A population mean is represented by $\mu$, a population proportion by $p$, and a population standard deviation by $\sigma$.

## 2. Null and Alternative Hypotheses

### Null Hypothesis

The **null hypothesis**, denoted by $H_0$, is the reference claim evaluated using sample evidence.

For example:

$H_0:\mu=50$

This states that the population mean equals 50.

### Alternative Hypothesis

The **alternative hypothesis**, denoted by $H_a$ or $H_1$, represents the difference or effect being investigated.

The alternative hypothesis determines the direction of the test.

| Test type | Alternative hypothesis | Meaning |
|---|---|---|
| Two-tailed | $H_a:\mu\ne\mu_0$ | The mean is different |
| Right-tailed | $H_a:\mu>\mu_0$ | The mean is greater |
| Left-tailed | $H_a:\mu<\mu_0$ | The mean is smaller |

For example, if a company claims that the average delivery time is 30 minutes and we want to determine whether it differs from the claim:

$H_0:\mu=30$

$H_a:\mu\ne30$

The hypotheses should be selected according to the research question before examining the results.

## 3. Steps in Hypothesis Testing

A hypothesis test generally follows these steps:

1. Define the research question and population parameter.
2. State the null and alternative hypotheses.
3. Choose the significance level $\alpha$.
4. Select an appropriate statistical test.
5. Calculate the test statistic.
6. Obtain the p-value or compare the statistic with a critical value.
7. Make the statistical decision.
8. Interpret the result in the original context.

## 4. Significance Level

The **significance level**, denoted by $\alpha$, is the threshold used to determine whether the evidence is sufficiently strong to reject the null hypothesis.

Common significance levels are:

- $\alpha=0.10$
- $\alpha=0.05$
- $\alpha=0.01$

A significance level of 0.05 corresponds to a 5% long-run probability of rejecting a true null hypothesis when the testing procedure's assumptions hold.

A smaller significance level generally requires stronger evidence to reject $H_0$.

## 5. Test Statistic

A **test statistic** measures how far the observed sample result is from the value expected under the null hypothesis, relative to its standard error.

A general structure is:

Test statistic = (Observed estimate − Null value) / Standard error

The exact formula depends on the statistical test being used.

Examples include:

- Z-statistic for z-tests.
- t-statistic for t-tests.
- F-statistic for F-tests.
- Chi-square statistic for Chi-Square tests.

Detailed ANOVA and Chi-Square procedures are covered in their respective folders.

## 6. P-Value

The **p-value** is the probability, assuming the null hypothesis is true, of obtaining a test statistic as extreme as or more extreme than the observed result in the direction specified by the alternative hypothesis.

The standard decision rule is:

- If $p\le\alpha$, reject $H_0$.
- If $p>\alpha$, fail to reject $H_0$.

For example, suppose:

$p=0.03,\quad \alpha=0.05$

Since $0.03<0.05$, we reject the null hypothesis.

However, if:

$p=0.08,\quad \alpha=0.05$

we fail to reject the null hypothesis.

**Important:** The p-value is not the probability that the null hypothesis is true. Failing to reject $H_0$ does not prove that it is true.

## 7. Critical Value and Rejection Region

A **critical value** is a threshold determined by the significance level and the relevant probability distribution.

The **rejection region** contains the test-statistic values for which the null hypothesis is rejected.

For a two-tailed z-test at $\alpha=0.05$, the standard normal critical values are approximately:

$z=-1.96 \quad \text{and} \quad z=1.96$

The null hypothesis is rejected if the observed z-statistic is below −1.96 or above 1.96.

The p-value method and critical-value method are two ways of making the same statistical decision when applied consistently.

## 8. Type I and Type II Errors

A hypothesis test uses sample data, so an incorrect decision is possible.

| Error | Meaning | Probability |
|---|---|---|
| Type I error | Rejecting a true $H_0$ | $\alpha$ |
| Type II error | Failing to reject a false $H_0$ | $\beta$ |

### Type I Error

A Type I error occurs when the test concludes that there is evidence against the null hypothesis even though the null hypothesis is true.

### Type II Error

A Type II error occurs when the test fails to reject the null hypothesis even though it is false.

### Statistical Power

Statistical power is the probability of correctly rejecting a false null hypothesis.

$Power=1-\beta$

Power generally increases with a larger sample size, a larger true effect, or a higher significance level, assuming other factors remain unchanged.

## 9. Z-Test

A **z-test** uses the standard normal distribution to evaluate a hypothesis.

For a one-sample population mean with a known population standard deviation:

$z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$

Where:

- $\bar{x}$ = sample mean
- $\mu_0$ = mean specified under the null hypothesis
- $\sigma$ = known population standard deviation
- $n$ = sample size

### Example

Suppose a sample has:

- Sample mean = 52
- Hypothesised population mean = 50
- Known population standard deviation = 10
- Sample size = 100

The test statistic is:

$z=\frac{52-50}{10/\sqrt{100}}$

$z=\frac{2}{1}=2$

For a two-tailed test at $\alpha=0.05$, the critical values are approximately −1.96 and 1.96.

Since $2>1.96$, reject $H_0$.

The sample provides statistically significant evidence that the population mean differs from 50, subject to the test assumptions.

A one-sample z-test for a mean is appropriate when the population standard deviation is known and the sampling conditions support the normal approximation.

## 10. T-Test

A **t-test** is commonly used to test hypotheses about population means when the population standard deviation is unknown.

### One-Sample T-Test

Used to compare a sample mean with a hypothesised population mean.

$t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$

Degrees of freedom:

$df=n-1$

Here, $s$ is the sample standard deviation.

### Independent Two-Sample T-Test

Used to compare the means of two independent groups.

Welch's t-test is often a suitable default because it does not require equal population variances.

### Paired T-Test

Used when observations are naturally paired, such as measurements taken from the same individuals before and after a treatment.

First calculate the difference for each pair. Then test whether the population mean difference equals zero.

### Python Example

```python
from scipy import stats

group_a = [72, 75, 78, 74, 77]
group_b = [80, 82, 79, 85, 81]

# Independent two-sample Welch's t-test
t_statistic, p_value = stats.ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
```

This test evaluates whether the two population means differ. The conclusion should also consider the effect size, data quality, and assumptions.

## 11. One-Proportion Z-Test

A one-proportion z-test evaluates a hypothesis about a population proportion.

For the null hypothesis $H_0:p=p_0$, the test statistic is:

$z=\frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$

Where:

- $\hat{p}$ = observed sample proportion
- $p_0$ = proportion specified under the null hypothesis
- $n$ = sample size

The null proportion $p_0$ is used to calculate the standard error under the null hypothesis.

The normal approximation requires suitable sample-size conditions. If the sample is small or the approximation is unsuitable, an exact binomial test may be preferable.

### Python Example

```python
from statsmodels.stats.proportion import (
    proportions_ztest
)

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

This example tests whether the population proportion differs from 0.50 using the default two-sided alternative.

## 12. Choosing the Appropriate Test

| Research question | Common test |
|---|---|
| Is a population mean different from a specified value, with known population standard deviation? | One-sample z-test |
| Is a population mean different from a specified value, with unknown population standard deviation? | One-sample t-test |
| Do two independent population means differ? | Independent two-sample t-test, often Welch's |
| Did the mean change between paired measurements? | Paired t-test |
| Does a population proportion differ from a specified value? | One-proportion z-test, when its conditions hold |
| Do three or more population means differ? | ANOVA |
| Are two categorical variables associated? | Chi-Square test of independence |

ANOVA is covered in `07_ANOVA`, while Chi-Square methods are covered in `08_Chi_Square_Test`. Their detailed theory and formulas should remain in those folders.

## 13. Assumptions of Hypothesis Testing

The assumptions depend on the selected test. Common considerations include:

**Random sampling:** The sample should represent the population of interest.

**Independence:** Observations should satisfy the independence conditions required by the test. Paired tests instead account for the pairing.

**Distributional conditions:** Small-sample t-tests commonly rely on the relevant population or difference distribution being approximately normal, while large-sample methods may rely on suitable approximations.

**Outliers:** Extreme observations can substantially affect means and test statistics.

**Equal variances:** Some pooled two-sample procedures assume equal population variances. Welch's t-test does not require this assumption.

**Proportion approximation:** A proportion z-test requires conditions that make the normal approximation reasonable.

If assumptions are not satisfied, consider a suitable alternative rather than automatically applying the same test.

## 14. Statistical Significance vs Practical Significance

**Statistical significance** indicates that the data provide evidence against the null hypothesis under the selected procedure.

**Practical significance** concerns whether the observed difference is meaningful in the real-world context.

A very large dataset can produce a small p-value for a difference that has little practical importance. Conversely, a potentially meaningful difference may not be statistically significant in a small sample.

Therefore, interpretation should consider the estimated difference, effect size, uncertainty, sample size, and domain context—not only the p-value.

## 15. Common Mistakes

1. Treating the p-value as the probability that $H_0$ is true.
2. Accepting the null hypothesis merely because the result is not significant.
3. Choosing a one-tailed test after seeing the results.
4. Ignoring assumptions or data quality.
5. Confusing statistical significance with practical importance.
6. Using a z-test for a population mean when the population standard deviation is unknown without justification.
7. Reporting only “significant” without the test statistic, p-value, and contextual conclusion.
8. Performing many tests without considering the increased risk of false-positive findings.

The correct wording for a non-significant result is **“fail to reject the null hypothesis,”** not “accept the null hypothesis.”

## 16. Reporting Results

A useful report identifies the test, hypotheses, test statistic, degrees of freedom when applicable, p-value, significance level, decision, and contextual conclusion.

For example:

> A one-sample t-test was conducted to examine whether the population mean differs from 50. The test produced a t-statistic of 2.50 with 35 degrees of freedom. At the 5% significance level, the null hypothesis was rejected, providing evidence that the population mean differs from 50.

In a complete analysis, also report an appropriate effect size and confidence interval where relevant.

## 17. Formula Summary

| Concept | Formula |
|---|---|
| One-sample z-test for a mean | $z=(\bar{x}-\mu_0)/(\sigma/\sqrt{n})$ |
| One-sample t-test | $t=(\bar{x}-\mu_0)/(s/\sqrt{n})$ |
| Degrees of freedom for one-sample t-test | $df=n-1$ |
| One-proportion z-test | $z=(\hat{p}-p_0)/\sqrt{p_0(1-p_0)/n}$ |
| Statistical power | $1-\beta$ |
| Reject decision | $p\le\alpha$ |
| Fail-to-reject decision | $p>\alpha$ |

## 18. Key Points to Remember

1. Hypothesis testing evaluates population claims using sample evidence.
2. The null hypothesis is the reference claim; the alternative defines the departure being investigated.
3. The significance level is chosen before interpreting the test result.
4. A p-value measures how extreme the observed evidence is under the null hypothesis.
5. Reject $H_0$ when $p\le\alpha$ under the standard decision rule.
6. Failing to reject $H_0$ does not establish that it is true.
7. Type I and Type II errors describe different kinds of incorrect decisions.
8. Select the test according to the research question, data structure, and assumptions.
9. Statistical significance does not automatically imply practical importance.
10. Report the result in context and consider effect size and uncertainty.

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
10. Why should a statistically significant result also be evaluated for practical significance?

## 20. References

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [SciPy Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)
- [Penn State — STAT 500: Applied Statistics](https://online.stat.psu.edu/stat500/)

---

**Folder placement:** Save this file as `06_Hypothesis_Testing/README.md`.

Keep detailed ANOVA and Chi-Square explanations in their dedicated folders. Keep confidence intervals and estimation methods primarily in `05_Inferential_Statistics`, referring to their relationship with hypothesis testing here without duplicating the entire chapter.
