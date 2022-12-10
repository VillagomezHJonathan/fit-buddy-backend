from datetime import datetime
from models.db import db

class Routine(db.Model):
  __tablename__ = 'routines'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  created_at = db.Column(db.DateTime, default = datetime.now, nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now, nullable = False, onupdate = datetime.now())
  user = db.relationship('User', back_populates = 'routines')

  def __init__(self, name):
    self.name = name

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return Routine.query.find()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description = f'Routine with id of {id} is not available')