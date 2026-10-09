# Statistics for Machine Learning

Statistics provides the mathematical language used to understand data, uncertainty, estimation, relationships between variables, and model performance.

The earlier chapters in this Mathematics & Statistics section developed individual statistical ideas in detail. This final chapter brings the most useful ideas together in a **machine-learning context**.

The purpose here is not to repeat complete chapters on probability, descriptive statistics, hypothesis testing, correlation, regression, or bias and variance. Instead, this chapter focuses on how those ideas are used together when preparing data, building models, evaluating predictions, and interpreting results.

The central workflow is:

$\boxed{ \text{Data} \rightarrow \text{Explore} \rightarrow \text{Prepare} \rightarrow \text{Model} \rightarrow \text{Evaluate} \rightarrow \text{Interpret} }$

Throughout this chapter, statistical concepts are connected to practical machine-learning decisions.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain why statistics is important in machine learning.
2. Distinguish descriptive, inferential, and predictive uses of statistics.
3. Identify variables, observations, features, and targets.
4. Understand the effect of measurement scale on modelling choices.
5. Use summary statistics appropriately during data exploration.
6. Interpret distributions and identify unusual observations.
7. Understand the importance of representative samples.
8. Explain sampling bias and selection bias.
9. Understand train, validation, and test sets.
10. Explain data leakage statistically.
11. Understand population shift and sampling differences.
12. Use standardisation and z-scores correctly.
13. Distinguish standardisation from normalisation.
14. Understand skewness and transformations.
15. Understand covariance and correlation in feature analysis.
16. Interpret a covariance matrix and correlation matrix.
17. Understand multicollinearity.
18. Explain statistical dependence between variables.
19. Understand conditional relationships.
20. Interpret regression coefficients statistically.
21. Distinguish association from causation.
22. Understand confidence intervals and uncertainty in estimates.
23. Interpret prediction intervals conceptually.
24. Understand statistical hypothesis testing as a supporting tool.
25. Interpret p-values carefully.
26. Understand effect size and practical significance.
27. Recognise multiple-comparison problems.
28. Understand class imbalance and conditional probabilities.
29. Understand calibration and predicted probabilities.
30. Choose appropriate evaluation metrics based on the problem.
31. Interpret residuals statistically.
32. Understand bias–variance considerations in model development.
33. Use resampling and cross-validation.
34. Understand bootstrap-based uncertainty.
35. Apply statistical thinking to a complete machine-learning workflow.

---

# 2. Why Statistics Matters in Machine Learning

Machine learning models learn patterns from data.

Statistics helps us answer questions such as:

- What does the data look like?
- How variable are the observations?
- Are the observed patterns likely to be meaningful?
- How representative is the sample?
- How uncertain is an estimate?
- Are two variables associated?
- How reliable is a prediction?
- Does a model generalise beyond the training sample?
- Is a difference practically important?
- Could an apparent pattern be caused by sampling variation?

Machine learning therefore uses statistical ideas at many stages, even when the final model is not itself a statistical model.

---

# 3. Three Uses of Statistics

Statistics can be viewed through three broad purposes.

## Descriptive statistics

Descriptive statistics summarise observed data.

Examples:

- mean,
- median,
- standard deviation,
- quartiles,
- frequency tables,
- histograms.

## Inferential statistics

Inferential statistics use a sample to learn about a broader population.

Examples:

- confidence intervals,
- hypothesis tests,
- sampling distributions,
- estimation.

## Predictive modelling

Predictive modelling uses observed data to predict outcomes for new observations.

Examples:

- regression,
- classification,
- probability prediction.

These purposes overlap, but they answer different questions.

---

# 4. Observations, Features, and Target

Suppose a dataset contains information about houses.

Each row represents one observation.

Columns might include:

- area,
- number of bedrooms,
- age,
- location,
- price.

The input variables are called **features**.

The variable we want to predict is the **target**.

For a regression problem:

$X= \text{features}$

and:

$Y= \text{target}$

The model learns a relationship such as:

$\hat{Y}=f(X)$

---

# 5. Statistical View of a Dataset

A dataset can be represented as:

$D= \{(x_i,y_i)\}_{i=1}^{n}$

where:

- $n$ is the number of observations,
- $x_i$ is the feature vector for observation $i$,
- $y_i$ is its target value.

For example:

$x_i= \begin{bmatrix} x_{i1}\\ x_{i2}\\ \vdots\\ x_{ip} \end{bmatrix}$

where $p$ is the number of features.

The statistical question is not only how well a model fits $D$, but how well it performs on observations generated from the same or a suitably related population.

---

# 6. Population and Sample in Machine Learning

A machine-learning dataset is often a sample from a larger population of possible observations.

For example:

- Population: all future customers.
- Sample: customers present in the historical dataset.

The distinction matters because a model is normally intended to work beyond the exact observations used during training.

Therefore:

$\boxed{ \text{Training data is not necessarily the complete population.} }$

---

# 7. Representative Sampling

A sample should reflect the population relevant to the modelling task.

Suppose a model is intended to predict customer behaviour across an entire country, but the training data comes almost entirely from one city.

The model may learn patterns that are specific to that city.

This is a sampling problem.

A useful question is:

> Does the training sample represent the population on which the model will be used?

---

# 8. Sampling Bias

Sampling bias occurs when the process used to obtain observations systematically favours some members of the population over others.

Examples include:

- voluntary-response samples,
- convenience samples,
- missing groups,
- restricted geographic coverage,
- historical selection rules.

Sampling bias can cause the observed distribution to differ from the target population distribution.

More data from the same biased sampling process does not necessarily solve the problem.

---

# 9. Selection Bias

Selection bias occurs when inclusion in the dataset depends on characteristics related to the outcome or variables of interest.

For example, if a healthcare dataset contains only patients who visited a hospital, it may not represent the entire population.

A model trained on selected observations may perform poorly when applied to a broader population.

---

# 10. Measurement Bias

Bias can also arise from how variables are measured.

Examples:

- faulty sensors,
- inconsistent survey questions,
- incorrect labels,
- changes in measurement systems,
- systematic recording errors.

If the measurement process changes, the statistical relationship learned by the model may change as well.

---

# 11. Data Quality and Statistical Analysis

Before modelling, inspect:

- missing values,
- duplicates,
- impossible values,
- inconsistent units,
- unusual categories,
- measurement errors,
- outliers,
- target-label errors.

A statistical summary of incorrect data can still be mathematically correct but practically misleading.

Therefore:

$\boxed{ \text{Good modelling begins with trustworthy measurements.} }$

---

# 12. Measurement Scales

Variables can have different measurement structures.

Common categories are:

| Scale | Meaning | Example |
|---|---|---|
| Nominal | Categories without numerical order | City |
| Ordinal | Ordered categories | Satisfaction level |
| Interval | Equal differences, no meaningful zero | Temperature in °C |
| Ratio | Equal differences and meaningful zero | Income, height |

The measurement scale affects:

- summaries,
- visualisations,
- transformations,
- statistical tests,
- feature encoding.

---

# 13. Descriptive Statistics for Model Development

Descriptive statistics help answer:

- What is the centre of the feature?
- How variable is it?
- Is it strongly skewed?
- Are there unusual observations?
- Are feature scales very different?
- Are some categories rare?

Useful summaries include:

$\text{Mean}$

$\text{Median}$

$\text{Standard deviation}$

$\text{Quartiles}$

and:

$\text{Minimum and maximum}$

The correct summary depends on the distribution and measurement scale.

---

# 14. Mean and Median in Feature Analysis

The mean is sensitive to extreme observations.

The median is more resistant to extreme values.

Suppose annual income contains a small number of extremely high values.

The mean may be substantially larger than the median.

Therefore, comparing:

$\boxed{ \text{Mean versus median} }$

can provide useful information about skewness and unusual observations.

---

# 15. Variability

Two features can have the same mean but very different variability.

For example:

Dataset A:

$10,\ 10,\ 10,\ 10,\ 10$

Dataset B:

$2,\ 6,\ 10,\ 14,\ 18$

Both have mean:

$10$

but Dataset B has much greater spread.

Standard deviation and variance quantify this variability.

---

# 16. Standardisation

A common transformation is the z-score:

$\boxed{ z= \frac{x-\mu}{\sigma} }$

When population quantities are not known and sample statistics are used:

$\boxed{ z= \frac{x-\bar{x}}{s} }$

Standardisation centres a variable around zero and expresses values in standard-deviation units.

---

# 17. Worked Standardisation Example

Suppose:

$x=80$

with:

$\mu=70$

and:

$\sigma=5$

Then:

$z= \frac{80-70}{5}$

$=\frac{10}{5}$

$=2$

Therefore:

$\boxed{z=2}$

The observation is 2 standard deviations above the mean.

---

# 18. Why Standardisation Can Matter

Suppose one feature is measured in rupees and another in years.

Their numerical scales may be very different.

Standardisation gives each feature a common scale:

$\text{mean}\approx0$

and:

$\text{standard deviation}\approx1$

This can be particularly useful for methods whose calculations depend on distances, dot products, or coefficient magnitudes.

Standardisation does not make a dataset normally distributed.

---

# 19. Standardisation vs Normalisation

These terms are sometimes used inconsistently, so the exact transformation should always be stated.

A common min–max transformation is:

$\boxed{ x'= \frac{x-x_{\min}} {x_{\max}-x_{\min}} }$

This maps values to the interval:

$[0,1]$

when the minimum and maximum are finite and fixed.

Standardisation instead uses the mean and standard deviation.

Therefore:

$\boxed{ \text{Standardisation}\ne\text{Min-max scaling} }$

---

# 20. Skewness and Transformations

A feature may have a long right tail.

Examples often include:

- income,
- transaction amount,
- counts,
- file sizes.

A common transformation is:

$x'=\log(x)$

for positive $x$.

This can compress large values and sometimes make a strongly right-skewed distribution more manageable.

For nonnegative counts, another option is:

$x'=\log(1+x)$

The transformation should be chosen based on the data and modelling objective, not applied automatically.

---

# 21. Outliers

An outlier is an observation that is unusually far from the general pattern of the data.

Outliers can result from:

- measurement errors,
- data-entry mistakes,
- rare but genuine observations,
- unusual circumstances.

Do not automatically remove every outlier.

First ask:

1. Is the observation valid?
2. Is it relevant to the target population?
3. Does it represent a real but rare event?
4. Is it caused by measurement or recording error?

---

# 22. Missing Data

Missing values can occur for many reasons.

Examples:

- a measurement was not taken,
- a question was skipped,
- a sensor failed,
- information was unavailable.

The mechanism causing missingness can matter statistically.

Three common theoretical categories are:

- MCAR: Missing Completely At Random
- MAR: Missing At Random conditional on observed information
- MNAR: Missing Not At Random

These assumptions influence how missing values should be handled.

---

# 23. Missing-Value Imputation

Common approaches include:

- mean imputation,
- median imputation,
- mode imputation,
- constant-value imputation,
- model-based imputation.

For a skewed numeric feature, median imputation may be more robust than mean imputation.

However, imputation should be performed using information available from the training data only.

---

# 24. Data Leakage Through Preprocessing

Suppose we calculate the mean and standard deviation using the entire dataset before splitting into training and test sets.

The test-set information has influenced the preprocessing parameters.

This creates leakage.

The correct principle is:

$\boxed{ \text{Fit preprocessing on training data only.} }$

Then apply the learned transformation to validation and test data.

---

# 25. Train, Validation, and Test Sets

A dataset may be divided into:

### Training set

Used to fit model parameters.

### Validation set

Used for model selection and hyperparameter decisions.

### Test set

Used for final evaluation.

The key principle is that the test set should remain isolated from decisions that influence the final model.

---

# 26. Why a Test Set Is Needed

Suppose we compare 20 models and choose the model with the lowest test error.

The test set has now influenced model selection.

It is no longer a clean final evaluation set.

Repeatedly using the test set for decisions can lead to optimistic performance estimates.

Therefore:

$\boxed{ \text{Do not repeatedly tune the model against the final test set.} }$

---

# 27. Cross-Validation

Cross-validation repeatedly divides the training data into training and validation portions.

In $k$-fold cross-validation:

1. Split data into $k$ folds.
2. Train on $k-1$ folds.
3. Validate on the remaining fold.
4. Repeat until every fold has been used as validation.
5. Average the validation performance.

If the fold errors are:

$E_1,E_2,\ldots,E_k$

then the mean cross-validation error is:

$\boxed{ CV\ Error = \frac{1}{k} \sum_{j=1}^{k}E_j }$

---

# 28. Statistical Reason for Cross-Validation

A single train-validation split can produce a noisy estimate of generalisation performance.

Cross-validation uses several splits.

This gives a broader view of how the model behaves across different subsets of the available training data.

The resulting estimate is still not a guarantee of future performance.

---

# 29. Stratified Sampling in Classification

Suppose a classification dataset contains:

$95\%$

class 0 and:

$5\%$

class 1.

A random split can accidentally produce a validation set with a different class proportion.

Stratified splitting attempts to preserve class proportions across splits.

This is especially useful when classes are imbalanced.

---

# 30. Class Imbalance

Suppose:

$P(Y=1)=0.01$

and:

$P(Y=0)=0.99$

A model that always predicts class 0 achieves:

$99\%$

accuracy.

Yet it completely fails to identify the minority class.

Therefore:

$\boxed{ \text{Accuracy alone can be misleading for imbalanced classification.} }$

---

# 31. Confusion Matrix

For binary classification, the confusion matrix contains:

- True Positive (TP)
- False Positive (FP)
- True Negative (TN)
- False Negative (FN)

These counts form the basis of several evaluation metrics.

---

# 32. Classification Metrics

### Accuracy

$\boxed{ Accuracy= \frac{TP+TN} {TP+TN+FP+FN} }$

### Precision

$\boxed{ Precision= \frac{TP}{TP+FP} }$

### Recall

$\boxed{ Recall= \frac{TP}{TP+FN} }$

### F1 score

$\boxed{ F_1= 2 \frac{Precision\cdot Recall} {Precision+Recall} }$

The appropriate metric depends on the cost of different types of errors.

---

# 33. Precision and Recall Interpretation

High precision means that among predicted positives, many are actually positive.

High recall means that among actual positives, many are successfully identified.

For example, in a screening problem:

- missing a true positive may be very costly,
- so recall may be especially important.

In another application, false alarms may be more costly, making precision more important.

Metrics should therefore reflect the decision problem.

---

# 34. Conditional Probability in Classification

Classification probabilities can be written as:

$P(Y=c\mid X=x)$

This is the probability of class $c$ given the observed features.

For binary classification:

$P(Y=1\mid X=x)$

and:

$P(Y=0\mid X=x)$

satisfy:

$P(Y=1\mid X=x)+P(Y=0\mid X=x)=1$

when these are the only two classes.

---

# 35. Predicted Probabilities and Thresholds

A classifier may output:

$\hat{p}=P(Y=1\mid X=x)$

A common decision rule is:

$\hat{Y}= \begin{cases} 1,&\hat{p}\ge0.5\\ 0,&\hat{p}<0.5 \end{cases}$

But 0.5 is not universally optimal.

The threshold should depend on:

- class prevalence,
- error costs,
- business requirements,
- desired precision,
- desired recall.

---

# 36. Calibration

A classifier is well calibrated when predicted probabilities correspond reasonably well to observed frequencies.

For example, among observations assigned predicted probability near:

$0.8$

approximately 80% should belong to the positive class if the model is well calibrated in that region.

Calibration is different from discrimination.

A model can rank observations well but produce poorly calibrated probabilities.

---

# 37. Covariance

For two variables $X$ and $Y$, sample covariance is:

$\boxed{ s_{XY} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i-\bar{x})(y_i-\bar{y}) }$

Covariance indicates whether the variables tend to move together.

Positive covariance suggests that larger values of one variable tend to occur with larger values of the other.

Negative covariance suggests an opposite tendency.

The magnitude depends on the measurement scales.

---

# 38. Correlation

Pearson correlation standardises covariance:

$\boxed{ r= \frac{s_{XY}} {s_Xs_Y} }$

where:

- $s_X$ is the sample standard deviation of $X$,
- $s_Y$ is the sample standard deviation of $Y$.

The correlation lies between:

$-1\le r\le1$

A value near 1 indicates strong positive linear association.

A value near -1 indicates strong negative linear association.

A value near 0 indicates weak linear association, but does not prove independence.

---

# 39. Correlation Does Not Imply Causation

Suppose two variables are correlated.

This does not establish:

$X\rightarrow Y$

as a causal relationship.

Possible explanations include:

- reverse causation,
- confounding variables,
- selection effects,
- common external causes,
- coincidence.

Therefore:

$\boxed{ \text{Association is not automatically causation.} }$

---

# 40. Correlation Matrix

For several numerical features, correlations can be arranged into a matrix:

$R= \begin{bmatrix} 1&r_{12}&\cdots&r_{1p}\\ r_{21}&1&\cdots&r_{2p}\\ \vdots&\vdots&\ddots&\vdots\\ r_{p1}&r_{p2}&\cdots&1 \end{bmatrix}$

The diagonal entries are:

$r_{ii}=1$

because each variable is perfectly correlated with itself.

---

# 41. Multicollinearity

Multicollinearity occurs when predictors contain substantial overlapping information.

For example:

- house area,
- number of rooms,
- built-up area

may be strongly related.

In linear regression, multicollinearity can make coefficient estimates unstable and difficult to interpret.

A model may still predict reasonably well even when individual coefficients are unstable.

---

# 42. Variance Inflation Factor

A common diagnostic for linear-model multicollinearity is the Variance Inflation Factor:

$\boxed{ VIF_j= \frac{1}{1-R_j^2} }$

where $R_j^2$ is obtained by regressing predictor $X_j$ on the other predictors.

A large VIF indicates that $X_j$ is strongly explained by the other predictors.

There is no single universal cutoff that should be treated as a law. Context matters.

---

# 43. Conditional Relationships

A relationship observed between two variables can change after conditioning on another variable.

Symbolically:

$P(Y\mid X)$

may differ from:

$P(Y\mid X,Z)$

Similarly, correlation between $X$ and $Y$ can change after controlling for $Z$.

This is why multivariable analysis can reveal relationships that are hidden or distorted in simple pairwise analysis.

---

# 44. Simpson's Paradox

Simpson's paradox occurs when an association observed in aggregated data reverses or changes substantially after the data are divided into relevant groups.

For example, an overall treatment comparison might favour one treatment, while every important subgroup favours the other.

This demonstrates that:

$\boxed{ \text{Aggregated relationships can differ from conditional relationships.} }$

The correct interpretation depends on the data-generating context.

---

# 45. Regression Coefficients as Statistical Quantities

In a linear model:

$Y= \beta_0+ \beta_1X_1+ \cdots+ \beta_pX_p+ \varepsilon$

the coefficients describe the model's conditional mean relationship under the model assumptions.

For a one-predictor model:

$Y=\beta_0+\beta_1X+\varepsilon$

$\beta_1$ represents the expected change in the conditional mean of $Y$ for a one-unit increase in $X$ under the model.

This is a statistical interpretation, not automatically a causal interpretation.

---

# 46. Confidence Intervals for Model Parameters

An estimated coefficient:

$\hat{\beta}$

is not usually treated as perfectly known.

A confidence interval can quantify uncertainty around the parameter estimate under the assumptions of the chosen inferential procedure.

A general large-sample form is:

$\boxed{ \hat{\beta} \pm (\text{critical value}) \times SE(\hat{\beta}) }$

The exact critical value and standard error depend on the model and inferential framework.

---

# 47. Confidence Interval Interpretation

A 95% confidence interval should not be interpreted as:

> There is a 95% probability that the fixed parameter is inside this particular interval.

Under the frequentist interpretation, the procedure is designed so that across repeated samples, approximately 95% of intervals constructed by that procedure contain the true parameter when assumptions hold.

The exact interpretation therefore concerns the procedure, not a probability assigned to the fixed parameter after the interval is observed.

---

# 48. Prediction Interval

A confidence interval for a mean response and a prediction interval for a new observation are different.

A prediction interval must account for:

- uncertainty in the estimated mean,
- random variation of a new observation.

Therefore, prediction intervals are generally wider than confidence intervals for the mean response at the same input.

---

# 49. Hypothesis Testing as a Supporting Tool

Hypothesis tests can be useful when investigating whether an observed relationship is compatible with a specified null hypothesis.

A typical structure is:

$H_0: \text{specified null relationship}$

versus:

$H_1: \text{alternative relationship}$

The test produces a statistic and, under the chosen framework, a p-value.

Hypothesis testing should support scientific or modelling reasoning rather than replace it.

---

# 50. P-Value

A p-value is the probability, under the null model, of observing a test statistic at least as incompatible with the null as the observed result, according to the test's definition.

It is **not**:

$P(H_0\mid Data)$

and it is not the probability that the observed result occurred "by chance" in an unrestricted sense.

---

# 51. Statistical Significance vs Practical Significance

With a very large sample, a tiny effect can produce a very small p-value.

For example, a difference of:

$0.1$

could be statistically significant in a huge dataset.

But the effect may have little practical importance.

Therefore, consider:

- effect size,
- uncertainty,
- practical impact,
- sample size,
- domain context.

---

# 52. Effect Size

An effect size describes the magnitude of a difference or relationship.

For example, a standardised mean difference can be written as:

$d= \frac{\bar{x}_1-\bar{x}_2}{s_p}$

where $s_p$ is an appropriate pooled standard deviation under the chosen definition.

Effect sizes help distinguish:

$\boxed{ \text{Is there evidence of a difference?} }$

from:

$\boxed{ \text{How large is the difference?} }$

---

# 53. Multiple Comparisons

Suppose we perform many statistical tests.

Even if every null hypothesis is true, some p-values may be small simply due to repeated testing.

If $m$ independent tests are each performed at significance level $\alpha$, the probability of at least one false positive is:

$1-(1-\alpha)^m$

For example, with:

$\alpha=0.05$

and:

$m=20$

we obtain:

$1-(0.95)^{20} \approx0.642$

Thus:

$\boxed{ \text{The probability of at least one false positive can become large.} }$

Multiple-testing procedures can be used when appropriate.

---

# 54. Resampling

Resampling methods repeatedly create samples from observed data or partition data into different subsets.

Important examples include:

- bootstrap,
- cross-validation,
- permutation methods.

They are useful because many theoretical distributions are difficult to derive analytically for complex modelling procedures.

---

# 55. Bootstrap

The bootstrap repeatedly samples observations from the observed dataset with replacement.

If the original sample contains:

$n$

observations, a bootstrap sample usually also contains:

$n$

draws, with replacement.

An estimator is calculated for each bootstrap sample.

The resulting distribution can be used to study:

- estimator variability,
- confidence intervals,
- uncertainty.

---

# 56. Bootstrap Standard Error

Suppose bootstrap estimates are:

$\hat{\theta}^{(1)},\ldots,\hat{\theta}^{(B)}$

Their mean is:

$\bar{\theta}_{boot} = \frac1B \sum_{b=1}^{B} \hat{\theta}^{(b)}$

The bootstrap standard deviation is:

$\boxed{ SE_{boot} = \sqrt{ \frac{1}{B-1} \sum_{b=1}^{B} (\hat{\theta}^{(b)}-\bar{\theta}_{boot})^2 } }$

This provides an empirical estimate of estimator variability under the bootstrap assumptions.

---

# 57. Permutation Testing

A permutation test creates a reference distribution by rearranging labels or values under a null hypothesis.

The central idea is:

> If the null hypothesis were true, how unusual would the observed statistic be under random rearrangements consistent with that null?

Permutation tests can be useful when a simple parametric reference distribution is questionable.

---

# 58. Residuals

For a regression prediction:

$\hat{y}_i$

the residual is:

$\boxed{ e_i=y_i-\hat{y}_i }$

Residual analysis can reveal:

- nonlinearity,
- unequal variance,
- unusual observations,
- systematic prediction errors.

A good regression model should not leave obvious systematic structure in residuals when the assumptions and model form are appropriate.

---

# 59. Residual Mean and Intercept

In ordinary least squares regression with an intercept, the residuals satisfy:

$\sum_{i=1}^{n}e_i=0$

Therefore:

$\bar{e}=0$

for the fitted training data under the standard OLS setup.

This does not mean that future prediction errors will have mean exactly zero.

It is a property of the fitted sample and the optimisation procedure.

---

# 60. Heteroscedasticity

Heteroscedasticity means that the variance of the errors changes across levels of predictors or fitted values.

For example, residuals may become more spread out as the predicted value increases.

A residual plot can help detect this pattern.

The presence of heteroscedasticity can affect standard errors and inference in regression models.

---

# 61. Statistical Dependence and Feature Leakage

A feature can be highly predictive because it contains information that would not actually be available at prediction time.

For example, suppose we want to predict whether a customer will cancel a subscription next month.

A feature created from the cancellation record itself would leak future information.

The statistical association may be extremely strong, but it is not a legitimate predictive feature.

Therefore:

$\boxed{ \text{Predictive association is useful only when the information is legitimately available at prediction time.} }$

---

# 62. Distribution Shift

The training distribution may differ from the deployment distribution.

Let:

$P_{train}(X,Y)$

represent the training distribution and:

$P_{deploy}(X,Y)$

represent the deployment distribution.

If:

$P_{train}(X,Y) \ne P_{deploy}(X,Y)$

then model performance can change after deployment.

Distribution shift can involve:

- feature distribution changes,
- class-prior changes,
- changes in conditional relationships.

---

# 63. Covariate Shift

Covariate shift is a situation where:

$P_{train}(X) \ne P_{deploy}(X)$

while the conditional relationship may remain approximately:

$P_{train}(Y\mid X) \approx P_{deploy}(Y\mid X)$

This distinction helps diagnose why a model may perform differently after deployment.

---

# 64. Prior Probability Shift

In prior probability shift, class proportions change:

$P_{train}(Y) \ne P_{deploy}(Y)$

For example, a fraud-detection system may experience a different fraud rate during a new period.

Changes in class prevalence can affect predictive values and threshold performance.

---

# 65. Concept Drift

Concept drift refers broadly to changes in the relationship between inputs and outcomes.

Conceptually:

$P_{train}(Y\mid X) \ne P_{deploy}(Y\mid X)$

Examples may include:

- changing customer behaviour,
- changing market conditions,
- new fraud strategies,
- policy changes.

Statistical monitoring is therefore useful after deployment, not only before model training.

---

# 66. Evaluation Metrics and Statistical Meaning

A metric is not just a number.

It is a statistic calculated from observed predictions and outcomes.

Examples include:

- accuracy,
- precision,
- recall,
- F1,
- MAE,
- MSE,
- RMSE,
- $R^2$,
- log loss.

The metric should match the modelling objective and the consequences of errors.

---

# 67. Regression Error Metrics

For residuals:

$e_i=y_i-\hat{y}_i$

### MAE

$\boxed{ MAE= \frac1n \sum_{i=1}^{n}|e_i| }$

### MSE

$\boxed{ MSE= \frac1n \sum_{i=1}^{n}e_i^2 }$

### RMSE

$\boxed{ RMSE= \sqrt{ \frac1n \sum_{i=1}^{n}e_i^2 } }$

MSE and RMSE place greater emphasis on large errors because the errors are squared.

---

# 68. Choosing Between MAE and RMSE

MAE is easier to interpret because it is in the same units as the target.

RMSE penalises large errors more strongly.

Therefore:

- use MAE when average absolute error is the main concern,
- use RMSE when larger errors should receive stronger penalties.

Neither metric is universally superior.

---

# 69. Classification Metric Selection

A useful starting table is:

| Situation | Useful metric |
|---|---|
| Balanced classes, equal error costs | Accuracy |
| False positives are costly | Precision |
| False negatives are costly | Recall |
| Need a balance between precision and recall | F1 |
| Need ranking across thresholds | ROC-AUC |
| Strong class imbalance and positive-class focus | PR-AUC |
| Need reliable probabilities | Log loss and calibration measures |

Metric selection should be based on the actual decision problem.

---

# 70. Statistical Thinking About Model Comparison

Suppose Model A has test RMSE:

$10.2$

and Model B has:

$10.0$

The numerical difference is:

$0.2$

But we should ask:

- Is the difference stable?
- Was the same test set used?
- Is the test sample large enough?
- Does cross-validation show a consistent advantage?
- Is the improvement practically meaningful?
- Is the evaluation process free from leakage?

A small observed difference should not automatically be treated as a meaningful improvement.

---

# 71. Confidence Intervals for Performance

Performance metrics are calculated from finite samples and therefore have uncertainty.

For example, an accuracy of:

$0.90$

on one test set does not imply that the model's true future accuracy is exactly:

$0.90$

Uncertainty can be studied using:

- analytical methods,
- bootstrap methods,
- repeated cross-validation,
- appropriate confidence intervals.

The correct method depends on the metric and sampling design.

---

# 72. Statistical Significance of Model Differences

When comparing models, it can be useful to examine paired differences in their predictions on the same observations.

Let:

$d_i=L_i^{(A)}-L_i^{(B)}$

where $L_i^{(A)}$ and $L_i^{(B)}$ are losses for models A and B.

Then the mean difference is:

$\bar{d} = \frac1n \sum_{i=1}^{n}d_i$

A confidence interval for the mean difference can provide more information than simply reporting two separate averages.

However, the assumptions and dependence structure of the evaluation design must be considered.

---

# 73. Practical Statistical Workflow

A statistically informed machine-learning workflow can be organised as follows.

### Step 1: Define the population and prediction task

Clarify who or what the model is intended to serve.

### Step 2: Collect and inspect data

Check quality, coverage, missingness, and measurement.

### Step 3: Explore distributions

Use descriptive statistics and visualisations.

### Step 4: Split data correctly

Separate training and evaluation information.

### Step 5: Fit preprocessing on training data

Avoid leakage.

### Step 6: Train candidate models

Use appropriate modelling procedures.

### Step 7: Validate

Use validation sets or cross-validation.

### Step 8: Evaluate on the held-out test set

Use metrics that reflect the real objective.

### Step 9: Quantify uncertainty

Use confidence intervals, bootstrap methods, or repeated evaluation where appropriate.

### Step 10: Monitor after deployment

Look for distribution shift, calibration changes, and performance degradation.

---

# 74. Complete Example: Customer Churn

Suppose we want to predict whether a customer will leave a service.

Features include:

- tenure,
- monthly charges,
- contract type,
- number of support calls,
- payment method.

Target:

$Y= \begin{cases} 1,&\text{customer churns}\\ 0,&\text{customer stays} \end{cases}$

A statistically informed analysis should consider:

1. class prevalence,
2. missing values,
3. feature distributions,
4. sampling bias,
5. leakage,
6. train-test splitting,
7. class imbalance,
8. probability calibration,
9. precision and recall,
10. threshold selection,
11. confidence in performance estimates,
12. possible distribution shift after deployment.

---

# 75. Worked Class-Imbalance Example

Suppose a test set contains:

$1000$

customers.

Only:

$20$

churn.

A model predicts no customer will churn.

Then:

$TN=980$

and:

$FN=20$

Accuracy is:

$Accuracy= \frac{980+0}{1000}$

$=0.98$

Therefore:

$\boxed{Accuracy=98\%}$

But recall is:

$Recall= \frac{TP}{TP+FN}$

Since:

$TP=0$

we obtain:

$Recall=0$

Thus the model has excellent-looking accuracy but completely fails to identify churners.

---

# 76. Statistical Interpretation of the Example

The previous example demonstrates why a metric must be interpreted relative to the data distribution and decision problem.

The majority class dominates the accuracy calculation.

Therefore:

$\boxed{ \text{A high aggregate metric can hide poor minority-class performance.} }$

This is a statistical reason to inspect class distributions before selecting evaluation metrics.

---

# 77. Reproducibility

Statistical experiments should be reproducible where possible.

Set a random seed for simulations:

```python
rng = np.random.default_rng(42)
```

Document:

- dataset version,
- sampling procedure,
- preprocessing,
- random seed,
- model settings,
- evaluation procedure.

Reproducibility makes it easier to determine whether an observed difference is due to the method or random variation.

---

# 78. Practical Python: Basic Statistical Summary

```python
import pandas as pd

df = pd.DataFrame({
    "age": [21, 25, 29, 31, 45],
    "income": [25000, 32000, 41000, 45000, 90000]
})

print(df.describe())
```

This provides common descriptive statistics such as:

- count,
- mean,
- standard deviation,
- minimum,
- quartiles,
- maximum.

---

# 79. Practical Python: Standardisation

```python
from sklearn.preprocessing import StandardScaler

X = df[["age", "income"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled)
```

The important statistical rule is:

$\boxed{ \text{fit the scaler on training data only} }$

For validation or test data, use:

```python
X_test_scaled = scaler.transform(X_test)
```

not:

```python
scaler.fit_transform(X_test)
```

---

# 80. Practical Python: Correlation Matrix

```python
correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)
```

A correlation matrix helps identify strong linear associations between numerical variables.

It should be treated as an exploratory tool rather than proof of causation.

---

# 81. Practical Python: Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    df["income"],
    cv=5,
    scoring="neg_mean_squared_error"
)

mse_scores = -scores

print("Fold MSE:", mse_scores)
print("Mean CV MSE:", mse_scores.mean())
```

Each fold provides a different validation estimate.

The average summarises the observed cross-validation performance.

---

# 82. Practical Python: Bootstrap Mean

```python
rng = np.random.default_rng(42)

data = np.array([12, 15, 14, 18, 21, 16, 17, 13])

bootstrap_means = []

for _ in range(5000):
    sample = rng.choice(data, size=len(data), replace=True)
    bootstrap_means.append(sample.mean())

bootstrap_means = np.array(bootstrap_means)

print("Bootstrap mean:", bootstrap_means.mean())
print("Bootstrap standard error:", bootstrap_means.std(ddof=1))
```

The bootstrap distribution provides an empirical view of the uncertainty in the sample mean.

---

# 83. Practical Python: Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1, 1, 0, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0, 1, 0]

cm = confusion_matrix(y_true, y_pred)

print(cm)
```

From this matrix, calculate:

- TP,
- TN,
- FP,
- FN,

and then the relevant classification metrics.

---

# 84. Practical Python: Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))
```

Do not report these metrics without considering class balance and the cost of errors.

---

# 85. Common Mistakes in Statistics for Machine Learning

### Mistake 1: Treating correlation as causation

Correlation only describes association under the chosen calculation.

### Mistake 2: Scaling before the train-test split

This can leak information from evaluation data.

### Mistake 3: Using accuracy for every classification problem

Class imbalance can make accuracy misleading.

### Mistake 4: Repeatedly tuning on the test set

This contaminates the final evaluation.

### Mistake 5: Removing every outlier

Some outliers are genuine and important.

### Mistake 6: Assuming a small p-value means a large effect

Statistical significance and practical importance are different.

### Mistake 7: Assuming more data automatically solves every problem

More data can reduce sampling variability but cannot automatically remove biased sampling or structural model limitations.

### Mistake 8: Interpreting model coefficients causally

A fitted coefficient is not automatically a causal effect.

### Mistake 9: Ignoring uncertainty in model metrics

Performance estimates come from finite samples and can vary.

### Mistake 10: Treating one validation split as absolute truth

Validation performance is an estimate, not a guarantee.

---

# 86. Important Formula Summary

### Z-score

$\boxed{ z=\frac{x-\mu}{\sigma} }$

### Min-max scaling

$\boxed{ x'= \frac{x-x_{\min}} {x_{\max}-x_{\min}} }$

### Sample covariance

$\boxed{ s_{XY} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i-\bar{x})(y_i-\bar{y}) }$

### Pearson correlation

$\boxed{ r= \frac{s_{XY}}{s_Xs_Y} }$

### VIF

$\boxed{ VIF_j= \frac{1}{1-R_j^2} }$

### Cross-validation mean error

$\boxed{ CV\ Error= \frac1k \sum_{j=1}^{k}E_j }$

### Accuracy

$\boxed{ Accuracy= \frac{TP+TN}{TP+TN+FP+FN} }$

### Precision

$\boxed{ Precision= \frac{TP}{TP+FP} }$

### Recall

$\boxed{ Recall= \frac{TP}{TP+FN} }$

### F1 score

$\boxed{ F_1= 2 \frac{Precision\cdot Recall} {Precision+Recall} }$

### MAE

$\boxed{ MAE= \frac1n\sum_{i=1}^{n}|y_i-\hat y_i| }$

### MSE

$\boxed{ MSE= \frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2 }$

### RMSE

$\boxed{ RMSE= \sqrt{ \frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2 } }$

### Multiple-comparison probability

For $m$ independent tests at level $\alpha$:

$\boxed{ P(\text{at least one false positive}) = 1-(1-\alpha)^m }$

---

# 87. Quick Concept Comparison

| Concept | Main purpose |
|---|---|
| Descriptive statistics | Summarise observed data |
| Inferential statistics | Learn about a population from a sample |
| Sampling bias | Detect systematic differences caused by sample selection |
| Standardisation | Put numerical features on a common standard-deviation scale |
| Correlation | Measure linear association |
| Covariance | Measure joint variation in original units |
| Cross-validation | Estimate generalisation performance using repeated validation splits |
| Bootstrap | Estimate sampling variability by resampling observations |
| Confidence interval | Quantify uncertainty using an inferential procedure |
| p-value | Measure compatibility of data with a null model under a test |
| Effect size | Quantify the magnitude of an observed difference or relationship |
| Calibration | Assess whether predicted probabilities match observed frequencies |
| Residual | Difference between observed and predicted response |
| Data leakage | Unintended use of information that would not be available at prediction time |
| Distribution shift | Difference between training and deployment distributions |
| Class imbalance | Unequal class frequencies |
| Multicollinearity | Strong dependence among predictors |
| MAE | Average absolute prediction error |
| RMSE | Square-root average squared prediction error |

---

# 88. Points to Remember

1. Statistics helps machine learning understand data, uncertainty, relationships, and generalisation.
2. A dataset is usually a sample from a broader population relevant to the task.
3. Sampling bias can cause a model to learn an unrepresentative pattern.
4. More observations from a biased process do not automatically remove sampling bias.
5. Descriptive statistics should be chosen according to the variable and distribution.
6. Standardisation and min-max scaling are different transformations.
7. Scaling parameters should be learned from training data only.
8. Correlation measures association, not causation.
9. Multicollinearity can make regression coefficients unstable.
10. Train, validation, and test data have different roles.
11. Test data should remain isolated from model-selection decisions.
12. Cross-validation provides an estimate of generalisation performance but is not a guarantee.
13. Class imbalance can make accuracy misleading.
14. Precision and recall answer different questions.
15. Predicted probabilities should be evaluated for calibration when probability quality matters.
16. A p-value is not the probability that the null hypothesis is true.
17. Statistical significance does not automatically imply practical significance.
18. Multiple testing increases the chance of false positives if no adjustment or appropriate control is used.
19. Bootstrap methods can estimate sampling variability empirically.
20. Residual analysis can reveal model problems.
21. Data leakage can produce unrealistically strong evaluation results.
22. Distribution shift can reduce deployment performance.
23. Performance metrics are themselves estimates based on finite data.
24. Statistical reasoning should be integrated with the actual decision problem.
25. Good machine learning is not only about fitting a model; it is also about understanding how the data and evaluation process affect the conclusions.

---

# 89. Chapter Summary

Statistics for machine learning is not a separate collection of formulas. It is the use of statistical reasoning throughout the modelling process.

The first question is about the data:

$\boxed{ \text{What population does this sample represent?} }$

The next questions concern the variables:

$\boxed{ \text{How are the variables distributed and related?} }$

Then we consider model development:

$\boxed{ \text{How can we estimate performance without leakage?} }$

Finally, we consider uncertainty and deployment:

$\boxed{ \text{How stable is the result, and will it generalise?} }$

Important statistical tools include:

- descriptive statistics,
- standardisation,
- sampling,
- correlation,
- covariance,
- confidence intervals,
- hypothesis testing,
- effect sizes,
- resampling,
- cross-validation,
- calibration,
- residual analysis,
- distribution-shift analysis.

The most important practical principle is:

$\boxed{ \text{A model result is only as trustworthy as the data, assumptions, and evaluation procedure behind it.} }$

This chapter therefore serves as the bridge between the statistical foundations developed throughout the Mathematics & Statistics section and the applied modelling work in the Machine Learning section.

---

# 90. References

- Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, *An Introduction to Statistical Learning*.
- Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning*.
- Larry Wasserman, *All of Statistics*.
- Casella and Berger, *Statistical Inference*.
- Stanford University, statistical learning resources.
- MIT OpenCourseWare, probability and statistics resources.
- Scikit-learn Documentation.
- NumPy Documentation.
- SciPy Documentation.
- Matplotlib Documentation.
