
# Bias and Variance

Bias and variance are fundamental concepts in statistics and machine learning. They help explain how accurately an estimator measures an unknown quantity and how well a machine learning model performs on unseen data.

**Bias** measures systematic error, while **variance** measures how much estimates change across different samples.

A model with high bias may be too simple to capture important patterns. A model with high variance may fit its training data closely but fail to generalise to new observations.

The objective is to balance these sources of error and achieve good predictive performance.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Define bias and variance.
2. Distinguish parameters, estimators, and estimates.
3. Calculate bias, variance, standard error, and MSE.
4. Derive the bias–variance decomposition.
5. Understand consistency and efficiency.
6. Explain the bias–variance trade-off.
7. Identify underfitting and overfitting.
8. Understand irreducible prediction error.
9. Explain regularisation and cross-validation.
10. Implement bias and variance experiments using Python.

---

# 2. Parameters, Estimators, and Estimates

A **parameter** is a numerical characteristic of a population, such as the population mean $\mu$ or population variance $\sigma^2$.

An **estimator** is a rule used to estimate a parameter from sample data.

For example, the sample mean estimates the population mean:

$$
\bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_i
$$

Here, $n$ represents the sample size and $X_i$ represents an observation.

An **estimate** is the numerical value obtained after applying the estimator to a particular sample.

| Term | Meaning |
|---|---|
| Parameter | Population quantity |
| Estimator | Rule used to estimate the parameter |
| Estimate | Calculated value from a sample |

Different samples can produce different estimates. This variation is the foundation of bias and variance.

---

# 3. Bias

Bias measures the difference between the expected value of an estimator and the true parameter.

For an estimator $\hat{\theta}$ of a parameter $\theta$:

$$
\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta
$$

There are three possibilities.

**Zero bias**

$$
\text{Bias}(\hat{\theta}) = 0
$$

The estimator is unbiased.

**Positive bias**

$$
\text{Bias}(\hat{\theta}) > 0
$$

The estimator overestimates the parameter on average.

**Negative bias**

$$
\text{Bias}(\hat{\theta}) < 0
$$

The estimator underestimates the parameter on average.

## Worked Example

Suppose:

$$
E[\hat{\theta}] = 12.5,\qquad \theta = 10
$$

Using the bias formula:

$$
\begin{aligned}
\text{Bias}(\hat{\theta}) &= 12.5 - 10 \\
&= 2.5
\end{aligned}
$$

The estimator has positive bias of 2.5.

## Unbiased Estimator

An estimator is unbiased when its expected value equals the true parameter:

$$
E[\hat{\theta}] = \theta
$$

For the sample mean, under the usual random-sampling assumptions:

$$
E[\bar{X}] = \mu
$$

Therefore:

$$
\text{Bias}(\bar{X}) = 0
$$

Unbiasedness does not mean that every estimate is correct. It means the estimator is correct on average across repeated samples.

---

# 4. Variance of an Estimator

Variance measures the spread of an estimator across repeated samples.

The variance of an estimator is:

$$
\text{Var}(\hat{\theta})=
E\left[(\hat{\theta}-E[\hat{\theta}])^2\right]
$$

An equivalent formula is:

$$\text{Var}(\hat{\theta})=
E[\hat{\theta}^2]-(E[\hat{\theta}])^2
$$

A low-variance estimator produces estimates that tend to be close to one another.

A high-variance estimator produces estimates that may differ considerably across samples.

Variance is always non-negative:

$$
\text{Var}(\hat{\theta}) \geq 0
$$

## Variance of the Sample Mean

For independent observations with population variance $\sigma^2$, the variance of the sample mean is:

$$
\text{Var}(\bar{X}) = \frac{\sigma^2}{n}
$$

The standard error of the sample mean is:

$$
SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

### Worked Example

Suppose:

$$
\sigma = 12,\qquad n = 36
$$

Then:

$$
\begin{aligned}
SE(\bar{X}) &= \frac{12}{\sqrt{36}} \\
&= \frac{12}{6} \\
&= 2
\end{aligned}
$$

The standard error is 2 units.

**Important:** Under these assumptions, quadrupling the sample size halves the standard error. More data generally reduce sampling variability, but they do not automatically eliminate model bias.

---

# 5. Bias, Variance, and Standard Error

These quantities describe different properties of an estimator.

| Quantity | Meaning |
|---|---|
| Bias | Systematic difference from the true parameter |
| Variance | Spread across repeated estimates |
| Standard error | Square root of estimator variance |
| MSE | Expected squared estimation error |

The standard error is:

$$
SE(\hat{\theta}) = \sqrt{\text{Var}(\hat{\theta})}
$$

Variance is expressed in squared units, whereas standard error uses the same units as the estimator.

An estimator can have low bias but high variance, or high bias but low variance. Neither bias nor variance alone provides a complete measure of estimator quality.

---

# 6. Mean Squared Error (MSE)

Mean squared error measures the expected squared difference between an estimator and the true parameter.

$$\text{MSE}(\hat{\theta})=
E[(\hat{\theta}-\theta)^2]
$$

The bias–variance decomposition is:

$$\text{MSE}(\hat{\theta})=
\text{Bias}(\hat{\theta})^2
+
\text{Var}(\hat{\theta})
$$

This formula combines systematic error and sampling variability.

## Derivation of the MSE Formula

Start with:

$$\text{MSE}(\hat{\theta})=
E[(\hat{\theta}-\theta)^2]
$$

Add and subtract $E[\hat{\theta}]$:

$$\hat{\theta}-\theta=
(\hat{\theta}-E[\hat{\theta}])
+
(E[\hat{\theta}]-\theta)
$$

Expanding the square and taking expectations gives:

$$
\begin{aligned}
\text{MSE}(\hat{\theta})
&= \text{Var}(\hat{\theta}) \\
&\quad + 2(E[\hat{\theta}]-\theta)
E[\hat{\theta}-E[\hat{\theta}]] \\
&\quad + (E[\hat{\theta}]-\theta)^2
\end{aligned}
$$

The middle term is zero because:

$$
E[\hat{\theta}-E[\hat{\theta}]] = 0
$$

Therefore:

$$\boxed{\text{MSE}(\hat{\theta})=
\text{Var}(\hat{\theta})
+
\text{Bias}(\hat{\theta})^2
}
$$

This is the bias–variance decomposition for parameter estimation under squared-error loss.

## Worked Example

Suppose an estimator has bias 2 and variance 9.

$$
\begin{aligned}
\text{MSE} &= 2^2 + 9 \\
&= 4 + 9 \\
&= 13
\end{aligned}
$$

Therefore, the MSE is 13.

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE:

$$
\text{RMSE} = \sqrt{\text{MSE}}
$$

For the example above:

$$
\text{RMSE} = \sqrt{13} \approx 3.606
$$

RMSE uses the same units as the quantity being estimated.

For an unbiased estimator, MSE equals variance. For a biased estimator, MSE includes both variance and squared bias.

---

# 7. Consistency and Efficiency

## Consistency

An estimator is consistent if it converges in probability to the true parameter as the sample size increases.

$$
\hat{\theta}_n \xrightarrow{p} \theta
$$

Informally, larger samples increasingly concentrate the estimator around the true parameter.

Consistency is different from unbiasedness. An estimator can be biased for finite samples and still be consistent.

## Efficiency

When comparing unbiased estimators of the same parameter under the same assumptions, the estimator with lower variance is generally more precise.

If:

$$
\text{Var}(\hat{\theta}_1)
<
\text{Var}(\hat{\theta}_2)
$$

then estimator 1 has lower variance under this comparison.

When estimators are biased, MSE may be a more informative comparison than variance alone.

---

# 8. Bias–Variance Trade-Off

The bias–variance trade-off describes the tension between systematic error and estimation variability.

A simple model may be unable to capture complex relationships, resulting in higher bias.

A flexible model may capture more complex relationships but become more sensitive to changes in the training data, resulting in higher variance.

| Model behaviour | Bias | Variance |
|---|---|---|
| Simple model | Often higher | Often lower |
| Flexible model | Often lower | Often higher |

These are general tendencies, not universal rules.

The objective is to select a model that performs well on unseen data rather than automatically choosing the simplest or most complex model.

---

# 9. Prediction Error Decomposition

In machine learning, suppose the response variable is generated by:

$$
Y = f(X) + \varepsilon
$$

Here:

- $f(X)$ represents the systematic relationship.
- $\varepsilon$ represents random noise.
- $\hat{f}(x)$ represents the model's prediction at input $x$.

Assume the noise has conditional mean zero and conditional variance $\sigma_\varepsilon^2(x)$.

The expected squared prediction error at a fixed input $x$ can be decomposed as:

$$
\begin{aligned}
E[(Y-\hat{f}(x))^2\mid X=x]
&= \text{Bias}(\hat{f}(x))^2 \\
&\quad + \text{Var}(\hat{f}(x)) \\
&\quad + \sigma_\varepsilon^2(x)
\end{aligned}
$$

The three components are:

1. **Squared bias:** Systematic difference between the average prediction and the true relationship.
2. **Variance:** Variation in predictions across different training samples.
3. **Irreducible noise:** Random variation in the response that remains even when the systematic relationship is known.

This explains why prediction error cannot always be eliminated by increasing model complexity.

---

# 10. Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to capture important patterns in the data.

It is commonly associated with high bias.

Typical signs include:

- High training error.
- High validation error.
- Important patterns remaining unexplained.

For example, a straight-line model may underfit data generated by a strongly nonlinear relationship.

Possible solutions include choosing a more suitable model, adding meaningful features, or reducing excessive regularisation.

## Overfitting

Overfitting occurs when a model learns details specific to the training data, including random noise, that do not generalise.

It is commonly associated with high variance.

Typical signs include:

- Very low training error.
- Much higher validation or test error.
- Unstable predictions across different training samples.

Possible solutions include regularisation, cross-validation, reducing unnecessary complexity, or collecting more representative training data.

## Training Error vs Test Error

| Situation | Training Error | Test Error |
|---|---|---|
| Underfitting | High | High |
| Good generalisation | Low or moderate | Low |
| Overfitting | Very low | High |

These patterns are useful diagnostic clues, not absolute rules.

---

# 11. Regularisation and Cross-Validation

## Regularisation

Regularisation discourages overly complex solutions by adding a penalty to the model-fitting objective.

For example, ridge regression uses a squared-error objective with an L2 penalty:

$$
\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
+
\lambda\sum_{j=1}^{p}\beta_j^2
$$

Here, $\lambda$ controls the penalty strength.

Increasing regularisation often increases bias and reduces variance. The exact effect depends on the model and dataset.

## Cross-Validation

Cross-validation estimates how well a model may generalise.

In $k$-fold cross-validation:

1. Divide the data into $k$ folds.
2. Train the model using $k-1$ folds.
3. Evaluate it on the remaining fold.
4. Repeat until each fold has been used for validation.
5. Compare the average validation scores.

Cross-validation can help select model complexity and hyperparameters.

The final test set should be reserved for final evaluation rather than repeatedly used to choose models.

---

# 12. Bias and Variance in Machine Learning Models

| Model | Typical consideration |
|---|---|
| Linear regression | May have high bias for strongly nonlinear relationships |
| High-degree polynomial regression | Can fit complex patterns but may have high variance |
| Decision tree | Deep trees may overfit training data |
| Random forest | Averaging trees often reduces variance compared with a single tree |
| K-nearest neighbours | Small values of $k$ can be sensitive to individual observations |
| Neural networks | Behaviour depends on architecture, data, optimisation, and regularisation |

These are general tendencies. Actual performance depends on the data, features, model configuration, and evaluation method.

For a data scientist, the important task is to diagnose the source of poor generalisation before changing the model.

---

# 13. Python Implementation: Simulating Bias and Variance

## 13.1 Simulating Sample Means

Suppose a population has mean 50 and standard deviation 10.

We can repeatedly generate samples and calculate their means.

```python
import numpy as np

rng = np.random.default_rng(42)

mu = 50
sigma = 10
n = 30
repetitions = 5000

sample_means = np.array([
    rng.normal(mu, sigma, n).mean()
    for _ in range(repetitions)
])

print("Mean of sample means:", sample_means.mean())
print("Variance of sample means:", sample_means.var())
```

The simulated mean should be close to 50.

The theoretical variance of the sample mean is:

$$
\text{Var}(\bar{X}) = \frac{10^2}{30} \approx 3.333
$$

The empirical variance may differ slightly because the simulation uses a finite number of repetitions.

## 13.2 Comparing Theoretical and Empirical Variance

```python
theoretical_variance = sigma**2 / n
empirical_variance = sample_means.var()

print("Theoretical variance:", theoretical_variance)
print("Empirical variance:", empirical_variance)
```

The theoretical variance follows from the assumptions. The empirical variance is estimated from the simulated sample means.

## 13.3 Simulating a Biased Estimator

Define a new estimator by adding 2 to each sample mean:

$$
\hat{\mu}_{\text{biased}} = \bar{X} + 2
$$

```python
biased_estimates = sample_means + 2

print("Mean of biased estimates:", biased_estimates.mean())
print("Estimated bias:", biased_estimates.mean() - mu)

print("Original variance:", sample_means.var())
print("Biased estimator variance:", biased_estimates.var())
```

The estimated bias should be close to 2.

Adding a constant changes the mean but does not change the variance:

$$
\text{Var}(\bar{X}+2) = \text{Var}(\bar{X})
$$

## 13.4 Calculating MSE from Simulation

```python
theta = mu

estimated_bias = biased_estimates.mean() - theta
estimated_variance = biased_estimates.var()

estimated_mse = np.mean(
    (biased_estimates - theta)**2
)

print("Bias:", estimated_bias)
print("Variance:", estimated_variance)
print("MSE:", estimated_mse)

print(
    "Bias squared + Variance:",
    estimated_bias**2 + estimated_variance
)
```

The two MSE values should be close, subject to simulation variability and the variance convention used.

---

# 14. Python Experiment: Model Complexity

We can compare polynomial models of different degrees using training and test error.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)

X = np.linspace(-3, 3, 200).reshape(-1, 1)
y = X[:, 0]**2 + rng.normal(0, 2, size=200)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

degrees = range(1, 16)
train_errors = []
test_errors = []

for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree=degree),
        LinearRegression()
    )

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_errors.append(
        mean_squared_error(y_train, train_predictions)
    )

    test_errors.append(
        mean_squared_error(y_test, test_predictions)
    )

plt.plot(degrees, train_errors, marker="o", label="Training MSE")
plt.plot(degrees, test_errors, marker="o", label="Test MSE")

plt.xlabel("Polynomial Degree")
plt.ylabel("Mean Squared Error")
plt.title("Model Complexity and Prediction Error")
plt.legend()
plt.show()
```

Training error often decreases as model complexity increases. Test error may decrease initially and then increase if the model starts fitting noise.

The exact result depends on the dataset and random noise.

This experiment demonstrates why model selection should consider generalisation performance rather than training error alone.

For rigorous model selection, use cross-validation and reserve the final test set for final evaluation.

---

# 15. Common Mistakes

1. **Confusing bias with variance:** Bias measures systematic error; variance measures variability.
2. **Forgetting to square bias:** The MSE formula uses squared bias.
3. **Assuming unbiased means exact:** An unbiased estimator can produce inaccurate individual estimates.
4. **Assuming more data eliminates all bias:** Structural model bias may remain.
5. **Equating training error with bias:** Training error is an observed performance measure, not the theoretical definition of bias.
6. **Assuming the most complex model is best:** Greater flexibility can increase overfitting.
7. **Ignoring the loss function:** The classical decomposition in this chapter applies to squared-error loss.

---

# 16. Formula Summary

**Bias**

$$
\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta
$$

**Variance**

$$
\text{Var}(\hat{\theta})=
E[(\hat{\theta}-E[\hat{\theta}])^2]
$$

**Standard error**

$$
SE(\hat{\theta}) = \sqrt{\text{Var}(\hat{\theta})}
$$

**Variance of the sample mean**

$$
\text{Var}(\bar{X}) = \frac{\sigma^2}{n}
$$

**Standard error of the sample mean**

$$
SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

**Mean squared error**

$$
\text{MSE}(\hat{\theta})=
\text{Bias}(\hat{\theta})^2
+
\text{Var}(\hat{\theta})
$$

**Root mean squared error**

$$
\text{RMSE} = \sqrt{\text{MSE}}
$$

**Prediction error decomposition**

$$
\begin{aligned}
\text{Expected prediction error}
&= \text{Bias}^2 \\
&\quad + \text{Variance} \\
&\quad + \text{Irreducible noise}
\end{aligned}
$$

---

# 17. Points to Remember

- Bias measures systematic error.
- Variance measures variability across repeated estimates.
- Standard error is the square root of estimator variance.
- MSE combines squared bias and variance.
- More data often reduce variance but may not eliminate model bias.
- Underfitting is commonly associated with high bias.
- Overfitting is commonly associated with poor generalisation and may be associated with high variance.
- Cross-validation helps compare modelling choices.
- Regularisation can control model complexity.
- The best model is the one that performs well on the relevant generalisation objective.

---

# 18. References

1. James, G., Witten, D., Hastie, T., Tibshirani, R., and Taylor, J. *An Introduction to Statistical Learning*. [Official book website](https://www.statlearning.com/)

2. Hastie, T., Tibshirani, R., and Friedman, J. *The Elements of Statistical Learning*. [Official book website](https://hastie.su.domains/ElemStatLearn/)

3. scikit-learn documentation. [Model selection and evaluation](https://scikit-learn.org/stable/model_selection.html)

4. scikit-learn documentation. [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

---

**Next topic:** Statistics for Machine Learning — Folder 15.
