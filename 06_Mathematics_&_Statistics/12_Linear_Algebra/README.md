# Linear Algebra

Linear Algebra is a branch of mathematics that studies vectors, matrices, linear equations, and linear transformations. It provides the mathematical foundation for many algorithms used in Data Science, Machine Learning, Deep Learning, and Artificial Intelligence.

In Data Science, datasets are represented as matrices, observations can be represented as vectors, and model calculations frequently use matrix multiplication. Linear Algebra is also important in Linear Regression, Principal Component Analysis (PCA), neural networks, recommendation systems, and dimensionality reduction.

This chapter covers the essential Linear Algebra concepts required for Data Science and Machine Learning, with mathematical explanations, worked examples, and Python implementations using NumPy.

## 1. Learning Objectives

After completing this chapter, you should be able to:

1. Understand scalars, vectors, and matrices.
2. Perform vector and matrix operations.
3. Calculate vector norms, distances, and dot products.
4. Understand matrix multiplication and transpose.
5. Represent and solve systems of linear equations.
6. Understand determinants, inverse matrices, and matrix rank.
7. Explain linear independence, span, and basis.
8. Understand orthogonality and projections.
9. Understand eigenvalues and eigenvectors.
10. Explain Singular Value Decomposition (SVD).
11. Understand covariance matrices.
12. Apply Linear Algebra using NumPy.
13. Identify how Linear Algebra is used in Machine Learning.

## 2. Scalars, Vectors, and Matrices

Linear Algebra works with three fundamental mathematical objects: scalars, vectors, and matrices.

### 2.1 Scalars

A **scalar** is a single numerical value.

Examples:

$$
a = 5,\qquad b = -2.5,\qquad c = \frac{3}{4}
$$

Scalars are used to represent individual quantities and multiply vectors or matrices.

### 2.2 Vectors

A **vector** is an ordered collection of numerical values.

For example:

$$
\mathbf{x} = (3,5,7)
$$

This vector contains three components and belongs to three-dimensional space, denoted by $\mathbb{R}^3$.

In Data Science, a vector can represent the features of one observation, such as age, income, and years of experience.

A vector with $n$ components belongs to $\mathbb{R}^n$.

### 2.3 Matrices

A **matrix** is a rectangular arrangement of numerical values.

For example, matrix $A$ is:

```text
A = [[1, 2, 3],
     [4, 5, 6]]
```

It has two rows and three columns. Its shape is $2 \times 3$.

A dataset containing $m$ observations and $n$ features can be represented by a matrix with shape $m \times n$.

Here, rows represent observations and columns represent features.

### Python Implementation

```python
import numpy as np

scalar = 5

vector = np.array([3, 5, 7])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Scalar:", scalar)
print("Vector:", vector)
print("Vector shape:", vector.shape)
print("Matrix:\n", matrix)
print("Matrix shape:", matrix.shape)
```

**Important:** A NumPy array with shape `(3,)` is a one-dimensional array. An array with shape `(3, 1)` is an explicit column vector. Their shapes can affect mathematical operations.

## 3. Vector Operations

### 3.1 Vector Addition and Subtraction

Two vectors can be added or subtracted when they have the same dimensions. The operations are performed component by component.

Suppose:

$$
\mathbf{a} = (2,4,6)
$$

$$
\mathbf{b} = (1,3,5)
$$

Their sum is:

$$
\mathbf{a}+\mathbf{b}=(3,7,11)
$$

Their difference is:

$$
\mathbf{a}-\mathbf{b}=(1,1,1)
$$

### 3.2 Scalar Multiplication

Scalar multiplication multiplies every component of a vector by the same number.

For $\mathbf{x}=(2,4,6)$:

$$
3\mathbf{x}=(6,12,18)
$$

### Python Implementation

```python
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Scalar multiplication:", 3 * a)
```

Vector operations are useful when manipulating feature values, model coefficients, and numerical representations.

## 4. Vector Norm, Unit Vector, and Distance

### 4.1 Euclidean Norm

The **Euclidean norm** measures the length or magnitude of a vector.

For a vector with components $x_1,x_2,\ldots,x_n$:

$$
\|\mathbf{x}\|_2 = \sqrt{x_1^2+x_2^2+\cdots+x_n^2}
$$

Consider the vector $\mathbf{x}=(3,4)$.

Its magnitude is:

$$
\|\mathbf{x}\|_2 = \sqrt{3^2+4^2}
$$

$$
\|\mathbf{x}\|_2 = \sqrt{25}=5
$$

### 4.2 Unit Vector

A **unit vector** has a magnitude equal to $1$.

For a non-zero vector, its unit vector is obtained by dividing the vector by its magnitude.

$$
\hat{\mathbf{x}}=\frac{\mathbf{x}}{\|\mathbf{x}\|_2}
$$

For $\mathbf{x}=(3,4)$, the magnitude is $5$.

Therefore:

$$
\hat{\mathbf{x}}=(0.6,0.8)
$$

The resulting vector has a magnitude of $1$.

The zero vector cannot be normalised using this formula because its magnitude is zero.

### 4.3 Euclidean Distance

Euclidean distance measures the straight-line distance between two vectors.

$$
d(\mathbf{x},\mathbf{y})=\|\mathbf{x}-\mathbf{y}\|_2
$$

Suppose:

$$
\mathbf{x}=(3,4),\qquad \mathbf{y}=(1,1)
$$

The difference is:

$$
\mathbf{x}-\mathbf{y}=(2,3)
$$

Therefore:

$$
d(\mathbf{x},\mathbf{y})=\sqrt{2^2+3^2}
$$

$$
d(\mathbf{x},\mathbf{y})=\sqrt{13}\approx3.606
$$

Euclidean distance is used in K-Means clustering, nearest-neighbour algorithms, and similarity analysis. Feature scaling may be necessary when features have very different numerical ranges.

### Python Implementation

```python
x = np.array([3, 4])
y = np.array([1, 1])

norm = np.linalg.norm(x)
unit_vector = x / norm
distance = np.linalg.norm(x - y)

print("Norm:", norm)
print("Unit vector:", unit_vector)
print("Distance:", distance)
```

## 5. Dot Product and Orthogonality

### 5.1 Dot Product

The **dot product** multiplies corresponding components of two vectors and adds the results.

$$
\mathbf{x}^T\mathbf{y}=\sum_{i=1}^{n}x_i y_i
$$

Suppose:

$$
\mathbf{x}=(1,2,3)
$$

$$
\mathbf{y}=(4,5,6)
$$

Then:

$$
\mathbf{x}^T\mathbf{y}=(1)(4)+(2)(5)+(3)(6)
$$

$$
\mathbf{x}^T\mathbf{y}=32
$$

The dot product produces a scalar.

### 5.2 Angle Between Vectors

The dot product is related to the angle between two non-zero vectors.

$$
\cos\theta=
\frac{\mathbf{x}^T\mathbf{y}}
{\|\mathbf{x}\|_2\|\mathbf{y}\|_2}
$$

This relationship is the foundation of **cosine similarity**, which is widely used to compare text embeddings and other vector representations.

### 5.3 Orthogonal Vectors

Two vectors are orthogonal when their dot product is zero.

$$
\mathbf{x}^T\mathbf{y}=0
$$

For example, let $\mathbf{x}=(1,2)$ and $\mathbf{y}=(2,-1)$.

$$
\mathbf{x}^T\mathbf{y}=(1)(2)+(2)(-1)=0
$$

Therefore, the vectors are orthogonal.

### Python Implementation

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

dot_product = np.dot(x, y)

cosine_similarity = (
    np.dot(x, y)
    / (np.linalg.norm(x) * np.linalg.norm(y))
)

print("Dot product:", dot_product)
print("Cosine similarity:", cosine_similarity)
```

Cosine similarity requires both vectors to be non-zero.

## 6. Matrix Operations

### 6.1 Matrix Addition and Subtraction

Matrices can be added or subtracted only when their shapes match.

Suppose:

```text
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

Their sum is:

```text
A + B = [[6, 8],
         [10, 12]]
```

Their difference is:

```text
A - B = [[-4, -4],
         [-4, -4]]
```

### 6.2 Identity Matrix

An identity matrix contains ones on its main diagonal and zeros elsewhere.

For example:

```text
I = [[1, 0],
     [0, 1]]
```

For a compatible matrix $A$:

$$
AI=IA=A
$$

The identity matrix plays the role of $1$ in matrix multiplication.

### 6.3 Matrix Multiplication

Matrix multiplication follows the row-by-column rule.

If $A$ has shape $m \times n$ and $B$ has shape $n \times p$, the product has shape $m \times p$.

$$
(m\times n)(n\times p)=m\times p
$$

The inner dimensions must match.

Consider:

```text
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

The product is:

```text
AB = [[19, 22],
      [43, 50]]
```

For example, the first element is calculated as:

$$
(1)(5)+(2)(7)=19
$$

**Matrix multiplication is not generally commutative.**

$$
AB\ne BA
$$

The order of multiplication matters.

### 6.4 Matrix Multiplication Versus Element-Wise Multiplication

In NumPy, `A @ B` performs matrix multiplication, while `A * B` performs element-wise multiplication.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Addition:\n", A + B)
print("Matrix multiplication:\n", A @ B)
print("Element-wise multiplication:\n", A * B)
print("Transpose:\n", A.T)
```

Matrix operations form the computational foundation of regression models, neural networks, and many other Machine Learning algorithms.

## 7. Transpose of a Matrix

The **transpose** exchanges the rows and columns of a matrix.

For example:

```text
A = [[1, 2, 3],
     [4, 5, 6]]
```

Its transpose is:

```text
A.T = [[1, 4],
       [2, 5],
       [3, 6]]
```

The shape changes from $2\times3$ to $3\times2$.

Important properties include:

$$
(A^T)^T=A
$$

$$
(AB)^T=B^TA^T
$$

Notice that the order reverses when taking the transpose of a product.

In NumPy, the transpose is obtained using `A.T`.

## 8. Systems of Linear Equations

A system of linear equations contains equations involving unknown variables.

Consider:

$$
2x+y=5
$$

$$
x-y=1
$$

These equations can be represented in matrix form as:

$$
A\mathbf{x}=\mathbf{b}
$$

where:

```text
A = [[2, 1],
     [1, -1]]

x = (x, y)

b = (5, 1)
```

From the second equation:

$$
x=y+1
$$

Substituting into the first equation:

$$
2(y+1)+y=5
$$

$$
3y+2=5
$$

Therefore:

$$
y=1,\qquad x=2
$$

The solution is:

$$
\mathbf{x}=(2,1)^T
$$

### Gaussian Elimination

Gaussian elimination solves systems of linear equations using elementary row operations.

The allowed operations are:

1. Interchange two rows.
2. Multiply a row by a non-zero scalar.
3. Add a multiple of one row to another row.

These operations simplify the system until the unknown variables can be determined.

A system may have:

- One unique solution.
- Infinitely many solutions.
- No solution.

### Python Implementation

```python
A = np.array([
    [2, 1],
    [1, -1]
], dtype=float)

b = np.array([5, 1], dtype=float)

solution = np.linalg.solve(A, b)

print("Solution:", solution)
print("Verification:", A @ solution)
```

`np.linalg.solve()` is generally preferable to calculating an inverse when the goal is to solve a linear system.

## 9. Determinants and Inverse Matrices

### 9.1 Determinant of a 2 × 2 Matrix

For the matrix

```text
A = [[a, b],
     [c, d]]
```

the determinant is:

$$
\det(A)=ad-bc
$$

Consider:

```text
A = [[2, 3],
     [1, 4]]
```

Then:

$$
\det(A)=(2)(4)-(3)(1)=5
$$

### 9.2 Meaning of the Determinant

The determinant provides important information about a square matrix.

- If $\det(A)=0$, the matrix is singular and has no ordinary inverse.
- If $\det(A)\ne0$, the matrix is invertible.
- The absolute value of the determinant represents the area-scaling factor for a two-dimensional linear transformation.

### 9.3 Inverse Matrix

For a $2\times2$ matrix:

```text
A = [[a, b],
     [c, d]]
```

when $ad-bc\ne0$, its inverse is:

$$
A^{-1}=\frac{1}{ad-bc}
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
$$

An inverse satisfies:

$$
AA^{-1}=A^{-1}A=I
$$

If a matrix is invertible, the equation $A\mathbf{x}=\mathbf{b}$ can be expressed as:

$$
\mathbf{x}=A^{-1}\mathbf{b}
$$

However, when solving a linear system in Python, using `np.linalg.solve()` is generally more appropriate than explicitly calculating the inverse.

### Python Implementation

```python
A = np.array([
    [2, 3],
    [1, 4]
], dtype=float)

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Determinant:", determinant)
print("Inverse:\n", inverse)
print("Identity check:\n", A @ inverse)
```

## 10. Linear Independence, Span, and Basis

### 10.1 Linear Combination

A linear combination is formed by multiplying vectors by scalars and adding the results.

For vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$:

$$
c_1\mathbf{v}_1+c_2\mathbf{v}_2+\cdots+c_k\mathbf{v}_k
$$

where $c_1,c_2,\ldots,c_k$ are scalars.

For example, let $\mathbf{v}_1=(1,0)$ and $\mathbf{v}_2=(0,1)$.

$$
3\mathbf{v}_1+4\mathbf{v}_2=(3,4)
$$

### 10.2 Span

The **span** of a collection of vectors is the set of all possible linear combinations of those vectors.

The vectors $(1,0)$ and $(0,1)$ span $\mathbb{R}^2$, because every vector $(x,y)$ can be represented as:

$$
(x,y)=x(1,0)+y(0,1)
$$

### 10.3 Linear Independence

Vectors are linearly independent if a linear combination can equal the zero vector only when all its coefficients are zero.

For example:

$$
\mathbf{v}_1=(1,2),\qquad \mathbf{v}_2=(2,4)
$$

Since $\mathbf{v}_2=2\mathbf{v}_1$, these vectors are linearly dependent.

Linear independence is important in understanding redundant features and multicollinearity in datasets.

### 10.4 Basis and Dimension

A **basis** is a set of linearly independent vectors that spans a vector space.

The standard basis of $\mathbb{R}^2$ is $(1,0)$ and $(0,1)$.

The dimension of a vector space is the number of vectors in its basis.

Therefore:

$$
\dim(\mathbb{R}^2)=2
$$

$$
\dim(\mathbb{R}^3)=3
$$

These concepts help explain the number of independent directions represented by numerical data.

## 11. Rank, Column Space, and Null Space

### 11.1 Rank of a Matrix

The **rank** of a matrix is the number of linearly independent columns. It is also equal to the number of linearly independent rows.

Consider:

```text
A = [[1, 2],
     [2, 4]]
```

The second row is twice the first row. Therefore, the matrix has only one independent row.

$$
\mathrm{rank}(A)=1
$$

For a matrix with $m$ rows and $n$ columns:

$$
\mathrm{rank}(A)\leq\min(m,n)
$$

Rank helps identify redundant features and understand whether a system of linear equations has a unique solution.

### 11.2 Column Space

The column space is the span of the columns of a matrix.

It describes all vectors that can be produced by multiplying the matrix by an appropriate input vector.

### 11.3 Null Space

The null space contains all vectors that a matrix maps to the zero vector.

$$
\mathrm{Null}(A)=\{\mathbf{x}:A\mathbf{x}=\mathbf{0}\}
$$

Consider:

```text
A = [[1, 2],
     [2, 4]]
```

To find the null space, solve:

$$
x+2y=0
$$

Therefore, $x=-2y$.

Letting $y=t$ gives:

$$
\mathbf{x}=t(-2,1)
$$

Thus, the null space is the span of $(-2,1)$.

### 11.4 Rank-Nullity Theorem

For a matrix with $n$ columns:

$$
\mathrm{rank}(A)+\mathrm{nullity}(A)=n
$$

The nullity is the dimension of the null space.

For the example above, the rank is $1$ and the nullity is $1$. Their sum equals the number of columns, which is $2$.

### Python Implementation

```python
A = np.array([
    [1, 2],
    [2, 4]
], dtype=float)

rank = np.linalg.matrix_rank(A)

print("Rank:", rank)

U, S, VT = np.linalg.svd(A)

print("Singular values:", S)
```

Numerical rank is estimated using floating-point tolerances.

## 12. Orthogonality and Projection

### 12.1 Orthogonality

Two vectors are orthogonal when their dot product is zero.

$$
\mathbf{x}^T\mathbf{y}=0
$$

Orthogonality is important in least-squares regression, projections, and numerical methods.

### 12.2 Projection of a Vector

The projection of a vector $\mathbf{x}$ onto a non-zero vector $\mathbf{u}$ is:

$$
\mathrm{proj}_{\mathbf{u}}(\mathbf{x})=
\frac{\mathbf{x}^T\mathbf{u}}{\mathbf{u}^T\mathbf{u}}\mathbf{u}
$$

Suppose:

$$
\mathbf{x}=(3,4),\qquad \mathbf{u}=(1,0)
$$

The dot products are:

$$
\mathbf{x}^T\mathbf{u}=3
$$

$$
\mathbf{u}^T\mathbf{u}=1
$$

Therefore, the projection is:

$$
\mathrm{proj}_{\mathbf{u}}(\mathbf{x})=(3,0)
$$

The projection represents the component of $\mathbf{x}$ in the direction of $\mathbf{u}$.

### Application in Machine Learning

Projection is useful in least-squares regression, where observed values are approximated by values that can be represented using the model's feature matrix.

## 13. Eigenvalues and Eigenvectors

### 13.1 Definition

For a square matrix $A$, a non-zero vector $\mathbf{v}$ is an eigenvector if:

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

Here, $\lambda$ is the corresponding eigenvalue.

An eigenvector represents a direction that remains unchanged under the transformation, apart from scaling or possible reversal.

### 13.2 Finding Eigenvalues

Eigenvalues satisfy the characteristic equation:

$$
\det(A-\lambda I)=0
$$

Consider the diagonal matrix:

```text
A = [[2, 0],
     [0, 3]]
```

Then:

$$
\det(A-\lambda I)=(2-\lambda)(3-\lambda)=0
$$

Therefore, the eigenvalues are:

$$
\lambda_1=2,\qquad\lambda_2=3
$$

### 13.3 Finding Eigenvectors

For $\lambda=2$, solve:

$$
(A-2I)\mathbf{v}=\mathbf{0}
$$

One valid eigenvector is:

$$
\mathbf{v}=(1,0)
$$

Any non-zero scalar multiple of this vector is also an eigenvector for the same eigenvalue.

### 13.4 Applications in Data Science

Eigenvalues and eigenvectors are important in:

- Principal Component Analysis (PCA).
- Dimensionality reduction.
- Covariance matrix analysis.
- Understanding important directions in numerical data.
- Certain optimisation and graph algorithms.

### Python Implementation

```python
A = np.array([
    [2, 0],
    [0, 3]
], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

NumPy returns eigenvectors as columns of the eigenvector matrix. The order of the eigenvalues is not guaranteed.

## 14. Singular Value Decomposition (SVD)

Singular Value Decomposition is a matrix factorisation that works for square and rectangular matrices.

The decomposition is:

$$
A=U\Sigma V^T
$$

Here:

- $U$ contains the left singular vectors.
- $\Sigma$ contains the singular values.
- $V$ contains the right singular vectors.

The singular values are non-negative and are conventionally arranged from largest to smallest.

### 14.1 Relationship Between SVD and Eigenvalues

The squared singular values of a matrix are the eigenvalues of $A^TA$.

If $\lambda_i$ is an eigenvalue of $A^TA$, then:

$$
\sigma_i=\sqrt{\lambda_i}
$$

### 14.2 Applications of SVD

SVD is used in:

- Dimensionality reduction.
- Low-rank matrix approximation.
- Data compression.
- Recommendation systems.
- Noise reduction.
- Latent semantic analysis.

In dimensionality reduction, retaining the largest singular values can provide a lower-dimensional representation of the original data.

### Python Implementation

```python
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=float)

U, S, VT = np.linalg.svd(A, full_matrices=False)

print("U shape:", U.shape)
print("Singular values:", S)
print("VT shape:", VT.shape)

A_reconstructed = U @ np.diag(S) @ VT

print("Reconstructed matrix:\n", A_reconstructed)
print("Reconstruction is close:",
      np.allclose(A, A_reconstructed))
```

SVD is particularly useful when working with large numerical datasets and dimensionality-reduction techniques.

## 15. Covariance Matrices

A covariance matrix describes the variances of individual variables and the covariances between pairs of variables.

For two variables $X$ and $Y$, covariance measures how they vary together.

- Positive covariance indicates that the variables tend to move in the same direction.
- Negative covariance indicates that they tend to move in opposite directions.
- Covariance near zero indicates little linear co-variation, although a nonlinear relationship may still exist.

For variables $X_1$ and $X_2$, the covariance matrix is:

```text
Sigma = [[Var(X1),       Cov(X1, X2)],
         [Cov(X2, X1),   Var(X2)]]
```

A covariance matrix is symmetric and positive semidefinite.

### Python Implementation

```python
data = np.array([
    [2, 4],
    [3, 5],
    [4, 7],
    [5, 8]
], dtype=float)

covariance_matrix = np.cov(data, rowvar=False)

print("Covariance matrix:\n", covariance_matrix)
print("Symmetric:",
      np.allclose(covariance_matrix, covariance_matrix.T))
```

Here, each row represents an observation and each column represents a variable. NumPy's default covariance calculation uses the sample covariance denominator, $n-1$.

Covariance matrices are important in PCA, statistical modelling, and multivariate data analysis.

## 16. Linear Algebra in Machine Learning

Linear Algebra is used throughout the Machine Learning workflow.

### 16.1 Dataset Representation

A dataset containing $m$ observations and $n$ features can be represented as:

$$
X\in\mathbb{R}^{m\times n}
$$

Each row represents an observation and each column represents a feature.

### 16.2 Linear Regression

A linear regression model can be expressed as:

$$
\hat{\mathbf{y}}=X\boldsymbol{\beta}
$$

Here:

- $X$ is the feature matrix.
- $\boldsymbol{\beta}$ contains the model coefficients.
- $\hat{\mathbf{y}}$ contains the predicted values.

An intercept can be included by adding a column of ones to the feature matrix.

The least-squares objective is to minimise:

$$
\|X\boldsymbol{\beta}-\mathbf{y}\|_2^2
$$

This expression represents the sum of squared differences between predictions and actual values.

### 16.3 Neural Networks

A dense neural-network layer commonly uses a matrix multiplication followed by a bias addition:

$$
Z=XW+\mathbf{b}
$$

An activation function is then applied to the resulting values.

Matrix multiplication enables neural networks to process many observations efficiently.

### 16.4 Dimensionality Reduction

PCA uses directions associated with high variance to represent data in fewer dimensions. Eigenvalue analysis and SVD provide important mathematical tools for this process.

### 16.5 Clustering and Similarity

Vector distances and dot products are used in clustering and similarity-based algorithms.

Examples include:

- Euclidean distance in K-Means.
- Distance calculations in nearest-neighbour algorithms.
- Cosine similarity in text embeddings.

### 16.6 Recommendation Systems

Recommendation systems can represent users and items using vectors or matrices. Matrix factorisation techniques use lower-dimensional representations to discover patterns in user-item interactions.

## 17. Complete NumPy Practice Example

The following example combines matrix creation, matrix multiplication, solving a linear system, calculating eigenvalues, and performing SVD.

```python
import numpy as np

# Create a matrix and a vector
A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

b = np.array([5, 7], dtype=float)

# Inspect dimensions
print("Matrix shape:", A.shape)
print("Vector shape:", b.shape)

# Calculate determinant
print("Determinant:", np.linalg.det(A))

# Solve A x = b
solution = np.linalg.solve(A, b)
print("Solution:", solution)

# Verify the solution
print("Verification:", A @ solution)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A, full_matrices=False)

print("Singular values:", S)

# Reconstruct the matrix
A_reconstructed = U @ np.diag(S) @ VT

print("Reconstructed matrix:\n", A_reconstructed)
print("Reconstruction is close:",
      np.allclose(A, A_reconstructed))
```

This example demonstrates how NumPy implements Linear Algebra operations without requiring manual calculations for every step.

## 18. Common Mistakes

### Mistake 1: Ignoring Matrix Dimensions

The number of columns in the first matrix must equal the number of rows in the second matrix for matrix multiplication.

### Mistake 2: Assuming Matrix Multiplication Is Commutative

In general:

$$
AB\ne BA
$$

The order of matrices matters.

### Mistake 3: Confusing Transpose and Inverse

The transpose exchanges rows and columns. The inverse produces the identity when multiplied by the original matrix.

They are not generally equal.

### Mistake 4: Inverting a Singular Matrix

An ordinary inverse exists only for a square matrix with a non-zero determinant.

### Mistake 5: Confusing Dot Product and Element-Wise Multiplication

The dot product of two vectors produces a scalar. Element-wise multiplication produces corresponding products.

### Mistake 6: Ignoring Numerical Precision

Computer calculations use finite-precision arithmetic. Use `np.allclose()` when checking whether floating-point results are approximately equal.

### Mistake 7: Using Explicit Inversion Unnecessarily

When solving a system $A\mathbf{x}=\mathbf{b}$, prefer `np.linalg.solve()` instead of calculating the inverse solely to solve the system.

## 19. Important Formula Summary

**Euclidean norm**

$$
\|\mathbf{x}\|_2=\sqrt{\sum_i x_i^2}
$$

**Unit vector**

$$
\hat{\mathbf{x}}=\frac{\mathbf{x}}{\|\mathbf{x}\|_2}
$$

**Euclidean distance**

$$
d(\mathbf{x},\mathbf{y})=\|\mathbf{x}-\mathbf{y}\|_2
$$

**Dot product**

$$
\mathbf{x}^T\mathbf{y}=\sum_i x_i y_i
$$

**Cosine similarity**

$$
\cos\theta=
\frac{\mathbf{x}^T\mathbf{y}}
{\|\mathbf{x}\|_2\|\mathbf{y}\|_2}
$$

**Matrix multiplication dimensions**

$$
(m\times n)(n\times p)=m\times p
$$

**Transpose of a product**

$$
(AB)^T=B^TA^T
$$

**Determinant of a 2 × 2 matrix**

$$
\det(A)=ad-bc
$$

**Inverse of a 2 × 2 matrix**

For $A=[[a,b],[c,d]]$ and $ad-bc\ne0$:

$$
A^{-1}=\frac{1}{ad-bc}
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
$$

**Linear system**

$$
A\mathbf{x}=\mathbf{b}
$$

**Rank-nullity theorem**

$$
\mathrm{rank}(A)+\mathrm{nullity}(A)=n
$$

Here, $n$ is the number of columns.

**Orthogonality**

$$
\mathbf{x}^T\mathbf{y}=0
$$

**Projection**

$$
\mathrm{proj}_{\mathbf{u}}(\mathbf{x})=
\frac{\mathbf{x}^T\mathbf{u}}
{\mathbf{u}^T\mathbf{u}}\mathbf{u}
$$

The vector $\mathbf{u}$ must be non-zero.

**Eigenvalue equation**

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

**Characteristic equation**

$$
\det(A-\lambda I)=0
$$

**Singular Value Decomposition**

$$
A=U\Sigma V^T
$$

**Linear regression prediction**

$$
\hat{\mathbf{y}}=X\boldsymbol{\beta}
$$

**Neural-network linear layer**

$$
Z=XW+\mathbf{b}
$$

## 20. Points to Remember

1. Scalars represent individual numerical values, vectors represent ordered collections, and matrices represent rectangular arrays.
2. Vector addition requires vectors with matching dimensions.
3. Matrix multiplication requires compatible inner dimensions.
4. Matrix multiplication is generally not commutative.
5. Vector norms measure magnitude, while distances measure separation between vectors.
6. The dot product is useful for understanding angles and cosine similarity.
7. A square matrix is invertible if and only if its determinant is non-zero.
8. Rank measures the number of independent directions represented by a matrix.
9. A basis must span a vector space and be linearly independent.
10. The null space contains vectors mapped to zero by a matrix.
11. Eigenvectors satisfy the eigenvalue equation.
12. SVD is useful for dimensionality reduction and matrix factorisation.
13. Covariance matrices describe variances and relationships between numerical variables.
14. NumPy provides efficient implementations of Linear Algebra operations.
15. Linear Algebra is fundamental to regression, neural networks, clustering, PCA, and recommendation systems.

## 21. Chapter Summary

Linear Algebra provides the mathematical foundation for representing and manipulating numerical data. Vectors represent ordered values, while matrices organise data into rows and columns.

Vector operations, norms, distances, and dot products describe numerical and geometric relationships. Matrix operations and systems of linear equations provide a structured approach to solving mathematical problems.

Determinants, inverses, rank, and null spaces help explain the structure of matrices and the solutions of linear systems. Linear independence, span, and basis describe how vectors represent mathematical spaces.

Eigenvalues, eigenvectors, and Singular Value Decomposition provide tools for understanding transformations and reducing the dimensionality of numerical data. Covariance matrices connect Linear Algebra with Statistics and Machine Learning.

The central idea is that **Linear Algebra connects numerical data, mathematical structure, and efficient computation**. These concepts are essential for understanding Machine Learning, Deep Learning, and AI algorithms.

## 22. References

- Gilbert Strang, *Introduction to Linear Algebra*.
- David C. Lay, Steven R. Lay, and Judi J. McDonald, *Linear Algebra and Its Applications*.
- MIT OpenCourseWare, Linear Algebra.
- NumPy documentation: [Linear Algebra (`numpy.linalg`)](https://numpy.org/doc/stable/reference/routines.linalg.html).
- SciPy documentation: [Linear Algebra (`scipy.linalg`)](https://docs.scipy.org/doc/scipy/reference/linalg.html).
- GeeksforGeeks: [Linear Algebra](https://www.geeksforgeeks.org/maths/linear-algebra/).

## 23. Related Topics

- [Descriptive Statistics](../02_Descriptive_Statistics/README.md)
- [Correlation](../09_Correlation/README.md)
- [Regression](../10_Regression/README.md)
- [Regression Model Evaluation](../11_Regression_Model_Evaluation/README.md)
- [Statistics for Machine Learning](../15_Statistics_for_Machine_Learning/README.md)
