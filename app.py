from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import db


def create_app(test_config=None):
    app = Flask(__name__, static_folder='static')

    if test_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kresz:kresz@localhost:5432/kresz_db"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config.update(test_config)
    db.init_app(app)

    migrate = Migrate(app, db)

    @app.route('/')
    def home():
        from models import Question
        questions = Question.query.all()
        return render_template('home.html', questions=questions)

    @app.route('/quiz', methods=['POST'])
    def quiz():
        username = request.form.get('username')
        if username: username = username.strip()
        if not username: return redirect(url_for('home'))
        return render_template('quiz.html', username=username)

    @app.route("/result")
    def result():
        return render_template("result.html")

    @app.route("/leaderboard")
    def leaderboard():
        return render_template("leaderboard.html")

    # Import routes at the end to avoid circular imports
    try:
        from kresz_quiz.routes import quiz_bp
        app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
    except ImportError:
        print("Quiz blueprint not found, continuing without API routes")

    return app
app = create_app()
