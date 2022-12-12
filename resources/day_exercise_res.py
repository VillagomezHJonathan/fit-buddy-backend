from flask import request
from flask_restful import Resource
from models.db import db
from models.day_exercise import DayExercise

class DayExercises(Resource):
  def get(self):
    data = DayExercise.find_all()
    return [de.json() for de in data]

  def post(self):
    data = request.get_json()
    day_exercise = DayExercise(**data)
    day_exercise.create()
    return day_exercise.json(), 201