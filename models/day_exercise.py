from datetime import datetime
from models.db import db

class DayExercise(db.Model):
  __tablename__ = 'days_exercises'
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default = datetime.now, nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now, nullable = False, onupdate = datetime.now())

  