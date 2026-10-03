# MovieLens Data Analysis with Pandas

This project is a hands-on practice notebook for learning **Pandas** with the MovieLens dataset. It follows the trainer's Kaggle notebook as a learning reference and includes examples for loading, inspecting, cleaning, analysing, filtering, visualising, grouping, and merging data.

## 1. About Kaggle

[Kaggle](https://www.kaggle.com/) is an online platform for data science and machine learning. It provides datasets, notebooks, learning resources, and competitions where learners can practise with real data.

### Who uses Kaggle?

- **Students and beginners** learning Python, data analysis, and machine learning.
- **Data analysts and data scientists** exploring datasets and testing ideas.
- **Machine learning practitioners** preparing data and building models.
- **Researchers and teams** sharing notebooks and collaborating.

### Uses and benefits

- Find real-world datasets for practice and projects.
- Learn by reading and running public notebooks.
- Practise data loading, cleaning, analysis, and visualisation.
- Compare different approaches and learn from the community.
- Build a portfolio of data projects and take part in competitions.

## 2. Dataset and learning reference

This notebook uses the **MovieLens 20M Dataset** with Pandas.

- **Dataset:** [MovieLens 20M Dataset on Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)
- **Trainer's notebook:** [Pandas With Data Science.AI](https://www.kaggle.com/code/harunshimanto/pandas-with-data-science-ai)

The notebook is a practice version inspired by the trainer's workflow; it is not intended to be a verbatim copy.

## 3. Project files

Make sure your project folder has this structure:

```text
project-folder/
├── README.md
├── kaggle_pandas_workshop_polished.ipynb
└── Datasets/
    ├── movie.csv
    ├── rating.csv
    └── tag.csv
```

If you rename the notebook, use its actual filename in the instructions above. The notebook currently reads the CSV files from a folder named `Datasets` beside the notebook.

## 4. Download and prepare the dataset

1. Open the [MovieLens 20M Dataset page](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset).
2. Sign in to Kaggle if prompted.
3. Select **Download** and extract the ZIP file.
4. Create a folder named `Datasets` in the same directory as the notebook.
5. Copy `movie.csv`, `rating.csv`, and `tag.csv` into the `Datasets` folder.

All three CSV files are required by the current notebook because it loads the movies, ratings, and tags datasets near the beginning.

## 5. Requirements

Install these Python libraries if they are not already available in your environment:

```bash
pip install pandas matplotlib jupyter
```

The notebook uses:

- **Pandas** to load and analyse tabular data.
- **Matplotlib** to create charts.
- **Jupyter Notebook or JupyterLab** to run the notebook interactively.

## 6. Topics covered

1. **Load datasets** — use `pd.read_csv()` to load the movie, rating, and tag CSV files.
2. **Inspect data** — check `shape`, `columns`, `head()`, `index`, and selected rows with `iloc`.
3. **Descriptive statistics** — practise `describe()`, `mean()`, `min()`, `max()`, `std()`, `mode()`, and `corr()`.
4. **Handle missing values** — identify missing data with `isnull()` and remove incomplete tag rows with `dropna()`.
5. **Visualise data** — create a histogram and a box plot for movie ratings.
6. **Select columns and inspect values** — select one or multiple columns and count tag values with `value_counts()`.
7. **Filter rows** — use Boolean conditions to select high ratings and movies matching a genre.
8. **Group and aggregate** — use `groupby()` with counting and average calculations.
9. **Merge DataFrames** — combine movie details and tags using `merge()` and the shared `movieId` column.
10. **Combine operations** — calculate average ratings, merge them with movie details, and filter results by rating and genre.

## 7. How to run the notebook

1. Open the project folder in Jupyter Notebook or JupyterLab.
2. Confirm that all three CSV files are inside `Datasets`.
3. Open `kaggle_pandas_workshop_polished.ipynb` (or the notebook's current filename).
4. Run the cells from top to bottom.
5. Read each output before moving to the next cell.
6. Try changing values or conditions and run the cell again to understand how the output changes.
7. Add your own observations in Markdown cells.

## 8. Key takeaways

After completing this practice, you should have hands-on experience with loading CSV files, inspecting DataFrames, calculating descriptive statistics, handling missing values, creating basic plots, filtering rows, grouping records, and merging related datasets.

**Note:** Run the notebook from top to bottom in a fresh kernel to verify that the dataset paths and outputs work in your environment.
