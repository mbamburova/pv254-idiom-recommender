from src.models import db
from src.models.IdiomModel import IdiomModel

import random


def generate_question():
    idioms_count = db.session.query(IdiomModel).count()
    return IdiomModel.query.get(random.sample(range(1, idioms_count), 1))

