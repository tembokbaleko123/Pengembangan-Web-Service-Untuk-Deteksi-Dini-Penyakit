from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.diagnosis_service import diagnose
from utils.excel_loader import load_gejala
from models.diagnosis_history import DiagnosisHistory
from extensions import db
from utils.log_decorator import log_action

diagnosis_bp = Blueprint("diagnosis", __name__)


# =====================
# PAGE DIAGNOSIS
# =====================
@diagnosis_bp.route("/diagnosa", methods=["GET"])
def diagnosis_page():
    df = load_gejala()
    gejala = df.to_dict(orient="records")
    return render_template("diagnosa/diagnosa.html", gejala=gejala)

# =====================
# PAGE HASIL (OUTPUT) - TAMBAHAN BARU
# =====================
@diagnosis_bp.route("/diagnosis/hasil", methods=["GET"])
def result_page():
    # Halaman ini hanya merender template kosong
    # Data akan diisi oleh JavaScript dari localStorage
    return render_template("diagnosa/hasil_diagnosa.html")


# =====================
# API DIAGNOSIS (JWT)
# =====================
@diagnosis_bp.route("/api/diagnosis", methods=["POST"])
@jwt_required()
@log_action("DIAGNOSIS", "User melakukan diagnosis")
def diagnosis():
    user_id = get_jwt_identity()   # ambil user dari JWT
    user_input = request.get_json()

    result = diagnose(user_input)

    history = DiagnosisHistory(
        user_id=user_id,
        hasil=result
    )

    db.session.add(history)

    return jsonify(result), 200