import csv
import itertools
import pandas as pd
from decimal import Decimal
from matplotlib import pyplot

def success_rate_overall_answers_counter():
    answers = pd.read_csv('user_answers.csv', sep=';')
    answers['answers'] = "default"
    for i, row in answers.iterrows():
        if answers['version'][i] == 1 or answers['version'][i] == 2:
            answers.at[i ,'answers'] = "Random"
        else:
            answers.at[i ,'answers'] = "Trained"
    answers = answers.groupby('answers')['is_answered_correctly'].apply(lambda x: (x[x.astype(str) == 't'].count() / x.count()) * 100)
    answers = answers.sort_values(ascending=False)
    ax = answers.plot.bar(rot=0)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 16)
    ax.set_title("Success rate answers", size = 50)
    ax.set_ylabel("success rate in %", size = 35)
    ax.set_xlabel("recommender version", size = 35)
    for p in ax.patches:
        ax.annotate('{:.2F}%'.format(Decimal(str(p.get_height()))), (p.get_x() + (p.get_width() / 2), p.get_height() - 1), ha='center', va='top', fontsize=24)
    fig = ax.get_figure()
    fig.set_size_inches(18.5, 18.5)
    fig.savefig("./success_rate_overall_answers.pdf")

success_rate_overall_answers_counter()
