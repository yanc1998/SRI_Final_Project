class Token:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    @staticmethod
    def new(value, pos):
        if not isinstance(value, str):
            raise Exception('value most be a string')
        if not isinstance(pos, int) or pos < 0:
            raise Exception('pos most be a positive integer ')

        return Token(value, pos)
