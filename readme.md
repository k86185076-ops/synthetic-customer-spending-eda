# Exploratory Analysis of Synthetic Customer Spending Data

**Project overview**
This repository contains a complete, reproducible data science project that generates a synthetic customer spending dataset
and performs exploratory data analysis (EDA) using Python (NumPy, Pandas, Matplotlib, Seaborn).
The project includes scripts to:
- generate a synthetic dataset (`src/generate.py`)
- compute descriptive statistics & detect outliers (`src/eda.py`)
- create and save visualizations (`src/plots.py`)
- utility functions and simple unit tests

**Structure**
```
exploratory_customer_spending_project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/                  # generated dataset will be saved here
├── reports/               # plots and summary outputs saved here
├── src/
│   ├── generate.py
│   ├── eda.py
│   ├── plots.py
│   └── utils.py
├── tests/
│   └── test_generate.py
└── Makefile
```

**Quickstart**
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
2. Generate the dataset:
   ```bash
   python src/generate.py --n 500 --out data/synthetic_customers_v1.csv
   ```
3. Run EDA and save outputs:
   ```bash
   python src/eda.py --input data/synthetic_customers_v1.csv --outdir reports/
   ```
4. Run tests:
   ```bash
   pytest -q
   ```

**Reproducibility**
- The random seed is set by default (`seed=42`) and can be changed via CLI arguments.
- Generated data is saved to `data/` and plots/summaries to `reports/`.
