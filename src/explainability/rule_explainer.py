class RuleExplainer:
    def generate_rules(self, customer):
        reasons = []

        if customer["Age"] > 45:
            reasons.append("Customer belongs to an age group with higher churn risk")

        if customer["IsActiveMember"] == 0:
            reasons.append("Customer is not an active member")

        if customer["Balance"] > 100000:
            reasons.append("High account balance may indicate dissatisfaction")

        if customer["NumOfProducts"] == 1:
            reasons.append("Low product engagement detected")

        return reasons
