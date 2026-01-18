from flask import Blueprint, request, jsonify, render_template, session, url_for, redirect
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from extensions import db
from utils.log_decorator import log_action

auth_bp = Blueprint("auth", __name__)

# =====================
# SIGNUP PAGE
# =====================
@auth_bp.route("/signup", methods=["GET"])
def signup_page():
    return render_template("auth/signup.html")

# LOGIN PAGE
@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("auth/login.html")

# PROFILE PAGE
@auth_bp.route("/profile-page", methods=["GET"])
def profile_page():
    return render_template("profile/profile.html")

@auth_bp.route("/profile/edit", methods=["GET"])
def edit_profile_page():
    if "user_id" not in session:
        return redirect(url_for("auth.login_page"))

    user = User.query.get_or_404(session["user_id"])
    return render_template("profile/edit_profile.html", user=user)

# =====================
# REGISTER
# =====================
@auth_bp.route("/register", methods=["POST"])
@log_action("REGISTER", "User melakukan registrasi", use_jwt=False)
def register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    username = data.get("username")

    if not email or not password or not username:
        return jsonify({
            "message": "Email, password, dan username wajib diisi"
        }), 400

    # cek email sudah terdaftar
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email sudah terdaftar"}), 409

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username sudah digunakan"}), 409

    user = User(
        email=email,
        username=username
    )
    user.set_password(password)

    db.session.add(user)

    return jsonify({"message": "Registrasi berhasil"}), 201

# =====================
# LOGOUT
# =====================
@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for('index'))


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

        # 🔹 SIMPAN SESSION (INI KUNCI)
        session['user_id'] = user.id
        session['username'] = user.username
        session['profile_pic'] = (
    f"uploads/{user.image}" if user.image else "asset/img/dummy-pic.png"
)
        
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

    # Pastikan path image sesuai dengan folder uploads Anda
    pic_path = f"uploads/{user.image}" if user.image else "asset/img/dummy-pic.png"

    return jsonify({
        "email": user.email, 
        "profile_pic": pic_path # Sesuaikan path agar bisa dibaca frontend
    }), 200

# =====================
# UPDATE PROFILE
# =====================
@auth_bp.route("/profile", methods=["PUT"])
@jwt_required()
@log_action("UPDATE_PROFILE", "User mengubah profil")
def update_profile():
    user_id = get_jwt_identity()

    # kalau pakai form-data (untuk image)
    email = request.form.get("email")
    password = request.form.get("password")
    image = request.files.get("image")

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User tidak ditemukan"}), 404

    # 🔹 update email
    if email:
        if User.query.filter(User.email == email, User.id != user.id).first():
            return jsonify({"msg": "Email sudah digunakan"}), 400
        user.email = email

    # 🔹 update password
    if password:
        user.set_password(password)

    # 🔹 update image
    if image:
        filename = f"user_{user.id}_{image.filename}"
        image.save(f"static/uploads/{filename}")
        user.image = filename
        # Perbarui session agar Navbar langsung berubah tanpa relogin
        session['profile_pic'] = f"uploads/{filename}"

    return jsonify({"msg": "Profil berhasil diperbarui"}), 200