
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

sns.lineplot(x=None, y=None, data=None)

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


