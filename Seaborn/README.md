
# What is Seaborn :
Seaborn is a Python Library that is used for Data Visualization.Seaborn is built on top of Matplotlib.It Works directly with Pandas DataFrames. And Gives beautiful statistical plots with less code.
<br>
Seaborn Mostly used in Data Analysis and Data Science Projects.
<br>

<b>How to Insatll Seaborn :</b>

```bash

pip install seaborn

# If your using Python3 then use :
pip3 insatll seaborn


# if your in Anaconda / Conda:
conda insatll seaborn

#In Google Colab / Jupyter Notebook
!pip install seaborn

```

# Loading Built-in Datasets :
Seaborn comes with some built-in datasets for example:
<br>
tips , iris, titanic, flights
<br>

Example:

```bash

df = sns.load_dataset("titanic")
df.head()

```
# Basic Seaborn Plots :

<b>1. Line Plot :</b>
When to Use:
<br>
Trend over time, Ordered or continuous data, Growth, decline, pattern,Time series data, Trend analysis, Continuous x-axis.
<br>

Syntax:

```bash

sns.lineplot(x=(xlabel_Name), y=(ylabel_name), data)

```
Example:

```bash
# Line Plot
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# size is used for x label and total_bill is used for y label
sns.lineplot(x="size", y="total_bill", data=df)
plt.show()

```
<br>

<b>Bar chart </b>
<br>
It Shows average (mean) of numerical data for categories.
<br>

Syntax:

```bash
sns.barplot(x=(xlabel_Name), y=(ylabel_name), data)

# x = for x-axis 
# y = for y-axis
# data = data

```
<br>

Example:

```bash

# Bar Plot
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
sns.barplot(x="class", y="fare", data=df)
plt.show()

```
<br>

# Histogram Chart :
It Shows distribution of numerical data. 
<br>

Syntax:

```bash
sns.histplot(data, x, bins=value)

```
<br>

Example:

```bash
# histogram Plot

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
sns.histplot(x="age", data=df, bins=30, kde=True)
plt.show()

```
# Heatmap (Correlation)
What it is:
<br>
Shows correlation between numerical features
<br>
When to use:

Feature relationship analysis
<br>

Syntax:

```bash
sns.heatmap(data, annot=False, cmap=None)

```
<br>

Example:

```bash

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

```

# Distribution Plot :
A distribution plot is a graph used to show how data is spread (distributed) across different values. In simple words, it helps you see where most values lie, how often they occur, and the shape of the data.
<br>
Distribution plot is created for quantitative data. 
<br>
Here the quantitative means continuous values , numeric value,those value that not divide on category basis(like Gender,movie gener).
<br>
Example of quantitative data.
<br>
Age,Salary etc.
<br>

<b>Types of Distribution plot :</b>

```bash
1. sns.histplot()

2. sns.jointplot()

3. sns.pairplot()

4. sns.rugplot()

```
<br>

# Categorical Plot:
 categorical plot is created for qualitative data.
 <br>
 Here qualitative data means categories based data like Gender, Movie Gener etc.
<br>

<b>Types of Categorical Plot :</b>
<br>

```bash
1. sns.countplot()

2. sns.barplot()

3. sns.violinplot()

4. snx.boxplot()

```
