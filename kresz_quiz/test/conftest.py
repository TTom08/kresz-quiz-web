import uuid

import pytest
from app import create_app, db
from models import User, Question, Answer, Score

@pytest.fixture(scope='session')
def client():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    })

    with app.app_context():
        db.create_all()
        yield app.test_client()

@pytest.fixture(scope='function', autouse=True)
def session_scope(client):
    with client.application.app_context():
        yield db.session
        db.session.rollback()


@pytest.fixture
def test_user(session_scope):
    unique_username = "TestUser_" + str(uuid.uuid4())[:8]
    user = User(username=unique_username)
    session_scope.add(user)
    session_scope.commit()
    return user
