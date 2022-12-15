from flask import request
from flask_restful import Resource
from middleware import create_token, gen_password, strip_token, read_token, compare_password
from models.db import db
from models.user import User

class Register(Resource):
  def post(self):
    data = request.get_json()

    check_user = User.find_by_email(data['email'])
    if (check_user):
      return {'msg': 'Email already in use!'}, 400

    params = {
      'name': data['name'],
      'email': data['email'],
      'password': gen_password(data['password'])
    }

    user = User(**params)
    user.create()
    return user.json(), 201

class Login(Resource):
  def post(self):
    data = request.get_json()

    user = User.find_by_email(data['email'])
    if not user:
      return {'msg': 'Email or password are invalid!'}, 400

    check = compare_password(data['password'], user.password)

    if check:
      payload = user.json()
      token = create_token(payload)
      return {
        "user": payload,
        "token": token
      }
    else:
      return {'msg': 'Email or password are invalid!'}, 400

class CheckSession(Resource):
  def get(self):
    req = request
    token = strip_token(req)
    payload = read_token(token)
    return payload
