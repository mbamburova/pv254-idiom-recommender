import datetime
import random

from random import shuffle
from sqlalchemy.sql.elements import or_
from datetime import datetime
from src.models import db
from src.models.IdiomModel import IdiomModel
from src.models.GeneratedQuestionModel import GeneratedQuestionModel


def generate_answers(idiom):
    samples = get_random_ids(idiom.id)
    random_idioms = IdiomModel.query.filter(or_(
        IdiomModel.id == samples[0],
        IdiomModel.id == samples[1]
    ))

    question_id = save_question_model(idiom.id, random_idioms)

    return {
        "question_id": question_id,
        "question": idiom.text,
        "answers": get_answer_list(idiom, random_idioms)
    }


def get_answer_list(idiom, random_idioms):
    answer_list = [{"answer_text": idiom.definition, "answer_id": idiom.id}]
    for _idiom in random_idioms:
        answer_list.append({"answer_text": _idiom.definition, "answer_id": _idiom.id})

    shuffle(answer_list)
    return answer_list


def get_random_ids(idiom_id):
    idioms = IdiomModel.query.all()
    idiom_ids = []
    for idiom in idioms:
        idiom_ids.append(idiom.id)

    random.shuffle(idiom_ids)
    rand_positions = random.sample(range(0, len(idioms) - 1), 2)

    samples = [idiom_ids[rand_positions[0]], idiom_ids[rand_positions[1]]]
    while idiom_id in samples:
        rand_positions = random.sample(range(0, len(idioms) - 1), 2)
        samples = [idiom_ids[rand_positions[0]], idiom_ids[rand_positions[1]]]

    return samples


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
