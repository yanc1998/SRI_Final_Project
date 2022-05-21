from .redFiles import redfiles
from ..tokens.tokenizer import tokenizer
from .File import File


def get_all_files(path):
    files = redfiles(path)
    all_files = []
    for file_name in files:
        with open(path + '/' + file_name, "r", encoding="utf8") as file:
            text = file.read()
            clean_text = text
            tokens = tokenizer(clean_text, 0)
            all_files.append(File.new(file_name, tokens))

    return all_files
