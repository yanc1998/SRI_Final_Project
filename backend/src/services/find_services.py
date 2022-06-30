from ..TextProcessor.Token import tokenizer
from ..files.File import File


class FindService:
    def __init__(self, model):
        self.model = model

    def find(self, query: str, k: int):
        return self.model.similarity(query, k)
