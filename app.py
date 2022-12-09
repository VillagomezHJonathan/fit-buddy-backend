from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.exercise import Exercise
from models.muscle import Muscle
from resources.Muscle import MuscleList

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/fitbuddy_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(MuscleList, '/muscles')

if __name__ == '__main__':
    app.run(debug=True)
