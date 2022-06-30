from src.services.find_services import FindService
from src.services.file_service import FileService
from flask import Flask, request, make_response
from src.Model.vectorial import VectorialModel
from src.Model.boolean import BooleanModel
from src.files.File import get_all_files
from flask_cors import cross_origin
from urllib.parse import quote

import logging
import time
import os
import json

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
app = Flask(__name__)

MODEL_V = None
MODEL_B = None
PATHS = [f'{os.getcwd()}/public/files']
URLS = ['https://codeforces.com/blog/entry/104259']


# find the relevant documents for a query
@app.route('/find', methods=['POST'])
@cross_origin()
def find():
    type = request.json['type']

    find_service = FindService(MODEL_V if type == 'vectorial' else MODEL_B)
    query = request.json['query']
    count = request.json['count']

    # retorna una tupla (DataFrame, set(tuple)) con el resultado de la busqueda
    # y todas las posibles expansiones de consultas
    response, expand = find_service.find(query, count)
    print(query)
    print(response)
    print(expand)

    return {
        "data": (
            response,
            expand
        )
    }


# download a document
@app.route('/download', methods=['POST'])
@cross_origin()
def download():
    file = request.json['file_name']
    utf_filename = quote(file.encode('utf-8'))
    download_file = FileService.download(PATHS[0] + '/' + file)
    response = make_response(download_file)
    response.headers["Content-Disposition"] = "attachment;filename*=UTF-8''{}".format(utf_filename)
    response.headers['Content-Type'] = "application/octet-stream; charset=UTF-8"
    return response


def run():
    global MODEL_V, MODEL_B
    _files = get_all_files(PATHS, URLS)
    MODEL_V = VectorialModel(_files)
    MODEL_B = BooleanModel(_files)


if __name__ == '__main__':
    start = time.time()
    run()
    print(f'Executed Time: {round(time.time() - start)} seg')

start = time.time()
run()
print(f'Executed Time: {round(time.time() - start)} seg')
