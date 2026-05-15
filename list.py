# numbers = [10,20,30,40,50,60,70,80,90]

# #update one item in list
# numbers[1]= 100 # Replace 20 with 100
# print(numbers)

# #update multiple item in list
# numbers[1:5]= [200,300,400,500] #update value at index 1 to 4
# print(numbers)


# append()
numbers = [10,20,30,40,50]
numbers.append(100)
print(numbers)

# insert(index, value)
numbers = [10,20,30,40,50]
numbers.insert(5, 60)
print(numbers)


# extend()
numbers = [10,20,30]
numbers.extend([40,50,60,70])
print(numbers)  #[10, 20, 30, 40, 50, 60, 70]