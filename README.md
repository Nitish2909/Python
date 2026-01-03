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

