from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.diagnosis_service import diagnose
from utils.excel_loader import load_gejala
from models.diagnosis_history import DiagnosisHistory
from extensions import db

diagnosis_bp = Blueprint("diagnosis", __name__)


@diagnosis_bp.route("/api/diagnosis", methods=["POST"])
@jwt_required()
def diagnosis():
    user_id = get_jwt_identity()   # ambil user dari JWT
    user_input = request.get_json()

    result = diagnose(user_input)

    history = DiagnosisHistory(
        user_id=user_id,
        hasil=result
    )

    db.session.add(history)
    db.session.commit()

    return jsonify(result), 200


@diagnosis_bp.route("/", methods=["GET"])
def index():
    df = load_gejala()
    gejala = df.to_dict(orient="records")
    return render_template("index.html", gejala=gejala)
