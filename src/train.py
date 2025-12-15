import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from src.data_validation import validate_data
from src.feature_engineering import add_features
from src.preprocessing import get_preprocessor
from src.model import get_model

DATA_PATH = "data/raw/Churn_Modelling.csv"
MODEL_PATH = "artifacts/model.pkl"

def train():
    df = pd.read_csv(DATA_PATH)
    validate_data(df)

    df = add_features(df)

    X = df.drop(columns=['Exited', 'RowNumber', 'CustomerId', 'Surname'])
    y = df['Exited']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ('preprocessor', get_preprocessor()),
        ('model', get_model())
    ])

    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, MODEL_PATH)

    print("✅ Model trained and saved successfully")

if __name__ == "__main__":
    train()
