from src.files.getAllFiles import get_all_files
from src.vectorialModel.vectorialmode import VectorialMode
import os
from src.services.find_services import FindService

from flask import Flask, request

app = Flask(__name__)

path = os.getcwd() + '/public/files'
files = get_all_files(path)
vectorial = VectorialMode(files)


@app.route('/find', methods=['POST'])
def find():
    find_service = FindService(vectorial)
    query = request.json['query']
    print(query)
    response = find_service.find(query, 10)
    print(response)
    return {
        "data": response
    }
