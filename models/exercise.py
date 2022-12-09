from datetime import datetime
from models.db import db

class Exercise(db.Model):
  __tablename__ = 'excercises'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  type = db.Column(db.string(80), nullable = False)
  sets = db.Column(db.Integer)
  reps = db.Column(db.Integer)
  duration = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, default = datetime.now(), nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now(), nullable = False, onupdate = datetime.now())

  def __init__(self, name):
    self.name = name

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "type": self.type,
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
    return cls.query.all()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')




