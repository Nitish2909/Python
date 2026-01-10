
# class Students:
#     name="Nitish"
#     rollNo = 35
#     age=21
#     course="BCA"
    
#     # This is fuction that takes "self " as a parameters
#     def greet(self):
#         print("Good Morning Everyone")

# s1 = Students()
# print(s1.name,s1.age,s1.course)

# s1.greet()



# # Accessing Properties with self


# class person:
#     def __init__(self,name,course,age,rollno):
#         self.name=name
#         self.course=course
#         self.age=age
#         self.rollno=rollno

#     def displayinfo(self):
#         print(f"{self.name} {self.course} {self.age} {self.rollno}")


# p1 = person("Nitish","BCA",21,24)

# p1.displayinfo()


class Employee:
  
  def __init__(self, name):
       self.name=name

  def getSalary(self):
      print(f"{self.name}")
      
e1= Employee("Harry")
e1.getSalary()
