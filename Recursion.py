

# Factorial

# formula of finding factorial:

# factorial  =  n * factorial(n-1)

"""
factorial(0)  => 1

factorial(1)  => 1

factorial(5)    => 5! = 5 + 4 + 3 + 2 + 1
"""

# def factorial(n):

#     if(n==0 or n==1 ):     
#         return 1
#     return n * factorial(n-1)

# n= int(input("Enter a Number :"))

# print(" Factorial of given numbers is ",factorial(n))


# fibonacci series :


# 0 1  1  2  3  5  8 

# def fibonacci(n):
      
#       if( n ==0):  # base case
#             return 0
#       elif(n==1):  # base case
#             return 1
#       else:
#         return fibonacci(n-1) + fibonacci(n-2)   # recursive case

# n= int(input("Enter a Number :"))

# for i in range(n):

#  print(fibonacci(i) , end="")



# n = int(input("Enter Number :"))

# a= 0
# b=1
# for i in range(n):
#     print(a, end="")
#     a ,  b =b , a+ b


"""
1. Write a program using functions to find greatest of three numbers
"""

# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("A is greater")

#     elif(b>a and b>c):
#         print("B is greater")

#     else:
#         print("C is greater")


# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# c = int(input("Enter c :"))

# print(greatest(a,b,c))


"""
2. Write a python program using function to convert Fahrenheit to Celsius .

     Fahrenheit to Celsius Conversion Formula :

     Celsius (°C)=(Fahrenheit (°F)-32)+ 5 /9)

     
     E+ample :

    Convert 98.6°F to Celsius:
 
    c =  (98 - 32) + 5 /9
      =   66 + 5 /9
      =     330/9
      =     36.67 ∘C (appro+)
      =



"""

# def f_to_c(f):
#     return (f - 32) * 5/ 9

# f= float(input("Enter Temprature in fahrenheit : "))
 
# c =f_to_c(f)
# print(f"{round(c)}∘C")



"""
3. Write a python program using function to convert  Celsius  to Fahrenheit.

      Celsius to Fahrenheit Conversion Formula :

     Fahrenheit (°F)=( celsius (°C) + 9 / 5 + 32)

        Easy Trick to Remember

        Multiply Celsius by 9

        Divide by 5

        Add 32


     E+ample :

    Convert 37°C to Fahrenheit:
 
    f = ( celsius * 9) / 5 +32
    f = (37 * 9) /5 + 32
    f= 333/5  +  32
    f = 66.67 + 32
    f = 99


"""


# def c_to_f(c):
#     return (c * 9) / 5 + 32

# c= float(input("Enter Temprature in celsius : "))
 
# c =c_to_f(c)
# print(f"{round(c)}∘C")


""" 4. Write a recursive function to calculate the sum of first n natural numbers.


sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + .......+ n-1 + n

forrmula:

    sum = sum(n-1) + n

    sum(5)

      5 + 4 + 3 + 2 + 1

"""

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# n = int(input("Enter Number :"))

# print(sum(n))




  