
# Statistics for Machine Learning

Statistics provides the foundation for understanding data, uncertainty, relationships between variables, and machine learning model performance.

In Data Science, statistics is used to explore datasets, prepare features, select models, evaluate predictions, interpret results, and determine whether observed patterns are reliable.

This chapter connects the most important statistical concepts to practical machine learning workflows without repeating the full explanations already covered in the earlier chapters of this repository.

The overall workflow is:

$$
\text{Data}
\rightarrow
\text{Explore}
\rightarrow
\text{Prepare}
\rightarrow
\text{Model}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Interpret}
$$

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain the importance of statistics in machine learning.
2. Distinguish descriptive statistics, inferential statistics, and predictive modelling.
3. Understand populations, samples, features, and targets.
4. Identify sampling bias and data quality problems.
5. Use descriptive statistics to understand a dataset.
6. Apply standardisation and min-max scaling.
7. Understand skewness, outliers, and missing data.
8. Explain data leakage and correct data splitting.
9. Interpret covariance, correlation, and multicollinearity.
10. Understand regression coefficients and the difference between association and causation.
11. Interpret confidence intervals, p-values, and effect sizes.
12. Understand class imbalance and classification probabilities.
13. Select appropriate model evaluation metrics.
14. Understand cross-validation and bootstrap resampling.
15. Interpret residuals and prediction uncertainty.
16. Recognise distribution shift and its effect on model performance.
17. Apply statistical reasoning using Python.

---

# 2. Why Statistics Matters in Machine Learning

Machine learning models learn patterns from historical observations. Statistics helps us determine whether those patterns are meaningful and whether they are likely to remain useful for new observations.

Statistics helps answer questions such as:

- What does the dataset look like?
- How variable are the observations?
- Is the sample representative of the target population?
- Are two variables associated?
- Are there missing values or unusual observations?
- How should numerical features be scaled?
- How reliable is a model's performance estimate?
- Could data leakage make the results misleading?
- Does a model generalise to unseen data?
- Is a difference statistically and practically meaningful?

Three broad uses of statistics are particularly important.

| Purpose | Main objective | Examples |
|---|---|---|
| Descriptive statistics | Summarise observed data | Mean, median, standard deviation |
| Inferential statistics | Learn about a population from a sample | Confidence intervals, hypothesis tests |
| Predictive modelling | Predict outcomes for new observations | Regression, classification |

These purposes are related, but they answer different questions.

---

# 3. Population, Sample, Features, and Target

A **population** is the complete group relevant to a study or modelling problem.

A **sample** is the subset of observations available for analysis.

For example, if a model predicts customer churn:

- Population: customers to whom the model will be applied.
- Sample: customers represented in the available historical dataset.
- Features: tenure, monthly charges, contract type, and support calls.
- Target: whether a customer churns.

A dataset can be represented as:

$$
D = \{(x_i,y_i)\}_{i=1}^{n}
$$

where:

- \(n\) is the number of observations.
- \(x_i\) is the feature vector for observation \(i\).
- \(y_i\) is the corresponding target value.

A model learns a relationship between features and the target:

$$
\hat{Y} = f(X)
$$

The objective is not merely to fit the available sample. The model should perform well on relevant future observations.

---

# 4. Sampling Bias and Data Quality

## 4.1 Representative Sampling

A sample should represent the population in which the model will be used.

Suppose a customer-prediction model is intended for an entire country, but its training data comes almost entirely from one city.

The model may learn patterns that do not represent customers elsewhere.

**Sampling bias** occurs when the sampling process systematically favours some observations over others.

**Selection bias** occurs when inclusion in the dataset depends on characteristics related to the outcome or variables being studied.

Collecting more data from the same biased process does not necessarily remove these problems.

## 4.2 Data Quality

Before modelling, inspect:

- Missing values.
- Duplicate records.
- Incorrect labels.
- Impossible values.
- Inconsistent measurement units.
- Unusual categories.
- Outliers.
- Measurement errors.

A statistical calculation can be mathematically correct while still producing misleading conclusions if the underlying data is incorrect.

**Practical principle:** Good modelling begins with trustworthy data and a clear understanding of the target population.

---

# 5. Descriptive Statistics for Data Exploration

Descriptive statistics help us understand the centre, spread, and distribution of numerical features.

## 5.1 Mean

The sample mean is:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

The mean uses every observation, so extreme values can affect it substantially.

## 5.2 Median

The median is the middle value after observations are arranged in order.

It is generally more resistant to extreme observations than the mean.

## 5.3 Variance and Standard Deviation

The sample variance is:

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

The sample standard deviation is:

$$
s = \sqrt{s^2}
$$

These quantities describe the spread of observations around their mean.

## 5.4 Choosing a Summary

Suppose income data contains a small number of extremely high values. The mean may be much larger than the median.

Comparing mean and median can help identify skewness or unusual observations.

The appropriate summary depends on the distribution and measurement scale.

---

# 6. Standardisation and Min-Max Scaling

Numerical features may use very different measurement scales. For example, income may be measured in thousands of rupees, while age is measured in years.

Scaling can be useful for models that depend on distances, gradient-based optimisation, or coefficient magnitudes.

## 6.1 Standardisation

Standardisation transforms a value using the mean and standard deviation.

When population quantities are known:

$$
z = \frac{x-\mu}{\sigma}
$$

When sample statistics are used:

$$
z = \frac{x-\bar{x}}{s}
$$

The transformed values are centred around zero and expressed in standard-deviation units.

### Worked Example

Suppose:

$$
x=80,\qquad \mu=70,\qquad \sigma=5
$$

Then:

$$
\begin{aligned}
z &= \frac{80-70}{5} \\
&= \frac{10}{5} \\
&= 2
\end{aligned}
$$

The observation is two standard deviations above the mean.

Standardisation does not automatically make a feature normally distributed.

## 6.2 Min-Max Scaling

A common min-max transformation is:

$$
x' = \frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

When the minimum and maximum are valid and distinct, this transformation maps the observed range to the interval from 0 to 1.

| Method | Main transformation | Typical result |
|---|---|---|
| Standardisation | Subtract mean and divide by standard deviation | Mean near 0, standard deviation near 1 |
| Min-max scaling | Subtract minimum and divide by range | Values scaled to 0–1 |

These transformations are not interchangeable, and neither should be applied automatically to every feature.

---

# 7. Skewness, Outliers, and Missing Data

## 7.1 Skewness

A distribution is right-skewed when it has a longer tail toward larger values.

Income, transaction amounts, and counts can exhibit right-skewed distributions.

For positive values, a logarithmic transformation may help:

$$
x' = \log(x)
$$

For non-negative values, another option is:

$$
x' = \log(1+x)
$$

Transformations should be selected based on the data and modelling objective.

## 7.2 Outliers

An outlier is an observation that differs substantially from the general pattern of the data.

Outliers may result from:

- Measurement errors.
- Data-entry mistakes.
- Rare but genuine events.
- Unusual operating conditions.

Do not automatically remove every outlier. First determine whether it is incorrect, irrelevant, or a valid observation from the target population.

## 7.3 Missing Data

Missing values can arise because information was not recorded, a sensor failed, or a participant did not provide an answer.

Common imputation approaches include:

- Mean imputation.
- Median imputation.
- Mode imputation.
- Constant-value imputation.
- Model-based imputation.

The reason for missingness matters. In particular, missingness may depend on observed or unobserved characteristics.

**Important:** Learn imputation values from the training data only. Apply the learned transformation to validation and test data.

---

# 8. Data Leakage and Data Splitting

Data leakage occurs when information that should not be available during model training influences the model or its evaluation.

For example, calculating the mean and standard deviation from the entire dataset before splitting it into training and test sets allows test-set information to influence preprocessing.

The correct procedure is:

$$
\text{Split}
\rightarrow
\text{Fit preprocessing on training data}
\rightarrow
\text{Transform other sets}
$$

## 8.1 Training, Validation, and Test Sets

| Dataset | Purpose |
|---|---|
| Training set | Fit model parameters |
| Validation set | Select models and tune hyperparameters |
| Test set | Evaluate the final selected model |

The test set should remain isolated from decisions that influence the final model.

Repeatedly selecting models using test-set results makes the final performance estimate less reliable.

## 8.2 Cross-Validation

In \(k\)-fold cross-validation, the available training data is divided into \(k\) folds.

For each round:

1. Use \(k-1\) folds to train the model.
2. Use the remaining fold for validation.
3. Repeat until each fold has been used for validation.
4. Calculate the average validation error.

If the fold errors are \(E_1,E_2,\ldots,E_k\), the mean cross-validation error is:

$$
CV_{\text{error}} = \frac{1}{k}\sum_{j=1}^{k}E_j
$$

Cross-validation provides an estimate of generalisation performance, not a guarantee of future performance.

For classification with imbalanced classes, stratified splitting can help preserve class proportions across folds.

---

# 9. Covariance and Correlation

Covariance and correlation help describe relationships between numerical variables.

## 9.1 Sample Covariance

For two variables \(X\) and \(Y\), sample covariance is:

$$
s_{XY} =
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
$$

Positive covariance indicates that larger values of one variable tend to occur with larger values of the other.

Negative covariance indicates an opposite tendency.

Covariance depends on the measurement scales of the variables.

## 9.2 Pearson Correlation

Pearson correlation standardises covariance:

$$
r = \frac{s_{XY}}{s_Xs_Y}
$$

Its values satisfy:

$$
-1 \leq r \leq 1
$$

Interpretation:

- \(r\) near 1 indicates strong positive linear association.
- \(r\) near -1 indicates strong negative linear association.
- \(r\) near 0 indicates weak linear association.

A correlation near zero does not prove that the variables are independent. They may still have a nonlinear relationship.

## 9.3 Correlation Does Not Imply Causation

An association between two variables does not automatically establish that one causes the other.

Possible explanations include:

- Confounding variables.
- Reverse causation.
- Selection effects.
- Common external causes.
- Coincidence.

Correlation is useful for exploration, but causal conclusions require appropriate assumptions and study designs.

---

# 10. Multicollinearity

Multicollinearity occurs when predictors contain substantial overlapping information.

For example, house area, built-up area, and the number of rooms may be strongly related.

In linear regression, multicollinearity can make coefficient estimates unstable and difficult to interpret.

A common diagnostic is the Variance Inflation Factor (VIF):

$$
VIF_j = \frac{1}{1-R_j^2}
$$

Here, \(R_j^2\) is obtained by regressing predictor \(X_j\) on the other predictors.

A larger VIF indicates that the predictor is more strongly explained by the remaining predictors.

There is no single universal VIF cutoff that applies to every problem. Interpret it in context.

Multicollinearity can affect coefficient interpretation even when a model's predictive performance remains acceptable.

---

# 11. Regression Coefficients and Conditional Relationships

A linear regression model can be written as:

$$
Y = \beta_0+\beta_1X_1+\cdots+\beta_pX_p+\varepsilon
$$

The coefficients describe the model's relationship between the predictors and the expected response under the model assumptions.

For a single-predictor model:

$$
Y = \beta_0+\beta_1X+\varepsilon
$$

The coefficient \(\beta_1\) represents the expected change in the conditional mean of \(Y\) associated with a one-unit increase in \(X\), under the model.

This is not automatically a causal effect.

Relationships may also change after accounting for other variables. A simple pairwise relationship can differ from the relationship observed after conditioning on relevant predictors.

This is one reason why multivariable analysis can provide information that simple correlation analysis cannot.

---

# 12. Confidence Intervals and Prediction Intervals

## 12.1 Confidence Intervals

A confidence interval quantifies uncertainty about an estimated parameter using an inferential procedure.

A general large-sample form is:

$$
\text{Estimate}
\pm
\text{Critical value}\times SE
$$

For a regression coefficient:

$$
\hat{\beta}
\pm
\text{Critical value}\times SE(\hat{\beta})
$$

The exact method depends on the model and its assumptions.

A 95% frequentist confidence interval does not mean that there is a 95% probability that the fixed parameter lies inside the particular interval. Rather, the procedure is designed to cover the true parameter in approximately 95% of repeated samples when its assumptions hold.

## 12.2 Prediction Intervals

A confidence interval for a mean response and a prediction interval for a new observation are different.

A prediction interval accounts for uncertainty in the estimated mean as well as random variation in a new observation.

Consequently, prediction intervals are generally wider than confidence intervals for the mean response at the same input.

---

# 13. Hypothesis Testing, P-Values, and Effect Size

Hypothesis testing helps evaluate whether observed data are compatible with a specified null hypothesis.

A typical test compares:

- \(H_0\): the null hypothesis.
- \(H_1\): the alternative hypothesis.

The result may include a test statistic and a p-value.

## 13.1 P-Value

A p-value measures how unusual the observed test statistic, or a more extreme result, would be under the null model according to the chosen test.

It is not the probability that the null hypothesis is true.

A small p-value does not automatically imply that an effect is large or practically important.

## 13.2 Statistical and Practical Significance

With a very large sample, a small difference may be statistically significant even if its practical importance is limited.

An effect size describes the magnitude of a difference or relationship.

For example, a standardised mean difference may be expressed as:

$$
d = \frac{\bar{x}_1-\bar{x}_2}{s_p}
$$

where \(s_p\) is the appropriate pooled standard deviation under the chosen definition.

When interpreting results, consider the effect size, uncertainty, sample size, and practical consequences together.

## 13.3 Multiple Comparisons

Performing many hypothesis tests increases the chance of observing at least one false positive.

For \(m\) independent tests conducted at significance level \(\alpha\), the probability of at least one false positive when all null hypotheses are true is:

$$
P(\text{at least one false positive})=
1-(1-\alpha)^m
$$

For example, with 20 independent tests at a significance level of 0.05:

$$
1-(1-0.05)^{20}\approx0.642
$$

The probability is approximately 64.2%.

Multiple-testing procedures may be necessary when many hypotheses are examined.

---

# 14. Class Imbalance and Classification Metrics

Class imbalance occurs when some classes appear much more frequently than others.

Suppose only 1% of observations belong to the positive class.

A model that always predicts the negative class can achieve 99% accuracy while completely failing to identify positive cases.

Therefore, accuracy alone can be misleading for imbalanced classification.

## 14.1 Confusion Matrix

For binary classification, the confusion matrix contains:

- True Positive (TP).
- False Positive (FP).
- True Negative (TN).
- False Negative (FN).

These values form the basis of several classification metrics.

## 14.2 Accuracy

$$
\text{Accuracy}=
\frac{TP+TN}{TP+TN+FP+FN}
$$

Accuracy measures the proportion of correct predictions.

## 14.3 Precision

$$
\text{Precision} = \frac{TP}{TP+FP}
$$

Precision measures the proportion of predicted positives that are actually positive.

## 14.4 Recall

$$
\text{Recall} = \frac{TP}{TP+FN}
$$

Recall measures the proportion of actual positives that are correctly identified.

## 14.5 F1 Score

$$
F_1 =
2\frac{\text{Precision}\times\text{Recall}}
{\text{Precision}+\text{Recall}}
$$

F1 combines precision and recall through their harmonic mean.

## 14.6 Choosing a Metric

| Situation | Potentially useful metric |
|---|---|
| Classes are balanced and error costs are similar | Accuracy |
| False positives are costly | Precision |
| False negatives are costly | Recall |
| Precision and recall both matter | F1 |
| Ranking across thresholds matters | ROC-AUC |
| Minority-class retrieval is important | PR-AUC |
| Probability quality matters | Log loss and calibration measures |

The appropriate metric depends on the actual decision problem.

---

# 15. Predicted Probabilities and Calibration

A probabilistic classifier may estimate:

$$
P(Y=1\mid X=x)
$$

For binary classification, the two class probabilities satisfy:

$$
P(Y=1\mid X=x)+P(Y=0\mid X=x)=1
$$

A common classification rule predicts the positive class when the estimated probability reaches a chosen threshold.

$$
\hat{Y} = 1 \quad \text{if } \hat{p} \geq t
$$

$$
\hat{Y} = 0 \quad \text{if } \hat{p} < t
$$

Here, \(t\) is the decision threshold.

A threshold of 0.5 is common, but it is not universally optimal. Threshold selection depends on class prevalence, error costs, and operational requirements.

A model is well calibrated when its predicted probabilities correspond reasonably well to observed frequencies.

For example, among observations assigned probabilities near 0.8, approximately 80% should be positive if the model is well calibrated in that region.

Calibration and discrimination are different properties: a model can rank observations well while producing poorly calibrated probabilities.

---

# 16. Residual Analysis and Regression Metrics

A residual is the difference between an observed response and the model's prediction.

$$
e_i = y_i-\hat{y}_i
$$

Residual analysis can help identify:

- Nonlinear relationships not captured by the model.
- Unequal error variance.
- Unusual observations.
- Systematic prediction errors.

In ordinary least squares regression with an intercept, the training residuals sum to zero under the standard fitting procedure. This does not guarantee that future prediction errors will have mean zero.

## 16.1 Mean Absolute Error

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

MAE measures average absolute prediction error in the target's units.

## 16.2 Mean Squared Error

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

MSE penalises larger errors more heavily because the errors are squared.

## 16.3 Root Mean Squared Error

$$
RMSE =
\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

RMSE is expressed in the same units as the target.

MAE is useful when average absolute error is the main concern. RMSE is useful when larger errors should receive stronger penalties. Neither metric is universally superior.

---

# 17. Bootstrap and Resampling

Resampling methods help estimate variability or evaluate models when a single sample or split may provide an incomplete picture.

Common methods include:

- Bootstrap.
- Cross-validation.
- Permutation testing.

## 17.1 Bootstrap

The bootstrap repeatedly samples observations from the observed dataset with replacement.

Each bootstrap sample is used to calculate the statistic of interest.

The resulting distribution can help estimate sampling variability and construct uncertainty intervals under appropriate assumptions.

Suppose the bootstrap estimates are:

$$
\hat{\theta}^{(1)},\hat{\theta}^{(2)},\ldots,\hat{\theta}^{(B)}
$$

Their mean is:

$$
\bar{\theta}_{boot}=
\frac{1}{B}\sum_{b=1}^{B}\hat{\theta}^{(b)}
$$

The bootstrap standard error is the sample standard deviation of these estimates:

$$
SE_{boot}=
\sqrt{
\frac{1}{B-1}
\sum_{b=1}^{B}
(\hat{\theta}^{(b)}-\bar{\theta}_{boot})^2
}
$$

Bootstrap results depend on the sampling design and assumptions. Resampling does not automatically correct biased data or an unsuitable model.

---

# 18. Distribution Shift

A model is usually trained on one data distribution and later applied to new observations.

Let:

$$
P_{train}(X,Y)
$$

represent the training distribution and:

$$
P_{deploy}(X,Y)
$$

represent the deployment distribution.

If these distributions differ, model performance can change after deployment.

Important types include:

**Covariate shift:** The distribution of features changes, while the conditional relationship between target and features may remain approximately stable.

$$
P_{train}(X)\neq P_{deploy}(X)
$$

**Prior probability shift:** Class proportions change between training and deployment.

$$
P_{train}(Y)\neq P_{deploy}(Y)
$$

**Concept drift:** The conditional relationship between features and target changes.

$$
P_{train}(Y\mid X)\neq P_{deploy}(Y\mid X)
$$

Examples include changes in customer behaviour, market conditions, fraud patterns, or operating policies.

Monitoring data distributions and model performance is therefore important after deployment.

---

# 19. Practical Python: Statistical Summary

Pandas provides descriptive statistics for numerical columns.

```python
import pandas as pd

df = pd.DataFrame({
    "age": [21, 25, 29, 31, 45],
    "income": [25000, 32000, 41000, 45000, 90000]
})

print(df.describe())
```

The summary includes count, mean, standard deviation, minimum, quartiles, and maximum.

Use these values to identify differences in scale, potential outliers, and unusual distributions.

---

# 20. Practical Python: Standardisation Without Leakage

The following example separates the data before fitting the scaler.

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "age": [21, 25, 29, 31, 45, 35, 27, 42],
    "income": [25000, 32000, 41000, 45000,
               90000, 52000, 37000, 78000],
    "target": [0, 0, 1, 1, 1, 0, 0, 1]
})

X = df[["age", "income"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Training data:")
print(X_train_scaled)

print("Test data:")
print(X_test_scaled)
```

The scaler learns its mean and standard deviation from the training set only.

The same transformation is then applied to the test set. Do not fit a separate scaler on the test set when evaluating this model.

For larger projects, a scikit-learn pipeline can help keep preprocessing and modelling steps together.

---

# 21. Practical Python: Correlation Matrix

```python
import pandas as pd

df = pd.DataFrame({
    "age": [21, 25, 29, 31, 45, 35],
    "income": [25000, 32000, 41000, 45000, 90000, 52000],
    "experience": [0, 2, 4, 6, 20, 10]
})

correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)
```

A correlation matrix summarises pairwise linear associations between numerical variables.

It can help identify potentially related predictors, but it does not establish causation or fully describe nonlinear relationships.

---

# 22. Practical Python: Cross-Validation

The following example evaluates a regression model using cross-validation.

```python
import numpy as np

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

X, y = make_regression(
    n_samples=200,
    n_features=5,
    noise=15,
    random_state=42
)

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="neg_mean_squared_error"
)

mse_scores = -scores

print("Fold MSE:", mse_scores)
print("Mean CV MSE:", mse_scores.mean())
print("Standard deviation:", mse_scores.std(ddof=1))
```

Scikit-learn returns negative values for this loss because its scoring convention treats higher scores as better. Negating the values converts them to ordinary positive MSE values.

The average summarises performance across the folds. Variation across folds provides additional information about how performance changes with the validation split.

---

# 23. Practical Python: Bootstrap Standard Error

```python
import numpy as np

rng = np.random.default_rng(42)

data = np.array([12, 15, 14, 18, 21, 16, 17, 13])

bootstrap_means = []

for _ in range(5000):
    sample = rng.choice(
        data,
        size=len(data),
        replace=True
    )

    bootstrap_means.append(sample.mean())

bootstrap_means = np.array(bootstrap_means)

print("Original sample mean:", data.mean())
print("Bootstrap mean:", bootstrap_means.mean())
print(
    "Bootstrap standard error:",
    bootstrap_means.std(ddof=1)
)
```

The bootstrap distribution provides an empirical view of the uncertainty associated with the sample mean under the resampling procedure.

---

# 24. Practical Python: Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

y_true = [0, 0, 1, 1, 1, 0, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0, 1, 0]

print("Confusion matrix:")
print(confusion_matrix(y_true, y_pred))

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))
```

These metrics should be interpreted in the context of class prevalence and the cost of false positives and false negatives.

---

# 25. Complete Machine Learning Workflow

A statistically informed workflow can be organised into the following steps.

1. **Define the task.** Identify the target population and the outcome to predict.
2. **Inspect the data.** Check missing values, duplicates, measurement errors, and feature distributions.
3. **Explore relationships.** Use descriptive statistics, visualisations, and correlation where appropriate.
4. **Split the data.** Separate training and evaluation information before fitting preprocessing transformations.
5. **Prepare features.** Handle missing values, encode categories, and scale features when appropriate.
6. **Train candidate models.** Choose model families suitable for the task.
7. **Validate.** Use a validation set or cross-validation for model selection.
8. **Evaluate.** Select metrics based on the actual decision problem.
9. **Quantify uncertainty.** Consider confidence intervals, bootstrap methods, or variation across evaluation splits.
10. **Monitor deployment.** Check for distribution shift, calibration changes, and performance deterioration.

This workflow helps ensure that model performance reflects a meaningful evaluation rather than data leakage or an unsuitable sampling process.

---

# 26. Common Mistakes

1. **Treating correlation as causation.** Association alone does not establish a causal relationship.
2. **Scaling before splitting the data.** This can leak evaluation information into preprocessing.
3. **Using accuracy for every classification problem.** Class imbalance can make accuracy misleading.
4. **Repeatedly tuning against the test set.** This makes the final evaluation less reliable.
5. **Removing every outlier.** Some unusual observations are genuine and important.
6. **Assuming a small p-value means a large effect.** Statistical significance and practical importance are different.
7. **Assuming more data fixes every problem.** More data cannot automatically remove biased sampling or structural model limitations.
8. **Interpreting regression coefficients causally.** A fitted coefficient is not automatically a causal effect.
9. **Ignoring uncertainty in model metrics.** Evaluation metrics are estimates calculated from finite samples.
10. **Treating one validation split as absolute truth.** Validation performance is an estimate, not a guarantee.
11. **Ignoring deployment changes.** A model can deteriorate when the data distribution changes.
12. **Using predicted probabilities without checking calibration.** Reliable ranking does not necessarily imply reliable probabilities.

---

# 27. Important Formula Summary

### Sample mean

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

### Sample variance

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

### Z-score

$$
z = \frac{x-\mu}{\sigma}
$$

### Min-max scaling

$$
x' = \frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

### Sample covariance

$$
s_{XY} =
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
$$

### Pearson correlation

$$
r = \frac{s_{XY}}{s_Xs_Y}
$$

### Variance Inflation Factor

$$
VIF_j = \frac{1}{1-R_j^2}
$$

### Cross-validation mean error

$$
CV_{\text{error}} = \frac{1}{k}\sum_{j=1}^{k}E_j
$$

### Accuracy

$$
\text{Accuracy}=
\frac{TP+TN}{TP+TN+FP+FN}
$$

### Precision

$$
\text{Precision} = \frac{TP}{TP+FP}
$$

### Recall

$$
\text{Recall} = \frac{TP}{TP+FN}
$$

### F1 score

$$
F_1 =
2\frac{\text{Precision}\times\text{Recall}}
{\text{Precision}+\text{Recall}}
$$

### Mean Absolute Error

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

### Mean Squared Error

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Root Mean Squared Error

$$
RMSE =
\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

### Multiple-comparison probability

For \(m\) independent tests at significance level \(\alpha\):

$$
P(\text{at least one false positive})=
1-(1-\alpha)^m
$$

---

# 28. Points to Remember

1. Statistics helps machine learning understand data, uncertainty, relationships, and generalisation.
2. A dataset is usually a sample from a broader population.
3. Sampling bias can cause a model to learn unrepresentative patterns.
4. More observations from a biased process do not automatically remove sampling bias.
5. Descriptive statistics should be selected according to the variable and its distribution.
6. Standardisation and min-max scaling are different transformations.
7. Preprocessing parameters should be learned from training data only.
8. Correlation measures association, not causation.
9. Multicollinearity can make regression coefficients unstable.
10. Training, validation, and test sets have different roles.
11. Cross-validation estimates generalisation performance but does not guarantee future results.
12. Class imbalance can make accuracy misleading.
13. Precision and recall measure different aspects of classification performance.
14. Predicted probabilities should be checked for calibration when probability quality matters.
15. A p-value is not the probability that the null hypothesis is true.
16. Statistical significance does not automatically imply practical significance.
17. Bootstrap methods can help estimate sampling variability.
18. Residual analysis can reveal problems with regression models.
19. Data leakage can produce misleadingly strong evaluation results.
20. Distribution shift can reduce performance after deployment.
21. Evaluation metrics are themselves estimates based on finite data.
22. Statistical reasoning should be connected to the actual modelling and decision problem.

---

# 29. Chapter Summary

Statistics for machine learning is the application of statistical reasoning throughout the modelling process.

First, we examine the data and determine whether it represents the population relevant to the task. We then explore distributions, prepare features, and investigate relationships between variables.

During model development, correct data splitting, cross-validation, and appropriate evaluation metrics help reduce misleading conclusions. Confidence intervals, bootstrap methods, and careful interpretation of statistical tests provide additional insight into uncertainty.

Finally, deployment monitoring helps identify distribution changes that may affect model performance.

The central principle is:

$$
\boxed{
\text{Reliable Results}=
\text{Trustworthy Data}
+
\text{Sound Assumptions}
+
\text{Valid Evaluation}
}
$$

This chapter connects the statistical foundations developed throughout the Mathematics & Statistics section to the practical work of building, evaluating, and maintaining machine learning models.

---

# 30. References

1. James, G., Witten, D., Hastie, T., Tibshirani, R., and Taylor, J. *An Introduction to Statistical Learning*. [Official book website](https://www.statlearning.com/)

2. Hastie, T., Tibshirani, R., and Friedman, J. *The Elements of Statistical Learning*. [Official book website](https://hastie.su.domains/ElemStatLearn/)

3. Wasserman, L. *All of Statistics: A Concise Course in Statistical Inference*.

4. Scikit-learn documentation. [Model selection and evaluation](https://scikit-learn.org/stable/model_selection.html)

5. Scikit-learn documentation. [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)

6. NumPy documentation. [NumPy User Guide](https://numpy.org/doc/stable/user/)

7. Pandas documentation. [Getting started](https://pandas.pydata.org/docs/getting_started/index.html)

---


**Next step:** Apply these statistical concepts in the Machine Learning section of the repository.
