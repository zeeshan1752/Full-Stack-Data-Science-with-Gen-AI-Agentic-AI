# Import Matplotlib and NumPy
import matplotlib.pyplot as plt
import numpy as np


# Basic Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.show()


# Plotting a Single List
plt.plot([10, 20, 30, 40, 50])
plt.show()


# Plot Format String
plt.plot(x, y, "ro--")
plt.show()


# Multiple Lines
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()


# Figure
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.show()


# Current Figure and Axes
plt.plot(x, y)

print(plt.gcf())
print(plt.gca())

plt.show()


# Subplots
fig, ax = plt.subplots(2, 2, figsize=(8, 6))

ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)
ax[1, 0].bar(x, y)
ax[1, 1].plot(x, np.array(y) ** 2)

plt.show()


# Using subplot()
plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.scatter(x, y)

plt.subplot(2, 2, 3)
plt.bar(x, y)

plt.subplot(2, 2, 4)
plt.plot(x, np.array(y) ** 2)

plt.show()


# X and Y Labels
plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


# Title
plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Plot")

plt.show()


# Legend
sales = [10, 20, 30, 40, 50]
profit = [5, 15, 20, 30, 35]

plt.plot(x, sales, label="Sales")
plt.plot(x, profit, label="Profit")

plt.legend()
plt.show()


# Legend Location
plt.plot(x, sales, label="Sales")
plt.plot(x, profit, label="Profit")

plt.legend(loc="upper left")
plt.show()


# Grid
plt.plot(x, y)

plt.grid()
plt.show()


# X and Y Limits
plt.plot(x, y)

plt.xlim(1, 5)
plt.ylim(0, 60)

plt.show()


# axis()
plt.plot(x, y)

plt.axis([1, 5, 0, 60])

plt.show()


# X and Y Ticks
plt.plot(x, y)

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([10, 20, 30, 40, 50])

plt.show()


# Custom Tick Labels
months = ["Jan", "Feb", "Mar", "Apr", "May"]

plt.plot(months, sales)

plt.xticks(rotation=45)

plt.show()


# Colours
plt.plot(x, y, color="red")
plt.show()


# Line Styles
plt.plot(x, y, linestyle="-")
plt.plot(x, np.array(y) + 5, linestyle="--")
plt.plot(x, np.array(y) + 10, linestyle="-.")
plt.plot(x, np.array(y) + 15, linestyle=":")

plt.show()


# Markers
plt.plot(x, y, marker="o", ms=8)
plt.show()


# Combining Colour, Line Style and Marker
plt.plot(
    x,
    y,
    color="red",
    linestyle="--",
    marker="o",
    ms=8
)

plt.show()


# Matplotlib Styles
print(plt.style.available)


# Applying a Matplotlib Style
plt.style.use("ggplot")

plt.plot(x, y)
plt.show()


# Line Plot
plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")

plt.show()


# Scatter Plot
plt.scatter(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")

plt.show()


# Histogram
marks = [45, 50, 55, 60, 62, 65, 70, 72, 75, 80, 85, 90]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")

plt.show()


# Bar Chart
subjects = ["Maths", "Python", "SQL", "Java"]
marks = [80, 90, 75, 85]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject Marks")

plt.show()


# Horizontal Bar Chart
plt.barh(subjects, marks)

plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Subject Marks")

plt.show()


# Stacked Bar Chart
part1 = [10, 20, 30]
part2 = [5, 10, 15]

categories = ["A", "B", "C"]

plt.bar(categories, part1, label="Part 1")
plt.bar(categories, part2, bottom=part1, label="Part 2")

plt.legend()
plt.show()


# Error Bar Chart
error = [1, 2, 1, 3, 2]

plt.errorbar(x, y, yerr=error, fmt="o-")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Error Bar Chart")

plt.show()


# Pie Chart
values = [35, 25, 20, 20]
labels = ["Python", "Java", "SQL", "C++"]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Programming Languages")

plt.show()


# Box Plot
data = np.random.randn(100)

plt.boxplot(data)

plt.title("Box Plot")

plt.show()


# Area Chart
x_area = np.arange(1, 6)
y_area = np.array([1, 4, 6, 8, 4])

plt.fill_between(x_area, y_area)
plt.plot(x_area, y_area)

plt.title("Area Chart")

plt.show()


# Stack Plot
x_stack = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [5, 10, 15, 20]

plt.stackplot(x_stack, y1, y2)

plt.show()


# Contour Plot
matrix = np.random.rand(10, 20)

plt.contour(matrix)

plt.title("Contour Plot")

plt.show()


# NumPy with Matplotlib
x = np.arange(1, 11)
y = x ** 2

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("X²")
plt.title("Square of Numbers")
plt.grid()

plt.show()


# Sine and Cosine
x = np.linspace(0, 10, 50)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")

plt.legend()
plt.grid()

plt.show()


# Practical IPL Example
seasons = np.array([2019, 2020, 2021, 2022, 2023, 2024])

player1 = np.array([450, 500, 550, 480, 600, 650])
player2 = np.array([400, 450, 500, 520, 580, 620])

plt.figure(figsize=(8, 5))

plt.plot(
    seasons,
    player1,
    linestyle="-.",
    marker="d",
    ms=7,
    label="Player 1"
)

plt.plot(
    seasons,
    player2,
    linestyle="--",
    marker="o",
    ms=7,
    label="Player 2"
)

plt.xlabel("Season")
plt.ylabel("Runs")
plt.title("Player Performance Across Seasons")

plt.legend()
plt.grid()

plt.show()


# Saving a Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.savefig("line_plot.png")

plt.show()


# Saving a High-Quality Plot
plt.figure(figsize=(8, 5))

plt.plot(x, y)

plt.savefig(
    "line_plot_high_quality.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Complete Plot
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