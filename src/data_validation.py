import pandas as pd

REQUIRED_COLUMNS = [
    'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
    'Balance', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'EstimatedSalary', 'Exited'
]

def validate_data(df: pd.DataFrame):
    missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    if df.isnull().sum().any():
        raise ValueError("Dataset contains missing values")

    return True
