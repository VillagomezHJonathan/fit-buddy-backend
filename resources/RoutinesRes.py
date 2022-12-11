from flask import request
from flask_restful import Resource
from models.db import db
from models.routine import Routine

class RoutinesRes(Resource):
  def get(self):
    data = Routine.find_all()
    return [r.json() for r in data]

  def post(self):
    data = request.get_json()
    routine = Routine(**data)
    routine.create()
    return routine.json(), 201