from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.db import db
from models.user import User

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
    user = User.query.options(joinedload('routines')).filter_by(id=id).first()
    routines = [r.json() for r in user.routines]
    return {**user.json(), "routines": routines} 
