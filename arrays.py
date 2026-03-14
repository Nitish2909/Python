# # creating arrays using Python List

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers)

# # access elements:
# print(numbers[0]) # first element
# print(numbers[3]) # fourth element
# print(numbers[2]) #third element


# # creating arrays using array modules

# import array     # first way to import array
# import array as arr  # using alias
# from array import *  # third to import array

# # you can choose any one way to import array module

# arr1 = array('i', [1,2,3,4,5,6,7])

# # traversing array
# for i in range(0,7):
#     print(arr1[i], end=" ")


# # creating arrays using numpy library

# import numpy as np;

# arr = np.array([1,2,3,4,5,6,7])
# print(arr)



# Basic Array Operations:

# # 1. Accessing Elements:

# from array import * 

# arr = array('i',[10,20,30,40,50,60,70,80,90])

# print(arr)

# # positive indexing 
# print(arr[0])  # first element
# print(arr[2])  # third element

# # negative indexing
# print(arr[-1])  # last element
# print(arr[-3])  # third element from end

# # slicing
# print(arr[1:4]) #array('i', [20, 30, 40])
# print(arr[:2]) #array('i', [10,20])
# print(arr[::2]) #array('i', [10, 30, 50, 70, 90])
# print(arr[2:])  #array('i', [30, 40, 50, 60, 70, 80, 90])


# # 2. Updating an elements:

# from array import *
# arr = array('i',[10,20,30,40,50,60,70,80,90])

# # update single element
# arr[1]=200
# print(arr)

# #update slicing
# arr[1:3]= array('i',[300,400])

# print(arr)

# # 3. Traversing an Array
# from array import *

# arr1 = array('i', [1,2,3,4,5,6,7])

# # traversing array
# # Method: 1
# for i in range(0,7):
#     print(arr1[i], end=" ")
# print('\n')

# # Method: 2
# for a in arr1:
#     print(a, end=",")



# Some Common array methods:

from array import *

arr = array('i', [10,20,30,40,50])

#1.  array.append(value) => This Method add a new elements to the end of array
arr.append(60)


#2.  array.insert(index_number, value) => This Method add a new elements on the given index of an array
arr.insert(1,100)

#3. array.pop() => This method removes and returns last elemts of an array
arr.pop()

#4. array.reverse() => This method reverse the array 
arr.reverse()


#5. array.remove(value) => This method remove given elements from  the array 
arr.remove(10) 

# 6. array.count(value) => returns number of most occurrences of given elements
arr.count(20)


print(arr)






