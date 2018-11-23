from datetime import datetime
from src.models import db

from src.models.GeneratedQuestionModel import GeneratedQuestionModel


def generate_answers(idiom):
    return None


def save_question_model(idiom_id, random_idioms):
    question_model = GeneratedQuestionModel({
        "idiom_id": idiom_id,
        "answer_one_idiom_id": idiom_id,
        "answer_two_idiom_id": random_idioms[0].id,
        "answer_three_idiom_id": random_idioms[1].id,
        "created_at": datetime.utcnow()
    })

    db.session.add(question_model)
    db.session.commit()
    db.session.refresh(question_model)

    return question_model.id