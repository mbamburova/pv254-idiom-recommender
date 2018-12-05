import csv
import itertools
import pandas as pd
from decimal import Decimal
from matplotlib import pyplot

def anwered_questions_overall():
    idioms = pd.read_csv('user_answers.csv', sep=';')
    idioms = idioms.groupby('version')['is_answered_correctly'].apply(lambda x: ( x.count()))
    idioms = idioms.sort_values(ascending=False)
    ax = idioms.plot.bar(rot=0)
    labels = [item.get_text() for item in ax.get_xticklabels()]
    for index, label in enumerate(labels):
        if label == '1':
            labels[index] = 'RR'
        if label == '2':
            labels[index] = 'TR'
        if label == '3':
            labels[index] = 'RT'
        if label == '4':
            labels[index] = 'TT'
    ax.set_xticklabels(labels)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 16)
    ax.set_title("Number of answered questions", size = 50)
    ax.set_ylabel("answered", size = 35)
    ax.set_xlabel("recommender version", size = 35)
    for p in ax.patches:
        ax.annotate('{}'.format(str(p.get_height())), (p.get_x() + (p.get_width() / 2), p.get_height() - 1), ha='center', va='top', fontsize=24)
    fig = ax.get_figure()
    fig.set_size_inches(21, 16)
    fig.savefig("./anwered_questions_overall.pdf")

anwered_questions_overall()
