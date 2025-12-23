# 📉 Customer Churn Intelligence System

An end-to-end **Customer Churn Intelligence** platform that goes beyond prediction to deliver **explainable insights and actionable retention intelligence** using **Machine Learning + GenAI**, deployed via an interactive **Streamlit application**.

This project demonstrates how churn models can be transformed into **decision-support systems** rather than isolated predictive notebooks.

---

##  Project Overview

Customer churn is one of the most critical business problems in banking and subscription-driven industries.  
While most churn projects stop at prediction, this system focuses on:

- **Why a customer is likely to churn**
- **How the risk can be interpreted in business terms**
- **What retention actions can be considered**

The system combines:
- Traditional ML for churn prediction  
- Rule-based + feature-driven explainability  
- GenAI-powered natural language reasoning  
- A real-time user-facing web application  

---

##  Problem Statement

Given customer attributes such as:
- Credit score and demographics  
- Account balance and salary  
- Product usage and engagement behavior  

The system aims to:
1. Predict the probability of customer churn  
2. Explain the churn risk in **business-friendly language**  
3. Categorize customers into **Low / Medium / High churn risk**  
4. Generate **intelligent insights** to support retention decisions  

---

##  System Architecture 

```
Raw Customer Data
        ↓
Feature Engineering
        ↓
ML Churn Model
        ↓
Inference Pipeline
        ↓
Explainability Layer
        ↓
GenAI Reasoning Engine
        ↓
Streamlit Intelligence Dashboard
```

---

##  Project Structure

```
-CUSTOMER-CHURN-ANALYSIS/
│
├── app/
│ └── streamlit_app.py # Streamlit UI
│
├── artifacts/ # Generated artifacts 
│
├── data/
│
├── notebooks/
│
├── pipelines/
│ ├── churn_intelligence_pipeline.py
│ └── inference_pipeline.py
│
├── src/
│ ├── explainability/
│ │ ├── feature_importance.py
│ │ └── rule_explainer.py
│ │
│ ├── gen_ai/
│ │ ├── llm_explainer.py
│ │ ├── prompt_templates.py
│ │ └── retention_agent.py
│ │
│ ├── data_validation.py
│ ├── feature_engineering.py
│ ├── preprocessing.py
│ ├── model.py
│ └── train.py
│
├── test/
│
├── .env # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  Methodology & Design Choices

### 1️⃣ Data Validation
- Schema and column checks before training  
- Prevents silent failures due to malformed data  

---

### 2️⃣ Feature Engineering
Business-driven features designed to capture churn behavior:
- **CreditUtilization** = Balance / CreditScore  
- **BalanceToSalaryRatio**  
- **EngagementScore** (products + activity + credit card ownership)  

The **same feature logic** is reused across:
- Training
- Inference
- Explainability  

➡️ This ensures **training–inference consistency**.

---

### 3️⃣ Model Training
- Scikit-learn pipelines used for preprocessing and modeling  
- Multiple algorithms evaluated during experimentation  
- Best-performing model selected based on business-aligned metrics  
- Model artifacts generated via reproducible training scripts  

---

### 4️⃣ Inference Pipeline
- Loads trained model and feature metadata  
- Applies identical transformations to unseen input  
- Outputs churn probability with confidence interpretation  

---

### 5️⃣ Explainability Layer (No SHAP by Design)
Instead of relying solely on technical explainability tools, the system focuses on:
- Feature contribution reasoning  
- Rule-based risk signals  
- Human-readable explanations  

This makes outputs understandable to **non-technical stakeholders**.

---

### 6️⃣ GenAI-Powered Intelligence
A GenAI layer converts structured churn signals into:
- Natural language explanations answering **“Why will this customer churn?”**
- Context-aware reasoning based on customer profile  

---

### 7️⃣ Streamlit Intelligence Dashboard
The Streamlit application provides:
- Real-time customer input  
- Churn probability prediction  
- Risk categorization (Low / Medium / High)  
- Clear textual explanations of churn risk  

---

##  How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 2️⃣ Train the model
```bash
python src/train.py
```

---

### 3️⃣ Run the Streamlit app
```bash
streamlit run streamlit_app/streamlit_app.py
```

---

### 4️⃣ Access the app
```
http://localhost:8501
```

---

##  Environment Variables

Create a `.env` file locally:
```
GROQ_API_KEY=your_api_key_here
```

---

##  Key Takeaways

- End-to-end ML + GenAI system  
- Business-first explainability  
- Production-aware design  
- Interview-ready project  

---

##  Author
**Samyak Jain**  
B.Tech CSE | Data Science & Machine Learning
