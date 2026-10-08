# Linear Algebra

Linear algebra is the branch of mathematics that studies **vectors, matrices, linear transformations, and systems of linear equations**.

It provides a mathematical language for representing collections of numerical values and for performing operations on structured data.

This chapter develops the linear algebra foundations required for quantitative computing. It begins with vectors and matrices and gradually moves toward matrix operations, systems of equations, determinants, inverse matrices, linear transformations, vector spaces, linear independence, basis, rank, eigenvalues, eigenvectors, and singular value decomposition.

The emphasis is on understanding what the mathematical objects mean, how their operations work, and how to perform the calculations correctly.

---

# 1. Learning Objectives

After completing this chapter, you should be able to:

1. Explain scalars, vectors, and matrices.
2. Distinguish row vectors and column vectors.
3. Perform vector addition and scalar multiplication.
4. Calculate vector magnitude and distance.
5. Understand dot products and their geometric meaning.
6. Calculate matrix dimensions.
7. Perform matrix addition and subtraction.
8. Perform scalar multiplication of matrices.
9. Perform matrix multiplication.
10. Understand transpose.
11. Understand symmetric matrices.
12. Represent systems of linear equations using matrices.
13. Solve simple systems using substitution and matrix methods.
14. Understand determinants.
15. Calculate the inverse of a matrix.
16. Understand identity matrices.
17. Explain linear transformations.
18. Understand vector spaces and subspaces.
19. Explain linear combinations and span.
20. Understand linear independence and dependence.
21. Understand basis and dimension.
22. Understand rank.
23. Explain orthogonality and orthonormality.
24. Understand projections.
25. Explain eigenvalues and eigenvectors.
26. Understand diagonalisation at a basic level.
27. Understand singular value decomposition.
28. Perform basic linear algebra operations using NumPy.

---

# 2. Scalars, Vectors, and Matrices

Linear algebra commonly works with three basic types of mathematical objects:

- scalars,
- vectors,
- matrices.

A **scalar** is a single number.

For example:

$$
5
$$

A **vector** is an ordered collection of numbers.

For example:

$$
\mathbf{x}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

A **matrix** is a rectangular arrangement of numbers.

For example:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

---

# 3. Scalars

A scalar contains only one value.

Examples:

$$
a=5
$$

$$
b=-2.5
$$

$$
c=\frac{3}{4}
$$

Scalars can be added, subtracted, multiplied, and divided according to ordinary arithmetic rules.

In linear algebra, scalars are often used to scale vectors and matrices.

---

# 4. Vectors

A vector is an ordered list of values.

A column vector can be written as:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

The vector has:

$$
n
$$

components.

For example:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
5\\
7
\end{bmatrix}
$$

has three components.

Its dimension is:

$$
\boxed{3}
$$

---

# 5. Row and Column Vectors

A row vector is written horizontally:

$$
\mathbf{x}
=
\begin{bmatrix}
1&2&3
\end{bmatrix}
$$

A column vector is written vertically:

$$
\mathbf{x}
=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

They contain the same numerical values but have different shapes.

The row vector has dimension:

$$
1\times3
$$

The column vector has dimension:

$$
3\times1
$$

Shape matters when performing matrix multiplication.

---

# 6. Vector Addition

Two vectors can be added when they have the same dimension.

Let:

$$
\mathbf{a}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

and:

$$
\mathbf{b}
=
\begin{bmatrix}
1\\
3\\
5
\end{bmatrix}
$$

Then:

$$
\mathbf{a}+\mathbf{b}
=
\begin{bmatrix}
2+1\\
4+3\\
6+5
\end{bmatrix}
$$

Therefore:

$$
\boxed{
\mathbf{a}+\mathbf{b}
=
\begin{bmatrix}
3\\
7\\
11
\end{bmatrix}}
$$

Vector addition is performed component by component.

---

# 7. Vector Subtraction

Using the same vectors:

$$
\mathbf{a}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

and:

$$
\mathbf{b}
=
\begin{bmatrix}
1\\
3\\
5
\end{bmatrix}
$$

we obtain:

$$
\mathbf{a}-\mathbf{b}
=
\begin{bmatrix}
2-1\\
4-3\\
6-5
\end{bmatrix}
$$

Thus:

$$
\boxed{
\mathbf{a}-\mathbf{b}
=
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}}
$$

---

# 8. Scalar Multiplication of a Vector

Suppose:

$$
\mathbf{x}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

and the scalar is:

$$
c=3
$$

Then:

$$
c\mathbf{x}
=
3
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

Multiply every component by 3:

$$
c\mathbf{x}
=
\begin{bmatrix}
6\\
12\\
18
\end{bmatrix}
$$

Therefore:

$$
\boxed{
3\mathbf{x}
=
\begin{bmatrix}
6\\
12\\
18
\end{bmatrix}}
$$

---

# 9. Zero Vector

The zero vector contains only zeros.

For a three-dimensional vector:

$$
\mathbf{0}
=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
$$

It acts as the additive identity:

$$
\mathbf{x}+\mathbf{0}=\mathbf{x}
$$

For example:

$$
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
+
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

---

# 10. Vector Magnitude

The magnitude or Euclidean norm of:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

is:

$$
\|\mathbf{x}\|
=
\sqrt{x_1^2+x_2^2+\cdots+x_n^2}
$$

For:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

we have:

$$
\|\mathbf{x}\|
=
\sqrt{3^2+4^2}
$$

$$
=
\sqrt{9+16}
$$

$$
=\sqrt{25}
$$

Therefore:

$$
\boxed{\|\mathbf{x}\|=5}
$$

---

# 11. Unit Vector

A unit vector has magnitude:

$$
1
$$

Given a non-zero vector $\mathbf{x}$, its unit vector in the same direction is:

$$
\hat{\mathbf{x}}
=
\frac{\mathbf{x}}{\|\mathbf{x}\|}
$$

For:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

and:

$$
\|\mathbf{x}\|=5
$$

we obtain:

$$
\hat{\mathbf{x}}
=
\frac{1}{5}
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Therefore:

$$
\boxed{
\hat{\mathbf{x}}
=
\begin{bmatrix}
0.6\\
0.8
\end{bmatrix}}
$$

---

# 12. Distance Between Two Vectors

The Euclidean distance between vectors $\mathbf{x}$ and $\mathbf{y}$ is:

$$
d(\mathbf{x},\mathbf{y})
=
\|\mathbf{x}-\mathbf{y}\|
$$

Suppose:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

and:

$$
\mathbf{y}
=
\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

Then:

$$
\mathbf{x}-\mathbf{y}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

Therefore:

$$
d(\mathbf{x},\mathbf{y})
=
\sqrt{2^2+3^2}
$$

$$
=
\sqrt{13}
$$

Thus:

$$
\boxed{d(\mathbf{x},\mathbf{y})=\sqrt{13}\approx3.606}
$$

---

# 13. Dot Product

The dot product of two vectors of the same dimension is:

$$
\mathbf{x}^{T}\mathbf{y}
=
\sum_{i=1}^{n}x_iy_i
$$

For:

$$
\mathbf{x}
=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

and:

$$
\mathbf{y}
=
\begin{bmatrix}
4\\
5\\
6
\end{bmatrix}
$$

we calculate:

$$
\mathbf{x}^{T}\mathbf{y}
=
(1)(4)+(2)(5)+(3)(6)
$$

$$
=4+10+18
$$

Therefore:

$$
\boxed{\mathbf{x}^{T}\mathbf{y}=32}
$$

---

# 14. Geometric Meaning of the Dot Product

The dot product can also be written as:

$$
\mathbf{x}^{T}\mathbf{y}
=
\|\mathbf{x}\|
\|\mathbf{y}\|
\cos\theta
$$

where $\theta$ is the angle between the vectors.

Therefore:

$$
\cos\theta
=
\frac{\mathbf{x}^{T}\mathbf{y}}
{\|\mathbf{x}\|\|\mathbf{y}\|}
$$

This relationship connects algebraic multiplication with geometry.

---

# 15. Orthogonal Vectors

Two non-zero vectors are orthogonal when their dot product is zero.

Thus:

$$
\mathbf{x}^{T}\mathbf{y}=0
$$

Suppose:

$$
\mathbf{x}
=
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

and:

$$
\mathbf{y}
=
\begin{bmatrix}
2\\
-1
\end{bmatrix}
$$

Then:

$$
\mathbf{x}^{T}\mathbf{y}
=
(1)(2)+(2)(-1)
$$

$$
=2-2
$$

$$
=0
$$

Therefore:

$$
\boxed{\mathbf{x}\perp\mathbf{y}}
$$

---

# 16. Matrices

A matrix is a rectangular arrangement of numbers.

For example:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

This matrix has:

- 2 rows,
- 3 columns.

Therefore, its order is:

$$
\boxed{2\times3}
$$

The first number represents rows and the second represents columns.

---

# 17. Matrix Elements

For a matrix $A$, the element in row $i$ and column $j$ is written:

$$
a_{ij}
$$

For:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

we have:

$$
a_{12}=2
$$

because it is in row 1, column 2.

Similarly:

$$
a_{23}=6
$$

---

# 18. Square Matrix

A matrix with the same number of rows and columns is called a **square matrix**.

For example:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

has order:

$$
2\times2
$$

Therefore, it is a square matrix.

---

# 19. Row Matrix

A matrix with one row is a row matrix.

Example:

$$
A=
\begin{bmatrix}
1&2&3&4
\end{bmatrix}
$$

Its order is:

$$
1\times4
$$

---

# 20. Column Matrix

A matrix with one column is a column matrix.

Example:

$$
A=
\begin{bmatrix}
1\\
2\\
3\\
4
\end{bmatrix}
$$

Its order is:

$$
4\times1
$$

---

# 21. Zero Matrix

A zero matrix contains only zeros.

For example:

$$
A=
\begin{bmatrix}
0&0\\
0&0
\end{bmatrix}
$$

It is the additive identity for matrices:

$$
A+0=A
$$

---

# 22. Identity Matrix

The identity matrix contains 1s on the main diagonal and 0s elsewhere.

For a $3\times3$ matrix:

$$
I=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{bmatrix}
$$

It satisfies:

$$
AI=IA=A
$$

whenever the dimensions permit the multiplication.

The identity matrix plays the same role in matrix multiplication that the number 1 plays in ordinary multiplication.

---

# 23. Diagonal Matrix

A diagonal matrix has non-zero values only on the main diagonal.

For example:

$$
D=
\begin{bmatrix}
2&0&0\\
0&5&0\\
0&0&7
\end{bmatrix}
$$

This is a diagonal matrix.

The identity matrix is a special diagonal matrix in which every diagonal element is 1.

---

# 24. Matrix Addition

Two matrices can be added only when they have the same dimensions.

Let:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

Then:

$$
A+B
=
\begin{bmatrix}
1+5&2+6\\
3+7&4+8
\end{bmatrix}
$$

Therefore:

$$
\boxed{
A+B=
\begin{bmatrix}
6&8\\
10&12
\end{bmatrix}}
$$

---

# 25. Matrix Subtraction

Using the same matrices:

$$
A-B
=
\begin{bmatrix}
1-5&2-6\\
3-7&4-8
\end{bmatrix}
$$

Thus:

$$
\boxed{
A-B=
\begin{bmatrix}
-4&-4\\
-4&-4
\end{bmatrix}}
$$

---

# 26. Scalar Multiplication of a Matrix

Let:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
c=3
$$

Then:

$$
3A=
\begin{bmatrix}
3&6\\
9&12
\end{bmatrix}
$$

Every element is multiplied by the scalar.

---

# 27. Matrix Multiplication

Matrix multiplication is different from element-by-element multiplication.

Suppose:

$$
A
$$

has dimensions:

$$
m\times n
$$

and:

$$
B
$$

has dimensions:

$$
n\times p
$$

Then:

$$
AB
$$

has dimensions:

$$
m\times p
$$

The inner dimensions must match.

$$
\boxed{(m\times n)(n\times p)=m\times p}
$$

---

# 28. Worked Matrix Multiplication

Let:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

Calculate $AB$.

The first element is:

$$
(1)(5)+(2)(7)
$$

$$
=5+14=19
$$

The second element is:

$$
(1)(6)+(2)(8)
$$

$$
=6+16=22
$$

The third element is:

$$
(3)(5)+(4)(7)
$$

$$
=15+28=43
$$

The fourth element is:

$$
(3)(6)+(4)(8)
$$

$$
=18+32=50
$$

Therefore:

$$
\boxed{
AB=
\begin{bmatrix}
19&22\\
43&50
\end{bmatrix}}
$$

---

# 29. Matrix Multiplication Is Not Generally Commutative

In ordinary arithmetic:

$$
ab=ba
$$

But for matrices:

$$
AB\ne BA
$$

in general.

The products may have different values or one product may exist while the other does not.

Therefore:

$$
\boxed{AB\neq BA\text{ in general}}
$$

---

# 30. Transpose of a Matrix

The transpose changes rows into columns.

If:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

then:

$$
A^T=
\begin{bmatrix}
1&4\\
2&5\\
3&6
\end{bmatrix}
$$

The dimensions change from:

$$
2\times3
$$

to:

$$
3\times2
$$

---

# 31. Properties of Transpose

Important properties include:

$$
(A^T)^T=A
$$

and:

$$
(A+B)^T=A^T+B^T
$$

For compatible matrices:

$$
(AB)^T=B^TA^T
$$

Notice the order reversal in the product.

---

# 32. Symmetric Matrix

A square matrix is symmetric if:

$$
A^T=A
$$

For example:

$$
A=
\begin{bmatrix}
2&3\\
3&5
\end{bmatrix}
$$

Its transpose is:

$$
A^T=
\begin{bmatrix}
2&3\\
3&5
\end{bmatrix}
$$

Therefore:

$$
\boxed{A^T=A}
$$

and $A$ is symmetric.

---

# 33. Systems of Linear Equations

Consider:

$$
2x+y=5
$$

and:

$$
x-y=1
$$

These equations can be represented using matrices.

The coefficient matrix is:

$$
A=
\begin{bmatrix}
2&1\\
1&-1
\end{bmatrix}
$$

The variable vector is:

$$
\mathbf{x}
=
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

The constant vector is:

$$
\mathbf{b}
=
\begin{bmatrix}
5\\
1
\end{bmatrix}
$$

Therefore:

$$
\boxed{A\mathbf{x}=\mathbf{b}}
$$

---

# 34. Solving a System by Substitution

Given:

$$
2x+y=5
$$

and:

$$
x-y=1
$$

From the second equation:

$$
x=y+1
$$

Substitute into the first equation:

$$
2(y+1)+y=5
$$

$$
2y+2+y=5
$$

$$
3y=3
$$

Therefore:

$$
y=1
$$

Then:

$$
x=1+1
$$

$$
x=2
$$

Hence:

$$
\boxed{x=2,\quad y=1}
$$

---

# 35. Determinant of a $2\times2$ Matrix

For:

$$
A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

the determinant is:

$$
\det(A)=ad-bc
$$

Consider:

$$
A=
\begin{bmatrix}
2&3\\
1&4
\end{bmatrix}
$$

Then:

$$
\det(A)
=
(2)(4)-(3)(1)
$$

$$
=8-3
$$

Therefore:

$$
\boxed{\det(A)=5}
$$

---

# 36. Meaning of a Determinant

The determinant provides important information about a square matrix.

If:

$$
\det(A)=0
$$

the matrix is **singular** and does not have an ordinary inverse.

If:

$$
\det(A)\ne0
$$

the matrix is **non-singular** and is invertible.

For a two-dimensional transformation, the absolute value of the determinant also represents the factor by which areas are scaled.

---

# 37. Inverse Matrix

For a square matrix $A$, an inverse $A^{-1}$ satisfies:

$$
AA^{-1}=A^{-1}A=I
$$

The inverse exists only when the matrix is invertible.

For:

$$
A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

with:

$$
ad-bc\ne0
$$

the inverse is:

$$
A^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d&-b\\
-c&a
\end{bmatrix}
$$

---

# 38. Worked Example: Matrix Inverse

Let:

$$
A=
\begin{bmatrix}
2&3\\
1&4
\end{bmatrix}
$$

We already calculated:

$$
\det(A)=5
$$

Therefore:

$$
A^{-1}
=
\frac{1}{5}
\begin{bmatrix}
4&-3\\
-1&2
\end{bmatrix}
$$

Hence:

$$
\boxed{
A^{-1}
=
\begin{bmatrix}
0.8&-0.6\\
-0.2&0.4
\end{bmatrix}}
$$

---

# 39. Solving a Matrix Equation Using an Inverse

For:

$$
A\mathbf{x}=\mathbf{b}
$$

if $A$ is invertible:

$$
A^{-1}A\mathbf{x}=A^{-1}\mathbf{b}
$$

Since:

$$
A^{-1}A=I
$$

we obtain:

$$
\boxed{\mathbf{x}=A^{-1}\mathbf{b}}
$$

This is a mathematical method for solving a linear system.

In numerical computing, however, explicitly calculating an inverse is often less preferable than using a dedicated linear-system solver.

---

# 40. Rank of a Matrix

The **rank** of a matrix is the maximum number of linearly independent rows or columns.

For example:

$$
A=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
$$

The second row is:

$$
2
\begin{bmatrix}
1&2
\end{bmatrix}
$$

Therefore, the rows are linearly dependent.

There is only one independent row.

Hence:

$$
\boxed{\operatorname{rank}(A)=1}
$$

---

# 41. Full Rank

For an $m\times n$ matrix, the rank cannot exceed:

$$
\min(m,n)
$$

A matrix has **full column rank** if:

$$
\operatorname{rank}(A)=n
$$

when it has $n$ columns.

A square $n\times n$ matrix has full rank when:

$$
\operatorname{rank}(A)=n
$$

For a square matrix:

$$
\det(A)\ne0
$$

is equivalent to full rank.

---

# 42. Linear Combination

A linear combination of vectors $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_k$ is:

$$
c_1\mathbf{v}_1+
c_2\mathbf{v}_2+
\cdots+
c_k\mathbf{v}_k
$$

where the $c_i$ values are scalars.

For:

$$
\mathbf{v}_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

and:

$$
\mathbf{v}_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

we can form:

$$
3\mathbf{v}_1+4\mathbf{v}_2
$$

$$
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

---

# 43. Span

The **span** of a collection of vectors is the set of all linear combinations of those vectors.

The standard basis vectors:

$$
\mathbf{e}_1=
\begin{bmatrix}
1\\
0
\end{bmatrix},
\qquad
\mathbf{e}_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

span $\mathbb{R}^2$ because every vector:

$$
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

can be written as:

$$
x\mathbf{e}_1+y\mathbf{e}_2
$$

---

# 44. Linear Independence

Vectors are linearly independent if the equation:

$$
c_1\mathbf{v}_1+
c_2\mathbf{v}_2+
\cdots+
c_k\mathbf{v}_k
=
\mathbf{0}
$$

has only the trivial solution:

$$
c_1=c_2=\cdots=c_k=0
$$

If a non-zero combination produces the zero vector, the vectors are linearly dependent.

---

# 45. Example of Linear Dependence

Let:

$$
\mathbf{v}_1=
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

and:

$$
\mathbf{v}_2=
\begin{bmatrix}
2\\
4
\end{bmatrix}
$$

We can write:

$$
\mathbf{v}_2=2\mathbf{v}_1
$$

Therefore, one vector is a scalar multiple of the other.

Hence:

$$
\boxed{\mathbf{v}_1,\mathbf{v}_2\text{ are linearly dependent}}
$$

---

# 46. Basis

A basis of a vector space is a set of vectors that:

1. spans the space, and
2. is linearly independent.

The standard basis of $\mathbb{R}^3$ is:

$$
\mathbf{e}_1=
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix},
\quad
\mathbf{e}_2=
\begin{bmatrix}
0\\
1\\
0
\end{bmatrix},
\quad
\mathbf{e}_3=
\begin{bmatrix}
0\\
0\\
1
\end{bmatrix}
$$

These vectors span $\mathbb{R}^3$ and are linearly independent.

---

# 47. Dimension

The dimension of a vector space is the number of vectors in any basis of that space.

Therefore:

$$
\dim(\mathbb{R}^2)=2
$$

and:

$$
\dim(\mathbb{R}^3)=3
$$

For a matrix, rank is related to the dimension of its column space and row space.

---

# 48. Vector Space

A vector space is a set of vectors that is closed under vector addition and scalar multiplication and satisfies the required vector-space axioms.

Examples include:

$$
\mathbb{R}^2
$$

and:

$$
\mathbb{R}^3
$$

The important idea is that vectors in the space can be added together and multiplied by scalars without leaving the space.

---

# 49. Subspace

A subspace is a subset of a vector space that is itself a vector space under the same operations.

For a subset $W$ of a vector space $V$, a basic test is:

1. $\mathbf{0}\in W$,
2. if $\mathbf{u},\mathbf{v}\in W$, then $\mathbf{u}+\mathbf{v}\in W$,
3. if $\mathbf{u}\in W$ and $c$ is a scalar, then $c\mathbf{u}\in W$.

A line through the origin in $\mathbb{R}^2$ is an example of a subspace.

---

# 50. Column Space

The **column space** of a matrix is the span of its columns.

For:

$$
A=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
$$

the columns are:

$$
\begin{bmatrix}
1\\
0
\end{bmatrix},
\quad
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

These span:

$$
\mathbb{R}^2
$$

Therefore:

$$
\operatorname{Col}(A)=\mathbb{R}^2
$$

---

# 51. Null Space

The **null space** of a matrix $A$ is the set of all vectors $\mathbf{x}$ satisfying:

$$
A\mathbf{x}=\mathbf{0}
$$

For:

$$
A=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
$$

we solve:

$$
A
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

The first equation is:

$$
x+2y=0
$$

so:

$$
x=-2y
$$

Let:

$$
y=t
$$

Then:

$$
\mathbf{x}
=
\begin{bmatrix}
-2t\\
t
\end{bmatrix}
=
t
\begin{bmatrix}
-2\\
1
\end{bmatrix}
$$

Therefore the null space is:

$$
\boxed{
\operatorname{Null}(A)
=
\operatorname{span}
\left\{
\begin{bmatrix}
-2\\
1
\end{bmatrix}
\right\}}
$$

---

# 52. Rank-Nullity Theorem

For a matrix $A$ with $n$ columns:

$$
\boxed{
\operatorname{rank}(A)
+
\operatorname{nullity}(A)
=
n
}
$$

Here:

- rank = dimension of the column space,
- nullity = dimension of the null space,
- $n$ = number of columns.

For the previous $2\times2$ matrix:

$$
\operatorname{rank}(A)=1
$$

and:

$$
\operatorname{nullity}(A)=1
$$

Therefore:

$$
1+1=2
$$

which agrees with the number of columns.

---

# 53. Orthogonality

Two vectors are orthogonal when:

$$
\mathbf{x}^{T}\mathbf{y}=0
$$

Orthogonality is the higher-dimensional generalisation of perpendicular directions.

An orthonormal set contains vectors that are:

1. mutually orthogonal, and
2. each of unit length.

Thus:

$$
\mathbf{q}_i^T\mathbf{q}_j
=
\begin{cases}
1,&i=j\\
0,&i\ne j
\end{cases}
$$

---

# 54. Projection of One Vector Onto Another

The projection of $\mathbf{x}$ onto a non-zero vector $\mathbf{u}$ is:

$$
\operatorname{proj}_{\mathbf{u}}\mathbf{x}
=
\frac{\mathbf{x}^{T}\mathbf{u}}
{\mathbf{u}^{T}\mathbf{u}}
\mathbf{u}
$$

Consider:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

and:

$$
\mathbf{u}
=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

Then:

$$
\mathbf{x}^{T}\mathbf{u}=3
$$

and:

$$
\mathbf{u}^{T}\mathbf{u}=1
$$

Therefore:

$$
\operatorname{proj}_{\mathbf{u}}\mathbf{x}
=
3
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

Thus:

$$
\boxed{
\operatorname{proj}_{\mathbf{u}}\mathbf{x}
=
\begin{bmatrix}
3\\
0
\end{bmatrix}}
$$

---

# 55. Orthogonal Decomposition

A vector can be decomposed into:

- a component parallel to a subspace,
- a component orthogonal to that subspace.

For a projection onto vector $\mathbf{u}$:

$$
\mathbf{x}
=
\operatorname{proj}_{\mathbf{u}}\mathbf{x}
+
\mathbf{r}
$$

where:

$$
\mathbf{r}
$$

is orthogonal to $\mathbf{u}$.

Therefore:

$$
\mathbf{u}^{T}\mathbf{r}=0
$$

This idea is central to many least-squares and projection calculations.

---

# 56. Linear Transformation

A transformation $T$ is linear if:

$$
T(\mathbf{u}+\mathbf{v})
=
T(\mathbf{u})+T(\mathbf{v})
$$

and:

$$
T(c\mathbf{u})
=
cT(\mathbf{u})
$$

for vectors $\mathbf{u},\mathbf{v}$ and scalar $c$.

A matrix can represent a linear transformation.

For example:

$$
T(\mathbf{x})=A\mathbf{x}
$$

---

# 57. Matrix as a Transformation

Let:

$$
A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
$$

and:

$$
\mathbf{x}
=
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

Then:

$$
A\mathbf{x}
=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
2\\
6
\end{bmatrix}
$$

The transformation stretches the first coordinate by 2 and the second coordinate by 3.

---

# 58. Eigenvectors and Eigenvalues

For a square matrix $A$, a non-zero vector $\mathbf{v}$ is an eigenvector if:

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

where:

- $\mathbf{v}$ = eigenvector,
- $\lambda$ = eigenvalue.

The transformation changes the length and possibly the direction sign of an eigenvector but does not rotate it away from its eigen-direction.

---

# 59. Finding Eigenvalues

Eigenvalues satisfy:

$$
\det(A-\lambda I)=0
$$

Consider:

$$
A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
$$

Then:

$$
A-\lambda I
=
\begin{bmatrix}
2-\lambda&0\\
0&3-\lambda
\end{bmatrix}
$$

The determinant is:

$$
(2-\lambda)(3-\lambda)
$$

Set equal to zero:

$$
(2-\lambda)(3-\lambda)=0
$$

Therefore:

$$
\lambda=2
$$

or:

$$
\lambda=3
$$

Hence:

$$
\boxed{\lambda_1=2,\quad\lambda_2=3}
$$

---

# 60. Finding an Eigenvector

For:

$$
\lambda=2
$$

solve:

$$
(A-2I)\mathbf{v}=0
$$

We obtain:

$$
\begin{bmatrix}
0&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
v_1\\
v_2
\end{bmatrix}
=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

This gives:

$$
v_2=0
$$

Choose:

$$
v_1=1
$$

Then:

$$
\boxed{
\mathbf{v}
=
\begin{bmatrix}
1\\
0
\end{bmatrix}}
$$

is an eigenvector associated with $\lambda=2$.

---

# 61. Diagonalisation

A matrix may be diagonalised when it has a sufficient number of linearly independent eigenvectors.

The diagonalisation can be written:

$$
A=PDP^{-1}
$$

where:

- $P$ contains eigenvectors,
- $D$ is a diagonal matrix of eigenvalues.

Diagonal matrices are often easier to work with because their powers and many other operations are simpler.

---

# 62. Singular Value Decomposition

The **Singular Value Decomposition (SVD)** decomposes a matrix as:

$$
\boxed{
A=U\Sigma V^T
}
$$

where:

- $U$ contains left singular vectors,
- $\Sigma$ contains singular values,
- $V$ contains right singular vectors.

For an $m\times n$ matrix, the dimensions are:

$$
U:m\times m
$$

$$
\Sigma:m\times n
$$

$$
V:n\times n
$$

for the full SVD.

The singular values are non-negative.

---

# 63. Singular Values

The singular values of $A$ are related to the eigenvalues of:

$$
A^TA
$$

If:

$$
\lambda_i
$$

is an eigenvalue of $A^TA$, then the corresponding singular value is:

$$
\sigma_i=\sqrt{\lambda_i}
$$

The singular values are usually arranged in descending order:

$$
\sigma_1\ge\sigma_2\ge\cdots\ge0
$$

---

# 64. Matrix Norm

The Frobenius norm of a matrix is:

$$
\|A\|_F
=
\sqrt{
\sum_{i=1}^{m}
\sum_{j=1}^{n}
a_{ij}^2
}
$$

For:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

we obtain:

$$
\|A\|_F
=
\sqrt{1^2+2^2+3^2+4^2}
$$

$$
=
\sqrt{1+4+9+16}
$$

$$
=\sqrt{30}
$$

Therefore:

$$
\boxed{\|A\|_F=\sqrt{30}}
$$

---

# 65. Distance and Norm

For vectors:

$$
\mathbf{x},\mathbf{y}
$$

the Euclidean distance is:

$$
\|\mathbf{x}-\mathbf{y}\|_2
$$

The Euclidean norm is:

$$
\|\mathbf{x}\|_2
=
\sqrt{\mathbf{x}^T\mathbf{x}}
$$

Thus:

$$
\boxed{
d(\mathbf{x},\mathbf{y})
=
\|\mathbf{x}-\mathbf{y}\|_2
}
$$

This gives a compact matrix notation for ordinary Euclidean distance.

---

# 66. Matrix Trace

The trace of a square matrix is the sum of its diagonal elements.

For:

$$
A=
\begin{bmatrix}
2&1\\
3&5
\end{bmatrix}
$$

the trace is:

$$
\operatorname{tr}(A)=2+5
$$

Therefore:

$$
\boxed{\operatorname{tr}(A)=7}
$$

For a square matrix, the trace also equals the sum of its eigenvalues, counting algebraic multiplicity.

---

# 67. Determinant and Eigenvalues

For a square matrix, the determinant equals the product of its eigenvalues:

$$
\boxed{
\det(A)=\prod_i\lambda_i
}
$$

The trace equals their sum:

$$
\boxed{
\operatorname{tr}(A)=\sum_i\lambda_i
}
$$

For:

$$
A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
$$

the eigenvalues are 2 and 3.

Therefore:

$$
\det(A)=2(3)=6
$$

and:

$$
\operatorname{tr}(A)=2+3=5
$$

---

# 68. Matrix Rank and Determinant

For an $n\times n$ matrix:

$$
\det(A)\ne0
$$

if and only if:

$$
\operatorname{rank}(A)=n
$$

Such a matrix is full rank and invertible.

If:

$$
\det(A)=0
$$

then:

$$
\operatorname{rank}(A)<n
$$

and the matrix is singular.

---

# 69. Gaussian Elimination

Gaussian elimination is a systematic method for solving systems of linear equations and reducing matrices.

The basic row operations are:

1. interchange two rows,
2. multiply a row by a non-zero scalar,
3. add a multiple of one row to another row.

These operations can transform a system into an equivalent form that is easier to solve.

---

# 70. Row-Echelon Form

A matrix is in row-echelon form when its non-zero rows are arranged with leading entries moving to the right as we move downward, and entries below each leading entry are zero.

The process can be used to identify:

- rank,
- independent equations,
- solutions to systems.

Reduced row-echelon form goes further by making each pivot the only non-zero value in its column.

---

# 71. Solving a System Using an Augmented Matrix

Consider:

$$
x+y=5
$$

$$
2x+y=7
$$

The augmented matrix is:

$$
\left[
\begin{array}{cc|c}
1&1&5\\
2&1&7
\end{array}
\right]
$$

Replace row 2 with:

$$
R_2\leftarrow R_2-2R_1
$$

Then:

$$
\left[
\begin{array}{cc|c}
1&1&5\\
0&-1&-3
\end{array}
\right]
$$

Thus:

$$
-y=-3
$$

so:

$$
y=3
$$

Substitute into:

$$
x+y=5
$$

to obtain:

$$
x+3=5
$$

Therefore:

$$
x=2
$$

Hence:

$$
\boxed{x=2,\quad y=3}
$$

---

# 72. Consistent and Inconsistent Systems

A system is **consistent** if it has at least one solution.

It is **inconsistent** if it has no solution.

A consistent system may have:

- exactly one solution,
- infinitely many solutions.

For example:

$$
x+y=2
$$

and:

$$
2x+2y=4
$$

represent the same line, so there are infinitely many solutions.

---

# 73. Homogeneous Systems

A homogeneous linear system has the form:

$$
A\mathbf{x}=\mathbf{0}
$$

It always has at least the trivial solution:

$$
\mathbf{x}=\mathbf{0}
$$

If the matrix has a non-trivial null space, additional non-zero solutions also exist.

---

# 74. Positive Definite Matrices

A symmetric matrix $A$ is positive definite if:

$$
\mathbf{x}^TA\mathbf{x}>0
$$

for every non-zero vector $\mathbf{x}$.

Positive definite matrices have important properties, including strictly positive eigenvalues.

For example:

$$
A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
$$

gives:

$$
\mathbf{x}^TA\mathbf{x}
=
2x_1^2+3x_2^2
$$

which is positive for every non-zero $\mathbf{x}$.

---

# 75. Covariance Matrices

A covariance matrix is a square matrix describing pairwise covariance among variables.

For variables:

$$
X_1,X_2,\ldots,X_p
$$

the covariance matrix can be represented as:

$$
\Sigma=
\begin{bmatrix}
\operatorname{Var}(X_1)&\operatorname{Cov}(X_1,X_2)&\cdots\\
\operatorname{Cov}(X_2,X_1)&\operatorname{Var}(X_2)&\cdots\\
\vdots&\vdots&\ddots
\end{bmatrix}
$$

A covariance matrix is symmetric because:

$$
\operatorname{Cov}(X_i,X_j)
=
\operatorname{Cov}(X_j,X_i)
$$

---

# 76. Important Matrix Properties

Some important properties are:

### Associative multiplication

$$
(AB)C=A(BC)
$$

when the products are defined.

### Distributive property

$$
A(B+C)=AB+AC
$$

and:

$$
(A+B)C=AC+BC
$$

### Identity

$$
AI=IA=A
$$

### Transpose of product

$$
(AB)^T=B^TA^T
$$

### Inverse of product

For invertible matrices:

$$
(AB)^{-1}=B^{-1}A^{-1}
$$

The order is reversed.

---

# 77. Common Mistakes

### Mistake 1: Ignoring dimensions

Always check matrix dimensions before multiplication.

### Mistake 2: Assuming $AB=BA$

Matrix multiplication is not generally commutative.

### Mistake 3: Confusing transpose with inverse

In general:

$$
A^T\ne A^{-1}
$$

### Mistake 4: Calculating an inverse without checking invertibility

An inverse exists only when:

$$
\det(A)\ne0
$$

for a square matrix.

### Mistake 5: Confusing dot product with element-wise multiplication

The dot product produces a scalar, while element-wise multiplication produces a vector of the same shape.

### Mistake 6: Assuming every set of vectors is independent

Scalar multiples and other linear combinations can create dependence.

### Mistake 7: Forgetting that eigenvectors must be non-zero

The zero vector is not considered an eigenvector.

### Mistake 8: Confusing rank with number of rows

Rank measures independent directions, not simply the number of rows.

---

# 78. NumPy: Creating Vectors

```python
import numpy as np

x = np.array([1, 2, 3])

print(x)
print(x.shape)
```

The shape is:

```python
(3,)
```

For an explicit column vector:

```python
x_column = np.array([[1], [2], [3]])

print(x_column.shape)
```

The shape is:

```python
(3, 1)
```

---

# 79. NumPy: Vector Operations

```python
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print(a + b)
print(a - b)
print(3 * a)
```

Dot product:

```python
dot_product = np.dot(a, b)

print(dot_product)
```

---

# 80. NumPy: Vector Norm

```python
x = np.array([3, 4])

norm = np.linalg.norm(x)

print(norm)
```

The result is:

$$
\boxed{5}
$$

---

# 81. NumPy: Creating Matrices

```python
A = np.array([
    [1, 2],
    [3, 4]
])

print(A)
print(A.shape)
```

The matrix has shape:

```python
(2, 2)
```

---

# 82. NumPy: Matrix Multiplication

Use `@` for matrix multiplication:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A @ B

print(C)
```

This is different from:

```python
A * B
```

which performs element-wise multiplication.

---

# 83. NumPy: Transpose and Determinant

```python
A = np.array([
    [2, 3],
    [1, 4]
])

print(A.T)
print(np.linalg.det(A))
```

The determinant is:

$$
\boxed{5}
$$

---

# 84. NumPy: Solving a Linear System

Rather than explicitly calculating an inverse, NumPy can directly solve:

$$
A\mathbf{x}=\mathbf{b}
$$

using:

```python
A = np.array([
    [2, 1],
    [1, -1]
])

b = np.array([5, 1])

x = np.linalg.solve(A, b)

print(x)
```

The solution is:

$$
\boxed{
\mathbf{x}
=
\begin{bmatrix}
2\\
1
\end{bmatrix}}
$$

---

# 85. NumPy: Matrix Inverse

```python
A = np.array([
    [2, 3],
    [1, 4]
])

A_inverse = np.linalg.inv(A)

print(A_inverse)
```

For numerical problems, direct linear-system solvers are generally preferred when the goal is only to solve:

$$
A\mathbf{x}=\mathbf{b}
$$

rather than explicitly needing $A^{-1}$.

---

# 86. NumPy: Eigenvalues and Eigenvectors

```python
A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
```

The eigenvalues are:

$$
\boxed{2,\ 3}
$$

up to numerical representation and ordering.

---

# 87. NumPy: Singular Value Decomposition

```python
A = np.array([
    [1, 2],
    [3, 4]
])

U, S, VT = np.linalg.svd(A)

print("U:")
print(U)

print("Singular values:")
print(S)

print("V^T:")
print(VT)
```

The decomposition follows:

$$
A=U\Sigma V^T
$$

within numerical precision.

---

# 88. A Complete Linear Algebra Example

Consider:

$$
A=
\begin{bmatrix}
2&1\\
1&3
\end{bmatrix}
$$

### Step 1: Determinant

$$
\det(A)
=
(2)(3)-(1)(1)
$$

$$
=6-1
$$

$$
\boxed{\det(A)=5}
$$

Since:

$$
\det(A)\ne0
$$

the matrix is invertible.

### Step 2: Inverse

$$
A^{-1}
=
\frac{1}{5}
\begin{bmatrix}
3&-1\\
-1&2
\end{bmatrix}
$$

### Step 3: Solve

Suppose:

$$
A\mathbf{x}
=
\begin{bmatrix}
5\\
7
\end{bmatrix}
$$

Then:

$$
\mathbf{x}=A^{-1}\mathbf{b}
$$

$$
=
\frac{1}{5}
\begin{bmatrix}
3&-1\\
-1&2
\end{bmatrix}
\begin{bmatrix}
5\\
7
\end{bmatrix}
$$

First component:

$$
\frac{15-7}{5}
=
\frac{8}{5}
$$

Second component:

$$
\frac{-5+14}{5}
=
\frac{9}{5}
$$

Therefore:

$$
\boxed{
\mathbf{x}
=
\begin{bmatrix}
1.6\\
1.8
\end{bmatrix}}
$$

---

# 89. Linear Algebra in Data Tables

A rectangular numerical dataset can be represented as a matrix.

Suppose five observations have three numerical variables:

$$
X=
\begin{bmatrix}
x_{11}&x_{12}&x_{13}\\
x_{21}&x_{22}&x_{23}\\
x_{31}&x_{32}&x_{33}\\
x_{41}&x_{42}&x_{43}\\
x_{51}&x_{52}&x_{53}
\end{bmatrix}
$$

The matrix has:

$$
5
$$

rows and:

$$
3
$$

columns.

Rows can represent observations and columns can represent variables, provided that this convention is defined for the analysis.

---

# 90. Matrix-Vector Multiplication

Suppose:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
\mathbf{x}
=
\begin{bmatrix}
5\\
6
\end{bmatrix}
$$

Then:

$$
A\mathbf{x}
=
\begin{bmatrix}
1(5)+2(6)\\
3(5)+4(6)
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
5+12\\
15+24
\end{bmatrix}
$$

Therefore:

$$
\boxed{
A\mathbf{x}
=
\begin{bmatrix}
17\\
39
\end{bmatrix}}
$$

---

# 91. Matrix Representation of Multiple Equations

A collection of linear equations can be written compactly as:

$$
A\mathbf{x}=\mathbf{b}
$$

This notation replaces a long list of equations with three mathematical objects:

- coefficient matrix $A$,
- unknown vector $\mathbf{x}$,
- constant vector $\mathbf{b}$.

This representation is one of the main reasons matrices are so useful in quantitative mathematics.

---

# 92. Important Formula Summary

### Vector norm

$$
\|\mathbf{x}\|_2
=
\sqrt{\sum_i x_i^2}
$$

### Euclidean distance

$$
d(\mathbf{x},\mathbf{y})
=
\|\mathbf{x}-\mathbf{y}\|_2
$$

### Dot product

$$
\mathbf{x}^T\mathbf{y}
=
\sum_i x_iy_i
$$

### Angle between vectors

$$
\cos\theta
=
\frac{\mathbf{x}^T\mathbf{y}}
{\|\mathbf{x}\|\|\mathbf{y}\|}
$$

### Matrix multiplication dimensions

$$
(m\times n)(n\times p)=m\times p
$$

### Determinant of $2\times2$

$$
\det
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
=
ad-bc
$$

### Matrix inverse of $2\times2$

$$
A^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d&-b\\
-c&a
\end{bmatrix}
$$

### Matrix equation

$$
A\mathbf{x}=\mathbf{b}
$$

### Solution using inverse

$$
\mathbf{x}=A^{-1}\mathbf{b}
$$

when $A^{-1}$ exists.

### Linear combination

$$
\sum_i c_i\mathbf{v}_i
$$

### Rank-nullity theorem

$$
\operatorname{rank}(A)+\operatorname{nullity}(A)=n
$$

for a matrix with $n$ columns.

### Orthogonality

$$
\mathbf{x}^T\mathbf{y}=0
$$

### Projection

$$
\operatorname{proj}_{\mathbf{u}}\mathbf{x}
=
\frac{\mathbf{x}^T\mathbf{u}}
{\mathbf{u}^T\mathbf{u}}
\mathbf{u}
$$

### Eigenvalue equation

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

### Characteristic equation

$$
\det(A-\lambda I)=0
$$

### Diagonalisation

$$
A=PDP^{-1}
$$

### SVD

$$
A=U\Sigma V^T
$$

### Frobenius norm

$$
\|A\|_F
=
\sqrt{\sum_i\sum_j a_{ij}^2}
$$

---

# 93. Quick Concept Comparison

| Concept | Meaning |
|---|---|
| Scalar | Single number |
| Vector | Ordered collection of numbers |
| Matrix | Rectangular array of numbers |
| Norm | Size or length of a vector |
| Dot product | Scalar product of two vectors |
| Orthogonal | Dot product equals zero |
| Matrix multiplication | Row-by-column multiplication |
| Transpose | Rows become columns |
| Identity matrix | Multiplicative identity for matrices |
| Determinant | Scalar describing important properties of a square matrix |
| Inverse | Matrix that produces identity when multiplied by the original |
| Rank | Number of independent directions represented by a matrix |
| Null space | Vectors mapped to zero |
| Span | All linear combinations of given vectors |
| Basis | Independent spanning set |
| Eigenvector | Direction preserved by a transformation |
| Eigenvalue | Scaling factor associated with an eigenvector |
| SVD | Factorisation into singular-vector matrices and singular values |

---

# 94. Points to Remember

1. Scalars are single numerical values.
2. Vectors are ordered collections of values.
3. Matrices are rectangular arrays.
4. Vector addition requires equal dimensions.
5. Matrix addition requires equal dimensions.
6. Matrix multiplication requires matching inner dimensions.
7. Matrix multiplication is not generally commutative.
8. The transpose changes rows into columns.
9. A square matrix is invertible when its determinant is non-zero.
10. Rank measures the number of independent directions.
11. Linear combinations use scalar multiples of vectors.
12. A basis must span the space and be linearly independent.
13. Orthogonal vectors have zero dot product.
14. Eigenvectors satisfy:
    $$
    A\mathbf{v}=\lambda\mathbf{v}
    $$
15. Eigenvalues can be found from:
    $$
    \det(A-\lambda I)=0
    $$
16. The null space contains vectors satisfying:
    $$
    A\mathbf{x}=\mathbf{0}
    $$
17. The rank-nullity theorem connects rank and nullity.
18. SVD decomposes a matrix as:
    $$
    A=U\Sigma V^T
    $$
19. Matrix dimensions should always be checked before multiplication.
20. NumPy provides efficient implementations of common linear algebra operations.

---

# 95. Chapter Summary

Linear algebra provides a structured language for working with numerical quantities.

Vectors represent ordered collections of values, while matrices represent rectangular collections of values and transformations.

The dot product provides both an algebraic operation and a geometric interpretation through the angle between vectors.

Matrices can be added, multiplied, transposed, and, when appropriate, inverted. Systems of linear equations can be written compactly as:

$$
A\mathbf{x}=\mathbf{b}
$$

The determinant helps determine whether a square matrix is invertible. Rank describes the number of independent directions represented by a matrix, while the null space describes vectors mapped to zero.

Vector spaces, spans, bases, and linear independence provide the theoretical structure behind linear algebra.

Orthogonality and projection describe geometric relationships between vectors. Eigenvalues and eigenvectors identify directions that a matrix transformation preserves up to scaling.

Finally, SVD provides a powerful matrix decomposition:

$$
A=U\Sigma V^T
$$

The central idea is:

$$
\boxed{
\text{Linear Algebra}
=
\text{Vectors}
+
\text{Matrices}
+
\text{Transformations}
+
\text{Structure}
}
$$

A strong understanding of these foundations makes later mathematical and computational topics much easier to understand.

---

# 96. References

- Gilbert Strang, *Introduction to Linear Algebra*.
- David C. Lay, Steven R. Lay, Judi J. McDonald, *Linear Algebra and Its Applications*.
- OpenStax, *Contemporary Mathematics* and related mathematical resources.
- MIT OpenCourseWare, Linear Algebra.
- NumPy Documentation, `numpy.linalg`.
- SciPy Documentation, Linear Algebra.
- GeeksforGeeks, educational resources on linear algebra.
