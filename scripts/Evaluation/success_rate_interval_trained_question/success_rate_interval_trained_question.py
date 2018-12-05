import csv
import itertools, math, collections
import pandas as pd
from decimal import Decimal
from matplotlib import pyplot

def success_rate_interval_trained_question():
    data = pd.read_csv('user_answers_trained_question.csv', sep=';')
    output = pd.DataFrame(columns=['interval','rate'])
    dictionary={}
    for name, group in data.groupby('user_id'):
        group = group.reset_index()
        total = len(group.index)
        if total > 5:
            print("More")
        intervals = math.ceil(total/5)
        for i in range(intervals):
            if i == intervals-1:
                continue;
            for j in range(5):
                dictionary.setdefault(str(i*5) + "-" + str(i*5 + 5),[]).append(group.iloc[i*5+j]['is_answered_correctly'])
    for key, list in dictionary.items():
        if len(list) < 20:
            continue
        rate = list.count('t') / len(list) * 100
        output = output.append({'interval':key, 'rate':rate}, ignore_index=True)
    ax = output.plot.bar(rot=0)
    ax.set_xticklabels(output.interval)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 16)
    ax.set_title("Interval success rate for trained questions", size = 50)
    ax.set_ylabel("success rate in %", size = 35)
    ax.set_xlabel("interval", size = 35)
    for p in ax.patches:
        ax.annotate('{:.0F}%'.format(Decimal(str(p.get_height()))), (p.get_x() + (p.get_width() / 2), p.get_height() - 1), ha='center', va='top', fontsize=24)
    fig = ax.get_figure()
    fig.set_size_inches(18.5*2, 18.5)
    fig.savefig("./success_rate_interval_trained_question.pdf")

success_rate_interval_trained_question()
