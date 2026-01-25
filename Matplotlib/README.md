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

# Matplotlib Object Oriented API 
The object-oriented API gives direct control over Figure and Axes objects to create flexible and scalable plots.
<br>
There are Two key object of OOA :
<br>

```bash
1. Figure => Figure means the entire canvas and windowx.It can contain multiple axes.

2. Axes => Axes means the actual ploting area where data is drawn.

# simple rule to remembers this :

figure holds Axes,Axes holds plot.

```
<br>

<b>Simple Example By Using OOA:</b>
<br>

```bash
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots(figsize=(6,4))

ax.plot(x, y, marker='o', color='blue', label='Sales')
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.legend()
ax.grid(True)

plt.show()

```

# Matplotlib Ploting Function :

```bash

from matplotlib.lines import lineStyles
# syntax: x and y is mandatory others are optional
# 1. plt.plot(x,y, color="color" ,linestyle="line_style", linewidth=value,marker="marker symbol",label="label name")

# Example:
import matplotlib.pyplot as plt

months = [1,2,3,4,5,6,7]
sales = [20000,30000,12000,4000,34000,1100,100000]

plt.plot(months,sales,color='blue',linestyle='--',linewidth=2,marker='o',label='2026 sales data')
# labeling
plt.xlabel("Months")
plt.ylabel("Sales Per Month")
# for title
plt.title("Monthly Sales Data Report")
# legend : it makes a box 
plt.legend()
# grid(color="colorname",linestyle='line_style',linewidth:value) : It draw horizontal line or vertical line on background of of graph
plt.grid(color='gray',linestyle=':',linewidth=1)

plt.show()


```

# Bar Chart in matplotlib :
A bar chart represents data using rectangular bars, where:
<br>
Height/length of bar = value
<br>
Used for comparison between categories.
<br>

Example:

```bash
# syntax:
#plt.bar(x, height, color="colorname",width=value,label="label name")
# vertical bar chart

import matplotlib.pyplot as plt

product = ['A','B','C','D','E']
sales= [1000,1500,700,1200,1100]

plt.bar(product,sales,color='orange',label='2025 sales')

plt.xlabel('Products')
plt.ylabel('Sales')

plt.title('Product Sales Comparision')

plt.legend()
plt.show()

```

# Pie Chart :
A pie chart shows how a whole (100%) is divided into parts.
Each slice represents a proportion / percentage.
<br>
In simple words A pie chart shows how a whole is divided into parts using slices of a circle.
<br>

Syntax:

```bash
plt.pie(
    data,                # values (numbers)
    labels=labels,       # names of slices
    autopct='%1.1f%%',   # show percentage
    startangle=90,       # rotate chart
    explode=explode,     # separate slice
    colors=colors        # slice colors
)
plt.show()

```

Example:

```bash

import matplotlib.pyplot as plt

regions = ['North','South',"East",'West']
revenue = [3000,2000,1500,1000]

explode = [0.1, 0, 0, 0]

plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen','coral'] , explode=explode)
plt.title("Revenue Contribution by Regions")

plt.show()

```

