from . import db
from marshmallow import Schema, fields


class AnswerModel(db.Model):
    __tablename__ = 'idioms'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    correctly_answered = db.Column(db.Boolean, nullable=False)
    version  db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.question_id = data.get('question_id')
        self.user_id = data.get('user_id')
        self.example = data.get('example')
        self.version = data.get('version')

    def create_answer(answer):
        db.session.add(answer)
        db.session.commit()

    def delete_answer(answer):
        db.session.delete(answer)
        db.session.commit()

    def get_all():
        return db.session.query(AnswerModel).all()

    def get_answer_by_id(answer_id):
        return db.session.query(AnswerModel).get(answer_id)


class AnswerSchema(Schema):
    question_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    correctly_answered = fields.Boolean(required=True)
    version = fields.Integer(required=True)
