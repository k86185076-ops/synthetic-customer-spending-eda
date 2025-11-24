"""Utility functions for EDA project."""
from pathlib import Path
import pandas as pd
import numpy as np

def ensure_dataframe(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

def descriptive_stats(df, cols):
    stats = df[cols].agg(['mean','median','std','min','max']).T
    stats = stats.rename(columns={'std':'std_dev'})
    return stats

def flag_outliers_zscore(df, cols, threshold=3.0):
    """Return boolean series marking rows with any z-score magnitude > threshold for given cols."""
    from scipy.stats import zscore
    zs = df[cols].apply(lambda col: zscore(col.fillna(col.mean())))
    mask = (zs.abs() > threshold).any(axis=1)
    return mask
