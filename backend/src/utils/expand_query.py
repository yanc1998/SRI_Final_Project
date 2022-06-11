class ExpandQuery:
    def __init__(self, files, alpha=0.5):
        self.files = files
        self.relations = {}
        self.count_words = {}
        self.relations_words = {}
        self._find_relation_words(alpha)

    def _find_relation_words(self, alpha):
        for file in self.files:
            for i in range(len(file.tokens) - 1):
                try:
                    self.relations[(file.tokens[i], file.tokens[i + 1])] += 1
                except:
                    self.relations[(file.tokens[i], file.tokens[i + 1])] = 1

                try:
                    self.relations[(file.tokens[i + 1], file.tokens[i])] += 1
                except:
                    self.relations[(file.tokens[i + 1], file.tokens[i])] = 1

                try:
                    self.count_words[file.tokens[i]] += 1
                except:
                    self.count_words[file.tokens[i]] = 1

                self.relations_words[file.tokens[i]] = []

                if i == len(file.tokens) - 1:
                    try:
                        self.count_words[file.tokens[i + 1]] += 1
                    except:
                        self.count_words[file.tokens[i + 1]] = 1

                    self.relations_words[file.tokens[i + 1]] = []

        for rel in self.relations.values():
            self.relations[rel] /= self.count_words[rel[0]]

        for file in self.files:
            for word1 in file.tokens:
                for word2 in file.tokens:
                    if word2 != word1 and self.relations[(word1, word2)] > alpha:
                        self.relations_words[word1].append(word2)

    def expand_query(self, query):
        expand_query = []
        for token in query:
            try:
                for relation_token in self.relations_words[token]:
                    expand_query.append(relation_token)
            except:
                pass

        return expand_query
