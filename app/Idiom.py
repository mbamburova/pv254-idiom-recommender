from flask import request
from flask_restful import Resource
from Model import db, Idiom, IdiomSchema

idioms_schema = IdiomSchema(many=True)
idiom_schema = IdiomSchema()


class IdiomApi(Resource):
    def get(self):
        idioms = Idiom.query.all()
        idioms = idioms_schema.dump(idioms).data
        return {'status': 'success', 'data': idioms}, 200
