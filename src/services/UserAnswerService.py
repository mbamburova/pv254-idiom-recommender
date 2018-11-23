from src.models import db, GeneratedQuestionModel
from src.models.UserAnswerModel import UserAnswerModel
from ..models.GeneratedQuestionModel import GeneratedQuestionModel


def already_answered(question_id):
    return UserAnswerModel.query.get(question_id)


def save_answer(user_id, question_id, answer_id):
    generated_question = GeneratedQuestionModel.query.get(question_id)

    user_answer_model = UserAnswerModel({
        "generated_question_id": question_id,
        "user_id": user_id,
        "is_answered_correctly": generated_question.idiom_id == answer_id,
        "user_answer_idiom_id": answer_id
    })

    db.session.add(user_answer_model)
    db.session.commit()

    return {
        "correct_answer_id": generated_question.idiom_id
    }
