# Streamlit

Streamlit is an open-source Python framework for building interactive web applications. It allows us to turn a Python script into a web app using familiar Python code, without needing to build the user interface with separate HTML, CSS, or JavaScript.

Streamlit is commonly used for:
- Data analysis and exploratory data analysis (EDA) dashboards
- Visualising data with charts and tables
- Demonstrating machine learning models
- Building small tools such as calculators, filters, and prediction apps
- Sharing interactive prototypes with teammates or users

This folder contains three beginner-friendly programs based on the Streamlit examples shared by our trainer and our practice files.

## Files in This Folder

| File | Topics Covered |
|---|---|
| `01_hello_streamlit.py` | App title, text, headings, and Markdown |
| `02_square_calculator.py` | Slider input, variables, exponent operator, and displaying a result |
| `03_widgets_and_balloons.py` | Sidebar, text input, slider, selectbox, DataFrame, checkbox, button, success message, and balloons |

Run one Python file at a time.

## 1. What Is Streamlit?

Streamlit is a Python framework that makes it easy to create interactive web apps from Python scripts. We write Python code, run it with Streamlit, and view the result in a browser.

For example, a normal Python program may use `print()` to show a result in the terminal. A Streamlit app can display the same result on a web page and let users change values through controls such as sliders, text boxes, and dropdown menus.

### Why use Streamlit?

- **Beginner-friendly:** We can start with Python knowledge and learn the UI functions gradually.
- **Fast development:** We can create a useful interface with a few lines of code.
- **Interactive:** Users can enter values, select options, and click buttons.
- **Data-friendly:** Streamlit works well with Pandas DataFrames, charts, and machine learning libraries.
- **Useful for projects:** We can present data analysis or model results in a browser instead of showing only terminal output.

### How a Streamlit app works

1. Write the app in a Python file ending with `.py`.
2. Import Streamlit using `import streamlit as st`.
3. Use Streamlit functions such as `st.title()` and `st.write()` to build the page.
4. Run the file using the `streamlit run filename.py` command.
5. Streamlit starts a local server and displays a local URL.
6. Open that URL in a browser to use the app.
7. When a user changes a widget, Streamlit normally reruns the script from top to bottom and refreshes the output.

## 2. Installation and Setup

Open the VS Code terminal in this folder and install the libraries used by these examples:

```bash
python -m pip install streamlit pandas numpy
```

What each library is used for:

- `streamlit` builds the web app and its interactive components.
- `pandas` creates and manages tabular data.
- `numpy` generates random numerical data for the DataFrame example.

To check the Streamlit installation:

```bash
streamlit --version
```

If the terminal says that the `streamlit` command is not recognised, check that Streamlit was installed in the Python environment you are using in VS Code.

## 3. Run a Streamlit App

Run the first example:

```bash
streamlit run 01_hello_streamlit.py
```

Run the square calculator:

```bash
streamlit run 02_square_calculator.py
```

Run the widgets example:

```bash
streamlit run 03_widgets_and_balloons.py
```

Streamlit normally prints a local URL such as `http://localhost:8501` in the terminal. Open that URL in your browser if it does not open automatically.

To stop the running app, click inside the terminal and press `Ctrl + C`.

**Important:** Use `streamlit run filename.py` for these applications. Running `python filename.py` directly will not start the normal Streamlit web interface.

## 4. Display Text and Headings

File: `01_hello_streamlit.py`

### `st.title()`

Displays the main title of the app.

```python
st.title("My First Streamlit App")
```

**What you will see:** A large heading that says `My First Streamlit App`.

### `st.write()`

Displays text, numbers, and many Python objects.

```python
st.write("Hello! Welcome to my first Streamlit application.")
```

**Output displayed in the app:**

```text
Hello! Welcome to my first Streamlit application.
```

### `st.header()` and `st.subheader()`

These functions display headings for sections of the page.

```python
st.header("About This App")
st.subheader("Result")
```

Use `st.header()` for a main section heading and `st.subheader()` for a smaller heading inside a section.

### `st.markdown()`

Displays text using Markdown formatting, such as bullet points, bold text, and links.

```python
st.markdown(
    """
    This app demonstrates:
    - Displaying a title
    - Writing text
    - Using Markdown
    """
)
```

**What you will see:** A paragraph followed by three bullet points.

### Complete example

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! Welcome to my first Streamlit application.")

st.header("About This App")
st.markdown(
    """
    This app demonstrates the basic use of Streamlit:
    - Displaying a title
    - Writing text
    - Using Markdown
    """
)
```

`import streamlit as st` imports the library and gives it the short name `st`. The remaining lines display content in the browser.

## 5. Take Input Using a Slider

File: `02_square_calculator.py`

A slider lets a user choose a value by moving a control on the page.

```python
number = st.slider("Pick a number", min_value=0, max_value=100, value=25)
```

The arguments mean:

- `"Pick a number"` is the label displayed above the slider.
- `min_value=0` is the smallest allowed value.
- `max_value=100` is the largest allowed value.
- `value=25` is the starting value.

The selected value is stored in the variable `number`.

### Example

If the user selects `5`, then the variable contains the value `5`. The user can choose a different value in the browser without editing the Python file.

## 6. Calculate the Square of a Number

The square of a number is the number multiplied by itself.

```python
squared_number = number ** 2
```

In Python, `**` is the exponentiation operator. Therefore, `number ** 2` means “number raised to the power of 2.”

### Example

```python
number = 5
squared_number = number ** 2
print(squared_number)
```

Output:

```text
25
```

This is because 5 multiplied by 5 equals 25.

The Streamlit app displays the result using:

```python
st.write(f"The square of **{number}** is **{squared_number}**.")
```

The `f` before the string makes it an f-string, so Python inserts variable values inside curly braces. The double asterisks are Markdown syntax that makes the values bold in the app.

**Example result in the app:** The square of 5 is 25.

### Complete square calculator

```python
import streamlit as st

st.title("Square Calculator")
st.write("Move the slider to select a number and calculate its square.")

number = st.slider("Pick a number", min_value=0, max_value=100, value=25)
squared_number = number ** 2

st.subheader("Result")
st.write(f"The square of **{number}** is **{squared_number}**.")
```

When the app first opens, the slider starts at 25 and the result is 625. If the user changes the slider to 5, the result changes to 25.

## 7. Add Controls to the Sidebar

File: `03_widgets_and_balloons.py`

The sidebar is a separate panel on the left side of the app. It is useful for placing input controls and filters away from the main content.

```python
st.sidebar.header("User Input Features")
user_name = st.sidebar.text_input("What is your name?", "Guest")
```

- `st.sidebar.header()` displays a heading in the sidebar.
- `st.sidebar.text_input()` creates a text box in the sidebar.
- `"Guest"` is the default text shown in the text box.
- The value entered by the user is stored in `user_name`.

If the user types `Aisha`, the variable `user_name` contains the string `"Aisha"`.

```python
st.header(f"Welcome, {user_name}!")
```

Example displayed heading:

```text
Welcome, Aisha!
```

## 8. Use a Slider in the Sidebar

```python
age = st.sidebar.slider("Select your age", min_value=0, max_value=100, value=25)
```

This creates a slider for selecting an age from 0 to 100. Its initial value is 25. The selected value is stored in `age`.

```python
st.write(f"You are {age} years old.")
```

If the user selects 22, the app displays:

```text
You are 22 years old.
```

## 9. Use a Select Box

A select box lets the user choose one option from a list.

```python
favorite_color = st.sidebar.selectbox(
    "What is your favorite color?",
    ["Blue", "Red", "Green", "Yellow"],
)
```

The first argument is the label. The list contains the available choices. The selected choice is stored in `favorite_color`.

For example, if the user selects `Green`, then `favorite_color` contains `"Green"`.

```python
st.write(f"Your favorite color is {favorite_color}.")
```

Output displayed in the app:

```text
Your favorite color is Green.
```

## 10. Create and Display a DataFrame

A DataFrame is a two-dimensional table with rows and columns. Pandas provides `DataFrame()` to create one.

In this example, NumPy generates random numbers and Pandas puts them into a table.

```python
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=[f"Column {i}" for i in range(1, 6)],
)
```

### How this code works

- `np.random.randn(10, 5)` generates an array with 10 rows and 5 columns of random numbers.
- `pd.DataFrame(...)` converts the array into a Pandas DataFrame.
- `[f"Column {i}" for i in range(1, 6)]` creates the column names `Column 1` through `Column 5`.
- The resulting DataFrame is stored in the variable `data`.

To display the table in the app:

```python
st.dataframe(data, use_container_width=True)
```

`st.dataframe()` displays the table in the browser. `use_container_width=True` lets it use the available page width.

**Expected shape:** 10 rows and 5 columns. The numerical values vary because they are randomly generated.

## 11. Show or Hide Data Using a Checkbox

A checkbox represents an option that can be selected or cleared.

```python
if st.checkbox("Show raw data"):
    st.write(data)
```

How it works:

1. Streamlit displays a checkbox labelled `Show raw data`.
2. If the user checks it, the condition is true and `st.write(data)` displays the DataFrame.
3. If the user clears it, the indented statement is not executed on that run.

This is useful when we want to show extra details only when the user requests them.

## 12. Use a Button, Balloons, and a Success Message

A button lets the user trigger an action.

```python
if st.button("Send balloons!"):
    st.balloons()
    st.success("Great! You clicked the button.")
```

- `st.button("Send balloons!")` displays a clickable button.
- When the button is clicked, the `if` condition is true for that run.
- `st.balloons()` displays a balloon animation.
- `st.success()` displays a success message.

The success message appears after the user clicks the button.

## 13. Full Widgets Example

The third program combines the concepts covered above:

```python
import numpy as np
import pandas as pd
import streamlit as st

st.title("Streamlit Widgets and Balloons")
st.write("Explore sidebar inputs, a sample DataFrame, and a button.")

st.sidebar.header("User Input Features")
user_name = st.sidebar.text_input("What is your name?", "Guest")
age = st.sidebar.slider("Select your age", min_value=0, max_value=100, value=25)
favorite_color = st.sidebar.selectbox(
    "What is your favorite color?",
    ["Blue", "Red", "Green", "Yellow"],
)

st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=[f"Column {i}" for i in range(1, 6)],
)
st.dataframe(data, use_container_width=True)

if st.checkbox("Show raw data"):
    st.write(data)

if st.button("Send balloons!"):
    st.balloons()
    st.success("Great! You clicked the button.")
```

When the program runs, the page shows a title, sidebar controls, a personalised welcome heading, a DataFrame, a checkbox, and a button.

## 14. Common Streamlit Functions

| Function | Purpose |
|---|---|
| `st.title()` | Displays the main title |
| `st.write()` | Displays text or Python objects |
| `st.markdown()` | Displays Markdown-formatted content |
| `st.header()` | Displays a section heading |
| `st.subheader()` | Displays a smaller heading |
| `st.slider()` | Lets the user select a value |
| `st.text_input()` | Accepts text from the user |
| `st.selectbox()` | Lets the user select one option |
| `st.sidebar` | Places elements in the sidebar |
| `st.dataframe()` | Displays tabular data |
| `st.checkbox()` | Provides a checkable option |
| `st.button()` | Creates a clickable button |
| `st.balloons()` | Displays a balloon animation |
| `st.success()` | Displays a success message |

## 15. Points to Remember

- Streamlit is a Python framework for creating interactive web apps.
- Save the app code in a `.py` file.
- Start a Streamlit app with `streamlit run filename.py`.
- `import streamlit as st` allows us to call Streamlit functions using the short name `st`.
- Functions such as `st.title()` and `st.write()` display content in the main page.
- Widgets such as sliders, text inputs, select boxes, and checkboxes let users interact with the app.
- Use `st.sidebar` to place controls in the sidebar instead of the main page.
- Use `st.dataframe()` to display tabular data in the browser.
- Streamlit generally reruns the script from top to bottom when a user interacts with a widget.
- Python indentation is important, especially for statements inside `if` blocks.
- Install the required libraries in the same Python environment used to run the app.
- Stop the app with `Ctrl + C` in the terminal.
