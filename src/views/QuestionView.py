from flask import request, json, Response, Blueprint
from ..models.QuestionModel import QuestionModel, QuestionSchema
from datetime import datetime

# CONFIG
questions_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1/questions')

questions_schema = QuestionSchema(many=True)
question_schema = QuestionSchema()

# ROUTES
@questions_blueprint.route('/get_new_question', methods=['GET'])
def get_new_question():
    q = {"type": 1,
         "text": "QWERTY",
         "explanation": "TROLOLO",
         "answers": None,
         "created_at": datetime.utcnow()
         }
    question = QuestionModel(q)
    response = question_schema.dump(question)
    return custom_response(response, 200)

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
