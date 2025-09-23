import random
from mock_data import questions, leaderboard

MAX_POINTS = 100
TIME_LIMIT = 40

def choose_questions(n=5):

    return random.sample(questions, min(n, len(questions)))

def calculate_score(elapsed_time, correct=True):

    if not correct or elapsed_time >= TIME_LIMIT:
        return 0
    score = MAX_POINTS * ((TIME_LIMIT - elapsed_time) / TIME_LIMIT)
    return round(score, 2)

def add_score(username, score):

    leaderboard.append({"username": username, "score": score})

def get_leaderboard():

    return sorted(leaderboard, key=lambda x: x["score"], reverse=True)
