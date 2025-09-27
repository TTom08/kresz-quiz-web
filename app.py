from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import db  # Import db from models

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kresz:kresz@localhost:5432/kresz_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    # Import inside function to avoid circular imports
    from models import Question
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
    from models import Score, User  # Import inside function
    # Add leaderboard logic here
    return render_template("leaderboard.html")

# Import routes at the end to avoid circular imports
try:
    from kresz_quiz.routes import quiz_bp
    app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
except ImportError:
    print("Quiz blueprint not found, continuing without API routes")