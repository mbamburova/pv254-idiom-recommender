import pickle
from datetime import datetime

import os

from sqlalchemy import or_
from src.models.IdiomModel import IdiomModel
from src.models import db
from src.models.GeneratedQuestionModel import GeneratedQuestionModel
from src.models.UserAnswerModel import UserAnswerModel

MODEL_WEIGHT = 1000.0
SIMILARITY_UPPER_BOUND = 0.35585
MY_PATH = os.path.dirname(os.path.abspath(__file__))

matrix_path = os.path.join(MY_PATH, 'final_matrix.pkl')
sim_matrix = pickle.load(open(matrix_path, 'rb'))

def generate_answers(idiom):
    same_categories = get_same_category_idioms(idiom)
    similar = get_similar_idioms(idiom)
    mistaken = get_incorrectly_answered_idioms(idiom)

    summed_weights_idioms = {}
    all_idioms = set(similar.keys()).union(set(same_categories.keys())).union(set(mistaken.keys()))

    for i in all_idioms:
        w1 = similar.get(i, 0.0)
        w2 = same_categories.get(i, 0.0)
        w3 = mistaken.get(i, 0.0)

        summed_weights_idioms[i] = w1 + w2 + w3

    generated_answer_id1 =  max(summed_weights_idioms, key=summed_weights_idioms.get)
    summed_weights_idioms.pop(generated_answer_id1)
    generated_answer_id2 = max(summed_weights_idioms, key=summed_weights_idioms.get)

    random_idioms = IdiomModel.query.filter(or_(
        IdiomModel.id == generated_answer_id1,
        IdiomModel.id == generated_answer_id2
    ))

    question_id = save_question_model(idiom.id, random_idioms)

    return {
        "question_id": question_id,
        "question": idiom.text,
        "answers": get_answer_list(idiom, random_idioms)
    }


def get_similar_idioms(idiom):
    vec = sim_matrix[idiom.id]
    if vec is None or len(vec) == 0:
        return {}
    if len(vec) == 1:
        return {vec[0]: MODEL_WEIGHT}

    indexed_similarities = [(i, x) for i, x in enumerate(vec)]
    sorted_similarities = sorted(indexed_similarities, key=lambda x: x[1])
    result_similarities = [s[0] for s in sorted_similarities if s[1] > 0]

    sim_count = len(result_similarities)
    if sim_count == 2:
        return {result_similarities[0]: 2*(MODEL_WEIGHT / 3.0), result_similarities[1]: MODEL_WEIGHT / 3.0}

    weighted_idioms = {}
    min_weight = 1.0
    step = (2*min_weight + ((2*MODEL_WEIGHT) / sim_count)) / (sim_count - 1)
    current_weight = min_weight

    for i in result_similarities:
        if vec[i] > SIMILARITY_UPPER_BOUND:
            # Too similar definition, should never appear in answers
            weighted_idioms[i] = MODEL_WEIGHT * (-10)
        else:
            weighted_idioms[i] = current_weight
        current_weight += step

    return weighted_idioms


def get_same_category_idioms(idiom):
    idioms = IdiomModel.query.filter(IdiomModel.category == idiom.category).all()
    weighted_idioms = {}

    id_weight = MODEL_WEIGHT / len(idioms)
    for i in idioms:
        weighted_idioms[i.id] = id_weight

    return weighted_idioms


def get_incorrectly_answered_idioms(idiom):
    questions_with_idiom = db.session.query(UserAnswerModel, GeneratedQuestionModel) \
        .filter(GeneratedQuestionModel.id == UserAnswerModel.generated_question_id) \
        .filter(GeneratedQuestionModel.idiom_id == idiom.id).all()

    if len(questions_with_idiom) == 0:
        return {}

    mistaken_answers = set([i.UserAnswerModel.user_answer_idiom_id for i in questions_with_idiom\
                            if i.UserAnswerModel.is_answered_correctly == False])
    if len(mistaken_answers) == 0:
        return {}
    if len(mistaken_answers) == 1:
        return {mistaken_answers.pop(): MODEL_WEIGHT}

    mistakes_with_ratios = {}
    for mistake in mistaken_answers:
        mistakes_count = len([i for i in questions_with_idiom if i.UserAnswerModel.user_answer_idiom_id == mistake])
        questions_with_mistaken_idiom = len([i for i in questions_with_idiom \
                                             if i.GeneratedQuestionModel.answer_one_idiom_id == mistake\
                                             or i.GeneratedQuestionModel.answer_two_idiom_id == mistake\
                                             or i.GeneratedQuestionModel.answer_three_idiom_id == mistake])

        ratio = float(mistakes_count) / questions_with_mistaken_idiom
        mistakes_with_ratios[mistake] = ratio

    mistaken_answers = [key for key, val in sorted(mistakes_with_ratios.items(), key=lambda kv: kv[1])]

    mist_count = len(mistaken_answers)
    if mist_count == 2:
        return {mistaken_answers[0]: 2*(MODEL_WEIGHT / 3.0), mistaken_answers[1]: MODEL_WEIGHT / 3.0}

    weighted_idioms = {}
    min_weight = 1.0
    step = (2*min_weight + ((2*MODEL_WEIGHT) / mist_count)) / (mist_count - 1)
    current_weight = min_weight

    for i in mistaken_answers:
        weighted_idioms[i] = current_weight
        current_weight += step

    return weighted_idioms


def get_answer_list(idiom, random_idioms):
    answer_list = [{"answer_text": idiom.definition, "answer_id": idiom.id}]
    for _idiom in random_idioms:
        answer_list.append({"answer_text": _idiom.definition, "answer_id": _idiom.id})

    return answer_list


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