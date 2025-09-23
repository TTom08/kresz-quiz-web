import random
from mock_data import questions, leaderboard

MAX_POINTS = 100
TIME_LIMIT = 40

def choose_questions(n=5):

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of questions must be a positive integer")
    if n > len(questions):
        raise ValueError("Requested number of questions exceeds available questions")
    return random.sample(questions, n)

def calculate_score(elapsed_time, correct=True):

    if not isinstance(elapsed_time, (int, float)) or elapsed_time < 0:
        raise ValueError("Elapsed time must be a non-negative number")
    if not isinstance(correct, bool):
        raise ValueError("Correct must be a boolean value")
    if not correct or elapsed_time >= TIME_LIMIT:
        return 0
    score = MAX_POINTS * ((TIME_LIMIT - elapsed_time) / TIME_LIMIT)
    return round(score, 2)

def add_score(username, score):

    if not username or not isinstance(username, str):
        raise ValueError("Username must be a non-empty string")
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number")
    if score < 0 or score > MAX_POINTS:
        raise ValueError(f"Score must be between 0 and {MAX_POINTS}")
    leaderboard.append({"username": username, "score": score})

def get_leaderboard():

    if not isinstance(leaderboard, list):
        raise ValueError("Leaderboard must be a list")
       
    if not leaderboard:
        return []
    return sorted(leaderboard, key=lambda x: x["score"], reverse=True)

