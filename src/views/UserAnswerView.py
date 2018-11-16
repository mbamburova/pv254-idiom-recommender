from flask import json, Response, Blueprint

from ..models.UserAnswerModel import UserAnswerModel, UserAnswerSchema

# CONFIG
user_answers_blueprint = Blueprint('user_answers', __name__, url_prefix='/api/v1/user_answers')

user_answers_schema = UserAnswerSchema(many=True)
user_answer_schema = UserAnswerSchema()


# ROUTES
@user_answers_blueprint.route('/', methods=['GET'])
def get_all_answers():
    user_answers = UserAnswerModel.query.all()
    response = user_answers_schema.dump(user_answers)
    return custom_response(response, 200)


@user_answers_blueprint.route('/<int:answer_id>', methods=['GET'])
def get_answer_by_id(answer_id):
    answer = UserAnswerModel.get_answer_by_id(answer_id)
    response = user_answer_schema.dump(answer)
    return custom_response(response, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
