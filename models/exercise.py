from datetime import datetime
from models.db import db

class Exercise(db.Model):
  __tablename__ = 'exercises'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  type = db.Column(db.String(80), nullable = False)
  muscle = db.Column(db.String(80), nullable = False)
  equipment = db.Column(db.String(80), nullable = False)
  instructions = db.Column(db.String(255), nullable = False)
  sets = db.Column(db.Integer)
  reps = db.Column(db.Integer)
  duration = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, default = datetime.now, nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now, nullable = False, onupdate = datetime.now())
  day_exercises = db.relationship('DayExercise', back_populates='exercises')

  def __init__(self, name, type, muscle, equipment, instructions, sets, reps, duration):
    self.name = name
    self.type = type
    self.muscle = muscle
    self.equipment = equipment
    self.instructions = instructions
    self.sets = sets
    self.reps = reps
    self.duration = duration

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "type": self.type,
      "muscle": self.muscle,
      "equipment": self.equipment,
      "instructions": self.instructions,
      "sets": self.sets,
      "reps": self.reps,
      "duration": self.duration,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return Exercise.query.all()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description = f'Exercise with id of {id} is not available')



