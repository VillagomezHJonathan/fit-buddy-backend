from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.db import db
from models.routine import Routine

class Routines(Resource):
  def get(self):
    data = Routine.find_all()
    return [r.json() for r in data]

  def post(self):
    data = request.get_json()
    routine = Routine(**data)
    routine.create()
    return routine.json(), 201

class SingleRoutine(Resource):
  def get(self, id):
    routine = Routine.query.options(joinedload('days_exercises')).filter_by(id=id).first()
    days_exercises = [r.json() for r in routine.days_exercises]
    return {**routine.json(), "exercises": days_exercises} 