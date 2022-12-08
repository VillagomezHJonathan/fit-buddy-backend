from datetime import datetime
from models.db import db

class Exercise(db.Model):
  __tablename__ = 'excercises'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  created_at = db.Column(db.DateTime, default = datetime.now(), nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now(), nullable = False, onupdate = datetime.now())

  def __init__(self, name):
    self.name = name