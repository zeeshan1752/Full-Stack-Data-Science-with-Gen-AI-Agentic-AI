# Probability Distributions

## Chapter Overview

A **probability distribution** describes how probabilities are assigned to the possible values of a random variable. It provides a mathematical framework for understanding uncertainty, calculating probabilities, analysing data, and building statistical models.

Probability distributions are fundamental to Data Science and Machine Learning. They are used to model customer purchases, website traffic, waiting times, measurement errors, model predictions, and many other real-world phenomena.

This chapter covers discrete and continuous random variables, probability mass functions, probability density functions, cumulative distribution functions, expected value, variance, important probability distributions, and their implementation using Python.

### Learning Objectives

After completing this chapter, you should be able to:

- Distinguish between discrete and continuous random variables.
- Understand and calculate probabilities using PMFs, PDFs, and CDFs.
- Calculate expected value, variance, and standard deviation.
- Identify and apply common probability distributions.
- Implement probability calculations using NumPy and SciPy.
- Select a suitable distribution based on the problem and its assumptions.
- Understand the role of probability distributions in statistical modelling and Machine Learning.

---

## 1. Introduction to Probability Distributions

A probability distribution describes the possible outcomes of a random variable and the probability associated with each outcome or range of outcomes.

A **random variable** is a numerical representation of the outcome of a random process.

For example, suppose a fair coin is tossed three times. Let \(X\) represent the number of Heads obtained.

The possible values are:

$$
X \in \{0,1,2,3\}
$$

The probability distribution is:

| Number of Heads ($X$) | Probability $P(X=x)$ |
|---:|---:|
| 0 | 0.125 |
| 1 | 0.375 |
| 2 | 0.375 |
| 3 | 0.125 |

A valid probability distribution must satisfy two conditions.

**Condition 1: Non-negative probabilities**

$$
P(X=x)\geq 0
$$

**Condition 2: Total probability equals one**

$$
\sum_x P(X=x)=1
$$

For continuous distributions, the corresponding condition is that the total area under the probability density curve equals one.

Probability distributions help us answer questions such as:

- What is the probability that a customer purchases a product?
- How many support tickets might arrive in one hour?
- What is the probability that a waiting time is less than five minutes?
- How much variation should we expect in a model's predictions?

---

## 2. Discrete and Continuous Random Variables

Random variables are commonly classified as discrete or continuous.

### 2.1 Discrete Random Variables

A **discrete random variable** takes a finite or countably infinite set of values.

Examples include:

- Number of purchases made by a customer.
- Number of defective products in a batch.
- Number of emails received in an hour.
- Number of successful predictions in a set of trials.

Discrete random variables are described using a Probability Mass Function (PMF).

For example, the number of purchases might take values such as 0, 1, 2, 3, and so on.

### 2.2 Continuous Random Variables

A **continuous random variable** can take any value within an interval of the real number line.

Examples include:

- Customer waiting time.
- Product weight.
- Temperature.
- Distance travelled.
- Time required to complete a task.

Continuous random variables are described using a Probability Density Function (PDF).

For a continuous random variable, the probability of an exact value is zero:

$$
P(X=a)=0
$$

Probabilities are calculated over intervals:

$$
P(a\leq X\leq b)=\int_a^b f_X(x)\,dx
$$

### 2.3 Comparison

| Feature | Discrete Random Variable | Continuous Random Variable |
|---|---|---|
| Possible values | Finite or countable | Values across an interval |
| Main function | PMF | PDF |
| Probability calculation | Sum of probabilities | Area under the density curve |
| Probability of an exact value | Can be positive | Zero |
| Examples | Binomial, Poisson | Normal, Uniform, Exponential |

### 2.4 Python Example

```python
import numpy as np

# Discrete observations: number of purchases
purchases = np.array([0, 1, 2, 3, 4])

# Continuous observations: waiting times
waiting_times = np.array([1.2, 2.5, 3.1, 4.7, 5.4])

print("Purchase counts:", purchases)
print("Waiting times:", waiting_times)
```

The arrays contain sample observations. The classification depends on the type of variable being measured, not simply on whether its values are stored as integers or floating-point numbers.

---

## 3. Probability Mass Function (PMF)

A **Probability Mass Function (PMF)** gives the probability that a discrete random variable takes a particular value.

It is defined as:

$$
p_X(x)=P(X=x)
$$

A valid PMF satisfies:

$$
p_X(x)\geq 0
$$

and

$$
\sum_x p_X(x)=1
$$

### 3.1 Worked Example

Suppose the random variable \(X\) has the following distribution.

| $x$ | $P(X=x)$ |
|---:|---:|
| 0 | 0.2 |
| 1 | 0.5 |
| 2 | 0.3 |

Check whether the distribution is valid.

**Step 1: Add the probabilities.**

$$
0.2+0.5+0.3=1
$$

**Step 2: Check non-negativity.**

All probabilities are non-negative.

Therefore, this is a valid probability distribution.

The probability that \(X=1\) is:

$$
P(X=1)=0.5
$$

### 3.2 Python Implementation

```python
import numpy as np

values = np.array([0, 1, 2])
probabilities = np.array([0.2, 0.5, 0.3])

print("P(X = 1):", probabilities[1])
print("Total probability:", probabilities.sum())
print("All probabilities non-negative:",
      np.all(probabilities >= 0))
```

For a manually defined PMF, always check that the probabilities are non-negative and sum to one.

---

## 4. Probability Density Function (PDF)

A **Probability Density Function (PDF)** describes the density of probability for a continuous random variable. It is represented by \(f_X(x)\).

A valid PDF satisfies:

$$
f_X(x)\geq 0
$$

and

$$
\int_{-\infty}^{\infty}f_X(x)\,dx=1
$$

The probability that \(X\) lies between \(a\) and \(b\) is:

$$
P(a\leq X\leq b)=\int_a^b f_X(x)\,dx
$$

The total area under the density curve equals one.

**Important:** A PDF value is a density, not the probability of an exact observation. A density value can even exceed one, provided the total area under the curve remains one.

### 4.1 Python Implementation

```python
from scipy.stats import norm

# Standard Normal distribution
density = norm.pdf(0)

print("Density at X = 0:", density)
```

The result is approximately `0.3989`. This is the density at zero, not the probability that the variable equals zero.

To calculate an interval probability, use the CDF or integrate the PDF over that interval.

---

## 5. Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)** gives the probability that a random variable is less than or equal to a particular value.

It is defined as:

$$
F_X(x)=P(X\leq x)
$$

For a discrete random variable:

$$
F_X(x)=\sum_{t\leq x}P(X=t)
$$

For a continuous random variable:

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
$$

A CDF has the following properties:

- Its values lie between zero and one.
- It is non-decreasing.
- It approaches zero as \(x\) approaches negative infinity.
- It approaches one as \(x\) approaches positive infinity.

### 5.1 Worked Example

Suppose a random variable has the distribution:

| $x$ | $P(X=x)$ |
|---:|---:|
| 0 | 0.2 |
| 1 | 0.5 |
| 2 | 0.3 |

Find \(P(X\leq 1)\).

**Step 1: Add the probabilities for all values up to 1.**

$$
P(X\leq 1)=P(X=0)+P(X=1)
$$

**Step 2: Substitute the probabilities.**

$$
P(X\leq 1)=0.2+0.5
$$

Therefore:

$$
P(X\leq 1)=0.7
$$

### 5.2 Python Implementation

```python
from scipy.stats import norm

x = 1

probability = norm.cdf(x)

print("P(Z <= 1):", probability)
```

For a standard Normal random variable, the result is approximately `0.8413`.

---

## 6. Relationship Between PMF, PDF, and CDF

PMF, PDF, and CDF are three important ways of describing a probability distribution.

| Function | Meaning | Used For |
|---|---|---|
| PMF | Probability of an individual value | Discrete distributions |
| PDF | Density of probability | Continuous distributions |
| CDF | Probability up to a value | Both discrete and continuous distributions |

For a continuous distribution, the PDF and CDF are related by differentiation when the derivative exists:

$$
f_X(x)=\frac{d}{dx}F_X(x)
$$

The CDF is obtained by integrating the PDF:

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
$$

The probability of an interval can be calculated using the CDF:

$$
P(a<X\leq b)=F_X(b)-F_X(a)
$$

For a continuous random variable, including or excluding interval endpoints does not change the probability.

### 6.1 Worked Example

Let \(Z\) follow a standard Normal distribution. Find:

$$
P(-1<Z\leq 1)
$$

Using the CDF:

$$
P(-1<Z\leq 1)=F_Z(1)-F_Z(-1)
$$

The corresponding CDF values are approximately:

$$
F_Z(1)=0.8413
$$

$$
F_Z(-1)=0.1587
$$

Therefore:

$$
P(-1<Z\leq 1)\approx 0.8413-0.1587
$$

$$
P(-1<Z\leq 1)\approx 0.6826
$$

Approximately 68.27% of observations from a standard Normal distribution lie between minus one and plus one standard deviations from the mean.

### 6.2 Python Implementation

```python
from scipy.stats import norm

lower = -1
upper = 1

probability = norm.cdf(upper) - norm.cdf(lower)

print("P(-1 < Z <= 1):", probability)
```

---

## 7. Expected Value

The **expected value** is the theoretical long-run average of a random variable under its probability distribution.

It is also called the mathematical expectation or population mean of the distribution.

### 7.1 Expected Value of a Discrete Random Variable

$$
E(X)=\sum_x xP(X=x)
$$

Here:

- \(X\) = random variable.
- \(x\) = a possible value of the variable.
- \(P(X=x)\) = probability of that value.

### 7.2 Expected Value of a Continuous Random Variable

$$
E(X)=\int_{-\infty}^{\infty}xf_X(x)\,dx
$$

### 7.3 Worked Example

Suppose the probability distribution is:

| $X$ | $P(X=x)$ |
|---:|---:|
| 0 | 0.2 |
| 1 | 0.5 |
| 2 | 0.3 |

Calculate the expected value.

**Step 1: Multiply each value by its probability.**

$$
E(X)=0(0.2)+1(0.5)+2(0.3)
$$

**Step 2: Calculate the sum.**

$$
E(X)=0+0.5+0.6
$$

Therefore:

$$
E(X)=1.1
$$

The expected value is 1.1, even though 1.1 is not a possible outcome of this random variable.

### 7.4 Python Implementation

```python
import numpy as np

values = np.array([0, 1, 2])
probabilities = np.array([0.2, 0.5, 0.3])

expected_value = np.sum(values * probabilities)

print("Expected value:", expected_value)
```

### 7.5 Applications

Expected value is useful for:

- Estimating average customer spending.
- Calculating expected demand.
- Evaluating expected profit or loss.
- Understanding the average number of events.
- Calculating theoretical means for probability models.

---

## 8. Variance and Standard Deviation

**Variance** measures the expected squared deviation of a random variable from its mean.

It describes the spread of a probability distribution.

Let the mean be:

$$
\mu=E(X)
$$

The variance is:

$$
\mathrm{Var}(X)=E[(X-\mu)^2]
$$

An equivalent formula is:

$$
\mathrm{Var}(X)=E(X^2)-[E(X)]^2
$$

The standard deviation is the square root of variance:

$$
\sigma=\sqrt{\mathrm{Var}(X)}
$$

Variance is expressed in squared units, while standard deviation is expressed in the original units of the variable.

### 8.1 Worked Example

Using the distribution from Section 7, we already know:

$$
E(X)=1.1
$$

First, calculate the second moment:

$$
E(X^2)=\sum_x x^2P(X=x)
$$

Substituting the values:

$$
E(X^2)=0^2(0.2)+1^2(0.5)+2^2(0.3)
$$

$$
E(X^2)=0+0.5+1.2=1.7
$$

Now calculate the variance:

$$
\mathrm{Var}(X)=E(X^2)-[E(X)]^2
$$

$$
\mathrm{Var}(X)=1.7-(1.1)^2
$$

$$
\mathrm{Var}(X)=1.7-1.21=0.49
$$

Finally, calculate the standard deviation:

$$
\sigma=\sqrt{0.49}=0.7
$$

**Interpretation:** The distribution has a mean of 1.1, variance of 0.49, and standard deviation of 0.7.

### 8.2 Python Implementation

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

This calculates the theoretical variance of the probability distribution. It is different from estimating sample variance from observed data.

---

## 9. Bernoulli Distribution

The **Bernoulli distribution** models a single trial with two possible outcomes, usually called success and failure.

Let \(p\) be the probability of success. Then the probability of failure is \(1-p\).

The random variable takes values:

$$
X\in\{0,1\}
$$

Its PMF is:

$$
P(X=x)=p^x(1-p)^{1-x}
$$

where \(x\) is either zero or one.

The mean is:

$$
E(X)=p
$$

The variance is:

$$
\mathrm{Var}(X)=p(1-p)
$$

### 9.1 Worked Example

Suppose the probability that a customer purchases a product is 0.2.

Let \(X=1\) represent a purchase and \(X=0\) represent no purchase.

The probability of purchase is:

$$
P(X=1)=0.2
$$

The probability of no purchase is:

$$
P(X=0)=1-0.2=0.8
$$

The expected value is:

$$
E(X)=0.2
$$

The variance is:

$$
\mathrm{Var}(X)=0.2(1-0.2)=0.16
$$

### 9.2 Python Implementation

```python
from scipy.stats import bernoulli

p = 0.2

print("P(X = 1):", bernoulli.pmf(1, p))
print("P(X = 0):", bernoulli.pmf(0, p))
print("Mean:", bernoulli.mean(p))
print("Variance:", bernoulli.var(p))
```

### 9.3 Applications

Bernoulli models are useful for binary outcomes, including:

- Purchase or no purchase.
- Churn or no churn.
- Fraud or no fraud.
- Success or failure.
- Click or no click.

In classification, a binary target can be represented using zero and one, although a classifier's predicted probability is not itself automatically a Bernoulli observation.

---

## 10. Binomial Distribution

The **Binomial distribution** models the number of successes in a fixed number of independent trials, where each trial has the same probability of success.

It is represented as:

$$
X\sim\mathrm{Binomial}(n,p)
$$

Where:

- \(X\) = number of successes.
- \(n\) = total number of trials.
- \(p\) = probability of success on each trial.

The PMF is:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

for \(x=0,1,\ldots,n\).

The combination term is:

$$
\binom{n}{x}=\frac{n!}{x!(n-x)!}
$$

The mean is:

$$
E(X)=np
$$

The variance is:

$$
\mathrm{Var}(X)=np(1-p)
$$

### 10.1 Conditions for the Binomial Distribution

A Binomial model is appropriate when:

1. The number of trials is fixed.
2. Each trial has two relevant outcomes.
3. Trials are independent.
4. The probability of success remains constant.

If these conditions do not hold, another model may be more suitable.

### 10.2 Worked Example

A fair coin is tossed four times. Find the probability of obtaining exactly two Heads.

Given:

- \(n=4\)
- \(p=0.5\)
- \(x=2\)

Using the Binomial PMF:

$$
P(X=2)=\binom{4}{2}(0.5)^2(1-0.5)^2
$$

Calculate the combination:

$$
\binom{4}{2}=\frac{4!}{2!2!}=6
$$

Substitute:

$$
P(X=2)=6(0.5)^2(0.5)^2
$$

$$
P(X=2)=6(0.0625)=0.375
$$

Therefore, the probability is 0.375, or 37.5%.

### 10.3 Python Implementation

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

`binom.sf(2, n, p)` calculates \(P(X>2)\), which is the same as \(P(X\geq3)\) for this integer-valued variable.

### 10.4 Applications

The Binomial distribution is useful for modelling the number of successes among a fixed number of independent binary outcomes, such as purchases among a fixed set of customers when the model assumptions are reasonable.

---

## 11. Poisson Distribution

The **Poisson distribution** models the number of events occurring in a fixed interval of time, distance, area, or another exposure unit.

It is commonly used when events occur according to a suitable constant-rate process.

The distribution is represented as:

$$
X\sim\mathrm{Poisson}(\lambda)
$$

Here, \(\lambda\) is the expected number of events in the interval being modelled.

The PMF is:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}
$$

where \(x=0,1,2,\ldots\).

The mean and variance are:

$$
E(X)=\lambda
$$

$$
\mathrm{Var}(X)=\lambda
$$

### 11.1 Worked Example

A support centre receives an average of three calls per minute. Find the probability of receiving exactly two calls in one minute.

Given:

$$
\lambda=3,\qquad x=2
$$

Using the Poisson PMF:

$$
P(X=2)=\frac{e^{-3}3^2}{2!}
$$

Simplifying:

$$
P(X=2)=\frac{9e^{-3}}{2}
$$

Therefore:

$$
P(X=2)\approx0.2240
$$

The probability is approximately 22.4%.

### 11.2 Python Implementation

```python
from scipy.stats import poisson

lam = 3

print("P(X = 2):", poisson.pmf(2, lam))
print("P(X <= 2):", poisson.cdf(2, lam))
print("P(X >= 2):", poisson.sf(1, lam))

print("Mean:", poisson.mean(lam))
print("Variance:", poisson.var(lam))
```

The survival function call `poisson.sf(1, lam)` calculates \(P(X>1)\), equivalent to \(P(X\geq2)\).

### 11.3 Applications

Poisson models can be useful for:

- Website requests per minute.
- Support tickets per hour.
- Defects per unit of production.
- Incoming calls.
- Other event counts over a defined interval.

The model should not be selected simply because the data contain counts. Its assumptions and fit must also be considered.

---

## 12. Geometric Distribution

The **Geometric distribution** models the number of independent trials required to obtain the first success when the probability of success remains constant.

In this chapter, \(X\) counts the trial on which the first success occurs.

Its PMF is:

$$
P(X=x)=(1-p)^{x-1}p
$$

where \(x=1,2,3,\ldots\).

The mean is:

$$
E(X)=\frac{1}{p}
$$

The variance is:

$$
\mathrm{Var}(X)=\frac{1-p}{p^2}
$$

### 12.1 Worked Example

Suppose the probability of success on each trial is \(p=0.2\). Find the probability that the first success occurs on the third trial.

$$
P(X=3)=(1-p)^{3-1}p
$$

Substituting:

$$
P(X=3)=(1-0.2)^2(0.2)
$$

$$
P(X=3)=0.8^2(0.2)=0.128
$$

The probability is 12.8%.

The expected number of trials is:

$$
E(X)=\frac{1}{0.2}=5
$$

### 12.2 Python Implementation

```python
from scipy.stats import geom

p = 0.2

print("P(X = 3):", geom.pmf(3, p))
print("Mean:", geom.mean(p))
print("Variance:", geom.var(p))
```

**Important:** Some textbooks define the Geometric distribution as the number of failures before the first success. SciPy's `geom` uses the trial-number convention, starting at one.

---

## 13. Negative Binomial Distribution

The **Negative Binomial distribution** models the number of trials required to obtain a specified number of successes in independent Bernoulli trials with constant success probability.

Let:

- \(r\) = required number of successes.
- \(p\) = probability of success on each trial.
- \(X\) = total number of trials required.

Under the trials-counting convention, the PMF is:

$$
P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r}
$$

where \(x=r,r+1,\ldots\).

The mean is:

$$
E(X)=\frac{r}{p}
$$

The variance is:

$$
\mathrm{Var}(X)=\frac{r(1-p)}{p^2}
$$

The Geometric distribution is a special case of the Negative Binomial distribution when \(r=1\).

### 13.1 Python Implementation

SciPy's `nbinom` counts the number of failures before the required number of successes, rather than the total number of trials.

```python
from scipy.stats import nbinom

r = 3
p = 0.4

# Probability of 5 failures before 3 successes
print("Probability:", nbinom.pmf(5, r, p))

print("Expected failures:", nbinom.mean(r, p))
print("Variance of failures:", nbinom.var(r, p))

# Expected total number of trials
print("Expected trials:", r / p)
```

The expected number of failures is \(r(1-p)/p\). Adding the required number of successes gives the expected number of trials, \(r/p\).

### 13.2 Applications

The Negative Binomial distribution can model the number of attempts required to achieve a target number of successes. In data analysis, a related Negative Binomial count model is also used for overdispersed count data, where the variance exceeds the mean.

---

## 14. Hypergeometric Distribution

The **Hypergeometric distribution** models the number of successes in a sample drawn without replacement from a finite population.

Let:

- \(N\) = population size.
- \(K\) = number of successes in the population.
- \(n\) = sample size.
- \(X\) = number of successes in the sample.

The PMF is:

$$
P(X=x)=
\frac{\binom{K}{x}\binom{N-K}{n-x}}
{\binom{N}{n}}
$$

### 14.1 Worked Example

A box contains ten products: four defective and six non-defective. Three products are selected without replacement.

Find the probability of selecting exactly two defective products.

Given:

$$
N=10,\qquad K=4,\qquad n=3,\qquad x=2
$$

Using the PMF:

$$
P(X=2)=
\frac{\binom{4}{2}\binom{6}{1}}
{\binom{10}{3}}
$$

Calculate the combinations:

$$
P(X=2)=\frac{6\times6}{120}
$$

Therefore:

$$
P(X=2)=0.3
$$

The probability is 30%.

### 14.2 Python Implementation

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

### 14.3 Binomial vs Hypergeometric Distribution

| Feature | Binomial | Hypergeometric |
|---|---|---|
| Population | Often modelled as repeated independent trials | Finite population |
| Sampling | Independent trials | Without replacement |
| Success probability | Constant | Changes across draws |
| Main use | Independent binary outcomes | Finite-population sampling |

When sampling without replacement, the Hypergeometric distribution may be more appropriate than the Binomial distribution.

---

## 15. Uniform Distribution

The **continuous Uniform distribution** models a variable whose probability density is constant across a specified interval.

It is represented as:

$$
X\sim U(a,b)
$$

where \(a\) is the lower limit and \(b\) is the upper limit, with \(a<b\).

The PDF is:

$$
f_X(x)=\frac{1}{b-a},\qquad a\leq x\leq b
$$

Outside the interval, the density is zero.

The mean is:

$$
E(X)=\frac{a+b}{2}
$$

The variance is:

$$
\mathrm{Var}(X)=\frac{(b-a)^2}{12}
$$

### 15.1 Worked Example

Suppose \(X\sim U(0,10)\). Find the probability that \(X\) lies between 2 and 6.

For a continuous Uniform distribution, the interval probability is the interval length divided by the total interval length:

$$
P(2\leq X\leq6)=\frac{6-2}{10-0}
$$

Therefore:

$$
P(2\leq X\leq6)=0.4
$$

The probability is 40%.

### 15.2 Python Implementation

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

In SciPy, `loc` represents the lower endpoint and `scale` represents the interval width.

---

## 16. Normal Distribution

The **Normal distribution** is a continuous, symmetric, bell-shaped probability distribution. It is widely used in statistical modelling and inference.

It is represented as:

$$
X\sim N(\mu,\sigma^2)
$$

where:

- \(\mu\) = mean.
- \(\sigma^2\) = variance.
- \(\sigma\) = standard deviation.

The PDF is:

$$
f_X(x)=
\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

For a Normal distribution:

$$
\text{Mean}=\text{Median}=\text{Mode}=\mu
$$

The distribution is symmetric around its mean.

### 16.1 The 68–95–99.7 Rule

For a Normal distribution, approximately:

- 68% of observations lie within one standard deviation of the mean.
- 95% lie within two standard deviations.
- 99.7% lie within three standard deviations.

These are approximate probabilities, not exact percentages.

### 16.2 Worked Example

Suppose examination scores follow a Normal distribution with mean 100 and standard deviation 15.

Find the probability that a score is between 85 and 115.

Given:

$$
\mu=100,\qquad \sigma=15
$$

The interval is one standard deviation below and above the mean.

Standardise the endpoints:

$$
Z_1=\frac{85-100}{15}=-1
$$

$$
Z_2=\frac{115-100}{15}=1
$$

Therefore:

$$
P(85\leq X\leq115)=P(-1\leq Z\leq1)
$$

The probability is approximately:

$$
P(85\leq X\leq115)\approx0.6827
$$

Approximately 68.27% of scores are expected to lie in this interval under the model.

### 16.3 Python Implementation

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

### 16.4 Applications

The Normal distribution is important in:

- Statistical inference.
- Measurement-error modelling.
- Understanding sampling distributions.
- Some Machine Learning assumptions and statistical methods.
- Modelling approximately symmetric continuous measurements.

Not every dataset follows a Normal distribution. The suitability of the model should be assessed rather than assumed.

---

## 17. Standard Normal Distribution and Z-Scores

The **Standard Normal distribution** is a Normal distribution with mean zero and standard deviation one.

It is represented as:

$$
Z\sim N(0,1)
$$

A value from a Normal distribution can be standardised using the z-score:

$$
Z=\frac{X-\mu}{\sigma}
$$

where:

- \(X\) = observed value.
- \(\mu\) = population mean.
- \(\sigma\) = population standard deviation.
- \(Z\) = standardised value.

A z-score indicates how many standard deviations an observation lies above or below the mean.

- Positive z-score: above the mean.
- Negative z-score: below the mean.
- Zero z-score: equal to the mean.

### 17.1 Worked Example

Suppose:

$$
X=70,\qquad \mu=60,\qquad \sigma=5
$$

Calculate the z-score:

$$
Z=\frac{70-60}{5}
$$

$$
Z=2
$$

The observation is two standard deviations above the mean.

### 17.2 Python Implementation

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

The lower-tail probability is \(P(Z\leq2)\), while the upper-tail probability is \(P(Z>2)\).

**Note:** When the population standard deviation is unknown and estimated from sample data, the appropriate standardisation and statistical procedure may differ. A t-distribution is often used in relevant inference problems.

---

## 18. Exponential Distribution

The **Exponential distribution** models continuous waiting time until an event occurs under a suitable constant-rate process.

It is commonly associated with the waiting time between events in a Poisson process.

Let:

$$
X\sim\mathrm{Exponential}(\lambda)
$$

where \(\lambda>0\) is the rate parameter.

The PDF is:

$$
f_X(x)=\lambda e^{-\lambda x},\qquad x\geq0
$$

The CDF is:

$$
F_X(x)=1-e^{-\lambda x},\qquad x\geq0
$$

The mean is:

$$
E(X)=\frac{1}{\lambda}
$$

The variance is:

$$
\mathrm{Var}(X)=\frac{1}{\lambda^2}
$$

### 18.1 Worked Example

Suppose the average waiting time for a service is five minutes.

The mean waiting time is:

$$
E(X)=5
$$

Since the mean equals \(1/\lambda\):

$$
\frac{1}{\lambda}=5
$$

Therefore:

$$
\lambda=\frac{1}{5}=0.2
$$

Find the probability that the waiting time is less than or equal to three minutes.

Using the CDF:

$$
P(X\leq3)=1-e^{-\lambda(3)}
$$

Substituting \(\lambda=0.2\):

$$
P(X\leq3)=1-e^{-0.6}
$$

Therefore:

$$
P(X\leq3)\approx0.4512
$$

The probability is approximately 45.12%.

### 18.2 Python Implementation

```python
from scipy.stats import expon

average_wait = 5

# SciPy uses scale = 1 / rate
distribution = expon(scale=average_wait)

print("P(X <= 3):", distribution.cdf(3))
print("Mean:", distribution.mean())
print("Variance:", distribution.var())
```

### 18.3 Applications

The Exponential distribution can be used to model:

- Waiting time between incoming requests.
- Time between events in suitable processes.
- Certain reliability and lifetime models.
- Service waiting times under appropriate assumptions.

---

## 19. Memoryless Property and the Poisson–Exponential Relationship

### 19.1 Memoryless Property

A distribution is memoryless when the remaining waiting time does not depend on how much time has already elapsed, under the model.

The Exponential distribution satisfies:

$$
P(X>s+t\mid X>s)=P(X>t)
$$

for \(s,t\geq0\).

The Geometric distribution has the corresponding property in its discrete setting.

This property is not shared by all probability distributions.

### 19.2 Relationship Between Poisson and Exponential Distributions

The Poisson and Exponential distributions are related through a Poisson process with constant event rate \(\lambda\).

The Poisson distribution models the number of events during a time interval \(t\):

$$
N(t)\sim\mathrm{Poisson}(\lambda t)
$$

The Exponential distribution models the waiting time until the next event:

$$
X\sim\mathrm{Exponential}(\lambda)
$$

For a Poisson process:

- The number of events in an interval follows a Poisson model.
- The waiting time between consecutive events follows an Exponential model.

### 19.3 Python Implementation

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

The rate and time units must be consistent. For example, if the rate is events per minute, the interval must be expressed in minutes.

---

## 20. Rules for Expected Value and Variance

Expected value and variance follow useful mathematical rules that simplify probability calculations.

### 20.1 Linear Transformation of Expected Value

For constants \(a\) and \(b\):

$$
E(aX+b)=aE(X)+b
$$

Multiplying a random variable by a constant scales its expected value. Adding a constant shifts its expected value.

### 20.2 Linear Transformation of Variance

$$
\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)
$$

Adding a constant does not change variance. Multiplying a random variable by a constant changes the variance by the square of that constant.

### 20.3 Expected Value of a Sum

For random variables \(X\) and \(Y\):

$$
E(X+Y)=E(X)+E(Y)
$$

This rule does not require independence, provided the relevant expectations exist.

### 20.4 Variance of a Sum

For two random variables with finite variances:

$$
\mathrm{Var}(X+Y)=
\mathrm{Var}(X)+\mathrm{Var}(Y)
+2\mathrm{Cov}(X,Y)
$$

If \(X\) and \(Y\) are independent, their covariance is zero. Therefore:

$$
\mathrm{Var}(X+Y)=
\mathrm{Var}(X)+\mathrm{Var}(Y)
$$

For independent random variables \(X_1,\ldots,X_n\):

$$
\operatorname{Var}(X_1 + X_2 + \cdots + X_n)
= \operatorname{Var}(X_1) + \operatorname{Var}(X_2) + \cdots + \operatorname{Var}(X_n)
$$

### 20.5 Python Example

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

NumPy's default `var()` uses population variance with `ddof=0`. The code demonstrates the transformation rules on the given data.

---

## 21. Law of Total Expectation

The **Law of Total Expectation** calculates an overall expected value by averaging conditional expected values across possible groups or conditions.

It is expressed as:

$$
E(X)=E[E(X\mid Y)]
$$

For a discrete variable \(Y\):

$$
E(X)=\sum_y E(X\mid Y=y)P(Y=y)
$$

This is useful when the expected value of a variable differs between groups.

### 21.1 Worked Example

Suppose customers belong to two groups:

| Group | Probability | Expected Purchase Amount |
|---|---:|---:|
| A | 0.6 | 100 |
| B | 0.4 | 200 |

The overall expected purchase amount is:

$$
E(X)=100(0.6)+200(0.4)
$$

$$
E(X)=60+80
$$

Therefore:

$$
E(X)=140
$$

The overall expected purchase amount is 140.

### 21.2 Python Implementation

```python
import numpy as np

conditional_means = np.array([100, 200])
group_probabilities = np.array([0.6, 0.4])

overall_mean = np.sum(
    conditional_means * group_probabilities
)

print("Overall expected value:", overall_mean)
```

### 21.3 Applications

This principle is useful for combining expected outcomes across customer segments, product categories, regions, or other groups in data analysis.

---

## 22. Central Limit Theorem

The **Central Limit Theorem (CLT)** explains why the sampling distribution of a sample mean becomes approximately Normal under suitable conditions as the sample size increases.

Suppose independent observations have mean \(\mu\) and finite variance \(\sigma^2\).

For a sample of size \(n\), the sample mean is:

$$
\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

Its expected value is:

$$
E(\bar{X})=\mu
$$

For independent observations with the same variance, the variance of the sample mean is:

$$
\mathrm{Var}(\bar{X})=\frac{\sigma^2}{n}
$$

Its standard error is:

$$
SE(\bar{X})=\frac{\sigma}{\sqrt{n}}
$$

Under suitable conditions, the distribution of the standardised sample mean approaches the Standard Normal distribution as the sample size increases.

**Important distinction:** The CLT concerns the sampling distribution of a statistic, such as the sample mean. It does not state that the original observations themselves become Normally distributed.

A larger sample often improves the Normal approximation, but the required sample size depends on the original distribution and the conditions of the problem.

### 22.1 Python Demonstration

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

sample_size = 50
number_of_samples = 5000

sample_means = np.array([
    rng.exponential(scale=1, size=sample_size).mean()
    for _ in range(number_of_samples)
])

plt.hist(sample_means, bins=40, density=True)
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.title("Sampling Distribution of the Sample Mean")
plt.show()

print("Mean of sample means:", sample_means.mean())
print("SD of sample means:", sample_means.std())
```

The original observations come from a right-skewed Exponential distribution. The distribution of the sample means tends to be more symmetric as the sample size increases.

A full treatment of sampling distributions, standard errors, confidence intervals, and statistical inference belongs in the Inferential Statistics chapter.

---

## 23. Choosing the Correct Probability Distribution

The appropriate distribution depends on the type of random variable, the data-generating process, and the assumptions that are reasonable for the problem.

| Situation | Possible Distribution |
|---|---|
| One binary trial | Bernoulli |
| Number of successes in a fixed number of independent trials | Binomial |
| Number of events in a fixed interval | Poisson |
| Number of trials until the first success | Geometric |
| Number of trials until a specified number of successes | Negative Binomial |
| Sampling without replacement from a finite population | Hypergeometric |
| Continuous variable with constant density over an interval | Uniform |
| Continuous variable modelled with a symmetric bell-shaped curve | Normal |
| Waiting time under a constant-rate process | Exponential |

These are modelling guidelines, not automatic rules. Real datasets may violate the assumptions of a theoretical distribution.

Before selecting a distribution, consider:

1. Is the variable discrete or continuous?
2. Does it represent a count, a binary outcome, or a measurement?
3. Are trials independent?
4. Is the probability of success constant?
5. Is sampling performed with or without replacement?
6. Does the assumed distribution reasonably describe the observed data?

---

## 24. Common Mistakes

### 24.1 Confusing PMF and PDF

A PMF gives probabilities for individual discrete values. A PDF describes density for a continuous variable.

### 24.2 Treating a PDF Value as a Probability

The PDF value at an exact point is not the probability of that point. Continuous probabilities are calculated using interval areas or CDF differences.

### 24.3 Ignoring Binomial Assumptions

The Binomial distribution requires a fixed number of independent trials and a constant probability of success.

### 24.4 Confusing the Poisson Parameter with a Probability

The parameter \(\lambda\) represents an expected event count for the specified interval, or a rate multiplied by the interval length. It is not restricted to values between zero and one.

### 24.5 Confusing Variance with Standard Deviation

Variance is expressed in squared units, whereas standard deviation is expressed in the original units.

### 24.6 Assuming Every Dataset Is Normally Distributed

A Normal distribution should not be assumed without considering the data and the purpose of the analysis.

### 24.7 Confusing Geometric and Exponential Distributions

The Geometric distribution is discrete and models the trial number until the first success. The Exponential distribution is continuous and models waiting time.

### 24.8 Ignoring Sampling Without Replacement

For finite-population sampling without replacement, a Hypergeometric model may be more appropriate than a Binomial model.

### 24.9 Misinterpreting the Central Limit Theorem

The CLT concerns the distribution of suitable sample statistics, not necessarily the distribution of the original observations.

### 24.10 Mixing Up Software Parameterisations

Statistical libraries may use different definitions for the same named distribution. In particular, check whether the Geometric or Negative Binomial implementation counts trials or failures.

### 24.11 Ignoring Units

Rates and intervals must use consistent units. A rate expressed per minute cannot be multiplied directly by an interval expressed in hours without conversion.

---

## 25. Applications in Data Science and Machine Learning

Probability distributions help describe uncertainty and model different types of data.

### 25.1 Customer Analytics

Bernoulli and Binomial models can represent binary purchase outcomes and counts of purchases among a fixed number of customers under suitable assumptions.

### 25.2 Website Traffic and Event Counts

Poisson models can represent requests, visits, or incoming support tickets over a fixed interval when the model assumptions are reasonable.

### 25.3 Waiting-Time Analysis

Exponential models can represent waiting times between events in a suitable constant-rate process.

### 25.4 Quality Control

Binomial and Hypergeometric distributions can help model defective items, depending on whether trials are independent or items are sampled without replacement.

### 25.5 Statistical Modelling

Expected values and variances describe central tendency and spread. Probability distributions also provide a foundation for estimation, statistical tests, uncertainty quantification, and related methods.

### 25.6 Machine Learning

Probability distributions appear in probabilistic classification, likelihood-based estimation, Bayesian methods, uncertainty modelling, and generative modelling.

The appropriate distribution depends on the target variable, model assumptions, and the problem being solved.

---

## 26. Points to Remember

1. A probability distribution describes how probabilities are assigned to a random variable.
2. Discrete random variables are described using PMFs.
3. Continuous random variables are described using PDFs.
4. A CDF gives the probability that a variable is less than or equal to a specified value.
5. The expected value represents a theoretical long-run average.
6. Variance measures spread, while standard deviation is the square root of variance.
7. The Bernoulli distribution models a single binary trial.
8. The Binomial distribution models successes in a fixed number of independent trials.
9. The Poisson distribution models event counts under suitable assumptions.
10. Geometric and Negative Binomial distributions model the number of trials or failures until a specified number of successes.
11. The Hypergeometric distribution models sampling without replacement from a finite population.
12. The continuous Uniform distribution has constant density over an interval.
13. The Normal distribution is symmetric and bell-shaped.
14. A z-score expresses an observation's distance from the mean in standard-deviation units.
15. The Exponential distribution models waiting times under a suitable constant-rate process.
16. Poisson and Exponential distributions are related through the Poisson process.
17. The Law of Total Expectation combines conditional expected values across groups.
18. The CLT concerns the sampling distribution of suitable statistics.
19. Distribution assumptions and parameter definitions must be checked before using a model.
20. NumPy and SciPy provide useful tools for probability calculations, simulations, and statistical analysis.

---

## 27. Important Formula Summary

### 27.1 Probability Functions

**Probability Mass Function**

$$
p_X(x)=P(X=x)
$$

**Cumulative Distribution Function**

$$
F_X(x)=P(X\leq x)
$$

**Continuous Interval Probability**

$$
P(a\leq X\leq b)=\int_a^b f_X(x)\,dx
$$

**CDF Difference**

$$
P(a<X\leq b)=F_X(b)-F_X(a)
$$

### 27.2 Expected Value and Variance

**Discrete Expected Value**

$$
E(X)=\sum_x xP(X=x)
$$

**Continuous Expected Value**

$$
E(X)=\int_{-\infty}^{\infty}xf_X(x)\,dx
$$

**Variance**

$$
\mathrm{Var}(X)=E[(X-E(X))^2]
$$

**Alternative Variance Formula**

$$
\mathrm{Var}(X)=E(X^2)-[E(X)]^2
$$

**Standard Deviation**

$$
\sigma=\sqrt{\mathrm{Var}(X)}
$$

### 27.3 Bernoulli Distribution

$$
P(X=x)=p^x(1-p)^{1-x}
$$

$$
E(X)=p
$$

$$
\mathrm{Var}(X)=p(1-p)
$$

### 27.4 Binomial Distribution

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

$$
E(X)=np
$$

$$
\mathrm{Var}(X)=np(1-p)
$$

### 27.5 Poisson Distribution

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
E(X)=\mathrm{Var}(X)=\lambda
$$

### 27.6 Geometric Distribution

For the trial-number convention:

$$
P(X=x)=(1-p)^{x-1}p
$$

$$
E(X)=\frac{1}{p}
$$

$$
\mathrm{Var}(X)=\frac{1-p}{p^2}
$$

### 27.7 Negative Binomial Distribution

For the number of trials required to obtain \(r\) successes:

$$
P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r}
$$

$$
E(X)=\frac{r}{p}
$$

$$
\mathrm{Var}(X)=\frac{r(1-p)}{p^2}
$$

### 27.8 Hypergeometric Distribution

$$
P(X=x)=
\frac{\binom{K}{x}\binom{N-K}{n-x}}
{\binom{N}{n}}
$$

### 27.9 Continuous Uniform Distribution

$$
f_X(x)=\frac{1}{b-a},\qquad a\leq x\leq b
$$

$$
E(X)=\frac{a+b}{2}
$$

$$
\mathrm{Var}(X)=\frac{(b-a)^2}{12}
$$

### 27.10 Normal Distribution and Z-Score

$$
f_X(x)=
\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

$$
Z=\frac{X-\mu}{\sigma}
$$

### 27.11 Exponential Distribution

$$
f_X(x)=\lambda e^{-\lambda x},\qquad x\geq0
$$

$$
F_X(x)=1-e^{-\lambda x},\qquad x\geq0
$$

$$
E(X)=\frac{1}{\lambda}
$$

$$
\mathrm{Var}(X)=\frac{1}{\lambda^2}
$$

### 27.12 Expected Value and Variance Rules

$$
E(aX+b)=aE(X)+b
$$

$$
\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)
$$

$$
E(X+Y)=E(X)+E(Y)
$$

$$
\mathrm{Var}(X+Y)=
\mathrm{Var}(X)+\mathrm{Var}(Y)
+2\mathrm{Cov}(X,Y)
$$

For independent random variables:

$$
\mathrm{Var}(X+Y)=
\mathrm{Var}(X)+\mathrm{Var}(Y)
$$

### 27.13 Central Limit Theorem

**Sample Mean**

$$
\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

**Expected Value of the Sample Mean**

$$
E(\bar{X})=\mu
$$

**Variance of the Sample Mean**

$$
\mathrm{Var}(\bar{X})=\frac{\sigma^2}{n}
$$

**Standard Error of the Sample Mean**

$$
SE(\bar{X})=\frac{\sigma}{\sqrt{n}}
$$

---

## 28. Practice Questions

1. Explain the difference between a PMF, PDF, and CDF.
2. A random variable takes values 0, 1, and 2 with probabilities 0.2, 0.5, and 0.3. Calculate its expected value and variance.
3. A customer has a 30% probability of purchasing a product. Which distribution could model the purchase outcome for one customer?
4. A fair coin is tossed five times. What is the probability of obtaining exactly three Heads?
5. A service receives an average of four requests per minute. Under a suitable Poisson model, calculate the probability of exactly two requests in one minute.
6. Explain when a Hypergeometric distribution is more suitable than a Binomial distribution.
7. A Normal distribution has mean 50 and standard deviation 10. Calculate the z-score for an observation of 70.
8. The average waiting time is four minutes under an Exponential model. Determine the rate parameter.
9. Explain the memoryless property of the Exponential distribution.
10. Explain the difference between the distribution of individual observations and the sampling distribution of a sample mean.

---

## 29. References

### GeeksforGeeks

- [Statistics](https://www.geeksforgeeks.org/maths/statistics/)
- [Probability](https://www.geeksforgeeks.org/maths/probability/)

### OpenStax

- [Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e)

### SciPy Documentation

- [Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Probability Distributions](https://docs.scipy.org/doc/scipy/tutorial/stats.html)

### NumPy Documentation

- [NumPy User Guide](https://numpy.org/doc/stable/)
- [Random Sampling](https://numpy.org/doc/stable/reference/random/index.html)
