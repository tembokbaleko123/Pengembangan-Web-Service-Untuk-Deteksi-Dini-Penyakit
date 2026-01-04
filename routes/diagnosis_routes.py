from flask import Blueprint, request, jsonify, render_template
from services.diagnosis_service import diagnose
from utils.excel_loader import load_gejala


diagnosis_bp = Blueprint("diagnosis", __name__)

@diagnosis_bp.route("/diagnosis", methods=["POST"])
def diagnosis():
    return jsonify(diagnose(request.json))


@diagnosis_bp.route("/", methods=["GET"])
def index():
    df = load_gejala()

    gejala = df.to_dict(orient="records")
    return render_template("index.html", gejala=gejala)
