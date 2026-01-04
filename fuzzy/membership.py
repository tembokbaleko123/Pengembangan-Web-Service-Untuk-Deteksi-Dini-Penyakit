import numpy as np
import skfuzzy as fuzz

def gejala_membership(x):
    return {
        "rendah": fuzz.trimf(x, [0, 0, 0.5]),
        "sedang": fuzz.trimf(x, [0.3, 0.5, 0.7]),
        "tinggi": fuzz.trimf(x, [0.5, 1, 1])
    }
