from pydoc import doc
from sklearn.feature_extraction.text import TfidfVectorizer
from ..Improvement.query_expansion import expand
from ..TextProcessor.Token import tokenizer
import pandas as pd
import numpy as np


class VectorialModel:

    def __init__(self, files):
        self.files = files
        self.get_vocabulary()
        self.compute_tf_idf()
        self.generate_glove_matrix()

    def get_vocabulary(self):
        self.vocabulary = set()
        for file in self.files:
            self.vocabulary.update(file.tokens)
        self.vocabulary = list(self.vocabulary)

    def compute_tf_idf(self):
        self.vectorizer = TfidfVectorizer(vocabulary=self.vocabulary)
        self.vectorizer.fit([','.join(file.tokens) for file in self.files])
        self.TF_IDF = self.vectorizer.transform([','.join(file.tokens) for file in self.files])

    def generate_glove_matrix(self):
        self.corr = dict()
        for file in self.files:
            for j in range(1, len(file.tokens)):
                try:
                    self.corr[file.tokens[j - 1]][file.tokens[j]] += 1
                except:
                    try:
                        self.corr[file.tokens[j - 1]][file.tokens[j]] = 1
                    except:
                        self.corr[file.tokens[j - 1]] = dict()
                        self.corr[file.tokens[j - 1]][file.tokens[j]] = 1

    def gen_vector_T(self, tokens, a=0.4):
        query = np.zeros((len(self.vocabulary)))
        x = self.vectorizer.transform([','.join(tokens)])

        for token in tokens:
            try:
                ind = self.vocabulary.index(token)
                query[ind] = x[0, self.vectorizer.vocabulary_[token]]
                query[ind] = query[ind] * (1 - a) + self.vectorizer.vocabulary_[token] * a
            except:
                pass
        return query

    def cosine_sim(self, a, b):
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0
        cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        return cos_sim

    def similarity(self, query, k):
        doc_rank = list()

        query_token = tokenizer(query)
        query_vector = self.gen_vector_T(query_token)
        for i, d in enumerate(self.TF_IDF.A):
            doc_rank.append((self.cosine_sim(query_vector, d), self.files[i].name))

        doc_rank.sort()
        doc_rank = doc_rank[::-1]
        return doc_rank[:k], expand(self, query_token)
