import math
from nltk import FreqDist


class VectorialMode:
    def __init__(self, files):
        self.files = files
        self.wij, self.tf, self.idf = self.fill_w(self.files, 0)
        print('end')

    # retorna el conjunto de los tokens que estan presente en los archivos
    def get_all_tokens(self, files):
        distinct_tokens = set()
        for file in files:
            for token in file.tokens:
                distinct_tokens.add(token)

        return distinct_tokens

    # retorna para cada token, en la cantidad de documentos donde aparece
    def get_cant_files_in_word(self, files):
        cant = {}
        for distinct_token in self.get_all_tokens(files):
            for file in files:
                if distinct_token in file.tokens:
                    try:
                        cant[distinct_token] += 1
                    except:
                        cant[distinct_token] = 1

        return cant

    # calcula el tf
    def fill_tf(self, files):
        tf = [{} for _ in range(len(files))]
        for i, file in enumerate(files):
            freq = FreqDist(file.tokens)
            max_freq = max(freq.values()) if len(freq.values()) > 0 else 0
            # rellenar el tf
            for f in freq.keys():
                tf[i][f] = freq[f] / max_freq
            # poner cero a todas los tokens que no aparcen en ese docuento
            for dist_token in self.get_all_tokens(files):
                if not dist_token in file.tokens:
                    tf[i][dist_token] = 0

        return tf

        # calcula el idf

    def fill_idf(self, files):
        idf = {}
        n = len(files)
        cant = self.get_cant_files_in_word(files)
        for ni in cant.keys():
            idf[ni] = math.log(n / cant[ni])

        return idf

        # calcula el peso de los documentos

    def fill_w(self, files, a=0.5, is_query=False):
        tf = self.fill_tf(files)
        idf = self.fill_idf(files) if not is_query else self.idf
        wij = [{} for _ in range(len(files))]
        for i, tfs in enumerate(tf):
            for tf in tfs.keys():
                try:
                    _idf = idf[tf]
                except:
                    _idf = 0
                wij[i][tf] = (a + (1 - a) * tfs[tf]) * _idf

        return wij, tf, idf

    def fill_query(self, query, k):
        wq, _, _ = self.fill_w(query, 0.4, is_query=True)
        sim = []
        for j, file in enumerate(self.files):
            s1 = 0
            s2 = 0
            s3 = 0
            for q in wq[0]:
                try:
                    wij = self.wij[j][q]
                except:
                    wij = 0
                s1 += wij * wq[0][q]
                s2 += wij ** 2
                s3 += wq[0][q] ** 2
            sim.append((file.name, 0 if s2 == 0 or s3 == 0 else s1 / (math.sqrt(s2) * math.sqrt(s3))))
        mor_relevant = sorted(sim, key=lambda x: x[1], reverse=True)
        return [item[0] for item in mor_relevant[:k]]
