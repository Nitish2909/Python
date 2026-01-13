
# Logical operators

# And

# Example : 1

# username="admin"
# password="12345"

# if(username=="admin" and password=="12345"):
#     print("Successful login")

# else:
#     print("Invalid credentials")


# Example : 2

# marks=65
# attendance=80

# if(marks>=45 and attendance>=75):
#     print("Student pass")
# else:
#     print("Student fail")



# # OR operator :

# age =65
# is_member=True

# if(age >=60 or is_member):
#     print("Discount allowed")

# else:
#     print("discount is not allowed")




# Bitwise operator :

# # bitwise And => &

# a =5       #    0101
# b =3       #  & 0011
#            #   -------
#            #    0001
# print(a&b)

#       # output =1


# a =12     # 1100
# b= 8      # 1000
#           # -----
#           # 1000

# print(a&b)

#        #output = 8


# # bitwise OR => | 

# a =7     # 0111
# b =5     # 0101
#          #------
#          # 0111

# print(a|b)


# # bitwise XOR => ^

# Result bit is 1 if bits are different and if both bits are 1 tahn it return 0

# a = 7    # 0111
# b = 8    # 1000
#          #------
#          # 1111

# print(a^b)


# bitwise not =>  ~

a = 9   # 00001001 (binary of a=9)
        # 11110110 (apply bitwise not = ~a)
        

        # 00001001   (1's complement of  ~a)
        #       +1    (2' complement )
        #----------
        # 00001010  
print(~a)

        # output = -9

# left shift  =>   <<

a = 5

print(a<<2)


