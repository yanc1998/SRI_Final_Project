from src.files.redFiles import redfiles
from src.files.getAllFiles import get_all_files
from src.vectorialModel.vectorialmode import VectorialMode
import os
from src.tokens.tokenizer import tokenizer
from src.files.File import File


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = os.getcwd() + '/public/files'
    files = get_all_files(path)
    vectorial = VectorialMode(files)
    query = 'an experimental study of a wing in a propeller slipstream was'
    tokens = tokenizer(query, 0)
    res = vectorial.fill_query([File.new('query', tokens)], 10)
    print(res)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
