import uuid

import pytest
# KIZÁRÓLAG a create_app függvényt importáljuk, nem a globális app példányt!
from app import create_app, db
from models import User, Question, Answer, Score

@pytest.fixture(scope='session')
def client():
    # Itt hozza létre az alkalmazást a tesztkonfigurációval,
    # amely felülírja az éles PostgreSQL URI-t.
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', # Elszigetelt, ideiglenes DB
    })

    with app.app_context():
        # A memóriában lévő DB tábláinak létrehozása
        db.create_all()
        yield app.test_client()

@pytest.fixture(scope='function', autouse=True)
def session_scope(client):
    # Ez továbbra is gondoskodik a tesztek közötti rollbackről (takarításról)
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
