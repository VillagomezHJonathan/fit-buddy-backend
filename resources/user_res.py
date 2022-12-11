from flask import request
from flask_restful import Resource
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
    data = User.find_by_id(id)
    return data.json()
