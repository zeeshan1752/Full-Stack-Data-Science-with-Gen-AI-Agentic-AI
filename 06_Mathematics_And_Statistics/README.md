
# Mathematics and Statistics

Mathematics and Statistics form the foundation of Data Science, Machine Learning, Artificial Intelligence, and many areas of computer science.

Data Science is not only about writing Python code or using machine-learning libraries. It also requires understanding data, identifying patterns, measuring uncertainty, analysing relationships, building mathematical models, and evaluating predictions.

This section develops these foundations step by step, from basic statistical concepts to the mathematical principles behind modern machine-learning algorithms.

The main objective is to understand **why mathematical and statistical methods work, when to use them, and how they support real-world data-driven decisions.**

---

## 1. Learning Objectives

After completing this section, you should be able to:

- Understand populations, samples, variables, and statistical measurements.
- Summarise and visualise datasets using descriptive statistics.
- Apply probability rules and understand conditional probability.
- Identify and work with common probability distributions.
- Estimate population parameters and quantify uncertainty.
- Perform hypothesis tests and interpret statistical results.
- Compare multiple groups using ANOVA and analyse categorical data using Chi-Square tests.
- Measure relationships between variables using correlation.
- Build and interpret regression models.
- Evaluate regression models using appropriate metrics.
- Represent datasets and mathematical operations using vectors and matrices.
- Understand derivatives, gradients, and optimisation.
- Explain the bias-variance trade-off, underfitting, and overfitting.
- Apply statistical reasoning throughout a machine-learning workflow.
- Implement statistical calculations and experiments using Python.

---

## 2. Repository Structure

The Mathematics and Statistics section contains 15 topic-wise folders.

```text
Mathematics_and_Statistics/
│
├── README.md
│
├── 01_Statistics_Fundamentals/
│   ├── README.md
│   └── statistics_fundamentals.ipynb
│
├── 02_Descriptive_Statistics/
│   ├── README.md
│   └── descriptive_statistics.ipynb
│
├── 03_Probability/
│   ├── README.md
│   └── probability.ipynb
│
├── 04_Probability_Distributions/
│   ├── README.md
│   └── probability_distributions.ipynb
│
├── 05_Inferential_Statistics/
│   ├── README.md
│   └── inferential_statistics.ipynb
│
├── 06_Hypothesis_Testing/
│   ├── README.md
│   └── hypothesis_testing.ipynb
│
├── 07_ANOVA/
│   ├── README.md
│   └── anova.ipynb
│
├── 08_Chi_Square_Test/
│   ├── README.md
│   └── chi_square_test.ipynb
│
├── 09_Correlation/
│   ├── README.md
│   └── correlation.ipynb
│
├── 10_Regression/
│   ├── README.md
│   └── regression.ipynb
│
├── 11_Regression_Model_Evaluation/
│   ├── README.md
│   └── regression_model_evaluation.ipynb
│
├── 12_Linear_Algebra/
│   ├── README.md
│   └── linear_algebra.ipynb
│
├── 13_Calculus/
│   ├── README.md
│   └── calculus.ipynb
│
├── 14_Bias_And_Variance/
│   ├── README.md
│   └── bias_and_variance.ipynb
│
└── 15_Statistics_for_Machine_Learning/
    ├── README.md
    └── statistics_for_machine_learning.ipynb
```

Each folder has a specific purpose.

The `README.md` explains concepts, formulas, assumptions, worked examples, and applications. The Jupyter Notebook provides Python implementations, calculations, visualisations, and practical experiments.

---

## 3. Overview of All 15 Folders

### Folder 01 — Statistics Fundamentals

**Purpose:** Understand the basic terminology and principles used in statistics.

Key topics:

- Population and sample
- Parameters and statistics
- Variables and observations
- Qualitative and quantitative data
- Discrete and continuous variables
- Levels of measurement
- Sampling methods
- Sampling bias and data collection
- Statistical reasoning

**Application:** Understanding what a dataset represents, how it was collected, and whether its observations are suitable for analysis.

### Folder 02 — Descriptive Statistics

**Purpose:** Summarise and understand the main characteristics of observed data.

Key topics:

- Mean, median, and mode
- Weighted mean
- Range, variance, and standard deviation
- Quartiles and percentiles
- Interquartile range (IQR)
- Five-number summary
- Frequency distributions and histograms
- Box plots and outliers
- Skewness and kurtosis

**Application:** Exploratory Data Analysis (EDA), data cleaning, feature analysis, reporting, and preprocessing.

### Folder 03 — Probability

**Purpose:** Understand uncertainty and calculate the likelihood of events.

Key topics:

- Experiments, outcomes, sample spaces, and events
- Probability rules
- Addition and multiplication rules
- Conditional probability
- Independent events
- Bayes' theorem
- Random variables
- Expected value and variance
- Covariance
- Permutations and combinations

**Application:** Classification probabilities, Bayesian methods, risk estimation, probabilistic modelling, and decision-making under uncertainty.

### Folder 04 — Probability Distributions

**Purpose:** Understand how probabilities are distributed across possible values of random variables.

Key topics:

- Probability mass function (PMF)
- Probability density function (PDF)
- Cumulative distribution function (CDF)
- Bernoulli distribution
- Binomial distribution
- Poisson distribution
- Geometric and Negative Binomial distributions
- Hypergeometric distribution
- Uniform distribution
- Normal and Standard Normal distributions
- Exponential distribution
- Expected value and variance
- Z-scores
- Central Limit Theorem

**Application:** Statistical inference, simulation, uncertainty modelling, anomaly detection, and understanding data distributions.

### Folder 05 — Inferential Statistics

**Purpose:** Draw conclusions about a population using sample data.

Key topics:

- Sampling distributions
- Standard error
- Point estimation
- Properties of estimators
- Confidence intervals
- Confidence levels
- Margin of error
- Sample-size considerations
- Bootstrap confidence intervals

**Application:** Estimating population characteristics, analysing experiments, quantifying uncertainty, and assessing the reliability of statistical conclusions.

### Folder 06 — Hypothesis Testing

**Purpose:** Evaluate statistical claims using sample evidence.

Key topics:

- Null and alternative hypotheses
- Significance level
- Test statistics and critical values
- P-values
- One-tailed and two-tailed tests
- Type I and Type II errors
- Statistical power
- Z-tests and t-tests
- Proportion tests
- Effect size
- Practical versus statistical significance

**Application:** Comparing groups, evaluating experiments, testing assumptions, and interpreting evidence.

### Folder 07 — ANOVA

**Purpose:** Compare group means using Analysis of Variance.

Key topics:

- Between-group and within-group variation
- Total sum of squares
- Degrees of freedom
- Mean squares
- F-statistic and F-distribution
- ANOVA tables
- One-way and two-way ANOVA
- Assumptions of ANOVA
- Post-hoc tests, including Tukey HSD
- Effect sizes

**Application:** Comparing multiple treatments, product variants, teaching methods, or experimental groups.

### Folder 08 — Chi-Square Test

**Purpose:** Analyse categorical frequency data.

Key topics:

- Observed and expected frequencies
- Chi-Square goodness-of-fit test
- Test of independence
- Test of homogeneity
- Contingency tables
- Degrees of freedom
- Standardised or adjusted residuals
- Cramer's V and Phi coefficient
- Yates' correction
- Fisher's exact test

**Application:** Analysing relationships between categorical variables, such as device type and customer churn or region and purchase preference.

### Folder 09 — Correlation

**Purpose:** Measure the strength and direction of relationships between variables.

Key topics:

- Covariance
- Pearson correlation
- Spearman rank correlation
- Correlation matrices
- Scatter plots
- Positive and negative relationships
- Outliers and their effects
- Nonlinear relationships
- Correlation versus causation

**Application:** EDA, feature analysis, identifying related variables, and investigating possible multicollinearity.

### Folder 10 — Regression

**Purpose:** Model relationships between variables and predict numerical outcomes.

Key topics:

- Simple linear regression
- Slope and intercept
- Least squares estimation
- Fitted values and residuals
- Multiple linear regression
- Categorical predictors and dummy variables
- Interaction terms
- Polynomial regression
- Feature transformations
- Regression assumptions
- Interpretation of coefficients

**Application:** Predicting house prices, sales, demand, income, and other numerical outcomes.

### Folder 11 — Regression Model Evaluation

**Purpose:** Measure regression performance and assess how well a model generalises to unseen data.

Key topics:

- Residual analysis
- Sum of Squared Errors (SSE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- R-squared and adjusted R-squared
- Baseline models
- Training and test performance
- Train-test splitting
- Cross-validation
- Model comparison
- Data leakage
- Generalisation

**Application:** Comparing regression models, detecting poor predictions, and selecting suitable evaluation metrics.

### Folder 12 — Linear Algebra

**Purpose:** Understand the mathematical representation and manipulation of multidimensional data.

Key topics:

- Scalars, vectors, and matrices
- Vector and matrix operations
- Matrix multiplication and transpose
- Determinants and inverse matrices
- Systems of linear equations
- Gaussian elimination
- Rank and linear independence
- Span and basis
- Dot product and norms
- Distance and orthogonality
- Projections
- Eigenvalues and eigenvectors
- Diagonalisation
- Singular Value Decomposition (SVD)

**Application:** Linear regression, Principal Component Analysis (PCA), neural networks, dimensionality reduction, recommendation systems, and computer vision.

### Folder 13 — Calculus

**Purpose:** Understand rates of change, accumulation, and mathematical optimisation.

Key topics:

- Functions and limits
- Continuity
- Derivatives and differentiation rules
- Higher-order derivatives
- Partial derivatives
- Gradients and directional derivatives
- Critical points and optimisation
- Convexity
- Hessians
- Integration and definite integrals
- Numerical integration
- Gradient descent
- Chain rule and backpropagation

**Application:** Understanding loss functions, optimisation algorithms, neural-network training, and parameter updates.

### Folder 14 — Bias and Variance

**Purpose:** Understand model complexity, prediction error, and generalisation.

Key topics:

- Estimator bias and variance
- Standard error
- Mean Squared Error (MSE)
- Bias-variance decomposition
- Consistency and efficiency
- Prediction bias and variance
- Irreducible error
- Underfitting and overfitting
- Model complexity
- Regularisation
- Learning curves
- Bootstrap perspective

**Application:** Diagnosing model performance, balancing model complexity, choosing regularisation strength, and improving generalisation.

### Folder 15 — Statistics for Machine Learning

**Purpose:** Apply statistical concepts throughout practical machine-learning workflows.

Key topics:

- Sampling and representativeness
- Feature distributions
- Standardisation and normalisation
- Skewness, outliers, and missing data
- Data leakage
- Training, validation, and test sets
- Cross-validation
- Covariance and correlation
- Multicollinearity
- Confidence intervals and statistical significance
- Effect size
- Class imbalance
- Classification metrics
- Probability thresholds and calibration
- Bootstrap and resampling
- Residual analysis
- Distribution shift
- Model comparison and uncertainty in performance

**Application:** Preparing datasets, selecting evaluation methods, comparing models, interpreting predictions, and monitoring deployed machine-learning systems.

---

## 4. Recommended Learning Order

Follow the folder sequence to build concepts progressively.

```text
01. Statistics Fundamentals
          |
          v
02. Descriptive Statistics
          |
          v
03. Probability
          |
          v
04. Probability Distributions
          |
          v
05. Inferential Statistics
          |
          v
06. Hypothesis Testing
          |
          v
07. ANOVA
          |
          v
08. Chi-Square Test
          |
          v
09. Correlation
          |
          v
10. Regression
          |
          v
11. Regression Model Evaluation
          |
          v
12. Linear Algebra
          |
          v
13. Calculus
          |
          v
14. Bias and Variance
          |
          v
15. Statistics for Machine Learning
```

The sequence provides a recommended path, not a strict prerequisite chain. You can begin basic Machine Learning before mastering every mathematical topic and study advanced concepts when they become relevant.

For example, linear algebra and calculus can also be studied alongside regression and machine learning rather than only after completing regression evaluation.

---

## 5. How the Topics Connect

The 15 folders are related parts of a larger system.

| Concept | Connection to Other Topics |
|---|---|
| Statistics Fundamentals | Establishes the terminology for every statistical topic |
| Descriptive Statistics | Summarises the data studied through probability and inference |
| Probability | Provides the foundation for probability distributions |
| Probability Distributions | Supports estimation, confidence intervals, and hypothesis tests |
| Inferential Statistics | Uses sample data to estimate population characteristics |
| Hypothesis Testing | Evaluates statistical claims using probability and sampling distributions |
| ANOVA | Applies hypothesis testing to comparisons involving multiple group means |
| Chi-Square Test | Applies statistical testing to categorical frequency data |
| Correlation | Measures association between variables and supports feature analysis |
| Regression | Models relationships and produces predictions |
| Regression Model Evaluation | Measures prediction errors and generalisation |
| Linear Algebra | Represents data and model parameters using vectors and matrices |
| Calculus | Supports optimisation and gradient-based learning |
| Bias and Variance | Explains the relationship between model complexity and prediction error |
| Statistics for Machine Learning | Integrates these concepts into practical modelling workflows |

---

## 6. Mathematics vs Statistics vs Machine Learning

These fields overlap, but each has a different primary role.

| Area | Main Purpose | Example |
|---|---|---|
| Mathematics | Represents and calculates relationships | Matrix multiplication, derivatives, and gradients |
| Statistics | Understands data, variability, and uncertainty | Confidence intervals and hypothesis testing |
| Machine Learning | Learns patterns for prediction or decision-making | Training a model to predict customer churn |

Consider a dataset containing customer information.

Mathematics helps represent the dataset and calculate model outputs.

Statistics helps describe the customers, analyse relationships, and assess uncertainty.

Machine Learning uses the data to train a model that predicts an outcome for new customers.

These three areas work together in practical Data Science projects.

---

## 7. Statistics Across the Data Science Workflow

Statistical thinking is useful at every stage of a data project.

### Stage 1: Data Collection

Use statistical concepts to understand the population, select a sampling method, and assess whether the sample is representative.

### Stage 2: Data Cleaning

Examine missing values, unusual observations, inconsistent measurements, and potential data-quality problems.

### Stage 3: Exploratory Data Analysis

Calculate descriptive statistics, examine distributions, create visualisations, and investigate relationships between variables.

### Stage 4: Feature Engineering and Preprocessing

Study feature distributions, select suitable transformations, scale numerical features where needed, and investigate redundant variables.

### Stage 5: Model Building

Use probability, linear algebra, calculus, and statistical modelling to understand the mathematical foundations of learning algorithms.

### Stage 6: Model Evaluation

Choose appropriate metrics, compare against baseline models, use cross-validation when suitable, and assess the uncertainty of performance estimates.

### Stage 7: Deployment and Monitoring

Monitor changing feature distributions, changes in the relationship between features and targets, and degradation in model performance.

---

## 8. A Practical Machine-Learning Workflow

The following workflow connects statistical foundations to machine-learning implementation.

```text
Raw Dataset
     |
     v
Understand Population and Features
     |
     v
Explore Data and Distributions
     |
     v
Check Data Quality
     |
     v
Split Data into Training and Evaluation Sets
     |
     v
Fit Preprocessing on Training Data
     |
     v
Train Baseline and Candidate Models
     |
     v
Validate and Tune Models
     |
     v
Evaluate on Unseen Data
     |
     v
Analyse Errors and Uncertainty
     |
     v
Deploy and Monitor
```

Important practices:

- Keep the test set separate from model development and tuning.
- Fit preprocessing steps, such as scaling and imputation, using training data only.
- Use cross-validation when appropriate for reliable model comparison.
- Choose evaluation metrics according to the problem and the consequences of errors.
- Do not assume that statistical significance automatically means practical importance.
- Monitor whether the data encountered after deployment differs from the training data.

---

## 9. Python Libraries for Mathematics and Statistics

The following libraries support the practical implementation of these concepts.

| Library | Main Purpose |
|---|---|
| NumPy | Numerical computation, arrays, vectors, and matrices |
| pandas | Data manipulation and descriptive summaries |
| SciPy | Statistical tests, distributions, and scientific computation |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| SymPy | Symbolic mathematics, differentiation, and integration |
| scikit-learn | Preprocessing, regression, model evaluation, and cross-validation |
| statsmodels | Statistical modelling, regression summaries, and inference |

Install the commonly used libraries with:

```bash
pip install numpy pandas scipy matplotlib seaborn sympy scikit-learn statsmodels
```

### Example: Basic Statistical Analysis

```python
import numpy as np
import pandas as pd

data = pd.Series([10, 20, 20, 30, 40])

print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode().tolist())
print("Variance:", data.var())
print("Standard Deviation:", data.std())
print("Minimum:", data.min())
print("Maximum:", data.max())
```

Note that pandas uses sample variance and sample standard deviation by default. NumPy's `np.var()` and `np.std()` use population-based calculations by default (`ddof=0`). Always check which convention is appropriate for the problem.

---

## 10. Recommended Study Method

Use the following process for each folder.

1. Read the folder's `README.md`.
2. Understand the concepts and terminology.
3. Study the formulas and their assumptions.
4. Solve the worked examples manually.
5. Open the corresponding Jupyter Notebook.
6. Run the Python implementations.
7. Change the input data and observe the results.
8. Create visualisations where appropriate.
9. Solve practice questions.
10. Review the common mistakes and points to remember.

Do not focus only on memorising formulas. For every concept, ask:

- What does it mean?
- Why is it needed?
- When should it be used?
- What assumptions does it make?
- How should its result be interpreted?
- How can it affect a Data Science or Machine Learning decision?

Understanding these questions is more valuable than memorising formulas without knowing how to apply them.

---

## 11. Recommended Foundations Before Machine Learning

You do not need to master every topic before beginning Machine Learning. However, the following foundations will make algorithms easier to understand.

### Statistics

- Mean, median, variance, and standard deviation
- Probability and conditional probability
- Common probability distributions
- Sampling and statistical inference
- Confidence intervals and hypothesis testing
- Correlation and regression
- Bias, variance, and generalisation

### Mathematics

- Vectors and matrices
- Matrix operations and dot products
- Basic eigenvalues and eigenvectors
- Functions and derivatives
- Partial derivatives and gradients
- Optimisation fundamentals

### Practical Machine Learning

- Train-test splitting
- Preprocessing without data leakage
- Cross-validation
- Regression and classification metrics
- Overfitting and underfitting
- Model comparison

Study advanced material, such as Hessians, detailed distribution theory, and specialised statistical tests, when your projects require it.

---

## 12. Common Mistakes to Avoid

- Confusing a sample statistic with a population parameter.
- Assuming that correlation proves causation.
- Treating a p-value as the probability that the null hypothesis is true.
- Ignoring assumptions when applying statistical tests.
- Comparing model metrics without considering the target's scale and meaning.
- Treating a high training score as proof of good generalisation.
- Fitting preprocessing steps on the complete dataset before splitting.
- Selecting evaluation metrics without considering the real-world problem.
- Ignoring class imbalance when evaluating classification models.
- Assuming that every feature needs standardisation.
- Assuming that every dataset follows a normal distribution.
- Confusing statistical significance with practical importance.
- Treating data drift and model performance degradation as identical problems.

The appropriate method depends on the data, the research question, the model, and the consequences of an incorrect conclusion.

---

## 13. Final Learning Checklist

Use this checklist to review your understanding of the Mathematics and Statistics section.

### Statistical Foundations

- [ ] Population, sample, parameters, and statistics
- [ ] Variables, observations, and measurement scales
- [ ] Sampling methods and sampling bias
- [ ] Mean, median, mode, variance, and standard deviation
- [ ] Quartiles, percentiles, IQR, and outliers
- [ ] Skewness and probability distributions

### Probability and Inference

- [ ] Probability rules and conditional probability
- [ ] Independence and Bayes' theorem
- [ ] Random variables and expected value
- [ ] Common discrete and continuous distributions
- [ ] Sampling distributions and standard error
- [ ] Point estimation and confidence intervals
- [ ] Hypothesis testing, p-values, and statistical power
- [ ] ANOVA and Chi-Square tests
- [ ] Effect size and practical significance

### Relationships and Modelling

- [ ] Covariance and correlation
- [ ] Simple and multiple linear regression
- [ ] Regression assumptions and coefficient interpretation
- [ ] SSE, MSE, RMSE, MAE, and R-squared
- [ ] Residual analysis and cross-validation
- [ ] Baselines, model comparison, and generalisation

### Mathematical Foundations

- [ ] Vectors and matrices
- [ ] Matrix operations and dot products
- [ ] Rank, linear independence, and projections
- [ ] Eigenvalues, eigenvectors, and SVD
- [ ] Functions, derivatives, and partial derivatives
- [ ] Gradients and optimisation
- [ ] Chain rule and backpropagation fundamentals

### Statistics for Machine Learning

- [ ] Feature distributions and preprocessing
- [ ] Missing data and outlier analysis
- [ ] Data leakage prevention
- [ ] Train, validation, and test sets
- [ ] Bias-variance trade-off
- [ ] Underfitting, overfitting, and regularisation
- [ ] Class imbalance and classification metrics
- [ ] Probability thresholds and calibration
- [ ] Bootstrap and uncertainty estimation
- [ ] Distribution shift and model monitoring

---

## 14. References and Learning Resources

Use textbooks and official documentation to deepen your understanding.

### Books

- Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, and Jonathan Taylor — *An Introduction to Statistical Learning*
- Trevor Hastie, Robert Tibshirani, and Jerome Friedman — *The Elements of Statistical Learning*
- Larry Wasserman — *All of Statistics*
- George Casella and Roger L. Berger — *Statistical Inference*

### Online Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [SymPy Documentation](https://docs.sympy.org/latest/index.html)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [statsmodels Documentation](https://www.statsmodels.org/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [GitHub Mathematical Expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)


---

## Conclusion

Mathematics and Statistics provide the foundation for understanding data, evaluating uncertainty, building predictive models, and interpreting machine-learning results.

The 15 folders progress from statistical fundamentals to probability, inference, relationships, regression, mathematical foundations, model generalisation, and practical statistical reasoning.

The overall progression is:

**Understand Data → Describe Data → Model Uncertainty → Make Inferences → Analyse Relationships → Build Models → Evaluate Generalisation → Apply Statistics to Machine Learning**

The purpose is not simply to memorise formulas. It is to understand the reasoning behind the methods and learn when and why to apply them.

With these foundations in place, the Machine Learning, Deep Learning, Generative AI, and Agentic AI sections can focus more effectively on algorithms, implementation, experimentation, and real-world applications.
