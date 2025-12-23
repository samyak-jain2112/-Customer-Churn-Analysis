import os
from groq import Groq


def retention_prompt(explanation):
    return f"""
You are a customer retention expert working in a bank.

Based on the churn explanation below:
1. Suggest 3 actionable retention strategies
2. Keep them practical and cost-aware
3. Add a short business justification for each

Churn Explanation:
{explanation}
"""


class RetentionAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_strategy(self, explanation):
        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  
                messages=[
                    {"role": "user", "content": retention_prompt(explanation)}
                ],
                temperature=0.5
            )

            return response.choices[0].message.content

        except Exception:
          
            return (
                "Suggested retention actions:\n"
                "1. Increase engagement through personalized offers and communication.\n"
                "2. Assign a relationship manager for proactive support.\n"
                "3. Encourage product bundling with loyalty benefits."
            )
