from restdemo import db
from sqlalchemy import ForeignKey 
from restdemo.model.base import Base

class Dailyinfo(Base):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.String(64), ForeignKey('users.u_id'))
    date = db.Column(db.String(64))
    time = db.Column(db.String(64))
    food_name = db.Column(db.String(64))
    food_calories = db.Column(db.Float)
    exercise_name = db.Column(db.String(64))
    exercise_duration = db.Column(db.Float)
    weight_target = db.Column(db.Float)
    bmr_target = db.Column(db.Float)
    calories_burned = db.Column(db.Float)


    def __repr__(self):
        return f"uid: {self.u_id} , food name: {self.food_name}"   
        
    def as_dict(self):
         t = {c.name: getattr(self, c.name) for c in self.__table__.columns  if c.name not in ('id', 'u_id')}
         return t
    