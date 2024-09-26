
from restdemo import db
from sqlalchemy.orm import relationship
from restdemo.model.base import Base

class Users(Base):
    u_id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    gender = db.Column(db.String(1))
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    activity_level = db.Column(db.Float)
    daily_info = relationship("Dailyinfo")

    def __repr__(self):
        return f"id: {self.u_id}, username: {self.name}"

    @staticmethod
    def query_by_username(username):
        return db.session.query(Users).filter(Users.username == username).first()
  
    @staticmethod
    def query_by_id(id):
        return db.session.query(Users).filter(Users.u_id == id).first()
    
    @staticmethod
    def get_metadata():
        return  [column.name  for column in Users.__table__.columns]

