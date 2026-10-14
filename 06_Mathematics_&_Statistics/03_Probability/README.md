# Probability

## 1. Introduction to Probability

Probability is a branch of mathematics that measures the likelihood of an event occurring. It helps us understand uncertainty and make decisions based on possible outcomes.

Probability values range from 0 to 1.

- **Probability = 0:** The event is impossible.
- **Probability = 1:** The event is certain.
- **Probability = 0.5:** The event has a 50% chance of occurring.

For example, when a fair coin is tossed, the probability of getting heads is 1/2.

## 2. Random Experiment

A random experiment is an experiment whose exact outcome cannot be predicted with certainty before it is performed, even when the conditions are known.

**Examples:**

- Tossing a coin.
- Rolling a die.
- Drawing a card from a deck.
- Selecting a student randomly from a class.

## 3. Outcome

An outcome is a possible result of a random experiment.

For example, when a die is rolled, getting 1, 2, 3, 4, 5, or 6 are possible outcomes.

## 4. Sample Space

The sample space is the set of all possible outcomes of a random experiment. It is usually represented by \(S\) or \(\Omega\).

For a coin toss:

\[
S = \{H,T\}
\]

For a die roll:

\[
S = \{1,2,3,4,5,6\}
\]

Here, \(H\) represents heads and \(T\) represents tails.

## 5. Event

An event is a collection of one or more outcomes of a random experiment. It is usually represented by a capital letter such as \(A\), \(B\), or \(C\).

For example, when a die is rolled, let event \(A\) represent getting an even number.

\[
A = \{2,4,6\}
\]

An event occurs when the observed outcome belongs to that event.

## 6. Classical Probability

When all outcomes are equally likely, the probability of an event is the ratio of the number of favourable outcomes to the total number of possible outcomes.

\[
P(A)=\frac{\text{Number of favourable outcomes}}{\text{Total number of equally likely outcomes}}
\]

For example, when a fair die is rolled, the probability of getting an even number is:

\[
P(A)=\frac{3}{6}=\frac{1}{2}
\]

This formula applies when the possible outcomes are equally likely.

## 7. Basic Properties and Axioms of Probability

Probability follows three fundamental axioms.

### 7.1 Non-negativity

The probability of any event cannot be negative.

\[
P(A)\geq 0
\]

### 7.2 Normalization

The probability of the entire sample space is 1.

\[
P(S)=1
\]

This means that some outcome in the sample space must occur.

### 7.3 Additivity

If two events \(A\) and \(B\) are mutually exclusive, their probabilities can be added to find the probability that either event occurs.

\[
P(A\cup B)=P(A)+P(B)
\]

This rule applies when \(A\) and \(B\) cannot occur together.

## 8. Complement of an Event

The complement of an event \(A\), written as \(A^c\) or \(A'\), represents the event that \(A\) does not occur.

The complement rule is:

\[
P(A^c)=1-P(A)
\]

Therefore,

\[
P(A)+P(A^c)=1
\]

**Example:**

If the probability of passing an examination is 0.8, the probability of not passing is:

\[
P(A^c)=1-0.8=0.2
\]

## 9. Union of Events

The union of two events, written as \(A\cup B\), means that event \(A\) occurs, event \(B\) occurs, or both events occur.

For example, when a die is rolled, let:

\[
A=\{2,4,6\}
\]

\[
B=\{4,5,6\}
\]

Then,

\[
A\cup B=\{2,4,5,6\}
\]

The union includes every outcome that belongs to at least one of the two events.

## 10. Intersection of Events

The intersection of two events, written as \(A\cap B\), represents the outcomes common to both events. In other words, both events occur.

Using the previous example:

\[
A=\{2,4,6\}
\]

\[
B=\{4,5,6\}
\]

Therefore,

\[
A\cap B=\{4,6\}
\]

**Remember:**

- \(A\cup B\): At least one of the events occurs.
- \(A\cap B\): Both events occur.
- \(A^c\): Event \(A\) does not occur.

## 11. Addition Rule of Probability

The addition rule calculates the probability that event \(A\), event \(B\), or both occur.

For any two events:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]

We subtract the intersection because it is counted twice when \(P(A)\) and \(P(B)\) are added.

**Example:**

Suppose:

\[
P(A)=0.5,\quad P(B)=0.4
\]

and

\[
P(A\cap B)=0.2
\]

Then,

\[
P(A\cup B)=0.5+0.4-0.2
\]

\[
\boxed{P(A\cup B)=0.7}
\]

## 12. Mutually Exclusive Events

Two events are mutually exclusive if they cannot occur simultaneously.

For mutually exclusive events:

\[
P(A\cap B)=0
\]

Therefore, the addition rule becomes:

\[
P(A\cup B)=P(A)+P(B)
\]

**Example:**

When a single die is rolled, getting a 2 and getting a 5 are mutually exclusive events. A single roll cannot produce both results.

**Important:** Mutually exclusive events are not necessarily independent. In fact, two mutually exclusive events with positive probabilities are dependent.

## 13. Conditional Probability

Conditional probability is the probability of an event occurring given that another event has already occurred.

It is represented by \(P(A\mid B)\), which is read as "the probability of \(A\) given \(B\)."

The formula is:

\[
\boxed{P(A\mid B)=\frac{P(A\cap B)}{P(B)}}
\]

where \(P(B)>0\).

Here:

- \(P(A\mid B)\) is the conditional probability of \(A\) given \(B\).
- \(P(A\cap B)\) is the probability that both events occur.
- \(P(B)\) is the probability of the given event \(B\).

**Example:**

A card is selected from a standard deck of 52 cards. Given that the selected card is a face card, find the probability that it is a king.

A standard deck has 12 face cards: 4 jacks, 4 queens, and 4 kings.

\[
P(\text{King}\mid\text{Face Card})
=\frac{4}{12}
\]

\[
\boxed{P(\text{King}\mid\text{Face Card})=\frac{1}{3}}
\]

The condition reduces the relevant possibilities from all 52 cards to the 12 face cards.

## 14. Joint Probability

Joint probability is the probability that two or more events occur together.

It is represented by:

\[
P(A\cap B)
\]

For example, if \(A\) means that a student studies mathematics and \(B\) means that the student passes an examination, then \(P(A\cap B)\) represents the probability that both events occur.

Joint probability is different from conditional probability. Joint probability considers both events together, whereas conditional probability considers the probability of one event under a given condition.

## 15. Multiplication Rule of Probability

The multiplication rule is used to calculate the probability that two events occur together.

From the definition of conditional probability:

\[
\boxed{P(A\cap B)=P(A\mid B)P(B)}
\]

Equivalently,

\[
\boxed{P(A\cap B)=P(B\mid A)P(A)}
\]

These formulas apply when the relevant conditional probabilities are defined.

**Example:**

Suppose:

\[
P(B)=0.5
\]

and

\[
P(A\mid B)=0.4
\]

Then,

\[
P(A\cap B)=0.4\times0.5
\]

\[
\boxed{P(A\cap B)=0.2}
\]

## 16. Independent Events

Two events \(A\) and \(B\) are independent if the occurrence of one event does not change the probability of the other event.

For independent events:

\[
P(A\mid B)=P(A)
\]

when \(P(B)>0\).

The multiplication rule becomes:

\[
\boxed{P(A\cap B)=P(A)P(B)}
\]

**Example:**

A fair coin is tossed twice. Let \(A\) be getting heads on the first toss and \(B\) be getting heads on the second toss.

The tosses are independent.

\[
P(A\cap B)=\frac{1}{2}\times\frac{1}{2}
\]

\[
\boxed{P(A\cap B)=\frac{1}{4}}
\]

**Important:** Independent events and mutually exclusive events are different concepts.

## 17. Law of Total Probability

The law of total probability calculates the probability of an event by dividing the sample space into mutually exclusive and exhaustive cases.

If \(B_1,B_2,\ldots,B_n\) form a partition of the sample space, then:

\[
\boxed{P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)}
\]

For two cases:

\[
P(A)=P(A\mid B_1)P(B_1)+P(A\mid B_2)P(B_2)
\]

**Example:**

A factory uses two machines to produce items.

- Machine 1 produces 60% of the items, and 2% of its items are defective.
- Machine 2 produces 40% of the items, and 5% of its items are defective.

Let \(D\) represent the event that an item is defective.

\[
P(D)=P(D\mid M_1)P(M_1)+P(D\mid M_2)P(M_2)
\]

Substituting the values:

\[
P(D)=(0.02)(0.60)+(0.05)(0.40)
\]

\[
P(D)=0.012+0.020
\]

\[
\boxed{P(D)=0.032=3.2\%}
\]

Therefore, the probability that a randomly selected item is defective is 3.2%.

## 18. Bayes' Theorem

Bayes' theorem calculates the probability of an event using new evidence. It allows us to update an initial probability after observing relevant information.

The theorem is:

\[
\boxed{P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}}
\]

where \(P(B)>0\).

### 18.1 Prior Probability

The prior probability is the probability of an event before considering the new evidence.

It is represented by:

\[
P(A)
\]

For example, if 1% of a population has a disease, the prior probability of having the disease is 0.01.

### 18.2 Likelihood

The likelihood describes the probability of observing the evidence when a particular event or hypothesis is true.

It is represented by:

\[
P(B\mid A)
\]

For example, it is the probability that a medical test returns positive when a person actually has the disease.

### 18.3 Evidence

The evidence is the overall probability of observing the available information.

It is represented by:

\[
P(B)
\]

Using the law of total probability:

\[
P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)
\]

### 18.4 Posterior Probability

The posterior probability is the updated probability of an event after considering the evidence.

It is represented by:

\[
P(A\mid B)
\]

Bayes' theorem combines the prior, likelihood, and evidence:

\[
\boxed{\text{Posterior}=\frac{\text{Likelihood}\times\text{Prior}}{\text{Evidence}}}
\]

This is a conceptual description of the theorem, not a separate probability formula.

### 18.5 Worked Example: Medical Test

Suppose:

- 1% of people have a particular disease.
- The test correctly gives a positive result for 95% of people who have the disease.
- The test gives a negative result for 95% of people who do not have the disease.

Find the probability that a person actually has the disease given a positive test result.

Let:

- \(D\): The person has the disease.
- \(+\): The test result is positive.

Given:

\[
P(D)=0.01
\]

\[
P(D^c)=0.99
\]

\[
P(+\mid D)=0.95
\]

The specificity is 95%, so the false-positive rate is:

\[
P(+\mid D^c)=1-0.95=0.05
\]

Using Bayes' theorem:

\[
P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+)}
\]

First, calculate the overall probability of a positive result:

\[
P(+)=P(+\mid D)P(D)+P(+\mid D^c)P(D^c)
\]

\[
P(+)=(0.95)(0.01)+(0.05)(0.99)
\]

\[
P(+)=0.0095+0.0495=0.059
\]

Now calculate the posterior probability:

\[
P(D\mid +)=\frac{(0.95)(0.01)}{0.059}
\]

\[
P(D\mid +)=\frac{0.0095}{0.059}
\]

\[
\boxed{P(D\mid +)\approx 0.1610=16.10\%}
\]

Although the test has 95% sensitivity and 95% specificity, the probability that a person has the disease after receiving a positive result is approximately 16.10% under these assumptions.

This example demonstrates why the prior probability, also called the base rate, matters when interpreting test results.

## 19. Probability Tree Diagram

A probability tree diagram represents possible outcomes and their probabilities across multiple stages of an experiment.

The probability of a path is calculated by multiplying the probabilities along that path.

For example, suppose a fair coin is tossed twice.

The probability of getting heads on both tosses is:

\[
P(HH)=P(H)\times P(H)
\]

\[
P(HH)=\frac{1}{2}\times\frac{1}{2}=\frac{1}{4}
\]

If different paths lead to the same event, add the probabilities of those paths when they are mutually exclusive.

Probability trees are particularly useful for conditional probability, the law of total probability, and Bayes' theorem.

## 20. Empirical Probability

Empirical probability is calculated using observed data or experimental results.

\[
\boxed{P(A)=\frac{\text{Number of times event }A\text{ occurs}}{\text{Total number of trials}}}
\]

**Example:**

A coin is tossed 100 times, and heads occurs 54 times.

\[
P(H)=\frac{54}{100}=0.54
\]

The empirical probability of heads is 0.54, or 54%.

Unlike classical probability, empirical probability is based on observed frequencies rather than assuming equally likely outcomes.

## 21. Common Probability Mistakes

### 21.1 Confusing Union and Intersection

The union \(A\cup B\) means that at least one event occurs. The intersection \(A\cap B\) means that both events occur.

### 21.2 Adding Probabilities Without Subtracting the Overlap

For general events, use:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]

Simply adding \(P(A)\) and \(P(B)\) is correct when the events are mutually exclusive.

### 21.3 Confusing Independent and Mutually Exclusive Events

Independent events do not change each other's probabilities. Mutually exclusive events cannot occur together.

### 21.4 Ignoring the Condition in Conditional Probability

When calculating \(P(A\mid B)\), restrict attention to the cases in which \(B\) has occurred.

### 21.5 Ignoring the Base Rate in Bayes' Theorem

A test's sensitivity and specificity alone do not determine the probability that a person has a condition after a positive result. The prior probability must also be considered.

## 22. Probability Formula Summary

| Concept | Formula |
|---|---|
| Classical probability | \(P(A)=\frac{\text{Favourable outcomes}}{\text{Total equally likely outcomes}}\) |
| Complement rule | \(P(A^c)=1-P(A)\) |
| General addition rule | \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\) |
| Mutually exclusive events | \(P(A\cup B)=P(A)+P(B)\) |
| Conditional probability | \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\) |
| Multiplication rule | \(P(A\cap B)=P(A\mid B)P(B)\) |
| Independent events | \(P(A\cap B)=P(A)P(B)\) |
| Total probability | \(P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i)\) |
| Bayes' theorem | \(P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}\) |
| Empirical probability | \(P(A)=\frac{\text{Observed occurrences}}{\text{Total trials}}\) |

## 23. Points to Remember

Probability measures uncertainty and assigns values between 0 and 1 to events. The sample space contains all possible outcomes, while an event contains the outcomes of interest.

The complement rule is useful when calculating the probability that an event does not occur. The addition rule handles the probability that at least one of two events occurs, and the multiplication rule handles the probability that both events occur.

Conditional probability incorporates known information. Independence means that one event does not affect the probability of another, whereas mutually exclusive events cannot occur together.

The law of total probability combines different possible cases to calculate an overall probability. Bayes' theorem reverses conditional probabilities and updates an initial probability using observed evidence.

## 24. References

1. [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)
2. [GeeksforGeeks — Probability](https://www.geeksforgeeks.org/maths/probability/)
3. [OpenStax — Introductory Statistics](https://openstax.org/details/books/introductory-statistics)
4. [Wikipedia — Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
