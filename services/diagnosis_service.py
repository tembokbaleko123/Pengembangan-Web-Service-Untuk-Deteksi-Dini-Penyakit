from utils.excel_loader import load_gejala
from fuzzy.fuzzification import fuzzify
from fuzzy.inference import infer
from fuzzy.defuzzification import defuzzify
from cf.cf_rules import cf_gejala
from cf.cf_engine import combine_cf

def diagnose(user_input):
    df = load_gejala()
    hasil = {"P1": 0.0, "P2": 0.0, "P3": 0.0, "P4": 0.0}

    for _, row in df.iterrows():
        kode = row["Kode"]

        # 🔒 validasi input
        if kode not in user_input:
            continue
        if user_input[kode] <= 0:
            continue

        # 1️⃣ fuzzifikasi input user
        fuzzy_input = fuzzify(user_input[kode])

        # 2️⃣ ambil nilai representatif fuzzy (sedang + tinggi)
        fuzzy_strength = max(
            fuzzy_input["sedang"],
            fuzzy_input["tinggi"]
        )

        for p in hasil:
            if row[p] == "X":
                # 3️⃣ Mamdani (MIN)
                mamdani = infer(
                    {"sedang": fuzzy_strength, "tinggi": fuzzy_strength},
                    1.0  # ❗ densitas TIDAK dipakai di sini
                )

                crisp = defuzzify(mamdani)

                # 4️⃣ CF pakar (densitas dipakai SEKALI)
                cf = cf_gejala(crisp, row["Nilai Densitas"])

                # 5️⃣ Combine CF
                hasil[p] = combine_cf(hasil[p], cf)

    return {k: round(v * 100, 2) for k, v in hasil.items()}
