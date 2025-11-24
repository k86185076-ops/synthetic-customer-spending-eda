import pandas as pd
from src.generate import generate_synthetic

def test_generate_length_and_cols():
    df = generate_synthetic(n=200, seed=123)
    assert len(df) == 200
    expected_cols = {'Customer ID','Age','Annual Income (k$)','Spending Score (1-100)','Customer Segment'}
    assert set(df.columns) == expected_cols

def test_ranges():
    df = generate_synthetic(n=1000, seed=1)
    assert df['Age'].between(18,70).all()
    assert df['Annual Income (k$)'].between(15,150).all()
    assert df['Spending Score (1-100)'].between(1,100).all()
