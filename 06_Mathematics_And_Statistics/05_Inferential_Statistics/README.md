# Inferential Statistics

## Introduction to Inferential Statistics

**Inferential Statistics** is the branch of statistics used to draw conclusions about a population using information collected from a sample.

Descriptive statistics summarises the data we already have. Inferential statistics goes further by using sample data to estimate population parameters, quantify uncertainty, construct confidence intervals, and support statistical decisions.

For example, a university may have 20,000 students. Instead of measuring the study time of every student, we can select 500 students, calculate their average study time, and use that result to estimate the average for all students.

Different samples may produce different results. Inferential statistics helps us understand and quantify this sampling uncertainty.

### What This Chapter Covers

- Population, sample, parameter, and statistic
- Sampling methods and sampling variability
- Sampling distributions and standard error
- Point estimation and estimator properties
- Confidence intervals and margin of error
- Confidence intervals for means and proportions
- Sample-size determination
- Finite population correction
- Bootstrap confidence intervals
- Practical implementation using Python

---

## 1. Population and Sample

A **population** is the complete group about which we want to draw conclusions.

A **sample** is a subset selected from that population.

For example, if a university has 20,000 students and we survey 500 students:

- Population: all 20,000 students.
- Sample: the 500 selected students.
- Population mean: the actual average study time of all students.
- Sample mean: the average study time calculated from the 500 students.

A population parameter is often unknown, whereas a sample statistic can be calculated from observed data.

## 2. Parameter and Statistic

A **parameter** describes a population, while a **statistic** describes a sample.

| Population parameter | Sample statistic |
|---|---|
| Population mean, $\mu$ | Sample mean, $\bar{x}$ |
| Population variance, $\sigma^2$ | Sample variance, $s^2$ |
| Population standard deviation, $\sigma$ | Sample standard deviation, $s$ |
| Population proportion, $p$ | Sample proportion, $\hat{p}$ |

For example, if the average study time of a sample is 4.8 hours, then $\bar{x}=4.8$ is a statistic used to estimate the unknown population mean $\mu$.

### Python Implementation

```python
import numpy as np

study_hours = np.array([3, 4, 5, 6, 4, 5, 3, 8, 6, 4])

sample_mean = np.mean(study_hours)
sample_sd = np.std(study_hours, ddof=1)

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_sd)
```

The sample mean and standard deviation describe the observed sample. They do not automatically equal the corresponding population values.

## 3. Sampling Methods

The method used to select a sample affects how reliably the results represent the target population.

### 3.1 Simple Random Sampling

Every population member has an equal chance of selection.

**Example:** Randomly selecting 500 students from a university database.

### 3.2 Stratified Sampling

The population is divided into meaningful groups called *strata*. Samples are then selected from these groups.

**Example:** Dividing students by academic year and selecting students from each year.

Stratified sampling can help ensure representation of important subgroups.

### 3.3 Systematic Sampling

Observations are selected at regular intervals after choosing an appropriate starting point.

**Example:** Selecting every 20th customer from a list after choosing a random starting position.

### 3.4 Cluster Sampling

The population is divided into natural groups called *clusters*. Some clusters are selected, and observations within those clusters are studied.

**Example:** Randomly selecting several colleges and surveying students in those colleges.

### 3.5 Convenience Sampling

Observations are selected because they are easy to access.

**Example:** Surveying people near a particular shop.

Convenience sampling can introduce selection bias and should not automatically be treated as representative.

**Important:** A large sample does not automatically eliminate bias. The sampling design and quality of the data also matter.

## 4. Sampling Variability and Sampling Distribution

Different random samples from the same population usually contain different observations. Consequently, their statistics can differ. This variation is called **sampling variability**.

A **sampling distribution** is the probability distribution of a statistic across repeated samples of the same size from a population.

For example, imagine repeatedly selecting samples of 100 students and calculating the mean study time for each sample. The distribution of these sample means is the sampling distribution of the sample mean.

A sampling distribution describes the behaviour of a statistic, not the distribution of individual observations.

For independent observations with population mean $\mu$ and finite population variance $\sigma^2$:

$$
E(\bar{X})=\mu
$$

$$
\mathrm{Var}(\bar{X})=\frac{\sigma^2}{n}
$$

The standard deviation of the sampling distribution is called the **standard error**:

$$
SE(\bar{X})=\frac{\sigma}{\sqrt{n}}
$$

Here, $n$ is the sample size.

## 5. Standard Error

The **standard error (SE)** measures the sampling variability of an estimate.

For the sample mean, when the population standard deviation is known:

$$
SE(\bar{x})=\frac{\sigma}{\sqrt{n}}
$$

When the population standard deviation is unknown, we commonly estimate the standard error using the sample standard deviation:

$$
SE(\bar{x})=\frac{s}{\sqrt{n}}
$$

### Worked Example

Suppose the population standard deviation is 12.

For a sample size of 36:

$$
SE=\frac{12}{\sqrt{36}}=\frac{12}{6}=2
$$

For a sample size of 144:

$$
SE=\frac{12}{\sqrt{144}}=\frac{12}{12}=1
$$

The sample size becomes four times larger, while the standard error becomes half as large.

### Standard Deviation vs Standard Error

| Standard deviation | Standard error |
|---|---|
| Measures the spread of observations | Measures sampling variability of an estimate |
| Describes variation in the observed data | Describes uncertainty in a statistic |
| Does not automatically decrease when sample size increases | Usually decreases as sample size increases |
| Expressed in the measurement units of the data | Expressed in the units of the statistic |

### Python Implementation

```python
import numpy as np

population_sd = 12

for n in [36, 144, 576]:
    standard_error = population_sd / np.sqrt(n)
    print(f"Sample size: {n}, SE: {standard_error:.4f}")
```

## 6. Sampling Distribution of a Sample Proportion

A **sample proportion** estimates the proportion of a population that has a particular characteristic.

The formula is:

$$
\hat{p}=\frac{x}{n}
$$

where:

- $x$ is the number of observations with the characteristic.
- $n$ is the sample size.
- $\hat{p}$ is the observed sample proportion.

Under independent Bernoulli sampling:

$$
E(\hat{p})=p
$$

$$
\mathrm{Var}(\hat{p})=\frac{p(1-p)}{n}
$$

The standard deviation of the sampling distribution is:

$$
SD(\hat{p})=\sqrt{\frac{p(1-p)}{n}}
$$

When the population proportion is unknown, its estimated standard error is:

$$
SE(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

### Worked Example

Suppose 120 out of 200 customers prefer Product A.

$$
\hat{p}=\frac{120}{200}=0.60
$$

The estimated proportion is 60%.

The estimated standard error is:

$$
SE(\hat{p})=\sqrt{\frac{0.60(1-0.60)}{200}}
$$

$$
SE(\hat{p})\approx0.0346
$$

### Python Implementation

```python
import numpy as np

successes = 120
n = 200

p_hat = successes / n
standard_error = np.sqrt(p_hat * (1 - p_hat) / n)

print("Sample proportion:", p_hat)
print("Percentage:", p_hat * 100)
print("Estimated standard error:", standard_error)
```

## 7. Point Estimation

A **point estimate** is a single numerical value used to estimate an unknown population parameter.

Examples include:

- $\bar{x}$ estimates the population mean $\mu$.
- $\hat{p}$ estimates the population proportion $p$.
- $s^2$ estimates the population variance $\sigma^2$.

Suppose a sample of students has an average study time of 4.8 hours per day. The point estimate of the population mean is 4.8 hours.

A point estimate gives one value but does not directly communicate how uncertain that estimate is. Confidence intervals provide additional information.

### Estimator vs Estimate

An **estimator** is a statistic or rule used to estimate a population parameter. An **estimate** is the numerical value obtained after applying that estimator to a particular sample.

The sample mean estimator is:

$$
\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

If a particular sample produces $\bar{x}=72.4$, then 72.4 is the estimate.

## 8. Properties of a Good Estimator

Three important properties used to compare estimators are unbiasedness, consistency, and efficiency.

### 8.1 Unbiasedness

An estimator $\hat{\theta}$ is unbiased for a parameter $\theta$ if its expected value equals the true parameter:

$$
E(\hat{\theta})=\theta
$$

The sample mean is an unbiased estimator of the population mean under the usual sampling assumptions:

$$
E(\bar{X})=\mu
$$

Unbiasedness does not mean that every estimate equals the true parameter. It means that the estimator is correct on average across repeated samples.

### 8.2 Bias

The bias of an estimator is:

$$
Bias(\hat{\theta})=E(\hat{\theta})-\theta
$$

Suppose an estimator has expected value 52 when the true parameter is 50.

$$
Bias(\hat{\theta})=52-50=2
$$

The estimator has an upward bias of 2.

### 8.3 Consistency

An estimator is **consistent** if it approaches the true parameter as the sample size increases.

The notation is:

$$
\hat{\theta}_n\xrightarrow{P}\theta
$$

This represents convergence in probability to the true parameter.

An estimator can be biased for finite samples and still be consistent.

### 8.4 Efficiency

When comparing unbiased estimators of the same parameter, the estimator with smaller variance is generally considered more efficient.

Suppose:

$$
\mathrm{Var}(\hat{\theta}_1)=4
$$

$$
\mathrm{Var}(\hat{\theta}_2)=9
$$

Estimator 1 has lower variance and therefore greater precision under this comparison.

**Remember:** Unbiasedness concerns correctness on average, consistency concerns behaviour as sample size grows, and efficiency concerns variability relative to alternative estimators.

## 9. Confidence Intervals

A **confidence interval (CI)** is an interval estimate constructed from sample data to estimate a population parameter.

Instead of reporting only a sample mean of 72, we might report an interval from 68 to 76.

A common structure is:

$$
CI=\text{Point Estimate}\pm\text{Margin of Error}
$$

For many standard intervals:

$$
ME=\text{Critical Value}\times SE
$$

Therefore:

$$
CI=\text{Estimate}\pm\text{Critical Value}\times SE
$$

A confidence interval communicates both an estimate and its uncertainty.

## 10. Confidence Level and Critical Values

Common confidence levels include 90%, 95%, and 99%.

A 95% confidence procedure means that if the same valid sampling procedure were repeated many times and an interval constructed each time, approximately 95% of those intervals would contain the fixed population parameter.

It does not mean that a fixed parameter has a 95% probability of lying inside one already-calculated frequentist confidence interval.

For a standard Normal distribution, common two-sided critical values are:

| Confidence level | Critical value |
|---|---:|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

A higher confidence level generally produces a wider interval when other factors remain constant.

### Python Implementation

```python
from scipy.stats import norm

for confidence in [0.90, 0.95, 0.99]:
    alpha = 1 - confidence
    z_critical = norm.ppf(1 - alpha / 2)

    print(
        f"Confidence: {confidence:.0%}, "
        f"z critical: {z_critical:.3f}"
    )
```

## 11. Confidence Interval for a Population Mean When Population SD Is Known

When the population standard deviation $\sigma$ is known, a standard confidence interval for the population mean is:

$$
\bar{x}\pm z^*\frac{\sigma}{\sqrt{n}}
$$

where:

- $\bar{x}$ is the sample mean.
- $z^*$ is the Normal critical value.
- $\sigma$ is the population standard deviation.
- $n$ is the sample size.

### Worked Example

Suppose:

- Sample mean = 72
- Population standard deviation = 10
- Sample size = 100
- Confidence level = 95%

The critical value is $z^*=1.96$.

Calculate the standard error:

$$
SE=\frac{10}{\sqrt{100}}=1
$$

Calculate the margin of error:

$$
ME=1.96(1)=1.96
$$

Therefore:

$$
CI=72\pm1.96
$$

$$
CI=(70.04,\ 73.96)
$$

### Python Implementation

```python
from scipy.stats import norm

sample_mean = 72
population_sd = 10
n = 100
confidence = 0.95

z_critical = norm.ppf(1 - (1 - confidence) / 2)
standard_error = population_sd / (n ** 0.5)
margin_of_error = z_critical * standard_error

lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error

print("Standard error:", standard_error)
print("Margin of error:", margin_of_error)
print("Confidence interval:", (lower, upper))
```

## 12. Confidence Interval for a Population Mean When Population SD Is Unknown

In most real-world situations, the population standard deviation is unknown. We estimate it using the sample standard deviation $s$ and commonly use the **t-distribution**.

The interval is:

$$
\bar{x}\pm t^*\frac{s}{\sqrt{n}}
$$

For a standard one-sample t interval, the degrees of freedom are:

$$
df=n-1
$$

The t-distribution has heavier tails than the standard Normal distribution, particularly for small samples. It approaches the standard Normal distribution as the degrees of freedom increase.

### Worked Example

Suppose:

- $\bar{x}=50$
- $s=8$
- $n=16$
- Confidence level = 95%

Degrees of freedom:

$$
df=16-1=15
$$

The two-sided critical value is approximately $t^*=2.131$.

Standard error:

$$
SE=\frac{8}{\sqrt{16}}=2
$$

Margin of error:

$$
ME=2.131(2)=4.262
$$

Confidence interval:

$$
CI=50\pm4.262
$$

$$
CI\approx(45.738,\ 54.262)
$$

### Python Implementation

```python
from scipy.stats import t

sample_mean = 50
sample_sd = 8
n = 16
confidence = 0.95

df = n - 1
t_critical = t.ppf(1 - (1 - confidence) / 2, df)

standard_error = sample_sd / (n ** 0.5)
margin_of_error = t_critical * standard_error

lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error

print("Degrees of freedom:", df)
print("Standard error:", standard_error)
print("Confidence interval:", (lower, upper))
```

The usual one-sample t interval assumes independent observations and is exact under a Normal population model. Strong skewness or influential outliers may affect its suitability.

## 13. Confidence Interval for a Population Proportion

A common large-sample confidence interval for a population proportion is:

$$
\hat{p}\pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

Suppose 120 out of 200 customers prefer Product A.

$$
\hat{p}=\frac{120}{200}=0.60
$$

For 95% confidence, $z^*=1.96$.

The estimated standard error is:

$$
SE=\sqrt{\frac{0.60(0.40)}{200}}\approx0.0346
$$

The margin of error is approximately:

$$
ME=1.96(0.0346)\approx0.0678
$$

Therefore:

$$
CI=0.60\pm0.0678
$$

$$
CI\approx(0.5322,\ 0.6678)
$$

The estimated proportion is 60%, with an approximate interval of 53.2% to 66.8%.

The basic Normal approximation is more suitable when the sample is sufficiently large. A common check is:

$$
n\hat{p}\geq10
$$

$$
n(1-\hat{p})\geq10
$$

For small samples or proportions close to 0 or 1, a Wilson interval may perform better than the basic Wald interval.

### Python Implementation

```python
from statsmodels.stats.proportion import proportion_confint

successes = 120
n = 200

lower, upper = proportion_confint(
    count=successes,
    nobs=n,
    alpha=0.05,
    method="wilson"
)

print("Sample proportion:", successes / n)
print("95% Wilson confidence interval:", (lower, upper))
```

Install the dependency if necessary:

```bash
pip install statsmodels
```

This implementation uses the Wilson interval, which differs from the simple Normal-approximation formula above.

## 14. Confidence Interval for the Difference Between Two Means

When comparing two independent groups, we may want to estimate the difference between their population means:

$$
\mu_1-\mu_2
$$

An estimated standard error is:

$$
SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

A general confidence interval is:

$$
(\bar{x}_1-\bar{x}_2)\pm\text{Critical Value}\times SE
$$

When population standard deviations are unknown and unequal variances are plausible, **Welch's t interval** is commonly used.

### Worked Example

Suppose:

| Group | Mean | SD | Sample size |
|---|---:|---:|---:|
| Group 1 | 82 | 10 | 100 |
| Group 2 | 78 | 12 | 144 |

Difference between sample means:

$$
\bar{x}_1-\bar{x}_2=82-78=4
$$

Estimated standard error:

$$
SE=\sqrt{\frac{10^2}{100}+\frac{12^2}{144}}
$$

$$
SE=\sqrt{2}\approx1.414
$$

Using 1.96 as an illustrative large-sample Normal critical value:

$$
ME=1.96(1.414)\approx2.77
$$

The illustrative interval is:

$$
CI=4\pm2.77
$$

$$
CI\approx(1.23,\ 6.77)
$$

For formal inference with unknown population standard deviations, use an appropriate t-based interval.

### Python Implementation: Welch's t Interval

```python
import numpy as np
from scipy.stats import t

mean1, sd1, n1 = 82, 10, 100
mean2, sd2, n2 = 78, 12, 144

difference = mean1 - mean2

v1 = sd1**2 / n1
v2 = sd2**2 / n2
se = np.sqrt(v1 + v2)

df = (v1 + v2)**2 / (
    v1**2 / (n1 - 1) + v2**2 / (n2 - 1)
)

critical = t.ppf(0.975, df)

lower = difference - critical * se
upper = difference + critical * se

print("Mean difference:", difference)
print("Standard error:", se)
print("Degrees of freedom:", df)
print("95% Welch confidence interval:", (lower, upper))
```

## 15. Confidence Interval for the Difference Between Two Proportions

For two independent groups, the estimated difference between sample proportions is:

$$
\hat{p}_1-\hat{p}_2
$$

A common large-sample standard error is:

$$
SE=\sqrt{
\frac{\hat{p}_1(1-\hat{p}_1)}{n_1}
+
\frac{\hat{p}_2(1-\hat{p}_2)}{n_2}
}
$$

The approximate confidence interval is:

$$
(\hat{p}_1-\hat{p}_2)\pm z^*SE
$$

### Worked Example

Suppose Group 1 has 60 successes out of 100 and Group 2 has 45 successes out of 100.

$$
\hat{p}_1=0.60
$$

$$
\hat{p}_2=0.45
$$

The difference is:

$$
\hat{p}_1-\hat{p}_2=0.15
$$

The estimated standard error is:

$$
SE=\sqrt{\frac{0.60(0.40)}{100}+\frac{0.45(0.55)}{100}}
$$

$$
SE\approx0.0698
$$

For 95% confidence:

$$
ME=1.96(0.0698)\approx0.1368
$$

Therefore:

$$
CI=0.15\pm0.1368
$$

$$
CI\approx(0.0132,\ 0.2868)
$$

The estimated difference is 15 percentage points. The interval describes the uncertainty in that difference under the large-sample approximation.

## 16. Margin of Error and Confidence Interval Width

The **margin of error** is the amount added to and subtracted from a point estimate to form a symmetric confidence interval.

For a mean with known population standard deviation:

$$
ME=z^*\frac{\sigma}{\sqrt{n}}
$$

For a mean using the t-distribution:

$$
ME=t^*\frac{s}{\sqrt{n}}
$$

For a proportion using the basic Normal approximation:

$$
ME=z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

The width of a confidence interval is:

$$
\text{Width}=\text{Upper Limit}-\text{Lower Limit}
$$

For a symmetric interval:

$$
ME=\frac{\text{Width}}{2}
$$

Three major factors affect the margin of error:

1. **Confidence level:** Higher confidence generally produces a larger margin of error.
2. **Sample size:** Larger samples generally reduce the margin of error.
3. **Variability:** Greater variability generally increases the margin of error.

These relationships assume other relevant factors remain fixed.

## 17. Sample Size for Estimating a Population Mean

Suppose we want to estimate a population mean with a margin of error no greater than $E$.

Using a Normal critical value and a known or planning estimate of the population standard deviation:

$$
n=\left(\frac{z^*\sigma}{E}\right)^2
$$

### Worked Example

Suppose:

- $\sigma=12$
- Desired margin of error $E=2$
- 95% confidence, so $z^*=1.96$

Then:

$$
n=\left(\frac{1.96(12)}{2}\right)^2
$$

$$
n=138.2976
$$

The sample size must be rounded upward:

$$
n=139
$$

At least 139 observations are required under these planning assumptions.

### Python Implementation

```python
import numpy as np
from scipy.stats import norm

population_sd = 12
margin_of_error = 2
confidence = 0.95

z_critical = norm.ppf(1 - (1 - confidence) / 2)

n_required = (
    z_critical * population_sd / margin_of_error
) ** 2

print("Unrounded sample size:", n_required)
print("Required sample size:", int(np.ceil(n_required)))
```

## 18. Sample Size for Estimating a Population Proportion

A common planning formula for a population proportion is:

$$
n=\frac{(z^*)^2p(1-p)}{E^2}
$$

where:

- $p$ is the anticipated population proportion.
- $E$ is the desired margin of error.
- $z^*$ is the critical value.

If the population proportion is unknown, a conservative choice is:

$$
p=0.5
$$

This maximises $p(1-p)$ and gives the largest required sample size for the specified confidence level and margin of error.

### Worked Example

Suppose we want 95% confidence and a margin of error of 0.05.

Use $z^*=1.96$ and $p=0.5$.

$$
n=\frac{(1.96)^2(0.5)(0.5)}{(0.05)^2}
$$

$$
n=384.16
$$

Rounding upward gives:

$$
n=385
$$

### Python Implementation

```python
import numpy as np
from scipy.stats import norm

confidence = 0.95
margin_of_error = 0.05
p = 0.5

z_critical = norm.ppf(1 - (1 - confidence) / 2)

n_required = (
    z_critical**2 * p * (1 - p)
    / margin_of_error**2
)

print("Unrounded sample size:", n_required)
print("Required sample size:", int(np.ceil(n_required)))
```

These calculations assume an appropriate sampling design and do not automatically account for nonresponse, clustering, or other design effects.

## 19. Point Estimate vs Interval Estimate

| Point estimate | Interval estimate |
|---|---|
| Gives one numerical value | Gives a range of values |
| Easy to communicate | Communicates uncertainty |
| Example: $\bar{x}=72$ | Example: 95% CI from 70 to 74 |
| Does not directly show sampling uncertainty | Reflects uncertainty through an interval procedure |

Reporting a point estimate together with a confidence interval is often more informative than reporting the point estimate alone.

## 20. Confidence Interval vs Prediction Interval

A **confidence interval** estimates a population parameter, such as the population mean.

A **prediction interval** estimates a range for a future individual observation.

For example:

- Confidence interval: What is the population's average delivery time?
- Prediction interval: What delivery time might occur for one future order?

A prediction interval is generally wider because it accounts for uncertainty in the estimated mean as well as the natural variation of individual observations.

These intervals answer different questions and should not be used interchangeably.

## 21. Finite Population Correction

When sampling without replacement from a finite population, the standard error may need an adjustment if the sample is a substantial fraction of the population.

The **finite population correction (FPC)** is:

$$
FPC=\sqrt{\frac{N-n}{N-1}}
$$

where:

- $N$ is the population size.
- $n$ is the sample size.

The adjusted standard error is:

$$
SE_{\text{adjusted}}=SE\times FPC
$$

### Worked Example

Suppose $N=1000$ and $n=100$.

$$
FPC=\sqrt{\frac{1000-100}{1000-1}}
$$

$$
FPC\approx0.949
$$

The unadjusted standard error is multiplied by approximately 0.949.

### Python Implementation

```python
import numpy as np

N = 1000
n = 100
unadjusted_se = 2

fpc = np.sqrt((N - n) / (N - 1))
adjusted_se = unadjusted_se * fpc

print("Finite population correction:", fpc)
print("Adjusted standard error:", adjusted_se)
```

The correction applies to appropriate finite-population sampling designs. It is close to 1 when the sample is small relative to the population.

## 22. Bootstrap Confidence Intervals

The **bootstrap** is a resampling technique used to approximate the sampling variability of a statistic.

Instead of collecting new samples from the population, we repeatedly draw samples **with replacement** from the observed sample.

For example, if the observed sample is:

$$
[10,\ 12,\ 15,\ 18,\ 20]
$$

A bootstrap sample might be:

$$
[12,\ 12,\ 18,\ 20,\ 10]
$$

Each bootstrap sample has the same size as the original sample. We calculate the statistic of interest, such as the mean, for every resample.

### Bootstrap Procedure

1. Start with the observed sample.
2. Draw a new sample of the same size with replacement.
3. Calculate the statistic.
4. Repeat the process many times.
5. Examine the resulting bootstrap distribution.
6. Construct an appropriate confidence interval.

### Python Implementation

```python
import numpy as np

rng = np.random.default_rng(42)

data = np.array([4, 5, 6, 7, 8])

number_of_resamples = 10_000
bootstrap_means = np.empty(number_of_resamples)

for i in range(number_of_resamples):
    resample = rng.choice(
        data,
        size=len(data),
        replace=True
    )
    bootstrap_means[i] = resample.mean()

lower, upper = np.percentile(
    bootstrap_means,
    [2.5, 97.5]
)

print("Original sample mean:", data.mean())
print("Bootstrap percentile interval:", (lower, upper))
```

The percentile interval uses the 2.5th and 97.5th percentiles of the bootstrap estimates.

**Important:** A bootstrap does not eliminate uncertainty or guarantee a valid interval. Its performance depends on the original sample, statistic, sampling design, and interval method.

## 23. Sampling Distribution vs Bootstrap Distribution

| Sampling distribution | Bootstrap distribution |
|---|---|
| Describes a statistic across repeated samples from the population | Approximates the statistic's behaviour through resampling |
| May be derived mathematically | Often generated computationally |
| Describes theoretical sampling behaviour | Uses the observed sample as an approximation to the population |
| May have an analytical formula | Can help when an analytical formula is difficult |

The bootstrap is useful for estimating uncertainty when direct mathematical calculations are difficult, provided its assumptions and limitations are considered.

## 24. Assumptions Behind Statistical Inference

Inferential methods depend on assumptions. Important considerations include:

**Random sampling:** The sample should be selected appropriately for the intended population.

**Independence:** Observations should be independent when required by the method.

**Distributional conditions:** Some procedures require a Normal population, an approximately Normal sampling distribution, or sufficiently large samples.

**Representative data:** A large sample can still be misleading if the selection process systematically excludes important groups.

**Correct study design:** Paired, clustered, stratified, and independent samples can require different methods.

Always check the assumptions before applying a formula.

## 25. Statistical Precision vs Practical Importance

Statistical precision and practical importance are different.

A very large sample may allow a tiny difference to be estimated precisely. However, that difference may not matter much in the real situation.

- **Statistical precision:** How accurately has the parameter been estimated?
- **Practical importance:** Is the estimated difference meaningful in context?

A good interpretation considers both the numerical estimate and its practical implications.

## 26. Applications in Data Science and Machine Learning

Inferential statistics is useful in many data science workflows.

### A/B Testing

Confidence intervals can estimate differences in conversion rates between two website designs or marketing campaigns.

### Model Evaluation

Sampling-based methods can help quantify uncertainty in model performance metrics, such as accuracy or mean absolute error.

### Customer Analytics

Sample surveys can estimate customer satisfaction, product preference, and retention-related proportions.

### Business Forecasting

Confidence intervals can communicate uncertainty around estimates used in business planning.

### Data Collection

Sample-size calculations help determine how much data may be needed to achieve a desired level of precision.

### Important Distinction

Confidence intervals for population parameters are not automatically prediction intervals for future machine-learning outputs. The method must match the question being answered.

## 27. Common Mistakes

1. **Treating a sample statistic as the exact population parameter.** A statistic is an estimate and can vary across samples.
2. **Confusing standard deviation and standard error.** Standard deviation describes variation in observations; standard error describes sampling variability.
3. **Misinterpreting a 95% confidence interval.** The frequentist interpretation concerns the long-run performance of the interval procedure.
4. **Assuming higher confidence gives a narrower interval.** Higher confidence generally produces a wider interval.
5. **Ignoring the t-distribution.** For a one-sample mean with unknown population standard deviation, the t-distribution is commonly used.
6. **Forgetting degrees of freedom.** For the standard one-sample t procedure, $df=n-1$.
7. **Rounding sample size downward.** Required sample sizes should normally be rounded upward.
8. **Assuming a large sample removes bias.** A large but poorly selected sample can remain unrepresentative.
9. **Applying a formula without checking assumptions.** Sampling design and independence matter.
10. **Confusing confidence intervals and prediction intervals.** They answer different questions.
11. **Treating bootstrap intervals as automatically reliable.** Resampling does not fix every limitation of the original sample.
12. **Ignoring practical importance.** A precise estimate may still represent a practically insignificant difference.

## 28. Important Formula Summary

### Sample Mean

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

### Sample Proportion

$$
\hat{p}=\frac{x}{n}
$$

### Standard Error of the Mean

When population standard deviation is known:

$$
SE(\bar{x})=\frac{\sigma}{\sqrt{n}}
$$

Estimated using sample standard deviation:

$$
SE(\bar{x})=\frac{s}{\sqrt{n}}
$$

### Standard Error of a Proportion

$$
SE(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

### Bias of an Estimator

$$
Bias(\hat{\theta})=E(\hat{\theta})-\theta
$$

### Confidence Interval for a Mean: Known Population SD

$$
\bar{x}\pm z^*\frac{\sigma}{\sqrt{n}}
$$

### Confidence Interval for a Mean: Unknown Population SD

$$
\bar{x}\pm t^*\frac{s}{\sqrt{n}}
$$

### Degrees of Freedom for a One-Sample t Interval

$$
df=n-1
$$

### Approximate Confidence Interval for a Proportion

$$
\hat{p}\pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

### Standard Error for the Difference Between Two Independent Means

$$
SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

### Approximate Confidence Interval for the Difference Between Two Means

$$
(\bar{x}_1-\bar{x}_2)\pm\text{Critical Value}\times SE
$$

### Approximate Confidence Interval for the Difference Between Two Proportions

$$
(\hat{p}_1-\hat{p}_2)\pm z^*SE
$$

### Sample Size for Estimating a Mean

$$
n=\left(\frac{z^*\sigma}{E}\right)^2
$$

### Sample Size for Estimating a Proportion

$$
n=\frac{(z^*)^2p(1-p)}{E^2}
$$

For an unknown proportion, use $p=0.5$ for conservative planning:

$$
n=\frac{(z^*)^2(0.25)}{E^2}
$$

### Finite Population Correction

$$
FPC=\sqrt{\frac{N-n}{N-1}}
$$

### Adjusted Standard Error

$$
SE_{\text{adjusted}}=SE\times FPC
$$

### Width of a Symmetric Confidence Interval

$$
\text{Width}=\text{Upper Limit}-\text{Lower Limit}
$$

$$
ME=\frac{\text{Width}}{2}
$$

---

## 29. Points to Remember

1. Inferential statistics uses sample data to draw conclusions about a population.
2. A parameter describes a population; a statistic describes a sample.
3. Different samples can produce different estimates.
4. A sampling distribution describes the behaviour of a statistic across repeated samples.
5. Standard error measures sampling variability.
6. The standard error of the mean decreases with the square root of sample size under the usual assumptions.
7. A point estimate provides a single estimated value.
8. A confidence interval communicates uncertainty through an interval procedure.
9. Higher confidence generally means a wider interval.
10. Larger samples generally produce narrower intervals.
11. The t-distribution is commonly used for means when the population standard deviation is unknown.
12. An unbiased estimator is correct on average.
13. A consistent estimator approaches the true parameter as sample size grows.
14. Efficiency concerns variability relative to alternative estimators.
15. Required sample sizes should normally be rounded upward.
16. A large sample does not automatically eliminate selection bias.
17. Confidence intervals and prediction intervals have different purposes.
18. The bootstrap approximates sampling behaviour through resampling.
19. Statistical precision and practical importance are different concepts.
20. Always check assumptions before applying an inferential method.

## 30. Chapter Summary

Inferential statistics helps us use sample data to estimate population parameters and quantify uncertainty. Sampling distributions explain how statistics vary across samples, while standard errors measure their sampling variability.

Point estimates provide single numerical estimates. Confidence intervals provide ranges that reflect uncertainty under a specified statistical procedure. Sample-size calculations help plan studies, and bootstrap methods offer a resampling-based way to approximate uncertainty.

These concepts form an important foundation for hypothesis testing, A/B testing, statistical model evaluation, and data-driven decision-making.

## 31. References and Further Reading

### Textbooks and Educational Resources

- OpenStax, [Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e)
- NIST/SEMATECH, [e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- Penn State, [Online Statistics Courses](https://online.stat.psu.edu/)
- Casella and Berger, *Statistical Inference*
- Montgomery and Runger, *Applied Statistics and Probability for Engineers*

### Python Documentation

- NumPy, [Official Documentation](https://numpy.org/doc/stable/)
- SciPy, [Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- Statsmodels, [Official Documentation](https://www.statsmodels.org/stable/)

### Related Topics in This Repository

- `01_Statistics_Fundamentals`
- `02_Descriptive_Statistics`
- `03_Probability`
- `04_Probability_Distributions`
- `06_Hypothesis_Testing`
- `07_ANOVA`
- `09_Correlation`
- `10_Regression`
- `11_Regression_Model_Evaluation`
- `15_Statistics_for_Machine_Learning`
