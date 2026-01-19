
# import numpy as np 

# arr = np.array([10,20,30,40,50,60,70])

# # 1. Modify Single Element (Indexing)
# arr[1]=100
# print(arr) # [ 10 100  30  40  50  60  70]


# #2. Modify Multiple Elements (Slicing)
# # array[start:end-1]
# arr[1:3] = 1
# print(arr) #[10  1  1 40 50 60 70]


# # 3. Boolean Indexing
# arr[arr >40] = 22
# print(arr) #[10  1  1 40 22 22 22] 


# # 4. Replace Using where()
# # where(condition , value_if_true, value_if_false)
# new_arr= np.where(arr % 2 ==0 ,0 ,1)
# print(new_arr)   #[0 1 1 0 0 0 0]


# # 5. Append Elements
# # np.append(array,value)
# append_element= np.append(arr,100) # does not change original array
# print(append_element) #[ 10   1   1  40  22  22  22 100]


# # 6. Insert Elements
# # np.insert(array,indexNo,value)
# insert_element= np.insert(arr,1,200)
# print(insert_element) #[ 10 200   1   1  40  22  22  22]

# # 7. Delete elements
# # np.delete(array,indexNo)
# print(arr) # [10  1  1 40 22 22 22]

# arr2 = np.delete(arr,2) # [10  1 40 22 22 22]
# print(arr2)




# # splitting an Array :

# import numpy as np

# # splitting a 1D array
# arr = np.array([10,20,30,40,50,60,70,80])
# print(np.split(arr,2))

# # splitting a 2D array 
# arr_2d = np.array([[20,30,40],
#                    [50,60,70],
#                    [1,2,3]])

# print(np.split(arr_2d,3))

