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

# Data cleaning Techniques:
Data cleaning (also called Data cleansing or Data Preprocessing) is the process of detecting, correcting, or removing inaccurate, incomplete, duplicate, inconsistent, or irrelevant data from a dataset to improve its quality and reliability.
<br>
In Simple word we can say that Data cleaning means making raw data usable and accurate for analysis.
<br>
Clean Data is essentials for correct descision-making, Reliable Data analysis and accurate machine learning predections.
<br>

<b>There are three most important Techniques that are used for Data Cleaning:</b>

```bash

1. Handling Missing Values

2. Removing Duplicates

3. Correcting Data inconsistent

```

<b>Why Data Cleaning is Important:</b>

```bash
1. Improves accuracy of results.

2. Enhance data quality.

3. Build Better Models.

4. Saves time and efforts.

5. Improves descision-making. 

6. Prevents wrong conclusions.

7. Increases model performance (in machine learning).

8. Ensures consistency and reliability
```

# 1. Handling Missing values in Pandas:
Here the steps to how to Handling missing values:
<br>

<b>1. Import Required Library</b>

```bash

import pandas as pd
import numpy as np
```

<b>2. Create / Load Dataset :</b>

```bash
data = {
    "Name": ["Rohan", "Shyam", "Mohan", "Raju"],
    "Age": [20, np.nan, 25, np.nan],
    "Marks": [85, 90, np.nan, 95]
}

df = pd.DataFrame(data)
print(df)

              # output:
                  Name   Age   Marks
              0   Rohan   20.0   85.0
              1  Shyam   NaN   90.0
              2  Mohan  25.0   NaN
              3   Raju   NaN   95.0

```

<b>3.Detect or Identify Missing Values</b>

```bash
isnull()  => If any Missing values in dataframe it shows True in place of missing values.
             If not any Missing values in dataframe it shows false in that place.


Example:

df.isnull()


         # Output:      
            Name	Age	    Marks
        0	False	False	False
        1	False	True	False
        2	False	False	True
        3	False	True	False


```

<b>4. Count missing values:</b>

```bash
df.isnull().sum()

=> It helps to count number of missing value in each column.It also helps to understand which column need cleaning.

     
        # Output:
          0
         Name	0
         Age	2
        Marks	1

```

<b>5. Removing Missing Values :</b>

```bash
df.dropna() => It Removes rows that containing any NaN Values

df.dropna(axis=0) => Removes rows(by default).

df.dropna(axis=1) => Removes colums with missing values.


```

<b>6. Fill Missing Values(Imputation) :</b>

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

# 2. Removing Duplicates :
Removing duplicates is the process of identifying and eliminating repeated records or entries in a dataset so that each data point appears only once, ensuring accuracy, consistency, and unbiased analysis.
<br>

<b>Steps to Handling or Removes duplicate</b>
<br>

<b>1. Import Required Library :</b>

```bash
import pandas as pd

```

<b>2. Create Dataset with Duplicates</b>

```bash
data = {
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["Ram", "Shyam", "Shyam", "Mohan", "Sita", "Sita"],
    "Marks": [85, 90, 90, 88, 95, 95]
}

df = pd.DataFrame(data)
print(df)



        # Output:
           ID   Name  Marks
        0   1    Ram     85
        1   2  Shyam     90
        2   2  Shyam     90
        3   3  Mohan     88
        4   4   Sita     95
        5   4   Sita     95

```

<b>3. Detect Duplicate Rows</b>

```bash
# Check duplicates

df.duplicated()

=> It Returns True Duplicate for Rows (after the first occurance)



     #Output :
     
             0
        0	False
        1	False
        2	True
        3	False
        4	False
        5	True

```

<b>4. Remove Duplicate Rows :</b>

```bash

# 1. Remove full duplicate rows
df.drop_duplicates() 

=> It Removes duplicate rows, keeping the first row by default (means keep first occurance from duplicate rows)

   # Output:
            ID	  Name	   Marks
   0	    1	    Ram	      85
   1	    2	   Shyam	  90
   3	    3	   Mohan	  88
   4	    4	   Sita	      95


   # 2. Remove duplicates permanently

   df = df.drop_duplicates() 


```

# 3. Data Inconsistencies :
Data Inconsistencies means that the same information appears in different or conflicting form within Dataset or across System.It make data confusing and hard to analyze.
<br>

Example:

```bash
If One record says "20/3/2026" and another says "03-20-2026" both may represent the same date, but the format Inconsistencies can cause errror during analysis.

```

# Data Transformation:
Data transformation is the process of converting data into a suitable format or structure so that it can be effectively used for analysis, visualization, or machine learning.
<br>
It mainly includes:

```bash
1. Data Type Conversion
2. Normalization
3. Scaling

```

# 1. Data Type Conversion( type casting):
Data type conversion or type casting is the process of changing a column's data type from one type to another (e.g., string -> integer) so that operations can be performed correctly.

```bash

data = {
    "Age":["20","21","22","24","25"]
}

df = pd.DataFrame(data)
print(df)

# check data type:
df.dtypes


# convert string into integer
df['Age'] = df['Age'].astype('int64')

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

# Advance Features of Pandas:

<b>1. Handling Missing Values/Data:</b>
<br>
Handling missing values/Data is the process of identifying, managing, replacing, or removing incomplete, null, or undefined data from a dataset to improve data quality and ensure accurate analysis.
<br>
In Pandas missing value/data is represented as:
<br>
1. NaN -> Not a number
<br>
2. None
<br>
3. NaT -> Missing Data/ Time Value
<br>

<b>Here are some important functions and Methods that is used for handling missing values in Pandas:</b>

```bash

1. isnull() -> It is a method that check missing value in datasets. If any Missing values in dataframe it shows True in place of missing values.If not any Missing values in dataframe it shows false in that place.

2. dropna() -> This method removes rows and columns that containing any missing values.

3. fillna() -> This methods helps to fill missing values with a specified value.

4.  sum() -> This methods counts how many missing values are present in a single column.

```

Example:

```bash

import pandas as pd
import numpy as np

data = {
    "Name": ["Rohan", "Shyam", "Mohan", "Raju"],
    "Marks": [85, 90, np.nan, 95]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\Count Missing Values")
print(df.isnull().sum())

df["Marks"].fillna(df["Marks"].mean(), inplace=True)

```

<b>2. GroupBy Operations :</b>
<br>
GroupBy operation in Pandas is a technique used to split data into groups based on one or more columns and then perform calculations or aggregate functions on each group.
<br>
It follows Simple concept of Split -> Apply -> Combine
<br>
In Simple words we can say that GroupBy operation in Pandas is a powerful feature used to organize data into groups and perform calculations like sum, mean, count, minimum, and maximum values efficiently. It is widely used in data analysis, reporting, and machine learning preprocessing.
<br>

<b>Syntax :</b>

```bash
df.groupby("column_name")

```
Example:

```bash
import pandas as pd

data = {
      "Department": ["IT", "HR", "IT", "HR"],
      "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].sum()
# print(result)

# You can aslo use more advance method that is agg()

agg = df.groupby("Department")["Salary"].agg(["sum","min","max"])
print(agg)

```

<b>3. MultiIndexing :</b>
<br>
MultiIndexing in Pandas is an advanced indexing technique that allows multiple levels of indexes in rows or columns of a DataFrame or Series.It is also called Hierarchical Indexing because data is organized in a hierarchy of multiple indexes.
<br>

Example:

```bash
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Employee": ["A", "B", "C", "D"],
    "Salary": [50000, 60000, 45000, 47000]
}

df = pd.DataFrame(data)

df = df.set_index(["Department", "Employee"])

print(df)

```
<b>You can also Create multiple index </b>

```bash
import pandas as pd

arrays = [
    ["IT", "IT", "HR", "HR"],
    ["A", "B", "C", "D"]
]

index = pd.MultiIndex.from_arrays(arrays)

df = pd.DataFrame(
    {"Salary": [50000, 60000, 45000, 47000]},
    index=index
)

print(df)

```

<b>4. Pivot Table :</b>
<br>
A Pivot Table in Pandas is a data summarization tool used to organize, analyze, and aggregate data from a large dataset into a meaningful table format.
<br>
It helps in Summarizing data , Calculating totals and averages, Comparing categories, Generating reports
<br>

<b>Syntax:</b>

```bash
pd.pivot_table(
    data,
    values,
    index,
    columns,
    aggfunc
)


# parameters:
data -> DataFrame

values -> Column to aggregate

index -> Row grouping

columns -> Column grouping

aggfunc -> Aggregate function

```

Example:

```bash
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50000, 60000, 45000, 47000]
}

df = pd.DataFrame(data)

table = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(table)

```
<b>output:</b>

```bash
Department     F	   M
HR	        47000	 45000
IT	        60000	 50000

```

