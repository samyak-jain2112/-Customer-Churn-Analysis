from sklearn.ensemble import GradientBoostingClassifier

def get_model():
    return GradientBoostingClassifier(random_state=42)
