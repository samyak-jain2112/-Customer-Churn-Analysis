import os
from groq import Groq

class LLMExplainer:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def explain(self, customer, top_features, rules):
        prompt = f"""
Customer profile:
{customer}

Important churn features:
{top_features}

Rule-based reasons:
{rules}

Explain in simple business language why this customer may churn.
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  # fastest, least deprecated
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content

        except Exception as e:
            # 🔥 FALLBACK (THIS IS IMPORTANT)
            return (
                "LLM explanation currently unavailable. "
                "Based on rule-based analysis, the customer shows churn risk due to: "
                + ", ".join(rules)
            )
