import pandas as pd
import joblib
import numpy as np

class FeatureImportanceExplainer:
    def __init__(self, model):
        self.model = model
        self.feature_names = joblib.load("artifacts/feature_names.pkl")

    def _get_final_estimator(self):
        """
        Agar model Pipeline hai to last estimator return karo,
        warna direct model return karo.
        """
        if hasattr(self.model, "steps"):
            return self.model.steps[-1][1]
        return self.model

    def get_top_features(self, top_k=5):
        estimator = self._get_final_estimator()

        # 1️⃣ Importance nikaalo
        if hasattr(estimator, "feature_importances_"):
            importances = estimator.feature_importances_

        elif hasattr(estimator, "coef_"):
            importances = np.abs(estimator.coef_[0])

        else:
            raise ValueError("Model does not support feature importance")

        # 2️⃣ SAFETY: length mismatch handle karo
        min_len = min(len(self.feature_names), len(importances))

        features = self.feature_names[:min_len]
        importances = importances[:min_len]

        # 3️⃣ DataFrame banao (ab kabhi error nahi aayega)
        df = pd.DataFrame({
            "feature": features,
            "importance": importances
        })

        return (
            df.sort_values(by="importance", ascending=False)
              .head(top_k)
              .reset_index(drop=True)
        )
