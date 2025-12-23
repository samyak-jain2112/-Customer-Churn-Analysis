from pipelines.inference_pipeline import ChurnPredictor
from src.explainability.feature_importance import FeatureImportanceExplainer
from src.explainability.rule_explainer import RuleExplainer
from src.gen_ai.llm_explainer import LLMExplainer
from src.gen_ai.retention_agent import RetentionAgent
from src.feature_engineering import add_features
import pandas as pd

class ChurnIntelligencePipeline:
    def __init__(self):
        self.predictor = ChurnPredictor()
        self.rule_explainer = RuleExplainer()
        self.llm = LLMExplainer()
        self.retention = RetentionAgent()

    def run(self, input_data: dict):
        #Prediction
        churn_prob = self.predictor.predict_proba(input_data)

        #Feature importance 
        model = self.predictor.get_model()
        df = pd.DataFrame([input_data])
        df = add_features(df)

        fi_explainer = FeatureImportanceExplainer(model)

        top_features = fi_explainer.get_top_features()

        #Rule-based explanation
        rules = self.rule_explainer.generate_rules(input_data)

        #LLM explanation
        explanation = self.llm.explain(
            customer=input_data,
            top_features=top_features.to_dict(orient="records"),
            rules=rules
        )

        #Retention strategy
        strategy = self.retention.generate_strategy(explanation)

        return {
            "churn_probability": float(churn_prob),
            "explanation": explanation,
            "retention_strategy": strategy
        }
