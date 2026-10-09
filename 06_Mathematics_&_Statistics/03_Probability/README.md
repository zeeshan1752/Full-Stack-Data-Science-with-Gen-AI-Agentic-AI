# Probability

Probability is the mathematical language used to describe **uncertainty and randomness**.

In real-world data, outcomes are not always known in advance. A customer may or may not purchase a product, a machine may or may not fail, a transaction may or may not be fraudulent, and a sampled observation may or may not have a particular property.

Probability provides a formal framework for describing such uncertain events.

This chapter develops probability from its basic ideas to conditional probability, independence, Bayes' theorem, counting methods, and important probability concepts used as foundations for later statistical and machine learning topics.

---

## 1. Introduction to Probability

Probability measures how likely an event is to occur.

The probability of an event $A$ is written as:

$P(A)$

For an ordinary probability:

$0 \leq P(A) \leq 1$

The two extreme cases are:

$P(A)=0$

which represents an impossible event, and:

$P(A)=1$

which represents a certain event.

A probability can also be expressed as a percentage.

For example:

$P(A)=0.75$

is equivalent to:

$75\%$

Probability does not guarantee that an event will occur. It describes the likelihood of the event based on the probability model being used.

---

## 2. Random Experiment

A **random experiment** is a process whose exact outcome cannot be known with certainty before the experiment is performed.

Examples include:

- Tossing a coin
- Rolling a die
- Drawing a card
- Selecting a customer at random
- Selecting a product from a warehouse
- Observing whether a machine fails during a given period

Although the exact outcome is uncertain, the possible outcomes can usually be described.

For example, when a standard die is rolled, the possible outcomes are:

$\{1,2,3,4,5,6\}$

---

## 3. Outcome

An **outcome** is one possible result of a random experiment.

When a coin is tossed, the possible outcomes are:

$\{H,T\}$

where:

- $H$ = Heads
- $T$ = Tails

When a die is rolled:

$\{1,2,3,4,5,6\}$

Each individual result is an outcome.

---

## 4. Sample Space

The **sample space** is the set of all possible outcomes of a random experiment.

The sample space is commonly represented by:

$S$

### Example 1: Coin Toss

For one coin toss:

$S=\{H,T\}$

### Example 2: Die Roll

For one die roll:

$S=\{1,2,3,4,5,6\}$

### Example 3: Two Coin Tosses

For two coin tosses:

$S=\{HH,HT,TH,TT\}$

There are four possible outcomes.

Therefore:

$|S|=4$

where $|S|$ represents the number of outcomes in the sample space.

---

## 5. Event

An **event** is a subset of the sample space.

Suppose a die is rolled.

The sample space is:

$S=\{1,2,3,4,5,6\}$

Let event $A$ represent obtaining an even number.

Then:

$A=\{2,4,6\}$

Therefore, $A$ is a subset of $S$:

$A \subseteq S$

An event may contain:

- One outcome
- Several outcomes
- All outcomes
- No outcomes

---

## 6. Simple and Compound Events

### Simple Event

A simple event contains exactly one outcome.

For a die:

$A=\{4\}$

This is the event of obtaining 4.

### Compound Event

A compound event contains more than one outcome.

For example:

$B=\{2,4,6\}$

represents obtaining an even number.

The distinction is useful when constructing events and calculating their probabilities.

---

## 7. Probability of an Event

When all outcomes are equally likely, the probability of an event can be calculated using:

$P(A)=\frac{|A|}{|S|}$

where:

- $|A|$ = number of favourable outcomes
- $|S|$ = total number of outcomes

### Worked Example

A fair die is rolled. What is the probability of obtaining an even number?

Sample space:

$S=\{1,2,3,4,5,6\}$

Even outcomes:

$A=\{2,4,6\}$

Therefore:

$|A|=3$

and:

$|S|=6$

Apply the formula:

$P(A)=\frac{3}{6}$

$P(A)=\frac{1}{2}$

Therefore:

$\boxed{P(A)=0.5}$

or:

$\boxed{P(A)=50\%}$

This formula assumes that the possible outcomes are equally likely.

---

## 8. Equally Likely Outcomes

Two or more outcomes are **equally likely** when they have the same probability.

For a fair coin:

$P(H)=P(T)=\frac{1}{2}$

For a fair die:

$P(1)=P(2)=\cdots=P(6)=\frac{1}{6}$

The simple ratio:

$P(A)=\frac{|A|}{|S|}$

is appropriate when the relevant outcomes are equally likely.

If outcomes are not equally likely, their individual probabilities must be taken into account.

---

## 9. Probability Axioms

The modern mathematical foundation of probability is commonly expressed through three basic axioms.

### Axiom 1: Non-Negativity

For every event $A$:

$P(A)\geq0$

A probability cannot be negative.

### Axiom 2: Probability of the Sample Space

The probability that some outcome in the sample space occurs is:

$P(S)=1$

### Axiom 3: Additivity for Mutually Exclusive Events

If $A$ and $B$ cannot occur together:

$A\cap B=\varnothing$

then:

$P(A\cup B)=P(A)+P(B)$

These axioms form the foundation from which many probability rules are derived.

---

## 10. Complement of an Event

The **complement** of event $A$ represents all outcomes in the sample space that are not in $A$.

It is commonly written as:

$A^c$

The probability of the complement is:

$P(A^c)=1-P(A)$

### Worked Example

Suppose:

$P(A)=0.7$

Then:

$P(A^c)=1-0.7$

Therefore:

$\boxed{P(A^c)=0.3}$

The probability that event $A$ does not occur is 0.3.

---

## 11. Addition Rule of Probability

The general addition rule is:

$P(A\cup B)=P(A)+P(B)-P(A\cap B)$

where:

- $A\cup B$ means $A$ or $B$ occurs.
- $A\cap B$ means both $A$ and $B$ occur.

The intersection is subtracted because it is counted twice when $P(A)$ and $P(B)$ are added.

### Worked Example

Suppose:

$P(A)=0.5$

$P(B)=0.4$

and:

$P(A\cap B)=0.2$

Then:

$P(A\cup B)=0.5+0.4-0.2$

Therefore:

$\boxed{P(A\cup B)=0.7}$

---

## 12. Mutually Exclusive Events

Two events are **mutually exclusive** if they cannot occur together.

For mutually exclusive events:

$A\cap B=\varnothing$

Therefore:

$P(A\cap B)=0$

The addition rule becomes:

$P(A\cup B)=P(A)+P(B)$

### Example

When a single die is rolled:

- Event $A$ = obtaining 2
- Event $B$ = obtaining 5

Both cannot happen on the same roll.

Therefore:

$P(A\cap B)=0$

and:

$P(A\cup B)=P(A)+P(B)$

$=\frac{1}{6}+\frac{1}{6}$

$\boxed{P(A\cup B)=\frac{1}{3}}$

Mutual exclusivity is different from independence.

---

## 13. Conditional Probability

Conditional probability measures the probability of an event **given that another event is known to have occurred**.

The probability of $A$ given $B$ is written as:

$P(A\mid B)$

and is calculated as:

$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$

provided:

$P(B)>0$

### Worked Example

Suppose:

$P(A\cap B)=0.2$

and:

$P(B)=0.5$

Then:

$P(A\mid B)=\frac{0.2}{0.5}$

Therefore:

$\boxed{P(A\mid B)=0.4}$

The information that $B$ occurred changes the probability assigned to $A$.

---

## 14. Conditional Probability Using a Table

Suppose a group of 100 students is classified by whether they study regularly and whether they pass an examination.

| | Pass | Fail | Total |
|---|---:|---:|---:|
| Study Regularly | 45 | 5 | 50 |
| Do Not Study Regularly | 25 | 25 | 50 |
| Total | 70 | 30 | 100 |

Let:

- $A$ = student passes
- $B$ = student studies regularly

We want:

$P(A\mid B)$

Among the 50 students who study regularly, 45 passed.

Therefore:

$P(A\mid B)=\frac{45}{50}$

$\boxed{P(A\mid B)=0.9}$

Thus, within the group of students who study regularly, the observed probability of passing is 90%.

The denominator is the group specified by the condition.

---

## 15. Multiplication Rule

Starting from conditional probability:

$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$

Multiply both sides by $P(B)$:

$P(A\cap B)=P(A\mid B)P(B)$

Therefore:

$\boxed{P(A\cap B)=P(A\mid B)P(B)}$

Similarly:

$P(A\cap B)=P(B\mid A)P(A)$

This rule is useful for calculating the probability that multiple events occur together.

---

## 16. Independence

Two events $A$ and $B$ are **independent** when the occurrence of one event does not change the probability of the other.

Mathematically:

$P(A\mid B)=P(A)$

when $P(B)>0$.

An equivalent multiplication rule is:

$P(A\cap B)=P(A)P(B)$

### Example

Suppose a fair coin is tossed twice.

Let:

- $A$ = first toss is Heads
- $B$ = second toss is Heads

The result of the first toss does not affect the second toss.

Therefore:

$P(A)=\frac{1}{2}$

and:

$P(B)=\frac{1}{2}$

Thus:

$P(A\cap B)=\frac{1}{2}\times\frac{1}{2}$

$\boxed{P(A\cap B)=\frac{1}{4}}$

### Important Distinction

**Mutually exclusive** events cannot occur together.

**Independent** events do not affect each other's probabilities.

If two events have positive probability and are mutually exclusive, they cannot also be independent.

---

## 17. Conditional Probability and Independence

Conditional probability and independence are closely related.

If $A$ and $B$ are independent:

$P(A\mid B)=P(A)$

and:

$P(B\mid A)=P(B)$

Therefore:

$P(A\cap B)=P(A)P(B)$

Independence should not be assumed merely because two events appear unrelated. It is a property of the probability model or data-generating process.

---

## 18. Law of Total Probability

Suppose the sample space is divided into mutually exclusive and exhaustive events:

$B_1,B_2,\ldots,B_n$

Then the probability of event $A$ can be calculated as:

$P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)$

For two events $B$ and $B^c$:

$P(A)=P(A\mid B)P(B)+P(A\mid B^c)P(B^c)$

### Worked Example

Suppose a factory has two production lines.

- Line A produces 60% of products.
- Line B produces 40% of products.
- Line A has a defect rate of 2%.
- Line B has a defect rate of 5%.

Let $D$ represent a defective product.

Then:

$P(A)=0.6$

$P(B)=0.4$

$P(D\mid A)=0.02$

$P(D\mid B)=0.05$

Therefore:

$P(D)=P(D\mid A)P(A)+P(D\mid B)P(B)$

Substitute:

$P(D)=(0.02)(0.6)+(0.05)(0.4)$

$P(D)=0.012+0.020$

Therefore:

$\boxed{P(D)=0.032}$

As a percentage:

$\boxed{P(D)=3.2\%}$

---

## 19. Bayes' Theorem

Bayes' theorem provides a way to reverse a conditional probability.

Starting with:

$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$

and:

$P(B\mid A)=\frac{P(A\cap B)}{P(A)}$

we obtain:

$\boxed{ P(A\mid B)= \frac{P(B\mid A)P(A)} {P(B)} }$

Using the law of total probability, when $A$ and $A^c$ partition the sample space:

$P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)$

Therefore:

$\boxed{ P(A\mid B)= \frac{P(B\mid A)P(A)} {P(B\mid A)P(A)+P(B\mid A^c)P(A^c)} }$

Bayes' theorem is especially important when we want to update a prior belief after observing new evidence.

![Bayes theorem probability illustration](https://media.geeksforgeeks.org/wp-content/uploads/20250222144920592095/stat.webp)

---

## 20. Bayes' Theorem — Worked Example

Suppose a screening test is used for a condition.

Assume:

- 1% of the population has the condition.
- The test is positive for 95% of people who have the condition.
- The test is positive for 5% of people who do not have the condition.

Let:

- $D$ = person has the condition
- $+$ = test result is positive

We know:

$P(D)=0.01$

$P(D^c)=0.99$

$P(+\mid D)=0.95$

$P(+\mid D^c)=0.05$

We want:

$P(D\mid +)$

Using Bayes' theorem:

$P(D\mid +)= \frac{P(+\mid D)P(D)} {P(+\mid D)P(D)+P(+\mid D^c)P(D^c)}$

Substitute:

$P(D\mid +)= \frac{(0.95)(0.01)} {(0.95)(0.01)+(0.05)(0.99)}$

Calculate the numerator:

$(0.95)(0.01)=0.0095$

Calculate the second term in the denominator:

$(0.05)(0.99)=0.0495$

Therefore:

$P(D\mid +)= \frac{0.0095}{0.0095+0.0495}$

$P(D\mid +)=\frac{0.0095}{0.059}$

Therefore:

$\boxed{P(D\mid +)\approx0.161}$

or approximately:

$\boxed{16.1\%}$

The important lesson is that a positive test result does not automatically mean that the person has a 95% probability of having the condition.

The 95% figure in the example is $P(+\mid D)$, while the quantity of interest is $P(D\mid +)$. These are different conditional probabilities.

---

## 21. Random Variables

A **random variable** assigns a numerical value to the outcome of a random experiment.

It is commonly represented by a capital letter such as:

$X$

### Example

Suppose a coin is tossed twice.

The possible outcomes are:

$\{HH,HT,TH,TT\}$

Let $X$ represent the number of Heads.

Then:

| Outcome | $X$ |
|---|---:|
| HH | 2 |
| HT | 1 |
| TH | 1 |
| TT | 0 |

The random variable converts experimental outcomes into numerical values.

Random variables can be:

- Discrete
- Continuous

These ideas lead naturally to probability distributions.

---

## 22. Discrete Random Variable

A discrete random variable takes countable values.

Examples:

- Number of customers arriving in one hour
- Number of defective products
- Number of Heads in three coin tosses
- Number of website purchases

For example, if $X$ is the number of Heads in two coin tosses:

$X\in\{0,1,2\}$

---

## 23. Continuous Random Variable

A continuous random variable can take values over an interval.

Examples:

- Height
- Weight
- Temperature
- Waiting time
- Distance

For example:

$X=2.1,\;2.15,\;2.157,\ldots$

may represent a measured time.

For a continuous random variable, the probability of one exact point is generally:

$P(X=x)=0$

Probabilities are instead assigned to intervals, such as:

$P(a<X<b)$

---

## 24. Expected Value

The **expected value** represents the long-run average value of a random variable under a specified probability model.

For a discrete random variable:

$E(X)=\sum_x xP(X=x)$

### Worked Example

Suppose a fair die is rolled.

The possible values are:

$1,2,3,4,5,6$

Each has probability:

$\frac{1}{6}$

Therefore:

$E(X)= 1\left(\frac{1}{6}\right)+ 2\left(\frac{1}{6}\right)+ 3\left(\frac{1}{6}\right)+ 4\left(\frac{1}{6}\right)+ 5\left(\frac{1}{6}\right)+ 6\left(\frac{1}{6}\right)$

Factor out $\frac{1}{6}$:

$E(X)=\frac{1+2+3+4+5+6}{6}$

$E(X)=\frac{21}{6}$

Therefore:

$\boxed{E(X)=3.5}$

A die does not produce 3.5 on a single roll. The expected value is a theoretical long-run average.

---

## 25. Linearity of Expectation

Expected value has an important property called **linearity of expectation**.

For random variables $X$ and $Y$:

$E(X+Y)=E(X)+E(Y)$

More generally:

$E(aX+b)=aE(X)+b$

where $a$ and $b$ are constants.

Importantly, linearity of expectation does not require $X$ and $Y$ to be independent.

---

## 26. Variance of a Random Variable

Variance measures the spread of a random variable around its expected value.

The definition is:

$Var(X)=E[(X-E(X))^2]$

An equivalent formula is:

$\boxed{Var(X)=E(X^2)-[E(X)]^2}$

The standard deviation is:

$SD(X)=\sqrt{Var(X)}$

Variance is non-negative:

$Var(X)\geq0$

---

## 27. Covariance

Covariance describes how two numerical random variables vary together.

The covariance is:

$Cov(X,Y)=E[(X-E(X))(Y-E(Y))]$

An equivalent form is:

$Cov(X,Y)=E(XY)-E(X)E(Y)$

A positive covariance generally indicates that larger values of one variable tend to occur with larger values of the other.

A negative covariance generally indicates an opposite tendency.

Covariance depends on the scale of the variables, so its magnitude is not directly comparable across differently scaled variable pairs.

---

## 28. Correlation

Correlation is a standardised measure of linear association.

The population correlation coefficient is:

$\rho_{X,Y}= \frac{Cov(X,Y)} {\sigma_X\sigma_Y}$

The sample correlation coefficient is commonly written as:

$r= \frac{Cov(X,Y)} {s_Xs_Y}$

Correlation typically lies between:

$-1\leq r\leq1$

Interpretation:

- $r$ close to 1 → strong positive linear association
- $r$ close to -1 → strong negative linear association
- $r$ close to 0 → weak or no linear association

A correlation close to zero does not necessarily mean that no relationship exists; a strong nonlinear relationship can still have a small linear correlation.

Correlation also does not by itself establish causation.

---

## 29. Counting Principles

Counting methods are useful for calculating probabilities when the sample space contains many possible outcomes.

Two fundamental counting rules are:

- Multiplication rule
- Addition rule

### Multiplication Principle

If one task can be completed in $m$ ways and another independent stage can be completed in $n$ ways, the combined number of possibilities is:

$m\times n$

### Example

Suppose a password contains:

- 3 choices for the first character
- 4 choices for the second character
- 5 choices for the third character

Then the total number of possible passwords is:

$3\times4\times5=60$

Therefore:

$\boxed{60}$

possible combinations exist under these choices.

---

## 30. Factorial

The factorial of a positive integer $n$ is:

$n!=n(n-1)(n-2)\cdots2\cdot1$

For example:

$5!=5\times4\times3\times2\times1$

$\boxed{5!=120}$

By convention:

$\boxed{0!=1}$

Factorials are used extensively in permutations and combinations.

---

## 31. Permutations

A permutation is an arrangement in which **order matters**.

The number of ways to arrange $n$ distinct objects is:

$n!$

More generally, the number of ways to select and arrange $r$ objects from $n$ distinct objects is:

${}^nP_r=\frac{n!}{(n-r)!}$

### Worked Example

How many ways can 3 students be selected and arranged from 5 students?

Here:

$n=5,\quad r=3$

Therefore:

${}^5P_3=\frac{5!}{(5-3)!}$

$=\frac{5!}{2!}$

$=\frac{120}{2}$

Therefore:

$\boxed{{}^5P_3=60}$

---

## 32. Combinations

A combination is a selection in which **order does not matter**.

The number of ways to select $r$ objects from $n$ objects is:

${}^nC_r=\frac{n!}{r!(n-r)!}$

It is also written as:

$\binom{n}{r}$

### Worked Example

How many ways can 3 students be selected from 5 students?

Here:

$n=5,\quad r=3$

Therefore:

${}^5C_3= \frac{5!}{3!2!}$

$=\frac{120}{6\times2}$

$\boxed{{}^5C_3=10}$

The difference from permutations is important:

- Permutation → order matters.
- Combination → order does not matter.

---

## 33. Binomial Probability

Suppose an experiment has two possible outcomes:

- Success
- Failure

If:

- $n$ = number of trials
- $p$ = probability of success
- $1-p$ = probability of failure
- $X$ = number of successes

then the probability of exactly $x$ successes is:

$P(X=x)= \binom{n}{x} p^x(1-p)^{n-x}$

This formula forms the basis of the binomial probability distribution.

### Worked Example

Suppose a fair coin is tossed 4 times. What is the probability of exactly 2 Heads?

Here:

$n=4$

$x=2$

$p=0.5$

Therefore:

$P(X=2)= \binom{4}{2}(0.5)^2(0.5)^2$

Calculate the combination:

$\binom{4}{2}=6$

Therefore:

$P(X=2)=6(0.25)(0.25)$

$P(X=2)=0.375$

Therefore:

$\boxed{P(X=2)=0.375}$

or:

$\boxed{37.5\%}$

---

## 34. Conditional Probability vs Joint Probability

These concepts should not be confused.

### Joint Probability

Joint probability is the probability that two events occur together:

$P(A\cap B)$

### Conditional Probability

Conditional probability is the probability of one event given that another has occurred:

$P(A\mid B)$

The relationship is:

$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$

Therefore, the condition changes the reference set.

---

## 35. Odds and Probability

Probability and odds are related but not identical.

If:

$P(A)=p$

then the odds in favour of $A$ are:

$\text{Odds}=\frac{p}{1-p}$

### Example

Suppose:

$P(A)=0.75$

Then:

$\text{Odds}=\frac{0.75}{1-0.75}$

$=\frac{0.75}{0.25}$

Therefore:

$\boxed{\text{Odds}=3:1}$

This means there are three units of probability weight in favour for every one unit against, under the odds representation.

---

## 36. Law of Large Numbers

The **law of large numbers** describes the behaviour of sample averages as the number of repeated observations becomes large under appropriate conditions.

For example, consider repeatedly tossing a fair coin.

The theoretical probability of Heads is:

$P(H)=0.5$

If the coin is tossed only 10 times, the observed proportion of Heads may be 0.3 or 0.7.

With a very large number of tosses, the observed proportion tends to move closer to 0.5 under the standard independent fair-coin model.

The law does not say that short sequences must look balanced.

---

## 37. Gambler's Fallacy

The **gambler's fallacy** is the incorrect belief that independent random events must compensate for previous outcomes.

Suppose a fair coin produces:

```
H H H H H
```

The probability of Heads on the next toss is still:

$P(H)=0.5$

The previous five outcomes do not make Tails "due" on the next independent toss.

Long-run frequencies and short-run sequences should not be confused.

---

## 38. Probability Tree

A probability tree is a visual method for representing sequential events.

Suppose a coin is tossed twice.

```
                 First Toss
                 /        \
                H          T
               / \        / \
              H   T      H   T
```

The four paths correspond to:

$HH,\ HT,\ TH,\ TT$

For a fair coin, each path has probability:

$\frac{1}{2}\times\frac{1}{2}$

Therefore:

$\boxed{P(\text{each path})=\frac{1}{4}}$

Probability trees become especially useful when later probabilities depend on earlier outcomes.

---

## 39. Probability from Empirical Data

Probability can also be estimated from observed data.

Suppose an online store records 1,000 visitors and 80 make a purchase.

The empirical purchase probability is:

$\hat{p}=\frac{80}{1000}$

Therefore:

$\boxed{\hat{p}=0.08}$

or:

$\boxed{\hat{p}=8\%}$

The symbol $\hat{p}$ indicates an estimated probability or sample proportion.

An empirical probability is based on observed data and may differ from the underlying long-run probability.

---

## 40. A Complete Probability Example

Suppose a company receives orders from two regions.

- Region A generates 70% of orders.
- Region B generates 30% of orders.
- 3% of Region A orders are returned.
- 8% of Region B orders are returned.

Let:

- $A$ = order came from Region A
- $B$ = order came from Region B
- $R$ = order is returned

We know:

$P(A)=0.70$

$P(B)=0.30$

$P(R\mid A)=0.03$

$P(R\mid B)=0.08$

### Step 1: Overall Probability of a Return

Using the law of total probability:

$P(R)=P(R\mid A)P(A)+P(R\mid B)P(B)$

Substitute:

$P(R)=(0.03)(0.70)+(0.08)(0.30)$

$P(R)=0.021+0.024$

Therefore:

$\boxed{P(R)=0.045}$

or:

$\boxed{P(R)=4.5\%}$

### Step 2: Probability That a Returned Order Came From Region B

We want:

$P(B\mid R)$

Using Bayes' theorem:

$P(B\mid R)= \frac{P(R\mid B)P(B)} {P(R)}$

Substitute:

$P(B\mid R)= \frac{(0.08)(0.30)} {0.045}$

$P(B\mid R)= \frac{0.024}{0.045}$

Therefore:

$\boxed{P(B\mid R)\approx0.5333}$

or approximately:

$\boxed{53.33\%}$

Although Region B produces only 30% of orders, it accounts for approximately 53.33% of returned orders under this probability model because its return probability is higher.

---

## 41. Common Mistakes

### Mistake 1: Confusing $P(A\mid B)$ With $P(B\mid A)$

They are generally different:

$P(A\mid B)\neq P(B\mid A)$

### Mistake 2: Forgetting the Intersection in the Addition Rule

For general events:

$P(A\cup B)=P(A)+P(B)-P(A\cap B)$

### Mistake 3: Assuming Events Are Independent

Independence must be justified by the model or evidence.

### Mistake 4: Confusing Mutually Exclusive and Independent Events

Mutually exclusive events cannot happen together.

Independent events do not change each other's probabilities.

### Mistake 5: Using the Equally-Likely Formula When Outcomes Are Not Equally Likely

The formula:

$P(A)=\frac{|A|}{|S|}$

requires equally likely outcomes.

### Mistake 6: Confusing Probability With Percentage

For example:

$0.25=25\%$

but 0.25 and 25 are not the same numerical probability.

### Mistake 7: Confusing Probability With Odds

A probability of 0.75 corresponds to odds of 3:1, not 75:25 as a probability statement.

### Mistake 8: Interpreting Expected Value as a Guaranteed Outcome

An expected value is a theoretical average, not necessarily an outcome that must occur.

### Mistake 9: Treating a Positive Test Rate as the Probability of Having a Condition

The quantities:

$P(+\mid D)$

and:

$P(D\mid +)$

are different.

---

# 42. Points to Remember

1. Probability measures uncertainty.
2. Probability lies between 0 and 1.
3. A random experiment has possible outcomes.
4. The sample space contains all possible outcomes.
5. An event is a subset of the sample space.
6. For equally likely outcomes, $P(A)=|A|/|S|$.
7. The complement rule is $P(A^c)=1-P(A)$.
8. The general addition rule is $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
9. Mutually exclusive events cannot occur together.
10. Conditional probability is written as $P(A\mid B)$.
11. The multiplication rule is $P(A\cap B)=P(A\mid B)P(B)$.
12. Independent events do not change each other's probabilities.
13. The law of total probability combines conditional probabilities across a partition.
14. Bayes' theorem reverses a conditional probability.
15. A random variable assigns numerical values to outcomes.
16. Expected value represents a theoretical long-run average.
17. Variance measures the spread of a random variable.
18. Covariance describes joint variation between two variables.
19. Correlation standardises linear association.
20. Permutations are used when order matters.
21. Combinations are used when order does not matter.
22. The law of large numbers concerns long-run behaviour.
23. Independent random events do not become "due" because of previous outcomes.

---

# 43. Important Formula Summary

### Probability of an Event

$P(A)=\frac{|A|}{|S|}$

when outcomes are equally likely.

### Complement Rule

$P(A^c)=1-P(A)$

### General Addition Rule

$P(A\cup B)=P(A)+P(B)-P(A\cap B)$

### Mutually Exclusive Events

$P(A\cup B)=P(A)+P(B)$

when:

$A\cap B=\varnothing$

### Conditional Probability

$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$

### Multiplication Rule

$P(A\cap B)=P(A\mid B)P(B)$

### Independence

$P(A\cap B)=P(A)P(B)$

### Law of Total Probability

$P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)$

### Bayes' Theorem

$P(A\mid B)= \frac{P(B\mid A)P(A)} {P(B)}$

### Expected Value

$E(X)=\sum_x xP(X=x)$

### Variance

$Var(X)=E[(X-E(X))^2]$

### Alternative Variance Formula

$Var(X)=E(X^2)-[E(X)]^2$

### Standard Deviation

$SD(X)=\sqrt{Var(X)}$

### Covariance

$Cov(X,Y)=E[(X-E(X))(Y-E(Y))]$

### Correlation

$\rho_{X,Y}= \frac{Cov(X,Y)} {\sigma_X\sigma_Y}$

### Factorial

$n!=n(n-1)(n-2)\cdots1$

### Permutation

${}^nP_r=\frac{n!}{(n-r)!}$

### Combination

${}^nC_r=\frac{n!}{r!(n-r)!}$

### Binomial Probability

$P(X=x)= \binom{n}{x}p^x(1-p)^{n-x}$

### Odds

$\text{Odds}=\frac{p}{1-p}$

### Empirical Probability

$\hat{p}=\frac{\text{Observed favourable outcomes}} {\text{Total observations}}$

---

# 44. Quick Concept Comparison

| Concept | Meaning |
|---|---|
| Experiment | Process producing an uncertain outcome |
| Outcome | One possible result |
| Sample Space | Set of all possible outcomes |
| Event | Subset of the sample space |
| Complement | Event not occurring |
| Mutually Exclusive | Events cannot occur together |
| Independent | Occurrence of one does not change the probability of the other |
| Joint Probability | Probability of events occurring together |
| Conditional Probability | Probability given another event |
| Expected Value | Theoretical long-run average |
| Variance | Measure of squared spread |
| Covariance | Joint variation of two variables |
| Correlation | Standardised linear association |
| Permutation | Arrangement where order matters |
| Combination | Selection where order does not matter |
| Bayes' Theorem | Updates or reverses conditional probability |
| Law of Large Numbers | Long-run averages tend toward expected values under appropriate conditions |

---

# 45. Chapter Summary

Probability provides a mathematical framework for reasoning about uncertain events.

The foundation begins with **random experiments, outcomes, sample spaces, and events**. From these ideas we develop probability rules such as the complement rule and addition rule.

Conditional probability allows us to update probabilities when information is available. The multiplication rule describes joint events, while independence describes situations where one event does not change another event's probability.

The **law of total probability** combines probabilities across different cases, and **Bayes' theorem** allows a conditional probability to be reversed using prior information and evidence.

Probability also provides the foundation for **random variables, expected value, variance, covariance, and correlation**. Counting methods such as permutations and combinations make it possible to calculate probabilities in more complex sample spaces.

The central lesson is that probability statements must always be interpreted according to the underlying assumptions. In particular, equally likely outcomes, independence, conditional probability, and population proportions should never be assumed without justification.

---

# 46. References

1. Standard introductory probability and statistics resources covering probability spaces, conditional probability, independence, Bayes' theorem, random variables, and counting.
2. Open educational resources for probability and statistics.
3. Course notes and classroom material used for the Mathematics & Statistics section of this repository.
