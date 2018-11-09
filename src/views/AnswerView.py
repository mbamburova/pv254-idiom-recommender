from flask import request, json, Response, Blueprint
from ..models.AnswerModel import AnswerModel, AnswerSchema

# CONFIG
answers_blueprint = Blueprint('answers', __name__, url_prefix='/api/v1/answers')

answers_schema = AnswerSchema(many=True)
answer_schema = AnswerSchema()

# ROUTES
@answers_blueprint.route('/', methods=['GET'])
def get_all_answers():
    answers = AnswerModel.get_all()
    response = answers_schema.dump(answers)
    return custom_response(response, 200)

@answers_blueprint.route('/<int:answer_id>', methods=['GET'])
def get_answer_by_id(answer_id):
    answer = AnswerModel.get_answer_by_id(answer_id)
    response = answer_schema.dump(answer)
    return custom_response(response, 200)

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res.data),
        status=status_code
    )
