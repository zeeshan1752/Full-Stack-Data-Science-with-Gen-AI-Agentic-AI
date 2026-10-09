# Mathematics and Statistics

Mathematics and Statistics form the foundation of Data Science, Machine Learning, Artificial Intelligence, and many areas of computer science.

A machine-learning model does not simply learn by "running an algorithm". It works with data, measurements, probabilities, relationships between variables, uncertainty, optimisation, and mathematical representations.

This section builds those foundations step by step.

The purpose of this folder is to understand **the mathematical and statistical ideas behind data analysis and machine learning**, before moving into practical machine-learning algorithms.

---

# 1. Why Mathematics and Statistics Are Important

When working with data, we constantly ask questions such as:

- What does the data look like?
- What is the average value?
- How much does the data vary?
- How likely is an event?
- How can we estimate an unknown quantity?
- Is an observed difference meaningful?
- Are two variables related?
- How strong is that relationship?
- Can one variable be used to predict another?
- How accurately does a model predict?
- Is a model overfitting?
- How uncertain is a prediction?
- What happens when the data changes?
- How can numerical data be represented using vectors and matrices?
- How can a model minimise an error function?

These questions are answered using different areas of mathematics and statistics.

Therefore, this section is organised as a progression rather than as unrelated topics.

---

# 2. How This Section Is Organised

The Mathematics and Statistics section contains **15 folders**.

```text
Mathematics_and_Statistics/
│
├── 01_Statistics_Fundamentals/
├── 02_Descriptive_Statistics/
├── 03_Probability/
├── 04_Probability_Distributions/
├── 05_Inferential_Statistics/
├── 06_Hypothesis_Testing/
├── 07_ANOVA/
├── 08_Chi_Square_Test/
├── 09_Correlation/
├── 10_Regression/
├── 11_Regression_Model_Evaluation/
├── 12_Linear_Algebra/
├── 13_Calculus/
├── 14_Bias_and_Variance/
└── 15_Statistics_for_Machine_Learning/
```

Each topic folder contains:

```text
README.md
Topic_Name.ipynb
```

The `README.md` provides the textbook-style explanation.

The `.ipynb` notebook provides practical calculations, Python implementation, visualisation, experiments, and exercises.

---

# 3. Recommended Learning Order

The folders are arranged in a logical learning sequence.

$$
\boxed{
\text{Statistics Fundamentals}
\rightarrow
\text{Descriptive Statistics}
\rightarrow
\text{Probability}
\rightarrow
\text{Probability Distributions}
}
$$

Then:

$$
\boxed{
\text{Inference}
\rightarrow
\text{Hypothesis Testing}
\rightarrow
\text{ANOVA}
\rightarrow
\text{Chi-Square}
}
$$

Then:

$$
\boxed{
\text{Correlation}
\rightarrow
\text{Regression}
\rightarrow
\text{Regression Evaluation}
}
$$

And the mathematical foundations:

$$
\boxed{
\text{Linear Algebra}
\rightarrow
\text{Calculus}
\rightarrow
\text{Bias and Variance}
}
$$

Finally:

$$
\boxed{
\text{Statistics for Machine Learning}
}
$$

The final folder brings together the statistical concepts that are repeatedly used during practical machine-learning work.

---

# 4. Folder 01 — Statistics Fundamentals

## What is covered?

This folder introduces the basic language of statistics.

Topics include:

- population,
- sample,
- parameter,
- statistic,
- variables,
- observations,
- qualitative and quantitative data,
- discrete and continuous variables,
- levels of measurement,
- sampling,
- sampling methods,
- bias,
- data collection,
- statistical reasoning.

## Where is it used?

These concepts are used whenever data is collected or analysed.

For example, before training a model, we need to understand:

- What population does the dataset represent?
- How was the sample collected?
- Are the observations representative?
- What type of variables are present?
- Are the measurements reliable?

## Why study it first?

This folder establishes the vocabulary required for the rest of the Statistics section.

---

# 5. Folder 02 — Descriptive Statistics

## What is covered?

Descriptive statistics focuses on summarising and understanding observed data.

Topics include:

- mean,
- median,
- mode,
- weighted mean,
- range,
- variance,
- standard deviation,
- quartiles,
- percentiles,
- IQR,
- five-number summary,
- box plots,
- outliers,
- skewness,
- kurtosis,
- frequency distributions,
- histograms.

## Where is it used?

Descriptive statistics is heavily used during **Exploratory Data Analysis (EDA)**.

For example, before training a model, we may want to know:

```text
What is the average age?
What is the typical income?
How spread out are the values?
Are there extreme observations?
Is the feature highly skewed?
```

A simple summary can reveal problems that would otherwise remain hidden.

## Practical use

Descriptive statistics is used in:

- Data Analysis
- EDA
- Data Cleaning
- Feature Analysis
- Reporting
- Business Analytics
- Machine Learning preprocessing

---

# 6. Folder 03 — Probability

## What is covered?

Probability provides the mathematical language for uncertainty.

Topics include:

- experiments,
- outcomes,
- sample spaces,
- events,
- conditional probability,
- independence,
- addition rule,
- multiplication rule,
- Bayes' theorem,
- random variables,
- expectation,
- variance,
- covariance,
- permutations,
- combinations.

## Where is it used?

Probability is fundamental to machine learning because predictions are often uncertain.

For example:

$$
P(Y=1\mid X)
$$

can represent the probability of a class given observed features.

Probability is used in:

- classification,
- Bayesian methods,
- probabilistic modelling,
- risk estimation,
- anomaly detection,
- decision-making,
- uncertainty estimation.

---

# 7. Folder 04 — Probability Distributions

## What is covered?

This folder studies probability distributions and how random variables behave.

Important distributions include:

- Bernoulli,
- Binomial,
- Poisson,
- Geometric,
- Negative Binomial,
- Hypergeometric,
- Uniform,
- Normal,
- Standard Normal,
- Exponential.

It also covers:

- PMF,
- PDF,
- CDF,
- expected value,
- variance,
- z-scores,
- Central Limit Theorem.

## Where is it used?

Probability distributions help us model different types of data and random events.

Examples:

| Situation | Possible distribution |
|---|---|
| Success/failure | Bernoulli |
| Number of successes | Binomial |
| Number of events in an interval | Poisson |
| Waiting time | Exponential |
| Continuous measurement | Normal |
| Sampling without replacement | Hypergeometric |

Understanding distributions is useful for:

- statistical inference,
- simulation,
- anomaly detection,
- probabilistic modelling,
- confidence intervals,
- hypothesis testing.

---

# 8. Folder 05 — Inferential Statistics

## What is covered?

Inferential statistics moves from describing observed data to making conclusions about a larger population.

Topics include:

- sampling distributions,
- standard error,
- point estimation,
- estimator properties,
- confidence intervals,
- margin of error,
- confidence levels,
- sample-size considerations,
- bootstrap confidence intervals.

## Where is it used?

Suppose we have data from 10,000 customers but want to understand the behaviour of millions of potential customers.

We cannot directly observe everyone.

Inference provides methods for estimating population quantities from samples.

It is useful for:

- experiments,
- surveys,
- scientific studies,
- business decisions,
- model analysis,
- uncertainty estimation.

---

# 9. Folder 06 — Hypothesis Testing

## What is covered?

Hypothesis testing provides a formal framework for evaluating statistical claims.

Topics include:

- null hypothesis,
- alternative hypothesis,
- significance level,
- test statistic,
- p-value,
- critical value,
- one-tailed tests,
- two-tailed tests,
- Type I error,
- Type II error,
- statistical power,
- common statistical tests.

## Where is it used?

Hypothesis testing can be used when comparing groups or evaluating whether observed evidence is compatible with a specified null hypothesis.

Examples:

- comparing two treatments,
- testing a population proportion,
- evaluating a difference between groups,
- analysing experimental results.

It should be used together with effect size and practical significance rather than relying only on a p-value.

---

# 10. Folder 07 — ANOVA

## What is covered?

ANOVA, or Analysis of Variance, is used to compare means across multiple groups.

Important concepts include:

- between-group variation,
- within-group variation,
- total variation,
- sums of squares,
- degrees of freedom,
- mean squares,
- F-statistic,
- F-distribution,
- ANOVA table,
- post-hoc tests,
- Tukey HSD,
- assumptions,
- effect sizes.

## Where is it used?

Suppose we want to compare the average performance of students from:

- Teaching Method A
- Teaching Method B
- Teaching Method C
- Teaching Method D

Instead of performing many pairwise tests, ANOVA provides an overall comparison.

It is useful in:

- experiments,
- A/B and multi-group experiments,
- business analysis,
- scientific research,
- comparing multiple groups.

---

# 11. Folder 08 — Chi-Square Test

## What is covered?

The Chi-Square section focuses on categorical data.

Topics include:

- observed frequency,
- expected frequency,
- goodness-of-fit,
- test of independence,
- test of homogeneity,
- contingency tables,
- degrees of freedom,
- residuals,
- Cramer's V,
- Phi coefficient,
- Yates' correction,
- Fisher's exact test.

## Where is it used?

Chi-Square methods are useful when working with categorical variables.

Examples:

```text
Gender × Product Preference
Education × Employment Status
Device Type × Purchase
Region × Customer Churn
```

It helps answer questions such as:

> Are these categorical variables statistically associated?

---

# 12. Folder 09 — Correlation

## What is covered?

Correlation studies the strength and direction of relationships between variables.

Topics include:

- covariance,
- Pearson correlation,
- Spearman correlation,
- correlation matrices,
- scatter plots,
- outliers,
- nonlinear relationships,
- interpretation of correlation.

## Where is it used?

Correlation is commonly used during exploratory analysis.

For example, we may examine whether:

$$
\text{Study Hours}
$$

and:

$$
\text{Exam Score}
$$

are associated.

It is also useful for identifying highly related features.

However:

$$
\boxed{
\text{Correlation does not imply causation.}
}
$$

---

# 13. Folder 10 — Regression

## What is covered?

Regression models relationships between variables and can be used for prediction.

Topics include:

- simple linear regression,
- slope,
- intercept,
- least squares,
- fitted values,
- residuals,
- prediction,
- multiple regression,
- categorical predictors,
- dummy variables,
- interaction terms,
- polynomial regression,
- transformations,
- regression assumptions.

## Where is it used?

Regression is used when the target is numerical.

Examples:

- predicting house prices,
- predicting sales,
- predicting temperature,
- predicting demand,
- estimating a numerical outcome.

A simple regression model can be written as:

$$
Y=\beta_0+\beta_1X+\varepsilon
$$

Regression is also an important foundation for understanding many machine-learning models.

---

# 14. Folder 11 — Regression Model Evaluation

## What is covered?

This folder focuses specifically on evaluating regression models.

Topics include:

- residuals,
- SSE,
- MSE,
- RMSE,
- MAE,
- MAPE,
- $R^2$,
- adjusted $R^2$,
- train/test performance,
- generalisation,
- cross-validation,
- residual analysis,
- model comparison,
- data leakage,
- baseline models.

## Where is it used?

After creating a regression model, we need to determine whether it actually performs well.

For example:

$$
RMSE=5000
$$

means something very different depending on whether the target represents:

- monthly income,
- house price,
- temperature,
- number of sales.

Therefore, model metrics must always be interpreted in context.

---

# 15. Folder 12 — Linear Algebra

## What is covered?

Linear algebra provides the mathematical language used to represent and manipulate multidimensional data.

Topics include:

- scalars,
- vectors,
- matrices,
- matrix operations,
- matrix multiplication,
- transpose,
- determinant,
- inverse,
- systems of equations,
- Gaussian elimination,
- rank,
- linear independence,
- span,
- basis,
- dot product,
- norms,
- distance,
- orthogonality,
- projections,
- eigenvalues,
- eigenvectors,
- diagonalisation,
- Singular Value Decomposition (SVD).

## Where is it used?

Machine-learning datasets are naturally represented as matrices.

For example:

$$
X\in\mathbb{R}^{n\times p}
$$

where:

- $n$ = number of observations,
- $p$ = number of features.

Linear algebra is used extensively in:

- linear regression,
- PCA,
- neural networks,
- recommendation systems,
- dimensionality reduction,
- optimisation,
- computer vision,
- natural language processing.

---

# 16. Folder 13 — Calculus

## What is covered?

Calculus studies change, rates of change, accumulation, and optimisation.

Topics include:

- functions,
- limits,
- continuity,
- derivatives,
- derivative rules,
- higher derivatives,
- critical points,
- optimisation,
- convexity,
- partial derivatives,
- gradients,
- directional derivatives,
- Hessians,
- integration,
- numerical integration.

## Where is it used?

Calculus becomes particularly important when understanding how machine-learning models learn.

A model often minimises a loss function:

$$
L(\theta)
$$

The gradient:

$$
\nabla L(\theta)
$$

describes the direction of greatest increase of the loss.

Optimisation algorithms can then use gradient information to search for parameters that reduce the loss.

Calculus is therefore an important mathematical foundation for:

- gradient descent,
- neural networks,
- optimisation,
- loss functions,
- backpropagation,
- continuous mathematical models.

---

# 17. Folder 14 — Bias and Variance

## What is covered?

This folder explains why a model may fail to generalise.

Topics include:

- estimator bias,
- estimator variance,
- standard error,
- MSE,
- bias-variance decomposition,
- consistency,
- efficiency,
- prediction bias,
- prediction variance,
- irreducible error,
- model complexity,
- underfitting,
- overfitting,
- regularisation,
- learning curves,
- bootstrap perspective.

A useful conceptual relationship is:

$$
\boxed{\text{Total Prediction Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}}
$$

## Where is it used?

Bias and variance are used to understand:

- underfitting,
- overfitting,
- model complexity,
- generalisation,
- training vs test performance,
- regularisation,
- model selection.

This is one of the most important statistical ideas for understanding why a model performs differently on training and unseen data.

---

# 18. Folder 15 — Statistics for Machine Learning

The final folder brings the most important statistical ideas together in a machine-learning workflow.

## What is covered?

Topics include:

- sampling and representativeness,
- feature distributions,
- standardisation,
- normalisation,
- skewness,
- outliers,
- missing data,
- data leakage,
- train/validation/test sets,
- cross-validation,
- class imbalance,
- classification metrics,
- probability thresholds,
- calibration,
- covariance,
- correlation,
- multicollinearity,
- confidence intervals,
- p-values,
- effect size,
- bootstrap,
- permutation testing,
- residual analysis,
- distribution shift,
- model comparison,
- uncertainty in model performance.

## Where is it used?

This knowledge is used directly while building machine-learning projects.

For example:

```text
Raw Dataset
     ↓
Understand Population
     ↓
Explore Data
     ↓
Check Distributions
     ↓
Handle Missing Values
     ↓
Detect Outliers
     ↓
Split Data
     ↓
Preprocess Without Leakage
     ↓
Train Model
     ↓
Cross-Validate
     ↓
Evaluate
     ↓
Understand Uncertainty
     ↓
Monitor Distribution Shift
```

This folder acts as the bridge between the statistical foundations in this section and the practical Machine Learning section of the repository.

---

# 19. Where Each Topic Is Used

| Topic | Main Use |
|---|---|
| Statistics Fundamentals | Understanding datasets and sampling |
| Descriptive Statistics | EDA and data summarisation |
| Probability | Uncertainty and probabilistic reasoning |
| Probability Distributions | Modelling random variables |
| Inferential Statistics | Estimation and uncertainty |
| Hypothesis Testing | Testing statistical claims |
| ANOVA | Comparing multiple group means |
| Chi-Square Test | Analysing categorical relationships |
| Correlation | Measuring linear association |
| Regression | Modelling and predicting numerical outcomes |
| Regression Evaluation | Measuring prediction performance |
| Linear Algebra | Representing and transforming multidimensional data |
| Calculus | Optimisation and learning algorithms |
| Bias and Variance | Understanding generalisation |
| Statistics for ML | Applying statistical reasoning throughout ML workflows |

---

# 20. How These Topics Connect

The topics are not isolated.

For example, consider a simple machine-learning project.

First, we use **Statistics Fundamentals** to understand the population, sample, and variables.

Then we use **Descriptive Statistics** to understand the dataset.

Probability helps us reason about uncertainty.

Probability distributions help us understand the behaviour of random variables.

Inferential statistics helps us estimate population quantities.

Hypothesis testing helps us evaluate statistical claims.

ANOVA and Chi-Square provide specialised methods for comparing groups and analysing categorical data.

Correlation helps us investigate relationships.

Regression provides a mathematical framework for modelling numerical outcomes.

Regression evaluation tells us whether the resulting model performs well.

Linear Algebra provides the mathematical representation required for many ML algorithms.

Calculus provides the mathematical foundation for optimisation.

Bias and Variance help explain generalisation and overfitting.

Finally, **Statistics for Machine Learning** brings these ideas together in practical modelling workflows.

---

# 21. Statistics Across the Data Science Workflow

Statistics appears throughout the complete Data Science workflow.

### 1. Data Collection

Statistics helps determine:

- what population to study,
- how to sample,
- how much data is needed,
- whether the sample is representative.

### 2. Data Cleaning

Statistics helps identify:

- unusual values,
- outliers,
- inconsistent measurements,
- missing-value patterns.

### 3. Exploratory Data Analysis

Statistics helps summarise:

- centre,
- spread,
- distribution,
- relationships,
- categorical frequencies.

### 4. Feature Engineering

Statistical ideas help with:

- scaling,
- transformations,
- correlation,
- redundancy,
- distributions.

### 5. Model Building

Probability, linear algebra, calculus, and statistical modelling provide mathematical foundations for algorithms.

### 6. Model Evaluation

Statistics helps determine:

- whether the evaluation is reliable,
- whether differences between models are meaningful,
- how uncertain performance estimates are.

### 7. Deployment

Statistical monitoring can detect:

- distribution shift,
- changing class proportions,
- changing relationships,
- performance degradation.

---

# 22. Mathematics vs Statistics vs Machine Learning

These areas overlap, but they have different roles.

| Area | Main Question |
|---|---|
| Mathematics | How can we represent and calculate relationships? |
| Statistics | What can we learn from data and uncertainty? |
| Machine Learning | How can we learn useful patterns for prediction or decision-making? |

For example:

### Mathematics

Vectors and matrices provide:

$$
X\beta
$$

### Statistics

We study uncertainty and relationships between:

$$
X \quad \text{and} \quad Y
$$

### Machine Learning

We use the data to construct a model:

$$
\hat{Y}=f(X)
$$

The three areas work together.

---

# 23. Recommended Study Method

For every folder, follow this sequence:

```text
1. Read README.md
        ↓
2. Understand the concepts
        ↓
3. Work through the mathematical examples
        ↓
4. Open the Jupyter Notebook
        ↓
5. Run the calculations
        ↓
6. Modify the examples
        ↓
7. Create your own examples
        ↓
8. Solve the practice questions
        ↓
9. Review Points to Remember
        ↓
10. Move to the next folder
```

Do not focus only on memorising formulas.

Try to understand:

> **What does the formula mean?**

> **Why is it needed?**

> **When should it be used?**

> **What assumptions does it make?**

> **How does the result affect a data or modelling decision?**

---

# 24. Recommended Order Before Machine Learning

Before starting serious Machine Learning implementation, it is recommended to have a comfortable understanding of:

### Statistics

- descriptive statistics,
- probability,
- probability distributions,
- inference,
- hypothesis testing,
- correlation,
- regression,
- bias and variance.

### Mathematics

- vectors,
- matrices,
- matrix operations,
- basic eigen concepts,
- derivatives,
- gradients,
- optimisation fundamentals.

You do not need to become a mathematician before starting Machine Learning.

However, understanding these foundations makes it much easier to understand **why ML algorithms work**, rather than only learning how to call them using Python libraries.

---

# 25. Repository Learning Path

The overall learning path can be viewed as:

**Python**

↓

**Mathematics and Statistics**

↓

**Data Analysis**

↓

**Machine Learning**

↓

**Deep Learning**

↓

**Generative AI**

↓

**Agentic AI**

This learning path moves from programming fundamentals to mathematical and statistical foundations, then into practical data analysis, machine learning, deep learning, and finally modern AI systems.

The Mathematics and Statistics section provides the foundation between programming and practical machine learning.
---

# 26. Final Perspective

The goal of this section is not to memorise a collection of formulas.

The real goal is to develop statistical and mathematical thinking.

When you see a dataset, you should be able to ask:

$$
\boxed{
\text{What does this data represent?}
}
$$

Then:

$$
\boxed{
\text{How is the data distributed?}
}
$$

Then:

$$
\boxed{
\text{What relationships exist?}
}
$$

Then:

$$
\boxed{
\text{How uncertain are my conclusions?}
}
$$

And finally:

$$
\boxed{
\text{Will the pattern generalise to new data?}
}
$$

That way of thinking is more important than memorising individual formulas.

---

# 27. Final Checklist

Before considering the Mathematics and Statistics section complete, you should be comfortable with:

- [ ] Population and sample
- [ ] Variables and measurement scales
- [ ] Sampling and sampling bias
- [ ] Mean, median, mode
- [ ] Variance and standard deviation
- [ ] Quartiles and percentiles
- [ ] Skewness and distributions
- [ ] Probability rules
- [ ] Conditional probability
- [ ] Bayes' theorem
- [ ] Random variables
- [ ] Probability distributions
- [ ] Expected value and variance
- [ ] Sampling distributions
- [ ] Confidence intervals
- [ ] Hypothesis testing
- [ ] p-values and significance
- [ ] ANOVA
- [ ] Chi-Square tests
- [ ] Covariance and correlation
- [ ] Linear regression
- [ ] Regression evaluation
- [ ] Vectors and matrices
- [ ] Eigenvalues and eigenvectors
- [ ] Derivatives and gradients
- [ ] Optimisation fundamentals
- [ ] Bias and variance
- [ ] Overfitting and underfitting
- [ ] Cross-validation
- [ ] Data leakage
- [ ] Class imbalance
- [ ] Calibration
- [ ] Distribution shift
- [ ] Statistical thinking in ML workflows

---

# 28. Conclusion

Mathematics and Statistics provide the foundation on which reliable Data Science and Machine Learning are built.

The 15 folders in this section move from basic statistical concepts to probability, inference, relationships, modelling, mathematical foundations, generalisation, and finally practical statistical reasoning for machine learning.

The progression is:

$$
\boxed{
\begin{aligned}
&\text{Understand Data}\\
&\downarrow\\
&\text{Describe Data}\\
&\downarrow\\
&\text{Understand Uncertainty}\\
&\downarrow\\
&\text{Make Statistical Inferences}\\
&\downarrow\\
&\text{Analyse Relationships}\\
&\downarrow\\
&\text{Build Mathematical Models}\\
&\downarrow\\
&\text{Evaluate Generalisation}\\
&\downarrow\\
&\text{Apply Statistics to Machine Learning}
\end{aligned}
}
$$

Once these foundations are comfortable, the Machine Learning section can focus more on **algorithms, implementation, experimentation, and real-world modelling**, because the mathematical and statistical reasoning required to understand those algorithms has already been developed here.

---

## References

- Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani — *An Introduction to Statistical Learning*
- Trevor Hastie, Robert Tibshirani, Jerome Friedman — *The Elements of Statistical Learning*
- Larry Wasserman — *All of Statistics*
- George Casella and Roger L. Berger — *Statistical Inference*
- MIT OpenCourseWare — Mathematics, Probability and Statistics resources
- Stanford University — Statistical Learning resources
- NumPy Documentation
- SciPy Documentation
- Scikit-learn Documentation
- Matplotlib Documentation

---

## Mathematical Formula Formatting

All equations in this section use GitHub-compatible LaTeX math delimiters:

- Use single dollar signs for inline expressions, such as $\mu$, $\sigma^2$, and $R^2$.
- Put important or multi-line equations on separate lines between `$$` delimiters.
- Use `\frac{a}{b}` for fractions, `\sum` for summations, and `\sqrt{}` for square roots.
- Keep explanatory prose outside display-math blocks so equations remain readable in GitHub's README renderer.
- Escape percentage signs inside math as `\%`. A raw `%` starts a LaTeX comment and can hide a closing brace, causing an “Extra open brace or missing close brace” error.
- Keep Markdown headings (for example, `### Continuous Probability`) on their own lines; never prefix a math block with `#`. Put equations on separate lines between `$` delimiters.

For details, see the [GitHub documentation for mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
