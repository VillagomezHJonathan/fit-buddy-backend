from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.db import db
from models.routine import Routine
from models.day import Day
from models.exercise import Exercise

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
    days_exercises = [de.json() for de in routine.days_exercises]
    return {**routine.json(), "exercises": days_exercises} 

class UserRoutine(Resource):
  def get(self, user_id):
    routine = Routine.query.options(joinedload('days_exercises')).filter_by(user_id=user_id).first()

    exercises = []
    for de in routine.days_exercises:
      day = Day.query.filter_by(id=de.day_id).first()
      exercise = Exercise.query.filter_by(id=de.exercise_id).first()
      dict = {
        "day_name": day.name,
        "exercise_name": exercise.name,
				"type": exercise.type,
				"muscle": exercise.muscle,
				"equipment": exercise.equipment,
				"instructions": exercise.instructions,
				"sets": exercise.sets,
				"reps": exercise.reps,
				"duration": exercise.duration
      }

      exercises.append(dict)
    
    if routine:
      return {**routine.json(), 'exercises': exercises}

    return 404