from ..TextProcessor.Token import tokenizer
from bs4 import BeautifulSoup
import urllib.request
import re, string
import json
import os

class File:
    def __init__(self, path, tokens, name = None):
        self.tokens = tokens
        if name is None:
            self.name = path.split('/')[-1]
        else:
            self.name = name
        self.path = path

    @staticmethod
    def new(name, tokens):
        if not isinstance(name, str):
            raise Exception('name most be an string')
        if not isinstance(tokens, list):
            raise Exception('tokens most be an tokens array')

        return File(name, tokens)
            

def load_file(file_path, file_name):
    with open(file_path, "r", encoding="utf8") as fd:
        text = fd.read()
        
    tokenized_text = tokenizer(text)
    return File.new(file_name, tokenized_text)


def get_all_files(paths, urls = None):
    all_files = list()
    for path in paths:
        with os.scandir(path) as files:
            for file in files:
                if file.is_file() and file.name.endswith('.txt'):
                    all_files.append(load_file(f'{path}/{file.name}', f'{path}/{file.name}'))
    
    for i, url in enumerate(urls):
        text = BeautifulSoup(urllib.request.urlopen(url)).get_text()
        text = ','.join(re.sub('[%s]' % re.escape(string.punctuation), ' ', text).split())
        file = f'{os.getcwd()}/processed/{i}.txt'
        with open(file, 'w') as fd:
            fd.write(text)
        all_files.append(File(file, tokenizer(text), name = url))
        
    return all_files