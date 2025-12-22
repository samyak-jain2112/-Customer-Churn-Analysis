def churn_explanation_prompt(customer, top_features, rules):
    return f"""
You are a senior banking analyst.

Customer details:
{customer}

Top churn influencing features:
{top_features}

Rule-based observations:
{rules}

Task:
- Explain ONLY why this customer is likely to churn
- Provide business interpretation of the risk factors
- Do NOT suggest any actions, recommendations, or strategies
- Keep the explanation simple, clear, and non-technical
"""
