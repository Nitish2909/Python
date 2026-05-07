

# Here use loops to solve
import numpy as np 

a = np.array([10,20,30,40])

for i in range(len(a)):
    a[i]= a[i] *2

print(a)   


# Now use vectorisation

a = np.array([10,20,30,40])

a = a *2

print(a)
