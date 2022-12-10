from datetime import datetime
from models.db import db

class DayExercise(db.Model):
  __tablename__ = 'days_exercises'
  id = db.Column(db.Integer, primary_key=True)
  routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
  day_id = db.Column(db.Integer, db.ForeignKey('days.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False, onupdate=datetime.now())
  routines = db.relationship('Routine', back_populates='days_exercises')
  # exercise = db.relationship('Exercise', back_populates='exercise')
  # day = db.relationship('Day', back_populates='day')

  def __init__(self, routine_id, exercise_id, day_id):
    self.routine_id = routine_id
    self.exercise_id = exercise_id
    self.day_id = day_id

  def json(self):
    return {
      "id": self.id,
      "routine_id": self.routine_id,
      "exercise_id": self.exercise_id,
      "day_id": self.day_id,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return DayExercise.query.find()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description = f'Day exercises with id of {id} is not available')

