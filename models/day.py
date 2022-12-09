from datetime import datetime
from models.db import db

class Day(db.Model):
  __tablename__ = 'days'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), nullable = False)
  created_at = db.Column(db.DateTime, default = datetime.now, nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now, nullable = False, onupdate = datetime.now())

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
    return Day.query.find()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description = f'Exercise with id of {id} is not available')

  