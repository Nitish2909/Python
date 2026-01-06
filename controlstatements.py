# condition Statements:

# #  Write a program to print yes when the age entered by the user is greater than or equal to 18.

# age = int(input("Enter your age:"))

# if(age >= 18):
#     print("yes")

# else:
#     print("No ")
   


# # if-else

# age=20

# if(age>=18):
#     print("Your are Eligible to vote ")

# else:
#     print("Your are not Eligible to vote")


# # if-elif-else:

# marks =75

# if(marks >=90):
#     print("Grade A")

# elif(marks >=60):
#     print("Grade B")

# else:
#     print("Grade C")
   

# age = int(input("Enter Your Age :"))
# salary= int(input("Enter Your Salary :"))

# if(age >=18):
#     {
#            print("Eligible")
#     }

#     if(salary >=40000):
#         {
#             print("You are Eligible for Loan ")
#         }
#     else:
#         {
#             print("Not Eligible for Loan")
#         }
# else:
#     print("Your Not Eligible")


# QUESTIONS:

# # 1. Write a program to find the greatest of four numbers entered by the user.

# a = int(input("Enter 1 numbers: "))
# b = int(input("Enter 2 numbers: "))
# c = int(input("Enter 3 numbers: "))
# d = int(input("Enter 4 numbers: "))

# if(a >= b and a >= c and a >= d):
#     print("A is greater",a)

# elif(b >= a and b >= c and b >= d):
#     print("B is greater",b)

# elif(c >= a and c >= b and c >= d):
#     print("C is greater",c)

# else:
#     print("D is greater" ,d)


# """
# # 2. Write a program to find out whether a student has passed or failed if it requires a
# # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# # take marks as an input from the user.

# # """

# sub1 = int(input("enter number in 1 subject :"))

# sub2 = int(input("enter number in 2 subject :"))

# sub3 = int(input("enter number in 3 subject :"))

# total_percentage = ( 100 * (sub1 + sub2 + sub3) )/300

# if(total_percentage >=40 and sub1>=33 and sub2>=33 and sub3>=33):
#     print("you passed the exam",total_percentage)
# else:
#    print("you failed")



# """
# 4. Write a program to find whether a given username contains less than 10
# characters or not.
# """

# username = input("Enter your UserName :")

# if(len(username) <10 ):
#     print("Characters are less than 10 in username")

# else:
#     print("Character are more than 10 in username ")
    
    
# """
# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# """

# p1="Make a lot of money"
# p2="buy now" 
# p3="subscribe this"
# p4="click this"

# message = input("Enter your message :")

# if(message in p1 in  p2 in  p3 in p4):
#     print("Enter message is a spam comment")

# else:
#     print("Enter message is not a spam commnet")


# # 5. Write a program which finds out whether a given name is present in a list or not.

# list = ["Nitish","Rakesh","Shivam","Vasu"]

# name = input("Enter name :")

# if(name in list):
#     print("Name is present in list")

# else:
#     print("Name is not present in list")


