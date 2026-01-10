
"""

1. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
"""

# class Programmer:
#     name="NItish"
#     age=21
#     qualification="BTECH"
#     salary="400000"

# p1 = Programmer()
# print(p1.name,p1.age,p1.qualification,p1.salary)


'''
2. Write a class “Calculator” capable of finding square, cube and square root of a
number.
'''

# class Calculator:
#     def __init__(self,n , n2 , n3):
#          self.n=n
#          self.n2=n2
#          self.n3=n3
#     def square(self):
#          print(f"The Square of Given Number is {self.n*self.n}")     
#     def cube(self):
#          print(f"The cube of Given Number is {self.n2*self.n2*self.n2}")     
#     def squareRoot(self):
#          print(f"The SquareRoot of Given Number is {self.n3**1/2}")     

# c1 = Calculator(4 , 4 ,4)
# c1.square()
# c1.cube()
# c1.squareRoot()


"""
3. Create a class with a class attribute a; create an object from it and set "a"
directly using "object.a = 0". Does this change the class attribute?
"""
# Answer is no it just add an object attribute not change the class attribute
# class A:
#    a=4

# a1 = A()
# print(a1.a)
# a1.a=0
# print(a1.a)

# print(A.a)

"""
4. Add a static method in problem 2, to greet the user with hello
"""
class Calculator:
    def __init__(self,n , n2 , n3):
         self.n=n
         self.n2=n2
         self.n3=n3
    
    @staticmethod
    def greet():
         print("Hello")
    def square(self):
         print(f"The Square of Given Number is {self.n*self.n}")     
    def cube(self):
         print(f"The cube of Given Number is {self.n2*self.n2*self.n2}")     
    def squareRoot(self):
         print(f"The SquareRoot of Given Number is {self.n3**1/2}")     

c1 = Calculator(4 , 4 ,4)
c1.greet()
c1.square()
c1.cube()
c1.squareRoot()


