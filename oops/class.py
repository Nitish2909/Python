class Myclass:  
    # This is a class named Myclass
    # A class is a blueprint or template

    name = "Nitish Kumar"   # Class attribute (shared by all objects)
    language = "python"     # Class attribute
    rollNo = 35             # Class attribute


# Creating an object (instance) of Myclass
obj = Myclass()  
# obj is now an instance (object) of the class Myclass
# Memory is allocated for this object

obj.age=21   # This is an object attribute

# Accessing class attributes using the object
print( obj.age ,obj.name, obj.rollNo)
