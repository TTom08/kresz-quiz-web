from app import db
from models import User, Score, Question


MAX_POINTS = 10
TIME_LIMIT = 40

def choose_questions(n=22):
    total_questions = Question.query.count()
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of questions must be a positive integer")
    if n > total_questions:
        raise ValueError("Requested number of questions exceeds available questions")

    return Question.query.order_by(db.func.random()).limit(n).all()

def calculate_score(elapsed_time, correct=True):

    if not isinstance(elapsed_time, (int, float)) or elapsed_time < 0:
        raise ValueError("Elapsed time must be a non-negative number")
    if not isinstance(correct, bool):
        raise ValueError("Correct must be a boolean value")
    if not correct or elapsed_time >= TIME_LIMIT:
        return 0
    score = MAX_POINTS * ((TIME_LIMIT - elapsed_time) / TIME_LIMIT)
    return round(score, 2)

def add_score(username, score):

    if not username or not isinstance(username, str):
        raise ValueError("Username must be a non-empty string")
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number")
    if score < 0 or score > MAX_POINTS:
        raise ValueError(f"Score must be between 0 and {MAX_POINTS}")

    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username)
        db.session.add(user)
        db.session.flush()

    new_score = Score(user_id=user.id, score=score)
    db.session.add(new_score)
    db.session.commit()


def get_leaderboard(limit=10):
    results = (
        db.session.query(User.username, Score.score, Score.timestamp)
        .join(Score, User.id == Score.user_id)
        .order_by(Score.score.desc())
        .limit(limit)
        .all()
    )
    return [{"username": r.username, "score": r.score, "timestamp": r.timestamp} for r in results]

