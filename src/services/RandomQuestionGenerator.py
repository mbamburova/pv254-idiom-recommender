from src.models.IdiomModel import IdiomModel

import random


def generate_question():
    idioms = IdiomModel.query.all()
    idiom_ids = []
    for idiom in idioms:
        idiom_ids.append(idiom.id)

    random.shuffle(idiom_ids)
    rand_position = random.randint(0, len(idioms) - 1)

    return IdiomModel.query.get(idiom_ids[rand_position])

