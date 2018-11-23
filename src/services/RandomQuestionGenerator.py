from src.models.IdiomModel import IdiomModel

import random


def generate_question():
    return IdiomModel.query.get(random.sample(range(1, 1041), 1))

