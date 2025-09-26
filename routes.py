from flask import Blueprint, request, jsonify
from app import db
from models import User, Question, Answer, Score

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/start", methods=["POST"])
def start_quiz():
    data = request.get_json()
    username = data.get("username")

    if not username or username.strip() == "":
        return jsonify({"error": "Felhasználónév kötelező"}), 400 # OK

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"error": "Ez a felhasználónév már foglalt"}), 409  # Conflict

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"Kvíz elindítva {username} számára"}), 201 # Created