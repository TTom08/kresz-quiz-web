import pytest
from app import create_app, db
from models import Question, Answer

@pytest.fixture(scope="function")
def client_with_questions():
    test_app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })
    with test_app.test_client() as client:
        with test_app.app_context():
            db.create_all()

            # 10 kérdés dummy válaszokkal
            for i in range(10):
                q = Question(text=f"Kérdés {i + 1}")
                db.session.add(q)
                db.session.flush()
                db.session.add_all([
                    Answer(text="Válasz A", is_correct=True, question_id=q.id),
                    Answer(text="Válasz B", is_correct=False, question_id=q.id),
                ])
            db.session.commit()

            yield client
            db.session.remove()
            db.drop_all()


def test_api_json_format_for_frontend(client_with_questions):

    client_with_questions.post('/api/quiz/start', json={'username': 'frontend'})


    response = client_with_questions.get('/api/quiz/leaderboard')
    data = response.get_json()


    assert 'leaderboard' in data
    for user in data['leaderboard']:
        assert 'username' in user
        assert 'score' in user


def test_questions_api_format(client_with_questions):
    response = client_with_questions.get('/api/quiz/questions')
    questions = response.get_json()

    for q in questions:
        assert 'text' in q
        assert 'answers' in q
        for a in q['answers']:
            assert 'text' in a
            assert 'is_correct' in a

