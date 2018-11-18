from . import db
from marshmallow import Schema, fields


class IdiomModel(db.Model):
    __tablename__ = 'idioms'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False, unique=True)
    definition = db.Column(db.String, nullable=False)
    example = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    frequency = db.Column(db.Integer)

    def __init__(self, data):
        self.text = data.get('text')
        self.definition = data.get('explanation')
        self.example = data.get('example')
        self.frequency = data.get('frequency')
        self.category = data.get('category')


class IdiomSchema(Schema):
    id = fields.Integer(required=True)
    text = fields.String(required=True)
    definition = fields.String(required=True)
    example = fields.String(required=True)
    frequency = fields.Integer()
    category = fields.String(required=True)
