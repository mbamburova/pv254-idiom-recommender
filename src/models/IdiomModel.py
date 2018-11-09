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

    def create_idiom(idiom):
        db.session.add(idiom)
        db.session.commit()

    def delete_idiom(idiom):
        db.session.add(idiom)
        db.session.commit()

    def get_all():
        return db.session.query(IdiomModel).all()

    def get_idiom_by_id(idiom_id):
        return db.session.query(IdiomModel).get(idiom_id)

    def get_idiom_by_name(idiom_name):
        return db.session.query(IdiomModel).filter_by(text=idiom_name).first()


class IdiomSchema(Schema):
    text = fields.String(required=True)
    definition = fields.String(required=True)
    example = fields.String(required=True)
    frequency = fields.Integer()
    category = fields.String(required=True)
