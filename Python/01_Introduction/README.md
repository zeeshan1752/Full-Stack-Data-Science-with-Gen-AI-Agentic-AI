# Python Introduction

## What is Python?

Python is a **high-level, interpreted, and general-purpose programming language**.

It is one of the most popular programming languages because its syntax is simple, readable, and easy to understand. Python is beginner-friendly and is widely used in many areas of technology.

Python is commonly used in:

* Data Science
* Machine Learning
* Artificial Intelligence (AI)
* Web Development
* Data Analysis
* Automation and Scripting
* Cyber Security
* Cloud Computing
* Desktop Applications
* Game Development

### Simple Example

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

The `print()` function is used to display something on the screen.

---

# History of Python

Python was created by **Guido van Rossum**, a Dutch programmer.

He started working on Python in the late 1980s, and Python was first released in **1991**.

Guido van Rossum is commonly known as the **Father of Python**.

The name **Python** was inspired by the British comedy show **Monty Python's Flying Circus**, not by the snake.

---

# Why is Python Popular?

Python is popular because:

* It is easy to learn.
* Its syntax is simple and readable.
* We can write programs using fewer lines of code.
* It has a large number of libraries and frameworks.
* It is used in many different fields.
* It has a large developer community.
* A lot of tutorials and documentation are available.
* It is widely used in Data Science, AI, and Machine Learning.

---

# Features of Python

## 1. Simple and Easy to Learn

Python has simple syntax, so beginners can understand and write programs easily.

```python
name = "Zeeshan"
print(name)
```

---

## 2. Easy to Read and Write

Python code is generally easy to read because its syntax is close to normal English in many places.

---

## 3. High-Level Language

Python is a **high-level programming language**.

It hides many low-level details such as direct memory management, allowing programmers to focus more on solving problems.

---

## 4. Interpreted Language

Python is commonly described as an **interpreted language** because Python programs are executed by the Python interpreter.

For example:

```python
print("Hello")
print("Python")
```

The Python interpreter processes the code and produces the output.

> Note: Internally, Python implementations such as CPython first compile Python source code into bytecode and then execute that bytecode. For beginners, it is enough to understand that the Python interpreter executes our Python program.

---

## 5. Open Source

Python is **open-source software**.

Its source code is publicly available, and Python can be used without paying for a license.

---

## 6. Platform Independent

Python can run on different operating systems such as:

* Windows
* Linux
* macOS

A Python program can usually be run on different platforms with little or no modification.

---

## 7. Object-Oriented

Python supports **Object-Oriented Programming (OOP)**.

It provides concepts such as:

* Class
* Object
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction

---

## 8. Dynamically Typed

Python is a **dynamically typed language**.

We do not need to specify the data type while creating a variable.

```python
age = 21
name = "Zeeshan"
```

Python automatically identifies the type of the values.

---

## 9. Large Standard Library

Python provides a large collection of built-in modules and libraries.

For example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

## 10. Huge Community Support

Python has a very large developer community.

We can easily find documentation, tutorials, examples, and solutions to common problems.

---

# Applications of Python

## 1. Data Science

Python is widely used for collecting, cleaning, analysing, and visualising data.

Popular libraries include:

* NumPy
* Pandas
* Matplotlib
* Seaborn

---

## 2. Machine Learning

Python is one of the most commonly used languages for Machine Learning.

Popular libraries include:

* Scikit-learn
* TensorFlow
* PyTorch

---

## 3. Artificial Intelligence

Python is widely used for:

* Natural Language Processing
* Computer Vision
* Generative AI
* Chatbots
* Recommendation Systems

---

## 4. Web Development

Python can be used to create websites and web applications.

Popular frameworks include:

* Django
* Flask
* FastAPI

---

## 5. Automation and Scripting

Python can automate repetitive tasks such as:

* Renaming files
* Reading files
* Working with folders
* Sending emails
* Generating reports
* Processing data

---

## 6. Data Analysis

Python is used to analyse data and find useful information from it.

For example:

* Student data
* Sales data
* Customer data
* Financial data

---

## 7. Cyber Security

Python can be used for:

* Automation
* Network analysis
* Security testing
* Log analysis
* Security scripts

---

## 8. Cloud Computing

Python is also used for cloud automation, APIs, DevOps tasks, and cloud-based applications.

---

# Python Interpreter

A **Python interpreter** is a program that executes Python code.

For example, when we write:

```python
print("Hello Python")
```

the Python interpreter processes the code and produces:

```text
Hello Python
```

After installing Python, we can normally start the interpreter using:

```bash
python
```

On some systems, we may use:

```bash
python3
```

---

# Python File Extensions

While learning Python, we commonly work with two file extensions:

* `.py`
* `.ipynb`

---

# `.py` File

`.py` is the file extension used for a **Python source code file**.

Example:

```text
hello.py
```

A `.py` file contains Python code that can be executed using the Python interpreter.

Example:

```python
name = "Zeeshan"
print(name)
```

We can run it using:

```bash
python hello.py
```

### `.py` files are commonly used for:

* Python programs
* Scripts
* Automation
* Projects
* Modules
* Applications

---

# `.ipynb` File

`.ipynb` stands for **IPython Notebook**.

It is mainly used with **Jupyter Notebook** and **JupyterLab**.

An `.ipynb` file allows us to write and execute code in separate **cells**.

Example:

### Cell 1

```python
name = "Zeeshan"
```

### Cell 2

```python
print(name)
```

Output:

```text
Zeeshan
```

An `.ipynb` file can contain:

* Python code
* Output
* Text
* Markdown
* Images
* Tables
* Graphs
* Mathematical equations

`.ipynb` files are very commonly used in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Data Analysis

---

# Difference Between `.py` and `.ipynb`

| `.py`                                                  | `.ipynb`                                      |
| ------------------------------------------------------ | --------------------------------------------- |
| Python source code file                                | IPython Notebook file                         |
| Mainly used for programs and scripts                   | Mainly used for interactive work              |
| Code is written in a normal file                       | Code is divided into cells                    |
| Output is normally displayed after running the program | Output can be displayed directly below a cell |
| Common in software projects                            | Common in Data Science and ML                 |
| Run using the Python interpreter                       | Usually used with Jupyter Notebook/JupyterLab |

### Simple Understanding

```text
.py     → Python Program

.ipynb  → Interactive Python Notebook
```

---

# IDE

IDE stands for **Integrated Development Environment**.

An IDE is software that provides different tools required for writing, running, testing, and debugging programs in one place.

---

# Features of an IDE

### Code Editor

Used to write programming code.

### Syntax Highlighting

Makes different parts of the code easier to identify and read.

### Auto Completion

Suggests functions, variables, keywords, and other code while typing.

### Debugging

Helps find and fix errors in a program.

### Integrated Terminal

Allows us to run commands without opening a separate terminal.

### Project Management

Helps manage multiple files and folders in a project.

### Extension Support

Allows us to add extra features according to our requirements.

---

# Popular Python IDEs and Code Editors

Some commonly used tools are:

* Visual Studio Code (VS Code)
* PyCharm
* Jupyter Notebook
* JupyterLab
* Spyder
* IDLE

### Simple Understanding

* **VS Code** → Code editor with extension support
* **PyCharm** → Full-featured Python IDE
* **Jupyter Notebook** → Interactive notebook environment
* **JupyterLab** → Advanced notebook environment
* **Spyder** → IDE mainly used for scientific computing and Data Science
* **IDLE** → Basic Python development environment

---

# Python Installation

For beginners using Windows, Python can be installed from the **official Python website**; it can also be installed through other options such as the Microsoft Store or Windows package managers.

## Steps to Install Python

### Step 1: Open the Official Website

Go to:

https://www.python.org/

### Step 2: Go to Downloads

Click on **Downloads** and select the latest stable Python version available for Windows.

### Step 3: Download the Installer

Download the Windows installer.

### Step 4: Open the Installer

Open the downloaded `.exe` installer.

### Step 5: Add Python to PATH

On the first installation screen, make sure this option is checked:

```text
Add python.exe to PATH
```

This is important because it allows us to run Python commands from Command Prompt or Terminal.

### Step 6: Install Python

Click:

```text
Install Now
```

Wait for the installation to complete.

### Step 7: Verify Installation

Open **Command Prompt** and run:

```bash
python --version
```

Example:

```text
Python 3.x.x
```

We can also check using:

```bash
py --version
```

---

# Python Installation – Important Beginner Points

### Python PATH

PATH allows Windows to find the Python executable when we type commands such as:

```bash
python
```

If Python was not added to PATH during installation, the `python` command may not work directly from Command Prompt.

### Python Launcher

Windows may provide the Python Launcher, which can be checked using:

```bash
py --version
```

### Python Version

Always check the installed version using:

```bash
python --version
```

or:

```bash
py --version
```

---

# VS Code Installation

VS Code stands for **Visual Studio Code**.

It is a lightweight and popular code editor used for Python and many other programming languages.

For Python development, VS Code is useful because we can install extensions and customise it according to our requirements.

## Steps to Install VS Code

### Step 1: Open the Official Website

Go to:

https://code.visualstudio.com/

### Step 2: Download VS Code

Click **Download for Windows**.

### Step 3: Open the Installer

Open the downloaded setup file.

### Step 4: Accept the License

Read and accept the license agreement.

### Step 5: Select Installation Options

Follow the setup instructions and select the required options.

### Step 6: Install VS Code

Click **Install** and wait for the installation to complete.

### Step 7: Open VS Code

After installation, open VS Code from the Start Menu or desktop shortcut.

---

# VS Code Extensions for Python

VS Code provides an **Extensions** section where we can install additional features.

Open:

```text
VS Code → Extensions
```

Search for the required extension and install it.

## 1. Python

Provides Python support such as running Python files, debugging, code completion, testing, and interpreter selection.

## 2. Pylance

Provides fast Python language support, IntelliSense, type checking, and better code analysis.

## 3. Python Environment Manager / Python Environment

Helps manage and select different Python environments used by projects.

## 4. Office Viewer

Allows us to view common Office documents such as Word, Excel, and PowerPoint files inside VS Code.

## 5. Jupyter

Provides support for `.ipynb` Jupyter Notebook files inside VS Code.

## 6. Cline

An AI coding assistant that can help with coding, understanding code, debugging, and development tasks.

## 7. Code Runner

Allows us to quickly run code from different programming languages directly inside VS Code.

## 8. AREPL for Python

Provides real-time Python code evaluation, allowing us to see results while editing Python code.

## 9. autoDocstring

Helps generate Python docstrings for functions and classes.

## 10. CodeSnap

Allows us to take clean screenshots of selected code.

## 11. PDF Viewer

Allows PDF files to be opened and viewed directly inside VS Code.

## 12. Markdown PDF

Allows Markdown files to be converted into PDF documents.

## 13. Python Extension Pack

A collection of useful Python-related extensions that can provide a ready-made Python development setup.

> **Note:** You do not need to install every extension. Install the extensions that are useful for your work. For basic Python and Jupyter practice, **Python, Pylance, and Jupyter** are the most important ones.

---

# Jupyter Support in VS Code

If we want to work with `.ipynb` files in VS Code, install the:

```text
Jupyter
```

extension.

After installation, we can create a notebook such as:

```text
practice.ipynb
```

and execute Python code cell by cell.

---

# Selecting Python Interpreter in VS Code

If multiple Python versions or environments are installed, VS Code needs to know which Python environment should be used.

We can select it using:

```text
Command Palette → Python: Select Interpreter
```

or by clicking the Python interpreter/environment shown in VS Code.

For beginners, select the Python installation that we want to use for the current project.

---

# Anaconda Installation

**Anaconda** is a Python distribution mainly used for:

* Data Science
* Machine Learning
* Artificial Intelligence
* Scientific Computing

It comes with Python and provides tools and packages that are useful for Data Science.

Anaconda can be downloaded from the official website, and it can also be installed using supported package-management options.

## Steps to Install Anaconda

### Step 1: Open the Official Website

Go to:

https://www.anaconda.com/

### Step 2: Go to Download

Open the download section and select the installer for your operating system.

### Step 3: Download the Installer

Download the Anaconda installer.

### Step 4: Open the Installer

Open the downloaded installer.

### Step 5: Follow the Setup

Follow the installation instructions and select the required installation options.

### Step 6: Complete Installation

Click **Install** and wait for the installation to finish.

### Step 7: Open Anaconda Navigator

After installation, search for:

```text
Anaconda Navigator
```

in the Windows Start Menu.

From Anaconda Navigator, we can launch applications such as:

* Jupyter Notebook
* JupyterLab
* Spyder

---

# Anaconda Prompt

Anaconda also provides **Anaconda Prompt**.

It is a command-line tool where we can run Python and Conda commands.

For example:

```bash
python --version
```

and:

```bash
conda --version
```

---

# Anaconda Navigator

Anaconda Navigator provides a graphical interface for managing and launching Data Science tools.

It can be useful for beginners because we can launch applications without using many terminal commands.

Common applications include:

* Jupyter Notebook
* JupyterLab
* Spyder

---

# pip

`pip` is a package installer for Python.

It is used to install Python packages and libraries.

Example:

```bash
python -m pip install pandas
```

Another example:

```bash
python -m pip install numpy
```

### Important

`pip` is a tool for installing Python packages. It is not a programming language.

---

# Python Package

A Python package is a collection of reusable Python code that provides additional functionality.

For example, we can install packages such as:

```bash
python -m pip install numpy pandas matplotlib
```

These packages are commonly used in Data Science.

---

# Python REPL

Python provides an interactive environment called the **REPL**.

REPL stands for:

**Read-Eval-Print Loop**

We can start it by typing:

```bash
python
```

Example:

```python
>>> 10 + 20
30
```

Another example:

```python
>>> print("Hello")
Hello
```

REPL is useful for quickly testing small pieces of Python code.

To exit:

```python
exit()
```

---

# First Python Program

Let's write our first Python program:

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

---

# Printing Different Values

## Printing Text

```python
print("Python")
```

Output:

```text
Python
```

## Printing Numbers

```python
print(10)
```

Output:

```text
10
```

## Printing Multiple Values

```python
print("My age is", 21)
```

Output:

```text
My age is 21
```

## Performing a Calculation

```python
print(10 + 20)
```

Output:

```text
30
```

---

# Comments in Python

Comments are notes written inside the program to explain the code.

Python ignores comments during execution.

A single-line comment starts with `#`.

```python
# This is my first Python program

print("Hello Python")
```

Comments are useful for making code easier to understand.

---

# Python is Case-Sensitive

Python is **case-sensitive**.

This means uppercase and lowercase letters are treated differently.

For example:

```python
name = "Zeeshan"
```

and:

```python
Name = "Zeeshan"
```

are two different variables.

Similarly:

```python
print("Hello")
```

is correct, while:

```python
Print("Hello")
```

is different and will not work as the `print()` function.

---

# Python Indentation

Python uses **indentation** to define blocks of code.

Example:

```python
if 10 > 5:
    print("10 is greater than 5")
```

The spaces before `print()` are important.

Python normally uses **4 spaces** for one level of indentation.

---

# Variables – Basic Introduction

A variable is a name used to refer to a value.

Example:

```python
name = "Zeeshan"
age = 21
```

Here:

```text
name → variable
"Zeeshan" → value

age → variable
21 → value
```

We can print the variables:

```python
print(name)
print(age)
```

Output:

```text
Zeeshan
21
```

Variables will be covered in more detail in the **Variables and Data Types** topic.

---

# Running a Python File

Suppose we create:

```text
hello.py
```

and write:

```python
print("Hello Python")
```

Open the terminal in the same folder and run:

```bash
python hello.py
```

Output:

```text
Hello Python
```

---

# Running Python in VS Code

### Steps

1. Open VS Code.
2. Open your Python practice folder.
3. Create a file named:

```text
hello.py
```

4. Write:

```python
print("Hello Python")
```

5. Save the file using:

```text
Ctrl + S
```

6. Click **Run Python File**.

The output will appear in the terminal.

---

# Basic Python Terms

## Program

A set of instructions given to a computer to perform a task.

## Source Code

The code written by a programmer.

Example:

```python
print("Hello")
```

## Syntax

The rules used to write code correctly.

## Error

A problem in a program that prevents it from working correctly or producing the expected result.

## Variable

A name used to refer to a value.

## Value

The actual data stored or used by a program.

Example:

```python
age = 21
```

Here:

```text
age → variable
21 → value
```

## Function

A reusable block of code that performs a particular task.

Example:

```python
print("Hello")
```

Here, `print()` is a built-in Python function.

## Library

A collection of reusable code that provides functionality to programmers.

## Package

A collection of Python modules and related files that can be installed and used in a project.

---

# Common Beginner Mistakes

## 1. Python Command Not Recognised

If you get an error such as:

```text
'python' is not recognized as an internal or external command
```

Python may not be installed correctly or may not have been added to PATH.

Try:

```bash
py --version
```

If it also doesn't work, check the Python installation.

---

## 2. Forgetting to Save the File

Before running a modified program, make sure the file is saved.

Shortcut:

```text
Ctrl + S
```

---

## 3. Wrong File Extension

Make sure the file is actually:

```text
hello.py
```

and not:

```text
hello.py.txt
```

In Windows File Explorer, enable **File name extensions** to check the actual extension.

---

## 4. Incorrect Indentation

Incorrect:

```python
if 10 > 5:
print("Hello")
```

Correct:

```python
if 10 > 5:
    print("Hello")
```

---

## 5. Case-Sensitivity Mistake

Incorrect:

```python
Print("Hello")
```

Correct:

```python
print("Hello")
```

# Practice

## 1. Print Your Name

```python
print("Zeeshan Jamshed")
```

## 2. Print Your College

```python
print("Integral University")
```

## 3. Print Your Course

```python
print("Full Stack Data Science with Gen AI & Agentic AI")
```

## 4. Print Multiple Lines

```python
print("My name is Zeeshan")
print("I am a B.Tech CSE student")
print("I am learning Python")
```

## 5. Print Numbers

```python
print(10)
print(20)
print(30)
```

## 6. Perform Calculations

```python
print(10 + 20)
print(50 - 20)
print(5 * 4)
print(20 / 5)
```

## 7. Print Text and Numbers

```python
print("My age is", 21)
```

---

# My First Python Practice

```python
# My first Python practice

print("Hello, World!")

print("My name is Zeeshan Jamshed")

print("I am a B.Tech CSE student")

print("I am learning Python")

print("I am learning Full Stack Data Science with Gen AI & Agentic AI")
```

---

# Summary

In this topic, I learned:

* What Python is
* History of Python
* Father of Python
* Why Python is popular
* Features of Python
* Applications of Python
* Python interpreter
* Python 3
* `.py` file extension
* `.ipynb` file extension
* Full form of IPYNB – IPython Notebook
* Difference between `.py` and `.ipynb`
* IDE
* Features of an IDE
* Popular Python IDEs and code editors
* Python installation
* Adding Python to PATH
* Checking Python version
* VS Code installation
* VS Code extensions
* Python extension
* Pylance
* Python Environment
* Office Viewer
* Jupyter
* Cline
* Code Runner
* AREPL for Python
* autoDocstring
* CodeSnap
* PDF Viewer
* Markdown PDF
* Python Extension Pack
* Anaconda installation
* Anaconda Navigator
* Anaconda Prompt
* `pip`
* Python packages
* Python REPL
* Running a `.py` file
* Running Python in VS Code
* Selecting Python interpreter
* Comments
* Case sensitivity
* Indentation
* Variables – basic introduction
* Common beginner mistakes
* Basic Python terminology

---
