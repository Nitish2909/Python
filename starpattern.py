
# """
#  *
# ***
# ***** for n = 3
# """

# n = int(input("Enter number :"))

# for i in range(1, n+1):
#      print(" " * (n-i) + "*" * (2*i-1) )
     

#      # formulas:
#     #   space =  (n-i)
#     # star print =  "*" * (2*i-1)




# """
# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# """

# n = int(input("Enter number :"))

# for i in range(1, n+1):
#      print( "*" * (2*i-1)+ " " * (n-i) )
     

#      # formulas:
#     #   space =  (n-i)
#     # star print =  "*" * (2*i-1)



"""
# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * * 

# """

# n = int(input("Enter number :"))

# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*" ,end="")
#         else:
#             print(" ",end="")

#     print()



# # 10. Write a program to print multiplication table of n using for loops in reversed order.

# num = int(input("Enter a Number :"))
# for i in range( 10 , 0, -1):      # start from 10
#                                   # end at 1
#                                   # decrease by 1

#       print(num, "x" ,i, "=" , num * i)
