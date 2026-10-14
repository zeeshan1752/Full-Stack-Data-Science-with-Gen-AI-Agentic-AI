# Hypothesis Testing

## Introduction

Hypothesis testing is a statistical framework used to evaluate claims about a population using sample data.

In inferential statistics, we usually cannot collect information about every member of a population. Instead, we select a sample and use the observed data to evaluate a claim about an unknown population parameter.

For example, suppose a company claims that the average delivery time is 30 minutes. We can collect a random sample of delivery times and determine whether the sample provides sufficient statistical evidence to question the claim.

Hypothesis testing provides a structured procedure for making this decision.

The objective is not to prove that a claim is absolutely true or false. Instead, we begin with a **null hypothesis**, measure how unusual the observed sample result would be if that hypothesis were true, and decide whether the evidence is strong enough to reject it.

This chapter covers null and alternative hypotheses, significance levels, p-values, test statistics, critical values, one-tailed and two-tailed tests, statistical errors, power, z-tests, t-tests, proportion tests, paired tests, assumptions, Python implementation, and practical interpretation.

## 1. What Is a Statistical Hypothesis?

A **statistical hypothesis** is a statement about a population parameter or probability distribution.

Examples include:

- The population mean is 50.
- The population proportion is 0.40.
- The average lifetime of a product is greater than 1,000 hours.
- The population mean differs from 75.

A hypothesis concerns a population parameter rather than a single observation.

For a population mean:

$\mu=50$

For a population proportion:

$p=0.40$

For a population variance:

$\sigma^2=25$

Here, $\mu$ represents the population mean, $p$ represents the population proportion, and $\sigma^2$ represents the population variance.

## 2. Hypothesis Testing as a Decision Process

A hypothesis test follows a systematic process.

1. Identify the population parameter.
2. State the null and alternative hypotheses.
3. Choose the significance level.
4. Collect sample data.
5. Select an appropriate statistical test.
6. Calculate the test statistic.
7. Find the p-value or critical value.
8. Make the statistical decision.
9. Interpret the result in the original context.

The calculation is only one part of hypothesis testing. The assumptions and interpretation are equally important.

## 3. Null Hypothesis

The **null hypothesis**, written as $H_0$, represents the default claim or reference value against which the sample evidence is evaluated.

Examples:

$H_0:\mu=50$

$H_0:p=0.40$

In ordinary hypothesis testing, the null hypothesis generally contains an equality. It establishes the reference condition used to calculate the test statistic.

The null hypothesis is not necessarily the researcher's preferred claim. It is the starting assumption against which evidence is evaluated.

## 4. Alternative Hypothesis

The **alternative hypothesis**, written as $H_a$ or $H_1$, represents the departure from the null hypothesis that the test is designed to detect.

There are three common forms.

### Two-sided alternative

$H_a:\mu\ne\mu_0$

This tests whether the population mean differs from the specified value in either direction.

### Right-tailed alternative

$H_a:\mu>\mu_0$

This tests whether the population mean is greater than the specified value.

### Left-tailed alternative

$H_a:\mu<\mu_0$

This tests whether the population mean is less than the specified value.

The alternative hypothesis determines the direction of the test.

## 5. Null and Alternative Hypotheses Together

Suppose a company claims that its average delivery time is 30 minutes.

If we want to investigate whether the true average is different from 30 minutes, we write:

$H_0:\mu=30$

$H_a:\mu\ne30$

This is a two-tailed test.

If we want to investigate whether delivery takes longer than claimed:

$H_0:\mu=30$

$H_a:\mu>30$

This is a right-tailed test.

If we want to investigate whether delivery is faster than claimed:

$H_0:\mu=30$

$H_a:\mu<30$

This is a left-tailed test.

The direction should be selected from the research question **before examining the result**.

## 6. Why Does the Null Hypothesis Contain Equality?

For an ordinary two-sided test, the standard formulation is:

$H_0:\mu=50$

$H_a:\mu\ne50$

The null hypothesis provides the reference value used to calculate the test statistic and its probability distribution.

A common beginner mistake is to reverse these hypotheses:

$H_0:\mu\ne50$

$H_a:\mu=50$

That is not the standard formulation for an ordinary two-sided test.

## 7. Significance Level

The **significance level**, denoted by $\alpha$, is the threshold used to decide when the sample evidence is sufficiently unusual under the null hypothesis.

Common values are:

- $\alpha=0.10$ — 10% significance level.
- $\alpha=0.05$ — 5% significance level.
- $\alpha=0.01$ — 1% significance level.

For example, $\alpha=0.05$ means that the testing procedure is designed with a 5% Type I error rate under the relevant assumptions.

The significance level should normally be selected before examining the test result.

### Important distinction

A significance level of 0.05 does **not** mean that there is a 5% probability that the null hypothesis is true.

It represents the long-run probability of rejecting a true null hypothesis when the testing procedure's assumptions hold.

## 8. Test Statistic

A **test statistic** measures how far the observed sample result is from the value expected under the null hypothesis, usually relative to its standard error.

For a population mean with known population standard deviation:

$z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$

Where:

- $\bar{x}$ = sample mean.
- $\mu_0$ = mean specified by the null hypothesis.
- $\sigma$ = known population standard deviation.
- $n$ = sample size.
- $\sigma/\sqrt{n}$ = standard error of the sample mean.

The numerator measures the difference between the observed sample mean and the hypothesised mean. The denominator expresses that difference in standard-error units.

### Interpreting the z-statistic

If $z=2$, the sample mean is two standard errors above the hypothesised mean.

If $z=-2$, the sample mean is two standard errors below the hypothesised mean.

A value near zero indicates that the sample result is relatively close to the null value.

A large absolute value, $|z|$, generally indicates greater disagreement with the null hypothesis.

## 9. The p-Value

The **p-value** is the probability, assuming the null hypothesis is true, of obtaining a test statistic at least as extreme as the observed statistic in the direction specified by the alternative hypothesis.

A small p-value indicates that the observed result would be unusual under the null model.

For a standard normal test statistic $Z$:

- Right-tailed test: $p=P(Z\ge z_{\text{obs}})$.
- Left-tailed test: $p=P(Z\le z_{\text{obs}})$.
- Two-tailed test: $p=2P(Z\ge |z_{\text{obs}}|)$.

These expressions assume a continuous standard normal reference distribution.

### p-Value decision rule

If:

$p\le\alpha$

then reject the null hypothesis.

If:

$p>\alpha$

then fail to reject the null hypothesis.

We generally do not say that the null hypothesis has been accepted merely because the p-value is greater than the significance level.

Failing to reject means that the evidence is insufficient to reject the null hypothesis at the chosen significance level.

### Example

Suppose a test produces:

$p=0.03$

and the selected significance level is:

$\alpha=0.05$

Since $0.03<0.05$, we reject the null hypothesis.

If instead $p=0.20$, we fail to reject the null hypothesis at the 5% significance level.

Neither decision, by itself, proves that the null hypothesis is true or false.

## 10. Critical Value Method

A hypothesis test can also be performed by comparing the test statistic with a **critical value**.

For a two-tailed z-test with $\alpha=0.05$, the critical values are approximately:

$z^*=-1.96,\quad z^*=1.96$

The rejection region is:

$z<-1.96\quad\text{or}\quad z>1.96$

Equivalently:

$|z|>1.96$

If the test statistic falls inside the interval from $-1.96$ to $1.96$, we fail to reject the null hypothesis.

### Common z critical values

| Test | Significance level | Critical value(s) |
|---|---:|---:|
| Right-tailed | 0.05 | $1.645$ |
| Left-tailed | 0.05 | $-1.645$ |
| Two-tailed | 0.05 | $\pm1.960$ |
| Two-tailed | 0.01 | $\pm2.576$ |
| Two-tailed | 0.10 | $\pm1.645$ |

The p-value method and the critical value method lead to the same decision when they use the same test, assumptions, and significance level.

## 11. One-Tailed and Two-Tailed Tests

The alternative hypothesis determines the test's tail structure.

| Test | Alternative hypothesis | Rejection region at $\alpha=0.05$ |
|---|---|---|
| Right-tailed z-test | $H_a:\mu>\mu_0$ | $z>1.645$ |
| Left-tailed z-test | $H_a:\mu<\mu_0$ | $z<-1.645$ |
| Two-tailed z-test | $H_a:\mu\ne\mu_0$ | $|z|>1.960$ |

### Right-tailed test

The entire significance level is placed in the right tail.

$H_a:\mu>\mu_0$

Reject when $z>1.645$ at the 5% significance level.

### Left-tailed test

The entire significance level is placed in the left tail.

$H_a:\mu<\mu_0$

Reject when $z<-1.645$ at the 5% significance level.

### Two-tailed test

The significance level is divided between both tails.

$H_a:\mu\ne\mu_0$

For $\alpha=0.05$, each tail contains $\alpha/2=0.025$.

Reject when $|z|>1.96$.

A one-tailed test must not be selected simply because it makes statistical significance easier to obtain. Its direction must be justified by the research question.

## 12. Type I Error

A **Type I error** occurs when we reject a true null hypothesis.

Symbolically:

$\text{Reject }H_0\text{ when }H_0\text{ is true}$

Its probability is represented by $\alpha$:

$P(\text{Type I error})=\alpha$

For a test using $\alpha=0.05$, the procedure has a 5% Type I error rate under the relevant assumptions.

For example, a medical test might indicate that a treatment has an effect when the null hypothesis of no effect is actually true.

## 13. Type II Error

A **Type II error** occurs when we fail to reject a false null hypothesis.

Symbolically:

$\text{Fail to reject }H_0\text{ when }H_0\text{ is false}$

The probability of a Type II error is denoted by $\beta$:

$P(\text{Type II error})=\beta$

For example, a study might fail to detect a real improvement because its sample is too small or its measurements are too variable.

## 14. Type I and Type II Errors Together

| Reality | Statistical decision | Result |
|---|---|---|
| $H_0$ is true | Reject $H_0$ | Type I error |
| $H_0$ is true | Fail to reject $H_0$ | Correct decision |
| $H_0$ is false | Reject $H_0$ | Correct rejection |
| $H_0$ is false | Fail to reject $H_0$ | Type II error |

The true state of the population is generally unknown, so we cannot know with certainty whether a particular decision is an error.

## 15. Statistical Power

The **power** of a hypothesis test is the probability of correctly rejecting a false null hypothesis.

$Power=1-\beta$

A test with high power is more likely to detect a real difference when one exists.

Power depends on:

- Sample size.
- Effect size.
- Population variability.
- Significance level.
- Whether the test is one-tailed or two-tailed.
- The statistical procedure and its assumptions.

### Factors that increase power

**Larger sample size:** Generally reduces the standard error and makes real differences easier to detect.

**Larger effect size:** A true parameter farther from the null value is easier to distinguish from the null.

**Lower variability:** Less variability can make a real effect easier to detect.

**Higher significance level:** Increasing $\alpha$ generally increases power, but also increases the Type I error rate.

Power calculations are useful when planning sample sizes for experiments, surveys, and machine learning evaluations.

## 16. One-Sample z-Test for a Population Mean

A one-sample z-test is used for a population mean when the population standard deviation $\sigma$ is known and the distributional assumptions for the test are reasonable.

The test statistic is:

$z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$

### Worked example

A company claims that the average delivery time is 30 minutes.

A random sample of 100 deliveries has:

- Sample mean: $\bar{x}=32$ minutes.
- Known population standard deviation: $\sigma=10$ minutes.
- Sample size: $n=100$.
- Significance level: $\alpha=0.05$.

We want to test whether the average delivery time differs from 30 minutes.

### Step 1: State the hypotheses

$H_0:\mu=30$

$H_a:\mu\ne30$

This is a two-tailed test.

### Step 2: Calculate the standard error

$SE=\frac{10}{\sqrt{100}}$

$SE=\frac{10}{10}=1$

### Step 3: Calculate the z-statistic

$z=\frac{32-30}{1}=2$

### Step 4: Compare with the critical values

For a two-tailed test at $\alpha=0.05$, the critical values are approximately $\pm1.96$.

Since $|2|>1.96$, we reject $H_0$.

### Step 5: Interpret the result

There is sufficient statistical evidence at the 5% significance level that the population mean delivery time differs from 30 minutes.

### Python implementation

```python
import numpy as np
from scipy import stats

sample_mean = 32
population_mean = 30
population_sd = 10
sample_size = 100
alpha = 0.05

standard_error = population_sd / np.sqrt(sample_size)
z_statistic = (sample_mean - population_mean) / standard_error

p_value = 2 * stats.norm.sf(abs(z_statistic))
critical_value = stats.norm.ppf(1 - alpha / 2)

print("Standard Error:", standard_error)
print("Z-statistic:", z_statistic)
print("P-value:", p_value)
print("Critical Values:", -critical_value, critical_value)

if p_value <= alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
```

The two-tailed p-value is approximately $0.0455$. Small differences from hand calculations may occur because of rounding.

## 17. Right-Tailed z-Test: Worked Example

A manufacturer claims that a machine produces an average of 100 units per hour. We want to determine whether its true mean production is greater than 100 units.

Given:

$\bar{x}=103,\quad \sigma=12,\quad n=64$

Hypotheses:

$H_0:\mu=100$

$H_a:\mu>100$

Significance level:

$\alpha=0.05$

### Step 1: Calculate the standard error

$SE=\frac{12}{\sqrt{64}}=\frac{12}{8}=1.5$

### Step 2: Calculate the test statistic

$z=\frac{103-100}{1.5}=2$

### Step 3: Compare with the critical value

For a right-tailed test at the 5% level:

$z^*=1.645$

Since $2>1.645$, reject $H_0$.

There is sufficient evidence that the mean production rate is greater than 100 units per hour.

### Python implementation

```python
from scipy import stats
import numpy as np

sample_mean = 103
null_mean = 100
population_sd = 12
n = 64
alpha = 0.05

se = population_sd / np.sqrt(n)
z = (sample_mean - null_mean) / se
p_value = stats.norm.sf(z)

print("Z-statistic:", z)
print("Right-tailed p-value:", p_value)

if p_value <= alpha:
    print("Reject H0: evidence supports a greater mean.")
else:
    print("Fail to reject H0.")
```

## 18. Left-Tailed z-Test: Worked Example

A filling machine is expected to fill bottles with an average of 500 ml. We want to determine whether it is underfilling.

Given:

$\bar{x}=496,\quad \sigma=12,\quad n=36$

Hypotheses:

$H_0:\mu=500$

$H_a:\mu<500$

At $\alpha=0.05$:

$SE=\frac{12}{\sqrt{36}}=2$

$z=\frac{496-500}{2}=-2$

The left-tail critical value is $-1.645$.

Since $-2<-1.645$, reject $H_0$.

There is sufficient statistical evidence that the machine's mean fill amount is below 500 ml.

### Python implementation

```python
from scipy import stats
import numpy as np

sample_mean = 496
null_mean = 500
population_sd = 12
n = 36

se = population_sd / np.sqrt(n)
z = (sample_mean - null_mean) / se
p_value = stats.norm.cdf(z)

print("Z-statistic:", z)
print("Left-tailed p-value:", p_value)
```

## 19. One-Sample t-Test

When the population standard deviation is unknown, a one-sample t-test is commonly used to test a population mean.

The test statistic is:

$t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$

Where:

- $\bar{x}$ = sample mean.
- $\mu_0$ = null-hypothesised mean.
- $s$ = sample standard deviation.
- $n$ = sample size.

Degrees of freedom:

$df=n-1$

The t-distribution accounts for the additional uncertainty introduced by estimating the population standard deviation using the sample.

### Worked example

Suppose a sample of 16 observations has:

$\bar{x}=52,\quad s=8$

We test:

$H_0:\mu=50$

$H_a:\mu\ne50$

At $\alpha=0.05$:

**Step 1: Degrees of freedom**

$df=16-1=15$

**Step 2: Standard error**

$SE=\frac{8}{\sqrt{16}}=2$

**Step 3: Test statistic**

$t=\frac{52-50}{2}=1$

**Step 4: Critical value**

For a two-tailed test with 15 degrees of freedom:

$t^*\approx2.131$

**Step 5: Decision**

Since $|1|<2.131$, fail to reject $H_0$.

There is insufficient statistical evidence at the 5% significance level that the population mean differs from 50.

### Python implementation

```python
from scipy import stats
import numpy as np

sample_mean = 52
null_mean = 50
sample_sd = 8
n = 16
alpha = 0.05

se = sample_sd / np.sqrt(n)
t_statistic = (sample_mean - null_mean) / se
df = n - 1

p_value = 2 * stats.t.sf(abs(t_statistic), df)
critical_value = stats.t.ppf(1 - alpha / 2, df)

print("Standard Error:", se)
print("T-statistic:", t_statistic)
print("Degrees of Freedom:", df)
print("P-value:", p_value)
print("Critical Values:", -critical_value, critical_value)
```

## 20. z-Test vs t-Test

| Feature | z-Test | t-Test |
|---|---|---|
| Standard deviation | Population SD $\sigma$ known | Population SD usually unknown |
| Standard deviation used | $\sigma$ | Sample SD $s$ |
| Reference distribution | Standard normal | t-distribution |
| Degrees of freedom | Not needed for the standard z distribution | Depends on the procedure |
| Common use | Known-$\sigma$ mean tests | Mean tests with unknown $\sigma$ |

The distinction should be based on the available information and assumptions, not simply on whether the sample is small or large.

## 21. Test for a Population Proportion

A one-proportion z-test evaluates a claim about a population proportion.

The sample proportion is:

$\hat{p}=\frac{x}{n}$

Where $x$ is the number of successes and $n$ is the sample size.

Suppose the null hypothesis is:

$H_0:p=p_0$

The standard error under the null hypothesis is:

$SE_0=\sqrt{\frac{p_0(1-p_0)}{n}}$

The test statistic is:

$z=\frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$

Notice that the denominator uses the null proportion $p_0$, rather than the observed sample proportion $\hat{p}$.

For the normal approximation, the expected numbers of successes and failures under the null are commonly checked:

$np_0\ge10$

$n(1-p_0)\ge10$

These are common guidelines, not universal guarantees. Exact methods may be preferable for small samples or extreme proportions.

### Worked example

A company claims that 60% of its customers are satisfied.

A sample of 200 customers contains 140 satisfied customers.

Therefore:

$\hat{p}=\frac{140}{200}=0.70$

Hypotheses:

$H_0:p=0.60$

$H_a:p\ne0.60$

At $\alpha=0.05$:

**Step 1: Calculate the null standard error**

$SE_0=\sqrt{\frac{0.60(1-0.60)}{200}}$

$SE_0=\sqrt{0.0012}\approx0.03464$

**Step 2: Calculate the test statistic**

$z=\frac{0.70-0.60}{0.03464}\approx2.89$

**Step 3: Make the decision**

The absolute test statistic exceeds 1.96, so reject $H_0$.

There is sufficient statistical evidence that the population customer satisfaction proportion differs from 60%.

### Python implementation

```python
from scipy import stats
import numpy as np

successes = 140
n = 200
p0 = 0.60
alpha = 0.05

sample_proportion = successes / n
se_null = np.sqrt(p0 * (1 - p0) / n)

z = (sample_proportion - p0) / se_null
p_value = 2 * stats.norm.sf(abs(z))

print("Sample Proportion:", sample_proportion)
print("Null Standard Error:", se_null)
print("Z-statistic:", z)
print("P-value:", p_value)
```

## 22. Hypothesis Test for a Difference Between Two Means

When comparing two population means, we may test whether the difference between them equals zero.

Hypotheses:

$H_0:\mu_1-\mu_2=0$

$H_a:\mu_1-\mu_2\ne0$

For two independent samples with unknown population variances, Welch's t-test is commonly used.

Its estimated standard error is:

$SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$

The test statistic is:

$t=\frac{(\bar{x}_1-\bar{x}_2)-0}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}}$

Welch's test uses an estimated degrees-of-freedom calculation that accounts for the sample sizes and sample variances.

### Worked example

Suppose the following results are obtained:

| Group | Mean | Standard deviation | Sample size |
|---|---:|---:|---:|
| Group 1 | 82 | 10 | 100 |
| Group 2 | 78 | 12 | 144 |

The estimated difference is:

$82-78=4$

The standard error is:

$SE=\sqrt{\frac{10^2}{100}+\frac{12^2}{144}}$

$SE=\sqrt{1+1}=\sqrt{2}\approx1.414$

The test statistic is approximately:

$t=\frac{4}{1.414}\approx2.83$

This indicates evidence against the null hypothesis under the test assumptions. The formal p-value should be calculated using the appropriate Welch degrees of freedom.

### Python implementation

```python
from scipy import stats

group1 = [80, 85, 78, 84, 83, 82, 79, 86]
group2 = [75, 80, 77, 79, 81, 76, 78, 74]

result = stats.ttest_ind(
    group1,
    group2,
    equal_var=False,
    alternative="two-sided"
)

print("T-statistic:", result.statistic)
print("P-value:", result.pvalue)
```

The example data are illustrative. Replace them with the actual observations for a real analysis.

## 23. Hypothesis Test for the Difference Between Two Proportions

Suppose we want to compare two population proportions.

The null hypothesis is:

$H_0:p_1-p_2=0$

The sample proportions are:

$\hat{p}_1=\frac{x_1}{n_1}$

$\hat{p}_2=\frac{x_2}{n_2}$

Under the null hypothesis of equal proportions, the pooled proportion is:

$\hat{p}_{\text{pooled}}=\frac{x_1+x_2}{n_1+n_2}$

The null standard error is:

$SE_0=\sqrt{\hat{p}_{\text{pooled}}(1-\hat{p}_{\text{pooled}})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}$

The test statistic is:

$z=\frac{\hat{p}_1-\hat{p}_2}{SE_0}$

This pooled standard error is used for the standard test of equal proportions. It is different from the unpooled standard error commonly used for a confidence interval estimating the difference between two proportions.

### Python implementation

```python
from statsmodels.stats.proportion import proportions_ztest

successes = [140, 120]
sample_sizes = [200, 200]

z_statistic, p_value = proportions_ztest(
    count=successes,
    nobs=sample_sizes,
    alternative="two-sided"
)

print("Z-statistic:", z_statistic)
print("P-value:", p_value)
```

The test compares the observed proportions with the null hypothesis that the population proportions are equal.

## 24. Paired t-Test

A paired t-test is appropriate when observations are naturally matched, such as:

- Before-and-after measurements on the same people.
- Measurements from matched subjects.
- Repeated measurements on the same experimental unit.

Paired observations should not automatically be treated as independent samples.

For each pair, calculate the difference:

$d_i=After_i-Before_i$

Let $\bar{d}$ be the mean of the differences and $s_d$ be their sample standard deviation.

The paired t-statistic is:

$t=\frac{\bar{d}-\mu_{d,0}}{s_d/\sqrt{n}}$

The usual null hypothesis is:

$H_0:\mu_d=0$

with degrees of freedom:

$df=n-1$

A paired t-test is therefore equivalent to a one-sample t-test applied to the within-pair differences.

### Python implementation

```python
from scipy import stats

before = [70, 75, 80, 65, 90, 72, 68, 85]
after = [75, 78, 83, 70, 94, 76, 72, 88]

result = stats.ttest_rel(
    after,
    before,
    alternative="two-sided"
)

print("T-statistic:", result.statistic)
print("P-value:", result.pvalue)
```

The paired measurements must be in matching order: each value in `before` should correspond to the same subject or unit in `after`.

## 25. Interpreting the p-Value Correctly

Suppose a hypothesis test produces:

$p=0.003$

with:

$\alpha=0.05$

Since $0.003<0.05$, we reject the null hypothesis.

A suitable interpretation is:

> The observed data provide strong statistical evidence against the null hypothesis at the 5% significance level.

A p-value is not:

- The probability that the null hypothesis is true.
- The probability that the alternative hypothesis is true.
- The probability that the result happened purely by chance.
- A measure of the effect size.
- The probability that the conclusion is wrong.

A p-value describes the extremeness of the observed data under the null model and the assumptions of the chosen test.

## 26. Statistical Significance vs Practical Significance

A result is statistically significant at level $\alpha$ when:

$p\le\alpha$

However, statistical significance does not automatically mean that an effect is important in practice.

For example, a very large dataset might detect a mean difference of only 0.01 with a very small p-value. Whether that difference matters depends on the application.

A complete analysis should consider:

- The estimated effect size.
- The uncertainty around the estimate.
- The p-value and significance level.
- The assumptions of the test.
- The practical context.

Whenever possible, report the estimated effect and its confidence interval alongside the hypothesis test.

## 27. Confidence Intervals and Hypothesis Tests

Confidence intervals and two-sided hypothesis tests are closely related.

For many standard procedures, a 95% confidence interval corresponds to a two-sided test at:

$\alpha=0.05$

Suppose we test:

$H_0:\mu=50$

If the corresponding 95% confidence interval does not contain 50, the two-sided test rejects $H_0$ at the 5% level.

If the interval contains 50, the test fails to reject $H_0$.

This relationship applies when the confidence interval and hypothesis test use matching procedures and assumptions.

A confidence interval provides additional information because it shows the range of parameter values compatible with the data under the method.

## 28. Assumptions for a One-Sample Mean Test

A one-sample mean test requires attention to the following assumptions.

### Random sampling

The sample should be collected in a way that supports inference about the target population.

### Independence

Observations should be independent when the chosen procedure assumes independence.

### Distributional shape

For small samples, the population distribution should be reasonably close to normal, especially when using the t procedure.

For larger samples, the sampling distribution of the mean may be approximately normal under suitable conditions. A large sample does not automatically eliminate every problem caused by extreme skewness, dependence, or outliers.

### Outliers

Extreme observations can strongly affect the sample mean, standard deviation, and t-statistic.

Assumptions should be evaluated rather than automatically assumed.

## 29. Assumptions for a Proportion Test

For the normal approximation in a one-proportion z-test, common checks under the null hypothesis are:

$np_0\ge10$

$n(1-p_0)\ge10$

These conditions help assess whether the normal approximation is reasonable.

When the sample is small or the proportion is close to zero or one, an exact binomial test or another suitable method may be preferable.

## 30. Multiple Testing

When many hypothesis tests are conducted, the probability of obtaining at least one false-positive result can increase.

For example, if many independent tests are each performed at $\alpha=0.05$, some tests may produce small p-values even when their null hypotheses are true.

Methods for handling multiple comparisons include:

- Bonferroni correction.
- Holm procedure.
- False discovery rate procedures.

These methods address different goals and should be selected according to the analysis.

The important principle is that **performing more tests creates more opportunities for false-positive findings**.

## 31. Reporting a Hypothesis Test

A clear statistical report should include:

1. The null and alternative hypotheses.
2. The test used.
3. The test statistic.
4. The degrees of freedom, when applicable.
5. The p-value.
6. The significance level.
7. The statistical decision.
8. A conclusion in the original context.
9. An estimate and confidence interval when relevant.

Example:

> A one-sample t-test was conducted to evaluate whether the population mean differs from 50. The test produced $t=2.50$ with 35 degrees of freedom. At $\alpha=0.05$, the null hypothesis was rejected, providing evidence that the population mean differs from 50.

Reporting only "the result is significant" does not provide enough information to understand the analysis.

## 32. Quick Test Selection Guide

| Statistical question | Common test |
|---|---|
| One population mean, known $\sigma$ | One-sample z-test |
| One population mean, unknown $\sigma$ | One-sample t-test |
| One population proportion | One-proportion z-test, when approximation conditions are met |
| Two independent population means | Two-sample t-test, often Welch's test |
| Before-and-after measurements | Paired t-test |
| Two independent proportions | Two-proportion z-test |
| Several population means | ANOVA |
| Association between categorical variables | Chi-square test of independence |

The appropriate test depends on the data structure, research question, and assumptions. ANOVA, chi-square tests, correlation tests, and regression inference should be studied in their respective chapters.

## 33. Important Formula Summary

### One-sample z-statistic for a mean

$z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$

### One-sample t-statistic

$t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$

Degrees of freedom:

$df=n-1$

### Sample proportion

$\hat{p}=\frac{x}{n}$

### One-proportion z-statistic

$z=\frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$

### Standard error for the difference between two independent means

$SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$

### Pooled proportion

$\hat{p}_{\text{pooled}}=\frac{x_1+x_2}{n_1+n_2}$

### Standard error for the difference between two proportions under the null

$SE_0=\sqrt{\hat{p}_{\text{pooled}}(1-\hat{p}_{\text{pooled}})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}$

### Paired t-statistic

$t=\frac{\bar{d}-\mu_{d,0}}{s_d/\sqrt{n}}$

### Type I error probability

$P(\text{Type I error})=\alpha$

### Type II error probability

$P(\text{Type II error})=\beta$

### Statistical power

$Power=1-\beta$

### p-value decision rule

$p\le\alpha\Rightarrow\text{Reject }H_0$

$p>\alpha\Rightarrow\text{Fail to reject }H_0$

## 34. Python Practice Exercises

Try solving the following exercises using Python, NumPy, and SciPy.

### Exercise 1: Two-tailed z-test

A population has a known standard deviation of 8. A random sample of 64 observations has a mean of 103. Test whether the population mean differs from 100 at $\alpha=0.05$.

Calculate:

- The standard error.
- The z-statistic.
- The p-value.
- The final decision.

### Exercise 2: One-sample t-test

A sample contains 25 observations with a mean of 52 and a sample standard deviation of 10. Test whether the population mean differs from 50 at the 5% significance level.

Calculate the t-statistic, degrees of freedom, and p-value.

### Exercise 3: One-proportion test

A company claims that 50% of customers prefer its product. In a sample of 200 customers, 115 prefer the product.

Test whether the population proportion differs from 0.50 at $\alpha=0.05$.

Check the normal approximation conditions before interpreting the result.

### Exercise 4: Independent samples

Two independent groups provide measurements of a performance score. Use Welch's t-test to evaluate whether their population means differ.

Explain why treating paired observations as independent would be inappropriate if the measurements actually came from the same individuals.

### Exercise 5: Paired observations

Record measurements before and after a training programme for the same group of participants. Use a paired t-test to test whether the mean change differs from zero.

Explain the meaning of the sign of the estimated mean difference.

### Exercise 6: Interpret p-values

For each p-value below, make a decision at $\alpha=0.05$:

- $p=0.001$
- $p=0.03$
- $p=0.05$
- $p=0.08$
- $p=0.20$

Explain why failing to reject the null hypothesis does not prove that it is true.

## 35. Points to Remember

1. A statistical hypothesis is a claim about a population parameter or distribution.
2. The null hypothesis is written as $H_0$.
3. The alternative hypothesis is written as $H_a$ or $H_1$.
4. The null hypothesis normally contains the equality in ordinary hypothesis tests.
5. The alternative hypothesis determines whether the test is one-tailed or two-tailed.
6. The significance level $\alpha$ should be selected before examining the result.
7. A p-value is calculated under the assumption that the null hypothesis is true.
8. A small p-value provides evidence against the null hypothesis.
9. Reject $H_0$ when $p\le\alpha$ under the standard decision rule.
10. If $p>\alpha$, fail to reject $H_0$.
11. Failing to reject $H_0$ does not prove that it is true.
12. A Type I error means rejecting a true null hypothesis.
13. A Type II error means failing to reject a false null hypothesis.
14. Statistical power is $1-\beta$.
15. A one-sample z-test for a mean uses a known population standard deviation.
16. A one-sample t-test commonly uses the sample standard deviation when the population standard deviation is unknown.
17. For a one-sample t-test, the degrees of freedom are $n-1$.
18. A one-proportion z-test uses the null proportion in its standard error.
19. Welch's t-test is commonly used to compare independent means when population variances are unknown and may differ.
20. A paired t-test analyses the differences within matched pairs.
21. Statistical significance does not automatically imply practical importance.
22. A p-value is not the probability that the null hypothesis is true.
23. Confidence intervals and two-sided hypothesis tests are closely related.
24. Assumptions must be checked before interpreting results.
25. A complete report should explain the result in the context of the original research question.

## 36. Chapter Summary

Hypothesis testing provides a formal framework for evaluating population claims using sample evidence.

The process begins by identifying the population parameter and translating the research question into a null hypothesis and an alternative hypothesis. The significance level defines the decision threshold, while the test statistic measures the difference between the observed result and the null value relative to its standard error.

The p-value describes how unusual the observed statistic, or a more extreme one, would be under the null hypothesis and the assumptions of the test.

The standard decision rules are:

$p\le\alpha\Rightarrow\text{Reject }H_0$

$p>\alpha\Rightarrow\text{Fail to reject }H_0$

A Type I error occurs when a true null hypothesis is rejected, while a Type II error occurs when a false null hypothesis is not rejected. The power of a test is:

$Power=1-\beta$

For population means, a z-test is used in the known-population-standard-deviation setting, while a t-test is commonly used when that standard deviation is unknown. Proportion tests use appropriate normal approximations when their conditions are satisfied. Two-sample and paired tests require careful attention to the relationship between observations.

A sound statistical analysis does not rely on the p-value alone. It also considers the estimated effect, uncertainty, assumptions, and practical context.

The complete process can be summarised as:

**Research question → Hypotheses → Significance level → Test statistic → p-value or critical value → Decision → Contextual conclusion**

## 37. References

1. OpenStax, *Introductory Statistics*. https://openstax.org/details/books/introductory-statistics
2. NIST/SEMATECH, *e-Handbook of Statistical Methods*. https://www.itl.nist.gov/div898/handbook/
3. Penn State Eberly College of Science, *STAT Online*. https://online.stat.psu.edu/
4. Montgomery, D. C., and Runger, G. C., *Applied Statistics and Probability for Engineers*.
5. Casella, G., and Berger, R. L., *Statistical Inference*.
6. SciPy Documentation, *Statistical Functions*. https://docs.scipy.org/doc/scipy/reference/stats.html
7. Statsmodels Documentation, *Proportion Tests*. https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportions_ztest.html

---

### Python libraries used in this chapter

Install the required packages using:

```bash
pip install numpy scipy statsmodels
```

- **NumPy:** Numerical calculations and square roots.
- **SciPy:** Probability distributions, p-values, z-test calculations, and t-tests.
- **Statsmodels:** Statistical tests for population proportions and other inferential procedures.
