from datetime import datetime

from flask import json, Response, Blueprint

from ..models.GeneratedQuestionModel import GeneratedQuestionModel, GeneratedQuestionSchema

# CONFIG
generated_questions_blueprint = Blueprint('generated_questions', __name__, url_prefix='/api/v1/generated_questions')

generated_questions_schema = GeneratedQuestionSchema(many=True)
generated_question_schema = GeneratedQuestionSchema()


# ROUTES
@generated_questions_blueprint.route('/', methods=['GET'])
def get_all_answers():
    user_answers = GeneratedQuestionModel.query.all()
    response = generated_question_schema.dump(user_answers)
    return custom_response(response, 200)


@generated_questions_blueprint.route('/get_new_question', methods=['GET'])
def get_new_question():
    q = {"type": 1,
         "text": "QWERTY",
         "explanation": "TROLOLO",
         "answers": None,
         "created_at": datetime.utcnow()
         }
    question = GeneratedQuestionModel(q)
    response = generated_question_schema.dump(question)
    return custom_response(response, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
