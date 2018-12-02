from src.models import db
from src.models.GeneratedQuestionModel import GeneratedQuestionModel
from src.models.IdiomModel import IdiomModel
from src.models.UserAnswerModel import UserAnswerModel

import random


def generate_question(user_id):
    answered_questions = get_user_answered_questions(user_id)

    if len(answered_questions) < 1:
        return generate_first_question()
    else:
        return generate_question_based_on_success_rate(answered_questions)


def get_sorted_idioms_with_frequency():
    return IdiomModel.query.order_by(IdiomModel.frequency.desc()).all()


def get_user_answered_questions(user_id):
    answered_questions = (db.session.query(UserAnswerModel, GeneratedQuestionModel).filter(
        UserAnswerModel.user_id == user_id).filter(
        GeneratedQuestionModel.id == UserAnswerModel.generated_question_id)
        .order_by(GeneratedQuestionModel.created_at.desc())
        .all())

    return answered_questions


def generate_first_question():
    sorted_idioms = get_sorted_idioms_with_frequency()

    return sorted_idioms[int(round(len(sorted_idioms)/2))]


def generate_question_based_on_success_rate(answered_questions):
    sorted_idioms = list(get_sorted_idioms_with_frequency())

    last_answered_question = answered_questions[0]
    position = get_position_of_last_question(sorted_idioms, last_answered_question)

    rate = success_rate(answered_questions)
    if rate > 0.9:
        return sorted_idioms[get_new_question_position(position + 61)]
    elif rate > 0.8:
        return sorted_idioms[get_new_question_position(position + 21)]
    elif rate > 0.6:
        return sorted_idioms[get_new_question_position(position - 21)]
    elif rate > 0.4:
        return sorted_idioms[get_new_question_position(position - 31)]
    else:
        return sorted_idioms[get_new_question_position(position - 61)]


def success_rate(answered_questions):
    questions_count = len(answered_questions)

    right_answered_count = 0
    for question in answered_questions:
        if question.UserAnswerModel.is_answered_correctly:
            right_answered_count = right_answered_count + 1

    return right_answered_count / questions_count


def get_position_of_last_question(sorted_idioms, last_answered_question):
    count = 0
    for idiom in sorted_idioms:
        if idiom.id == last_answered_question.GeneratedQuestionModel.idiom_id:
            return count
        else:
            count = count + 1

    return None


def get_new_question_position(new_position):
    min_range = new_position - 10
    max_range = new_position + 10

    if min_range < 0:
        min_range = 0

    if max_range > 1041:
        max_range = 1041

    return random.randint(min_range, max_range)

