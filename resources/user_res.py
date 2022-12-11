from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.db import db
from models.user import User
from models.routine import Routine
from models.day_exercise import DayExercise
from models.day import Day
from models.exercise import Exercise

class Users(Resource):
  def get(self):
    data = User.find_all()
    return [u.json() for u in data]

  def post(self):
    data = request.get_json()
    user = User(**data)
    user.create()
    return user.json(), 201

class SingleUser(Resource):
  def get(self, id):
    user = User.query.filter_by(id=id).first()

    routines_raw = Routine.query.filter_by(user_id=id).all()

    routines = []
    for r in routines_raw:
      de_raw = DayExercise.query.filter_by(routine_id=r.id).all()
      exercises = []
      for de in de_raw:
        day = Day.query.filter_by(id=de.day_id).first()
        exercise = Exercise.query.filter_by(id=de.exercise_id).first()
        dict = {
          **de.json(),
          "day": {**day.json()},
          "exercise": {**exercise.json()}
        }

        exercises.append(dict)


      dict = {
        **r.json(),
        "exercises": exercises
      }

      routines.append(dict)

    return {**user.json(), "routines": routines} 
