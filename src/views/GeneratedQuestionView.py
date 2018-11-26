from http import HTTPStatus

from flask import json, Response, Blueprint

from src.models.RecommenderVersion import RecommenderVersion
from src.models.UserModel import UserModel
from src.services import RandomQuestionGenerator, TrainedQuestionGenerator, RandomAnswersGenerator, \
    TrainedAnswersGenerator
from ..models.GeneratedQuestionModel import GeneratedQuestionSchema

# CONFIG
generated_questions_blueprint = Blueprint('question', __name__, url_prefix='/api/v1/question')

generated_questions_schema = GeneratedQuestionSchema(many=True)


# ROUTES
@generated_questions_blueprint.route('/<int:user_id>', methods=['GET'])
def get_new_question(user_id):
    user = UserModel.query.get(user_id)

    if user.version == RecommenderVersion.RR.value:
        random_question = RandomQuestionGenerator.generate_question()
        return custom_response(
            RandomAnswersGenerator.generate_answers(random_question),
            HTTPStatus.OK
        )

    elif user.version == RecommenderVersion.NR.value:
        trained_question = TrainedQuestionGenerator.generate_question()
        return custom_response(
            RandomAnswersGenerator.generate_answers(trained_question),
            HTTPStatus.OK
        )

    elif user.version == RecommenderVersion.RN.value:
        random_question = RandomQuestionGenerator.generate_question()
        return custom_response(
            TrainedAnswersGenerator.generate_answers(random_question),
            HTTPStatus.OK
        )

    elif user.version == RecommenderVersion.NN.value:
        trained_question = TrainedQuestionGenerator.generate_question()
        return custom_response(
            TrainedAnswersGenerator.generate_answers(trained_question),
            HTTPStatus.OK
        )
    else:
        custom_response({"error": "unsupported operation exception"}, 400)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
