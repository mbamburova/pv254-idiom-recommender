from flask import json, Response, Blueprint
from src.models.UserModel import UserModel
from ..models.GeneratedQuestionModel import GeneratedQuestionSchema
from src.services import RandomQuestionGenerator, TrainedQuestionGenerator, RandomAnswersGenerator, TrainedAnswersGenerator

# CONFIG
generated_questions_blueprint = Blueprint('question', __name__, url_prefix='/api/v1/question')

generated_questions_schema = GeneratedQuestionSchema(many=True)

# Version | Question  | Answers
# 1       | random    | random
# 2       | nerandom  | random
# 3       | random    | nerandom
# 4       | nerandom  | nerandom


# ROUTES
@generated_questions_blueprint.route('/<int:user_id>', methods=['GET'])
def get_new_question(user_id):
    user = UserModel.query.get(user_id)

    if user.version == 1:
        random_question = RandomQuestionGenerator.generate_question()
        return custom_response(
            RandomAnswersGenerator.generate_answers(random_question),
            200
        )

    elif user.version == 2:
        trained_question = TrainedQuestionGenerator.generate_question()
        return custom_response(
            RandomAnswersGenerator.generate_answers(trained_question),
            200
        )

    elif user.version == 3:
        random_question = RandomQuestionGenerator.generate_question()
        return custom_response(
            TrainedAnswersGenerator.generate_answers(random_question),
            200
        )

    elif user.version == 4:
        trained_question = TrainedQuestionGenerator.generate_question()
        return custom_response(
            TrainedAnswersGenerator.generate_answers(trained_question),
            200
        )
    else:
        custom_response({"error": "unsupported operation exception"}, 400)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
