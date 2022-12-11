from flask import request
from flask_restful import Resource
from models.db import db
from models.exercise import Exercise

class Exercises(Resource):
  def get(self):
    data = Exercise.find_all()
    return [e.json() for e in data]

  def post(self):
    data = request.get_json()
    exercise = Exercise(**data)
    exercise.create()
    return exercise.json(), 201