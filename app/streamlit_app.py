import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import streamlit as st
from pipelines.churn_intelligence_pipeline import ChurnIntelligencePipeline

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="GenAI Customer Churn Intelligence",
    layout="centered"
)

st.title(" GenAI-Powered Customer Churn Intelligence System")

pipeline = ChurnIntelligencePipeline()

# ---------------- Input Form ----------------
with st.form("customer_form"):
    CreditScore = st.number_input("Credit Score", 300, 900, 650)
    Geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", 18, 100, 35)
    Tenure = st.number_input("Tenure (years)", 0, 10, 3)
    Balance = st.number_input("Balance", 0.0, value=50000.0)
    NumOfProducts = st.number_input("Number of Products", 1, 4, 1)
    HasCrCard = st.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.selectbox("Is Active Member", [0, 1])
    EstimatedSalary = st.number_input("Estimated Salary", 0.0, value=60000.0)

    submit = st.form_submit_button("Analyze Churn Risk")

# ---------------- Prediction + GenAI ----------------
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

    with st.spinner("Analyzing customer risk using ML + GenAI..."):
        result = pipeline.run(input_data)

    churn_prob = result["churn_probability"]

    # ---------------- Risk Output ----------------
    st.subheader(f" Churn Probability: {churn_prob:.2f}")

    if churn_prob > 0.7:
        st.error(" High Risk Customer")
    elif churn_prob > 0.4:
        st.warning(" Medium Risk Customer")
    else:
        st.success("Low Risk Customer")

    # ---------------- Explanation ----------------
    st.divider()
    st.subheader("Why is this customer likely to churn?")
    st.write(result["explanation"])

    # ---------------- Retention Strategy ----------------
    st.divider()
    st.subheader("Recommended Retention Actions")
    st.write(result["retention_strategy"])
