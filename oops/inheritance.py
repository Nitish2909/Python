
# # Parent Class

# class Person:
#     def __init__(self,name,salary):
#         self.name= name
#         self.salary=salary

#     def showinfo(self):
#         print(f"{self.name} {self.salary}")    

# # p1 = Person("Nitish",250000)
# # p1.showinfo()


# # Child class

# class Employee(Person):
#     def __init__(self, name, salary,):
#        super().__init__(name,salary)
#        self.joiningYear=2020
# E = Employee("Rakesh",230000)
# print(E.joiningYear)



# single inheritance

# class Parent:
#     def show(self,name):
#         self.name=name
#         print("This is a parent class")

# class Child(Parent):
#     def display(self):
#        print("This is a child class that inherit properties and methods from parent class")
#        print(f"{self.name}")

# c1 = Child()
# c1.show("Rakesh")
# c1.display()


# # Multiple inheritance

# class Parent1:
#     def show(self,name):
#         self.name=name
#         print("This is a parent class")

# class Parent2:
#     def show2(self):
#         print("This is second parent class")

# class Child(Parent1,Parent2):
#     def display(self):
#        print("This is a child class that inherit properties and methods from parent class")
#        print(f"{self.name}")

# c1 = Child()
# c1.show("Rakesh")
# c1.show2()
# c1.display()


# # Multilevel inheritance

# class GrandParent:
#     def __init__(self,grandfathername):
#         self.grandfathername=grandfathername

# class Parent(GrandParent):
#     def __init__(self,fathername,grandfathername):
#         self.fathername=fathername
#         # call the constructor of GrandParent
#         GrandParent.__init__(self,grandfathername)
        
# class Child(Parent):
#     def __init__(self,sonname,fathername,grandfathername):
#         self.sonname=sonname
#           # call the constructor of Parent
#         Parent.__init__(self,fathername,grandfathername)
      
#     def printname(self):
#         print("Grandfather Name:",self.grandfathername)
#         print("Father Name:",self.fathername)
#         print("Child Name:",self.sonname)
        
# c1 = Child("Mohan","Sohan","Rohan")
# c1.printname()


# # Hieraachical inheritance

# class Person:
#     def show(self):
#         print("I am a person")

# class Student(Person):
#     def role1(self):
#         print("I am a student")

# class Teacher(Person):
#     def role2(self):
#         print("I am a teacher")

# s = Student()
# t = Teacher()

# s.show()
# s.role1()

# t.show()
# t.role2()
