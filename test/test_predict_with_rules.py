from pipelines.inference_pipeline import ChurnPredictor
from src.explainability.rule_explainer import RuleExplainer

predictor = ChurnPredictor()
rule_explainer = RuleExplainer()

customer = {
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Male",
    "Age": 50,
    "Tenure": 2,
    "Balance": 120000,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 0,
    "EstimatedSalary": 70000
}

prob = predictor.predict_proba(customer)
rules = rule_explainer.generate_rules(customer)

print("Churn Probability:", prob)
print("Reasons:")
for r in rules:
    print("-", r)
