# What is SciKet-learn ?
SciKet-learn is one of the most popular python library for Machine Learning and Data Analysis.It is built on top of NumPy, Pandas and Matplotlib etc.This Library is used to build and train machine learning models.It provides simple and efficient tools for analyzing data and creating predictive models.
<br>
In Simple words we can say that
Scikit-learn is a Python library that helps developers and data scientists create machine learning models easily using built-in algorithms and tools.
<br>

<b>Installation:</b>

```bash

pip install SciKet-learn

```

<b>Check it version:</b>

```bash

import sklearn
print(sklearn.__version__)
```

<b>Applications of Scikit-learn:</b>

```bash
1. Recommendation systems

2. Fraud detection

3. Medical diagnosis

4. Image classification

5. Sales prediction

5. Customer analysis

```

# Features of Scikit-learn:

<b>1. Simple and Easy to use : </b>
<br>
The first Features of Scikit-learn is it has simple syntax and beginner friendly functions.

Example:

```bash
from sklearn.linear_model import LinearRegression

model = LinearRegression()

```

<b>2. Open Source and Free :</b>
<br>
Scikit-learn is Free to use, Open-source, Community-supported. 

<b>3. Pipline</b>

<b>4. Feature Scaling</b>

<b>5. cross-validation</b>

<b>6. Hyperparameter Tuning</b>


# Some Important Modules of SciKet-learn

<b>1. sklearn.datasets :</b> This modules is used to load/import built-in datasets.Also used for generate sample datasets.some example of built-in datasets are Iris dataset, Wine dataset, Digits dataset.

Example:

```bash
from sklearn.datasets import load_iris

iris = load_iris()

```

<b>2. sklearn.model_selection :</b> This module is used for spliting datasets, cross-validation, Hyperparameter tuning.
<br>
Some important function that comes under model_selection module.

```bash
train_test_split() 
cross_val_score()
GridSearchCV

```

Example:

```bash
from sklearn.model_selection import train_test_split

```

<b>3. sklearn.linear_model :</b>  sklearn.linear_model is a module in Scikit-learn that provides linear machine learning algorithms used for Regression, Classification, Regularization.

Example:

```bash
from sklearn.linear_model import LinearRegression

```

# What is Regression Analysis :
Regression analysis is a statistical method in statistics used to examine or predict the relationship between a dependent variable(output) and one or more independent variable(inputs).
with the goal of prediction and understanding how variable influence each other.
Here Dependent variable (Y) means what you want to predict or explain and Independent variable(s) (X) means the predictors or inputs.
<br>
In Simple words we can say that it is the answer of the "if X changes, how will Y change ?"
<br>
Example: predicting house prices based on size, location, and age.

<b>Types of Regression Analysis :</b>

***1. Linear Regression***

Linear Regression is a supervised machine learning and statistical technique used to find the relationship between an independent variable (X) and a dependent variable (Y) by fitting a straight line through the data points.It is mainly used for prediction, forecasting, understanding relationships between variable.

Example:

```bash

Suppose,

Experiences            Salary
   1                   50000
   2                   60000
   3                   70000
   4                   80000
   5                   90000

 
Here:

 Experiences -> independent variable (X)
 Salary -> dependent variable (Y)

 Linear regression tries to find:

"How much Salary increase when Experiences increase."

```

<b>Implementing Simple linear regression using SciKet-learn :</b>
<br>
Example: Predict salary based on years of experience

```bash
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Experience":[1,2,3,4,5],
    "Salary" : [50000,60000,70000,80000,90000]
}

df = pd.DataFrame(data)

# independent (X) and Dependent (Y)
x = df[["Experience"]]
y = df[["Salary"]]

# split data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

#create model
model = LinearRegression()

#train model
model.fit(x_train, y_train)

#Predict
y_pred = model.predict(x_test)

print("Predicted", y_pred)

```

***Multiple Linear Regression***

Multiple Regression is an extension of simple Linear Regression.Multiple Linear Regression is a type of regression in machine learning and statistics.In this type of regression we use two or more independent variable (input) to predict a single dependent variable(output/target).
<br>
In simple words we can say that studies how multiple factors together affect one output.

Example:

```bash
Suppose we want to predict salary using:
experience
education

Experience	 Education         Salary
2	            12		       30000

4	            16		       50000

Here:

Experience, Education -> independent variables (X)
Salary -> dependent variable (Y)

```

<b>Example using Scikit-learn :</b>

```bash
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'Experience': [1, 2, 3, 4, 5],
    'Education': [10, 12, 12, 16, 18],
    'Salary': [30000, 35000, 40000, 50000, 60000]
}
df = pd.DataFrame(data)

# Independent variables
X = df[['Experience', 'Education']]
y = df['Salary']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Predicted:", y_pred)

```

# Data Analysis Tools:
Scikit-learn (or sklearn) is one of the most popular and powerful Python libraries for data
analysis and machine learning.It provides easy-to-use tools for :

1. Time Series Analysis -> It helps forecast future trends based on past patterns

2. Clustering  -> It identifies natural groupings in unlabeled data.

3. Classification -> It predicts discrete outcomes using labeled data.

Scikit-learn simplifies implementing these techniques with ready-to-use functions.Scikit-learn works well with other Python libraries like NumPy, pandas, and
matplotlib, forming a complete data analysis ecosystem.


# 1. Time Series Analysis :
Time Series Analysis is a statistical and data analysis tools and techniques that is used analysis or study data that changes over time like tempreture, monthly sales and stock prices etc.
It helps to find to patterns( like trends or seasons), Predict future values and understanding how past values affect future ones.

Example:  Daily sales

```bash
Day      Sales
1        100
2        120
3        130
4        150
Here, Sales is changing with Day (time).

We can analyze this to predict future sales-this is Time Series Analysis.

```

<b>Example Using Linear Regression</b>

```bash
import numpy as np
from sklearn.linear_model import LinearRegression

# Time data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Sales data
y = np.array([100, 120, 140, 160, 180])

model = LinearRegression()
model.fit(X, y)

# Predict future sales
prediction = model.predict([[6]])

print(prediction)





# output:
[200.]

Means Predicted sales for month 6 are 200.

```

# Clustering :
Clustering is a machine learning technique that is used to group similar data points together based on their characterstics.

<b>Some common Algoritms in Scikit-learn</b>

```bash
1. K-Means Clustering

2. DBSCAN(Density-Based)

3. Hierarchical Clustering

```

<b>1. K-Means Clustering  :</b>
<br>
K-Means is the most popular clustering algorithm in Machine Learning.
<br>
It groups data into K clusters, where K is the number of groups you choose.

Full Form

K = number of clusters
Means = average /centroid of each cluster

<b>Simple Example of K-Means </b>

```bash
from sklearn.cluster import KMeans
import numpy as np

X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

kmeans = KMeans(n_clusters=2)

kmeans.fit(X)

print(kmeans.labels_)




# output 
[1 1 1 0 0 0]

Means:
First 3 points belong to one cluster
Last 3 points belong to another cluster

```







