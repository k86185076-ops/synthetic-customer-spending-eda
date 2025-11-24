"""Plotting utilities: create and save charts used in the EDA."""
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set(style='whitegrid')

def plot_income_histogram(df, outpath):
    outpath = Path(outpath)
    plt.figure(figsize=(8,5))
    sns.histplot(df['Annual Income (k$)'], bins=20, kde=False)
    plt.title('Distribution of Annual Income (k$)')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Count')
    plt.tight_layout()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()

def plot_age_spending_scatter(df, outpath):
    outpath = Path(outpath)
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        data=df,
        x='Age',
        y='Spending Score (1-100)',
        hue='Customer Segment',
        palette='colorblind',
        alpha=0.75
    )
    plt.title('Age vs Spending Score (colored by Customer Segment)')
    plt.xlabel('Age')
    plt.ylabel('Spending Score (1-100)')
    plt.legend(title='Segment')
    plt.tight_layout()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()

def plot_box_by_segment(df, outpath):
    outpath = Path(outpath)
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x='Customer Segment', y='Spending Score (1-100)')
    plt.title('Spending Score Distribution by Customer Segment')
    plt.tight_layout()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
