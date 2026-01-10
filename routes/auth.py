from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from extensions import db
from utils.log_decorator import log_action

auth_bp = Blueprint("auth", __name__)


# =====================
# REGISTER
# =====================
@auth_bp.route("/register", methods=["POST"])
@log_action("REGISTER", "User melakukan registrasi", use_jwt=False)
def register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email dan password wajib diisi"}), 400

    # cek email sudah terdaftar
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email sudah terdaftar"}), 409

    user = User(email=email)
    user.set_password(password)

    db.session.add(user)

    return jsonify({"message": "Registrasi berhasil"}), 201




# =====================
# LOGIN
# =====================
@auth_bp.route("/login", methods=["POST"])
@log_action("LOGIN", "User melakukan login", use_jwt=False)
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data.get("email")).first()

    if user and user.check_password(data.get("password")):
        token = create_access_token(identity=str(user.id))
        return jsonify(access_token=token), 200

    return jsonify({"message": "Email atau password salah"}), 401




# =====================
# GET PROFILE
# =====================
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
@log_action("VIEW_PROFILE", "User melihat profil")
def get_profile():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User tidak ditemukan"}), 404

    return jsonify({
        "id": user.id,
        "email": user.email
    }), 200



# =====================
# UPDATE PROFILE
# =====================
@auth_bp.route("/profile", methods=["PUT"])
@jwt_required()
@log_action("UPDATE_PROFILE", "User mengubah data akun")
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User tidak ditemukan"}), 404

    # 🔹 Update email
    if "email" in data:
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"msg": "Email sudah digunakan"}), 400
        user.email = data["email"]

    # 🔹 Update password
    if "password" in data:
        user.set_password(data["password"])


    return jsonify({"msg": "Email atau password berhasil diperbarui"}), 200
