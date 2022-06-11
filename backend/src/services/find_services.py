from ..tokens.tokenizer import tokenizer
from ..files.File import File


class FindService:
    def __init__(self, vectorial_model, expand_query):
        self.vectorial_model = vectorial_model
        self.expand_query = expand_query

    def find(self, query: str, k: int):
        tokens = tokenizer(query, 0)
        expand_tokens = self.expand_query.expand_query(tokens)
        return self.vectorial_model.fill_query([File.new('query', expand_tokens)], k)
