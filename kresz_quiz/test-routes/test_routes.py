import json
from models import User, Score, Question, Answer
import pytest

def test_01_start_quiz_success(client, app_db):
    response = client.post('/api/quiz/start', json={'username': 'ujfelhasznalo'})
    assert response.status_code == 201
    assert User.query.filter_by(username='ujfelhasznalo').first() is not None


def test_02_start_quiz_username_taken(client, app_db):
    response = client.post('/api/quiz/start', json={'username': 'tomi'})

    assert response.status_code == 409

    data = response.get_json()

    expected_error_message = "Ez a felhasználónév már foglalt"

    assert data is not None
    assert data.get('error') == expected_error_message


def test_03_start_quiz_missing_username(client, app_db):
    response = client.post('/api/quiz/start', json={})

    assert response.status_code == 400

    data = response.get_json()

    expected_error_message = "Felhasználónév kötelező"

    assert data is not None
    assert data.get('error') == expected_error_message


def test_04_start_quiz_empty_username(client, app_db):
    response = client.post('/api/quiz/start', json={'username': '   '})
    assert response.status_code == 400


def test_05_start_quiz_user_count_increase(client, app_db):
    initial_count = User.query.count()
    client.post('/api/quiz/start', json={'username': 'uj_nev'})
    assert User.query.count() == initial_count + 1


# UNIT TESTS FOR THE /submit ENDPOINT

def test_06_submit_quiz_success(client, app_db):
    unique_score = 999

    response = client.post('/api/quiz/submit', json={'username': 'tomi', 'score': unique_score})

    assert response.status_code == 201

    assert Score.query.filter_by(score=unique_score).count() == 1

    data = response.get_json()
    assert data is not None
    assert data.get('message') == "Pontszám elmentve"


def test_07_submit_quiz_unknown_user(client, app_db):
    response = client.post('/api/quiz/submit', json={'username': 'ismeretlen', 'score': 10})

    assert response.status_code == 404

    data = response.get_json()
    expected_error_message = "Ismeretlen felhasználó"
    assert data is not None
    assert data.get('error') == expected_error_message


def test_08_submit_quiz_missing_score(client, app_db):
    response = client.post('/api/quiz/submit', json={'username': 'tomi'})

    assert response.status_code == 400

    data = response.get_json()
    expected_error_message = "Hiányzó adatok"
    assert data is not None
    assert data.get('error') == expected_error_message


def test_09_submit_quiz_score_count_increase(client, app_db):
    initial_count = Score.query.count()
    client.post('/api/quiz/submit', json={'username': 'anna', 'score': 99})
    assert Score.query.count() == initial_count + 1


def test_10_submit_quiz_zero_score(client, app_db):
    response = client.post('/api/quiz/submit', json={'username': 'zoli', 'score': 0})

    assert response.status_code == 201

    assert Score.query.filter_by(score=0, user_id=User.query.filter_by(username='zoli').first().id).count() == 1

# UNIT TESTS FOR THE /api/quiz/leaderboard PATH

def test_11_leaderboard_ordering(client, app_db):
    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert response.status_code == 200
    assert data[0]['username'] == 'zoli'
    assert data[1]['username'] == 'tomi'
    assert data[2]['username'] == 'anna'


def test_12_leaderboard_empty(client, app_db):
    app_db.session.query(Score).delete()
    app_db.session.query(User).delete()
    app_db.session.commit()

    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert response.status_code == 200
    assert len(data) == 0


def test_13_leaderboard_limit(client, app_db):
    for i in range(4, 14):
        u = User(username=f"tempuser{i}")
        app_db.session.add(u)

        app_db.session.flush()

        s = Score(score=i * 10, user_id=u.id)
        app_db.session.add(s)

    app_db.session.commit()
    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert response.status_code == 200
    assert len(data) == 10


def test_14_leaderboard_best_score_selection(client, app_db):
    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert response.status_code == 200

    tomi_score = next((item for item in data if item["username"] == "tomi"), None)

    assert tomi_score is not None
    assert tomi_score['best_score'] == 100


def test_15_leaderboard_no_scores(client, app_db):
    app_db.session.query(Score).delete()
    app_db.session.commit()

    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert response.status_code == 200
    assert len(data) == 0


# UNIT TESTS FOR THE /api/quiz/questions PATH

def test_16_get_questions_limit(client, app_db):
    response = client.get('/api/quiz/questions')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 10


def test_17_get_questions_question_image_path(client, app_db):
    response = client.get('/api/quiz/questions')
    data = response.get_json()
    q_with_img_text = Question.query.filter(Question.text.like('%Kérdés 2%')).first().text
    q_no_img_text = Question.query.filter(Question.text.like('%Kérdés 1%')).first().text

    q_with_img = next(q for q in data if q['text'] == q_with_img_text)
    assert q_with_img['image_path'] is not None

    q_no_img = next(q for q in data if q['text'] == q_no_img_text)
    assert q_no_img['image_path'] is None


def test_18_get_questions_answer_image_path(client, app_db):
    response = client.get('/api/quiz/questions')
    data = response.get_json()

    q_with_ans_img_text = Question.query.filter(Question.text.like('%Kérdés 3%')).first().text
    q_with_ans_img = next(q for q in data if q['text'] == q_with_ans_img_text)

    answer_with_img = next(a for a in q_with_ans_img['answers'] if a['text'] == 'Helyes 3')
    answer_without_img = next(a for a in q_with_ans_img['answers'] if a['text'] == 'Helytelen 3')

    assert answer_with_img['image_path'] is not None
    assert answer_without_img['image_path'] is None


def test_19_get_questions_correct_answer_flag(client, app_db):
    response = client.get('/api/quiz/questions')
    data = response.get_json()
    q = data[0]

    correct = next(a for a in q['answers'] if a['is_correct'])
    incorrect = next(a for a in q['answers'] if not a['is_correct'])

    assert correct['is_correct'] is True
    assert incorrect['is_correct'] is False


def test_20_get_questions_empty_db(client, app_db):
    app_db.session.query(Question).delete()
    app_db.session.query(Answer).delete()
    app_db.session.commit()

    response = client.get('/api/quiz/questions')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 0
