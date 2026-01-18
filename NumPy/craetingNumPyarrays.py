
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

# arange (start,stop,step) :- 
# This  Method or function  is use to Generate Sequence of numbers. It is a step based sequence.

# Common uses of arange()
"""
 Loop-like sequences
 Index generation
 Time steps
 Even / odd number
 you can also generate Tables
"""

# Example :

Arange = np.arange(2,21,2)

print(Arange)


# linspace (start,stop,num) :-

"""
linspace() is used when :
You want exact number of values.

you want equal spacing

Used in graph , ML and Math Function

"""


LineSpace = np.linspace(1,20,5)

print(LineSpace)

