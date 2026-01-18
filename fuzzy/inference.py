def infer(fuzzy_input, rule_strength):
    """
    Mamdani inference:
    MIN antara fuzzy input dan rule strength (densitas)
    """
    return min(
        max(fuzzy_input["sedang"], fuzzy_input["tinggi"]),
        rule_strength
    )
