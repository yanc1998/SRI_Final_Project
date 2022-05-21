from src.files.getAllFiles import get_all_files
from src.vectorialModel.vectorialmode import VectorialMode
import os
from src.services.find_services import FindService
from src.services.file_service import FileService
from flask import Flask, request

app = Flask(__name__)

path = os.getcwd() + '/public/files'
files = get_all_files(path)
vectorial = VectorialMode(files)


# find the relevant documents for a query
@app.route('/find', methods=['POST'])
def find():
    find_service = FindService(vectorial)
    query = request.json['query']
    count = request.json['count']
    response = find_service.find(query, count)
    return {
        "data": response
    }


# download a document
@app.route('/download', methods=['POST'])
def download():
    file = request.json['file_name']
    return FileService.download(path + '/' + file)
