from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kresz:kresz@localhost:5432/kresz_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Ide importáld a models-t, miután a 'db' objektum létrejött.
import models
from models import Question, Answer

# A route-ok maradjanak itt
@app.route('/')
def home():
    questions = Question.query.all()
    return render_template('home.html', questions=questions)