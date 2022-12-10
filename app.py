from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.exercise import Exercise
from models.user import User
from models.day import Day
from models.routine import Routine
from models.day_exercise import DayExercise
from resources.UsersRes import UsersRes
from resources.DaysRes import DaysRes

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/fitbuddy_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(UsersRes, '/users')
api.add_resource(DaysRes, '/days')

if __name__ == '__main__':
    app.run(debug=True)
