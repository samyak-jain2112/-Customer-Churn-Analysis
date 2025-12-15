# 📉 Customer Churn Prediction System

An end-to-end **Customer Churn Prediction** project that moves beyond notebook experimentation to a **real-time inference system** using a trained ML model and an interactive **Streamlit web application**.

This project demonstrates the **complete ML lifecycle**:
- Exploratory analysis & feature engineering  
- Model training with preprocessing  
- Real-time inference  
- User-facing application  

---

## 🚀 Project Motivation

Customer churn directly impacts revenue in subscription-based and banking businesses.  
The goal of this project is to **predict whether a customer is likely to churn**, using historical customer data and to expose the prediction through a **real-time UI**.

Unlike basic notebook projects, this implementation focuses on:
- **Training–inference consistency**
- **Reusable feature engineering**
- **Deployment-ready architecture**

---

## 🧠 Problem Statement

Given customer attributes such as:
- Credit score  
- Geography  
- Account balance  
- Engagement indicators (products, activity)  

Predict the probability that a customer will **exit (churn)**.

---

## 🗂️ Project Structure
Customer-Churn-Analysis/
│
├── data/
│ └── raw/
│ └── Churn_Modelling.csv
│
├── src/
│ ├── data_validation.py
│ ├── feature_engineering.py
│ ├── preprocessing.py
│ ├── model.py
│ └── train.py
│
├── pipelines/
│ └── inference_pipeline.py
│
├── app/
│ └── streamlit_app.py
│
├── artifacts/
│ └── model.pkl
│
├── notebooks/
│ └── eda-and-modeling.ipynb
│
├── requirements.txt
└── README.md

---

## 🔬 Approach & Methodology

### 1️⃣ Data Validation
- Ensures required columns are present  
- Prevents training on malformed datasets  

### 2️⃣ Feature Engineering
Custom business-driven features:
- **CreditUtilization** = Balance / CreditScore  
- **BalanceToSalaryRatio**  
- **InteractionScore** (products + activity + credit card)  

The **same feature logic** is reused for:
- Training  
- Real-time prediction  

➡️ This prevents training–inference mismatch.

---

### 3️⃣ Preprocessing & Model Training
- Categorical encoding and scaling handled via an sklearn pipeline  
- Multiple models were evaluated during experimentation  
- Best-performing model selected and saved as a single artifact  

---

### 4️⃣ Inference Pipeline
- Loads the trained model  
- Applies identical feature transformations  
- Returns churn probability for unseen customer input  

---

### 5️⃣ Streamlit Application
- Accepts real-time customer data  
- Displays churn probability  
- Categorizes customers into **Low / Medium / High Risk**  

---

## 🖥️ Streamlit App

The Streamlit app allows:
- Manual customer input  
- Instant churn probability prediction  
- Business-friendly risk interpretation  

---

## ⚙️ How to Run Locally

### 1️⃣ Install dependencies

pip install -r requirements.txt
---

### 2️⃣ Train the model
python src/train.py

---

### 3️⃣ Run Streamlit app
streamlit run app/streamlit_app.py

---

### 4️⃣ The app will open at:
http://localhost:8501

---


📊 Example Inputs
✅ Low-Risk Customer
CreditScore: 780
Age: 35
Tenure: 7
Balance: 20000
NumOfProducts: 2
HasCrCard: 1
IsActiveMember: 1
EstimatedSalary: 90000


Expected Output:

Low Risk (Low churn probability)