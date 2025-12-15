import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import streamlit as st
from pipelines.inference_pipeline import ChurnPredictor

st.set_page_config(page_title="Customer Churn Predictor")

st.title("Customer Churn Prediction System")

predictor = ChurnPredictor()

with st.form("customer_form"):
    CreditScore = st.number_input("Credit Score", 300, 900)
    Geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", 18, 100)
    Tenure = st.number_input("Tenure", 0, 10)
    Balance = st.number_input("Balance", 0.0)
    NumOfProducts = st.number_input("Number of Products", 1, 4)
    HasCrCard = st.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.selectbox("Is Active Member", [0, 1])
    EstimatedSalary = st.number_input("Estimated Salary", 0.0)

    submit = st.form_submit_button("Predict")

if submit:
    input_data = {
        "CreditScore": CreditScore,
        "Geography": Geography,
        "Gender": Gender,
        "Age": Age,
        "Tenure": Tenure,
        "Balance": Balance,
        "NumOfProducts": NumOfProducts,
        "HasCrCard": HasCrCard,
        "IsActiveMember": IsActiveMember,
        "EstimatedSalary": EstimatedSalary
    }

    prob = predictor.predict(input_data)

    st.subheader(f"Churn Probability: {prob:.2f}")

    if prob > 0.7:
        st.error("High Risk Customer")
    elif prob > 0.4:
        st.warning("Medium Risk Customer")
    else:
        st.success("Low Risk Customer")
