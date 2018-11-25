from http import HTTPStatus

from flask import json, Response, Blueprint

from src.models import db
from src.models.RecommenderVersion import RecommenderVersion
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


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )


def choose_recommender_version():
    # TODO: add logic for choosing rec version
    return RecommenderVersion.RR.value
