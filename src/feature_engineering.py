import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['CreditUtilization'] = df['Balance'] / (df['CreditScore'] + 1)
    df['BalanceToSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1)
    df['InteractionScore'] = (
        df['NumOfProducts'] +
        df['HasCrCard'] +
        df['IsActiveMember']
    )

    return df
