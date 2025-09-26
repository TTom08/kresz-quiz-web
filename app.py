from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kresz:kresz@localhost:5432/kresz_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Question


@app.route('/')
def home():
    questions = Question.query.all()
    return render_template('home.html', questions=questions)


@app.route('/quiz', methods=['POST'])
def quiz():
    username = request.form.get('username')

    if username:
        username = username.strip()

    if not username:
        return redirect(url_for('home'))

    return render_template('quiz.html', username=username)

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

from kresz_quiz.routes import quiz_bp
app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
