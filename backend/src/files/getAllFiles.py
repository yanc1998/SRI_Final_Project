from .redFiles import redfiles
from ..tokens.tokenizer import tokenizer
from .File import File
from ..utils.utils import read_doc


def get_all_files(path):
    files = redfiles(path)
    all_files = []
    for file_name in files:
        text = read_doc(path + '/' + file_name)
        clean_text = text
        tokens = tokenizer(clean_text, 0)
        all_files.append(File.new(file_name, tokens))

    return all_files
