# What is NumPy :
NumPy is a Python Library that is used for working with Arrays.
Numpy was created in 2005 Travis Oliphant.It is an open source project that you can use it freely.
<br>
NumPy Stands for Numerical Python.

# Why use NumPy :
NumPy is used to do fast , easy and powerful Numerical calculation in Python.
<br>
In simple world we can say that Numpy is a super- power calculator for Python.
<br>

Here are some points why use NumPy :

```bash
Why we use NumPy:

1. Fast calculations :
NumPy works much faster than normal Python lists, especially for large data.

2. Easy to handle large data :
It can store and process thousands or millions of numbers easily.

3. Less code, more work :
One line of NumPy code can do the work of many Python lines.

4. Best for math & data science:
Used in Data Science, Machine Learning, AI, and scientific calculations.

```
<br>

<b>Example :</b>

```bash
import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr)

```
# Creating NumPy Arrays :
<b>Create a NumPy ndarray Object :</b>
<br>

NumPy is used to work with arrays. The array object in NumPy is called ndarray.
<br><br>
We can create a NumPy ndarray object by using the array() function.
<br>

Example:

```bash
import numpy as np

arr = np.array([10 ,20,30,40,50])

print(arr)

print(type(arr))

```
<br>

To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

```bash
# use a tuple to create a numpy array


import numpy as np

oneD_array = np.array((20,40,50,60,70,90,78))

print(oneD_array)

```
# Creating NumPy arrays :

```bash

# creating NumPy arrays :

# from list :

import numpy as np

arr = np.array([20,30,40,50])

print(arr)

                    # output: 
                    #[20 30 40 50]


# 2D array

TwoD_array = np.array([[10,20,30,40] , [50,60,70,80]])

print(TwoD_array)
 
"""
# output:

[[10 20 30 40]
[50 60 70 80]]
"""

# Multidimension Array

MD_array = np.array([[10,20,30] , [40,50,60] , [70,80,90]])

print(MD_array)

# Zeros(shape) , Ones(shape)  and full(shape,value)
"""
Syntax:
zeros(shape) -> It fill the array as 0 given in shape values means number of rows and column

ones(shape) -> It fill the array as 1 given in shape values means number of rows and column

full(shape , value) -> Thhis function is used in situation where you want to print specific value in an array

"""

z = np.zeros((3,3))
print(z)


'''
 Output :

 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

O = np.ones((3,3))
print(O)

"""
Output :

[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]

"""

f = np.full((3,3),10)

print(f)


''''
Output :

[[10 10 10]
 [10 10 10]
 [10 10 10]]
'''

```

# arange() and linspace() Method :

<b>arange (start,stop,step) :</b>
This Method or function  is use to Generate Sequence of numbers. It is a step based sequence.
<br><br>

 Common uses of arange() :-
 <br>
 Loop-like sequences
 <br>
 Index generation
 <br>
 Time steps
 <br>
 Even / odd number
 <br>
 you can also generate Tables
 <br>

 <b>Example :</b>

```bash

Arange = np.arange(2,21,2)

print(Arange)


output:
[ 2  4  6  8 10 12 14 16 18 20] 

```
<br>

<b>linspace (start,stop,num) </b>
It is a equal part sequence method.
<br>
linspace() is used when :
<br>
You want exact number of values.
<br>
you want equal spacing
<br>
Used in graph , ML and Math Function
<br>

<b>Example :</b>

```bash
LineSpace = np.linspace(1,20,5)

print(LineSpace)

```

# NumPy Arrays Properties :

```bash


import numpy as np

arr_2D = np.array([[20,30,40,50],
                   [10,30,60,80]])

 # It print how Many Rows and columns are present in an array
print(arr_2D.shape)   


# It print(return) total how Many numbers of element are present in an array.
print(arr_2D.size)

# It returns number of dimensions of an array
print(arr_2D.ndim)

# It returns the data type of elements present in an array
print(arr_2D.dtype)

```
# astype() in NumPy :
astype()  method is used to change the data type (datatype) of a NumPy array.
<br>
This method helps in type conversion.
<br>
This method is used because sometimes Data comes as string , but we need numbers.In this situation we can use astype to convert data from string to integer and also convert float to an interger.
<br>

<b>Syntax:</b>

```bash
array.astype(new_datatype)

```
<br>

Example:

```bash

# astype ()

import numpy as np

arr = np.array([1.2,2.4,3.5,4.7,5.9])
print(arr)
print(arr.dtype)

arr2 = arr.astype(int)
print(arr2)
print(arr2.dtype)

```

# NumPy Array Operations :

```bash

import numpy as np

arr= np.array([10,20,30,40,50])

print(arr + 10)  # addition
print(arr - 10)  # Substraction
print(arr * 10)  # Multiplication
print(arr / 10)  # Division
print(arr ** 2) # Exponetial
print(arr % 3)  # Modules (reminders)
print(arr // 3) # Floor division 


Output :

[20 30 40 50 60]
[ 0 10 20 30 40]
[100 200 300 400 500]
[1. 2. 3. 4. 5.]
[ 100  400  900 1600 2500]
[1 2 0 1 2]
[ 3  6 10 13 16]


```

# Aggregation Function in NumPy :
Aggregation functions are used to combine multiple values into a single result
(like sum, average, max, min, mean, std(standard Deviation),var(Variance), median etc.).
<br>
They are very important in Data Science, ML, and Pandas.
<br>

<b>Why Aggregation Functions are used?</b>
To summarize data.
<br>
To analyze datasets.
<br>
To find patterns (mean, max, min).
<br>
Used in statistics & ML models.
<br>

<b>Example :</b>

```bash

"""
Aggregation Functions :

np.Sum(array) => It returns sum or total 

np.min(array) => It return minimum value present in an array.

np.max(array) => It return maximum value present in an array.

np.mean(array) => It returns average value

np.std(array)  => It return standard deviation

np.var(array)  => It Return variance

"""

import numpy as np

arr = np.array([10,90,50,30,80])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

```
<br>

<b>argmin() & argmax() (Index position)</b>

```bash
# argmin() and argmax() 

a = np.array([10,20,3,40,50,90])

print(np.argmin(a))   # index of min value

print(np.argmax(a)) # index of max value

```

# Indexing and Slicing in NumPy :
Indexing and slicing are used to access specific elements or parts of an array.
<br>
This is a core concept in NumPy, Pandas, and Machine Learning.
<br>

<b>Indexing in NumPy :</b>
<br>
Indexing is used for Accessing a single element from an array using its position (index).
<br>
Indexing always start with 0.
<br>

Example:

```bash

# In case of 1D Array 

import numpy as np
arr =  np.array([10,20,30,40,50,60,70,80,90])
print(arr[0])  # it return 0th index value
print(arr[3])  # it return 3rd index value
print(arr[5])  # it return 5th index value
print(arr[-1]) # it return last index element from array


# In case of 2D Array 
# array[rows][columns]

arr_2d = np.array([[20,30,40,50],
                   [90,40,60,20]])

print(arr_2d[1][3])

```
<b>Slicing in Numpy :</b>
<br>
Extracting multiple elements from an array in the form of (a sub-array).
<br>

<b>Syntax:</b>

```bash
array_name[start : stop : step]

start = 0th index (included)
stop = start to stop - 1  (excluded)

```
<br>

<b>Example:</b>

```bash
# 1D Array Slicing

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[1:5]) # it return array value that start from index=1 to index=4 
                #because index=5 in excluded

print(arr[:3]) # print first 3 element from array

print(arr[4:]) # print from index=4 to end  element from array

print(arr[::2]) #  Every 2nd element

print(arr[::-1])  # Reverse array



# 2D Array Slicing 

# syntax:

# arr[row_start:row_end, col_start:col_end]

arr_2d = np.array([[20,30,40],
                  [10,60,70],
                  [10,20,30]])

print(arr_2d[1:3 , 1:3])

print(arr_2d[:,1]) # All rows, column 1

print(arr_2d[1, :]) # All columns, Row 1


```
<br>

<b>Boolean Indexing :</b>
<br>
Boolean indexing is used to filter data based on condition.
<br>

<b>Example :</b>

```bash

# Boolean indexing :

import numpy as np

arr = np.array([20,90,40,10,30])

print(arr[arr > 10])

print(arr[arr<40])
```
<br>

<b>Fancy Indexing :</b>
<br>
Fancy indexing is used to Access multiple elements using a list of indices(indexes).
<br>

<b>Example :</b>

```bash


# fancy Indexing 

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[[0,3,5,7]]) 

```

# Reshaping & Manipulating in NumPy :

<b>Reshaping in NumPy :</b>
<br>
Reshaping is used to change the shape of an array without changing data.It does not create a copy.
<br>
for example you change an 1D array to 2D array with the help of reshape() method.
<br>
if dimensions does not match means Total element must match like (2 x 3) . if total elements does not match this method not works in this codition.

<b>Syntax :</b>

```bash

array.reshape(rows , columns)


```
<br>

<b>Example:</b>

```bash


import numpy as np 

arr = np.array([10,20,30,40,50,60])

reshaped_arr = arr.reshape(2,3)   # Total element must match like (2 x 3)

print(reshaped_arr)   

```
<br>

<b>Automatic Dimension(-1) :</b>
<br>
when using this NumPy automatically calculates the size.
<br>

Example :

```bash

# Automatic Dimension(-1)

arr = np.array([10,20,30,40,50,60])

reshaped_arr = arr.reshape(3,-1)

print(reshaped_arr)

```
<br>

<b>Flattening Arrays in NumPy:</b>
<br>
Flattening means converting a multi-dimensional array (2D / 3D) into a 1D array.
<br>
There are two methods:
<br>

```bash

1. flatten() => This method returns a new copy of thr array.

Exmaple :

# flatten() method :   

import numpy as np 

arr = np.array([[10,20,30,40],
                [50,60,70,80]])

flat_arr = arr.flatten()

print(flat_arr)       # Changes in flat_arr do NOT affect the original array.


# output :   [10 20 30 40 50 60 70 80]



2. ravel() method => This method Returns a view (not a copy) whenever possible.

Example :

# ravel() method :

import numpy as np 

arr = np.array([[10,20,30,40],
                [50,60,70,80]])

ravel_arr = arr.ravel()

print(ravel_arr)    # output : [10 20 30 40 50 60 70 80]

# If you want to modify array you can it.

ravel_arr[0]= 100

print(ravel_arr)   #output : [100  20  30  40  50  60  70  80] 

print(arr) #  when you modify ravel_arr it also change original array 

"""
output :

 [[100  20  30  40] 
 [ 50  60  70  80]]

"""

```







