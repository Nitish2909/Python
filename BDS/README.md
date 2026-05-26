# Inferential Statistics:
Inferential statistics is a branch of statistics used to make predictions, conclusions, or decisions about a large group of data (population) by studying only a smaller part of it (sample). It helps researchers understand patterns, test assumptions, compare results, and estimate future outcomes without examining every individual item. Inferential statistics is widely used in business, medicine, education, economics, and data science. It uses mathematical methods such as hypothesis testing, confidence intervals, regression, and probability analysis to determine whether observed results are meaningful or happened by chance. It is very useful for research, surveys, forecasting, and decision-making processes.

<b>Some real life Example are :</b>

```bash

1. Political Polls

2. Medical

3. Environmental Studies

4. Market Research

```
***Types Inferential Statistics***

<b>1. Hypothesis Testing :</b>

Hypothesis testing is a statistical method used to determine whether a statement or assumption about a population is true or false using sample data. It compares observed results with expected results and helps in making decisions based on probability and significance levels. It is widely used in business, science, medicine, education, and machine learning for decision-making, quality control, and research analysis. Hypothesis testing reduces uncertainty and helps identify whether results occurred by chance or due to a real effect.

<b>Example:</b>

```bash
from scipy.stats import ttest_1samp

# Sample data
marks = [72, 75, 78, 74, 77, 80, 73]

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(marks, 70)

# Display results
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Decision making
if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")

```

<b>General Steps of Hypothesis Testing :</b>

```bash
1. Define Hypothesis:

Null Hypothesis (H₀) -> No significant effect
Alternative Hypothesis (H₁) -> Significant effect exists
Example
H₀: Average marks = 70
H₁: Average marks ≠ 70


2. Choose Significance Level

The significance level (α) is usually 0.05. This means 95% confidence level.

3. Select Statistical Test

Choose an appropriate test based on data type:

T-Test
Chi-Square Test
Z-Test
ANOVA

4. Calculate Test Statistic

Use formulas or statistical software to calculate the test value.

5. Make Decision:

Compare the p-value to the significance level:

If p < 0.05, you reject the null hypothesis.
If p > 0.05, you fail to reject the null hypothesis.

6. Draw Conclusion

Interpret the result and make the final decision.

```


<b>Types of Hypothesis Testing :</b>

1. Null Hypothesis (H₀) :

The null hypothesis states that there is no significant difference, relationship, or effect between variables. It assumes that any observed variation happened only due to chance or random error.

Example:

There is no difference in marks between online and offline teaching methods

2. Alternative Hypothesis (H₁):

he alternative hypothesis states that a significant difference, relationship, or effect exists between variables. It is accepted when sufficient evidence rejects the null hypothesis.

Example

Online teaching improves student marks compared to offline teaching.

