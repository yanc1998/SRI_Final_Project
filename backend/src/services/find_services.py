from ..tokens.tokenizer import tokenizer
from ..files.File import File


class FindService:
    def __init__(self, vectorial_model):
        self.vectorial_model = vectorial_model

    def find(self, query: str, k: int):
        tokens = tokenizer(query, 0)
        return self.vectorial_model.fill_query([File.new('query', tokens)], k)
