from flask import json, Response, Blueprint
from src.services import UserAnswerService

# CONFIG
user_answers_blueprint = Blueprint('user_answers', __name__, url_prefix='/api/v1/answer')


# ROUTES
@user_answers_blueprint.route('/<int:user_id>/<int:question_id>/<int:answer_id>', methods=['GET'])
def get_answer_by_id(user_id, question_id, answer_id):
    if UserAnswerService.already_answered(question_id) is not None:
        return custom_response(
            {"error": "Bad request - question is already answered"},
            400
        )

    return custom_response(
        UserAnswerService.save_answer(user_id, question_id, answer_id),
        200
    )

@user_answers_blueprint.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
