from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models.db import db
from models.exercise import Exercise
from models.user import User
from models.day import Day
from models.routine import Routine
from models.day_exercise import DayExercise
from resources.auth import Register, Login, CheckSession
from resources.user_res import Users, SingleUser
from resources.day_res import Days, DayName
from resources.routine_res import Routines, SingleRoutine, UserRoutine
from resources.exercise_res import Exercises
from resources.day_exercise_res import DayExercises
from middleware import strip_token, read_token

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace(
        "://", "ql://", 1)
    app.config['SQLALCHEMY_ECHO'] = False
    app.env = 'production'
else:
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/fitbuddy_db"
    app.config['SQLALCHEMY_ECHO'] = True


db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Register, '/auth/register')
api.add_resource(Login, '/auth/login')
api.add_resource(CheckSession, '/auth/session')

api.add_resource(SingleUser, '/api/users/<int:id>')
api.add_resource(Users, '/api/users')

api.add_resource(DayName, '/api/days/<string:name>')
api.add_resource(Days, '/api/days')

api.add_resource(UserRoutine, '/api/routines/<int:user_id>')
api.add_resource(Routines, '/api/routines')

api.add_resource(Exercises, '/api/exercises')

api.add_resource(DayExercises, '/api/days-exercises')

if __name__ == '__main__':
    app.run()
