# test_inference.py
from pipelines.inference_pipeline import ChurnPredictor

predictor = ChurnPredictor()
print(predictor.predict_proba({
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Male",
    "Age": 40,
    "Tenure": 3,
    "Balance": 50000,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 0,
    "EstimatedSalary": 60000
}))
