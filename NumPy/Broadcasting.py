
# import numpy as np

# a = np.array([30,40,40])
# b= np.array([10,20,30])

# print(a + b)


# import numpy as np

# a = np.array([30,40,50])


# print(a + 10)



# Broadcasting Rules

# Rule 1: Dimensions must be equal


import numpy as np

a = np.array([[30,40,50],[60,70,80]])  # 2 x 3 

b= np.array([[10,20,30],[5,10,15]]) # 2 x 3 

print(a + b)


# Rule 2 :One of the dimensions must be 1
#If one of the dimensions is 1, NumPy stretches(expand) it to match the other.
import numpy as np

a = np.array([[30,40,50],[60,70,80]])  # 2 x 3 

b= np.array([10,20,30]) # 1 x 3 

print(a + b)
