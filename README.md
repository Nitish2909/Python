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

