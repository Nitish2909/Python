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


<b>2. T- Test </b>

A T-test is an inferential statistical method used to compare the means of two groups or compare a sample mean with a known value. It helps determine whether the difference between values is statistically significant or occurred by chance. T-tests are commonly used in research, education, medicine, and data analysis when the sample size is small and population variance is unknown.

<b>Example:</b>

```bash
from scipy.stats import ttest_1samp

# Sample marks
marks = [72, 75, 78, 74, 77, 80, 73]

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(marks, 70)

# Display result
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Decision making
if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")

```

<b>Types of T-Test :</b>

1. One-Sample T-Test:

A one-sample t-test compares the mean of a single sample with a known or assumed population mean to check whether there is a significant difference between them.

Example

Checking whether the average marks of students differ from the school average of 70.

2. Independent T-Test

An independent t-test compares the means of two different independent groups to determine whether their averages are significantly different.

Example

Comparing marks of students from two different classes.

3. Paired T-Test

A paired t-test compares two related observations, such as before and after measurements on the same group, to identify significant changes.

Example

Comparing student performance before and after training.



<b>3. Chi-Square Test </b>

A Chi-Square Test is an inferential statistical method used to determine whether there is a significant relationship or association between categorical variables. It compares observed data with expected data to check whether differences occur by chance or due to an actual relationship. The chi-square test is widely used in surveys, research, business analysis, medical studies, and social sciences. It works mainly with frequency data such as counts, categories, or groups. If the difference between observed and expected values is large, the variables are considered related. It helps researchers make decisions and test hypotheses using statistical significance.

<b>Example:</b>

```bash
from scipy.stats import chi2_contingency

# Observed frequency table
data = [[30, 20],
        [25, 25]]

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(data)

# Display results
print("Chi-Square Value:", chi2)
print("P-Value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:")
print(expected)

# Decision
if p < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")

```

# Predictive Modeling:
Predictive modeling is a statistical and machine learning technique used to predict future outcomes using historical data. It analyzes patterns, relationships, and trends in existing data to estimate unknown or future values. Predictive modeling uses algorithms such as regression, classification, decision trees, and neural networks to make accurate predictions. It is widely used in business, healthcare, banking, weather forecasting, marketing, and artificial intelligence. The main goal of predictive modeling is to improve decision-making, reduce risks, and identify future opportunities. The model learns from past data and applies that knowledge to predict future events or behaviors.

<b>1. Decision Trees :</b>

Decision trees are supervised machine learning models used for classification and regression tasks. They represent decisions and possible outcomes in the form of a tree-like structure consisting of nodes, branches, and leaf nodes. A decision tree starts with a root node and splits data into smaller groups based on conditions or rules. Each branch represents a decision, and each leaf node represents the final output or prediction. Decision trees are simple to understand, easy to visualize, and widely used in business, healthcare, banking, and artificial intelligence for prediction and decision-making problems.

Example:
<br>
Student Pass Prediction:

```bash
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Study hours and attendance
X = np.array([
    [2, 60],
    [4, 70],
    [6, 80],
    [8, 90]
])

# Pass(1) or Fail(0)
y = np.array([0, 0, 1, 1])

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict for new student
prediction = model.predict([[5, 75]])

print("Prediction:", prediction[0])

```

<b>2. Logistic Regression :</b>

Logistic regression is a supervised machine learning and statistical technique used for classification problems. It predicts the probability of a categorical outcome, usually binary outcomes such as Yes/No, True/False, or Spam/Not Spam. Unlike linear regression, logistic regression does not predict continuous values; instead, it predicts class probabilities using the logistic (sigmoid) function. It is widely used in healthcare, banking, marketing, fraud detection, and artificial intelligence. Logistic regression helps identify relationships between dependent and independent variables and makes predictions based on probability values between 0 and 1.

Example:

```bash
from sklearn.linear_model import LogisticRegression
import numpy as np

# Study hours
X = np.array([[1], [2], [3], [4], [5], [6]])

# Pass(1) or Fail(0)
y = np.array([0, 0, 0, 1, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict for student studying 4.5 hours
prediction = model.predict([[4.5]])

print("Prediction:", prediction[0])

```



