from . import db
from marshmallow import Schema, fields


class IdiomModel(db.Model):
    __tablename__ = 'idioms'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    explanation = db.Column(db.String)
    examples = db.Column(db.JSON, nullable=True)

    def __init__(self, data):
        self.text = data.get('text')
        self.explanation = data.get('explanation')
        self.examples = data.get('examples')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return IdiomModel.query.all()

    @staticmethod
    def get_idiom_by_id(idiom_id):
        return IdiomModel.query.get(idiom_id)


class QuestionSchema(Schema):
    id = fields.Integer(required=True)
    text = fields.String(required=True)
    explanation = fields.String(required=True)
    examples = fields.String()
