import csv
import itertools
import pandas as pd

def parser_categories():
    idioms = pd.read_csv('idioms.csv', sep=';')
    ax = pd.value_counts(idioms['category']).plot.bar()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 16)
    fig = ax.get_figure()
    fig.set_size_inches(18.5*3, 30)
    fig.savefig("./categories.pdf")

def parser_frequency():
    idioms = pd.read_csv('idioms_final.csv', sep=';')
    idioms = idioms.sort_values(ascending=False, by='frequency')
    ax = idioms.plot.bar(x='text')
    fig = ax.get_figure()
    fig.set_size_inches(46.811*4, 33.11*3 )
    fig.savefig("./frequency.pdf", dpi=4800)

parser_frequency()
