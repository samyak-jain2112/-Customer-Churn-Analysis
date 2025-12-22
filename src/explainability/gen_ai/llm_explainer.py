import os
from dotenv import load_dotenv
from groq import Groq
from .prompt_templates import churn_explanation_prompt

# Load .env file
load_dotenv()

class LLMExplainer:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def explain(self, customer, top_features, rules):
        prompt = churn_explanation_prompt(customer, top_features, rules)

        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content
