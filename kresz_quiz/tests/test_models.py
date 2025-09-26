from models import User, Question, Answer, Score
from app import db
import pytest

def test_1_create_user(session_scope):
    user = User(username='TestUser1')
    session_scope.add(user)
    session_scope.commit()
    assert user.id is not None


def test_2_read_user(session_scope):
    user = session_scope.query(User).filter_by(username='TestUser1').first()
    assert user is not None
    assert user.username == 'TestUser1'


def test_3_update_user(session_scope):
    user = session_scope.query(User).filter_by(username='TestUser1').first()
    user.username = 'UpdatedUser'
    session_scope.commit()
    updated_user = session_scope.query(User).filter_by(username='UpdatedUser').first()
    assert updated_user.username == 'UpdatedUser'

def test_4_delete_user(session_scope):
    user = session_scope.query(User).filter_by(username='UpdatedUser').first()
    session_scope.delete(user)
    session_scope.commit()
    deleted_user = session_scope.query(User).filter_by(username='UpdatedUser').first()
    assert deleted_user is None


def test_5_create_question_and_answer(session_scope):
    q = Question(text='Test Question with Answer')
    session_scope.add(q)
    session_scope.flush()
    a = Answer(text='Test Answer', is_correct=True, question_id=q.id)
    session_scope.add(a)
    session_scope.commit()
    assert len(q.answers) == 1


def test_6_read_question_and_answer(session_scope):
    q = session_scope.query(Question).filter(Question.text.like('%Test Question%')).first()
    assert q.answers[0].text == 'Test Answer'

def test_7_score_model_has_timestamp(session_scope, test_user):
    score = Score(score=10.0, user_id=test_user.id)
    session_scope.add(score)
    session_scope.commit()
    assert score.timestamp is not None

def test_8_answer_image_path_nullable(session_scope):
    q = Question(text='Nullable test')
    session_scope.add(q)
    session_scope.flush()

    a_txt = Answer(text='Only Text', image_path=None, is_correct=True, question_id=q.id)
    session_scope.add(a_txt)
    session_scope.commit()
    assert a_txt.image_path is None


def test_9_duplicate_username_fails(session_scope):
    user1 = User(username='UniqueName')
    user2 = User(username='UniqueName')
    session_scope.add(user1)
    session_scope.add(user2)
    with pytest.raises(Exception):
        session_scope.commit()
    session_scope.rollback()


def test_10_delete_user_leaves_scores(session_scope):
    user = User(username='DeleteUser')
    session_scope.add(user)
    session_scope.flush()
    score = Score(score=50.0, user_id=user.id)
    session_scope.add(score)
    session_scope.commit()

    score_id = score.id
    user_id = user.id

    session_scope.delete(user)
    session_scope.commit()

    assert session_scope.query(User).filter_by(id=user_id).first() is None

    remaining_score = session_scope.query(Score).filter_by(id=score_id).first()
    assert remaining_score is not None
    assert remaining_score.user_id is None
