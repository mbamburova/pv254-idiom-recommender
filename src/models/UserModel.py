from marshmallow import fields, Schema
from . import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.id = data.get('id')
        self.version = data.get('version')


class UserSchema(Schema):
    id = fields.Integer(required=True)
