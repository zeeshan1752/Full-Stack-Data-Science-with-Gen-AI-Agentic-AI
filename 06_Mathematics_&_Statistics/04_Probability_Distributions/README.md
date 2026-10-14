# Probability Distributions

A **probability distribution** describes how probabilities are assigned to the possible values of a random variable. It helps us understand uncertainty, calculate probabilities, summarise data, and build statistical models.

Probability distributions are widely used in Data Science and Machine Learning for analysing customer behaviour, predicting outcomes, understanding measurement errors, modelling event counts, and performing statistical inference.

This chapter covers discrete and continuous distributions, probability mass functions, probability density functions, cumulative distribution functions, expected value, variance, common probability distributions, and their implementation in Python.

## 1. Introduction to Probability Distributions

A probability distribution tells us which values a random variable can take and how likely those values are.

For example, consider tossing a fair coin three times. Let \(X\) represent the number of Heads.

The possible values are:

$X\in\{0,1,2,3\}$

The corresponding probability distribution is:

| Number of Heads (X) | Probability P(X = x) |
|---:|---:|
| 0 | 0.125 |
| 1 | 0.375 |
| 2 | 0.375 |
| 3 | 0.125 |

Every valid probability distribution must satisfy two conditions:

- All probabilities must be non-negative.
- The sum of all probabilities must equal 1.

Mathematically:

$P(X=x)\geq0$

$\sum_x P(X=x)=1$

These conditions ensure that the distribution represents a valid probability model.

## 2. Discrete and Continuous Random Variables

### Discrete Random Variables

A discrete random variable takes countable values.

Examples include the number of customers visiting a shop, defective products in a batch, emails received per hour, and successes in an experiment.

Discrete distributions assign probabilities to individual values.

### Continuous Random Variables

A continuous random variable can take values over an interval.

Examples include height, weight, temperature, distance, and waiting time.

For a continuous random variable, probability is calculated over an interval rather than at a single exact value.

For any exact value \(a\):

$P(X=a)=0$

For an interval:

$P(a<X<b)=\int_a^b f_X(x)\,dx$

### Comparison

| Feature | Discrete | Continuous |
|---|---|---|
| Possible values | Countable | Values over an interval |
| Main function | PMF | PDF |
| Probability calculation | Sum | Integral |
| Probability of one exact value | Can be positive | Zero |
| Examples | Binomial, Poisson | Normal, Uniform, Exponential |

### Python Example

```python
import numpy as np

# Discrete observations: number of purchases
purchases = np.array([0, 1, 2, 3, 4])

# Continuous observations: measured waiting times
waiting_times = np.array([1.2, 2.5, 3.1, 4.7, 5.4])

print("Purchase counts:", purchases)
print("Waiting times:", waiting_times)
```

## 3. Probability Mass Function (PMF)

A **Probability Mass Function (PMF)** gives the probability that a discrete random variable equals a particular value.

It is written as:

$p_X(x)=P(X=x)$

A valid PMF satisfies:

$p_X(x)\geq0$

$\sum_x p_X(x)=1$

### Worked Example

Suppose a random variable has this distribution:

| x | P(X = x) |
|---:|---:|
| 0 | 0.2 |
| 1 | 0.5 |
| 2 | 0.3 |

The total probability is:

$0.2+0.5+0.3=1$

Therefore, the distribution is valid.

The probability of \(X=1\) is:

$P(X=1)=0.5$

### Python Example

```python
import numpy as np

values = np.array([0, 1, 2])
probabilities = np.array([0.2, 0.5, 0.3])

print("P(X = 1):", probabilities[1])
print("Total probability:", probabilities.sum())
print("All probabilities non-negative:",
      np.all(probabilities >= 0))
```

## 4. Probability Density Function (PDF)

A **Probability Density Function (PDF)** describes the density of probability for a continuous random variable. It is represented by \(f_X(x)\).

A valid PDF satisfies:

$f_X(x)\geq0$

$\int_{-\infty}^{\infty}f_X(x)\,dx=1$

The probability that \(X\) lies between \(a\) and \(b\) is:

$P(a\leq X\leq b)=\int_a^b f_X(x)\,dx$

The area under the entire density curve is 1.

**Important:** The value of a PDF is a density, not necessarily the probability of a particular value.

### Python Example

```python
from scipy.stats import norm

# Standard Normal distribution
density = norm.pdf(0)

print("Density at X = 0:", density)
```

The PDF gives the density at zero. To calculate a probability, use a CDF difference.

## 5. Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)** gives the probability that a random variable is less than or equal to a particular value.

$F_X(x)=P(X\leq x)$

For a discrete random variable:

$F_X(x)=\sum_{t\leq x}P(X=t)$

For a continuous random variable:

$F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt$

The CDF satisfies:

$0\leq F_X(x)\leq1$

It is non-decreasing and approaches 0 and 1 at the lower and upper extremes of a valid distribution, respectively.

### Python Example

```python
from scipy.stats import norm

x = 1

probability = norm.cdf(x)

print("P(Z <= 1):", probability)
```

For a standard Normal variable, the probability is approximately 0.8413.

## 6. Relationship Between PMF, PDF, and CDF

| Function | Meaning | Used For |
|---|---|---|
| PMF | Probability of an individual value | Discrete distributions |
| PDF | Probability density | Continuous distributions |
| CDF | Probability up to a value | Both discrete and continuous distributions |

For a continuous distribution, the PDF and CDF are related by:

$f_X(x)=\frac{d}{dx}F_X(x)$

when the derivative exists.

The CDF is obtained by integrating the PDF:

$F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt$

The probability of an interval can be calculated using:

$P(a<X\leq b)=F_X(b)-F_X(a)$

For continuous distributions, including or excluding interval endpoints does not change the probability.

### Python Example

```python
from scipy.stats import norm

lower = -1
upper = 1

probability = norm.cdf(upper) - norm.cdf(lower)

print("P(-1 < Z <= 1):", probability)
```

## 7. Expected Value

The **expected value** is the theoretical long-run average of a random variable.

For a discrete random variable:

$E(X)=\sum_x xP(X=x)$

For a continuous random variable:

$E(X)=\int_{-\infty}^{\infty}xf_X(x)\,dx$

### Worked Example

Suppose:

| X | P(X = x) |
|---:|---:|
| 0 | 0.2 |
| 1 | 0.5 |
| 2 | 0.3 |

Calculate:

$E(X)=0(0.2)+1(0.5)+2(0.3)$

$E(X)=0+0.5+0.6$

Therefore:

$E(X)=1.1$

The expected value does not have to be one of the possible outcomes.

### Python Example

```python
import numpy as np

values = np.array([0, 1, 2])
probabilities = np.array([0.2, 0.5, 0.3])

expected_value = np.sum(values * probabilities)

print("Expected value:", expected_value)
```

## 8. Variance and Standard Deviation

**Variance** measures the spread of a random variable around its mean.

The formula is:

$\mathrm{Var}(X)=E[(X-\mu)^2]$

An equivalent formula is:

$\mathrm{Var}(X)=E(X^2)-[E(X)]^2$

where \(\mu=E(X)\).

The standard deviation is the square root of variance:

$SD(X)=\sqrt{\mathrm{Var}(X)}$

### Worked Example

Using the distribution from Section 7:

$E(X)=1.1$

Calculate the second moment:

$E(X^2)=0^2(0.2)+1^2(0.5)+2^2(0.3)$

$E(X^2)=0+0.5+1.2=1.7$

Then:

$\mathrm{Var}(X)=1.7-(1.1)^2$

$\mathrm{Var}(X)=1.7-1.21=0.49$

Therefore:

$SD(X)=\sqrt{0.49}=0.7$

### Python Example

```python
import numpy as np

values = np.array([0, 1, 2])
probabilities = np.array([0.2, 0.5, 0.3])

mean = np.sum(values * probabilities)
second_moment = np.sum(values**2 * probabilities)

variance = second_moment - mean**2
standard_deviation = np.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)
```

## 9. Bernoulli Distribution

The **Bernoulli distribution** models one trial with two possible outcomes: success and failure.

Let \(p\) be the probability of success.

$P(X=1)=p$

$P(X=0)=1-p$

The PMF is:

$P(X=x)=p^x(1-p)^{1-x}$

where \(x\in\{0,1\}\).

**Mean:**

$E(X)=p$

**Variance:**

$\mathrm{Var}(X)=p(1-p)$

### Worked Example

If the probability of success is \(p=0.2\):

$P(X=1)=0.2$

$P(X=0)=0.8$

The variance is:

$\mathrm{Var}(X)=0.2(1-0.2)=0.16$

### Python Example

```python
from scipy.stats import bernoulli

p = 0.2

print("P(X = 1):", bernoulli.pmf(1, p))
print("P(X = 0):", bernoulli.pmf(0, p))
print("Mean:", bernoulli.mean(p))
print("Variance:", bernoulli.var(p))
```

**Application:** Bernoulli outcomes are useful for representing binary events such as purchase/no purchase or success/failure.

## 10. Binomial Distribution

The **Binomial distribution** models the number of successes in a fixed number of independent trials when the probability of success remains constant.

It is represented as:

$X\sim\mathrm{Binomial}(n,p)$

where:

- \(n\) = number of trials
- \(p\) = probability of success
- \(X\) = number of successes

The PMF is:

$P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}$

for \(x=0,1,\ldots,n\).

**Mean:**

$E(X)=np$

**Variance:**

$\mathrm{Var}(X)=np(1-p)$

### Conditions

1. The number of trials is fixed.
2. Each trial has two relevant outcomes.
3. Trials are independent.
4. The success probability is constant.

### Worked Example

A fair coin is tossed four times. Find the probability of exactly two Heads.

Here, \(n=4\), \(p=0.5\), and \(x=2\).

$P(X=2)=\binom{4}{2}(0.5)^2(0.5)^2$

$P(X=2)=6(0.25)(0.25)$

Therefore:

$P(X=2)=0.375$

### Python Example

```python
from scipy.stats import binom

n = 4
p = 0.5

print("P(X = 2):", binom.pmf(2, n, p))
print("P(X <= 2):", binom.cdf(2, n, p))
print("P(X >= 3):", binom.sf(2, n, p))
print("Mean:", binom.mean(n, p))
print("Variance:", binom.var(n, p))
```

`binom.sf(2, n, p)` calculates \(P(X>2)\), which equals \(P(X\geq3)\) for this integer-valued variable.

## 11. Poisson Distribution

The **Poisson distribution** models the number of events occurring in a fixed interval of time, distance, area, or another exposure unit under suitable assumptions.

It is represented as:

$X\sim\mathrm{Poisson}(\lambda)$

where \(\lambda\) is the expected number of events in the interval.

The PMF is:

$P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}$

for \(x=0,1,2,\ldots\).

**Mean:**

$E(X)=\lambda$

**Variance:**

$\mathrm{Var}(X)=\lambda$

### Worked Example

A support centre receives an average of three calls per minute. Find the probability of exactly two calls in one minute.

Here, \(\lambda=3\) and \(x=2\).

$P(X=2)=\frac{e^{-3}3^2}{2!}$

$P(X=2)=\frac{9e^{-3}}{2}$

Therefore:

$P(X=2)\approx0.2240$

### Python Example

```python
from scipy.stats import poisson

lam = 3

print("P(X = 2):", poisson.pmf(2, lam))
print("P(X <= 2):", poisson.cdf(2, lam))
print("P(X >= 2):", poisson.sf(1, lam))
print("Mean:", poisson.mean(lam))
print("Variance:", poisson.var(lam))
```

**Application:** Poisson models can be used for event counts such as incoming support tickets or website requests when the model assumptions are reasonable.

## 12. Geometric Distribution

The **Geometric distribution** models the number of independent trials required to obtain the first success.

Let \(p\) be the probability of success. Under the trials-counting convention, the PMF is:

$P(X=x)=(1-p)^{x-1}p$

for \(x=1,2,3,\ldots\).

**Mean:**

$E(X)=\frac{1}{p}$

**Variance:**

$\mathrm{Var}(X)=\frac{1-p}{p^2}$

### Worked Example

If \(p=0.2\), find the probability that the first success occurs on the third trial.

$P(X=3)=(1-0.2)^2(0.2)$

$P(X=3)=0.8^2(0.2)=0.128$

### Python Example

```python
from scipy.stats import geom

p = 0.2

print("P(X = 3):", geom.pmf(3, p))
print("Mean:", geom.mean(p))
print("Variance:", geom.var(p))
```

**Note:** Some textbooks count failures before the first success instead of the trial number. Check the definition being used.

## 13. Negative Binomial Distribution

The **Negative Binomial distribution** models the number of trials needed to obtain a specified number of successes.

Let \(X\) be the number of trials required to obtain \(r\) successes. One common PMF is:

$P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r}$

where \(x=r,r+1,\ldots\).

**Mean:**

$E(X)=\frac{r}{p}$

**Variance:**

$\mathrm{Var}(X)=\frac{r(1-p)}{p^2}$

The Geometric distribution is the special case where \(r=1\).

### Python Example

SciPy counts failures before the required number of successes. If \(F\) is the number of failures, the number of trials is \(F+r\).

```python
from scipy.stats import nbinom

r = 3
p = 0.4

# Probability of 5 failures before 3 successes
print("Probability:", nbinom.pmf(5, r, p))

print("Expected failures:", nbinom.mean(r, p))
print("Variance of failures:", nbinom.var(r, p))

# Expected number of trials under the trials-counting convention
print("Expected trials:", r / p)
```

## 14. Hypergeometric Distribution

The **Hypergeometric distribution** models the number of successes in a sample drawn without replacement from a finite population.

Let:

- \(N\) = population size
- \(K\) = number of successes in the population
- \(n\) = sample size
- \(X\) = number of successes in the sample

The PMF is:

$P(X=x)=\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}$

### Worked Example

A box contains 10 products: four defective and six non-defective. Three products are selected without replacement. Find the probability of selecting exactly two defective products.

$P(X=2)=\frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}}$

$P(X=2)=\frac{6\times6}{120}$

Therefore:

$P(X=2)=0.3$

### Python Example

```python
from scipy.stats import hypergeom

N = 10
K = 4
n = 3

print("P(X = 2):", hypergeom.pmf(2, N, K, n))
print("P(X <= 2):", hypergeom.cdf(2, N, K, n))
print("Mean:", hypergeom.mean(N, K, n))
print("Variance:", hypergeom.var(N, K, n))
```

**Important:** Sampling without replacement changes the probabilities from one draw to the next. This is why the Hypergeometric distribution differs from the Binomial distribution.

## 15. Uniform Distribution

The **continuous Uniform distribution** has constant probability density across an interval.

It is represented as:

$X\sim U(a,b)$

The PDF is:

$f(x)=\frac{1}{b-a}$ for \(a\leq x\leq b\)

Outside the interval, the density is zero.

**Mean:**

$E(X)=\frac{a+b}{2}$

**Variance:**

$\mathrm{Var}(X)=\frac{(b-a)^2}{12}$

### Worked Example

Suppose \(X\sim U(0,10)\). Find the probability that \(X\) lies between 2 and 6.

$P(2\leq X\leq6)=\frac{6-2}{10-0}$

Therefore:

$P(2\leq X\leq6)=0.4$

### Python Example

```python
from scipy.stats import uniform

a = 0
b = 10

distribution = uniform(loc=a, scale=b - a)

probability = distribution.cdf(6) - distribution.cdf(2)

print("P(2 <= X <= 6):", probability)
print("Mean:", distribution.mean())
print("Variance:", distribution.var())
```

## 16. Normal Distribution

The **Normal distribution** is a continuous, symmetric, bell-shaped probability distribution.

It is represented as:

$X\sim N(\mu,\sigma^2)$

where:

- \(\mu\) = mean
- \(\sigma^2\) = variance
- \(\sigma\) = standard deviation

The PDF is:

$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

### Important Properties

For a Normal distribution:

$\text{Mean}=\text{Median}=\text{Mode}=\mu$

The distribution is symmetric around its mean.

The approximate 68–95–99.7 rule states that:

- Approximately 68% of observations lie within one standard deviation of the mean.
- Approximately 95% lie within two standard deviations.
- Approximately 99.7% lie within three standard deviations.

### Python Example

```python
from scipy.stats import norm

mu = 100
sigma = 15

distribution = norm(loc=mu, scale=sigma)

print("Mean:", distribution.mean())
print("Variance:", distribution.var())
print("P(X <= 115):", distribution.cdf(115))

probability = distribution.cdf(115) - distribution.cdf(85)
print("P(85 <= X <= 115):", probability)
```

**Application:** Normal distributions are important in statistical analysis, measurement modelling, and sampling distributions. However, not every dataset follows a Normal distribution.

## 17. Standard Normal Distribution and Z-Scores

The **Standard Normal distribution** has a mean of 0 and a standard deviation of 1.

$Z\sim N(0,1)$

A Normal variable can be standardised using the z-score:

$Z=\frac{X-\mu}{\sigma}$

A z-score measures how many standard deviations an observation lies above or below the mean.

- Positive z-score: above the mean.
- Negative z-score: below the mean.
- Zero z-score: equal to the mean.

### Worked Example

Suppose \(X=70\), \(\mu=60\), and \(\sigma=5\).

$Z=\frac{70-60}{5}=2$

The observation is two standard deviations above the mean.

### Python Example

```python
from scipy.stats import norm

x = 70
mu = 60
sigma = 5

z_score = (x - mu) / sigma

print("Z-score:", z_score)
print("Lower-tail probability:", norm.cdf(z_score))
print("Upper-tail probability:", norm.sf(z_score))
```

## 18. Exponential Distribution

The **Exponential distribution** models continuous waiting time until an event occurs under a suitable constant-rate process.

Let:

$X\sim\mathrm{Exponential}(\lambda)$

where \(\lambda>0\) is the rate parameter.

The PDF is:

$f(x)=\lambda e^{-\lambda x}$ for \(x\geq0\)

The CDF is:

$F(x)=1-e^{-\lambda x}$ for \(x\geq0\)

**Mean:**

$E(X)=\frac{1}{\lambda}$

**Variance:**

$\mathrm{Var}(X)=\frac{1}{\lambda^2}$

### Worked Example

Suppose the average waiting time is five minutes.

Then:

$E(X)=5$

Since \(E(X)=1/\lambda\):

$\lambda=\frac{1}{5}=0.2$

The probability of waiting less than three minutes is:

$P(X\leq3)=1-e^{-0.2(3)}$

$P(X\leq3)=1-e^{-0.6}$

Therefore:

$P(X\leq3)\approx0.4512$

### Python Example

```python
from scipy.stats import expon

average_wait = 5

# SciPy uses scale = 1 / rate
distribution = expon(scale=average_wait)

print("P(X <= 3):", distribution.cdf(3))
print("Mean:", distribution.mean())
print("Variance:", distribution.var())
```

**Application:** The Exponential distribution can model waiting times between events in appropriate processes.

## 19. Memoryless Property and Poisson–Exponential Relationship

The Geometric and Exponential distributions both have a memoryless property under their standard definitions.

For the Exponential distribution:

$P(X>s+t\mid X>s)=P(X>t)$

This means that, under the model, the additional waiting time does not depend on how long the process has already lasted.

The Poisson and Exponential distributions are also related through a Poisson process with constant event rate \(\lambda\):

**Poisson distribution:** Number of events in time \(t\).

$N(t)\sim\mathrm{Poisson}(\lambda t)$

**Exponential distribution:** Waiting time until the next event.

$X\sim\mathrm{Exponential}(\lambda)$

### Python Example

```python
from scipy.stats import poisson, expon

rate = 3
time_interval = 2

# Probability of exactly 4 events in 2 time units
event_probability = poisson.pmf(
    4, rate * time_interval
)

# Probability of waiting at most 1 time unit
waiting_probability = expon.cdf(
    1, scale=1 / rate
)

print("P(4 events in 2 units):", event_probability)
print("P(wait <= 1 unit):", waiting_probability)
```

## 20. Rules for Expected Value and Variance

For constants \(a\) and \(b\):

$E(aX+b)=aE(X)+b$

For variance:

$\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$

Adding a constant changes the mean but does not change the variance. Multiplying a random variable by a constant changes the variance by the square of that constant.

For two random variables:

$E(X+Y)=E(X)+E(Y)$

For the variance of their sum:

$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$

For independent random variables, covariance is zero. Therefore:

$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$

For independent random variables \(X_1,\ldots,X_n\):

$\mathrm{Var}\left(\sum_{i=1}^{n}X_i\right)=\sum_{i=1}^{n}\mathrm{Var}(X_i)$

### Python Example

```python
import numpy as np

data = np.array([10, 12, 14, 16, 18])

a = 3
b = 5

transformed = a * data + b

print("Original mean:", data.mean())
print("Transformed mean:", transformed.mean())

print("Original variance:", data.var())
print("Transformed variance:", transformed.var())
```

NumPy's default `var()` uses population variance (`ddof=0`).

## 21. Law of Total Expectation

The **law of total expectation** states:

$E(X)=E[E(X\mid Y)]$

For a discrete variable \(Y\):

$E(X)=\sum_y E(X\mid Y=y)P(Y=y)$

This rule calculates an overall expected value by averaging conditional expected values across groups.

### Worked Example

Suppose 60% of customers belong to Group A and 40% belong to Group B.

Their expected purchase amounts are 100 and 200, respectively.

$E(X)=100(0.6)+200(0.4)$

$E(X)=60+80=140$

### Python Example

```python
import numpy as np

conditional_means = np.array([100, 200])
group_probabilities = np.array([0.6, 0.4])

overall_mean = np.sum(
    conditional_means * group_probabilities
)

print("Overall expected value:", overall_mean)
```

## 22. Central Limit Theorem

The **Central Limit Theorem (CLT)** explains why the sampling distribution of a sample mean becomes approximately Normal under suitable conditions as the sample size increases.

Suppose independent observations have mean \(\mu\) and variance \(\sigma^2\).

For a sample of size \(n\):

$\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i$

The expected value of the sample mean is:

$E(\bar{X})=\mu$

Its variance is:

$\mathrm{Var}(\bar{X})=\frac{\sigma^2}{n}$

Its standard error is:

$SE(\bar{X})=\frac{\sigma}{\sqrt{n}}$

The CLT concerns the sampling distribution of the statistic, not the claim that the original observations must become Normal.

### Python Example

```python
import numpy as np

rng = np.random.default_rng(42)

sample_size = 50
number_of_samples = 5000

sample_means = np.array([
    rng.exponential(scale=1, size=sample_size).mean()
    for _ in range(number_of_samples)
])

print("Mean of sample means:", sample_means.mean())
print("SD of sample means:", sample_means.std())
```

The sample means tend to form a more symmetric distribution than the original right-skewed Exponential distribution.

## 23. Choosing the Correct Distribution

Selecting a probability distribution requires understanding the random variable and the process that generates the data.

| Situation | Possible Distribution |
|---|---|
| One success/failure trial | Bernoulli |
| Number of successes in fixed independent trials | Binomial |
| Event count in a fixed interval | Poisson |
| Number of trials until the first success | Geometric |
| Trials until a specified number of successes | Negative Binomial |
| Sampling without replacement | Hypergeometric |
| Continuous variable with constant density over an interval | Uniform |
| Continuous variable with a symmetric bell-shaped model | Normal |
| Waiting time under a constant-rate process | Exponential |

These are modelling guidelines, not automatic rules. The assumptions must fit the problem.

## 24. Common Mistakes

**1. Confusing PMF and PDF.** The PMF gives probabilities for discrete values; the PDF gives density for continuous values.

**2. Treating a PDF value as a probability.** A continuous probability is calculated from an interval's area or a CDF difference.

**3. Ignoring Binomial assumptions.** A fixed number of independent trials and a constant success probability are required.

**4. Confusing the Poisson parameter with a probability.** The parameter \(\lambda\) represents an expected event count or rate-scaled interval.

**5. Confusing variance with standard deviation.** Variance is in squared units; standard deviation is in the original units.

**6. Assuming all data follow a Normal distribution.** The model must be appropriate for the data and task.

**7. Confusing Geometric and Exponential distributions.** Geometric is discrete; Exponential is continuous.

**8. Ignoring sampling without replacement.** A Hypergeometric model may be needed for finite-population sampling.

**9. Misinterpreting the CLT.** The CLT concerns the distribution of suitable sample statistics, not necessarily the original data.

**10. Mixing up software parameterisations.** Check whether a library counts trials or failures, particularly for Geometric and Negative Binomial distributions.

## 25. Points to Remember

1. A probability distribution describes how probabilities are assigned to a random variable.
2. Discrete distributions use PMFs; continuous distributions use PDFs.
3. The CDF gives \(P(X\leq x)\).
4. The expected value describes a theoretical long-run average.
5. Variance measures spread, and standard deviation is its square root.
6. Bernoulli models one binary trial.
7. Binomial models successes in a fixed number of independent trials.
8. Poisson models event counts under suitable assumptions.
9. Geometric and Negative Binomial distributions model trials until successes.
10. Hypergeometric models sampling without replacement.
11. Uniform has constant density across an interval.
12. Normal is a symmetric bell-shaped distribution.
13. Z-scores express distance from the mean in standard-deviation units.
14. Exponential models waiting time under a constant-rate process.
15. Poisson and Exponential distributions are related through the Poisson process.
16. The CLT explains the approximate Normality of suitable sampling distributions.
17. Always check assumptions before selecting a distribution.
18. NumPy and SciPy provide practical tools for probability calculations and simulation.

## 26. Important Formula Summary

### Probability Functions

**PMF**

$p_X(x)=P(X=x)$

**CDF**

$F_X(x)=P(X\leq x)$

**Continuous interval probability**

$P(a\leq X\leq b)=\int_a^b f_X(x)\,dx$

### Expected Value and Variance

**Discrete expected value**

$E(X)=\sum_x xP(X=x)$

**Continuous expected value**

$E(X)=\int_{-\infty}^{\infty}xf_X(x)\,dx$

**Variance**

$\mathrm{Var}(X)=E[(X-E(X))^2]$

**Alternative variance formula**

$\mathrm{Var}(X)=E(X^2)-[E(X)]^2$

**Standard deviation**

$SD(X)=\sqrt{\mathrm{Var}(X)}$

### Bernoulli Distribution

$P(X=x)=p^x(1-p)^{1-x}$

$E(X)=p$

$\mathrm{Var}(X)=p(1-p)$

### Binomial Distribution

$P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}$

$E(X)=np$

$\mathrm{Var}(X)=np(1-p)$

### Poisson Distribution

$P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}$

$E(X)=\mathrm{Var}(X)=\lambda$

### Geometric Distribution

$P(X=x)=(1-p)^{x-1}p$

$E(X)=\frac{1}{p}$

$\mathrm{Var}(X)=\frac{1-p}{p^2}$

### Negative Binomial Distribution

$P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r}$

$E(X)=\frac{r}{p}$

$\mathrm{Var}(X)=\frac{r(1-p)}{p^2}$

### Hypergeometric Distribution

$P(X=x)=\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}$

### Uniform Distribution

$f(x)=\frac{1}{b-a}$ for \(a\leq x\leq b\)

$E(X)=\frac{a+b}{2}$

$\mathrm{Var}(X)=\frac{(b-a)^2}{12}$

### Normal Distribution

$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

$Z=\frac{X-\mu}{\sigma}$

### Exponential Distribution

$f(x)=\lambda e^{-\lambda x}$ for \(x\geq0\)

$F(x)=1-e^{-\lambda x}$ for \(x\geq0\)

$E(X)=\frac{1}{\lambda}$

$\mathrm{Var}(X)=\frac{1}{\lambda^2}$

### Variance of a Sum

For two random variables with finite variances:

$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$

For independent random variables:

$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$

### Standard Error of the Sample Mean

$SE(\bar{X})=\frac{\sigma}{\sqrt{n}}$

---

## 29. References

### GeeksforGeeks

- [Statistics](https://www.geeksforgeeks.org/maths/statistics/)
- [Probability](https://www.geeksforgeeks.org/maths/probability/)

### OpenStax

- [Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e)

### SciPy Documentation

- [Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Continuous and Discrete Distributions](https://docs.scipy.org/doc/scipy/reference/stats.html)

### NumPy Documentation

- [NumPy User Guide](https://numpy.org/doc/stable/)
- [Random Sampling](https://numpy.org/doc/stable/reference/random/index.html)
