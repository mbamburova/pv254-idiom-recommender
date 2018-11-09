from marshmallow import fields, Schema
from . import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, data):
        self.id = data.get('id')


    def create_user(user):
        db.session.add(user)
        db.session.commit()

    def delete_user(user):
        db.session.add(user)
        db.session.commit()

    def get_all():
        return db.session.query(UserModel).all()

    def get_user_by_id(user_id):
        return db.session.query(UserModel).get(user_id)

class UserSchema(Schema):
    id = fields.Integer(required=True)
