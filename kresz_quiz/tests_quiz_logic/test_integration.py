
import pytest
import uuid
from app import create_app, db
from models import User, Score

@pytest.fixture(scope="function")
def client():
    test_app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with test_app.test_client() as client:
        with test_app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


def unique_username():
    """Generate a unique username to avoid conflicts"""
    return f"user_{uuid.uuid4().hex[:8]}"


def test_start_quiz_creates_user(client):
    username = unique_username()
    response = client.post('/api/quiz/start', json={'username': username})
    assert response.status_code == 201

    user = User.query.filter_by(username=username).first()
    assert user is not None


def test_submit_quiz_saves_score(client):
    username = unique_username()
    client.post('/api/quiz/start', json={'username': username})

    response = client.post('/api/quiz/submit', json={'username': username, 'score': 7})
    assert response.status_code == 201

    user_id = User.query.filter_by(username=username).first().id
    score = Score.query.filter_by(user_id=user_id, score=7).first()
    assert score is not None


def test_leaderboard_returns_correct_order(client):
    username1 = unique_username()
    username2 = unique_username()

    client.post('/api/quiz/start', json={'username': username1})
    client.post('/api/quiz/start', json={'username': username2})

    client.post('/api/quiz/submit', json={'username': username1, 'score': 5})
    client.post('/api/quiz/submit', json={'username': username2, 'score': 10})

    response = client.get('/api/quiz/leaderboard')
    data = response.get_json()['leaderboard']

    assert data[0]['username'] == username2
    assert data[0]['score'] == 10
    assert data[1]['username'] == username1
    assert data[1]['score'] == 5
