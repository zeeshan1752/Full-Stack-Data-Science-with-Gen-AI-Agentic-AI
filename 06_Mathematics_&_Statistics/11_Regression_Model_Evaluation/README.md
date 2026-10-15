# Regression Model Evaluation

A regression model generates predictions, but fitting a model is only the beginning of the analysis. We must also determine how accurately it predicts new observations, where its errors occur, and whether its performance is reliable.

Regression model evaluation is an essential part of Data Science and Machine Learning because a model that performs well on training data may perform poorly on unseen data.

This chapter covers prediction errors, regression metrics, residual analysis, \(R^2\), adjusted \(R^2\), train-test splitting, cross-validation, overfitting, underfitting, generalisation, data leakage, and practical evaluation workflows.

**Scope:** Regression equations, coefficient interpretation, and model construction are covered in `10_Regression`. Detailed bias-variance theory is covered in `14_Bias_and_Variance`.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain why regression models require evaluation.
2. Calculate residuals, SSE, MSE, RMSE, and MAE.
3. Understand MAPE and its limitations.
4. Calculate and interpret \(R^2\) and adjusted \(R^2\).
5. Distinguish training, validation, and test data.
6. Explain generalisation, overfitting, and underfitting.
7. Understand k-fold cross-validation.
8. Interpret residual plots and actual-versus-predicted plots.
9. Compare models using appropriate evaluation metrics.
10. Identify data leakage and avoid common evaluation mistakes.
11. Implement regression evaluation using Python and scikit-learn.

# 2. Why Do We Evaluate a Regression Model?

Suppose a model predicts examination marks.

The predicted mark is 60, while the actual mark is 65.

The prediction error is:

$$
e = y-\hat{y}
$$

$$
e = 65-60=5
$$

The model underpredicted the actual mark by 5.

A regression model usually makes many predictions. We therefore need evaluation measures to understand the size of its errors, its performance on unseen observations, and whether it is better than alternative models.

# 3. Prediction Errors, Absolute Errors, and Squared Errors

For observation \(i\), the residual or prediction error is:

$$
e_i=y_i-\hat{y}_i
$$

Here, \(y_i\) is the actual value and \(\hat{y}_i\) is the predicted value.

A positive residual means the model underpredicted the observation. A negative residual means the model overpredicted it.

The absolute error measures the magnitude of the error without considering its direction:

$$
|e_i|=|y_i-\hat{y}_i|
$$

The squared error is:

$$
e_i^2=(y_i-\hat{y}_i)^2
$$

Squaring prevents positive and negative errors from cancelling and gives larger errors greater influence.

For example, an error of 2 produces a squared error of 4, whereas an error of 10 produces a squared error of 100.

## 3.1 Worked Example

Consider the following actual and predicted values.

| Observation | Actual | Predicted |
|---|---:|---:|
| 1 | 50 | 48 |
| 2 | 60 | 63 |
| 3 | 70 | 68 |
| 4 | 80 | 76 |

The errors are:

$$
e=[2,-3,2,4]
$$

The absolute errors are:

$$
|e|=[2,3,2,4]
$$

The squared errors are:

$$
e^2=[4,9,4,16]
$$

These quantities form the basis of several regression evaluation metrics.

# 4. Sum of Squared Errors (SSE)

The Sum of Squared Errors measures the total squared difference between actual and predicted values.

$$
SSE=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Using the previous example:

$$
SSE=4+9+4+16
$$

$$
SSE=33
$$

A lower SSE indicates a smaller total squared error on the same evaluation dataset. However, SSE depends on the number of observations and the scale of the response.

# 5. Mean Squared Error (MSE)

Mean Squared Error is the average of the squared prediction errors.

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Since \(SSE=33\) and \(n=4\):

$$
MSE=\frac{33}{4}=8.25
$$

MSE is measured in squared response units. If the response is measured in marks, MSE is measured in squared marks.

# 6. Root Mean Squared Error (RMSE)

Root Mean Squared Error is the square root of MSE.

$$
RMSE=\sqrt{MSE}
$$

Using the previous result:

$$
RMSE=\sqrt{8.25}
$$

$$
RMSE\approx2.87
$$

RMSE is expressed in the same units as the response, making it easier to interpret than MSE.

RMSE penalises large errors more heavily because it is based on squared errors.

# 7. Mean Absolute Error (MAE)

Mean Absolute Error calculates the average magnitude of prediction errors without squaring them.

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

Using the absolute errors from the example:

$$
MAE=\frac{2+3+2+4}{4}
$$

$$
MAE=\frac{11}{4}=2.75
$$

MAE is measured in the original response units and is often straightforward to communicate.

## 7.1 MAE vs MSE vs RMSE

| Metric | What it measures | Units | Sensitivity to large errors |
|---|---|---|---|
| MAE | Average absolute error | Original units | Lower than squared-error metrics |
| MSE | Average squared error | Squared units | High |
| RMSE | Square root of average squared error | Original units | High |

MAE is useful when average absolute error is easy to interpret. RMSE is useful when large errors should receive greater penalty.

## 7.2 Python: Calculate Regression Metrics

```python
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

y_actual = np.array([50, 60, 70, 80])
y_predicted = np.array([48, 63, 68, 76])

mae = mean_absolute_error(y_actual, y_predicted)
mse = mean_squared_error(y_actual, y_predicted)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
```

The expected results are MAE = 2.75, MSE = 8.25, and RMSE approximately 2.87.

# 8. Mean Absolute Percentage Error (MAPE)

Mean Absolute Percentage Error expresses absolute prediction errors relative to actual values.

$$
MAPE=\frac{100}{n}
\sum_{i=1}^{n}
\left|\frac{y_i-\hat{y}_i}{y_i}\right|
$$

For an actual value of 100 and a prediction of 90:

$$
\left|\frac{100-90}{100}\right|\times100=10\%
$$

The percentage error is 10%.

## 8.1 Limitations of MAPE

MAPE has important limitations:

- It is undefined when an actual value is zero.
- It can become extremely large when actual values are close to zero.
- It can behave asymmetrically for overpredictions and underpredictions.
- Percentage errors may not be meaningful for every response variable.

Therefore, MAPE should be used only when percentage-based errors make sense for the application.

# 9. Choosing an Error Metric

There is no universally best regression metric.

Use MAE when an interpretable average absolute error is important. Use RMSE when large prediction errors should be penalised more heavily. Use MAPE when relative percentage errors are meaningful and zero or near-zero actual values do not cause problems.

Two models can have different rankings under MAE and RMSE. The preferred metric should reflect the practical consequences of prediction errors.

# 10. Coefficient of Determination (\(R^2\))

The coefficient of determination measures how much variation in the response is accounted for by the fitted model relative to a mean-only baseline, under the standard regression formulation.

$$
R^2=1-\frac{SSE}{SST}
$$

Here, \(SSE\) is the residual sum of squares and \(SST\) is the total sum of squares.

The total sum of squares is:

$$
SST=\sum_{i=1}^{n}(y_i-\bar{y})^2
$$

Where \(\bar{y}\) is the mean of the actual response values.

## 10.1 Worked Example: Calculating \(R^2\)

Suppose:

$$
SSE=40,\qquad SST=200
$$

Then:

$$
R^2=1-\frac{40}{200}
$$

$$
R^2=1-0.20=0.80
$$

The fitted model accounts for 80% of the observed variation relative to the mean-only baseline.

This does **not** mean that the model causes 80% of the outcome. \(R^2\) describes a statistical relationship, not causation.

## 10.2 Interpreting \(R^2\)

An \(R^2\) of 0.80 indicates that the fitted model accounts for 80% of the observed variation under the stated formulation.

However, a high \(R^2\) does not automatically imply low prediction error on unseen data. A model may have a high \(R^2\) while still producing errors that are too large for its intended application.

For some regression settings, especially models without an intercept or evaluations on different datasets, \(R^2\) may be negative. It should therefore be interpreted in the context of the model and evaluation procedure.

## 10.3 Relationship Between \(R^2\) and Correlation

For simple linear regression with an intercept, evaluated on the same observations used to calculate the Pearson correlation:

$$
R^2=r^2
$$

For example, if \(r=0.80\):

$$
R^2=(0.80)^2=0.64
$$

This relationship does not mean that \(R^2\) in multiple regression equals the square of any single pairwise correlation.

# 11. Adjusted \(R^2\)

Ordinary \(R^2\) cannot decrease when additional predictors are added to a nested ordinary least-squares model fitted to the same observations.

A predictor can therefore increase \(R^2\) even when its practical contribution is small.

Adjusted \(R^2\) introduces a penalty based on the number of predictors.

$$
R^2_{\text{adj}}
=
1-\frac{(1-R^2)(n-1)}{n-p-1}
$$

Where:

- \(n\) is the number of observations.
- \(p\) is the number of predictors, excluding the intercept.
- \(R^2\) is the ordinary coefficient of determination.

## 11.1 Worked Example

Suppose:

$$
R^2=0.80,\quad n=100,\quad p=3
$$

Substituting into the formula:

$$
R^2_{\text{adj}}
=
1-\frac{(1-0.80)(100-1)}{100-3-1}
$$

$$
R^2_{\text{adj}}
=
1-\frac{19.8}{96}
$$

$$
R^2_{\text{adj}}\approx0.794
$$

The adjusted value is slightly lower than ordinary \(R^2\).

Adjusted \(R^2\) is useful when comparing models with different numbers of predictors, but it is not a substitute for evaluating predictive performance on unseen data.

## 11.2 Python: Calculate \(R^2\) and Adjusted \(R^2\)

```python
from sklearn.metrics import r2_score

y_actual = [10, 20, 30, 40, 50]
y_predicted = [12, 19, 31, 38, 49]

n = len(y_actual)
p = 2

r2 = r2_score(y_actual, y_predicted)

if n > p + 1:
    adjusted_r2 = (
        1 - (1 - r2) * (n - 1) / (n - p - 1)
    )
else:
    adjusted_r2 = float("nan")

print("R-squared:", r2)
print("Adjusted R-squared:", adjusted_r2)
```

This calculation assumes the usual definition of adjusted \(R^2\) for a regression model with an intercept and \(p\) predictors.

# 12. Training Error and Test Error

**Training error** measures model performance on the observations used to fit the model.

**Test error** measures performance on a separate set of observations that were not used to fit the final model.

A model with very low training error may still perform poorly on unseen data.

Consider the following example:

| Model | Training RMSE | Test RMSE |
|---|---:|---:|
| Model A | 2.0 | 2.5 |
| Model B | 0.8 | 6.0 |

Model B fits the training data more closely, but its test error is much higher. This suggests that Model B may have overfit the training observations.

# 13. Generalisation, Overfitting, and Underfitting

**Generalisation** means performing reasonably well on new observations from the relevant population or data-generating process.

The goal of predictive modelling is not simply to minimise training error. It is to build a model that performs well on relevant unseen data.

## 13.1 Overfitting

Overfitting occurs when a model learns noise or peculiarities in the training dataset rather than a pattern that generalises.

A common pattern is:

- Training error is very low.
- Test error is substantially higher.

More complex models are not necessarily better models.

## 13.2 Underfitting

Underfitting occurs when a model is too simple to capture important patterns in the data.

Typical signs include high training error, high test error, and systematic patterns in residual plots.

| Situation | Training error | Test error |
|---|---|---|
| Underfitting | High | High |
| Good generalisation | Low or moderate | Low |
| Overfitting | Very low | High |

These are conceptual patterns rather than strict numerical rules.

## 13.3 Bias-Variance Perspective

The bias-variance trade-off provides another way to understand model complexity.

A model that is too simple may have high bias. A highly flexible model may have high variance and respond strongly to changes in the training data.

The objective is to select a suitable level of complexity for the available data and prediction task.

Detailed theory is covered in `14_Bias_and_Variance`.

# 14. Train-Test Split

A train-test split divides the dataset into separate portions.

- The training set is used to fit the model.
- The test set is reserved for final evaluation.

An example split is 80% training data and 20% test data. The appropriate proportions depend on the dataset size and the problem.

## 14.1 Why the Test Set Must Be Protected

If the test set is repeatedly used to choose models, tune hyperparameters, or make modelling decisions, the final evaluation can become overly optimistic.

A better approach is to use validation data or cross-validation for model selection and reserve the test set for final assessment.

## 14.2 Python: Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The `random_state` makes the random split reproducible. For time-series problems, a chronological split is often more appropriate than a random split.

# 15. Validation Data

A modelling workflow may use three separate datasets.

| Dataset | Purpose |
|---|---|
| Training | Fit model parameters |
| Validation | Compare models and tune modelling choices |
| Test | Estimate final performance on held-out data |

The validation set helps select a model without repeatedly consulting the final test set.

For small datasets, a separate validation set may leave too few observations for fitting. Cross-validation can provide a more data-efficient alternative.

# 16. K-Fold Cross-Validation

K-fold cross-validation divides the available training data into \(k\) approximately equal folds.

For each round:

1. One fold is used for validation.
2. The remaining \(k-1\) folds are used for training.
3. The process is repeated until each fold has been used for validation.

For five-fold cross-validation:

| Round | Validation fold | Training folds |
|---|---|---|
| 1 | 1 | 2, 3, 4, 5 |
| 2 | 2 | 1, 3, 4, 5 |
| 3 | 3 | 1, 2, 4, 5 |
| 4 | 4 | 1, 2, 3, 5 |
| 5 | 5 | 1, 2, 3, 4 |

Each observation serves as validation data once.

## 16.1 Mean Cross-Validation Score

Suppose the validation RMSE scores are:

$$
2.1,\quad2.4,\quad2.0,\quad2.3,\quad2.2
$$

The mean score is:

$$
RMSE_{CV}=\frac{2.1+2.4+2.0+2.3+2.2}{5}
$$

$$
RMSE_{CV}=\frac{11.0}{5}=2.2
$$

The mean summarises average performance across the folds. The standard deviation of the fold scores provides information about how much the scores vary.

Cross-validation scores are estimates, not guarantees of future performance.

## 16.2 Python: K-Fold Cross-Validation

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

model = LinearRegression()

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=kf,
    scoring="neg_mean_squared_error"
)

mse_scores = -scores
rmse_scores = np.sqrt(mse_scores)

print("Fold RMSE:", rmse_scores)
print("Mean CV RMSE:", rmse_scores.mean())
print("Standard deviation:", rmse_scores.std())
```

Scikit-learn uses negative values for certain loss-based scoring functions so that larger scores consistently indicate better performance. Reverse the sign before interpreting the MSE values.

For grouped or time-dependent data, use a validation strategy that respects the data structure rather than automatically applying shuffled random folds.

# 17. Residual Analysis

A residual is:

$$
e_i=y_i-\hat{y}_i
$$

Residual analysis examines whether prediction errors show systematic patterns that a single metric might hide.

Useful questions include:

- Are residuals centred around zero?
- Does their spread change across fitted values?
- Is there a curved pattern?
- Are there unusual observations?
- Are errors dependent on time or group?
- Does the model systematically overpredict or underpredict in certain regions?

## 17.1 Residuals vs Fitted Values

A residual-versus-fitted plot places predicted values on the horizontal axis and residuals on the vertical axis.

A reasonably suitable model often produces a cloud of points around the zero line without a clear systematic pattern.

A curved pattern may indicate that the model form is inadequate. A funnel-shaped pattern may indicate changing error variance.

These plots help diagnose problems, but no single plot proves that every assumption is satisfied.

## 17.2 Python: Residual Plot

```python
import matplotlib.pyplot as plt

residuals = y_test - y_test_pred

plt.scatter(y_test_pred, residuals)
plt.axhline(0, linestyle="--")

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")

plt.show()
```

Look for patterns in the residuals rather than expecting every residual to equal zero.

# 18. Actual vs Predicted Plot

An actual-versus-predicted plot compares actual response values with model predictions.

A useful reference is the diagonal line:

$$
y=\hat{y}
$$

Points close to this line have relatively small prediction errors. Larger distances from the line indicate larger errors.

## 18.1 Python: Actual vs Predicted

```python
import matplotlib.pyplot as plt

plt.scatter(y_test, y_test_pred)

lower = min(min(y_test), min(y_test_pred))
upper = max(max(y_test), max(y_test_pred))

plt.plot([lower, upper], [lower, upper], linestyle="--")

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")

plt.show()
```

The plot complements numerical metrics by revealing prediction patterns that may not be obvious from an average error score.

# 19. Comparing Regression Models

Models should be compared using the same evaluation dataset and a metric appropriate to the task.

Suppose three models produce the following MAE values:

| Model | MAE |
|---|---:|
| A | 4.2 |
| B | 3.1 |
| C | 3.8 |

Model B has the lowest MAE among these models.

Now suppose the RMSE values are:

| Model | RMSE |
|---|---:|
| A | 5.8 |
| B | 4.2 |
| C | 4.9 |

Model B also has the lowest RMSE in this example.

However, a model may rank differently under MAE and RMSE because the metrics penalise errors differently. Model selection should consider the application, error costs, evaluation data, and model complexity.

# 20. Baseline Models

A regression model should often be compared with a simple baseline.

For a basic regression problem, a mean-prediction baseline predicts the mean response calculated from the training data for every observation:

$$
\hat{y}_i=\bar{y}_{train}
$$

If a complex model performs almost the same as this baseline on unseen data, its additional complexity may provide little predictive benefit.

A baseline gives a useful reference point for determining whether a model provides meaningful improvement.

# 21. Out-of-Sample Evaluation

Out-of-sample evaluation measures model performance on observations not used to fit the model.

Its purpose is to estimate how well the model may perform on future or otherwise unseen observations from the relevant population.

A good training score alone does not establish good out-of-sample performance.

The reliability of the estimate also depends on how representative the evaluation dataset is of the intended deployment setting.

# 22. Data Leakage

Data leakage occurs when information that would not legitimately be available during training or prediction enters the modelling process.

Examples include:

- Using test-set information to tune the model.
- Calculating preprocessing statistics from the full dataset before splitting.
- Using future information to predict an earlier outcome.
- Performing feature selection using information from the held-out test set.

Leakage can make evaluation scores appear much better than real-world performance.

## 22.1 Preprocessing and Cross-Validation

Suppose a preprocessing step calculates a feature's mean and uses it to standardise the feature.

If that mean is calculated using the full dataset before cross-validation, validation observations can influence the preprocessing applied during training.

A safer approach is to put preprocessing and the model inside a scikit-learn `Pipeline`. This ensures that preprocessing is fitted separately within each training fold.

# 23. Python: Complete Regression Evaluation Workflow

The following example combines splitting, model fitting, prediction, and evaluation.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Create an example regression dataset
X, y = make_regression(
    n_samples=300,
    n_features=5,
    noise=15,
    random_state=42
)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Training metrics
train_mae = mean_absolute_error(y_train, y_train_pred)
train_rmse = np.sqrt(
    mean_squared_error(y_train, y_train_pred)
)

# Test metrics
test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

print("Training MAE:", train_mae)
print("Training RMSE:", train_rmse)

print("Test MAE:", test_mae)
print("Test MSE:", test_mse)
print("Test RMSE:", test_rmse)
print("Test R-squared:", test_r2)
```

The training metrics describe performance on the observations used for fitting. The test metrics describe performance on the held-out test observations.

# 24. Reporting Evaluation Results

A useful evaluation report should state:

- Which dataset was used for evaluation.
- Which metrics were calculated.
- The numerical results.
- Whether residual diagnostics were examined.
- Any important limitations.

For example:

> The regression model was evaluated on a held-out test set. MAE and RMSE were used to summarise prediction error, while \(R^2\) was used to describe variation accounted for relative to a baseline. Residual plots were also examined for systematic patterns. These results describe performance on the available evaluation sample and do not establish a causal relationship.

# 25. Common Regression Evaluation Mistakes

**Evaluating only on training data.** This can hide overfitting.

**Repeatedly using the test set for model selection.** This can contaminate the final performance estimate.

**Reporting only \(R^2\).** A high \(R^2\) does not guarantee low prediction error in useful units.

**Using only one error metric.** Different metrics emphasise different aspects of model performance.

**Ignoring residual plots.** A single metric can hide systematic patterns.

**Using MAPE with zero actual values.** The formula is undefined when an actual value equals zero.

**Assuming lower training error always means a better model.** A flexible model may fit training data closely and generalise poorly.

**Ignoring data leakage.** Leakage can create unrealistically optimistic evaluation scores.

**Comparing models on different evaluation datasets.** Use comparable data and evaluation procedures.

**Ignoring practical consequences.** A numerical improvement may not be meaningful for the intended application.

# 26. Important Formula Summary

### Residual

$$
e_i=y_i-\hat{y}_i
$$

### Absolute error

$$
|e_i|=|y_i-\hat{y}_i|
$$

### Squared error

$$
e_i^2=(y_i-\hat{y}_i)^2
$$

### Sum of Squared Errors

$$
SSE=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Mean Squared Error

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Root Mean Squared Error

$$
RMSE=\sqrt{MSE}
$$

### Mean Absolute Error

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

### Mean Absolute Percentage Error

$$
MAPE=\frac{100}{n}
\sum_{i=1}^{n}
\left|\frac{y_i-\hat{y}_i}{y_i}\right|
$$

### Total Sum of Squares

$$
SST=\sum_{i=1}^{n}(y_i-\bar{y})^2
$$

### Coefficient of determination

$$
R^2=1-\frac{SSE}{SST}
$$

### Simple regression relationship

$$
R^2=r^2
$$

This relationship applies to simple linear regression with an intercept when correlation and \(R^2\) are calculated on the same observations.

### Adjusted \(R^2\)

$$
R^2_{\text{adj}}
=
1-\frac{(1-R^2)(n-1)}{n-p-1}
$$

# 27. Quick Concept Comparison

| Concept | Main purpose |
|---|---|
| Residual | Individual prediction error |
| SSE | Total squared error |
| MSE | Average squared error |
| RMSE | Square root of average squared error |
| MAE | Average absolute error |
| MAPE | Average absolute percentage error |
| \(R^2\) | Variation accounted for relative to a mean-only baseline |
| Adjusted \(R^2\) | \(R^2\) adjusted for predictor count |
| Training error | Performance on fitting data |
| Validation error | Performance used for model selection |
| Test error | Performance on held-out data |
| Cross-validation | Repeated training and validation |
| Residual plot | Visual diagnostic for systematic errors |
| Data leakage | Improper use of information during modelling |

# 28. Points to Remember

1. A regression model must be evaluated, not merely fitted.
2. MAE measures average absolute error.
3. MSE measures average squared error.
4. RMSE is expressed in the original response units.
5. RMSE penalises large errors more heavily than MAE.
6. MAPE is problematic when actual values are zero or close to zero.
7. \(R^2\) describes variation accounted for relative to a mean-only baseline.
8. Adjusted \(R^2\) accounts for the number of predictors.
9. Training performance may be overly optimistic.
10. Cross-validation helps compare models using repeated validation folds.
11. The final test set should be protected from model-selection decisions.
12. Residual plots can reveal curvature, changing variance, and unusual observations.
13. Lower error is generally preferable when the same metric and evaluation data are used.
14. Metric selection should reflect the practical cost of prediction errors.
15. Data leakage can produce misleadingly good evaluation results.
16. No single metric completely describes model quality.
17. Evaluation performance does not establish causation.
18. Regression construction belongs in Folder 10; regression evaluation belongs here.

# 29. Chapter Summary

Regression model evaluation determines how well a fitted model performs and whether its predictions are likely to generalise to unseen observations.

MAE measures average absolute error, MSE measures average squared error, and RMSE expresses the square root of average squared error in the original response units. \(R^2\) describes variation accounted for relative to a baseline, while adjusted \(R^2\) introduces a penalty for the number of predictors.

Reliable evaluation also requires separating training data from validation and test data, using cross-validation appropriately, protecting the test set, and avoiding data leakage.

Finally, numerical metrics should be combined with residual analysis. A good average score does not guarantee that a model has no systematic errors or that it will perform well in every deployment setting.

The central principle is:

$$
\text{Good evaluation}
=
\text{Appropriate metrics}
+
\text{Unseen-data testing}
+
\text{Residual analysis}
+
\text{Careful interpretation}
$$

# 30. References and Further Reading

- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [Penn State — STAT Online](https://online.stat.psu.edu/)
- [NIST/SEMATECH — e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [scikit-learn — Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [scikit-learn — Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)

# 31. Related Topics

- `10_Regression` — Regression equations, coefficients, and model construction.
- `12_Linear_Algebra` — Vectors, matrices, and matrix operations.
- `14_Bias_and_Variance` — Underfitting, overfitting, and the bias-variance trade-off.
- `15_Statistics_for_Machine_Learning` — Statistical concepts used in Machine Learning.

**Recommended file path:** `11_Regression_Model_Evaluation/README.md`
