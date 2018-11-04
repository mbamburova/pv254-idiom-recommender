from marshmallow import fields, Schema
from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_users(self):
        return User.query.all()
