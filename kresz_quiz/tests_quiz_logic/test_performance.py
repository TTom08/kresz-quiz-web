
import pytest
import uuid
import time
from app import app, db
from models import User, Score

@pytest.fixture(scope="function")
def client_with_many_users():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()


            for i in range(500):
                username = f"user_{i}_{uuid.uuid4().hex[:4]}"
                user = User(username=username)
                db.session.add(user)
                db.session.flush()
                score = Score(user_id=user.id, score=i % 10 + 1)
                db.session.add(score)

            db.session.commit()
            yield client
            db.session.remove()
            db.drop_all()

def test_leaderboard_performance(client_with_many_users):

    start_time = time.time()
    response = client_with_many_users.get('/api/quiz/leaderboard')
    duration = time.time() - start_time

    assert response.status_code == 200
    data = response.get_json()
    assert 'leaderboard' in data
    assert len(data['leaderboard']) <= 10

    print(f"Ranglista lekérés ideje 500 felhasználóval: {duration:.4f} s")
    assert duration < 1.0
