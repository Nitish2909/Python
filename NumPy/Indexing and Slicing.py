

# # INDEXING 

# # In case of 1D Array 
# import numpy as np
# arr =  np.array([10,20,30,40,50,60,70,80,90])
# print(arr[0])  # it return 0th index value
# print(arr[3])  # it return 3rd index value
# print(arr[5])  # it return 5th index value
# print(arr[-1]) # it return last index element from array


# # In case of 2D Array 
# # array[rows][columns]
# arr_2d = np.array([[20,30,40,50],
#                    [90,40,60,20]])

# print(arr_2d[1][3])



# SLICING 

# 1D Array Slicing
import numpy as np

# arr = np.array([10,20,30,40,50,60,70,80,90])

# print(arr[1:5]) # it return array value that start from index=1 to index=4 
#                 #because index=5 in excluded

# print(arr[:3]) # print first 3 element from array

# print(arr[4:]) # print from index=4 to end  element from array

# print(arr[::2]) #  Every 2nd element

# print(arr[::-1])  # Reverse array



# 2D Array Slicing 

# syntax:

# arr[row_start:row_end, col_start:col_end]

# arr_2d = np.array([[20,30,40],
#                   [10,60,70],
#                   [10,20,30]])

# print(arr_2d[1:3 , 1:3])

# print(arr_2d[:,1]) # All rows, column 1

# print(arr_2d[1, :]) # All columns, Row 1



# Boolean indexing :

import numpy as np

arr = np.array([20,90,40,10,30])

print(arr[arr > 10])

print(arr[arr<40])


# fancy Indexing 

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[[0,3,5,7]]) 

