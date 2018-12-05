import csv
import itertools, math
import pandas as pd
from decimal import Decimal
from matplotlib import pyplot

def success_rate_interval_trained_answers():
    data = pd.read_csv('user_answers_trained_answers.csv', sep=';')
    output = pd.DataFrame(columns=['interval','rate'])
    total = len(data.index)
    intervals = math.ceil(total/50)
    for i in range(intervals):
        intervals_rate = pd.read_csv('user_answers_trained_answers.csv', sep=';', skiprows= range(1, i * 50), nrows=50)
        if len(intervals_rate.index) < 40:
            continue
        rate =  len(intervals_rate[intervals_rate['is_answered_correctly'] == 't'])
        success_rate = (rate / len(intervals_rate.index)) * 100
        output = output.append({'interval':str(i * 50) + '-' + str(i * 50 + 50), 'rate':success_rate}, ignore_index=True)
    ax = output.plot.bar(rot=0)
    ax.set_xticklabels(output.interval)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 16)
    ax.set_title("Interval success rate for trained answers", size = 50)
    ax.set_ylabel("success rate in %", size = 35)
    ax.set_xlabel("interval", size = 35)
    for p in ax.patches:
        ax.annotate('{:.0F}%'.format(Decimal(str(p.get_height()))), (p.get_x() + (p.get_width() / 2), p.get_height() - 1), ha='center', va='top', fontsize=24)
    fig = ax.get_figure()
    fig.set_size_inches(18.5*4, 18.5*2)
    fig.savefig("./success_rate_intervall_trained_answers.pdf")

success_rate_interval_trained_answers()
