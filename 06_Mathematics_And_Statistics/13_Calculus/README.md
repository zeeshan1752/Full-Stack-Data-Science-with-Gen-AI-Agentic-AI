# Calculus

Calculus is a branch of mathematics that studies **change, rates of change, and accumulation**. It provides important mathematical foundations for Machine Learning, Deep Learning, optimisation, and statistical modelling.

The two main branches of calculus are differentiation and integration. Differentiation helps us understand how a quantity changes, while integration helps us calculate accumulated quantities.

In Machine Learning, calculus is particularly important for understanding gradients, loss functions, gradient descent, and backpropagation.

## 1. Learning Objectives

After completing this chapter, you should be able to:

1. Understand functions, limits, and continuity.
2. Calculate derivatives using basic differentiation rules.
3. Understand partial derivatives and gradients.
4. Apply derivatives to optimisation problems.
5. Understand gradient descent and its role in Machine Learning.
6. Understand the chain rule and its role in backpropagation.
7. Learn the basic concepts of integration.
8. Perform symbolic calculus using Python and SymPy.

## 2. Functions

A function represents a relationship between an input and an output.

For example:

$$
f(x) = x^2
$$

If the input is 3, then:

$$
f(3) = 3^2 = 9
$$

Here, `x` is the input, `f(x)` is the output, and `f` represents the rule connecting them.

Functions are used in Machine Learning to represent relationships between input features and predicted outputs.

### Common types of functions

**Linear function**

$$
f(x) = mx + c
$$

**Quadratic function**

$$
f(x) = ax^2 + bx + c
$$

**Exponential function**

$$
f(x) = e^x
$$

**Logarithmic function**

$$
f(x) = \ln(x)
$$

## 3. Limits

A limit describes the value that a function approaches as its input approaches a particular value.

The notation is:

$$
\lim_{x \to a} f(x) = L
$$

This means that as `x` approaches `a`, the function value approaches `L`.

### Example

Find the following limit:

$$
\lim_{x \to 3}(x + 2)
$$

Substitute `x = 3`:

$$
= 3 + 2 = 5
$$

Therefore, the limit is 5.

Limits are important because derivatives are defined using limits.

## 4. Continuity

A function is continuous at a point when the function value exists, the limit exists, and both values are equal.

The condition is:

$$
\lim_{x \to a} f(x) = f(a)
$$

For example, the function `f(x) = x²` is continuous for every real value of `x`.

Continuity is useful in mathematical analysis and optimisation because many calculus results require continuity or differentiability.

## 5. Derivatives

A derivative measures the instantaneous rate of change of a function.

The derivative of `f(x)` is defined as:

$$
f'(x) = \lim_{h \to 0}
\frac{f(x+h)-f(x)}{h}
$$

The derivative can also be written as `dy/dx` when `y = f(x)`.

### Geometric interpretation

The derivative represents the slope of the tangent line to a curve at a particular point.

- A positive derivative indicates that the function is increasing locally.
- A negative derivative indicates that the function is decreasing locally.
- A zero derivative indicates a horizontal tangent, although the point is not necessarily a maximum or minimum.

### Example: Derivative from first principles

Consider:

$$
f(x) = x^2
$$

Using the definition:

$$
f'(x) = \lim_{h \to 0}
\frac{(x+h)^2-x^2}{h}
$$

Expand the numerator:

$$
= \lim_{h \to 0}
\frac{x^2+2xh+h^2-x^2}{h}
$$

Simplify:

$$
= \lim_{h \to 0}(2x+h)
$$

Taking the limit gives:

$$
f'(x) = 2x
$$

Therefore, the derivative of `x²` is `2x`.

## 6. Basic Differentiation Rules

These rules make differentiation faster and are used frequently in Machine Learning.

### Constant rule

$$
\frac{d}{dx}(c) = 0
$$

The derivative of a constant is zero.

### Power rule

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$

Example:

$$
\frac{d}{dx}(x^4) = 4x^3
$$

### Constant multiple rule

$$
\frac{d}{dx}[cf(x)] = cf'(x)
$$

### Sum and difference rule

$$
\frac{d}{dx}[f(x)+g(x)]
= f'(x)+g'(x)
$$

### Product rule

$$
\frac{d}{dx}[u(x)v(x)]
= u'(x)v(x)+u(x)v'(x)
$$

### Quotient rule

For `v(x) ≠ 0`:

$\frac{d}{dx}\left(\frac{u}{v}\right)=
 \frac{vu'-uv'}{v^2}$

### Chain rule

When one function is inside another function:

$$
\frac{d}{dx}f(g(x))
= f'(g(x))g'(x)
$$

The chain rule is especially important for neural networks because backpropagation uses it to calculate gradients through multiple layers.

## 7. Derivatives of Common Functions

| Function | Derivative |
|---|---|
| `eˣ` | `eˣ` |
| `aˣ` | `aˣ ln(a)` |
| `ln(x)` | `1/x` |
| `sin(x)` | `cos(x)` |
| `cos(x)` | `-sin(x)` |
| `tan(x)` | `sec²(x)` |

For example, consider:

$$
f(x) = e^{2x}
$$

Using the chain rule:

$$
f'(x) = 2e^{2x}
$$

These derivatives are useful in mathematical modelling, probability, and neural network activation functions.

## 8. Higher-Order Derivatives

A higher-order derivative is obtained by differentiating a function more than once.

For example:

$$
f(x) = x^4
$$

First derivative:

$$
f'(x) = 4x^3
$$

Second derivative:

$$
f''(x) = 12x^2
$$

Third derivative:

$$
f'''(x) = 24x
$$

The second derivative describes how the first derivative changes. It is useful for studying curvature, convexity, and optimisation.

## 9. Partial Derivatives

A multivariable function depends on two or more input variables.

Consider:

$$
f(x,y) = x^2 + 3xy + y^2
$$

A partial derivative measures how the function changes with respect to one variable while treating the other variables as constants.

With respect to `x`:

$$
\frac{\partial f}{\partial x} = 2x + 3y
$$

With respect to `y`:

$$
\frac{\partial f}{\partial y} = 3x + 2y
$$

Partial derivatives are essential in Machine Learning because a model often has many parameters, and we need to calculate how the loss changes with respect to each parameter.

## 10. Gradient

The gradient is a collection of the first-order partial derivatives of a function.

For a function `f(x, y)`, the gradient is:

$$
\nabla f =
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y}
\right)
$$

Consider:

$$
f(x,y) = x^2 + y^2
$$

Its partial derivatives are:

$$
\frac{\partial f}{\partial x} = 2x
$$

$$
\frac{\partial f}{\partial y} = 2y
$$

Therefore:

$$
\nabla f = (2x, 2y)
$$

The gradient points in the direction of the greatest local increase of a differentiable function. The negative gradient points in the direction of the greatest local decrease.

This is the mathematical foundation of gradient-based optimisation.

## 11. Optimisation Using Derivatives

Optimisation means finding values of variables that minimise or maximise a function.

In Machine Learning, we generally want to minimise a loss function that measures the difference between predicted and actual values.

### Critical points

Critical points can occur where:

$$
f'(x) = 0
$$

They can also occur where the derivative does not exist, provided the point belongs to the function's domain.

### Second derivative test

At a critical point `x = c`:

- If `f''(c) > 0`, the function has a local minimum.
- If `f''(c) < 0`, the function has a local maximum.
- If `f''(c) = 0`, the test is inconclusive.

### Worked example

Consider:

$$
f(x) = x^2 - 6x + 5
$$

Differentiate:

$$
f'(x) = 2x - 6
$$

Set the derivative equal to zero:

$$
2x - 6 = 0
$$

Therefore:

$$
x = 3
$$

The second derivative is:

$$
f''(x) = 2
$$

Since the second derivative is positive, the function has a minimum at `x = 3`.

Calculate the minimum value:

$$
f(3) = 3^2 - 6(3) + 5 = -4
$$

The minimum value is `-4`, attained at `x = 3`.

## 12. Gradient Descent in Machine Learning

Gradient descent is an optimisation algorithm used to minimise a loss function by repeatedly updating model parameters.

The general update rule is:

$$\theta_{\text{new}}=\theta_{\text{old}}-\eta \nabla J(\theta)$$

Here:

- `θ` represents the model parameters.
- `J(θ)` is the loss function.
- `∇J(θ)` is the gradient of the loss.
- `η` is the learning rate.

The learning rate controls the size of each parameter update.

### Example

Consider the loss function:

$$
J(w) = (w-3)^2
$$

Its derivative is:

$$
\frac{dJ}{dw} = 2(w-3)
$$

Suppose the initial weight is `w = 0` and the learning rate is `0.1`.

The gradient at the initial weight is:

$$
\frac{dJ}{dw} = 2(0-3) = -6
$$

Update the weight:

$$
w_{\text{new}} = 0 - 0.1(-6)
$$

Therefore:

$$
w_{\text{new}} = 0.6
$$

The parameter moves closer to the minimum at `w = 3`.

Repeated updates can move the parameter toward the minimum. The behaviour depends on the learning rate and the loss function.

### Why gradient descent matters

Gradient descent is used to train many Machine Learning and Deep Learning models, including linear regression models trained with gradient-based methods and neural networks.

## 13. Chain Rule and Backpropagation

Backpropagation calculates gradients in neural networks by applying the chain rule through the sequence of operations in the network.

Suppose:

$$
y = (3x+1)^4
$$

Let:

$$
u = 3x+1
$$

Then:

$$
y = u^4
$$

Differentiate each part:

$$
\frac{dy}{du} = 4u^3
$$

$$
\frac{du}{dx} = 3
$$

Apply the chain rule:

$$\frac{dy}{dx}=
\frac{dy}{du}\frac{du}{dx}
$$

Substitute:

$$
\frac{dy}{dx} = 12(3x+1)^3
$$

Neural networks apply this same principle to more complex compositions of functions to calculate gradients for their trainable parameters.

## 14. Integration

Integration studies accumulation and is closely related to differentiation.

An indefinite integral represents a family of antiderivatives.

If:

$$
F'(x) = f(x)
$$

then:

$$
\int f(x)\,dx = F(x)+C
$$

Here, `C` is the constant of integration.

### Basic integration rules

**Power rule**

For `n ≠ -1`:

$$\int x^n\,dx=
\frac{x^{n+1}}{n+1}+C
$$

**Exponential function**

$$
\int e^x\,dx = e^x+C
$$

**Reciprocal function**

$$
\int \frac{1}{x}\,dx = \ln|x|+C
$$

### Example

Evaluate:

$$
\int x^2\,dx
$$

Apply the power rule:

$$
\int x^2\,dx = \frac{x^3}{3}+C
$$

Integration is important in probability, particularly when calculating probabilities from continuous probability density functions.

## 15. Definite Integrals

A definite integral calculates accumulated signed quantities over an interval.

The notation is:

$$
\int_a^b f(x)\,dx
$$

If `F'(x) = f(x)`, the Fundamental Theorem of Calculus gives:

$$
\int_a^b f(x)\,dx = F(b)-F(a)
$$

### Worked example

Evaluate:

$$
\int_0^2 x^2\,dx
$$

An antiderivative is:

$$
F(x) = \frac{x^3}{3}
$$

Apply the limits:

$$
\int_0^2 x^2\,dx
=
\frac{2^3}{3}-\frac{0^3}{3}
$$

Therefore:

$$
\int_0^2 x^2\,dx = \frac{8}{3}
$$

When the function is non-negative throughout the interval, the definite integral represents the area between the curve and the x-axis.

## 16. Calculus in Data Science and Machine Learning

Calculus supports several important concepts in data science and AI.

| Application | Role of calculus |
|---|---|
| Linear regression | Helps derive and optimise model parameters |
| Logistic regression | Supports gradient-based loss minimisation |
| Gradient descent | Uses derivatives to update parameters |
| Neural networks | Uses partial derivatives and the chain rule |
| Backpropagation | Calculates gradients through network layers |
| Probability | Integration helps calculate probabilities for continuous variables |
| Optimisation | Derivatives help identify minima and maxima |
| Deep Learning | Gradients help train model parameters |

You do not need to master every advanced calculus topic before starting Machine Learning. Focus first on derivatives, partial derivatives, gradients, the chain rule, and gradient descent.

## 17. Python Implementation Using SymPy

SymPy is a Python library for symbolic mathematics. It can calculate derivatives, integrals, and limits exactly when symbolic solutions are available.

Install it using:

```bash
pip install sympy
```

### Symbolic differentiation

```python
import sympy as sp

x = sp.symbols("x")

f = x**3 + 2*x**2 - 5*x + 4

derivative = sp.diff(f, x)

print("Function:", f)
print("Derivative:", derivative)
```

Output:

```text
Function: x**3 + 2*x**2 - 5*x + 4
Derivative: 3*x**2 + 4*x - 5
```

### Partial derivatives

```python
import sympy as sp

x, y = sp.symbols("x y")

f = x**2 + 3*x*y + y**2

fx = sp.diff(f, x)
fy = sp.diff(f, y)

print("Partial derivative with respect to x:", fx)
print("Partial derivative with respect to y:", fy)
```

### Symbolic integration

```python
import sympy as sp

x = sp.symbols("x")

f = x**2

integral = sp.integrate(f, x)

print("Integral:", integral)
```

Output:

```text
Integral: x**3/3
```

SymPy omits the arbitrary constant in its symbolic output.

### Definite integration

```python
import sympy as sp

x = sp.symbols("x")

f = x**2

result = sp.integrate(f, (x, 0, 2))

print("Definite integral:", result)
```

Output:

```text
Definite integral: 8/3
```

### Calculating a limit

```python
import sympy as sp

x = sp.symbols("x")

f = (x**2 - 4) / (x - 2)

result = sp.limit(f, x, 2)

print("Limit:", result)
```

Output:

```text
Limit: 4
```

## 18. Common Mistakes

1. Forgetting to reduce the exponent when applying the power rule.
2. Forgetting the chain rule when differentiating a composite function.
3. Applying the product rule incorrectly.
4. Confusing ordinary derivatives with partial derivatives.
5. Forgetting the constant of integration in indefinite integrals.
6. Confusing definite and indefinite integrals.
7. Assuming every point where the first derivative is zero is a minimum or maximum.
8. Assuming a larger learning rate always makes gradient descent faster or better.
9. Treating a numerical approximation as an exact mathematical result.

## 19. Important Formula Summary

**Derivative definition**

$$
f'(x) = \lim_{h \to 0}
\frac{f(x+h)-f(x)}{h}
$$

**Power rule**

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$

**Product rule**

$$
(uv)' = u'v+uv'
$$

**Quotient rule**

$$\left(\frac{u}{v}\right)'=
\frac{vu'-uv'}{v^2}
$$

**Chain rule**

$$
\frac{d}{dx}f(g(x)) = f'(g(x))g'(x)
$$

**Gradient descent**

$$\theta_{\text{new}}=
\theta_{\text{old}}-\eta\nabla J(\theta)
$$

**Indefinite integral**

$$
\int f(x)\,dx = F(x)+C
$$

**Definite integral**

$$
\int_a^b f(x)\,dx = F(b)-F(a)
$$

where `F'(x) = f(x)`.

## 20. Points to Remember

1. Limits provide the foundation for derivatives.
2. Derivatives measure instantaneous rates of change.
3. Partial derivatives measure changes with respect to individual variables.
4. The gradient contains the first-order partial derivatives of a function.
5. Gradient descent uses gradients to update model parameters.
6. The chain rule is fundamental to backpropagation.
7. Integration studies accumulation and is important for continuous probability distributions.
8. SymPy can perform symbolic differentiation, integration, and limit calculations.
9. Calculus is a mathematical foundation for optimisation in Machine Learning.

## 21. Chapter Summary

Calculus provides the mathematical tools required to understand continuous change and accumulation.

Differentiation measures rates of change, while partial derivatives and gradients extend this concept to functions with multiple variables. These concepts form the foundation of gradient descent and backpropagation, which are central to training many Machine Learning and Deep Learning models.

Integration provides tools for studying accumulation and calculating probabilities from continuous probability density functions.

For an FSDS learner, the most important priorities are differentiation, partial derivatives, gradients, the chain rule, and gradient descent. These concepts connect mathematical theory with practical model training.

## 22. References

- James Stewart, *Calculus: Early Transcendentals*.
- MIT OpenCourseWare, *Single Variable Calculus*.
- OpenStax, *Calculus*.
- [SymPy Documentation](https://docs.sympy.org/)
- [NumPy Documentation](https://numpy.org/doc/)

## Related Topics

- [Linear Algebra](../12_Linear_Algebra/README.md)
- [Probability](../03_Probability/README.md)
- [Probability Distributions](../04_Probability_Distributions/README.md)
- [Regression](../10_Regression/README.md)
- [Bias and Variance](../14_Bias_And_Variance/README.md)
- [Statistics for Machine Learning](../15_Statistics_for_Machine_Learning/README.md)
