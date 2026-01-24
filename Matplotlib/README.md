# Data Visualization :
Data Visualization means representing data in graphical or visual form so that humans can easily understand patterns, trends, and insights.
<br>
Instead of reading numbers in a table, you see the story through:
<br>
Charts
<br>
Graphs
<br>
Plots
<br>
Dashboards
<br>

<b>Why Data visualization is important :</b>

```bash
1. Understand Data Quickly

Spot trends

Find patterns

Detect outliers

2. Better Decision Making

Businesses decide strategy

Developers improve performance

ML engineers evaluate models

3. Communicate Insights

Present to clients

Explain results to non-technical people

```
<br>

<b> some common types of charts that is used for data visualization :</b>
    
```bash
1. Line Chart
Used for trends over time
Example: stock prices, accuracy vs epochs

2. Bar Chart
Used for comparison
Example: sales of different products

3. Scatter Plot
Used for relationships
Example: height vs weight

 4. Histogram
Used for data distribution
Example: exam scores

5. Pie Chart
Used for proportions
Example: market share

```

# What is Matplotlib :
Matplotlib is a python library that is used for data visualize using chats and graphs.
<br>
Matplotlib was created by <b>John D. hunter</b>. He was a American neurobiologist and the original author of Matplotlib.
<br>
Here are the meaning of name Matplotlib:
<br>
mat = MATLAB , plot = Ploting and lib = Library
<br>

<b>Why it is important :</b>

```bash
Data Analysis

Machine Learning

Research & Reports

Interviews + Projects
```
<b> Command to install Matplotlib :</b>

```bash

pip install Matplotlib

// if you use google collab

!pip install Matplotlib

```
<br>

# Matplotlib Terms You Should Know :

```bash
1. Data Point => It refers to a single pair of value in a datasets that is called data point.

Example:

x = [1,2,3,4,5]
y = [10,20,30,40,50]

(1,10) is a data point


2. x-axis and y-axis => x-axis is used for input like time , days etc and y-axis is used for output like showing sales etc.

3. Figure => The whole window / canvas where everything is drawn.Yoy think it like a blank paper.

plt.figure()

4. Axes  => The actual plotting area (where graph appears).

fig, ax = plt.subplots()

5. plot  => Drawing data on axes (line, bar, etc.)

plt.plot(x, y)


6. show => Displays the figure.

plt.show()

7. marker => A marker is the shape used to represent a data point on a plot.
Every dot, circle, star, or square you see on a graph = marker

Exmaple :

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.show()


8. line style => Line style controls how the line looks (solid, dashed, dotted).
example:
plt.plot(x, y, linestyle='--')

9. color  => Color controls the line or marker color.
example:
plt.plot(x, y, color='green')

10. legend =>  Legend explains which line belongs to which data.
Example:
plt.plot(x, y, label="Sales")
plt.plot(x, y2, label="Profit")
plt.legend()


11. A label describes what the data represents.
There are two types of labels:
Axis labels (X-axis & Y-axis)
Plot labels (used in legend)

Example:
# axis label 
plt.xlabel("Time")
plt.ylabel("Sales")

# plot label 
plt.plot(x, y, label="Sales Data")
plt.legend()

12. A title is the heading of the graph that explains the overall meaning of the plot.
eample:
plt.title("Monthly Sales Report")

13. grid =>The grid() function adds grid lines to a plot to make values easier to read.
syntax:
plt.grid()


14. function =>A function is a block of code that performs a specific task and is not tied to any object.
example:
def add(a, b):
    return a + b

print(add(2, 3))

15. method =>A method is a function that belongs to an object or class.
Syntax:
object.method()

Example:
text = "hello"
print(text.upper())  # upper() is method 


16. parameter =>A parameter is a variable in a function or method definition that receives a value when the function is called.

Example :

def greet(name):
    print("Hello", name)

greet("Nitish")

# name is a parameter
# Nitish is an argument


```

#  Understanding pyplot :

<b>what is pyplot :</b>
<br>
pyplot is a module in Matplotlib that provides a simple, MATLAB-like interface for creating plots.
<br>

```bash

import matplotlib.pyplot as plt

# plt is just an alias(short name)

```
<br>

<b>What does pyplot actually do?</b>

```bash
Creates figures

Manages axes

Keeps track of the current plot

Draws and displays graphs

Think of pyplot as a manager that remembers:

"Which figure and axes am I working on right now?"

```
<br>

<b>How pyplot Works (Behind the Scenes) :</b>

```bash

When you write:

plt.plot(x, y)


# Internally:

1. pyplot checks -> Is there a figure?

2. If not -> Create one

3. Checks -> Is there an axes?

4. If not -> Create axes

5. Plots data on the current axes

```

<b>Common pyplot Functions :</b>

```bash

Function	     purpose
plt.figure()	Create a new figure
plt.plot()	    Line plot
plt.scatter()	 Scatter plot
plt.bar()	     Bar chart
plt.hist()	     Histogram
plt.title()	     Title
plt.xlabel()	X-label
plt.ylabel()	Y-label
plt.legend()	Legend
plt.grid()	    Grid
plt.show()	    Display plot

```