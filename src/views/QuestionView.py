from flask import request, json, Response, Blueprint
from ..models.QuestionModel import QuestionModel, QuestionSchema
import datetime

question_api = Blueprint('questions', __name__)
question_schema = QuestionSchema()


@question_api.route('/', methods=['GET'])
def get_new_question():
    q = {"id": "1",
         "type": "1",
         "text": "QWERTY",
         "explanation": "Trolololo",
         "answers": None,
         "created_at": datetime.datetime.utcnow(),
         }
    question = QuestionModel(q)
    return custom_response(question, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
