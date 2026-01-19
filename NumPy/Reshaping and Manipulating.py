

#import numpy as np 

# arr = np.array([10,20,30,40,50,60])

# reshaped_arr = arr.reshape(2,3)

# print(reshaped_arr)


# # Automatic Dimension(-1)

# arr = np.array([10,20,30,40,50,60])

# reshaped_arr = arr.reshape(3,-1)

# print(reshaped_arr)



# # flatten() method :

# import numpy as np 

# arr = np.array([[10,20,30,40],
#                 [50,60,70,80]])

# flat_arr = arr.flatten()

# print(flat_arr)


# # output :   [10 20 30 40 50 60 70 80]




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


