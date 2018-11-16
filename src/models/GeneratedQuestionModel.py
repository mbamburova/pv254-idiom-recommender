from . import db
from marshmallow import Schema, fields


class GeneratedQuestionModel(db.Model):
    __tablename__ = 'generated_questions'

    id = db.Column(db.Integer, primary_key=True)
    idiom_id = db.Column(db.Integer, db.ForeignKey('idioms.id'))
    answer_one_idiom_id = db.Column(db.Integer, nullable=False)
    answer_two_idiom_id = db.Column(db.Integer, nullable=False)
    answer_three_idiom_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.idiom_id = data.get('idiom_id')
        self.answer_one_idiom_id = data.get('answer_one_idiom_id')
        self.answer_two_idiom_id = data.get('answer_two_idiom_id')
        self.answer_three_idiom_id = data.get('answer_three_idiom_id')
        self.created_at = data.get('created_at')


class GeneratedQuestionSchema(Schema):
    idiom_id = fields.Integer(required = True)
    answer_one_idiom_id = fields.Integer(required=True)
    answer_two_idiom_id = fields.Integer(required=True)
    answer_three_idiom_id = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
