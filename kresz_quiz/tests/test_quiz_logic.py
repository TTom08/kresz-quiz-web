import pytest
from app import app, db
from models import User, Score, Question, Answer
from kresz_quiz.quiz_logic import choose_questions, calculate_score, add_score, get_leaderboard


@pytest.fixture(scope="function")
def test_app():

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()


        q1 = Question(text="Mekkora a megengedett sebesség?")
        q2 = Question(text="Melyik jelzés tiltja a megállást?")
        db.session.add_all([q1, q2])
        db.session.flush()
        db.session.add_all([
            Answer(text="50 km/h", is_correct=True, question_id=q1.id),
            Answer(text="60 km/h", is_correct=False, question_id=q1.id),
            Answer(text="Piros kör X-szel", is_correct=True, question_id=q2.id),
            Answer(text="Sárga rombusz", is_correct=False, question_id=q2.id)
        ])
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def test_user(test_app):
    user = User(username="TestUser")
    db.session.add(user)
    db.session.commit()
    yield user
    db.session.rollback()


def test_choose_questions_negative_number(test_app):
    with pytest.raises(ValueError):
        choose_questions(-5)

def test_choose_questions_zero(test_app):
    with pytest.raises(ValueError):
        choose_questions(0)

def test_choose_questions_too_many(test_app):
    total_questions = Question.query.count()
    with pytest.raises(ValueError):
        choose_questions(total_questions + 1)

def test_choose_questions_valid(test_app):
    questions = choose_questions(2)
    assert len(questions) == 2


def test_calculate_score_negative_time():
    with pytest.raises(ValueError):
        calculate_score(-1)

def test_calculate_score_wrong_type_correct():
    with pytest.raises(ValueError):
        calculate_score(10, correct="yes")

def test_calculate_score_wrong_type_elapsed():
    with pytest.raises(ValueError):
        calculate_score("10", correct=True)

def test_calculate_score_wrong_answer():
    assert calculate_score(10, correct=False) == 0

def test_calculate_score_time_exceeded():
    assert calculate_score(50, correct=True) == 0

def test_calculate_score_normal():
    score = calculate_score(20, correct=True)
    assert score == 5  # MAX_POINTS=10, TIME_LIMIT=40


def test_add_score_non_existing_user(test_app):
    with pytest.raises(ValueError):
        add_score("NonExistentUser", 5)

def test_add_score_invalid_score_negative(test_app, test_user):
    with pytest.raises(ValueError):
        add_score(test_user.username, -1)

def test_add_score_invalid_score_too_high(test_app, test_user):
    with pytest.raises(ValueError):
        add_score(test_user.username, 20)

def test_add_score_valid(test_app, test_user):
    add_score(test_user.username, 7)
    scores = Score.query.filter_by(user_id=test_user.id).all()
    assert any(s.score == 7 for s in scores)


def test_get_leaderboard_empty(test_app):
    leaderboard = get_leaderboard()
    assert leaderboard == []

def test_get_leaderboard_single_user(test_app, test_user):
    add_score(test_user.username, 8)
    leaderboard = get_leaderboard()
    assert any(u["username"] == test_user.username for u in leaderboard)

def test_get_leaderboard_limit(test_app, test_user):
    add_score(test_user.username, 8)
    leaderboard = get_leaderboard(limit=1)
    assert len(leaderboard) <= 1


def test_choose_questions_exact_total(test_app):
    total = Question.query.count()
    questions = choose_questions(total)
    assert len(questions) == total


def test_add_score_zero_point(test_app, test_user):
    add_score(test_user.username, 0)
    scores = Score.query.filter_by(user_id=test_user.id).all()
    assert any(s.score == 0 for s in scores)


def test_add_score_max_point(test_app, test_user):
    add_score(test_user.username, 10)
    scores = Score.query.filter_by(user_id=test_user.id).all()
    assert any(s.score == 10 for s in scores)


def test_get_leaderboard_limit_exceeds(test_app, test_user):

    add_score(test_user.username, 7)
    leaderboard = get_leaderboard(limit=100)
    assert len(leaderboard) == 1
    assert leaderboard[0]["username"] == test_user.username
