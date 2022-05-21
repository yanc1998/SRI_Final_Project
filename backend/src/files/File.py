from ..tokens.Token import Token


class File:
    def __init__(self, name, tokens):
        self.tokens = tokens
        self.name = name

    @staticmethod
    def new(name, tokens):
        if not isinstance(name, str):
            raise Exception('name most be an string')
        if not isinstance(tokens, list):
            raise Exception('tokens most be an tokens array')

        return File(name, tokens)
