# Regression Model Evaluation

A regression model produces predictions, but fitting a model is only the beginning of an analysis. We also need to determine **how well the model performs**, where it makes errors, and whether its performance is likely to generalise to new observations.

This chapter focuses specifically on **regression model evaluation**.

The main topics are:

- fitted values and prediction errors,
- residual analysis,
- Sum of Squared Errors,
- Mean Squared Error,
- Root Mean Squared Error,
- Mean Absolute Error,
- Mean Absolute Percentage Error,
- coefficient of determination,
- adjusted $R^2$,
- training and testing data,
- generalisation,
- underfitting and overfitting,
- validation data,
- cross-validation,
- residual plots,
- error interpretation,
- comparing regression models,
- and practical evaluation workflows.

The construction of regression equations, interpretation of slopes and intercepts, categorical predictors, interaction terms, and polynomial regression are covered in **Folder 10 — Regression**.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain why regression models need to be evaluated.
2. Define prediction error and residual.
3. Calculate SSE.
4. Calculate MSE.
5. Calculate RMSE.
6. Calculate MAE.
7. Understand MAPE and its limitations.
8. Explain $R^2$.
9. Explain adjusted $R^2$.
10. Understand the difference between training and testing data.
11. Explain generalisation.
12. Identify the basic ideas of underfitting and overfitting.
13. Understand validation data.
14. Explain cross-validation.
15. Calculate and interpret residuals.
16. Use residual plots to identify systematic problems.
17. Compare regression models using appropriate metrics.
18. Understand why a single metric should not be used blindly.
19. Implement regression evaluation in Python.
20. Build a basic model-evaluation workflow.

---

# 2. Why Do We Evaluate a Regression Model?

Suppose a model predicts examination marks.

The model may produce:

$\hat{Y}=60$

for a student whose actual mark is:

$Y=65$

The prediction is not exact.

Therefore:

$\text{Error}=Y-\hat{Y}$

$\text{Error}=65-60=5$

A model can make many such predictions.

We need summary measures that tell us:

- how large the errors are,
- whether errors are systematically biased,
- how well the model fits observed data,
- how well it performs on unseen data,
- whether one model is better than another.

This is the purpose of regression model evaluation.

---

# 3. Prediction Error

For observation $i$:

$e_i=y_i-\hat{y}_i$

where:

- $y_i$ = actual response,
- $\hat{y}_i$ = predicted response,
- $e_i$ = prediction error or residual.

The sign tells us the direction of the error.

### Positive error

$e_i>0$

means:

$y_i>\hat{y}_i$

The model underpredicted.

### Negative error

$e_i<0$

means:

$y_i<\hat{y}_i$

The model overpredicted.

---

# 4. Absolute Error

The absolute error is:

$|e_i|=|y_i-\hat{y}_i|$

Absolute error ignores the direction and measures only the size of the error.

For example, if:

$e=-7$

then:

$|e|=7$

---

# 5. Squared Error

The squared error is:

$e_i^2=(y_i-\hat{y}_i)^2$

Squaring removes the sign and gives greater weight to large errors.

For example:

$e=2 \Rightarrow e^2=4$

while:

$e=10 \Rightarrow e^2=100$

Therefore, metrics based on squared errors are particularly sensitive to large prediction errors.

---

# 6. Example: Prediction Errors

Suppose the actual and predicted values are:

| Observation | Actual ($y$) | Predicted ($\hat{y}$) |
|---|---:|---:|
| 1 | 50 | 48 |
| 2 | 60 | 63 |
| 3 | 70 | 68 |
| 4 | 80 | 76 |

Calculate:

$e_i=y_i-\hat{y}_i$

| Observation | Actual | Predicted | Error | Absolute Error | Squared Error |
|---|---:|---:|---:|---:|---:|
| 1 | 50 | 48 | 2 | 2 | 4 |
| 2 | 60 | 63 | -3 | 3 | 9 |
| 3 | 70 | 68 | 2 | 2 | 4 |
| 4 | 80 | 76 | 4 | 4 | 16 |

These values form the basis for several evaluation metrics.

---

# 7. Sum of Squared Errors

The **Sum of Squared Errors** is:

$SSE=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$

Using the example:

$SSE=4+9+4+16$

$\boxed{SSE=33}$

A smaller SSE indicates smaller total squared prediction error for the same dataset.

However, SSE depends on sample size and the units of the response.

---

# 8. Mean Squared Error

The **Mean Squared Error** is:

$MSE= \frac{1}{n} \sum_{i=1}^{n}(y_i-\hat{y}_i)^2$

Since:

$SSE=33$

and:

$n=4$

we obtain:

$MSE=\frac{33}{4}$

$\boxed{MSE=8.25}$

MSE is the average squared prediction error.

Its units are the **square of the response units**.

---

# 9. Root Mean Squared Error

The **Root Mean Squared Error** is:

$RMSE=\sqrt{MSE}$

For:

$MSE=8.25$

we obtain:

$RMSE=\sqrt{8.25}$

$\boxed{RMSE\approx2.87}$

RMSE is useful because it is expressed in the same units as the response variable.

For example, if $Y$ is measured in marks, RMSE is measured in marks.

---

# 10. Why RMSE Is Sensitive to Large Errors

Because RMSE is based on squared errors, large errors receive more weight.

Suppose two models have errors:

Model A:

$[1,1,1,10]$

Model B:

$[3,3,3,3]$

Model A has one very large error.

Squared errors for Model A:

$1^2+1^2+1^2+10^2=103$

Squared errors for Model B:

$3^2+3^2+3^2+3^2=36$

Therefore, RMSE strongly penalises the large error in Model A.

---

# 11. Mean Absolute Error

The **Mean Absolute Error** is:

$MAE= \frac{1}{n} \sum_{i=1}^{n}|y_i-\hat{y}_i|$

For the example:

$MAE= \frac{2+3+2+4}{4}$

$MAE=\frac{11}{4}$

$\boxed{MAE=2.75}$

MAE is expressed in the same units as the response.

---

# 12. MAE vs RMSE

| Metric | Formula basis | Units | Large-error sensitivity |
|---|---|---|---|
| MAE | Absolute errors | Same as $Y$ | Lower |
| MSE | Squared errors | Squared units | High |
| RMSE | Square root of MSE | Same as $Y$ | High |

If large errors are especially undesirable, RMSE can be useful.

If we want an easier-to-interpret average error magnitude, MAE is often useful.

---

# 13. Mean Absolute Percentage Error

The **Mean Absolute Percentage Error** is commonly written as:

$MAPE= \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i-\hat{y}_i}{y_i} \right|$

MAPE expresses average absolute error relative to the actual value.

For example, if the actual value is 100 and the prediction is 90:

$\left|\frac{100-90}{100}\right| =0.10$

or:

$10\%$

---

# 14. Limitation of MAPE

MAPE has an important problem when actual values are zero:

$y_i=0$

because division by zero is undefined.

MAPE can also behave poorly when actual values are very close to zero.

Therefore, MAPE should not be used blindly.

The suitability of percentage-based errors depends on the response variable and application.

---

# 15. Worked Comparison of MAE, MSE, and RMSE

Consider:

| Actual | Predicted |
|---:|---:|
| 10 | 8 |
| 20 | 22 |
| 30 | 27 |

Errors:

$[2,-2,3]$

Absolute errors:

$[2,2,3]$

Squared errors:

$[4,4,9]$

### MAE

$MAE= \frac{2+2+3}{3}$

$\boxed{MAE=\frac{7}{3}\approx2.33}$

### MSE

$MSE= \frac{4+4+9}{3}$

$\boxed{MSE=\frac{17}{3}\approx5.67}$

### RMSE

$RMSE=\sqrt{5.67}$

$\boxed{RMSE\approx2.38}$

---

# 16. Choosing an Error Metric

There is no universally best metric.

Use **MAE** when:

- you want a straightforward average absolute error,
- all errors should be treated more evenly,
- interpretability in response units is important.

Use **RMSE** when:

- large errors should receive greater penalty,
- large mistakes are especially important,
- the squared-error framework is appropriate.

Use **MAPE** only when percentage error is meaningful and zero or near-zero actual values are not problematic.

---

# 17. Coefficient of Determination

The **coefficient of determination** is:

$R^2$

In the standard regression setting:

$R^2= 1-\frac{SSE}{SST}$

where:

- $SSE$ = residual sum of squares,
- $SST$ = total sum of squares.

The total sum of squares is:

$SST= \sum_{i=1}^{n}(y_i-\bar{y})^2$

---

# 18. Understanding $SST$

The total sum of squares measures total variation in the observed response around its mean.

$SST= \sum(y_i-\bar{y})^2$

For example, if:

$y=[10,20,30]$

then:

$\bar{y}=20$

and:

$SST=(10-20)^2+(20-20)^2+(30-20)^2$

$SST=100+0+100$

$\boxed{SST=200}$

---

# 19. Interpretation of $R^2$

Suppose:

$R^2=0.80$

In the standard regression interpretation, the fitted model accounts for 80% of the observed variation in the response relative to the mean-only baseline.

The remaining 20% is not accounted for by that fitted relationship.

It is incorrect to automatically say:

> The model causes 80% of the outcome.

$R^2$ is about variation explained by the fitted model, not causation.

---

# 20. Worked Example: $R^2$

Suppose:

$SSE=40$

and:

$SST=200$

Then:

$R^2= 1-\frac{40}{200}$

$R^2=1-0.20$

$\boxed{R^2=0.80}$

Thus, the fitted model accounts for 80% of the variation relative to the mean-only baseline.

---

# 21. Relationship Between $R^2$ and Correlation

For simple linear regression with an intercept:

$R^2=r^2$

For example, if:

$r=0.80$

then:

$R^2=(0.80)^2$

$\boxed{R^2=0.64}$

This direct relationship applies to simple linear regression with an intercept.

In multiple regression, $R^2$ is not simply the square of one pairwise correlation.

---

# 22. Adjusted $R^2$

Adding predictors to a regression model cannot decrease ordinary $R^2$.

Even a weak or irrelevant predictor can cause $R^2$ to increase slightly.

Adjusted $R^2$ introduces a penalty for model complexity.

A common formula is:

$R^2_{\text{adj}} = 1- \frac{(1-R^2)(n-1)} {n-p-1}$

where:

- $n$ = sample size,
- $p$ = number of predictors,
- $R^2$ = ordinary coefficient of determination.

Adjusted $R^2$ can decrease when an additional predictor does not provide enough improvement.

---

# 23. Worked Example: Adjusted $R^2$

Suppose:

$R^2=0.80$

with:

$n=100$

and:

$p=3$

Then:

$R^2_{\text{adj}} = 1- \frac{(1-0.80)(100-1)} {100-3-1}$

$= 1- \frac{0.20(99)} {96}$

$= 1-\frac{19.8}{96}$

$\boxed{R^2_{\text{adj}}\approx0.794}$

The adjusted value is slightly lower because the model contains multiple predictors.

---

# 24. $R^2$ vs Adjusted $R^2$

| Feature | $R^2$ | Adjusted $R^2$ |
|---|---|---|
| Measures model variation explained | Yes | Yes |
| Penalises number of predictors | No | Yes |
| Can decrease when predictor is added | No | Yes |
| Useful for comparing models with different predictor counts | Limited | More useful |

Neither measure should be interpreted as a complete evaluation of predictive performance.

---

# 25. Training Error

Suppose a model is fitted using a training dataset.

The predictions on that same dataset are called **training predictions**.

Training error measures how well the model fits data it has already seen.

For example:

$RMSE_{\text{train}}$

measures prediction error on the training data.

A very flexible model can have very small training error while performing poorly on new data.

---

# 26. Test Error

A **test dataset** contains observations that were not used to fit the final model.

Test error measures performance on unseen data.

For example:

$RMSE_{\text{test}}$

is calculated from test-set predictions.

A model that performs well on unseen data is more useful for prediction than one that only fits the training observations.

---

# 27. Training vs Test Performance

Suppose two models have:

| Model | Training RMSE | Test RMSE |
|---|---:|---:|
| Model A | 2.0 | 2.5 |
| Model B | 0.8 | 6.0 |

Model B fits the training data much better, but its test performance is much worse.

This is a warning sign of **overfitting**.

Model A may generalise better.

---

# 28. Generalisation

**Generalisation** means that a model performs reasonably well on new observations from the same relevant population or data-generating process.

The goal of predictive modelling is not merely:

$\text{minimise training error}$

but rather to obtain a model that performs well on appropriate unseen data.

Conceptually:

$\boxed{ \text{Good model} \Rightarrow \text{Good performance on relevant unseen data} }$

---

# 29. Overfitting

**Overfitting** occurs when a model captures noise or idiosyncrasies in the training data rather than learning a pattern that generalises well.

Typical pattern:

$\text{Training error}\downarrow$

while:

$\text{Test error}\uparrow$

As model complexity increases, training performance often improves, but test performance may eventually deteriorate.

---

# 30. Underfitting

**Underfitting** occurs when a model is too simple to capture important structure in the data.

Typical signs include:

- high training error,
- high test error,
- systematic patterns remaining in residuals.

A useful conceptual comparison is:

| Situation | Training Error | Test Error |
|---|---:|---:|
| Underfitting | High | High |
| Good generalisation | Low/moderate | Low |
| Overfitting | Very low | High |

These are conceptual patterns rather than strict numerical rules.

---

# 31. Bias-Variance Perspective

Prediction error can be understood through the bias-variance trade-off.

A highly simple model may have:

- high bias,
- low variance.

A highly flexible model may have:

- low bias,
- high variance.

The goal is to find a level of complexity that balances these sources of error.

The detailed Bias and Variance chapter is covered separately in **Folder 14**.

---

# 32. Train-Test Split

A common evaluation workflow is to divide the dataset into:

- training set,
- test set.

For example:

$80\%$

training and:

$20\%$

testing.

The model is fitted on the training set and evaluated on the test set.

The exact split depends on the dataset size, problem, and evaluation strategy.

---

# 33. Why the Test Set Must Be Protected

If we repeatedly use the test set to choose the model, tune hyperparameters, or make many decisions, the test set is no longer an unbiased final evaluation.

Therefore:

> The test set should ideally be used for final performance assessment after the modelling choices have been made.

When repeated model selection is necessary, validation or cross-validation should be used.

---

# 34. Validation Set

A three-way split can contain:

1. training set,
2. validation set,
3. test set.

The training set is used to fit models.

The validation set is used to compare or tune modelling choices.

The test set is reserved for final evaluation.

Conceptually:

$\text{Data} \rightarrow \begin{cases} \text{Training}\\ \text{Validation}\\ \text{Test} \end{cases}$

For small datasets, using a separate validation set may waste too much data, which motivates cross-validation.

---

# 35. Cross-Validation

**Cross-validation** repeatedly divides the training data into fitting and validation portions.

The most common form is **$k$-fold cross-validation**.

The dataset is divided into $k$ approximately equal folds.

For each round:

- one fold is used for validation,
- the remaining $k-1$ folds are used for training.

This process is repeated until every fold has served as the validation fold.

---

# 36. Five-Fold Cross-Validation

For:

$k=5$

the process is:

| Round | Training Folds | Validation Fold |
|---|---|---|
| 1 | 2,3,4,5 | 1 |
| 2 | 1,3,4,5 | 2 |
| 3 | 1,2,4,5 | 3 |
| 4 | 1,2,3,5 | 4 |
| 5 | 1,2,3,4 | 5 |

Each observation is used for validation exactly once.

---

# 37. Cross-Validation Score

Suppose the five validation RMSE values are:

$2.1,\quad2.4,\quad2.0,\quad2.3,\quad2.2$

The mean cross-validation RMSE is:

$RMSE_{CV} = \frac{2.1+2.4+2.0+2.3+2.2}{5}$

$RMSE_{CV} = \frac{11.0}{5}$

$\boxed{RMSE_{CV}=2.2}$

The variation among fold scores can also provide useful information about model stability.

---

# 38. Standard Deviation of Cross-Validation Scores

Suppose validation scores vary substantially across folds.

This may indicate that model performance depends strongly on which observations are used for validation.

Therefore, it is often useful to report:

$\text{mean CV score}$

along with:

$\text{standard deviation of CV scores}$

For example:

$2.20\pm0.15$

can summarise the average and variation across folds, depending on the reporting convention.

---

# 39. Cross-Validation and the Test Set

A common workflow is:

1. split data into training and test sets,
2. perform cross-validation only on the training data,
3. choose or tune the model,
4. fit the final selected model on the training data,
5. evaluate once on the untouched test set.

This helps keep the final test estimate separate from model-selection decisions.

---

# 40. Residual Analysis

A residual is:

$e_i=y_i-\hat{y}_i$

Residual analysis examines whether residuals show systematic patterns.

A useful residual analysis asks:

- Are residuals centred around zero?
- Is the spread reasonably stable?
- Is there curvature?
- Are there unusual observations?
- Is there dependence?
- Does the model systematically underpredict or overpredict in certain regions?

---

# 41. Residuals vs Fitted Values

A residual-versus-fitted plot places:

- fitted values on the horizontal axis,
- residuals on the vertical axis.

A well-behaved pattern often resembles a random cloud around:

$e=0$

A systematic curve may indicate that the model has not captured the relationship adequately.

A funnel shape may indicate changing error variance.

---

# 42. Example of a Good Residual Pattern

Conceptually:

```
Residual
   │  •     •
   │     •
 0 ├ •   •    •
   │    •
   │ •      •
   └──────────────── Fitted
```

There is no obvious systematic shape.

This does not prove that every assumption is satisfied, but it is more consistent with a reasonable model form.

---

# 43. Example of a Curved Residual Pattern

Conceptually:

```
Residual
   │ •           •
   │   •       •
 0 ├     •   •
   │       •
   │
   └──────────────── Fitted
```

A systematic curve suggests that a straight-line model may not adequately capture the relationship.

Possible remedies depend on the context and may include a different functional form or additional predictors.

---

# 44. Example of Heteroscedasticity

Conceptually:

```
Residual
   │       •
   │     •   •
 0 ├  • •     •
   │ •       •   •
   │             •
   └──────────────── Fitted
```

If residual spread grows with fitted values, the variance may not be constant.

This is a possible sign of heteroscedasticity.

---

# 45. Residual Mean

For ordinary least squares with an intercept:

$\sum e_i=0$

Therefore:

$\bar{e}=0$

This is a mathematical property of the fitted model.

It does not prove that the model is good.

A model can have residuals that sum to zero while still having large or systematically structured errors.

---

# 46. Comparing Models Using MAE

Suppose:

| Model | MAE |
|---|---:|
| A | 4.2 |
| B | 3.1 |
| C | 3.8 |

Lower MAE indicates smaller average absolute prediction error.

Therefore, among these models:

$3.1<3.8<4.2$

Model B has the smallest MAE.

However, model selection should consider the evaluation dataset, metric suitability, uncertainty, and model purpose.

---

# 47. Comparing Models Using RMSE

Suppose:

| Model | RMSE |
|---|---:|
| A | 5.8 |
| B | 4.2 |
| C | 4.9 |

The lowest RMSE is:

$4.2$

Therefore, Model B has the lowest RMSE among the three models on this evaluation dataset.

Because RMSE penalises large errors, it may prefer a model that avoids particularly large mistakes.

---

# 48. Metric Choice Changes Model Ranking

Two models may have different rankings under different metrics.

For example:

| Model | MAE | RMSE |
|---|---:|---:|
| A | 2.0 | 5.0 |
| B | 2.3 | 3.2 |

Model A has lower MAE.

Model B has lower RMSE.

This may happen because Model A makes one or more unusually large errors.

Therefore, metric selection should reflect what kinds of errors matter.

---

# 49. Error Distribution

It is useful to examine the distribution of residuals.

A histogram can show:

- centre,
- spread,
- skewness,
- unusual values.

However, a histogram alone cannot establish that regression assumptions are satisfied.

Residual plots and subject-matter knowledge should also be considered.

---

# 50. Actual vs Predicted Plot

An actual-vs-predicted plot compares:

- actual response values,
- predicted values.

A good predictive relationship generally places points near the diagonal line:

$y=\hat{y}$

Conceptually:

```
Actual
  │             •
  │          •
  │       •
  │    •
  │ •
  └──────────────── Predicted
```

Large deviations from the diagonal represent larger prediction errors.

---

# 51. Error in Original Units

One advantage of MAE and RMSE is that they can be interpreted in the response's original units.

Suppose:

$RMSE=4.5$

and $Y$ is measured in marks.

Then a typical model error, interpreted through RMSE, is on the scale of approximately 4.5 marks.

This is often easier to communicate than:

$MSE=20.25$

because MSE is measured in squared marks.

---

# 52. Baseline Model

A regression model should often be compared with a simple baseline.

For a basic regression problem, a mean-prediction baseline predicts:

$\hat{y}_i=\bar{y}_{train}$

for every observation.

The model should demonstrate useful predictive improvement over a meaningful baseline.

This is particularly important when $R^2$ or another metric is considered in isolation.

---

# 53. Baseline Example

Suppose the training mean is:

$\bar{y}=50$

The baseline predicts:

$\hat{y}=50$

for every test observation.

If a complex regression model has almost the same test error as this baseline, the additional model complexity may not provide much predictive value.

---

# 54. Out-of-Sample Evaluation

The most important predictive evaluation is usually performance on observations not used to fit the model.

This is called **out-of-sample evaluation**.

The goal is to estimate how the model will behave on future or otherwise unseen observations from the relevant population.

---

# 55. Data Leakage

**Data leakage** occurs when information that should not be available during model fitting or model selection enters the modelling process.

Examples include:

- using test-set information while tuning the model,
- calculating preprocessing statistics from the full dataset before splitting,
- using future information to predict the past.

Leakage can make evaluation results look much better than real-world performance.

---

# 56. Preprocessing and Cross-Validation

Suppose a preprocessing step calculates the mean of a feature.

If the mean is calculated using the entire dataset before cross-validation, validation folds can indirectly influence the training process.

A safer workflow is to perform preprocessing inside the cross-validation pipeline.

In scikit-learn, a `Pipeline` can help keep preprocessing and modelling together.

---

# 57. Model Evaluation With Python

A basic evaluation workflow can use scikit-learn:

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)
```

---

# 58. Train-Test Split in Python

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The `random_state` makes the split reproducible.

---

# 59. Fit and Evaluate a Regression Model

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
```

Then calculate metrics separately for training and testing data.

```python
train_rmse = np.sqrt(
    mean_squared_error(y_train, y_train_pred)
)

test_rmse = np.sqrt(
    mean_squared_error(y_test, y_test_pred)
)

print("Training RMSE:", train_rmse)
print("Test RMSE:", test_rmse)
```

---

# 60. K-Fold Cross-Validation in Python

```python
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="neg_mean_squared_error"
)

mse_scores = -scores
rmse_scores = np.sqrt(mse_scores)

print("Fold RMSE:", rmse_scores)
print("Mean CV RMSE:", rmse_scores.mean())
print("Std CV RMSE:", rmse_scores.std())
```

Scikit-learn returns negative loss values for certain scoring functions because its scoring convention treats larger scores as better. Therefore, the sign must be reversed before interpreting MSE.

---

# 61. Cross-Validation With MAE

```python
mae_scores = -cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="neg_mean_absolute_error"
)

print("Fold MAE:", mae_scores)
print("Mean CV MAE:", mae_scores.mean())
```

---

# 62. Cross-Validation With $R^2$

```python
r2_scores = cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="r2"
)

print("Fold R2:", r2_scores)
print("Mean CV R2:", r2_scores.mean())
```

Because $R^2$ is already represented as a higher-is-better score, no sign reversal is required.

---

# 63. Residual Plot in Python

```python
residuals = y_test - y_test_pred

plt.scatter(y_test_pred, residuals)

plt.axhline(0, linestyle="--")

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")

plt.show()
```

Look for systematic patterns rather than expecting all residuals to be exactly zero.

---

# 64. Actual vs Predicted Plot in Python

```python
plt.scatter(y_test, y_test_pred)

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")

plt.show()
```

A closer alignment with the diagonal relationship:

$y=\hat{y}$

generally indicates smaller prediction errors.

---

# 65. Evaluation Workflow

A practical evaluation workflow can be organised as:

### Step 1: Define the prediction task

Clearly identify the response and what constitutes a useful prediction.

### Step 2: Create an appropriate data split

Keep a final test set separate when possible.

### Step 3: Fit the model using training data

Do not use test information during fitting.

### Step 4: Use validation or cross-validation

Use training data to compare model choices.

### Step 5: Select the model

Choose based on appropriate metrics and practical considerations.

### Step 6: Fit the selected model appropriately

Use the available training data according to the evaluation plan.

### Step 7: Evaluate on the untouched test set

Calculate the final out-of-sample metrics.

### Step 8: Inspect errors

Use residual plots and other diagnostics.

### Step 9: Report limitations

Explain the data, metric, split, and assumptions.

---

# 66. A Complete Evaluation Example

Suppose a model produces the following test results:

| Actual | Predicted |
|---:|---:|
| 50 | 48 |
| 60 | 63 |
| 70 | 68 |
| 80 | 76 |

We already have:

$MAE=2.75$

and:

$MSE=8.25$

Therefore:

$RMSE=\sqrt{8.25}$

$\boxed{RMSE\approx2.87}$

Suppose the total variation is:

$SST=200$

and:

$SSE=33$

Then:

$R^2= 1-\frac{33}{200}$

$\boxed{R^2=0.835}$

The model therefore has:

- MAE = 2.75 response units,
- RMSE $\approx2.87$ response units,
- $R^2\approx0.835$ under the stated regression formulation.

These metrics answer different questions and should be interpreted together.

---

# 67. Model Evaluation Report

A useful report might say:

> The regression model was evaluated on a held-out test set. The model achieved an MAE of 2.75 units and an RMSE of approximately 2.87 units. The fitted model had an $R^2$ of approximately 0.835 relative to the mean-only baseline. Residual plots were also examined for systematic patterns. These results describe performance on the available evaluation sample and should not automatically be interpreted as evidence of causal relationships.

---

# 68. What a Good Evaluation Does Not Mean

A model with a low test RMSE does not automatically mean:

- the model is causal,
- the model is universally accurate,
- the model will work on a different population,
- the data contain no bias,
- the model satisfies every assumption,
- the model is the simplest or most useful choice.

Evaluation results are conditional on the dataset, target, metric, and evaluation procedure.

---

# 69. Common Mistakes

### Mistake 1: Evaluating only on training data

This can hide overfitting.

### Mistake 2: Using the test set repeatedly

Repeated test-set decisions can contaminate the final evaluation.

### Mistake 3: Reporting only $R^2$

A high $R^2$ does not necessarily imply low prediction error in useful units.

### Mistake 4: Reporting only one error metric

Different metrics emphasise different aspects of prediction error.

### Mistake 5: Ignoring residual patterns

A single summary metric can hide systematic errors.

### Mistake 6: Using MAPE with zero actual values

MAPE is undefined when the actual value is zero.

### Mistake 7: Treating lower training error as automatically better

A flexible model can achieve low training error while generalising poorly.

### Mistake 8: Data leakage

Using information from validation or test data during training can produce overly optimistic results.

### Mistake 9: Comparing metrics from different datasets

Metrics should be compared on comparable evaluation data.

### Mistake 10: Ignoring the practical meaning of an error

A numerical improvement may not matter if it is too small for the application.

---

# 70. Important Formula Summary

### Prediction error / residual

$e_i=y_i-\hat{y}_i$

### Absolute error

$|e_i|=|y_i-\hat{y}_i|$

### Squared error

$e_i^2=(y_i-\hat{y}_i)^2$

### Sum of Squared Errors

$SSE=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$

### Mean Squared Error

$MSE= \frac{1}{n} \sum_{i=1}^{n}(y_i-\hat{y}_i)^2$

### Root Mean Squared Error

$RMSE=\sqrt{MSE}$

### Mean Absolute Error

$MAE= \frac{1}{n} \sum_{i=1}^{n}|y_i-\hat{y}_i|$

### Mean Absolute Percentage Error

$MAPE= \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i-\hat{y}_i}{y_i} \right|$

### Total Sum of Squares

$SST= \sum_{i=1}^{n}(y_i-\bar{y})^2$

### Coefficient of determination

$R^2= 1-\frac{SSE}{SST}$

### Simple regression relationship

$R^2=r^2$

for simple linear regression with an intercept.

### Adjusted $R^2$

$R^2_{\text{adj}} = 1- \frac{(1-R^2)(n-1)} {n-p-1}$

---

# 71. Quick Concept Comparison

| Concept | Main purpose |
|---|---|
| Residual | Individual prediction error |
| SSE | Total squared error |
| MSE | Average squared error |
| RMSE | Square-rooted average squared error |
| MAE | Average absolute error |
| MAPE | Average absolute percentage error |
| $R^2$ | Variation accounted for relative to a mean-only baseline |
| Adjusted $R^2$ | $R^2$ with a predictor-complexity penalty |
| Training error | Performance on data used for fitting |
| Validation error | Performance used during model selection/tuning |
| Test error | Final performance on held-out data |
| Cross-validation | Repeated training/validation evaluation |
| Residual plot | Visual diagnostic for systematic error patterns |

---

# 72. Points to Remember

1. A regression model must be evaluated, not merely fitted.
2. Residuals are:
   $$
   e_i=y_i-\hat{y}_i
   $$
3. MAE measures average absolute error.
4. MSE measures average squared error.
5. RMSE is in the original response units.
6. RMSE penalises large errors more strongly than MAE.
7. MAPE can be problematic with zero or near-zero actual values.
8. $R^2$ measures variation accounted for relative to a mean-only baseline.
9. Adjusted $R^2$ accounts for the number of predictors.
10. Training performance can be overly optimistic.
11. Test performance estimates out-of-sample performance.
12. Cross-validation helps evaluate model choices using repeated validation folds.
13. The final test set should be protected from repeated model selection.
14. Residual plots can reveal curvature, changing variance, and unusual observations.
15. Lower error is generally better when the same metric and evaluation data are used.
16. A metric should be selected according to the practical cost of prediction errors.
17. Data leakage can produce unrealistically good evaluation results.
18. No single metric completely describes model quality.
19. Evaluation performance does not establish causation.
20. Folder 11 evaluates regression models; regression construction belongs to Folder 10.

---

# 73. Chapter Summary

Regression model evaluation determines how well a fitted model performs and whether its predictions are likely to generalise.

The fundamental prediction error is:

$e_i=y_i-\hat{y}_i$

From these errors we obtain several important metrics.

MAE measures average absolute error:

$MAE= \frac{1}{n}\sum|y_i-\hat{y}_i|$

MSE averages squared errors:

$MSE= \frac{1}{n}\sum(y_i-\hat{y}_i)^2$

RMSE converts MSE back to the original response scale:

$RMSE=\sqrt{MSE}$

$R^2$ compares residual variation with total variation:

$R^2=1-\frac{SSE}{SST}$

Adjusted $R^2$ introduces a penalty for the number of predictors.

Good evaluation also requires separating training performance from unseen-data performance. Train-test splits, validation sets, and cross-validation help estimate how well a model generalises.

Finally, numerical metrics should be combined with residual analysis. A model with a good average metric can still have systematic errors, outliers, or changing variance.

The central principle is:

$\boxed{ \text{Good regression evaluation} = \text{appropriate metrics} + \text{unseen-data testing} + \text{residual analysis} + \text{careful interpretation} }$

---

# 74. References

- OpenStax, *Introductory Statistics*.
- Penn State University, STAT Online resources.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*.
- scikit-learn Documentation, Model Evaluation.
- pandas Documentation.
- NumPy Documentation.
- GeeksforGeeks, educational resources on regression metrics and model evaluation.
