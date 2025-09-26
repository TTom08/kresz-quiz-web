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

@quiz_bp.route("/submit", methods=["POST"])
def submit_quiz():
    data = request.get_json()
    username = data.get("username")
    score_value = data.get("score")

    if not username or score_value is None:
        return jsonify({"error": "Hiányzó adatok"}), 400

    # Check user
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "Ismeretlen felhasználó"}), 404

    # Saving score
    new_score = Score(score=score_value, user_id=user.id)
    db.session.add(new_score)
    db.session.commit()

    return jsonify({
        "message": "Pontszám elmentve",
        "username": username,
        "score": score_value
    }), 201