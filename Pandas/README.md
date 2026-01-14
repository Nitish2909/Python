# What is Pandas :
Pandas is a Python Library that is used for working with data sets. Pandas is used for data analysis , Data Manipulation ,Data cleaning ,Handling tables(rows and column). It provides fast and flexible tools to work with tabular data, similar to spreadsheets or SQL tables.
<br>
Pandas is used in data science, machine learning, finance, analytics and automation etc.
<br><br>

<b>How to install pandas :</b>
<br>

```bash

pip install pandas

```
<br>
<b>How to import pandas :</b>

```bash

import pandas 

# you can also import like this using alias:

import pandas as pd

```
<br>

<b>How to check Pandas version</b>

```bash

import pandas as pd

print(pd.__version__)

```
# Pandas Series :
A Series in pandas is like a column in a table.It is a one dimensional array that holding data of any type.
<br>

<b>Create a pandas series :</b>

```bash
import pandas 

data =[10,20,30,40,50]

p = pandas.Series(data)

print(p)



# you can as give an index name

# import pandas as pd

# data = [10,20,30,40,50]

# p = pd.Series(data, index=["a","b","c","d","e"])

# print(p)
```

#  Dataframe 
A Pandas DataFrame is a 2 dimensional data structure.It is like a 2 dimensional array, or a table with rows and columns.
<br>

<b>Create a DataFrame:</b>

```bash
import pandas as pd 

data = {
    "Name" :["Nitish","Rakesh","Rohan"],
    "age" :[20,21,22]
}
df = pd.DataFrame(data)
print(df)

       output:
                Name    age
            0  Nitish   20
            1  Rakesh   21
            2   Rohan   22

```

# Basic operations to view Data 

```bash
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.shape       # rows, columns
df.columns     # column names
df.info()      # data info
df.describe()  # statistics

```
#  Handling Missing values in Pandas :
<b>What are Missing Values?</b>
<br>

Missing values mean no data is present.
<br>
Common representations:

```bash
NaN

None

empty cells

NULL (from databases)

```
<br>

<b>Check entire DataFrame by using:</b>

```bash

df.isnull()
```
<br>

isnull()  => If any Missing values in dataframe it shows True in place of missing values.
<br>
 If not any Missing values in dataframe it shows false in that place.
<br>

<b>Count missing values :</b>

```bash
df.isnull().sum()

```
<br>

<b>Percentage of missing values :</b>

```bash

(df.isnull().sum() / len(df)) * 100

```
# Fill Missing Values (Imputation) :

```bash

# Fill with a fixed value

df.fillna(0)


# Fill column-wise

df["Marks"].fillna(50, inplace=True)

# Fill with Mean (Numeric Data)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# Fill with Median (Better for Outliers)
df["Marks"].fillna(df["Marks"].median(), inplace=True)

# Fill with Mode (Categorical Data)
df["Grade"].fillna(df["Grade"].mode()[0], inplace=True)

```

# Aggregation and Group By in Pandas"
Aggregation means combining multiple values into a single value.
<br><br>
Examples: sum, mean, count, max, min
<br>

<b>Basic Aggregation on a Column :</b>

```bash

df["Marks"].sum()
df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].count()

```

