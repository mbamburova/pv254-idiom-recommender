from http import HTTPStatus

from flask import json, Response, Blueprint

from src.models.RecommenderVersion import RecommenderVersion as Version
from src.models.UserAnswerModel import db
from ..models.UserModel import UserModel, UserSchema

# CONFIG
users_blueprint = Blueprint('users', __name__, url_prefix='/api/v1')

users_schema = UserSchema(many=True)
user_schema = UserSchema()


@users_blueprint.route('/all-users', methods=['GET'])
def get_all_users():
    users = UserModel.query.all()
    response = users_schema.dump(users)
    return custom_response(response, HTTPStatus.OK)


@users_blueprint.route('/new-user', methods=['GET'])
def get_new_user():
    user = UserModel({
        "version": choose_recommender_version()
    })

    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    response = user_schema.dump(user)
    return custom_response(response, HTTPStatus.OK)


@users_blueprint.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )


first_random = 10
replicated_versions = [Version.RR.value] * first_random + [Version.RT.value] * first_random + \
                      [Version.TR.value] * first_random + [Version.TT.value] * first_random
versions = [v.value for v in Version]
limit = 4 * first_random


def choose_recommender_version():
    rows = db.session.query(UserModel).count()
    if rows < limit:
        return replicated_versions[rows]
    else:
        return versions[rows % 4]
