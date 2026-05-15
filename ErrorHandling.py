a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

try:
    result = a / b
    print("Result", result)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except ValueError:
    print("Invalid input")

else:
    print("Run only if no error occurs")

finally:
    print("Program ended.This runs always")



# # simple program:

# try:
#     result = a/b
#     print("Result is ", result)

# except:
#     print("Cannot Divide By Zero")


