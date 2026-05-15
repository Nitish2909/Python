class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Age : "))
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    else:
        print("Age is ", age)

except InvalidAgeError as e:
    print("Error :", e)