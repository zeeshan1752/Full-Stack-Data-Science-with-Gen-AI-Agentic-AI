# Probability

Probability is a branch of mathematics that measures the likelihood of an event occurring. It helps us understand uncertainty, analyse possible outcomes, and make decisions using mathematical reasoning.

In Data Science and Machine Learning, probability is used in classification, Bayesian inference, risk estimation, uncertainty modelling, recommendation systems, and many other applications.

Probability values range from 0 to 1.

- **Probability = 0:** The event is impossible.
- **Probability = 1:** The event is certain.
- **Probability = 0.5:** The event has a probability of 50%.

For example, when a fair coin is tossed, the probability of getting heads is one-half.

$$
P(H)=\frac{1}{2}=0.5
$$

This chapter covers probability fundamentals, event operations, probability rules, conditional probability, independence, the law of total probability, Bayes' theorem, and empirical probability, with worked examples and Python implementations.

---

## 1. Random Experiment, Outcome, and Sample Space

### 1.1 Random Experiment

A random experiment is an experiment whose exact outcome cannot be predicted with certainty before it is performed, even when the conditions are known.

Examples include tossing a coin, rolling a die, drawing a card, and randomly selecting a student.

### 1.2 Outcome

An outcome is a possible result of a random experiment.

When a die is rolled, the possible outcomes are 1, 2, 3, 4, 5, and 6.

### 1.3 Sample Space

The sample space is the set of all possible outcomes of a random experiment. It is usually represented by \(S\) or \(\Omega\).

For a coin toss:

$$
S=\{H,T\}
$$

For a die roll:

$$
S=\{1,2,3,4,5,6\}
$$

Here, \(H\) represents heads and \(T\) represents tails.

### 1.4 Event

An event is a collection of one or more outcomes of a random experiment.

For example, when a die is rolled, let \(A\) represent the event of getting an even number.

$$
A=\{2,4,6\}
$$

An event occurs when the observed outcome belongs to that event.

**Python implementation**

Python sets can represent sample spaces and events.

```python
sample_space = {1, 2, 3, 4, 5, 6}

even_event = {2, 4, 6}
greater_than_three = {4, 5, 6}

print("Sample space:", sample_space)
print("Even outcomes:", even_event)
print("Outcomes greater than 3:", greater_than_three)
```

This representation is useful for understanding event operations, although large or continuous sample spaces usually require mathematical or computational methods rather than explicit enumeration.

## 2. Classical Probability

Classical probability applies when all possible outcomes are equally likely.

The probability of an event is the number of favourable outcomes divided by the total number of equally likely outcomes.

$$
P(A)=\frac{\text{Favourable outcomes}}{\text{Total equally likely outcomes}}
$$

**Worked example**

A fair die is rolled. Find the probability of getting an even number.

The sample space is:

$$
S=\{1,2,3,4,5,6\}
$$

The favourable outcomes are:

$$
A=\{2,4,6\}
$$

There are three favourable outcomes and six equally likely outcomes.

$$
P(A)=\frac{3}{6}=\frac{1}{2}
$$

**Answer:** The probability of getting an even number is 0.5, or 50%.

The classical formula should not be applied blindly when outcomes are not equally likely.

**Python implementation**

```python
favourable_outcomes = 3
total_outcomes = 6

probability = favourable_outcomes / total_outcomes

print("Probability:", probability)
```

Expected output:

```text
Probability: 0.5
```

## 3. Basic Properties and Axioms of Probability

Probability follows three fundamental axioms.

### 3.1 Non-negativity

The probability of any event cannot be negative.

$$
P(A)\geq 0
$$

### 3.2 Normalization

The probability of the entire sample space is 1.

$$
P(S)=1
$$

This means that an outcome in the sample space must occur.

### 3.3 Additivity

If two events \(A\) and \(B\) are mutually exclusive, their probabilities can be added to find the probability that either event occurs.

$$
P(A\cup B)=P(A)+P(B)
$$

This rule applies when the events cannot occur together.

For any event \(A\), its probability must satisfy:

$$
0\leq P(A)\leq 1
$$

These properties form the foundation of the probability rules discussed in the following sections.

## 4. Complement of an Event

The complement of an event \(A\), written as \(A^c\), represents the event that \(A\) does not occur.

The complement rule is:

$$
P(A^c)=1-P(A)
$$

Equivalently:

$$
P(A)+P(A^c)=1
$$

**Worked example**

Suppose the probability of passing an examination is 0.8. Find the probability of not passing.

Let \(A\) represent passing the examination.

$$
P(A)=0.8
$$

Using the complement rule:

$$
P(A^c)=1-0.8=0.2
$$

**Answer:** The probability of not passing is 0.2, or 20%.

The complement rule is useful when calculating the probability of an event not occurring. It is also helpful when the probability of the opposite event is easier to calculate.

**Python implementation**

```python
probability_passing = 0.8

probability_not_passing = 1 - probability_passing

print("Probability of passing:", probability_passing)
print("Probability of not passing:", probability_not_passing)
```

## 5. Union and Intersection of Events

Event operations help us describe combinations of events mathematically.

Consider rolling a die.

Let:

$$
A=\{2,4,6\}
$$

Here, \(A\) represents getting an even number.

Let:

$$
B=\{4,5,6\}
$$

Here, \(B\) represents getting a number greater than 3.

### 5.1 Union of Events

The union \(A\cup B\) means that event \(A\) occurs, event \(B\) occurs, or both events occur.

$$
A\cup B=\{2,4,5,6\}
$$

The union includes every outcome belonging to at least one of the events.

### 5.2 Intersection of Events

The intersection \(A\cap B\) contains the outcomes common to both events.

$$
A\cap B=\{4,6\}
$$

Both events occur when the result is either 4 or 6.

### 5.3 Summary of Event Operations

| Operation | Meaning |
|---|---|
| \(A\cup B\) | At least one event occurs |
| \(A\cap B\) | Both events occur |
| \(A^c\) | Event \(A\) does not occur |

**Python implementation**

```python
A = {2, 4, 6}
B = {4, 5, 6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Complement of A:", {1, 2, 3, 4, 5, 6} - A)
```

Expected output, allowing for different set display orders:

```text
Union: {2, 4, 5, 6}
Intersection: {4, 6}
Complement of A: {1, 3, 5}
```

The complement calculation requires the sample space to be specified.

## 6. Addition Rule of Probability

The addition rule calculates the probability that event \(A\), event \(B\), or both occur.

For any two events:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

We subtract the intersection because it is counted twice when adding the individual event probabilities.

**Worked example**

Suppose:

$$
P(A)=0.5
$$

$$
P(B)=0.4
$$

$$
P(A\cap B)=0.2
$$

Using the addition rule:

$$
P(A\cup B)=0.5+0.4-0.2
$$

$$
P(A\cup B)=0.7
$$

**Answer:** The probability that at least one event occurs is 0.7, or 70%.

### 6.1 Mutually Exclusive Events

Two events are mutually exclusive if they cannot occur simultaneously.

For mutually exclusive events:

$$
P(A\cap B)=0
$$

Therefore, the addition rule becomes:

$$
P(A\cup B)=P(A)+P(B)
$$

For example, on a single die roll, getting a 2 and getting a 5 are mutually exclusive outcomes.

**Important:** Mutually exclusive events are not necessarily independent. Two mutually exclusive events with positive probabilities are dependent because the occurrence of one prevents the other from occurring.

**Python implementation**

```python
probability_A = 0.5
probability_B = 0.4
probability_intersection = 0.2

probability_union = (
    probability_A
    + probability_B
    - probability_intersection
)

print("Probability of A or B:", probability_union)
```

## 7. Conditional Probability

Conditional probability is the probability of an event occurring given that another event has already occurred.

It is represented by \(P(A\mid B)\), read as "the probability of A given B."

The formula is:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

This formula requires \(P(B)>0\).

Here:

- \(P(A\mid B)\) is the probability of \(A\) given \(B\).
- \(P(A\cap B)\) is the probability that both events occur.
- \(P(B)\) is the probability of the given event \(B\).

**Worked example**

A card is selected from a standard deck of 52 cards. Given that the selected card is a face card, find the probability that it is a king.

A standard deck contains 12 face cards: four jacks, four queens, and four kings.

The number of kings among the face cards is four.

$$
P(\text{King}\mid\text{Face Card})=\frac{4}{12}
$$

$$
P(\text{King}\mid\text{Face Card})=\frac{1}{3}
$$

**Answer:** The probability is one-third, approximately 33.33%.

The condition reduces the relevant possibilities from all 52 cards to the 12 face cards.

### 7.1 Joint Probability

Joint probability is the probability that two or more events occur together.

It is represented by:

$$
P(A\cap B)
$$

For example, if \(A\) means that a student studies mathematics and \(B\) means that the student passes an examination, then \(P(A\cap B)\) represents the probability that both events occur.

Joint probability and conditional probability are different. Joint probability considers both events together, whereas conditional probability considers one event under a given condition.

**Python implementation**

```python
kings = 4
face_cards = 12

probability_king_given_face_card = kings / face_cards

print(
    "P(King | Face Card):",
    probability_king_given_face_card
)
```

## 8. Multiplication Rule of Probability

The multiplication rule calculates the probability that two events occur together.

From the definition of conditional probability:

$$
P(A\cap B)=P(A\mid B)P(B)
$$

Equivalently:

$$
P(A\cap B)=P(B\mid A)P(A)
$$

These formulas apply when the relevant conditional probabilities are defined.

**Worked example**

Suppose:

$$
P(B)=0.5
$$

and:

$$
P(A\mid B)=0.4
$$

Then:

$$
P(A\cap B)=0.4\times0.5
$$

$$
P(A\cap B)=0.2
$$

**Answer:** The probability that both events occur is 0.2.

**Python implementation**

```python
probability_B = 0.5
probability_A_given_B = 0.4

probability_intersection = (
    probability_A_given_B * probability_B
)

print("P(A and B):", probability_intersection)
```

## 9. Independent Events

Two events \(A\) and \(B\) are independent if the occurrence of one event does not change the probability of the other event.

For independent events:

$$
P(A\mid B)=P(A)
$$

when \(P(B)>0\).

The multiplication rule becomes:

$$
P(A\cap B)=P(A)P(B)
$$

**Worked example**

A fair coin is tossed twice.

Let \(A\) represent getting heads on the first toss, and \(B\) represent getting heads on the second toss.

The two tosses are independent.

$$
P(A\cap B)=\frac{1}{2}\times\frac{1}{2}
$$

$$
P(A\cap B)=\frac{1}{4}
$$

**Answer:** The probability of getting heads on both tosses is 0.25, or 25%.

### 9.1 Independent vs Mutually Exclusive Events

| Independent Events | Mutually Exclusive Events |
|---|---|
| One event does not change the probability of the other | The events cannot occur together |
| Their intersection satisfies \(P(A\cap B)=P(A)P(B)\) | Their intersection has probability zero |
| Both can occur together | Both cannot occur together |
| Example: heads on two separate fair coin tosses | Example: getting a 2 and a 5 on one die roll |

**Python implementation**

```python
probability_first_heads = 0.5
probability_second_heads = 0.5

probability_both_heads = (
    probability_first_heads * probability_second_heads
)

print("Probability of two heads:", probability_both_heads)
```

## 10. Law of Total Probability

The law of total probability calculates the probability of an event by dividing the sample space into mutually exclusive and exhaustive cases.

If \(B_1,B_2,\ldots,B_n\) form a partition of the sample space, then:

$$
P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)
$$

For two cases:

$$
P(A)=P(A\mid B_1)P(B_1)+P(A\mid B_2)P(B_2)
$$

**Worked example: Factory Defects**

A factory uses two machines to produce items.

- Machine 1 produces 60% of the items, and 2% of its items are defective.
- Machine 2 produces 40% of the items, and 5% of its items are defective.

Let \(D\) represent the event that an item is defective.

The overall probability of a defective item is:

$$
P(D)=P(D\mid M_1)P(M_1)+P(D\mid M_2)P(M_2)
$$

Substitute the values:

$$
P(D)=(0.02)(0.60)+(0.05)(0.40)
$$

$$
P(D)=0.012+0.020
$$

$$
P(D)=0.032=3.2\%
$$

**Answer:** The probability that a randomly selected item is defective is 3.2%.

**Python implementation**

```python
machine_1_share = 0.60
machine_2_share = 0.40

defect_rate_1 = 0.02
defect_rate_2 = 0.05

overall_defect_probability = (
    defect_rate_1 * machine_1_share
    + defect_rate_2 * machine_2_share
)

print("Overall defect probability:", overall_defect_probability)
print("Overall defect percentage:", overall_defect_probability * 100, "%")
```

## 11. Bayes' Theorem

Bayes' theorem calculates the probability of an event using new evidence. It allows us to update an initial probability after observing relevant information.

The theorem is:

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

This formula requires \(P(B)>0\).

### 11.1 Important Terms in Bayes' Theorem

**Prior probability**

The prior probability is the probability of an event before considering new evidence.

$$
P(A)
$$

**Likelihood**

The likelihood describes the probability of observing the evidence when a particular event or hypothesis is true.

$$
P(B\mid A)
$$

**Evidence**

The evidence is the overall probability of observing the available information.

$$
P(B)
$$

**Posterior probability**

The posterior probability is the updated probability of an event after considering the evidence.

$$
P(A\mid B)
$$

Bayes' theorem combines these quantities:

$$
\text{Posterior}=\frac{\text{Likelihood}\times\text{Prior}}{\text{Evidence}}
$$

This is a conceptual description of the theorem, not a separate probability formula.

### 11.2 Calculating Evidence

For an event \(A\) and its complement \(A^c\), the total probability of observing evidence \(B\) is:

$$
P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)
$$

This form is useful when evidence can occur whether or not event \(A\) occurs.

### 11.3 Worked Example: Medical Test

Suppose:

- 1% of people have a particular disease.
- The test correctly gives a positive result for 95% of people who have the disease.
- The test gives a negative result for 95% of people who do not have the disease.

Find the probability that a person actually has the disease given a positive test result.

Let:

- \(D\): The person has the disease.
- \(+\): The test result is positive.

Given:

$$
P(D)=0.01
$$

$$
P(D^c)=0.99
$$

$$
P(+\mid D)=0.95
$$

The specificity is 95%, so the false-positive rate is:

$$
P(+\mid D^c)=1-0.95=0.05
$$

First, calculate the overall probability of a positive result:

$$
P(+)=P(+\mid D)P(D)+P(+\mid D^c)P(D^c)
$$

Substitute the values:

$$
P(+)=(0.95)(0.01)+(0.05)(0.99)
$$

$$
P(+)=0.0095+0.0495=0.059
$$

Now apply Bayes' theorem:

$$
P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+)}
$$

$$
P(D\mid +)=\frac{0.95\times0.01}{0.059}
$$

$$
P(D\mid +)=\frac{0.0095}{0.059}
$$

$$
P(D\mid +)\approx0.1610=16.10\%
$$

**Answer:** The probability that a person has the disease after a positive result is approximately 16.10%, under the stated assumptions.

Although the test has 95% sensitivity and 95% specificity, the posterior probability is much lower because the disease is uncommon in the population.

This example demonstrates why the prior probability, also called the base rate, matters when interpreting test results.

**Python implementation**

```python
prior = 0.01
sensitivity = 0.95
specificity = 0.95

false_positive_rate = 1 - specificity

positive_probability = (
    sensitivity * prior
    + false_positive_rate * (1 - prior)
)

posterior = (
    sensitivity * prior
    / positive_probability
)

print("Probability of a positive result:", positive_probability)
print("Probability of disease given a positive result:", posterior)
print("Posterior percentage:", posterior * 100, "%")
```

This calculation is a simplified mathematical illustration. Real medical test interpretation depends on the validity of the test characteristics and the population to which they apply.

## 12. Probability Tree Diagram

A probability tree diagram represents possible outcomes and their probabilities across multiple stages of an experiment.

The probability of a path is calculated by multiplying the probabilities along that path. If multiple mutually exclusive paths lead to the same event, their probabilities can be added.

For example, suppose a fair coin is tossed twice.

The probability of getting heads on both tosses is:

$$
P(HH)=P(H)\times P(H)
$$

$$
P(HH)=\frac{1}{2}\times\frac{1}{2}=\frac{1}{4}
$$

A tree for two coin tosses has four possible paths: HH, HT, TH, and TT. Each path has probability one-quarter.

Probability trees are useful for conditional probability, the law of total probability, and Bayes' theorem.

**Python implementation**

```python
from itertools import product

outcomes = list(product(["H", "T"], repeat=2))

for outcome in outcomes:
    probability = 0.5 * 0.5
    print(outcome, "Probability:", probability)
```

The example enumerates the four possible outcomes of two independent fair coin tosses.

## 13. Empirical Probability

Empirical probability is calculated using observed data or experimental results.

$$
P(A)=\frac{\text{Observed occurrences of A}}{\text{Total trials}}
$$

**Worked example**

A coin is tossed 100 times, and heads occurs 54 times.

$$
P(H)=\frac{54}{100}=0.54
$$

**Answer:** The empirical probability of heads is 0.54, or 54%.

Unlike classical probability, empirical probability is based on observed frequencies rather than assuming equally likely outcomes.

As the number of trials increases, empirical probabilities may approach theoretical probabilities under suitable conditions. They are not guaranteed to equal the theoretical probability in a finite experiment.

**Python implementation**

```python
observed_heads = 54
total_tosses = 100

empirical_probability = observed_heads / total_tosses

print("Empirical probability of heads:", empirical_probability)
print("Empirical percentage:", empirical_probability * 100, "%")
```

Empirical probability is useful in Data Science when estimating event frequencies from historical datasets.

## 14. Common Probability Mistakes

### 14.1 Confusing Union and Intersection

The union \(A\cup B\) means that at least one event occurs. The intersection \(A\cap B\) means that both events occur.

### 14.2 Adding Probabilities Without Subtracting the Overlap

For general events, use:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

Simply adding \(P(A)\) and \(P(B)\) is correct when the events are mutually exclusive.

### 14.3 Confusing Independent and Mutually Exclusive Events

Independent events do not change each other's probabilities. Mutually exclusive events cannot occur together. These concepts are not interchangeable.

### 14.4 Ignoring the Condition in Conditional Probability

When calculating \(P(A\mid B)\), restrict attention to cases in which \(B\) has occurred.

### 14.5 Ignoring the Base Rate in Bayes' Theorem

Sensitivity and specificity alone do not determine the probability that a person has a condition after a positive result. The prior probability must also be considered.

### 14.6 Applying Classical Probability to Unequal Outcomes

The classical formula assumes equally likely outcomes. When outcomes are not equally likely, use the appropriate probability model or observed data.

## 15. Points to Remember

1. Probability measures uncertainty and takes values between 0 and 1.
2. The sample space contains all possible outcomes.
3. An event is a collection of outcomes.
4. Classical probability assumes equally likely outcomes.
5. The complement rule calculates the probability that an event does not occur.
6. The union represents at least one event occurring.
7. The intersection represents both events occurring.
8. The general addition rule subtracts the probability of the intersection.
9. Conditional probability incorporates known information.
10. The multiplication rule calculates the probability of events occurring together.
11. Independent events do not change each other's probabilities.
12. Mutually exclusive events cannot occur together.
13. The law of total probability combines mutually exclusive and exhaustive cases.
14. Bayes' theorem updates probabilities using evidence.
15. Prior probability is important when interpreting evidence.
16. Empirical probability is calculated from observed frequencies.
17. Python sets can represent finite events, while ordinary calculations can implement probability rules directly.
18. Probability is a foundation for Bayesian inference and probabilistic machine learning.

## 16. Probability Formula Summary

**Classical probability**

$$
P(A)=\frac{\text{Favourable outcomes}}{\text{Total equally likely outcomes}}
$$

**Complement rule**

$$
P(A^c)=1-P(A)
$$

**General addition rule**

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

**Addition rule for mutually exclusive events**

$$
P(A\cup B)=P(A)+P(B)
$$

**Conditional probability**

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

**Multiplication rule**

$$
P(A\cap B)=P(A\mid B)P(B)
$$

**Multiplication rule for independent events**

$$
P(A\cap B)=P(A)P(B)
$$

**Law of total probability**

$$
P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)
$$

**Bayes' theorem**

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

**Empirical probability**

$$
P(A)=\frac{\text{Observed occurrences}}{\text{Total trials}}
$$

## 17. Chapter Summary

Probability provides a mathematical framework for understanding uncertainty and evaluating possible outcomes.

Sample spaces and events define the outcomes being studied. Complement, union, and intersection operations describe relationships between events. Addition and multiplication rules calculate probabilities involving multiple events, while conditional probability incorporates known information.

The law of total probability combines alternative cases to calculate an overall probability. Bayes' theorem uses evidence to update an initial probability, making it especially useful in Bayesian inference, classification, and decision-making.

In practical Data Science, probability concepts are applied to historical data, risk estimation, probabilistic models, and uncertainty analysis. Python can help implement these rules and verify calculations.

## 18. References and Further Reading

### Learning Resources

- [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)
- [GeeksforGeeks — Probability](https://www.geeksforgeeks.org/maths/probability/)
- [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
- [Wikipedia — Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)

### Related Topics in This Repository

- Statistics Fundamentals
- Descriptive Statistics
- Probability Distributions
- Inferential Statistics
- Hypothesis Testing
- Statistics for Machine Learning
