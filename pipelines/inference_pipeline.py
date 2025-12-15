import joblib
import pandas as pd
from src.feature_engineering import add_features

MODEL_PATH = "artifacts/model.pkl"

class ChurnPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])
        df = add_features(df)
        prob = self.model.predict_proba(df)[0][1]
        return prob
