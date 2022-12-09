from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.exercise import Exercise
from models.muscle import Muscle

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/fitbuddy_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)


muscles = [
('trapezius'),
'deltoid',
'pectoralis major',
'triceps',
'biceps',
'abdominal',
'serratus anterior',
'latissimus dorsi',
'external oblique',
'brachioradialis',
'finger extensors',
'finger flexors',
'quadriceps',
'hamstrings',
'sartorius',
'abductors',
'gastrocnemius',
'tibialis anterior',
'soleus',
'gluteus medius',
'gluteus maximus'
]