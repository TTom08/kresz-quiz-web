import pytest
from app import app, db
from models import User, Question, Answer, Score


@pytest.fixture(scope='session')
def flask_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        if hasattr(db, 'session'):
            db.session.remove()

        if hasattr(db, 'get_engine') and db.get_engine() is not None:
            db.get_engine().dispose()

        if 'sqlalchemy' in app.extensions:
            del app.extensions['sqlalchemy']

        db.init_app(app)

        yield app


@pytest.fixture(scope='function')
def app_db(flask_app):
    with flask_app.app_context():
        db.create_all()

        u1 = User(username="tomi")
        u2 = User(username="anna")
        u3 = User(username="zoli")
        db.session.add_all([u1, u2, u3])

        db.session.commit()

        db.session.add_all([
            Score(score=100, user_id=u1.id),
            Score(score=50, user_id=u1.id),
            Score(score=75, user_id=u2.id),
            Score(score=120, user_id=u3.id)
        ])

        for i in range(1, 13):
            q = Question(text=f"Kérdés {i}", image_path=f"/img/q{i}.png" if i % 2 == 0 else None)
            q.answers = [
                Answer(text=f"Helyes {i}", is_correct=True, image_path=f"/img/a{i}.png" if i % 3 == 0 else None),
                Answer(text=f"Helytelen {i}", is_correct=False),
            ]
            db.session.add(q)

        db.session.commit()

        yield db

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def client(flask_app):
    return flask_app.test_client()