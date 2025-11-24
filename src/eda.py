"""Perform EDA: descriptive statistics, outlier detection, segmentation summary, and save outputs."""
import argparse
from pathlib import Path
import pandas as pd
import json

from src.utils import ensure_dataframe, descriptive_stats, flag_outliers_zscore
from src.plots import plot_income_histogram, plot_age_spending_scatter, plot_box_by_segment

def main():
    parser = argparse.ArgumentParser(description='Run EDA on synthetic customer data')
    parser.add_argument('--input', type=str, default='data/synthetic_customers_v1.csv', help='input CSV path')
    parser.add_argument('--outdir', type=str, default='reports', help='output directory for reports/plots')
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = ensure_dataframe(args.input)

    numeric_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

    # Compute descriptive statistics
    stats = descriptive_stats(df, numeric_cols)
    stats_path = outdir / 'descriptive_stats.json'
    stats.to_json(stats_path, orient='index')
    print(f"Saved descriptive statistics to {stats_path}")

    # Outlier detection
    outlier_mask = flag_outliers_zscore(df, numeric_cols)
    outliers = df[outlier_mask]
    outliers_path = outdir / 'outliers_sample.csv'
    outliers.to_csv(outliers_path, index=False)
    print(f"Saved {len(outliers)} outlier rows to {outliers_path}")

    # Segment analysis: mean spending score per segment
    seg = df.groupby('Customer Segment')['Spending Score (1-100)'].mean().round(2)
    seg_path = outdir / 'segment_mean_spending.json'
    seg.to_json(seg_path)
    print(f"Saved segment mean spending to {seg_path}")

    # Plots
    plot_income_histogram(df, outdir / 'income_hist.png')
    plot_age_spending_scatter(df, outdir / 'age_spending_scatter.png')
    plot_box_by_segment(df, outdir / 'spending_box_by_segment.png')
    print(f"Saved plots to {outdir}")

if __name__ == '__main__':
    main()
