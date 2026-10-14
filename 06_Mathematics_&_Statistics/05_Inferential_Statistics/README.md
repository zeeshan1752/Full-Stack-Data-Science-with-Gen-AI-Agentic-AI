# Inferential Statistics

**Inferential Statistics** is the branch of statistics used to draw conclusions about a population using information collected from a sample.

Descriptive statistics summarises the data we already have. Inferential statistics goes further by using sample data to estimate population parameters, quantify uncertainty, construct confidence intervals, and support statistical decisions.

For example, a university may have 20,000 students. Instead of measuring the study time of every student, we can select a sample, calculate its average study time, and use that result to estimate the population mean.

Because different samples can produce different results, inferential statistics also measures **sampling uncertainty**.

This chapter covers population and sample, parameters and statistics, sampling methods, sampling distributions, standard error, point estimation, estimator properties, confidence intervals, margin of error, sample-size determination, finite population correction, bootstrap methods, and Python implementation.

## 1. Population and Sample

A **population** is the complete group about which we want to draw conclusions.

A **sample** is a subset selected from that population.

The relationship is:

**Sample ⊂ Population**

For example, if a university has 20,000 students and we select 500 students for a survey:

- Population: all 20,000 students.
- Sample: the 500 selected students.
- Population mean: the true average for all students.
- Sample mean: the average calculated from the selected students.

The population parameter is usually unknown, whereas the sample statistic can be calculated from observed data.

## 2. Parameter and Statistic

A **parameter** describes a population, while a **statistic** describes a sample.

| Population parameter | Sample statistic |
|---|---|
| Population mean, \(\mu\) | Sample mean, \(\bar{x}\) |
| Population variance, \(\sigma^2\) | Sample variance, \(s^2\) |
| Population standard deviation, \(\sigma\) | Sample standard deviation, \(s\) |
| Population proportion, \(p\) | Sample proportion, \(\hat{p}\) |

For example, if the average study time of 100 sampled students is 4.8 hours, then \(\bar{x}=4.8\) hours is a statistic used to estimate the unknown population mean \(\mu\).

### Python Example

```python
import numpy as np

study_hours = np.array([3, 4, 5, 6, 4, 5, 3, 8, 6, 4])

sample_mean = np.mean(study_hours)
sample_sd = np.std(study_hours, ddof=1)

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_sd)
```

The sample mean and standard deviation describe the observed sample. They do not automatically equal the corresponding population quantities.

## 3. Why Sampling Creates Uncertainty

Different random samples from the same population usually contain different observations. Consequently, their sample statistics can differ.

For example:

| Sample | Sample mean |
|---|---:|
| Sample 1 | 68.2 |
| Sample 2 | 67.5 |
| Sample 3 | 68.7 |
| Sample 4 | 67.9 |
| Sample 5 | 68.4 |

This variation is called **sampling variability**.

Inferential statistics addresses two main questions:

1. What is the best estimate of the population parameter?
2. How much uncertainty is associated with that estimate?

Point estimation addresses the first question. Standard errors and confidence intervals help address the second.

## 4. Sampling Methods

The method used to select a sample affects how reliably the results represent the target population.

### 4.1 Simple Random Sampling

In simple random sampling, every population member has an equal chance of selection.

Example: randomly selecting 500 students from a university's student database.

### 4.2 Stratified Sampling

The population is divided into meaningful groups called **strata**, and samples are selected from these groups.

Example: dividing students by academic year and sampling students from every year.

Stratified sampling can help ensure representation of important subgroups.

### 4.3 Systematic Sampling

Observations are selected at regular intervals after an appropriate starting point.

Example: selecting every 20th customer from an ordered list after choosing a random starting position.

### 4.4 Cluster Sampling

The population is divided into natural groups called **clusters**. Some clusters are selected, and observations within them are studied.

Example: randomly selecting several colleges and surveying students in those colleges.

### 4.5 Convenience Sampling

Observations are selected because they are easy to access.

Example: surveying only people near a particular shop.

Convenience sampling can introduce selection bias and should not automatically be treated as representative.

**Important:** A large sample does not automatically eliminate bias. The sampling design and quality of the data matter.

## 5. Sampling Distribution

A **sampling distribution** is the probability distribution of a statistic across repeated samples of the same size from a population.

Imagine repeatedly selecting samples of size \(n\), calculating the mean of each sample, and recording the results. The distribution of those means is the sampling distribution of the sample mean.

A sampling distribution describes the behaviour of a **statistic**, not the distribution of individual observations.

For the sample mean, assuming independent observations from a population with mean \(\mu\) and finite variance \(\sigma^2\):

$E(\bar{X})=\mu$

$\mathrm{Var}(\bar{X})=\frac{\sigma^2}{n}$

Therefore, the standard deviation of the sampling distribution is:

$SE(\bar{X})=\frac{\sigma}{\sqrt{n}}$

This is called the **standard error of the mean**.

## 6. Standard Error

The **standard error (SE)** measures the sampling variability of a statistic.

For the sample mean, when the population standard deviation is known:

$SE(\bar{x})=\frac{\sigma}{\sqrt{n}}$

When the population standard deviation is unknown, we commonly estimate the standard error using the sample standard deviation:

$SE(\bar{x})=\frac{s}{\sqrt{n}}$

For a sample proportion, the estimated standard error is:

$SE(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Standard Deviation vs Standard Error

| Standard deviation | Standard error |
|---|---|
| Measures the spread of observations | Measures the sampling variability of an estimate |
| Describes variability in the data | Describes uncertainty in a statistic |
| Does not automatically decrease when more observations are collected | Usually decreases as sample size increases |
| Expressed in the original measurement units | Expressed in the units of the statistic |

### Worked Example

Suppose the population standard deviation is 12.

For a sample of size 36:

$SE=\frac{12}{\sqrt{36}}=\frac{12}{6}=2$

For a sample of size 144:

$SE=\frac{12}{\sqrt{144}}=\frac{12}{12}=1$

The sample size becomes four times larger, while the standard error becomes half as large.

### Python Example

```python
import numpy as np

population_sd = 12

for n in [36, 144, 576]:
    standard_error = population_sd / np.sqrt(n)
    print(f"Sample size: {n}, SE: {standard_error:.4f}")
```

## 7. Sampling Distribution of a Sample Proportion

A sample proportion estimates the proportion of a population with a particular characteristic.

The formula is:

$\hat{p}=\frac{x}{n}$

where \(x\) is the number of observations with the characteristic and \(n\) is the sample size.

Its expected value under random sampling is:

$E(\hat{p})=p$

Its variance, under independent Bernoulli sampling, is:

$\mathrm{Var}(\hat{p})=\frac{p(1-p)}{n}$

Therefore, the standard deviation of its sampling distribution is:

$SD(\hat{p})=\sqrt{\frac{p(1-p)}{n}}$

When \(p\) is unknown, the estimated standard error is:

$SE(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Worked Example

Suppose 120 out of 200 customers prefer Product A.

$\hat{p}=\frac{120}{200}=0.60$

The estimated proportion is 60%.

Calculate the standard error:

$SE(\hat{p})=\sqrt{\frac{0.60(1-0.60)}{200}}$

$SE(\hat{p})=\sqrt{0.0012}$

$SE(\hat{p})\approx0.0346$

### Python Example

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

## 8. Point Estimation

A **point estimate** is a single numerical value used to estimate an unknown population parameter.

Examples include:

- \(\bar{x}\) estimates the population mean \(\mu\).
- \(\hat{p}\) estimates the population proportion \(p\).
- \(s^2\) estimates the population variance \(\sigma^2\).

Suppose a sample of students has an average study time of 4.8 hours per day.

The point estimate is:

$\hat{\mu}=4.8\text{ hours}$

A point estimate is useful, but it does not directly show how uncertain the estimate is. Standard errors and confidence intervals provide additional information.

## 9. Estimator and Estimate

An **estimator** is a statistic or rule used to estimate a population parameter.

An **estimate** is the numerical value obtained after applying that estimator to a particular sample.

For example:

$\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i$

is an estimator of the population mean \(\mu\).

If a particular sample gives:

$\bar{x}=72.4$

then 72.4 is the estimate.

In short:

- Estimator: the procedure or statistic.
- Estimate: the numerical result.

## 10. Properties of a Good Estimator

Three important properties of estimators are:

1. Unbiasedness
2. Consistency
3. Efficiency

These properties help us compare methods for estimating the same population parameter.

### 10.1 Unbiased Estimator

An estimator \(\hat{\theta}\) is unbiased for a parameter \(\theta\) if:

$E(\hat{\theta})=\theta$

This means that across repeated samples, the estimator's expected value equals the true parameter.

For the sample mean:

$E(\bar{X})=\mu$

Therefore, the sample mean is an unbiased estimator of the population mean under the usual sampling assumptions.

Unbiasedness does not mean that every estimate equals the true parameter. It means that the estimator is correct on average.

### 10.2 Bias of an Estimator

The bias of an estimator is:

$Bias(\hat{\theta})=E(\hat{\theta})-\theta$

If \(E(\hat{\theta})=\theta\), then the bias is zero.

For example, suppose the expected value of an estimator is 52 and the true parameter is 50.

$Bias(\hat{\theta})=52-50=2$

The estimator has an upward bias of 2.

### 10.3 Consistent Estimator

An estimator is **consistent** if it approaches the true parameter as the sample size increases.

Informally, increasing the amount of suitable data should make the estimate increasingly close to the population parameter.

A common notation is:

$\hat{\theta}_n\xrightarrow{P}\theta$

This denotes convergence in probability to the true parameter.

Consistency is different from unbiasedness. An estimator can be biased for finite samples and still be consistent.

### 10.4 Efficient Estimator

When comparing unbiased estimators of the same parameter, an estimator with smaller variance is generally considered more efficient.

Suppose two unbiased estimators have:

$\mathrm{Var}(\hat{\theta}_1)=4$

$\mathrm{Var}(\hat{\theta}_2)=9$

Estimator 1 is more precise because its estimates fluctuate less across repeated samples.

**Remember:** Unbiasedness concerns correctness on average, while efficiency concerns variability.

## 11. Confidence Intervals

A **confidence interval (CI)** is an interval estimate constructed from sample data to estimate a population parameter.

Instead of reporting only:

$\bar{x}=72$

we might report a confidence interval from 68 to 76.

A common structure is:

$\text{Confidence Interval}=\text{Point Estimate}\pm\text{Margin of Error}$

For many standard intervals:

$\text{Margin of Error}=\text{Critical Value}\times SE$

Therefore:

$CI=\text{Estimate}\pm\text{Critical Value}\times SE$

A confidence interval communicates both an estimate and its sampling uncertainty.

## 12. Confidence Level and Critical Values

Common confidence levels include 90%, 95%, and 99%.

A 95% confidence procedure has a long-run interpretation: if the same valid sampling procedure were repeated many times and an interval constructed each time, approximately 95% of those intervals would contain the fixed population parameter.

It does not mean that a fixed parameter has a 95% probability of lying inside one already-calculated frequentist confidence interval.

For a standard Normal distribution, common two-sided critical values are:

| Confidence level | Critical value \(z^*\) |
|---|---:|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

Higher confidence generally requires a larger critical value and therefore a wider interval, when other factors are held constant.

### Python Example

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

## 13. Confidence Interval for a Population Mean When \(\sigma\) Is Known

When the population standard deviation \(\sigma\) is known, a standard confidence interval for the population mean is:

$\bar{x}\pm z^*\frac{\sigma}{\sqrt{n}}$

where:

- \(\bar{x}\) = sample mean
- \(z^*\) = Normal critical value
- \(\sigma\) = population standard deviation
- \(n\) = sample size

### Worked Example

Suppose:

- Sample mean = 72
- Population standard deviation = 10
- Sample size = 100
- Confidence level = 95%

The critical value is:

$z^*=1.96$

Calculate the standard error:

$SE=\frac{10}{\sqrt{100}}=1$

Calculate the margin of error:

$ME=1.96(1)=1.96$

The interval is:

$CI=72\pm1.96$

Lower limit:

$72-1.96=70.04$

Upper limit:

$72+1.96=73.96$

Therefore:

$CI=(70.04,\ 73.96)$

### Python Example

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

## 14. Confidence Interval for a Population Mean When \(\sigma\) Is Unknown

In most real-world situations, the population standard deviation is unknown. We estimate it using the sample standard deviation \(s\) and commonly use the **t-distribution**.

The interval is:

$\bar{x}\pm t^*\frac{s}{\sqrt{n}}$

The degrees of freedom for the standard one-sample t interval are:

$df=n-1$

The t-distribution has heavier tails than the standard Normal distribution, particularly at low degrees of freedom. As the degrees of freedom increase, it approaches the standard Normal distribution.

### Worked Example

Suppose:

- \(\bar{x}=50\)
- \(s=8\)
- \(n=16\)
- Confidence level = 95%

Degrees of freedom:

$df=16-1=15$

The 95% two-sided critical value is approximately:

$t^*=2.131$

Calculate the standard error:

$SE=\frac{8}{\sqrt{16}}=2$

Calculate the margin of error:

$ME=2.131(2)=4.262$

Therefore:

$CI=50\pm4.262$

$CI\approx(45.738,\ 54.262)$

### Python Example

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

The usual one-sample t interval assumes independent observations and is exact under a Normal population model. For strongly skewed data or influential outliers, suitability should be assessed carefully.

## 15. Confidence Interval for a Population Proportion

A common large-sample confidence interval for a population proportion is:

$\hat{p}\pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

where:

- \(\hat{p}\) = sample proportion
- \(z^*\) = Normal critical value
- \(n\) = sample size

### Worked Example

Suppose 120 out of 200 customers prefer Product A.

$\hat{p}=\frac{120}{200}=0.60$

For 95% confidence:

$z^*=1.96$

Calculate the estimated standard error:

$SE=\sqrt{\frac{0.60(0.40)}{200}}$

$SE=\sqrt{0.0012}\approx0.0346$

The margin of error is approximately:

$ME=1.96(0.0346)\approx0.0678$

Therefore:

$CI=0.60\pm0.0678$

$CI\approx(0.5322,\ 0.6678)$

In percentage form, this is approximately 53.2% to 66.8%.

### Conditions

The simple Normal approximation should be used only when the sample is sufficiently large for the approximation to be reasonable. A common rule checks:

$n\hat{p}\geq10$

$n(1-\hat{p})\geq10$

For small samples or proportions close to 0 or 1, methods such as the Wilson interval may perform better than the basic Wald interval.

### Python Example

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

This example uses the Wilson method rather than the basic Normal-approximation interval. Install the dependency if necessary using `pip install statsmodels`.

## 16. Confidence Interval for the Difference Between Two Means

Suppose we want to estimate the difference between two population means:

$\mu_1-\mu_2$

For independent samples, an estimated standard error is:

$SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$

A general confidence interval is:

$(\bar{x}_1-\bar{x}_2)\pm\text{Critical Value}\times SE$

When population standard deviations are unknown and unequal variances are plausible, **Welch's t interval** is a common choice.

### Worked Example

Suppose two independent groups have these results:

| Group | Mean | Standard deviation | Sample size |
|---|---:|---:|---:|
| Group 1 | 82 | 10 | 100 |
| Group 2 | 78 | 12 | 144 |

Estimated difference:

$\bar{x}_1-\bar{x}_2=82-78=4$

Estimated standard error:

$SE=\sqrt{\frac{10^2}{100}+\frac{12^2}{144}}$

$SE=\sqrt{1+1}=\sqrt{2}\approx1.414$

Using 1.96 as an illustrative large-sample Normal critical value:

$ME=1.96(1.414)\approx2.77$

The illustrative interval is:

$CI=4\pm2.77$

$CI\approx(1.23,\ 6.77)$

For a formal analysis with unknown population standard deviations, use an appropriate t-based interval, such as Welch's method.

### Python Example

```python
import numpy as np
from scipy.stats import t

mean1, sd1, n1 = 82, 10, 100
mean2, sd2, n2 = 78, 12, 144

difference = mean1 - mean2

se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)

# Welch-Satterthwaite degrees of freedom
numerator = (sd1**2 / n1 + sd2**2 / n2) ** 2
denominator = (
    (sd1**2 / n1) ** 2 / (n1 - 1)
    + (sd2**2 / n2) ** 2 / (n2 - 1)
)
df = numerator / denominator

critical = t.ppf(0.975, df)

lower = difference - critical * se
upper = difference + critical * se

print("Mean difference:", difference)
print("Standard error:", se)
print("Degrees of freedom:", df)
print("95% Welch confidence interval:", (lower, upper))
```

## 17. Confidence Interval for the Difference Between Two Proportions

For two independent groups, the estimated difference between sample proportions is:

$\hat{p}_1-\hat{p}_2$

A common large-sample standard error is:

$SE=\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1}+\frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$

The corresponding approximate confidence interval is:

$(\hat{p}_1-\hat{p}_2)\pm z^*SE$

### Worked Example

Suppose:

- Group 1: 60 successes out of 100
- Group 2: 45 successes out of 100

Then:

$\hat{p}_1=0.60$

$\hat{p}_2=0.45$

Difference:

$\hat{p}_1-\hat{p}_2=0.15$

Standard error:

$SE=\sqrt{\frac{0.60(0.40)}{100}+\frac{0.45(0.55)}{100}}$

$SE=\sqrt{0.004875}\approx0.0698$

For 95% confidence:

$ME=1.96(0.0698)\approx0.1368$

Therefore:

$CI=0.15\pm0.1368$

$CI\approx(0.0132,\ 0.2868)$

The estimated difference is 15 percentage points. The interval describes uncertainty in that difference under the approximation.

## 18. Margin of Error

The **margin of error** is the amount added to and subtracted from a point estimate to form a symmetric confidence interval.

For a mean with known population standard deviation:

$ME=z^*\frac{\sigma}{\sqrt{n}}$

For a mean using the t-distribution:

$ME=t^*\frac{s}{\sqrt{n}}$

For a proportion using the basic Normal approximation:

$ME=z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

A smaller margin of error generally means greater precision.

## 19. Factors Affecting Margin of Error

Three important factors affect the margin of error.

**Confidence level:** A higher confidence level requires a larger critical value and generally a wider interval.

**Sample size:** A larger sample usually reduces standard error and narrows the interval.

**Variability:** Greater population or sample variability usually increases standard error and widens the interval.

When other factors remain fixed:

$ \text{Higher confidence}\Rightarrow\text{larger margin of error}$

$ \text{Larger sample}\Rightarrow\text{smaller margin of error}$

$ \text{Greater variability}\Rightarrow\text{larger margin of error}$

## 20. Width of a Confidence Interval

For a symmetric confidence interval:

$\text{Width}=\text{Upper Limit}-\text{Lower Limit}$

For example, if:

$CI=(70.04,\ 73.96)$

then:

$\text{Width}=73.96-70.04=3.92$

The margin of error is half the width:

$ME=\frac{3.92}{2}=1.96$

Therefore, for a symmetric interval:

$ME=\frac{\text{CI Width}}{2}$

## 21. Sample Size for Estimating a Population Mean

Suppose we want to estimate a population mean with a margin of error no greater than \(E\).

Using a Normal critical value and a known or planning estimate of the population standard deviation:

$E=z^*\frac{\sigma}{\sqrt{n}}$

Rearranging gives:

$n=\left(\frac{z^*\sigma}{E}\right)^2$

The calculated sample size must normally be **rounded upward** to ensure the desired margin of error is not exceeded under the planning assumptions.

### Worked Example

Suppose:

- \(\sigma=12\)
- Desired margin of error \(E=2\)
- 95% confidence, so \(z^*=1.96\)

Then:

$n=\left(\frac{1.96(12)}{2}\right)^2$

$n=(11.76)^2=138.2976$

Rounding upward:

$n=139$

At least 139 observations are required under these assumptions.

### Python Example

```python
import numpy as np
from scipy.stats import norm

population_sd = 12
margin_of_error = 2
confidence = 0.95

z_critical = norm.ppf(1 - (1 - confidence) / 2)

n_required = (z_critical * population_sd / margin_of_error) ** 2

print("Unrounded sample size:", n_required)
print("Required sample size:", int(np.ceil(n_required)))
```

## 22. Sample Size for Estimating a Population Proportion

A common planning formula for a population proportion is:

$n=\frac{(z^*)^2p(1-p)}{E^2}$

where:

- \(p\) = anticipated population proportion
- \(E\) = desired margin of error
- \(z^*\) = critical value

If the population proportion is unknown, a conservative choice is:

$p=0.5$

This maximises \(p(1-p)\) and therefore gives the largest required sample size for the specified confidence level and margin of error.

The formula becomes:

$n=\frac{(z^*)^2(0.25)}{E^2}$

### Worked Example

Suppose we want 95% confidence and a margin of error of 0.05, without a prior estimate of the proportion.

Use:

$z^*=1.96$

$p=0.5$

Then:

$n=\frac{(1.96)^2(0.25)}{(0.05)^2}$

$n=\frac{0.9604}{0.0025}=384.16$

Round upward:

$n=385$

### Python Example

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

## 23. Point Estimate vs Interval Estimate

| Point estimate | Interval estimate |
|---|---|
| Gives one numerical value | Gives a range of values |
| Easy to communicate | Communicates uncertainty |
| Example: \(\bar{x}=72\) | Example: 95% CI from 70 to 74 |
| Does not directly show sampling uncertainty | Incorporates uncertainty through a statistical procedure |

Point estimates and confidence intervals complement each other. Reporting both is often more informative than reporting the point estimate alone.

## 24. Confidence Interval vs Prediction Interval

A **confidence interval** estimates a population parameter, such as the population mean.

A **prediction interval** estimates a range for a future individual observation.

For example:

- Confidence interval: What is the population's average delivery time?
- Prediction interval: What delivery time might occur for one future order?

A prediction interval is generally wider because it accounts for both uncertainty in estimating the mean and the natural variation of individual observations.

These intervals answer different questions and should not be used interchangeably.

## 25. Finite Population Correction

When sampling without replacement from a finite population, the standard error may need an adjustment if the sample is a substantial fraction of the population.

The finite population correction (FPC) is:

$FPC=\sqrt{\frac{N-n}{N-1}}$

where \(N\) is the population size and \(n\) is the sample size.

The adjusted standard error is:

$SE_{\text{adjusted}}=SE\times\sqrt{\frac{N-n}{N-1}}$

### Worked Example

Suppose:

$N=1000$

$n=100$

Then:

$FPC=\sqrt{\frac{1000-100}{1000-1}}$

$FPC=\sqrt{\frac{900}{999}}\approx0.949$

The standard error is multiplied by approximately 0.949.

### Python Example

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

The correction is relevant for appropriate finite-population sampling designs. It is close to 1 when the sample is small relative to the population.

## 26. Bootstrap Confidence Intervals

The **bootstrap** is a resampling technique used to approximate the sampling variability of a statistic.

Instead of collecting new samples from the population, we repeatedly draw samples **with replacement** from the observed sample.

Suppose the observed data are:

$[10,\ 12,\ 15,\ 18,\ 20]$

A bootstrap sample of the same size might be:

$[12,\ 12,\ 18,\ 20,\ 10]$

Another might be:

$[15,\ 15,\ 10,\ 20,\ 18]$

For each resample, calculate the statistic of interest, such as the mean. Repeating this many times produces an empirical bootstrap distribution.

A confidence interval can then be constructed using a suitable method, such as the percentile method.

### Bootstrap Procedure

1. Start with the observed sample.
2. Draw a new sample of the same size with replacement.
3. Calculate the statistic.
4. Repeat many times.
5. Examine the bootstrap distribution.
6. Construct an appropriate confidence interval.

### Python Example

```python
import numpy as np

rng = np.random.default_rng(42)

data = np.array([4, 5, 6, 7, 8])

number_of_resamples = 10_000
bootstrap_means = np.empty(number_of_resamples)

for i in range(number_of_resamples):
    resample = rng.choice(data, size=len(data), replace=True)
    bootstrap_means[i] = resample.mean()

lower, upper = np.percentile(bootstrap_means, [2.5, 97.5])

print("Original sample mean:", data.mean())
print("Bootstrap percentile interval:", (lower, upper))
```

**Important:** A bootstrap does not eliminate uncertainty or guarantee a valid interval. Its performance depends on the sample, statistic, resampling design, and interval method.

## 27. Sampling Distribution vs Bootstrap Distribution

| Sampling distribution | Bootstrap distribution |
|---|---|
| Describes a statistic across repeated samples from the population | Approximates the statistic's behaviour through resampling |
| May be derived mathematically | Often generated computationally |
| Describes theoretical sampling behaviour | Uses the observed sample as an approximation to the population |
| Can have an analytical formula | Can be useful when an analytical formula is difficult |

The bootstrap is a practical tool for estimating uncertainty when direct mathematical calculations are difficult.

## 28. Assumptions Behind Statistical Inference

Inferential methods depend on assumptions. Important considerations include:

**Random sampling:** The sample should be selected appropriately for the intended population inference.

**Independence:** Observations should be independent when required by the method.

**Distributional conditions:** Some procedures require a Normal population, approximately Normal sampling distribution, or sufficiently large samples.

**Representative data:** A large sample can still be misleading if the selection process systematically excludes important parts of the population.

**Correct study design:** Paired, clustered, stratified, and independent samples can require different methods.

Always check the assumptions before applying a formula.

## 29. Statistical Precision vs Practical Importance

Statistical precision and practical importance are different.

A very large sample may allow a tiny difference to be estimated precisely. However, that difference may not matter much in the real situation.

Statistical precision asks:

> How accurately have we estimated the parameter?

Practical importance asks:

> Is the size of the difference meaningful in context?

A good interpretation considers both the numerical estimate and its practical implications.

## 30. Common Mistakes

**1. Treating a sample statistic as the exact population parameter.** A sample statistic is an estimate and can vary across samples.

**2. Confusing standard deviation and standard error.** Standard deviation describes variation in observations; standard error describes sampling variability.

**3. Misinterpreting a 95% confidence interval.** The standard frequentist interpretation concerns the long-run performance of the interval procedure.

**4. Assuming higher confidence gives a narrower interval.** Higher confidence generally produces a wider interval when other factors are fixed.

**5. Ignoring the t-distribution.** For a one-sample mean with unknown population standard deviation, the t-distribution is commonly used.

**6. Forgetting degrees of freedom.** For the standard one-sample t procedure, \(df=n-1\).

**7. Rounding sample size downward.** Required sample sizes should normally be rounded upward.

**8. Assuming a large sample removes bias.** A large but poorly selected sample can still be unrepresentative.

**9. Applying a formula without checking assumptions.** Independence, sampling design, and distributional conditions matter.

**10. Confusing confidence intervals and prediction intervals.** They answer different questions.

**11. Treating bootstrap intervals as automatically reliable.** Resampling approximates sampling behaviour but does not fix every limitation of the original sample.

## 31. Important Formula Summary

### Sample Mean

$\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$

### Standard Error of the Mean

When population standard deviation is known:

$SE(\bar{x})=\frac{\sigma}{\sqrt{n}}$

Estimated using the sample standard deviation:

$SE(\bar{x})=\frac{s}{\sqrt{n}}$

### Sample Proportion

$\hat{p}=\frac{x}{n}$

### Standard Error of a Proportion

$SE(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Bias

$Bias(\hat{\theta})=E(\hat{\theta})-\theta$

### z-Based Confidence Interval for a Mean

$\bar{x}\pm z^*\frac{\sigma}{\sqrt{n}}$

### t-Based Confidence Interval for a Mean

$\bar{x}\pm t^*\frac{s}{\sqrt{n}}$

### Degrees of Freedom for One-Sample t

$df=n-1$

### Approximate Confidence Interval for a Proportion

$\hat{p}\pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Difference Between Two Means

$(\bar{x}_1-\bar{x}_2)\pm\text{Critical Value}\times SE$

For independent samples:

$SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$

### Difference Between Two Proportions

$(\hat{p}_1-\hat{p}_2)\pm z^*\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1}+\frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$

### Sample Size for a Mean

$n=\left(\frac{z^*\sigma}{E}\right)^2$

### Sample Size for a Proportion

$n=\frac{(z^*)^2p(1-p)}{E^2}$

When \(p\) is unknown, use \(p=0.5\) for conservative planning:

$n=\frac{(z^*)^2(0.25)}{E^2}$

### Finite Population Correction

$FPC=\sqrt{\frac{N-n}{N-1}}$

---

## 32. Points to Remember

1. Inferential statistics uses sample data to draw conclusions about a population.
2. A parameter describes a population; a statistic describes a sample.
3. Different samples can produce different estimates.
4. A sampling distribution describes the behaviour of a statistic across repeated samples.
5. Standard error measures sampling variability.
6. The standard error of a mean decreases with the square root of sample size.
7. A point estimate provides a single estimated value.
8. A confidence interval communicates uncertainty through an interval procedure.
9. Higher confidence generally means a wider interval.
10. Larger samples generally produce narrower intervals.
11. The t-distribution is commonly used for means when the population standard deviation is unknown.
12. Unbiasedness means correct on average.
13. Consistency means approaching the true parameter as sample size grows.
14. Efficiency concerns the variability of an estimator relative to alternatives.
15. Required sample sizes should normally be rounded upward.
16. A large sample does not automatically eliminate selection bias.
17. Confidence intervals and prediction intervals have different purposes.
18. The bootstrap approximates sampling behaviour through resampling.
19. Statistical precision and practical importance are different concepts.
20. Always check assumptions before applying an inferential method.

---

## 33. References

### Textbooks and Educational Resources

- OpenStax, [Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e)
- NIST/SEMATECH, [e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- Penn State, [Online Statistics Courses](https://online.stat.psu.edu/)
- Casella and Berger, *Statistical Inference*.
- Montgomery and Runger, *Applied Statistics and Probability for Engineers*.

### Python Documentation

- NumPy, [Official Documentation](https://numpy.org/doc/stable/)
- SciPy, [Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- Statsmodels, [Official Documentation](https://www.statsmodels.org/stable/)

Use these resources alongside the worked examples and Python practice exercises in this repository.
