# Notebook Guide

## Environment

Use Python 3.12 or newer. From the repository root, create and activate a virtual environment, install the pinned direct dependencies, and start JupyterLab:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install numpy==2.5.3 pandas==3.0.6 matplotlib==3.11.2 openpyxl==3.1.5 Pillow==12.3.0 jupyterlab==4.6.3 ipykernel==7.4.0
jupyter lab
```

Open a notebook from the Jupyter file browser. Run it from top to bottom with a fresh kernel. Data-reading notebooks look for the included workbook relative to either the repository root or the notebook folder.

## Reproducibility conventions

- Dependency installation belongs in the setup instructions, not in notebook code cells.
- Examples use fixed sample values so “Run All” does not pause for interactive input.
- Cells that teach invalid operations catch and print the expected exception instead of saving a traceback.
- Clear stale outputs after changing source; keep outputs only when they still match the code.
- Use repository-relative paths and record the source and license for data and images in the relevant notebook or lesson README.

These notebooks are learning exercises, not portfolio case studies. Use separate, finished project repositories to demonstrate end-to-end work to hiring reviewers.
