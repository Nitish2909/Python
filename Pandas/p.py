import pandas as pd 
import numpy as np

data ={
    "Name" : ['Nitish','Rakesh','Rohan','None'],
    "Age" : [21,22,None,32],
    "Salary" : [90000,None,50000,80000]
}

df = pd.DataFrame(data)
print(df)