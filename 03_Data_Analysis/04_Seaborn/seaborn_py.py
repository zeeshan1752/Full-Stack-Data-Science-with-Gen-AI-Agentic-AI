# Seaborn: Data Visualization Practice
# Run this file from the project folder. Charts will be saved in the images/ folder.

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up folders and chart style
BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
sns.set_palette(["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"])
plt.rcParams["figure.figsize"] = (8, 5)

# Create a small example dataset so this script runs without an external file
df = pd.DataFrame({
    "Student": ["Amina", "Bilal", "Chen", "Diya", "Ethan", "Farah",
                "Gopal", "Hana", "Imran", "Jia", "Kabir", "Lina"],
    "StudyHours": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
    "Score": [42, 48, 51, 55, 59, 62, 67, 70, 74, 78, 84, 91],
    "Department": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C", "B", "A"],
    "Attendance": [60, 65, 70, 72, 75, 78, 80, 82, 85, 88, 92, 96],
    "ProjectScore": [45, 50, 53, 58, 61, 65, 68, 73, 76, 80, 86, 94],
})

print("Example dataset:")
print(df.head())
print("\\nDataset shape:", df.shape)
print("\\nMissing values:")
print(df.isna().sum())


def save_plot(filename):
    """Save the current Matplotlib figure and close it."""
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()


# 1. Histogram with KDE: inspect a numeric distribution
sns.histplot(data=df, x="Score", bins=6, kde=True, color="#4C72B0")
plt.title("Distribution of Student Scores")
plt.xlabel("Score")
plt.ylabel("Number of students")
save_plot("01_histogram_kde.png")

# 2. KDE plot: show a smoothed distribution estimate
sns.kdeplot(data=df, x="Attendance", fill=True, color="#4C72B0")
plt.title("Attendance Distribution (KDE)")
plt.xlabel("Attendance (%)")
plt.ylabel("Estimated density")
save_plot("02_kde_plot.png")

# 3. ECDF plot: show cumulative proportions
sns.ecdfplot(data=df, x="Score", color="#4C72B0")
plt.title("Cumulative Distribution of Scores")
plt.xlabel("Score")
plt.ylabel("Cumulative proportion")
save_plot("03_ecdf_plot.png")

# 4. Count plot: compare category frequencies
sns.countplot(data=df, x="Department", order=sorted(df["Department"].unique()), color="#4C72B0")
plt.title("Number of Students by Department")
plt.xlabel("Department")
plt.ylabel("Student count")
save_plot("04_count_plot.png")

# 5. Bar plot: compare mean scores across groups
sns.barplot(data=df, x="Department", y="Score", errorbar=("ci", 95), color="#4C72B0")
plt.title("Mean Score by Department")
plt.xlabel("Department")
plt.ylabel("Mean score")
save_plot("05_bar_plot.png")

# 6. Box plot: compare distributions and identify possible outliers
sns.boxplot(data=df, x="Department", y="Score", color="#4C72B0")
plt.title("Score Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Score")
save_plot("06_box_plot.png")

# 7. Violin plot: compare distribution shapes
sns.violinplot(data=df, x="Department", y="Score", inner="quartile", cut=0, color="#4C72B0")
plt.title("Score Distribution by Department (Violin Plot)")
plt.xlabel("Department")
plt.ylabel("Score")
save_plot("07_violin_plot.png")

# 8. Strip plot: show individual observations
sns.stripplot(data=df, x="Department", y="Score", jitter=0.18, alpha=0.8, color="#4C72B0")
plt.title("Individual Scores by Department")
plt.xlabel("Department")
plt.ylabel("Score")
save_plot("08_strip_plot.png")

# 9. Swarm plot: display points with reduced overlap
sns.swarmplot(data=df, x="Department", y="Score", size=6, color="#4C72B0")
plt.title("Scores by Department (Swarm Plot)")
plt.xlabel("Department")
plt.ylabel("Score")
save_plot("09_swarm_plot.png")

# 10. Scatter plot: examine two numeric variables
sns.scatterplot(data=df, x="StudyHours", y="Score", hue="Department", s=90)
plt.title("Study Hours vs Score")
plt.xlabel("Study hours")
plt.ylabel("Score")
save_plot("10_scatter_plot.png")

# 11. Regression plot: show a fitted linear trend
sns.regplot(data=df, x="StudyHours", y="Score", color="#4C72B0",
            scatter_kws={"alpha": 0.75}, line_kws={"color": "red"})
plt.title("Study Hours vs Score with Regression Line")
plt.xlabel("Study hours")
plt.ylabel("Score")
save_plot("11_regression_plot.png")

# 12. Residual plot: inspect model errors
sns.residplot(data=df, x="StudyHours", y="Score", lowess=True, color="#4C72B0")
plt.title("Residual Plot for Score")
plt.xlabel("Study hours")
plt.ylabel("Residual")
save_plot("12_residual_plot.png")

# 13. Line plot: connect observations along an ordered x-axis
line_df = df.sort_values("StudyHours")
sns.lineplot(data=line_df, x="StudyHours", y="Score", marker="o", errorbar=None, color="#4C72B0")
plt.title("Score by Study Hours")
plt.xlabel("Study hours")
plt.ylabel("Score")
save_plot("13_line_plot.png")

# 14. Joint plot: relationship plus marginal distributions
joint = sns.jointplot(data=df, x="StudyHours", y="Score", kind="reg", height=6)
joint.fig.suptitle("Study Hours and Scores", y=1.02)
joint.fig.savefig(IMAGES_DIR / "14_joint_plot.png", dpi=150, bbox_inches="tight")
plt.close(joint.fig)

# 15. Pair plot: compare several numeric columns
pair = sns.pairplot(df, vars=["StudyHours", "Score", "Attendance"], hue="Department", corner=True)
pair.fig.savefig(IMAGES_DIR / "15_pair_plot.png", dpi=150, bbox_inches="tight")
plt.close(pair.fig)

# 16. Correlation heatmap: visualize correlations between numeric columns
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Heatmap")
save_plot("16_correlation_heatmap.png")

# 17. Clustermap: group similar numeric patterns
cluster_data = df[["StudyHours", "Score", "Attendance", "ProjectScore"]]
cluster = sns.clustermap(cluster_data, standard_scale=1, cmap="vlag", figsize=(8, 6))
cluster.fig.savefig(IMAGES_DIR / "17_clustermap.png", dpi=150, bbox_inches="tight")
plt.close(cluster.fig)

# 18. Figure-level relplot: facet a relationship plot by category
rel = sns.relplot(data=df, x="StudyHours", y="Score", hue="Department",
                  col="Department", kind="scatter", height=3.2)
rel.fig.savefig(IMAGES_DIR / "18_relplot_facets.png", dpi=150, bbox_inches="tight")
plt.close(rel.fig)

# 19. Figure-level catplot: categorical plot interface
cat = sns.catplot(data=df, x="Department", y="Score", kind="box", height=4, aspect=1.3, color="#4C72B0")
cat.fig.suptitle("Scores by Department (catplot)", y=1.03)
cat.fig.savefig(IMAGES_DIR / "19_catplot.png", dpi=150, bbox_inches="tight")
plt.close(cat.fig)

# 20. Figure-level displot: distribution by category
dist = sns.displot(data=df, x="Score", hue="Department", kind="hist",
                   bins=6, element="step", height=4, aspect=1.4)
dist.fig.savefig(IMAGES_DIR / "20_displot.png", dpi=150, bbox_inches="tight")
plt.close(dist.fig)

# 21. Styling: use hue and marker style to distinguish groups
sns.set_theme(style="ticks")
sns.set_palette(["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"])
ax = sns.scatterplot(data=df, x="StudyHours", y="ProjectScore",
                     hue="Department", style="Department", s=100)
ax.set_title("Study Hours vs Project Score by Department")
ax.set_xlabel("Study hours")
ax.set_ylabel("Project score")
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
save_plot("21_styled_scatter_plot.png")

print(f"\\nFinished! Saved chart images to: {IMAGES_DIR}")
