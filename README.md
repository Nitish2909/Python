# Python:
Python is a simple, high level ,general purpose and interpreted programming language.It is designed to be simple and easy to learn.One of the key Features of this language is their simple syntax , open source and its versibility.
Python was created by <b>Guido van Rossum and first released in 1991</b>. It focuses on readability and uses simple, English-like syntax.
Python is a Object Oriented Programming language.

# Featurse of Python:

```bash

Simple & Easy to Learn -> readable syntax.

Interpreted Language  ->no need to compile. It runs line by line code.

High-Level -> memory management handled automatically.

Portable -> runs on Windows, Linux, macOS.

Open Source -> free to use.

Large Standard Library -> many built-in modules

```

# Python Interpreter:
A Python interpreter is a program that reads, translates, and executes Python code line by line. It converts Python source code into bytecode(machine-understandable) instructions and produces output immediately.
<br>
There is no separate compilation step, which makes Python an interpreted language.
<br>

<b>How interpreter Works:</b>

```bash

1. You write Python code.

2. Interpreter reads the code line by line.

3. Code is converted into bytecode.

4. Bytecode is executed by the Python Virtual Machine (PVM).

```
# Python as a Calculator:
Python can be used as a powerful calculator to perform basic and advanced mathematical calculations. This is usually done using the Python interpreter in interactive mode.
<br>

<b>How to use python as a calculator:</b>

```bash
1. Open command prompt or Terminal.

2. Type "python" . This open REPL(Read , Evaluate , Print ,Loop) in your cmd or terminal.

3. Type any calculation just like:
   
 2+2 = 4

4. For exit python type:
  
   exit()

```

# Python Shell:
The Python Shell is an interactive environment where you can write and execute Python commands one line at a time and get instant output. Python Shell is also called interactive interpreter.
<br>
It is identified by this :

```bash

>>>

```
<br>

<b>How to open Python shell :</b>

```bash

1. Open terminal or command prompt.

2. Type:
     python

3. You  will see:
    
    >>>

```

Example:

```bash
>>> print("Hello Python")
Hello Python
>>> 10 + 5
15
```
# indentation in python:
Indentation means the spaces or tabs at the beginning of a line of code.In Python, indentation is very important because it is used to define blocks of code.
<br>
 Unlike C, C++ or Java (which use { }), Python uses indentation to show structure or define the block of code.
<br>

<b>Why Indentation is important:</b>

```bash
1.It tells Python which statements belong together.

2.Controls the flow of:

if-else

for and while loops

functions

classes

3.Wrong indentation causes an Indentation error

```
Example:

```bash
num=8

if num%2==0:
    print("even number")
else:
    print(" odd number")    

```
# Comments in Python:
Comments are lines in a program that are ignored by the Python interpreter.
<br>
They are used to explain code, make programs easy to understand, and improve readability.
<br>

<b>Types of comments:</b>
<br>
There are Two types of comments in python:
<br>

1. Single-Line comments:
<br>
Single-Line commnets starts with hash sign (#). Anything written after hash sign is consider as comments and that line id ignored by python interpreter.
<br>
Example:

```bash
# This is a single-line comment
x = 10  # variable storing value

```
2. Multi-Line Comments:
<br>
Python does not have a separate multi-line comment syntax.
But we use triple quotes (''' or """) for multi-line comments (actually multi-line strings).
<br>
Example:

```bash
"""
This is a multi-line comment
used to explain
multiple lines of code
"""
```

# Variable in Python:
In python variables are used to store values that can be used later in a program. You think variable as a container that holds data.In python you don't need to explicitly declare the type of variable.You just simply assign a value to a variable by using " = " operator.
<br>

<b>Rules for Naming Variables</b>

```bash
1. Must start with a letter (a-z, A-Z) or underscore (_).

2. Cannot start with a number.

3. Can contain letters, numbers, and underscores.

4.Case-sensitive (age and Age are different).

5. Cannot use Python keywords.

```
Example:

```bash

# for creating variable no need to declare the type

name = "Nitish"
age = 20
_total = 100


# Multiple Assignment

a , b ,c = 1,3,4

```
# Identifiers:
An identifier is the name given to a variable, function, class, object, or module in Python. <br>
Identifiers are used to identify program elements uniquely. <br>

<b> Rules for Identifiers in Python:</b>

```bash

1. Must start with a letter (a-z or A-Z) or an underscore (_)

2.Cannot start with a number.

3. Can contain letters, numbers, and underscores.

4. No special characters like @, $, %, -

5. Case-sensitive (total and Total are different).

6.Cannot use  Python keyword.

```
<b>Here are some valid Identifiers:</b>

```bash
x
total_marks
_sum
student1
calculateTotal

```
<b>Some invalid Identifiers:</b>

```bash

1num       # starts with number
total-marks # hyphen not allowed
class      # keyword
@value     # special character

```
# Keywords:
Keywords are reserved or predfined  words in Python that have special meaning and cannot be used as identifiers (variable names, function names, etc.)
<br>
Python keywords define the syntax and structure of the language.
<br>

<b>List of keyword in python:</b>
<br>
There are total 35 keyword in python:

```bash

False    None     True
and      as       assert
async    await    break
class    continue def
del      elif     else
except   finally  for
from     global   if
import   in       is
lambda   nonlocal not
or       pass     raise
return   try
while    with     yield

```
Example of keywords in use:

```bash

if x > 0:
    print("Positive")
else:
    print("Negative")

    # Here if and else are keywords

```

<b>Categories of Keywords (For Simple Understanding):</b>

```bash

1. Control flow :- if, else, elif, for, while, break, continue

2. Logical:-  and, or, not

3. Value :- True, False, None

4. Function & class :- def, return, class

5. Exception handling :- try, except, finally, raise

6. Others :- import, from, pass, lambda, yield

```

<br>

<b>How to check keywords in python:</b>

```bash

import keyword
print(keyword.kwlist)

```

# Literals in python:
Literals in Python are fixed values written directly in the code that represent constant data. They provide a way to store numbers, text, or other essential information that does not change during program execution. Python supports different types of literals, such as numeric literals, string literals, Boolean literals, and special values like None.
<br>
<b> For example:</b>

```bash

10, 3.14, and 5 + 2j are numeric literals.
'Hello' and "Python" are string literals.
True and False are Boolean liter.

```

<b><u>Types of Literals:</u></b>
<br>

<b>1. Numeric Literals:</b>

<br>
Numeric literals represent numbers and are classified into three types:

1. Integer Literals -> Whole numbers (positive, negative, or zero) without a decimal point. 
<br>
   Example: 10, -25, 0
<br>

2. Floating-point (Decimal) Literals -> Numbers with a decimal point, representing real numbers.
<br>
   Example: 3.14, -0.01, 2.0
<br>

3. Complex Number Literals -> Numbers in the form a + bj, where a is the real part and b is the imaginary part.
<br>
  Example: 5 + 2j, 7 - 3j
<br>

Example:

```bash

# Integer literals
a = 100
b = -50

# Floating-point literals
c = 3.14
d = -0.005

# Complex number literals
e = 4 + 7j
f = -3j

print(a, b, c, d, e, f)

```
<br>

<b>2. String Literals:</b>

<br>
String literals are sequences of characters enclosed in quotes. They are used to represent text in Python.
<br>

<b>Types of String Literals:</b>

<br>
1. Single-quoted strings ->  Enclosed in single quotes (' ').
<br>
   Example: 'Hello, World!'
<br>

2. Double-quoted strings -> Enclosed in double quotes (" ").
<br>
   Example: "Python is fun!"
<br>

3. Triple-quoted strings -> Enclosed in triple single (''' ''') or triple double (""" """) quotes, generally used for multi-line strings or docstrings.
<br>
   Example:
   '''This is
   a multi-line
   string'''
<br>

4. Raw strings -> Prefix with r to ignore escape sequences (\n, \t, etc.). Example: r"C:\Users\Python" (backslashes are treated as normal characters).
<br>

Example of String Literals:

```bash

# Different string literals

a = 'Hello'      # Single-quoted
b = "Python"     # Double-quoted

c = '''This is 
a multi-line string'''  # Triple-quoted

d = r"C:\Users\Python"  # Raw string

print(a)
print(b)
print(c)
print(d)

                  Output:
                  Hello
                  Python
                  This is 
                  a multi-line string
                  C:\Users\Python
```
<br>

<b>3. Boolean Literals:</b>

<br>
Boolean literals represent truth values in Python. They help in decision-making and logical operations. Boolean literals are useful for controlling program flow in conditional statements like if, while, and for loops.
<br>
Types of Boolean Literals:
<br>
True ->  Represents a positive condition (equivalent to 1)
<br>
False -> Represents a negative condition (equivalent to 0)
<br><br>
Example:

```bash
# Boolean literals
a = True
b = False

print(a, b)       # Output: True False
print(1 == True)  # Output: True
print(0 == False) # Output: True
print(True + 5)   # Output: 6 (1 + 5)
print(False + 7)  # Output: 7 (0 + 7)

```
<br>

<b>4. Collection Literals:</b>

<br>
Python provides four different types of literal collections:
<br>
1. List literals: [1, 2, 3]
<br>
2. Tuple literals: (1, 2, 3)
<br>
3. Dictionary literals: {"key": "value"}
<br>
4. Set literals: {1, 2, 3}
<br><br>
Example:

```bash
Rank = ["First", "Second", "Third"]  # List

colors = ("Red", "Blue", "Green")  # Tuple

Class = { "Jai": 10, "Anaya": 12 }  # Dictionary

unique_num = {1, 2, 3}  # Set

print(Rank, colors, Class, unique_num)

```
# Operator :
In Python programming, Operators are used to perform operations on values and variables.
<br>
Operators: Special symbols like -, + , * , /, etc.
<br>
Operands: Value on which the operator is applied.
<br>

<b>Types of operators:</b>
<br>
<b>1. Arithmetic operators</b> -> Arithmetic operators are used to perform mathematical operations on numeric values.
 
```bash
Operator     	Name        	Example	

+	          Addition	       x + y	

-	         Subtraction    	 x - y	

*	        Multiplication   	 x * y

/  	      Division           x / y

%	         Modulus	          x % y

**     	Exponentiation      	x ** y

//	       Floor division	   x // y

```
<br>
Example:

```bash
a=20
                               
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

```
<br>
<b>2.Assignment operators</b> -> Assignment operators are used to assign values to a variable.
  
```bash
Operator	      Example	   Same As

 =	             x = 5	   Assign

+=	            x += 3	   x = x + 3

-=	            x -= 2	   x = x - 2

*=	            x *= 2	   x = x * 2

/=	            x /= 2      x = x / 2

```
<b>3.Comparison / Relation operators</b> -> Comparison operators are used to compare two values and return a Boolean values.

```bash

Operator         	Meaning      	    Example

   ==	            Equal to	           5 == 5

   !=	            Not equal	        5 != 3

   >	            Greater than	     5 > 3

   <	            Less than	        5 < 3

   >=	            Greater or equal	  5 >= 5

   <=	            Less or equal	     5 <= 3
```   

<b>4.Logical operators</b> -> Logical operators are used to combine conditional statements.

```bash

Operator	                Meaning   	                                     Example	

and 	          Returns True if both statements are true	              x < 5 and  x < 10	

or	           Returns True if one of the statements is true	           x < 5 or x < 4	

not	     Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)

```

<b>5.Bitwise operators</b> -> Bitwise operators are used to compare (binary) numbers.

```bash
   Operator	   Name	                               Meaning     	                                Example

   &           AND	             Sets each bit to 1 if both bits are 1	                     x & y	

   |	          OR	             Sets each bit to 1 if one of two bits is 1	               x | y	

   ^	         XOR	             Sets each bit to 1 if only one of two bits is 1	         x ^ y	

   ~	         NOT	             Inverts all the bits	                                      ~x	
   <<	    Zero fill left shift	 Shift left by pushing zeros in from the right and let 
                                  the leftmost bits fall off	                               x << 2	
   >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from 
                                  the left, and let the rightmost bits fall off	              x >> 2
```
Example:

```bash
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010

print(6 & 3)
                      
                       output:
                       2
```

<b>6. Identity operators</b> -> Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

```bash
Operator                    	Meaning               	                           Example	

is 	              Returns True if both variables are the same object	         x is y	

is not	          Returns True if both variables are not the same object	      x is not y

```
Example:

```bash

# is

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)     #True
print(x is y)     #False
print(x == y)     #True


# is not 

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)    #True

```

<b>7.Membership operators</b> -> Check if a value exists in a sequence.

```bash

Operator          Meaning     	                                        Example

in               	Returns True if a sequence with the specified
                  value is present in the object                          'a' in "apple"

not in	         Returns True if a sequence with the specified value 
                  is not present in the object	                            5 not in [1,2,3]

```

# String in Python:
Strings are a data type in python that is used to represent collections of characters.String is a sequence of character that are enclosed in Single-quotes,Double-quotes,Triple-quotes.
<br>
Strings are immutable means once a string is created that cannot be changed. 

Example:

```bash

fname="Nitish"
lastName="Kumar"

print(fname+" "+lastName)

```

<b>Indexing :</b> Indexing is used to access individual characters or elements of a sequence (like string, list, tuple) using their position number.
<br>

Example:

```bash

text ="Python"

 Index  0  1  2  3  4  5 

 Char   P  y  t  h  o  n
 
 
# How to access character using Indexing

text="Python"

print(text[4])

 ```
<b> String operators:</b>

```bash

Operator	       Use           	Example

   +	     Concatenation	   "Hi" + " All"

   *	     Repetition	      "Hi" * 3

   in	    Membership	        "P" in "Python"

```
<br>
 Example:

 ```bash
 fname="Nitish"
lastName="Kumar"

print(fname+" "+lastName)  # concatenation

print(fname*3)     # Repetaion

print("N" in fname)   # Membership

```
<br>
<b>Slicing:</b>A string in python can be sliced for getting a part of the strings.

```bash

# syntax:

slice= name[index_start : index_end]

index_start -> first index included
index_end -> last index is not included


# Example:
text="Hello World"

print(text[0:4])   # start from index 0 all the way till 4 (excluding index 5)


```

<b>Common String Methods:</b>

```bash
Method	             Description

upper()	          Convert to uppercase

lower()	          Convert to lowercase

capitalize()	    First letter capital

title()	          Capitalize each word

strip()	          Remove spaces

replace()        	Replace text

split()	         Split string

find()	         Find substring

len()	            Length of string

```
<br>
Example:

```bash
msg= " hello world from python"

print(msg.upper())  #uper()

print(msg.lower())  #lower()

print(len(msg))  #len()

print(msg.title())  #title()

print(msg.capitalize())  #captalize()

print(msg.strip())  #strip()

print(msg.find("python"))  #find()

```

# Input and Output Statements:
In Python, input and output statements are used to take data from the user and display results on the screen. They are very important for writing interactive programs.
<br>

<b>input statements:</b>

<br>
An input statement is used to accept data (taking input) from the user at runtime.
<br>
Python uses the input() function to take input from users.
<br>
The data entered by the user is always in string format, so we must convert it when needed.
<br>

<b>Syntax:</b>

```bash
variable = input("Message to user")

```
<br>
Example:

```bash
name = input("Enter your name: ")
print("Hello", name)

```
<br>

<b>Input with Type Conversion:</b>

```bash
age = int(input("Enter your age: "))
print("Your age is", age)


# int() → converts input to integer
#float() → converts input to decimal number

```
<br>

<b>Output Statements:</b>
 An output statement is used to display information or result on the screen.
 <br>
 Python uses the print() function for output.
<br><br>
 Syntax:

 ```bash
print(value)
print(value1, value2)


#Example: 

print("Hello World")

```
# List:
In Python a list is a versatile data structure that allow you to store and organize multiple items in a single variable.Lists are defined by enclosing a sequence of elements within a square bracket and seprating them with commas.
<br>
Lists are ordered, mutable (changeable), and can store different data types.
<br><br>
Example:

```bash
numbers = [10, 20, 30, 40]

names = ["Ram", "Shyam", "Mohan"]

mixed = [1, "Python", 3.5, True]

```   
<br>

<b>List Indexing:</b>
<br>
A list can be indexed just like string.
<br>

```bash
number =[1,2,4,5,3,2,3,5,8]

print(number[1])

```
<br>

<b> List Slicing:</b>

```bash
number =[1,2,4,5,3,2,3,5,8]

print(number[1:6])  #[2, 4, 5, 3, 2]

print(number[0:4])   #[1, 2, 4, 5]

```
<b>Adding Elements to List</b>

```bash
   Method	        Use	                  Example

   append()	      Add one element	   list.append(50)

   insert()	      Add at position	   list.insert(1, 15)

   extend()	      Add multiple	      list.extend([60,70])
```
<br>

Example:

```bash
number =[1,2,4,5,3,2,3,5,8]

number.append(23)  #append()
number.insert(2,3)  #insert()
number.extend([123,22]) #ectend()
print(number)

```
<b>LIST METHODS:</b>

<br>
Consider the following list:

```bash
l1 = [1,8,7,2,21,15]
• l1.sort(): updates the list to [1,2,7,8,15,21]

• l1.reverse(): updates the list to [15,21,2,7,8,1]

• l1.append(8): adds 8 at the end of the list

• l1.insert(3,8): This will add 8 at 3 index

• l1.pop(2): Will delete element at index 2 and return its value.

• l1.remove(21): Will remove 21 from the list. 
```
# Tuple:
A tuple is an immutable ordered collection of elements enclosed in paranthesis (). It is used to stored related data that should not be modified. 
<br>
Tuples are immutable, meaning their values cannot be changed after creation.
<br><br>
Example:

```bash
t1 = (10, 20, 30)

t2 = ("Ram", "Shyam", "Mohan")

t3 = (1, "Python", 3.5)

```
<b>Common Tuple Functions</b>

```bash
      Function	        Use

      len()	          Length

      max()	          Largest

      min()	          Smallest

      sum()	           Total

      count()	       Count value

      index()	      Find position
```

# Dictionary in Python:
A dictionary in Python is a collection of data stored in key-value pairs.
<br>
Each key is unique and is used to access its value.
<br>
Dictionaries are unordered, mutable (changeable), and written using curly braces { }.
<br>

syntax:

```bash

dictionary_name = {
    key1: value1,
    key2: value2
}

```
<br>

Example:

```bash
students ={
    "name":"Nitish",
    "age":21,
    "class": "BCA",
    "RollNo":36
}
```

Accessing dictionary values:

```bash

print(students["name"])


# Accessing by using get method also.

print(students.get("age"))


# how add elements in dictionary
students["State"] ="Haryana"
print(students)


# how to updates elements in dictionary
students["age"]=22
print(students)


```
<br>

<b>Removing Items:</b>

```bash
student.pop("course")   # removes specific key
del student["age"]      # deletes key-value pair
student.clear()         # removes all items

```
<br>

<b>Method	Description</b>

```bash

clear()	  ->   Removes all the elements from the dictionary.

copy()	  ->   Returns a copy of the dictionary.

fromkeys()	 ->  Returns a dictionary with the specified keys and value.

get()	      ->  Returns the value of the specified key.

items()	  ->   Returns a list containing a tuple for each key value pair.

keys()	   ->  Returns a list containing the dictionary's keys.

pop()	      ->  Removes the element with the specified key.

popitem()	  -> Removes the last inserted key-value pair.

setdefault()   ->	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

update()	 -> Updates the dictionary with the specified key-value pairs.

values()  ->	Returns a list of all the values in the dictionary.

```

# Sets:
A set in Python is a collection of unique elements.
<br>
It is unordered, mutable, and does not allow duplicate values.
<br>

Syntax:

```bash

set_name = {value1, value2, value3}

```
Example:

```bash
numbers = {1, 2, 3, 4, 5}
print(numbers)

```
<br>

<b>PROPERTIES OF SETS</b>

```bash
1. Sets are unordered => Element's order doesn't matter.
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

```
<br>

<b>some important points with example:</b>

```bash
# how to create sets:
mysets = {1,2,3,7,8,9,4,3,5,6,7,8}
print(mysets)

#How to create an empty sets:
sts = set()
print(type(sts))

# how to add an elements:
mysets.add(234)
print(mysets)

# add multiple elements in sets:

mysets.update([123,345,678,890])
print(mysets)

```
<br>

<b>Operation on Sets:</b>

```bash

# Union  -> It combines both sets in single one.

set1 ={12,13,14,15,16}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 | set2)


# Intersection   ->  It searches common elements in both sets

set1 ={12,13,1,15,16,4,6,7,2}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 & set2)


# Difference -> It returns elements that are present in the first set but NOT in the second set.

set1 ={12,13,1,15,16,4,6,7,2}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 - set2)

```
<br>

<b>Set Methods:</b>

```bash

Method	           Use

add()            	Add element

update()	         Add multiple elements

remove()	         Remove element

discard()	      Remove without error

union()	         Combine sets

intersection()	    Common elements

difference()	    Remaining elements

clear()	          Empty set
 
```

# Conditional Statements:
Conditional statements are used to make decisions in a program.
They allow the program to execute different blocks of code based on a condition.
<br>

1.<b>If Statements:</b> The if Statements is used in python to Executes a block of code only if the condition is true.
<br>

Syntax:

```bash

if condition:
    statement

```
<br>

Example:

```bash
age = 20
if age >= 18:
    print("Eligible to vote")

```
<br>

2.<b>If else</b> : The if else statements in python provides a way to perform different action based on a evaluation of a condition. It allows us to executes first block of code if condition is true and executes another block if condition is false.
<br>

<b>Syntax:</b>

```bash

if condition:
    statement
else:
    statement

```
<br>

<b>Example:</b>

```bash
age=20

if(age>=18):
    print("Your are Eligible to vote ")

else:
    print("Your are not Eligible to vote")

```
<br>

3.<b>If-elif-else :</b> This Statements is used when there are multiple condition.
<br>
important point about elif:
<br>
1. There can be any number of elif statements.
<br><br>
2. Last else is executed only if all the conditions inside elifs fail.
<br>

<b>Syntax:</b>

```bash
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```
<br>

<b>Example:</b>

```bash

# if-elif-else:

marks =75

if(marks >=90):
    print("Grade A")

elif(marks >=60):
    print("Grade B")

else:
    print("Grade C")
   
```

4.<b>Nested if statement:</b> An if statement inside another if statement in this condition we can say that it is a Nested if statement.
<br>

<b>Syntax:</b>

```bash

if condition1:
     statement

      if condition2:
          statement

      else:

else:

```
<br>

<b>Example:</b>

```bash

age = int(input("Enter Your Age :"))
salary= int(input("Enter Your Salary :"))

if(age >=18):
    {
           print("Eligible")
    }

    if(salary >=40000):
        {
            print("You are Eligible for Loan ")
        }
    else:
        {
            print("Not Eligible for Loan")
        }
else:
    print("Your Not Eligible")

```
5.<b>Short-hand if (One-line if)</b>

```bash
a = 10
if a > 5: print("Greater than 5")
```
<br>

6. <b>Short-hand if-else (Ternary Operator):</b>

```bash
a = 3
print("Even") if a % 2 == 0 else print("Odd")

```
# Loops:
Loops in Python are used to repeat a block of code multiple times until a condition is met or satisfied.
<br>

<b>Types of Loops :</b>
<br>
There are mainly two types of loops:
<br>

1. while Loop
<br><br>
2. for Loop
<br>

1. <b>while loop:</b> This loop is used when the number of iterations is not known.
<br>

<b>Syntax:</b>

```bash
while (condition):   # The block keeps executing until the condition is true
    statement


```
<br>
In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!
<br><br>
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False

<b>Example:</b>

```bash

# print 1 to 20 

i =0
while(i<=20):
    print(i)
    i = i+1
    
```
2. <b>For Loop :</b> This loop is used when the number of iterations is known.
<br>

<b>Syntax:</b>

```bash
for variable in sequence:
    statements
```
<br>

<b>Example:</b>

```bash

fruits = ["apple","mango","banana","papaya","pineapple"]

for fruit in fruits:
    print(fruit)
```

# Range function in python:
The range() function is used to generate a sequence of numbers.It is mainly used with for loops.
<br>
range() returns a sequence of numbers starting from a given value up to (but ending value not including) the ending value.
<br>

<b>Syntax:</b>

```bash
range(start, stop, step)           # Meaning
                                   start -> Starting value (default = 0)

                                   stop -> Ending value (not included)

                                   step -> Difference between numbers (default = 1)

```
<br>

<b>Example:</b>

```bash
for num in range(1 ,10):

    print(num)   # prints 1 to 9

```

# FOR LOOP WITH ELSE :
An optional else can be used with a for loop if the code is to be executed when the
loops exhausts.
<br>

<b>Example:</b>

```bash

l= [1,7,8]

for item in l:
print(item)

else:
print("done") # this is printed when the loop exhausts!


                  Output:
                  1
                  7
                  8
                  done

```

# Break statements :
The break statement is a loop control statement used to terminate (stop) a loop immediately, even if the loop condition is still true.
<br>

Example:

```bash
# break in for Loop

for i in range(1,8):
    if i==5:
        break
    print(i)

```

# continue statements:
The continue statement is a loop control statement used to skip the current iteration of a loop and move to the next iteration.
<br>

<b>Example:</b>

```bash
   
for i in range(1,8):
    if i==5:
        continue     # by using this statements it skip 5 
    print(i)
 

               output :
               it print 1 ,2 ,3 ,4 ,6 ,7
               
```
# Pass statement :
The pass statement is used as a placeholder where a statement is required but no operation is to be performed.
<br>

<b>Example:</b>

```bash

for i in range(5):
    pass

           # loop run but does nothing


```

# Function in Python:
A function is a block of reusable code that performs a specific task.
It runs only when it is called and helps in reducing and avoiding code repetition.
In Simple Word we can say that a function is a block of code that perform a specific task.
<br>

<b>Creating a function:</b>
<br>
In Python, a function is defined by using "def" keyword and function name  and paranthesis.
<br>

```bash
# function definition
def my_function():
    print("Hello from a function")

# function call
my_function()


#The code inside the function must be indented. Python uses indentation to define code blocks.

```
<br>

<b>Why we use Function:</b>

```bash

Reuse code

Reduce repetition

Make programs easy to understand

Improve modularity

Easy to maintain and debug

```
<br>

<b>Function Name Rules:</b>

```bash
Function names follow the same rules as variable names in Python:

        A function name must start with a letter or underscore.
        A function name can only contain letters, numbers, and underscores.
        Function names are case-sensitive (myFunction and myfunction are different).

```
<br>

<b>Types Of Function :</b>
<br>
There are two types of function:
<br>
<br>
1. <b>Built-in function :</b> print() , len() , input().
<br><br>
2. <b>User-defined function :</b> This type of function is created by programmers.
<br>

<b>FUNCTION DEFINITION :</b>
The part containing the exact set of instructions which are executed during the function call.
<br>

<b> FUNCTION CALL :</b>
Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
<br>

```bash
func1() # This is called function call

```
<br>

<b>Defalut parameters value :</b>
A default parameter value is a value given to a function parameter at the time of function definition.
<br>
If no argument is passed during the function call, the default value is used automatically.
<br>

```bash
def greet(name="Guest"):
    print("Hello", name)

greet("Nitish")
greet()


                    output:
                    Hello Nitish
                    Hello Guest


```
# Recursion in Python:
Recursion is a technique in which a function calls itself to solve a problem by breaking it into smaller subproblems.
<br>
In Simple world we can say that Recursion is a process where a function calls itself until a base condition is met.
<br>

<b>Every recursive function have two parts:</b>
<br>

```bash

1. Base Case => Condition where the function stops calling itself.

2. Recursive case => The function calls itself with a smaller problem.

<br>
It is used to directly use a mathematical formula as function. 
<br>
Example of using mathematical formula:

```bash
factorial(n) = n x factorial (n-1)
```
<br>



<b>Example of recursion</b>

```bash

def factorial(n):    

    if(n==0 or n==1 ):       # Base case 
        return 1
    return n * factorial(n-1)   # recursive case because it call itself .

n= int(input("Enter a Number :"))

print(" Factorial of given numbers is ",factorial(n))

```
<br>

<b>How factorial(5) works (Step by Step) :</b>

```bash

factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120

```
<br>

<b>fibonacci series :</b> The Fibonacci series is a sequence of numbers where each number is the sum of the previous two numbers.
<br>

```bash

Series:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Formula:

F(n) = F(n-1) + F(n-2)

```
<br>

<b>Example:</b>

```bash

def fibonacci(n):
      
      if( n ==0):  # base case
            return 0
      elif(n==1):  # base case
            return 1
      else:
        return fibonacci(n-1) + fibonacci(n-2)   # recursive case

n= int(input("Enter a Number :"))

for i in range(n):

 print(fibonacci(i) , end="")

```
<br>

<b>Dry run of this code:</b>

```bash

Assume input :

Enter Number : 5

range(n) -> range(5) -> i = 0, 1, 2, 3, 4


Iteration 1 :

i = 0
fibonacci(0) -> base case -> return 0
Printed: 0

Iteration 2 :

i = 1
fibonacci(1) -> base case -> return 1
Printed: 1

Iteration 3 :

i = 2
fibonacci(2)
= fibonacci(n-1) + (n-2)
= fibonacci(2-1) + (2-2)
= fibonacci(1) + fibonacci(0)
= 1 + 0
= 1
Printed: 1

Iteration 4 :

i = 3
fibonacci(3)
= fibonacci(n-1) + (n-2)
= fibonacci(3-1) + (3-2)
= fibonacci(2) + fibonacci(1)
= 1 + 1
= 2
Printed: 2

Iteration 5 :

i = 4
fibonacci(4)
= fibonacci(n-1) + (n-2)
= fibonacci(4-1) + (4-2)
= fibonacci(3) + fibonacci(2)
= 2 + 1
= 3
Printed: 3


                            output :
                            0 1 1 2 3

```

# OOP in Python:
 OOP stands for Object-Oriented Programming. <br>
 Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
<br>

```bash
Advantages of OOP:

Provides a clear structure to programs.

Makes code easier to maintain, reuse, and debug.

Helps keep your code DRY (Don't Repeat Yourself).

Allows you to build reusable applications with less code. 

         The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

```
<br>

1. <b>Class and Object:</b>
<br>

<b>Class :</b> A class is a blueprint / design /template  for creating an object.It defines properties(attributes) and behaviour(methods) that object of this class will have.
<br>
When a class is created it does not occupy memory itself.
<br>

<b>Object :</b> An object is a real world entity created by using a class.It occupies memory and can be used in a program.

Example:

```bash

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


# Accessing class attributes using the object
print(obj.name, obj.rollNo)

```
<br>

<b>Working of Above Example :</b>

```bash

Step 1: Class Definition

class Myclass:


- Python creates a class named Myclass

- No memory is allocated yet for objects

- Only the structure is defined


Step 2: Class Attributes

name = "Nitish Kumar"
language = "python"
rollNo = 35


- These are class variables (attributes)

- They belong to the class, not to any specific object

- All objects of Myclass can access these values


Step 3: Object Creation (Instance Creation)

obj = Myclass()


- Myclass() creates a new object

- obj stores the reference (address) of that object

- This object is an instance of Myclass

- Memory is allocated at runtime


Step 4: Accessing Attributes Using Object

print(obj.name, obj.rollNo)


- Python looks for name inside the object

- If not found, it checks the class

- Finds name and rollNo in Myclass

Prints the values

```

<b> SELF PARAMETER :</b>
self refers to the instance of the class. It is automatically passed with a function call from an object.
<br>
It is used to access properties(attribute) and methods that belong to the class.
<br>
You can use any name as a function parameters in place of "self".

Example :

```bash

class Students:
    name="Nitish"
    rollNo = 35
    age=21
    course="BCA"
    
    # This is fuction that takes "self " as a parameters
    def greet(self):
        print("Good Morning Everyone")

s1 = Students()
print(s1.name,s1.age,s1.course)

s1.greet()

```
<b>Accessing Properties with self :</b>

```bash
# Accessing Properties with self


class person:
    def __init__(self,name,course,age,rollno):
        self.name=name
        self.course=course
        self.age=age
        self.rollno=rollno

    def displayinfo(self):
        print(f"{self.name} {self.course} {self.age} {self.rollno}")


p1 = person("Nitish","BCA",21,24)

p1.displayinfo()

```
<br>

<b>STATIC METHOD</b>
Sometimes we need a function that does not use the self-parameter. We can define a
static method like this:
<br>

Example:

```bash
@staticmethod   # decorator to mark greet as a static method
def greet():
     print("Hello user")

```

<b>__init__ () Method :</b>
__init__() is a special method which is first run as soon as the object is created. <br>
__init__() method is also known as constructor.
<br>
It takes "self" argument and can also take further arguments.
<br>
The __init__() function is called automatically every time the class is being used to create a new object. 
<br>

Example:

```bash


class Employee:
  
  def __init__(self, name):
       self.name=name

  def getSalary(self):
      print(f"{self.name}")
      
e1= Employee("Harry")
e1.getSalary()

```
# Inheritance :
Inheritance means one class inherit or acquires the properties and methods of another class.
<br>
It helps in code reuse, reduces repetition, and makes programs easy to maintain.
<br>

<b>Basic Terms of inheritance :</b>

```bash
    Term	                                 Meaning

Parent / Base class	     =>      Class whose properties are inherited.
Child / Derived class    =>   	 Class that inherits from parent.
Inheritance	             =>     Relationship between parent and child.

```
<br>

<b>Syntax of inheritance :</b>

```bash

class Parent:
    # parent class code

class Child(Parent):
    # child class code

```
<br>

Example:

```bash
# Parent Class

class Person:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary

    def showinfo(self):
        print(f"{self.name} {self.salary}")    

p1 = Person("Nitish",250000)
p1.showinfo()


# Child class

class Employee(Person):
    pass

E = Employee("Rakesh",230000)
E.showinfo()

```
<br>

<b>What is the Use of "Pass" Keyword :</b>
<br>
The pass keyword  is used when you do not want to add any other properties or methods to the class.
<br>

<b> __init__() Function in inheritance :</b>
<br>
The __init__() function is called automatically every time the class is being used to create a new object.
<br>

```bash
class Employee(Person):
    def __init__(self, name, salary):
        # add properties etc.

```
<br>
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
<br><br>
Because  The child's __init__() function overrides the inheritance of the parent's __init__() function.
<br><br>
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
<br>

```bash
class Employee(Person):
  def __init__(self, name, salary):
    Person.__init__(self, name, salary)

```
<br>
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
<br>

<b>Use of super() Function :</b>
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
<br>

Example:

```bash
class Employee(Person):
  def __init__(self, name, salary):
    super().__init__(self, name, salary)


    # By using super function no need to use parent class name.
```
<br>

<b>Types of Inheritance :</b>
<br>
Python supports 5 types of inheritance:
<br>

1. <b>Single inheritance:</b>
<br>
In a single inheritance there is only one  parent and one child.
<br>

Syntax:

```bash
class Parent:
    pass

class Child(Parent):
    pass

```
<br>

Example:

```bash
# single inheritance

class Parent:
    def show(self,name):
        self.name=name
        print("This is a parent class")

class Child(Parent):
    def display(self):
       print("This is a child class that inherit properties and methods from parent class")
       print(f"{self.name}")

c1 = Child()
c1.show("Rakesh")
c1.display()

```
<br>

2. <b>Multiple inheritance :</b> 
<br>
In Multiple Inheritance there is one child class and two or more parent class.
<br>

Syntax:

```bash
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

```
<br>

Example:

```bash

# Multiple inheritance

class Parent1:
    def show(self,name):
        self.name=name
        print("This is a parent class")

class Parent2:
    def show2(self):
        print("This is second parent class")

class Child(Parent1,Parent2):
    def display(self):
       print("This is a child class that inherit properties and methods from parent class")
       print(f"{self.name}")

c1 = Child()
c1.show("Rakesh")
c1.show2()
c1.display()

```
<br>

3. <b>Multilevel Inheritance :</b>
<br>
Multilevel inheritance is a type of inheritance in which a class is derived from another derived class, forming a chain of inheritance. <br>
Example :
<br>
GrandParent -> Parent -> child
<br>

Syntax:

```bash

# Base/ Parent class
class A:
    pass

# Intermediate class
class B(A):
    pass

# Derived/child class
class C(B):
    pass

```
<br>

Example:

```bash

class GrandParent:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername

class Parent(GrandParent):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        # call the constructor of GrandParent
        GrandParent.__init__(self,grandfathername)
        
class Child(Parent):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
          # call the constructor of Parent
        Parent.__init__(self,fathername,grandfathername)
      
    def printname(self):
        print("Grandfather Name:",self.grandfathername)
        print("Father Name:",self.fathername)
        print("Child Name:",self.sonname)
        
c1 = Child("Mohan","Sohan","Rohan")
c1.printname()

```
<br>

<b>Flow Chart of This Program :</b>

```bash
┌───────────────────────────┐
│        Program Start      │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│  Class GrandParent Loaded │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│    Class Parent Loaded    │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│     Class Child Loaded    │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│  Object Creation          │
│  c1 = Child("Mohan",      │
│             "Sohan",      │
│             "Rohan")      │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ Child.__init__() called   │
│ self.sonname = "Mohan"    │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ Parent.__init__() called  │
│ self.fathername="Sohan"  │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ GrandParent.__init__()    │
│ self.grandfathername=    │
│ "Rohan"                  │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ c1.printname() called     │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ Print Grandfather Name    │
│ Print Father Name         │
│ Print Child Name          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        Program End        │
└───────────────────────────┘
```
<br>

4. <b>Hierarchical Inheritance :</b>
<br>
Hierarchical inheritance is a type of inheritance in which multiple child classes inherit from a single parent class.
In simple term there is One parent class and multiple child class.
<br>

Syntax:

```bash
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

```
<br>

Exmaple:

```bash

class Person:
    def show(self):
        print("I am a person")

class Student(Person):
    def role1(self):
        print("I am a student")

class Teacher(Person):
    def role2(self):
        print("I am a teacher")

s = Student()
t = Teacher()

s.show()
s.role1()

t.show()
t.role2()

```
<br>

5.<b>Hybrid Inheritance :</b>
<br>
Hybrid inheritance is a type of inheritance that combines two or more types of inheritance (such as multiple, multilevel, or hierarchical) in a single program.
<br>

Syntax:

```bash
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

```
