from flask import request
from flask_restful import Resource
from models.muscle import Muscle
from models.db import db


class MuscleList(Resource):
  def get(self):
    data = Muscle.find_all()
    result = [muscle.json() for muscle in data]
    return result

  def post(self):
    data = request.get_json()
    muscle = Muscle(**data)
    muscle.create()
    return muscle.json(), 201
