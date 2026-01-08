# a=10
# if a > 5:
#  print("a is greater")
# else:
#  print("b is greater")


# num=8

# if num%2==0:
#     print("even number")
# else:
#     print(" odd number")    


# variables
# a,b,c=23,45,67

# name="Nitish"
# print(name)

# a=20

# a=40

# b=20

# print(a+b)


# import keyword

# print(keyword.kwlist)

#operators

#Arithmetic operator
# a=20

# b=4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)


# # bitwise operator
# a = 10
# b = 4

# print(a & b)   #AND
# print(a | b)   #OR
# print(~a)      
# print(a ^ b)
# print(a >> 2)
# print(a << 2)


# a = int(input("Enter number 1 :"))
# b= int(input("Enter number 2 :"))

# print( a+ b)


# # Average of given numbers
# a = int(input("Enter number 1 :"))
# b= int(input("Enter number 2 :"))
# c= int(input("Enter number 3:"))
# d= int(input("Enter number 4 :"))

# print("Average of given number is",(a+b+c+d)/4)


# #Square of given number:

# a = int(input("Enter number 1 :"))
# b= int(input("Enter number 2 :"))

# print( a** b)


# Strings

# fname="Nitish"
# lastName="Kumar"

# print(fname+" "+lastName)

#indexing

# str = "HelloWorld"

# print(str[2])

# #slicing:

# text="Hello World"

# print(text[0:5])

# fname="Nitish"
# lastName="Kumar"

# print(fname+" "+lastName)  # concatenation

# print(fname*3)     # Repetaion

# print("N" in fname)   # Membership


#string methods:

# msg= " hello world from python"

# print(msg.upper())  #uper()

# print(msg.lower())  #lower()

# print(len(msg))  #len()

# print(msg.title())  #title()

# print(msg.capitalize())  #captalize()

# print(msg.strip())  #strip()

# print(msg.find("python"))  #find()


# n = str(input("enter your name :"))


# res=  "Good Afternoon"+" "+n

# print(res)

# #slicing:

# text="Hello World"

# print(text[0:4]) # start from index 0 all the way till 4 (excluding index 5)



# number =[1,2,4,5,3,2,3,5,8]

# # print(number[1:6])  #[2, 4, 5, 3, 2]

# # print(number[0:4])   #[1, 2, 4, 5]

# number.append(23)  #append()
# number.insert(2,3)  #insert()
# number.extend([123,22]) #ectend()
# print(number)



# #tuple

# num=(12,23,45,43,22,1,3,5,2,"hello")

# print(num[0])

# #tuple slicing

# print(num[2:5])

# num=(12,23,45,43,2,2,2,2,2,5,5,4,4,4,4,22,1,3,5,2,"hello")

# count = num.count(4)

# print(count)



# #dictionary

# students ={
#     "name":"Nitish",
#     "age":21,
#     "class": "BCA",
#     "RollNo":36
# }

# print(students["name"]) # accessing name 

# print(students.get("age")) # accessing dictionary by using get method

# # how add elements in dictionary
# students["State"] ="Haryana"
# print(students)

# # how to updates elements in dictionary

# students["age"]=22
# print(students)



#SETS

# # how to create sets:
# mysets = {1,2,3,7,8,9,4,3,5,6,7,8}
# print(mysets)

# #How to create an empty sets:
# sts = set()
# print(type(sts))

# # how to add an elements:
# mysets.add(234)
# print(mysets)

# # add multiple elements in sets:

# mysets.update([123,345,678,890])
# print(mysets)


# operation on sets:

# # Union  -> It combines both sets in single one.

# set1 ={12,13,14,15,16}

# set2 ={1,2,3,4,5,6,7,8,9,10,11}

# print(set1 | set2)


# # Intersection   ->  It searches common elements in both sets

# set1 ={12,13,1,15,16,4,6,7,2}

# set2 ={1,2,3,4,5,6,7,8,9,10,11}

# print(set1 & set2)


# # Difference ->

# set1 ={12,13,1,15,16,4,6,7,2}

# set2 ={1,2,3,4,5,6,7,8,9,10,11}

# print(set1 - set2)


# mysets = {1,2,3,7,8,9,4,3,5,6,7,8}
# print(mysets.pop())

# # Question:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# s.add(0.20)

# print(s)





# Function

# def my_function():
#     print("Hello from a function")
# my_function()


# # funtion definition
# def add(a,b):       # a and b are parameters
#     return a+b
# result = add(4,55)   


# print(result)   # function call











