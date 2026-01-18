import numpy as np
from fuzzy.membership import gejala_membership

def fuzzify(nilai):
    x = np.linspace(0, 1, 100)
    mf = gejala_membership(x)

    return {
        "rendah": np.interp(nilai, x, mf["rendah"]),
        "sedang": np.interp(nilai, x, mf["sedang"]),
        "tinggi": np.interp(nilai, x, mf["tinggi"])
    }
