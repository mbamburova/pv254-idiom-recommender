# nltk & sklearn is used only for one time preprocessing, it does not need to be available in the server
import json
import pickle

from sklearn.metrics import pairwise_distances
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk, string

'''
This script computes similarity for each pair of idioms in our database.
'''

# https://stackoverflow.com/questions/8897593/similarity-between-two-text-documents
# nltk.download('punkt')
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(texts):
    tfidfs = vectorizer.fit_transform(texts)

    return 1 - pairwise_distances(tfidfs.todense(), metric="cosine")

with open('idioms.json') as f:
    data = json.load(f)

idioms = {}
for i in data:
    idioms[i["id"]] = {"text": i["text"], "definition": i["definition"]}

dim = max([d['id'] for d in data]) + 1
train_set = []
for i in range(dim):
    train_set.append(idioms.get(i, {"definition": ""})["definition"])

matrix = cosine_sim(train_set)
pickle.dump(matrix, open('matrix.pkl', "wb"))
