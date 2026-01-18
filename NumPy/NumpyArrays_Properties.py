

# import numpy as np

# arr_2D = np.array([[20,30,40,50],
#                    [10,30,60,80]])

#  # It print how Many Rows and columns are present in an array
# print(arr_2D.shape)   


# # It print(return) total how Many numbers of element are present in an array.
# print(arr_2D.size)

# # It returns number of dimensions of an array
# print(arr_2D.ndim)

# # It returns the data type of elements present in an array
# print(arr_2D.dtype)



# astype ()

import numpy as np

arr = np.array([1.2,2.4,3.5,4.7,5.9])
print(arr)
print(arr.dtype)

arr2 = arr.astype(int)
print(arr2)
print(arr2.dtype)

