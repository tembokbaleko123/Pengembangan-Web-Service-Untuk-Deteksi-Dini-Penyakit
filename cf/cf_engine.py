def combine_cf(cf1, cf2):
    """
    Kombinasi CF positif:
    CFcombine = CF1 + CF2(1 − CF1)
    """
    return cf1 + cf2 * (1 - cf1)
