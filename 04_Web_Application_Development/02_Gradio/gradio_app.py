"""Sales & Profit Visual Explorer built with Gradio.

Run:
    python -m pip install gradio pandas matplotlib
    python gradio_app.py

Choose a chart in the browser to view the selected Matplotlib visualization.
"""
import gradio as gr
import matplotlib.pyplot as plt
import pandas as pd

# Sample sales and profit data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [10000, 12000, 15000, 13000, 17000, 16000],
    "Profit": [2000, 3000, 4000, 2500, 3500, 3000],
}

df = pd.DataFrame(data)


# Generate the selected chart
def generate_plot(plot_type):
    fig, ax = plt.subplots(figsize=(8, 5))

    if plot_type == "Line Plot":
        ax.plot(df["Month"], df["Sales"], color="blue", marker="o", label="Sales")
        ax.set_title("Sales Trend Over Months")
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")
        ax.grid(True)
        ax.legend()

    elif plot_type == "Stacked Bar Chart":
        ax.bar(df["Month"], df["Sales"], width=0.5, label="Sales", color="skyblue")
        ax.bar(
            df["Month"],
            df["Profit"],
            width=0.5,
            label="Profit",
            color="orange",
            bottom=df["Sales"],
        )
        ax.set_title("Sales and Profit Comparison by Month")
        ax.set_xlabel("Month")
        ax.set_ylabel("Amount")
        ax.legend()

    elif plot_type == "Pie Chart":
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(
            df["Profit"],
            labels=df["Month"],
            autopct="%1.1f%%",
            startangle=140,
        )
        ax.set_title("Profit Distribution by Month")

    elif plot_type == "Scatter Plot":
        ax.scatter(
            df["Sales"],
            df["Profit"],
            color="green",
            s=100,
            edgecolors="black",
        )
        ax.set_title("Sales vs Profit")
        ax.set_xlabel("Sales")
        ax.set_ylabel("Profit")
        ax.grid(True)

    elif plot_type == "Histogram":
        ax.hist(df["Sales"], bins=5, color="purple", edgecolor="black")
        ax.set_title("Sales Distribution")
        ax.set_xlabel("Sales")
        ax.set_ylabel("Frequency")

    elif plot_type == "Box Plot":
        ax.boxplot(df["Profit"], vert=False, patch_artist=True)
        ax.set_title("Profit Distribution")
        ax.set_xlabel("Profit")

    else:
        ax.text(0.5, 0.5, "Choose a chart type.", ha="center", va="center")
        ax.axis("off")

    fig.tight_layout()
    return fig


demo = gr.Interface(
    fn=generate_plot,
    inputs=gr.Radio(
        [
            "Line Plot",
            "Stacked Bar Chart",
            "Pie Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
        ],
        label="Choose Plot Type",
        value="Line Plot",
    ),
    outputs=gr.Plot(label="Visualization"),
    title="Sales & Profit Visual Explorer",
    description="Choose a chart type to visualize the sample monthly sales and profit data.",
)

if __name__ == "__main__":
    demo.launch()
