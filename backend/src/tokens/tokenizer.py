from .Token import Token
from ..utils.text_preprocessor import word_tokenize, normalize


def tokenizer(text, pos):
    words = word_tokenize(text)  # falta quitarle las articulos y esas cosas
    words = normalize(words)
    #tokens = []
    #for i, word in enumerate(words):
    #    tokens.append(Token.new(word, pos + i))
    #return tokens
    return words
