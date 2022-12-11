from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.db import db
from models.user import User
from models.routine import Routine
from models.day_exercise import DayExercise

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
      de = [d.json() for d in de_raw]

      dict = {
        **r.json(),
        "exercises": de
      }

      routines.append(dict)

      
    

    return {**user.json(), "routines": routines} 
