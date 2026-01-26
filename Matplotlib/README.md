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
# Histogram Chart :
A histogram shows how data is distributed by counting how many values fall into ranges (bins).This is used for continues numerical data.
<br>
<b>Important Points to Remember :</b>

```bash
Bins = groups/ranges

Height of bar = frequency (count)

No gap between bars

Used for numerical data

```

Syntax:

```bash
plt.hist(data, bins=5)
plt.show()

```

Example :

```bash
#Syntax:
#plt.hist(data,bins=value,color="color_name",edgecolor="color_name")
# bins means how many groups/ranges divide data
# In this example bins are 6 means it divide marks in 6 groups

import matplotlib.pyplot as plt

Marks = [50,45,67,30,22,89,58,85,75,67,56,57,48,90,46,89,66,88,99]

plt.hist(Marks,bins=6,color="purple",edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()



# here
# height of bars means number of Students

```

# Scatter Plot :
A scatter plot shows the relationship between two numerical variables using dots.
<br>
In Simple words Each dot represents one data point.
<br>
It helps to find the trends, relationship,outliners.
<br>

Syntax:

```bash
plt.scatter(x,y,color="color_name",marker="marker_style",label= "label name",s=value of size of dots)
```
<br>

Example :

```bash
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5]   # study hours
marks = [40, 50, 60, 70, 80]  # marks

plt.scatter(study_hours,marks,color="blue",marker="o",label="Student Data")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.grid(True)
plt.show()

```
# What does multiple datasets mean?
Plot more than one set of data on the same graph or same figure.
<br>
Example:
<br>
Sales vs Profit
<br>

Boys vs Girls marks
<br>

Model-1 vs Model-2 accuracy
<br>

Advertisement budget vs Profit or Sales
<br>

Temperature vs ice-cream sales
<br>

Example:

```bash
# Example Using Multiple Scatter Datasets

import matplotlib.pyplot as plt

study_hours= [1,2,3,4,5,6,7,8]
section_A_Marks =[80,75,78,90,88,76,87,95]
section_B_Marks = [55,66,56,45,55,60,65,59]

plt.scatter(study_hours,section_A_Marks,color="blue",label="Section A")
plt.scatter(study_hours,section_B_Marks,color="orange",label="Section B")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Comparison of Two Section A and B")
plt.legend()
plt.grid(True)
plt.show()

```

# Subplots and Layout Adjustments and (Essential subplots function in Matplotlib):
<b>What is subplots ? </b>
<br>
Subplots allow you to display multiple plots (charts) inside a single figure.
<br>
In Simple words we can say that One window, many graphs.

<b>Why do we need subplots? (Essential Purpose)</b>

```bash

Subplots are used when you want to:

Compare multiple datasets side-by-side

Show different views of the same data

Organize plots neatly in one figure

Instead of opening multiple windows, everything appears in one figure.

```
<br>

Syntax:

```bash
fig, ax = plt.subplots(nrows, ncols,figsize=(width,height))

# figsize is optional

```
Example:

```bash

import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,2,figsize = (10,5))

x =[1,2,3,4,5]
y= [10,20,30,40,50]

ax[0].plot(x,y)
ax[0].set_title("Line chart")

ax[1].bar(x,y)
ax[1].set_title("Bar chart")

plt.tight_layout()
plt.show()

```
<b>tight_layout()</b>
<br>
tight_layout() automatically adjusts spacing between subplots so labels, titles, and ticks dont overlap.
<br>
It is used in code just before show()
<br>

syntax:

```bash
plt.tight_layout()
```
<br>

Example :

```bash
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,2,figsize = (10,5))

x =[1,2,3,4,5]
y= [10,20,30,40,50]

ax[0].plot(x,y,color="blue")
ax[0].set_title("Line chart")

ax[1].bar(x,y,color="green")
ax[1].set_title("Bar chart")

# this is used for set the title for figure(window)
fig.suptitle("Comparison of Line Chart and Bar Chart")

# this is used for fixes the labels and title of charts
plt.tight_layout()
plt.show()

```
<br>

# savefig() Function :
savefig() is used to save a Matplotlib figure as an image file.
<br>
In simple word It stores the graph on your computer.
<br>
Always call savefig() before show()
<br>

syntax:

```bash
plt.savefig(
    "plot.png",
    dpi=300,
    bbox_inches='tight',
    transparent=False
)


# dpi(dot per image) -> image quality
# bbox_inches="tight" -> Removes extra white space
# transparent ->  Transparent background
# format -> File format (png, jpg, pdf)

```
<br>

Example:

```bash
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)
plt.savefig("line_plot.png", dpi= 300, bbox_inches='tight')
plt.show()

```




