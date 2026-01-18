
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



# argmin() and argmax() 

a = np.array([10,20,3,40,50,90])

print(np.argmin(a))

print(np.argmax(a))