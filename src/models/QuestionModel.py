from . import db
from marshmallow import Schema, fields


class QuestionModel(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    text = db.Column(db.String, nullable=False)
    answers = db.Column(db.JSON, nullable=False)
    right_answer = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime)
    idiom_id = db.Column(db.Integer, db.ForeignKey('idioms.id'))

    def __init__(self, data):
        self.text = data.get('text')
        self.type = data.get('type')
        self.answers = data.get('answers')
        self.created_at = data.get('created_at')
        self.right_answer = data.get('right_answer')
        self.idiom_id = data.get('idiom_id')

    def create_question(question):
        db.session.add(question)
        db.session.commit()

    def delete_question(question):
        db.session.add(question)
        db.session.commit()

    def get_all():
        return db.session.query(QuestionModel).all()

    def get_question_by_id(question_id):
        return db.session.query(QuestionModel).get(question_id)

class QuestionSchema(Schema):
    type = fields.Integer(required=True)
    text = fields.String(required=True)
    answers = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
    right_answer = fields.String(required = True)
    idiom_id = fields.Integer(required = True)
