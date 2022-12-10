from datetime import datetime
from models.db import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  email = db.Column(db.String(100), nullable = False)
  password = db.Column(db.String(100), nullable = False)
  created_at = db.Column(db.DateTime, default = datetime.now, nullable = False)
  updated_at = db.Column(db.DateTime, default = datetime.now, nullable = False, onupdate = datetime.now())
  tasks = db.relationship('Task', cascade = 'all', back_populates = 'users')

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "password": self.password,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return User.query.all()

  @classmethod
  def find_by_id(cls, id):
    return db.get_or_404(cls, id, description = f'Exercise with id of {id} is not available')