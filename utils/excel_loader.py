import pandas as pd

EXCEL_PATH = "dataset/diagnosa penyakit Cerebral Palsy.xlsx"

def load_gejala():
    return pd.read_excel(EXCEL_PATH, sheet_name="gejala")

def load_penyakit():
    return pd.read_excel(EXCEL_PATH, sheet_name="kode_penyakit")