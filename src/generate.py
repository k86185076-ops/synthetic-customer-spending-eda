"""Generate synthetic customer spending dataset.

Usage:
    python src/generate.py --n 500 --out data/synthetic_customers_v1.csv --seed 42
"""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

def generate_synthetic(n=500, seed=42):
    """Generate a reproducible synthetic dataset.

    Columns:
    - Customer ID (int)
    - Age (int)
    - Annual Income (k$) (int)
    - Spending Score (1-100) (int)
    - Customer Segment (Low/Medium/High) (str)
    """
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 71, size=n)  # 18-70
    income = rng.integers(15, 151, size=n)  # 15k$ - 150k$
    spending = rng.integers(1, 101, size=n)  # 1-100
    # Create segments with some dependence on income & spending (for realism)
    segments = []
    for inc, sp in zip(income, spending):
        if inc >= 100 and sp >= 60:
            segments.append('High')
        elif inc <= 40 and sp <= 40:
            segments.append('Low')
        else:
            segments.append('Medium')

    df = pd.DataFrame({
        'Customer ID': range(1, n+1),
        'Age': age.astype(int),
        'Annual Income (k$)': income.astype(int),
        'Spending Score (1-100)': spending.astype(int),
        'Customer Segment': segments
    })
    return df

def main():
    parser = argparse.ArgumentParser(description='Generate synthetic customer data')
    parser.add_argument('--n', type=int, default=500, help='number of records')
    parser.add_argument('--out', type=str, default='data/synthetic_customers_v1.csv', help='output CSV path')
    parser.add_argument('--seed', type=int, default=42, help='random seed')
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = generate_synthetic(n=args.n, seed=args.seed)
    df.to_csv(out_path, index=False)
    print(f"Saved synthetic dataset with {len(df)} rows to {out_path}")

if __name__ == '__main__':
    main()
