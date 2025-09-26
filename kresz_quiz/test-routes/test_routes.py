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
