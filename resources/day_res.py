from flask import request
from flask_restful import Resource
from models.db import db
from models.day import Day

class Days(Resource):
  def get(self):
    data = Day.find_all()
    return [d.json() for d in data]

  def post(self):
    data = request.get_json()
    day = Day(**data)
    day.create()
    return day.json(), 201

class DayName(Resource):
  def get(self, name):
    day = Day.query.filter_by(name=name).first()
    return day.json(), 201

