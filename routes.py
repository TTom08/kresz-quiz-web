from flask import render_template
from app import app
from models import Question, Answer

@app.route('/')
def home():
    questions = Question.query.all()
    return render_template('home.html', questions=questions)