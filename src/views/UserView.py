from flask import json, Response, Blueprint

from ..models.UserModel import UserModel, UserSchema

# CONFIG
users_blueprint = Blueprint('users', __name__, url_prefix='/api/v1/users')

users_schema = UserSchema(many=True)
user_schema = UserSchema()


# ROUTES
@users_blueprint.route('/', methods=['GET'])
def get_all_users():
    users = UserModel.query.all()
    response = users_schema.dump(users)
    return custom_response(response, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
