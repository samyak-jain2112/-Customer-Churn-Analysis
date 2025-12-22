from pipelines.churn_intelligence_pipeline import ChurnIntelligencePipeline

pipeline = ChurnIntelligencePipeline()

result = pipeline.run({
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
})

print("\n--- RESULT ---\n")
print(result)
