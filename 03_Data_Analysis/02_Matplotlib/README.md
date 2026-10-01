# Matplotlib

Matplotlib is a Python library used for **data visualization**.

It helps us represent numerical data using different types of plots and charts.

Some commonly used plots in Matplotlib are:

- Line Plot
- Scatter Plot
- Histogram
- Bar Chart
- Horizontal Bar Chart
- Stacked Bar Chart
- Error Bar Chart
- Pie Chart
- Box Plot
- Area Chart
- Contour Plot

Matplotlib also provides many options to customise plots using:

- Colours
- Line styles
- Markers
- Titles
- Labels
- Legends
- Grids
- Axes
- Ticks
- Figure size

---


# 1. Introduction to Data Visualization

## What is Data Visualization?

**Data Visualization** means representing data using plots, charts, graphs, and other visual elements.

Instead of reading a large amount of numerical data, we can use a graph to understand the information more easily.

For example, instead of looking at:


we can represent the values using a line plot.

## Why is Data Visualization useful?

Data visualization helps us to:

* Understand data easily
* Compare values
* Find patterns
* Identify trends
* Understand relationships
* Identify unusual values
* Communicate information clearly
* Make better decisions

---

# 2. Python Data Visualization Tools

Python provides several libraries and tools for data visualization.

Some commonly used tools are:

* Matplotlib
* Seaborn
* Pandas
* Bokeh
* Plotly

---

# 3. Introduction to Matplotlib

## What is Matplotlib?

**Matplotlib** is a Python library used for creating plots and visualizations.

It can create many types of charts, including:

* Line Plot
* Scatter Plot
* Histogram
* Bar Chart
* Error Bar Chart
* Pie Chart
* Box Plot
* Area Chart
* Contour Plot

Matplotlib can also be used for image visualization and supports different output formats.

Matplotlib is also used as a foundation by other Python visualization libraries.

---

# 4. Installing and Importing Matplotlib

## Installing Matplotlib

Matplotlib can be installed using:

```python
pip install matplotlib
```

## Importing Matplotlib

We can import Matplotlib using:

```python
import matplotlib
```

Most of the time, we work with the `pyplot` module.

```python
import matplotlib.pyplot
```

The commonly used shorthand is:

```python
import matplotlib.pyplot as plt
```

We can also import NumPy when working with numerical data:

```python
import numpy as np
```

### Example

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

# 5. Displaying Plots

Matplotlib can be used in different environments:

* Python Script
* IPython
* Jupyter Notebook

---

## Plotting from a Python Script

When using Matplotlib in a Python script, we normally use:

```python
plt.show()
```

Example:

```python
import matplotlib.pyplot as plt

plt.plot([10, 20, 30, 40])

plt.show()
```

`plt.show()` displays the active figure.

---

## Plotting from IPython

Matplotlib can also be used interactively in an IPython shell.

The `%matplotlib` magic command can be used to enable Matplotlib support.

---

## Plotting from Jupyter Notebook

In Jupyter Notebook, we can use:

```python
%matplotlib inline
```

This displays static plots directly inside the notebook.

We can also use:

```python
%matplotlib notebook
```

This provides interactive plots inside the notebook.

---

### Contexts for displaying plots


```python
%matplotlib inline
x1 = np.linspace(0, 10, 50)

# create a plot figure
#fig = plt.figure()

plt.plot(x1, np.sin(x1), '-')
plt.plot(x1, np.cos(x1), '--')
#plt.plot(x1, np.tan(x1), '--')
plt.show()
```

![Output](images/html-image-01-178a4b9bf93a.png)

Matplotlib can be used in three common contexts:

- Python Script
- IPython shell
- Jupyter Notebook

When working in a Python script, `plt.show()` is normally used to display the active figure.

# 6. Matplotlib Object Hierarchy

Matplotlib follows an object hierarchy.

A plot is made up of different objects arranged in a hierarchy.

![Matplotlib Object Hierarchy](images/matplotlib-hierarchy.png)

## Figure


```python
fig = plt.figure()

ax = plt.axes()
```

![Output](images/html-image-12-ff3a1248ee57.png)

A **Figure** is the complete container or canvas.

A Figure can contain one or more Axes.

## Axes

An **Axes** is the area where the actual data is plotted.

It normally contains:

* X-axis
* Y-axis
* Data
* Labels
* Title
* Legend
* Grid

## Axis

An **Axis** represents an X-axis or Y-axis.

It controls things such as:

* Limits
* Ticks
* Tick labels

## Artists

Artists are the visual elements of a Matplotlib figure.

Examples include:

* Lines
* Text
* Markers
* Labels
* Shapes

---

# 7. Matplotlib APIs

Matplotlib provides two main interfaces:

1. Pyplot API
2. Object-Oriented API

![Matplotlib APIs](images/matplotlib-apis.png)

## Pyplot API


```python
# create the first of two panels and set current axis
plt.subplot(2, 1, 1)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1), '*')
```

![Output](images/html-image-02-4b48c0ea3171.png)

The Pyplot API provides a simple, state-based interface.

Example:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])

plt.show()
```

## Object-Oriented API

The Object-Oriented API works directly with Figure and Axes objects.

Example:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4])

plt.show()
```

---

### API overview

Matplotlib mainly provides two interfaces:

- **Pyplot API** - simple, state-based interface
- **Object-Oriented API** - works directly with Figure and Axes objects

There is also a `pylab` interface that combines pyplot and NumPy. It is generally discouraged in modern Python code, so it is better to use `matplotlib.pyplot` and `numpy` separately.

# 8. Pyplot API

`matplotlib.pyplot` provides functions for creating and controlling plots.

```python
import matplotlib.pyplot as plt
```

Some commonly used functions are:

```python
plt.plot()
plt.figure()
plt.subplot()
plt.subplots()
plt.show()
plt.gcf()
plt.gca()
```

---

## `plt.figure()`


```python
# create a plot figure
plt.figure()


# create the first of two panels and set current axis
plt.subplot(2, 1, 1)   # (rows, columns, panel number)
plt.plot(x1, np.sin(x1))

# create the second of two panels and set current axis
plt.subplot(2, 1, 2)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1));
```

![Output](images/html-image-03-4500168c28fd.png)

`plt.figure()` creates a new Figure.

```python
plt.figure()
```

Example:

```python
import matplotlib.pyplot as plt

plt.figure()

plt.plot([10, 20, 30, 40])

plt.show()
```

---

## `plt.gcf()`

`gcf` means **Get Current Figure**.

```python
plt.gcf()
```

It returns the current Figure object.

---

## `plt.gca()`


```python
# get current axis information

print(plt.gca())
```

![Output](images/html-image-04-1cf177a77997.png)

`gca` means **Get Current Axes**.

```python
plt.gca()
```

It returns the current Axes object.

---

### How Pyplot works

`matplotlib.pyplot` provides a MATLAB-style, procedural interface to Matplotlib.

Pyplot keeps track of the current Figure and current Axes. This makes it convenient for interactive plotting because we can issue a command and see the result immediately.

For simple plots, Pyplot is easy to use. For more complex plots, the Object-Oriented API gives more direct control.

# 9. Object-Oriented API

The Object-Oriented API works with Figure and Axes objects.

The common syntax is:

```python
fig, ax = plt.subplots()
```

Here:

* `fig` represents the Figure
* `ax` represents the Axes

Example:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4])

plt.show()
```

Instead of:

```python
plt.plot()
```

we can use:

```python
ax.plot()
```

The Object-Oriented approach gives more direct control over individual Axes.

---

### Why use the Object-Oriented API?

The Object-Oriented API is useful for more complex plotting situations.

Instead of depending on an active Figure or Axes, we work with explicit objects:


For multiple plots, each Axes object can be controlled separately.

# 10. Figure and Subplots

A Figure can contain one or more subplots.

![Figure and Subplots](images/subplots.png)

## Creating a Single Subplot

```python
fig, ax = plt.subplots()
```

## Creating Multiple Subplots

```python
fig, ax = plt.subplots(2, 2)
```

```python
# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)


# Call plot() method on the appropriate object
ax[0].plot(x1, np.sin(x1), 'b-')
ax[1].plot(x1, np.cos(x1), 'b-');
```

![Output](images/html-image-10-ac6b8a0b8313.png)


This creates:

```text
2 rows × 2 columns
```

Visual structure:

![Figure and Subplots](images/subplots.png)

---

## `plt.subplot()`

`plt.subplot()` can be used to create a specific subplot.

Syntax:

```python
plt.subplot(rows, columns, position)
```

Example:

```python
import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3])

plt.subplot(2, 2, 2)
plt.plot([3, 2, 1])

plt.show()
```

---

### Creating subplots using `Figure.add_subplot()`


```python
fig = plt.figure()

x2 = np.linspace(0, 5, 10)
y2 = x2 ** 2

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x2, y2, 'r')

axes.set_xlabel('x2')
axes.set_ylabel('y2')
axes.set_title('title');
```

![Output](images/html-image-11-6cf966b8edef.png)

Another way to create subplots is to first create a Figure and then add individual Axes:


`fig.add_subplot(2, 2, 1)` means:

- `2` rows
- `2` columns
- `1` = first subplot

So, `2 × 2` creates four subplot positions.

# 11. First Plot with Matplotlib


```python
plt.plot([1,2,3,4], [1,8,2,16])
plt.ylabel('Numbers')
plt.show()
```

![Output](images/html-image-05-8e17c6179090.png)

![Output](images/line-plot.png)

The most basic plotting function is:

```python
plt.plot()
```

## Plotting a Single List


```python
plt.plot([1, 3, 2, 4], 'b-')

plt.show( )
```

![Output](images/html-image-13-4a309b83e2bc.png)


When only Y values are provided, Matplotlib automatically generates X values.

For example:

```text
Y values:
10  20  30  40  50

X values:
0   1   2   3   4
```

---

## Plotting X and Y Values


```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 8, 27, 64])
plt.show()
```

![Output](images/html-image-06-d96e309b3031.png)


```python
x3 = np.arange(0.0, 6.0, 0.01) 

plt.plot(x3, [xi**2 for xi in x3], 'b-') 

plt.show()
```

![Output](images/html-image-14-59ba7bdd8fd2.png)

---

# 12. Multiline Plots


```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
```

![Output](images/html-image-07-6108b0eac937.png)

---

### Plotting multiple lines


```python
x4 = range(1, 5)

plt.plot(x4, [xi*1.5 for xi in x4])

plt.plot(x4, [xi*3 for xi in x4])

plt.plot(x4, [xi/3.0 for xi in x4])

plt.show()
```

![Output](images/html-image-15-490c3ce504f1.png)

Multiple lines can be added to the same Figure before calling `plt.show()`.


# 13. Parts of a Plot

A plot can contain different components.

```text
                Title
                  |
       +-----------------------+
       |                       |
 Y     |       Plot Area       |  Legend
 Axis  |                       |
       |                       |
       +-----------------------+
            X Axis
```

Important parts include:

* Figure
* Axes
* X-axis
* Y-axis
* Title
* Labels
* Ticks
* Legend
* Grid
* Data lines
* Markers

---

# 14. Figure Size

We can control the size of a figure using `figsize`.

```python
plt.figure(figsize=(8, 5))
```

Here:

```text
8 = width
5 = height
```

Example:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.plot([10, 20, 30, 40])

plt.show()
```

We can also set the default figure size using:

```python
plt.rcParams['figure.figsize'] = (6, 3)
```

---

# 15. Handling Axes

Matplotlib automatically determines suitable axis limits.
Sometimes, we want to set the limits ourselves.

```python
x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.axis()   # shows the current axis limits values

plt.axis([0, 5, -1, 13])

plt.show()
```

![Output](images/html-image-29-91d61bb01526.png)


```python
x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.xlim([1.0, 4.0])

plt.ylim([0.0, 12.0])
```

![Output](images/html-image-30-2d09d6fc932a.png)

---

## `plt.axis()`


```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

![Output](images/html-image-08-ee90c831fa2e.png)

---

## `plt.xlim()`

Controls the X-axis limits.

```python
plt.xlim([1, 4])
```

## `plt.ylim()`

Controls the Y-axis limits.

```python
plt.ylim([0, 12])
```

Example:

```python
plt.xlim([1, 4])
plt.ylim([0, 12])
```

---

# 16. Handling X and Y Ticks

Ticks are the small reference marks shown on the axes.

```python
u = [5, 4, 9, 7, 8, 9, 6, 5, 7, 8]

plt.plot(u)

plt.xticks([2, 4, 6, 8, 10])
plt.yticks([2, 4, 6, 8, 10])

plt.show()
```

![Output](images/html-image-31-856ca41c4362.png)

---

## Tick Labels

We can provide custom labels.

```python
seasons = ["2015", "2016", "2017", "2018"]

plt.xticks([0, 1, 2, 3], seasons)
```

---

## Tick Rotation

We can rotate tick labels.

Vertical:

```python
plt.xticks(rotation="vertical")
```

Horizontal:

```python
plt.xticks(rotation="horizontal")
```

We can also use degrees:

```python
plt.xticks(rotation=45)
```

---

# 17. Adding Labels

Labels explain what the X-axis and Y-axis represent.

```python
plt.plot([1, 3, 2, 4])

plt.xlabel('This is the X axis')

plt.ylabel('This is the Y axis')

plt.show()
```

![Output](images/html-image-32-61aa4b575e93.png)

---

# 18. Adding a Title

A title describes the plot.
The title appears at the top of the plot.

```python
plt.plot([1, 3, 2, 4])

plt.title('First Plot')

plt.show()
```

![Output](images/html-image-33-234738ba0ef6.png)

---

# 19. Adding a Legend

A legend explains what each line or dataset represents.

```python
x15 = np.arange(1, 5)

fig, ax = plt.subplots()

ax.plot(x15, x15*1.5)
ax.plot(x15, x15*3.0)
ax.plot(x15, x15/3.0)

ax.legend(['Normal','Fast','Slow']);
```

![Output](images/html-image-34-fee08e8bd64e.png)


```python
x15 = np.arange(1, 5)

fig, ax = plt.subplots()

ax.plot(x15, x15*1.5, label='Normal')
ax.plot(x15, x15*3.0, label='Fast')
ax.plot(x15, x15/3.0, label='Slow')

ax.legend();
```

![Output](images/html-image-35-6ae216beadc2.png)

![Output](images/legend.png)

---

## Legend Location

We can control the position using `loc`.

```python
plt.legend(loc="upper left")
```

Common locations include:

```python
plt.legend(loc="upper right")
plt.legend(loc="upper left")
plt.legend(loc="lower left")
plt.legend(loc="lower right")
```

We can also use numerical location codes:

```python
plt.legend(loc=0)
plt.legend(loc=1)
plt.legend(loc=2)
plt.legend(loc=3)
plt.legend(loc=4)
```

---

### Legend using the `label` parameter

A good approach is to give each line a `label` while plotting and then call `legend()`.


This keeps the legend connected to the plotted data and is easier to maintain when lines are added or removed.

The `loc` parameter controls the legend position. Common values include:


# 20. Adding a Grid

A grid provides a reference system that makes values easier to read.

```python
x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.grid(True)

plt.show()
```

![Output](images/html-image-28-6e6fbd599fe5.png)

![Output](images/grid.png)

---

# 21. Controlling Colours

We can give different colours to different lines.

```python
x16 = np.arange(1, 5)

plt.plot(x16, 'r')
plt.plot(x16+1, 'g')
plt.plot(x16+2, 'b')

plt.show()
```

![Output](images/html-image-36-4b232a3f920b.png)

Common colour abbreviations:

| Abbreviation | Colour  |
| ------------ | ------- |
| `b`          | Blue    |
| `c`          | Cyan    |
| `g`          | Green   |
| `k`          | Black   |
| `r`          | Red     |
| `m`          | Magenta |
| `y`          | Yellow  |

We can also use the full colour name:


Other ways of specifying colours include:

* Full colour names
* Hexadecimal values
* RGB tuples
* Grayscale values

Example:

```python
plt.plot(x, color="#FF00FF")
```

---

# 22. Controlling Line Styles


```python
x16 = np.arange(1, 5)

plt.plot(x16, '--', x16+1, '-.', x16+2, ':')

plt.show()
```

![Output](images/html-image-37-4b232a3f920b.png)

![Output](images/line-styles.png)

Matplotlib provides different line styles.

| Symbol | Line Style |
| ------ | ---------- |
| `-`    | Solid      |
| `--`   | Dashed     |
| `-.`   | Dash-dot   |
| `:`    | Dotted     |

---

# 23. Markers

![Output](images/markers.png)

Markers show individual data points on a plot.

Example:

```python
plt.plot(x, y, marker="o")
```

Some common markers are:

| Marker | Meaning  |
| ------ | -------- |
| `o`    | Circle   |
| `s`    | Square   |
| `^`    | Triangle |
| `*`    | Star     |
| `+`    | Plus     |
| `x`    | X        |
| `d`    | Diamond  |

Example:

```python
plt.plot(
    x,
    y,
    marker="o"
)
```

---

## Marker Size

Marker size can be controlled using `ms`.

```python
plt.plot(
    x,
    y,
    marker="o",
    ms=10
)
```

---

# 24. Matplotlib Styles

Matplotlib provides predefined styles.

To see available styles:

```python
plt.style.available
```

Example:

```python
print(plt.style.available)
```

To apply a style:

```python
plt.style.use("style-name")
```

For example:

```python
plt.style.use("ggplot")
```

After applying a style, the plots created afterwards use that style.

> **Note:** Some older Matplotlib notebooks may contain style names that are no longer available in newer Matplotlib versions. Check `plt.style.available` before using a style.

---

# 25. Line Plot

A line plot is used to show trends or changes in data.

```python
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

![Output](images/html-image-09-38be155669bb.png)


```python
# Create figure and axes first
fig = plt.figure()

ax = plt.axes()

# Declare a variable x5
x5 = np.linspace(0, 10, 1000)


# Plot the sinusoid function
ax.plot(x5, np.sin(x5), 'b-');
```

![Output](images/html-image-17-424e9f45f8f5.png)

![Output](images/line-plot.png)

---

# 26. Scatter Plot

A scatter plot represents data using individual points.

```python
x7 = np.linspace(0, 10, 30)

y7 = np.sin(x7)

plt.plot(x7, y7, 'o', color = 'black');
```

![Output](images/html-image-18-215eebceb6d9.png)

![Output](images/scatter-plot.png)

Scatter plots are useful for understanding the relationship between two variables.

---

# 27. Histogram

A histogram shows the distribution of numerical data.

```python
data1 = np.random.randn(1000)

plt.hist(data1);
```

![Output](images/html-image-19-f9b9629de6c9.png)

![Output](images/histogram.png)

---

## Bins

Bins divide the data into intervals.

Example:

```python
plt.hist(marks, bins=5)
```

---

# 28. Bar Chart

A bar chart is useful for comparing values across categories.

```python
data2 = [5. , 25. , 50. , 20.]

plt.bar(range(len(data2)), data2)

plt.show()
```

![Output](images/html-image-20-650f41ec952e.png)

![Output](images/bar-chart.png)

---

# 29. Horizontal Bar Chart

```python
data2 = [5. , 25. , 50. , 20.]

plt.barh(range(len(data2)), data2)

plt.show()
```

![Output](images/html-image-21-d34242a2566f.png)

![Output](images/horizontal-bar-chart.png)

---

# 30. Stacked Bar Chart

A stacked bar chart places one dataset on top of another.

The `bottom` parameter is used for stacking.

```python
A = [15., 30., 45., 22.]

B = [15., 25., 50., 20.]

z2 = range(4)

plt.bar(z2, A, color = 'b')
plt.bar(z2, B, color = 'r', bottom = A)

plt.show()
```

![Output](images/html-image-23-313b4cff22df.png)

![Output](images/stacked-bar-chart.png)

The second set of bars starts from the values of the first set.

---

# 31. Error Bar Chart

An error bar chart shows values together with error or uncertainty.

```python
x9 = np.arange(0, 4, 0.2)

y9 = np.exp(-x9)

e1 = 0.1 * np.abs(np.random.randn(len(y9)))

plt.errorbar(x9, y9, yerr = e1, fmt = '.-')

plt.show();
```

![Output](images/html-image-22-7b4679b58cf5.png)

![Output](images/error-bar-chart.png)

---

# 32. Pie Chart

A pie chart represents data as sectors of a circle.

The sectors are also called **wedges**.

The size of each sector represents its proportion of the whole.

```python
plt.figure(figsize=(7,7))

x10 = [35, 25, 20, 20]

labels = ['Computer', 'Electronics', 'Mechanical', 'Chemical']

plt.pie(x10, labels=labels);

plt.show()
```

![Output](images/html-image-24-140ba0b6933c.png)

![Output](images/pie-chart.png)

---

# 33. Box Plot

A box plot is used to understand the distribution of data.
It can show:

* Median
* Quartiles
* Minimum
* Maximum
* Outliers

```python
data3 = np.random.randn(100)

plt.boxplot(data3)

plt.show();
```

![Output](images/html-image-25-8fd11a6a6c47.png)

![Output](images/box-plot.png)

---

### Understanding the box plot

A box plot gives a compact view of the distribution.

It can show:

- Median
- Lower and upper quartiles
- Whiskers
- Outliers

The interquartile range (IQR) is the distance between the lower quartile and upper quartile. In a standard box plot, points beyond the whisker range can be shown as outliers.

# 34. Area Chart

An Area Chart is similar to a Line Chart.

The area between the X-axis and the line is filled.

```python
# Create some data
x12 = range(1, 6)
y12 = [1, 4, 6, 8, 4]

# Area plot
plt.fill_between(x12, y12)
plt.show()
```

![Output](images/html-image-26-4ffae094b8fe.png)

![Output](images/area-chart.png)

## `fill_between()`

Example:

```python
import matplotlib.pyplot as plt

x = range(1, 6)
y = [1, 4, 6, 8, 4]

plt.fill_between(x, y)

plt.show()
```

---

## `stackplot()`

We can also create an area chart using:

```python
plt.stackplot(x, y)
```

Example:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [5, 10, 15, 20]

plt.stackplot(x, y1, y2)

plt.show()
```

---

# 35. Contour Plot

A contour plot is useful for representing three-dimensional data in two dimensions.

Contour lines are also called:

* Level lines
* Isolines
```python
# Create a matrix
matrix1 = np.random.rand(10, 20)

cp = plt.contour(matrix1)

plt.show()
```

![Output](images/html-image-27-7ab583cd0d44.png)

![Output](images/contour-plot.png)

The `contour()` function takes a 2D array as input.

---

## Contour Levels

The number of contour levels can also be specified.

```python
plt.contour(matrix, 10)
```

Here, `10` represents the number of levels.

---

### Understanding contour lines

Contour lines are also called level lines or isolines.

They connect points having the same value. Contour plots are useful when a two-dimensional view is needed for data that depends on two variables.

When contour lines are close together, the value changes more rapidly over that area.

---

# 36. Displaying Images with Matplotlib

Matplotlib can also be used to display images.

For image handling, we can use the **Pillow** library.

## Installing Pillow

```python
pip install pillow
```

## Importing Pillow

```python
from PIL import Image
```

## Opening an Image

```python
image = Image.open("image.jpg")
```

We can check the type:

```python
type(image)
```

---

## Converting Image to NumPy Array

We can convert the image into a NumPy array:

```python
image_arr = np.array(image)
```

We can check its shape:

```python
image_arr.shape
```

---

## Displaying the Image

Use:

```python
plt.imshow(image_arr)
plt.show()
```

Complete example:

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("image.jpg")

image_arr = np.array(image)

plt.imshow(image_arr)

plt.show()
```
---

# 37. Working with NumPy

![Output](images/sine-cosine.png)

NumPy arrays can be directly used with Matplotlib.

Example:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

plt.plot(x, y)

plt.show()
```

NumPy can also be used to generate data.

Example:

```python
x = np.arange(1, 11)
y = x ** 2

plt.plot(x, y)

plt.show()
```

Another example:

```python
x = np.linspace(0, 10, 50)

plt.plot(x, np.sin(x), "-")
plt.plot(x, np.cos(x), "--")

plt.show()
```
---

# 38. Practical IPL Data Analysis

![Output](images/ipl-analysis.png)

Matplotlib can be used with real-world numerical data.

In the practical example, IPL data is used to compare player information across different seasons.

The data includes:

* Seasons
* Players
* Salary
* Games

Example seasons:

```python
Seasons = [
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024"
]
```

A dictionary can be used to map seasons to positions:

```python
Sdict = {
    "2015": 0,
    "2016": 1,
    "2017": 2,
    "2018": 3,
    "2019": 4,
    "2020": 5,
    "2021": 6,
    "2022": 7,
    "2023": 8,
    "2024": 9
}
```


---

## Plotting Player Data

Example:

```python
import matplotlib.pyplot as plt

plt.plot(
    Salary[0],
    ls="-.",
    c="black",
    marker="d",
    ms=7
)

plt.plot(
    Salary[1],
    ls="--",
    c="red",
    marker="o",
    ms=7
)

plt.show()
```

---

## Adding Season Names

Instead of showing numerical positions on the X-axis, we can display the actual seasons.

```python
plt.xticks(
    list(range(0, 10)),
    Seasons
)
```

We can also rotate the labels:

```python
plt.xticks(
    list(range(0, 10)),
    Seasons,
    rotation="vertical"
)
```
---

## Adding Player Names

We can use the `label` parameter.

```python
plt.plot(
    Salary[0],
    ls="-.",
    c="black",
    marker="d",
    ms=7,
    label=Players[0]
)

plt.plot(
    Salary[1],
    ls="--",
    c="red",
    marker="o",
    ms=7,
    label=Players[1]
)

plt.legend()

plt.show()
```

This demonstrates how Matplotlib can be used to compare multiple datasets and customise the final visualization.

---

# 39. Saving Plots

Matplotlib provides:

```python
plt.savefig()
```
to save a plot as an image file.

```python
# Explore the contents of figure

from IPython.display import Image

Image('plot1.png')
```

![Output](images/html-image-16-28be1eff0f54.png)

We can save using different file extensions.

---

# 40. Complete Plot Example

The following example combines several concepts:

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 150, 130, 180, 220]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    color="blue",
    linestyle="-",
    marker="o",
    ms=8,
    label="Sales"
)

plt.xlabel("Month")
plt.ylabel("Sales")

plt.title("Monthly Sales")

plt.xticks(rotation=45)

plt.grid()
plt.legend()

plt.show()
```

This example uses:

* Figure size
* Line plot
* Colour
* Line style
* Marker
* Marker size
* X-axis label
* Y-axis label
* Title
* Tick rotation
* Grid
* Legend


---

# 41. Plot Selection Guide

| Plot           | Function               | Main Purpose                    |
| -------------- | ---------------------- | ------------------------------- |
| Line Plot      | `plt.plot()`           | Show trends                     |
| Scatter Plot   | `plt.scatter()`        | Show relationships              |
| Histogram      | `plt.hist()`           | Show distribution               |
| Bar Chart      | `plt.bar()`            | Compare categories              |
| Horizontal Bar | `plt.barh()`           | Compare categories horizontally |
| Stacked Bar    | `plt.bar()` + `bottom` | Compare parts of a whole        |
| Error Bar      | `plt.errorbar()`       | Show error or uncertainty       |
| Pie Chart      | `plt.pie()`            | Show parts of a whole           |
| Box Plot       | `plt.boxplot()`        | Show distribution and outliers  |
| Area Chart     | `fill_between()`       | Show values using filled areas  |
| Stack Plot     | `stackplot()`          | Show stacked areas              |
| Contour Plot   | `plt.contour()`        | Represent 2D/3D-related data    |

---

# 42. Summary

Matplotlib is an important Python library for data visualization.

In this guide, we learned:

* Data Visualization
* Matplotlib basics
* Installing Matplotlib
* Importing Matplotlib
* Displaying plots
* Matplotlib object hierarchy
* Pyplot API
* Object-Oriented API
* Figure and Axes
* Subplots
* Basic plotting
* Multiline plots
* Parts of a plot
* Figure size
* Axis limits
* X and Y ticks
* Labels
* Titles
* Legends
* Grid
* Colours
* Line styles
* Markers
* Matplotlib styles
* Line plots
* Scatter plots
* Histograms
* Bar charts
* Horizontal bar charts
* Stacked bar charts
* Error bar charts
* Pie charts
* Box plots
* Area charts
* Contour plots
* Image visualization
* NumPy with Matplotlib
* Practical IPL data analysis
* Saving plots

Matplotlib gives us the tools to convert numerical data into clear and meaningful visualizations.
