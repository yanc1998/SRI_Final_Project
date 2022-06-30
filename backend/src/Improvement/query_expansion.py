from nltk.corpus import wordnet as wn


def expand(model, query):
    suggest = set()
    for i in range(1, len(query)):
        if query[i - 1] in model.corr:
            for sug in model.corr[query[i - 1]]:
                suggest.add(tuple(query[:i] + [sug] + query[i + 1:]))

            for syn in wn.synsets(query[i]):
                if syn.name in model.corr[query[i - 1]]:
                    suggest.add(tuple(query[:i] + [syn.name] + query[i + 1:]))
        if query[i] in model.corr:
            for sug in model.vocabulary:
                if sug in model.corr and query[i] in model.corr[sug]:
                    suggest.add(tuple(query[:i - 2] + [sug] + query[i:]))

            for syn in wn.synsets(query[i - 1]):
                if syn.name in model.corr and query[i] in model.corr[syn.name]:
                    suggest.add(tuple(query[:i - 2] + [syn.name] + query[i:]))
    return list(suggest)
