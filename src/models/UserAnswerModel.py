from . import db
from marshmallow import Schema, fields


class UserAnswerModel(db.Model):
    __tablename__ = 'user_answers'

    id = db.Column(db.Integer, primary_key=True)
    generated_question_id = db.Column(db.Integer, db.ForeignKey('generated_questions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_answered_correctly = db.Column(db.Boolean, nullable=False)
    user_answer_idiom_id = db.Column(db.Integer, db.ForeignKey('idioms.id'))

    def __init__(self, data):
        self.generated_question_id = data.get('generated_question_id')
        self.user_id = data.get('user_id')
        self.is_answered_correctly = data.get('is_answered_correctly')
        self.user_answer_idiom_id = data.get('user_answer_idiom_id')


class UserAnswerSchema(Schema):
    generated_question_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    is_correctly_answered = fields.Boolean(required=True)
    user_answer_idiom_id = fields.Integer(required=True)
