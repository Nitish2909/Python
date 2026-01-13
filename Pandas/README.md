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

