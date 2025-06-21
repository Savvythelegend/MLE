## 1. Types of Statistics

### 🔹 Descriptive Statistics
Summarizes or describes a dataset.
- Examples: Mean, Median, Mode, Standard Deviation

### 🔹 Inferential Statistics
Draws conclusions about a population based on a sample.
- Examples: Hypothesis Testing, Confidence Intervals

---

## 2. Types of Data Analysis

### 🔹 Descriptive Analysis
What happened?

### 🔹 Predictive Analysis
What will happen?

---

## 3. Population vs Sample

- **Population**: The entire group.
- **Sample**: A subset of the population.

---

## 4. Measures of Central Tendency

### Mean

```python
import numpy as np
data = [10, 20, 30, 40]
np.mean(data)
````

### Median

```python
np.median(data)
```

### Mode

```python
from scipy import stats
stats.mode(data, keepdims=True)
```

---

## 5. Measures of Spread

### Range

```python
range_ = max(data) - min(data)
print(range_)
```

### Variance

```python
np.var(data)
```

### Standard Deviation

```python
np.std(data)
```

---

## 6. Probability Basics

* **Experiment**: A process with uncertain results
* **Sample Space**: All possible outcomes
* **Event**: A subset of the sample space

---

## 7. Types of Probability

### Marginal Probability

```python
# P(A)
```

### Joint Probability

```python
# P(A and B)
```

### Conditional Probability

```python
# P(A | B) = P(A and B) / P(B)
```

---

## 8. Bayes’ Theorem

```python
# P(A | B) = (P(B | A) * P(A)) / P(B)
```

---

## 9. Independence

```python
# Two events A and B are independent if:
# P(A and B) = P(A) * P(B)
```

---

## 10. Z-score

```python
X = 75
mean = 70
std = 5
z = (X - mean) / std
print(z)
```

---

## 11. Hypothesis Testing

* **Null Hypothesis (H₀)**: No effect
* **Alternative Hypothesis (H₁)**: There is an effect

---

## 12. P-value

```python
# P-value is the probability of observing data at least as extreme as the observed,
# assuming H₀ is true
```

---

## 13. Significance Level (α)

```python
alpha = 0.05
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
```

---

## 14. Confidence Interval

```python
import scipy.stats as st
data = [10, 20, 30, 40, 50]
confidence = 0.95
st.t.interval(confidence, len(data)-1, loc=np.mean(data), scale=st.sem(data))
```

---

## 15. Confidence vs Significance

* Confidence Level = 1 - α
* Confidence Interval: Gives a range of values
* Significance Testing: Gives a binary decision

---

## 16. Application in ML

* Descriptive Stats → EDA
* Inferential Stats → AB Testing, Evaluation
* Probability → Naive Bayes, Randomness
* Hypothesis Testing → Model Comparison
* Confidence Intervals → Reporting uncertainty in metrics

