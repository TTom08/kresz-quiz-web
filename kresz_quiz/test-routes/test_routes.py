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


