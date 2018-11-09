from flask import request, json, Response, Blueprint, redirect
from ..models.IdiomModel import IdiomModel, IdiomSchema

# CONFIG
idioms_blueprint = Blueprint('idioms', __name__, url_prefix='/api/v1/idioms')

idioms_schema = IdiomSchema(many=True)
idiom_schema = IdiomSchema()

# ROUTES
@idioms_blueprint.route('/', methods=['GET'])
def get_all_idioms():
    idioms = IdiomModel.get_all()
    response = idioms_schema.dump(idioms)
    return custom_response(response, 200)

@idioms_blueprint.route('/<int:idiom_id>', methods=['GET'])
def get_idiom_by_id(idiom_id):
    idiom = IdiomModel.get_idiom_by_id(idiom_id)
    response = idiom_schema.dump(idiom)
    return custom_response(response, 200)

@idioms_blueprint.route('/find/<idiom_name>', methods=['GET'])
def get_idiom_by_name(idiom_name):
    idiom = IdiomModel.get_idiom_by_name(idiom_name)
    response = idiom_schema.dump(idiom)
    return custom_response(response, 200)

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
