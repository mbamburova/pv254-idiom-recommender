from . import db
from marshmallow import Schema, fields


class QuestionModel(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    text = db.Column(db.String, nullable=False)
    explanation = db.Column(db.String)
    answers = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime)

    idiom_id = db.relationship('Idiom', backref='questions',)

    def __init__(self, data):
        self.text = data.get('text')
        self.type = data.get('type')
        self.explanation = data.get('explanation')
        self.answers = data.get('answers')

    def save(self):
        db.session.add(self)
        db.session.commit()


class QuestionSchema(Schema):
    id = fields.Integer(required=True)
    type = fields.Integer(required=True)
    text = fields.String(required=True)
    explanation = fields.String()
    answers = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
