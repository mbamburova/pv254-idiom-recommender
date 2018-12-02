import json
import pickle
import matplotlib.pyplot as plt
import numpy as np

# This script was used as a playground, to find threshold of too similar answers, we don't want to include in our answers generator

matrix = pickle.load(open('matrix.pkl', "rb")).tolist()
with open('idioms.json') as f:
    data = json.load(f)

idioms = {}
for i in data:
    idioms[i["id"]] = {"text": i["text"], "definition": i["definition"]}


np_matrix = np.array(matrix)
threshold = np.quantile(np_matrix[(np_matrix != 0) & (np_matrix != 1)], 0.99)
print(threshold)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > threshold and i > j:
            print("Idiom 1: "+idioms[i]["text"] +" Idiom 2: "+idioms[j]["text"] )
            print("Idiom 1: "+idioms[i]["definition"] +" Idiom 2: "+idioms[j]["definition"] )
            matrix[i][j] = 0.0
            matrix[j][i] = 0.0

counts = [(counter, len([x for x in vec if x > 0]) - 1) for counter, vec in enumerate(matrix)]
counts.sort(key=lambda x: x[1])
raw_counts = [x[1] for x in counts]

# Histogram of counts of similar
plt.hist(raw_counts, bins=20)
plt.show()
