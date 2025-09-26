from flask import Blueprint, request, jsonify
from app import db
from models import User, Score, Question, Answer

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/start", methods=["POST"])
def start_quiz():

    """
    Start a new quiz session for a user.

    Username is required to start the quiz.
    If the username already exists in the database, return a 409 Conflict.
    If the username doesn't exist yet, create a new User record.
    """

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

    """
    Submit a user's quiz score.

    Both username and score are required.
    If the username does not exist in the database, return 404 Not Found.
    If valid, save the new score for the user.
    """

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

@quiz_bp.route("/leaderboard", methods=["GET"])
def leaderboard():

    """
    Retrieve the top 10 users ranked by their best score.

    For each user, the highest score is selected.
    Results are ordered in descending order by best score.
    Only the top 10 users are returned.
    """

    results = (
        db.session.query(User.username, db.func.max(Score.score).label("best_score"))
        .join(Score)
        .group_by(User.username)
        .order_by(db.desc("best_score"))
        .limit(10)
        .all()
    )

    leaderboard = [
        {"username": row.username, "best_score": row.best_score} for row in results
    ]
    return jsonify({"leaderboard": leaderboard}), 200

@quiz_bp.route("/questions", methods=["GET"])
def get_questions():

    """
    Fetching quiz questions from the database in random order and with a limited number.
    """

    try:
        questions_data = Question.query.order_by(db.func.random()).limit(10).all()

        questions_list = []
        for q in questions_data:
            answers_list = [
                {"text": a.text,
                 "image_path": a.image_path,
                 "is_correct": a.is_correct}
                for a in q.answers
            ]
            questions_list.append({
                "id": q.id,
                "text": q.text,
                "image_path": q.image_path,
                "answers": answers_list
            })

        return jsonify(questions_list), 200

    except Exception as e:
        print(f"Hiba a kérdések lekérésekor: {e}")
        return jsonify({"error": "Szerveroldali hiba a kérdések betöltésekor."}), 500