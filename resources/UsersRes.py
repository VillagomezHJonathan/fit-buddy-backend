from flask import request
from flask_restful import Resource
from models.db import db
from models.user import User

class UsersRes(Resource):
  def get(self):
    data = User.find_all()
    return [u.json() for u in data]

  def post(self):
    data = request.get_json()
    user = User(**data)
    user.create()
    return user.json(), 201
