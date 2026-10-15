# Regression

Regression is a statistical method used to describe and model the relationship between a **response variable** and one or more **predictor variables**. It is widely used in Statistics, Data Science, Machine Learning, forecasting, and predictive analytics.

Correlation measures the strength and direction of association between two variables. Regression goes further by estimating a mathematical relationship that can be used to explain patterns and predict the response from predictor information.

![Linear regression line with observed points and residuals](https://miro.medium.com/1%2AjTznOE9Gq6QVrGJ5eVQI4A.png)

*Visual reference: observed data points, a fitted line, and residual errors. Source: [Simple Linear Regression Using Example](https://medium.com/%40sachin.hs20/simple-linear-regression-using-example-e4e2a89df54c).*

This chapter covers simple linear regression, least squares, coefficient interpretation, residuals, multiple regression, categorical predictors, interaction terms, polynomial regression, transformations, prediction, and basic assumptions.

**Scope:** Detailed model-evaluation metrics such as MAE, MSE, RMSE, R-squared, adjusted R-squared, and cross-validation are covered in `11_Regression_Model_Evaluation`.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain regression and its applications.
2. Identify response and predictor variables.
3. Understand simple and multiple linear regression.
4. Interpret regression slopes and intercepts.
5. Calculate a regression equation using least squares.
6. Understand fitted values, residuals, and residual sum of squares.
7. Make predictions using a fitted model.
8. Distinguish interpolation from extrapolation.
9. Represent categorical predictors using indicator variables.
10. Understand interaction terms and polynomial regression.
11. Explain the basic assumptions of linear regression.
12. Implement regression using Python and scikit-learn.

# 2. What Is Regression?

Regression models how a response variable changes in relation to one or more predictor variables.

For example, a university may want to study the relationship between study hours and examination marks.

Here:

- \(X\) represents study hours.
- \(Y\) represents examination marks.

A simple linear regression model is:

$$
Y = \beta_0 + \beta_1 X + \varepsilon
$$

Where:

- \(Y\) is the response variable.
- \(X\) is the predictor variable.
- \(\beta_0\) is the population intercept.
- \(\beta_1\) is the population slope.
- \(\varepsilon\) is the random error.

After estimating the model from observed data, the fitted regression equation is:

$$
\hat{Y} = b_0 + b_1 X
$$

Here, \(\hat{Y}\) is the predicted response, while \(b_0\) and \(b_1\) are the estimated intercept and slope.

## 2.1 Regression Terminology

| Term | Meaning |
|---|---|
| Response variable | Variable being predicted or explained |
| Outcome variable | Another name for the response |
| Dependent variable | Traditional term for the response |
| Predictor variable | Variable used to predict the response |
| Explanatory variable | Another name for a predictor |
| Independent variable | Traditional term for a predictor |
| Feature | Common Machine Learning term for a predictor |

In this chapter, the terms **response** and **predictor** are used to make the roles of the variables clear.

# 3. Simple Linear Regression

Simple linear regression uses one predictor and represents its systematic relationship with the response using a straight line.

The fitted equation is:

$$
\hat{Y} = b_0 + b_1 X
$$

The equation contains two coefficients: the intercept and the slope.

## 3.1 Understanding the Intercept

The intercept \(b_0\) is the predicted response when the predictor equals zero.

Starting with:

$$
\hat{Y} = b_0 + b_1 X
$$

When \(X=0\):

$$
\hat{Y} = b_0 + b_1(0)
$$

Therefore:

$$
\hat{Y} = b_0
$$

For example, consider:

$$
\hat{Y} = 35 + 6X
$$

The intercept is 35. The model predicts 35 marks when study hours equal zero.

**Important:** An intercept may not have a meaningful practical interpretation if zero lies outside the observed data range or has no real-world meaning.

## 3.2 Understanding the Slope

The slope \(b_1\) describes the estimated change in the predicted response for a one-unit increase in the predictor.

For the equation:

$$
\hat{Y} = 35 + 6X
$$

The slope is 6. According to this model, one additional hour of study is associated with an increase of 6 marks in the predicted response.

A positive slope indicates an increasing fitted relationship, while a negative slope indicates a decreasing fitted relationship.

## 3.3 Units of the Slope

The slope has units equal to the units of the response divided by the units of the predictor.

$$
\text{Slope units} =
\frac{\text{Units of }Y}{\text{Units of }X}
$$

If marks are measured in marks and study time in hours, the slope is measured in marks per hour.

Changing the measurement unit of a predictor changes the numerical value of its coefficient.

## 3.4 Predicting from a Regression Equation

Suppose the fitted equation is:

$$
\hat{Y} = 35 + 6X
$$

For a student who studies five hours:

$$
\hat{Y} = 35 + 6(5)
$$

$$
\hat{Y} = 35 + 30
$$

$$
\hat{Y} = 65
$$

The predicted mark is 65. This is an estimate, not a guarantee of the student's actual result.

# 4. Fitted Values and Residuals

A fitted value is the response predicted by the regression equation for an observed predictor value.

For observation \(i\):

$$
\hat{y}_i = b_0 + b_1 x_i
$$

The residual is the difference between the observed response and the fitted response.

$$
e_i = y_i - \hat{y}_i
$$

Where:

- \(e_i\) is the residual.
- \(y_i\) is the observed response.
- \(\hat{y}_i\) is the fitted response.

A residual represents the part of an observed value not captured by the fitted prediction.

## 4.1 Interpreting Residuals

- **Positive residual:** The observed value is above the fitted value.
- **Negative residual:** The observed value is below the fitted value.
- **Zero residual:** The observed value equals the fitted value.

For example, suppose:

$$
\hat{Y} = 20 + 5X
$$

For \(X=6\):

$$
\hat{Y} = 20 + 5(6) = 50
$$

If the observed response is 56, then:

$$
e = 56 - 50 = 6
$$

The model underpredicts the observed value by 6 units.

## 4.2 Python: Calculate Fitted Values and Residuals

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([42, 48, 55, 63, 70])

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)
residuals = y - predictions

print("Fitted values:", predictions)
print("Residuals:", residuals)
```

The residuals can help reveal whether a regression model captures the systematic pattern in the data. Detailed residual diagnostics belong in the Regression Model Evaluation chapter.

# 5. Least Squares Method

Several straight lines may describe the general pattern in a scatter plot. The **ordinary least squares (OLS)** method selects coefficients by minimising the sum of squared residuals.

The residual sum of squares is:

$$
SSE = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

The fitted coefficients are selected to minimise this quantity.

## 5.1 Why Are Residuals Squared?

Suppose two residuals are 5 and -5.

Adding them directly gives:

$$
5 + (-5) = 0
$$

This result hides the fact that both observations differ from their fitted values.

After squaring:

$$
5^2 + (-5)^2 = 50
$$

Squaring prevents positive and negative residuals from cancelling and penalises larger errors more heavily.

# 6. Calculating the Least-Squares Regression Line

For simple linear regression, the least-squares slope is:

$$
b_1 =
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

The intercept is:

$$
b_0 = \bar{y} - b_1\bar{x}
$$

Where:

- \(\bar{x}\) is the mean of the predictor.
- \(\bar{y}\) is the mean of the response.
- \(b_1\) is the estimated slope.
- \(b_0\) is the estimated intercept.

The final fitted equation is:

$$
\hat{Y} = b_0 + b_1 X
$$

The slope can also be expressed using sample covariance and sample variance:

$$
b_1 = \frac{s_{XY}}{s_X^2}
$$

## 6.1 Worked Example: Finding the Regression Equation

Consider the following data.

| \(X\) | \(Y\) |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 8 |

**Step 1: Calculate the means.**

$$
\bar{x} = \frac{1+2+3+4}{4} = 2.5
$$

$$
\bar{y} = \frac{2+4+5+8}{4} = 4.75
$$

**Step 2: Calculate the cross-products of deviations.**

$$
\sum (x_i-\bar{x})(y_i-\bar{y}) = 9.5
$$

**Step 3: Calculate the squared deviations of \(X\).**

$$
\sum (x_i-\bar{x})^2 = 5
$$

**Step 4: Calculate the slope.**

$$
b_1 = \frac{9.5}{5} = 1.9
$$

**Step 5: Calculate the intercept.**

$$
b_0 = 4.75 - (1.9)(2.5)
$$

$$
b_0 = 0
$$

Therefore, the fitted regression equation is:

$$
\hat{Y} = 1.9X
$$

**Step 6: Calculate a fitted value and residual.**

For \(X=3\):

$$
\hat{Y} = 1.9(3) = 5.7
$$

The observed value is \(Y=5\).

$$
e = 5 - 5.7 = -0.7
$$

The residual is -0.7, meaning the observed value is 0.7 units below the fitted value.

## 6.2 Python: Calculate the Regression Coefficients

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 8])

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("Regression equation:")
print(f"Y_hat = {model.intercept_:.2f} + "
      f"{model.coef_[0]:.2f}X")
```

The fitted line passes through the point \((\bar{x},\bar{y})\) when an intercept is included. For ordinary least squares with an intercept, the residuals also sum to zero, subject to numerical precision.

# 7. Regression and Correlation

Correlation and regression are mathematically related, but they serve different purposes.

For simple linear regression, the slope can be expressed in terms of Pearson correlation:

$$
b_1 = r\frac{s_Y}{s_X}
$$

Where \(r\) is the Pearson correlation coefficient, \(s_Y\) is the sample standard deviation of \(Y\), and \(s_X\) is the sample standard deviation of \(X\).

For example, suppose:

$$
r = 0.80,\quad s_X = 2,\quad s_Y = 10
$$

Then:

$$
b_1 = 0.80\frac{10}{2}
$$

$$
b_1 = 4
$$

Correlation is unitless, while the regression slope depends on the units of the variables.

| Feature | Correlation | Regression |
|---|---|---|
| Main purpose | Describe association | Model a response using predictors |
| Variable roles | Symmetric | Response and predictors have distinct roles |
| Output | Correlation coefficient | Equation and coefficients |
| Units | Unitless | Coefficients may have units |
| Prediction | Does not directly provide a fitted response equation | Provides fitted values and predictions |
| Causation | Does not establish causation | Does not automatically establish causation |

A strong correlation does not prove that one variable causes the other. Causal conclusions depend on study design and additional assumptions.

# 8. Multiple Linear Regression

Simple linear regression uses one predictor. **Multiple linear regression** uses two or more predictors to model a response.

The population model is:

$$
Y = \beta_0 + \beta_1X_1 + \beta_2X_2
+ \cdots + \beta_pX_p + \varepsilon
$$

The fitted equation is:

$$
\hat{Y} = b_0 + b_1X_1 + b_2X_2
+ \cdots + b_pX_p
$$

Here, \(p\) is the number of predictors.

For example, examination marks might be modelled using study hours, attendance, and assignment scores.

## 8.1 Interpreting Multiple Regression Coefficients

Suppose the fitted equation is:

$$
\hat{Y} = 20 + 3X_1 + 5X_2
$$

Where:

- \(X_1\) represents study hours.
- \(X_2\) represents an attendance measure.
- \(Y\) represents marks.

The coefficient of \(X_1\) is 3. Holding \(X_2\) constant, a one-unit increase in \(X_1\) is associated with a three-unit increase in predicted marks.

The coefficient of \(X_2\) is 5. Holding \(X_1\) constant, a one-unit increase in \(X_2\) is associated with a five-unit increase in predicted marks.

The phrase **holding the other included predictors constant** is essential when interpreting multiple regression coefficients.

## 8.2 Worked Multiple Regression Prediction

Suppose:

$$
\hat{Y} = 20 + 3X_1 + 5X_2
$$

For \(X_1=5\) and \(X_2=4\):

$$
\hat{Y} = 20 + 3(5) + 5(4)
$$

$$
\hat{Y} = 20 + 15 + 20
$$

$$
\hat{Y} = 55
$$

The predicted response is 55.

## 8.3 Python: Multiple Linear Regression

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6],
    "attendance": [60, 65, 70, 75, 80, 85],
    "marks": [42, 48, 55, 63, 70, 76]
})

X = df[["study_hours", "attendance"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

new_student = pd.DataFrame({
    "study_hours": [4],
    "attendance": [75]
})

print("Prediction:", model.predict(new_student)[0])
```

Each coefficient corresponds to the predictor in the same order as the columns in `X`.

# 9. Categorical Predictors

Regression can include categorical predictors, such as study mode, department, or product category. These variables are commonly represented using **indicator variables**, also called dummy variables.

Suppose study mode has two categories:

- Online: \(D=0\)
- Offline: \(D=1\)

A model containing study hours and study mode can be written as:

$$
\hat{Y} = b_0 + b_1X + b_2D
$$

Here, \(b_2\) represents the estimated difference between offline and online groups at the same value of \(X\), assuming the model contains no interaction between study mode and study hours.

## 9.1 Interpreting an Indicator Variable

Suppose:

$$
\hat{Y} = 40 + 5X + 8D
$$

For online students, \(D=0\):

$$
\hat{Y} = 40 + 5X
$$

For offline students, \(D=1\):

$$
\hat{Y} = 48 + 5X
$$

At the same value of \(X\), the model predicts a response eight units higher for the offline group.

For a categorical variable with \(k\) categories, a common approach uses \(k-1\) indicator variables when the model includes an intercept. The omitted category becomes the **reference category**.

## 9.2 Python: Encode Categorical Predictors

```python
import pandas as pd

df = pd.DataFrame({
    "study_hours": [2, 3, 4, 5],
    "study_mode": ["Online", "Offline", "Online", "Offline"],
    "marks": [45, 52, 58, 67]
})

df_encoded = pd.get_dummies(
    df,
    columns=["study_mode"],
    drop_first=True,
    dtype=int
)

print(df_encoded)
```

The omitted category is used as the reference category. Interpret the resulting coefficients according to the category coding and the fitted model.

# 10. Interaction Terms

An interaction occurs when the relationship between one predictor and the response depends on another predictor.

A model containing two predictors and their interaction is:

$$
\hat{Y} = b_0 + b_1X_1 + b_2X_2 + b_3X_1X_2
$$

The product \(X_1X_2\) is the interaction term.

For example, the relationship between study hours and marks may differ between two study modes.

Suppose \(D=0\) represents Group A and \(D=1\) represents Group B:

$$
\hat{Y} = 20 + 4X + 3D + 2XD
$$

For Group A, \(D=0\):

$$
\hat{Y} = 20 + 4X
$$

For Group B, \(D=1\):

$$
\hat{Y} = 23 + 6X
$$

The slope is 4 for Group A and 6 for Group B. The interaction allows the fitted slope to differ between the groups.

## 10.1 Python: Create an Interaction Term

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6],
    "offline": [0, 1, 0, 1, 0, 1],
    "marks": [40, 48, 50, 61, 60, 72]
})

df["interaction"] = (
    df["study_hours"] * df["offline"]
)

X = df[["study_hours", "offline", "interaction"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
```

The interaction coefficient describes how the slope associated with study hours changes for the group coded as 1 relative to the reference group.

# 11. Polynomial Regression

A straight-line relationship may not adequately represent data that curve. Polynomial regression introduces powers of predictors to represent curvature.

A quadratic regression model is:

$$
\hat{Y} = b_0 + b_1X + b_2X^2
$$

The squared term allows the fitted relationship to curve. Higher-degree models can include terms such as \(X^3\), although more complex polynomials can overfit the data.

Polynomial regression is nonlinear in the original predictor \(X\), but it is linear in the coefficients \(b_0\), \(b_1\), and \(b_2\).

## 11.1 Python: Polynomial Regression

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 6, 11, 18, 27, 38])

model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

model.fit(X, y)

print("Predictions:", model.predict(X))
```

The pipeline first generates polynomial features and then fits a linear regression model. For predictive work, model complexity should be assessed using appropriate validation methods in the Regression Model Evaluation chapter.

# 12. Transformations

Transformations change the representation of variables to help model a relationship or satisfy modelling requirements.

Common transformations include:

$$
\log(X),\qquad \sqrt{X},\qquad X^2
$$

For example, a model using the logarithm of a predictor can be written as:

$$
\hat{Y} = b_0 + b_1\log(X)
$$

The interpretation of \(b_1\) depends on the transformation used. A logarithm also requires values in its domain; the natural logarithm is defined for positive \(X\).

Transformations should be selected for a statistical or substantive reason, not simply to obtain a preferred numerical result.

# 13. Interpolation and Extrapolation

Regression predictions should be interpreted in relation to the range of the observed predictor values.

**Interpolation** means predicting within the observed range. If the available study-hour values range from 1 to 6, predicting at 4 hours is interpolation.

**Extrapolation** means predicting outside the observed range. Using the same data to predict at 20 hours is extrapolation.

Extrapolation can be unreliable because the relationship observed in the available data may not continue beyond that range.

# 14. Regression Through the Origin

A regression model without an intercept is written as:

$$
\hat{Y} = b_1X
$$

This forces the fitted line through \((0,0)\).

Such a model should only be used when there is a strong substantive or theoretical reason for the response to be zero when the predictor is zero. Removing the intercept merely to obtain a particular coefficient or result is generally inappropriate.

# 15. Matrix Form of Linear Regression

Multiple linear regression can be represented compactly using matrix notation:

$$
\mathbf{y} = \mathbf{X}\boldsymbol{\beta}
+ \boldsymbol{\varepsilon}
$$

Where:

- \(\mathbf{y}\) is the response vector.
- \(\mathbf{X}\) is the design matrix.
- \(\boldsymbol{\beta}\) is the coefficient vector.
- \(\boldsymbol{\varepsilon}\) is the error vector.

The fitted response vector is:

$$
\hat{\mathbf{y}} = \mathbf{X}\mathbf{b}
$$

When the design matrix has full column rank, the ordinary least-squares coefficient estimator can be written as:

$$
\mathbf{b} =
(\mathbf{X}^{T}\mathbf{X})^{-1}
\mathbf{X}^{T}\mathbf{y}
$$

The design matrix includes one row per observation and one column per model term. When an intercept is included, the first column contains ones.

This matrix representation is the mathematical foundation of many linear regression implementations.

# 16. Basic Regression Assumptions

Regression assumptions depend on the model and the intended analysis. Common considerations for ordinary least-squares regression include the following.

## 16.1 Linearity

The systematic relationship should be appropriately represented by the specified model.

For simple linear regression:

$$
E(Y\mid X) = \beta_0 + \beta_1X
$$

A strongly curved relationship may require transformations, polynomial terms, or another model form.

## 16.2 Independence of Errors

The error terms should generally be independent for standard classical inference.

This assumption may be problematic in time-series data, repeated measurements, or observations clustered within groups.

## 16.3 Constant Error Variance

Homoscedasticity means the conditional variance of the errors is approximately constant.

$$
\mathrm{Var}(\varepsilon\mid X) = \sigma^2
$$

If the spread of residuals changes systematically across predictor values, the data may exhibit heteroscedasticity. This can affect conventional standard errors and inference.

## 16.4 Normality of Errors

Normally distributed errors can be important for exact small-sample classical inference. Normality is not generally required to calculate the ordinary least-squares coefficients.

The assumption concerns the conditional error distribution, not a requirement that every predictor or the raw response be normally distributed.

## 16.5 Appropriate Data Structure

The observations should be collected and organised in a way that supports the intended analysis. Dependence, sampling bias, measurement error, and missing data can affect the validity of regression conclusions.

# 17. Multicollinearity

In multiple regression, multicollinearity occurs when predictors are strongly related to one another.

For example, including height in centimetres and the same height in metres as separate predictors creates redundant information.

Multicollinearity can make individual coefficient estimates unstable and difficult to interpret. It does not automatically mean that the model cannot predict well, but it can make the contribution of individual predictors difficult to separate.

# 18. Missing Data and Causal Interpretation

Regression requires a clearly defined analytical dataset. Missing observations should not be removed automatically without considering why the values are missing and how the removal might affect the analysis.

The appropriate approach depends on the missing-data mechanism, the variables involved, and the purpose of the analysis.

Likewise, adding predictors to a regression model does not automatically establish causality or eliminate confounding. Causal interpretation requires appropriate study design and additional assumptions.

Ordinary linear regression is designed for a quantitative response. For a binary response, such as an outcome coded 0 or 1, logistic regression is often more appropriate and is outside the scope of this chapter.

# 19. A Complete Regression Example

Consider the following data describing study hours and examination marks.

| Study Hours (\(X\)) | Marks (\(Y\)) |
|---:|---:|
| 1 | 42 |
| 2 | 48 |
| 3 | 55 |
| 4 | 63 |
| 5 | 70 |

The objective is to describe the fitted relationship between study hours and marks.

**Step 1: Calculate the means.**

$$
\bar{x} = \frac{1+2+3+4+5}{5} = 3
$$

$$
\bar{y} = \frac{42+48+55+63+70}{5} = 55.6
$$

**Step 2: Calculate the sum of cross-products.**

$$
\sum (x_i-\bar{x})(y_i-\bar{y}) = 70
$$

**Step 3: Calculate the sum of squared predictor deviations.**

$$
\sum (x_i-\bar{x})^2 = 10
$$

**Step 4: Calculate the slope.**

$$
b_1 = \frac{70}{10} = 7
$$

**Step 5: Calculate the intercept.**

$$
b_0 = 55.6 - 7(3)
$$

$$
b_0 = 34.6
$$

The fitted regression equation is:

$$
\hat{Y} = 34.6 + 7X
$$

**Step 6: Predict marks for four study hours.**

$$
\hat{Y} = 34.6 + 7(4)
$$

$$
\hat{Y} = 62.6
$$

The model predicts approximately 62.6 marks.

The observed mark for four study hours is 63, so the residual is:

$$
e = 63 - 62.6 = 0.4
$$

The model underpredicts this observation by 0.4 marks.

## 19.1 Python: Fit and Predict

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([42, 48, 55, 63, 70])

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

prediction = model.predict([[4]])
print("Predicted marks:", prediction[0])

fitted_values = model.predict(X)
residuals = y - fitted_values

print("Fitted values:", fitted_values)
print("Residuals:", residuals)
```

# 20. Common Regression Mistakes

**Confusing slope with correlation.** The slope has units, while correlation is unitless.

**Interpreting the intercept without context.** A value at \(X=0\) may not be meaningful if zero is outside the relevant data range.

**Treating predictions as guarantees.** Fitted values are estimates and may differ from observed outcomes.

**Extrapolating too far.** A relationship observed within a particular range may not continue outside it.

**Claiming that regression proves causation.** Regression describes a modelled relationship; causal conclusions require additional evidence and assumptions.

**Ignoring the roles of predictors.** Multiple-regression coefficients must be interpreted while holding the other included predictors constant.

**Ignoring multicollinearity.** Strongly related predictors can make individual coefficients unstable.

**Assuming predictors must be normally distributed.** Classical regression assumptions primarily concern the error structure and model specification, not normality of every predictor.

**Removing the intercept without justification.** A no-intercept model imposes a meaningful restriction on the fitted line.

# 21. Points to Remember

1. Regression models a response using one or more predictors.
2. Simple linear regression uses one predictor.
3. Multiple linear regression uses two or more predictors.
4. The slope describes the change in predicted response for a one-unit increase in a predictor.
5. The intercept is the predicted response when the predictor equals zero.
6. Least squares minimises the sum of squared residuals.
7. A residual equals the observed value minus the fitted value.
8. The least-squares line with an intercept passes through \((\bar{x},\bar{y})\).
9. With an intercept, the residuals sum to zero, subject to numerical precision.
10. Multiple-regression coefficients are interpreted while holding other included predictors constant.
11. Indicator variables represent categorical predictors.
12. Interaction terms allow relationships to differ across predictor values or groups.
13. Polynomial regression can represent curvature.
14. Interpolation is prediction within the observed range.
15. Extrapolation is prediction outside the observed range and may be unreliable.
16. Regression does not automatically establish causation.
17. Regression coefficients have units; correlation does not.
18. Detailed model evaluation belongs in `11_Regression_Model_Evaluation`.

# 22. Important Formula Summary

### Simple linear regression model

$$
Y = \beta_0 + \beta_1X + \varepsilon
$$

### Fitted regression equation

$$
\hat{Y} = b_0 + b_1X
$$

### Residual

$$
e_i = y_i - \hat{y}_i
$$

### Sum of squared residuals

$$
SSE = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Least-squares slope

$$
b_1 =
\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}
{\sum(x_i-\bar{x})^2}
$$

### Least-squares intercept

$$
b_0 = \bar{y} - b_1\bar{x}
$$

### Slope using covariance and variance

$$
b_1 = \frac{s_{XY}}{s_X^2}
$$

### Slope using correlation

$$
b_1 = r\frac{s_Y}{s_X}
$$

### Multiple linear regression

$$
\hat{Y} = b_0 + b_1X_1 + \cdots + b_pX_p
$$

### Interaction model

$$
\hat{Y} = b_0 + b_1X_1 + b_2X_2 + b_3X_1X_2
$$

### Quadratic regression

$$
\hat{Y} = b_0 + b_1X + b_2X^2
$$

### Matrix form

$$
\mathbf{y} = \mathbf{X}\boldsymbol{\beta}
+ \boldsymbol{\varepsilon}
$$

### Ordinary least-squares estimator

$$
\mathbf{b} =
(\mathbf{X}^{T}\mathbf{X})^{-1}
\mathbf{X}^{T}\mathbf{y}
$$

This estimator requires the design matrix to have full column rank.

# 23. Quick Concept Comparison

| Concept | Main purpose |
|---|---|
| Correlation | Describe the strength and direction of association |
| Regression | Model a response using predictor variables |
| Intercept | Predicted response at predictor value zero |
| Slope | Change in predicted response per predictor unit |
| Residual | Observed value minus fitted value |
| Least squares | Estimate coefficients by minimising squared residuals |
| Simple regression | Model with one predictor |
| Multiple regression | Model with two or more predictors |
| Indicator variable | Numerically represent a category |
| Interaction | Allow one predictor's relationship to depend on another |
| Polynomial regression | Represent curvature using predictor powers |
| Interpolation | Predict within the observed range |
| Extrapolation | Predict outside the observed range |

# 24. Chapter Summary

Regression provides a mathematical framework for describing how a response changes with one or more predictors. Simple linear regression uses a straight-line equation, while multiple regression incorporates several predictors.

Ordinary least squares estimates coefficients by minimising the sum of squared residuals. The resulting equation can be used to calculate fitted values and make predictions. Regression can also incorporate categorical predictors, interaction terms, and polynomial terms.

The central idea is:

$$
\text{Regression} =
\text{Model the response using predictor information}
$$

Regression is a fundamental tool in Data Science and Machine Learning, but its conclusions depend on the quality of the data, the model specification, and the assumptions supporting the intended analysis.

# 25. References and Further Reading

- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [Penn State — STAT Online](https://online.stat.psu.edu/)
- [NIST/SEMATECH — e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [scikit-learn — Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [GeeksforGeeks — Linear Regression](https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)

# 26. Related Topics

- `09_Correlation` — Correlation and association between variables.
- `11_Regression_Model_Evaluation` — Regression metrics, residual evaluation, model comparison, and validation.
- `12_Linear_Algebra` — Vectors, matrices, and matrix operations used in regression.
- `13_Calculus` — Derivatives and optimisation foundations.
- `14_Bias_and_Variance` — Underfitting, overfitting, and the bias–variance trade-off.
- `15_Statistics_for_Machine_Learning` — Statistical concepts used in Machine Learning.
