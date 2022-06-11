from src.files.getAllFiles import get_all_files
from src.vectorialModel.vectorialmode import VectorialMode
import os
from src.services.find_services import FindService
from src.services.file_service import FileService
from flask import Flask, request, make_response
from flask_cors import cross_origin
from urllib.parse import quote
from src.utils.expand_query import ExpandQuery

app = Flask(__name__)

path = os.getcwd() + '/public/files'
files = get_all_files(path)
expand_query = ExpandQuery(files)
vectorial = VectorialMode(files)


# find the relevant documents for a query
@app.route('/find', methods=['POST'])
@cross_origin()
def find():
    find_service = FindService(vectorial, expand_query)
    query = request.json['query']
    count = request.json['count']
    response = find_service.find(query, count)
    print(query)
    return {
        "data": response
    }


# download a document
@app.route('/download', methods=['POST'])
@cross_origin()
def download():
    file = request.json['file_name']
    utf_filename = quote(file.encode('utf-8'))
    download_file = FileService.download(path + '/' + file)
    response = make_response(download_file)
    response.headers["Content-Disposition"] = "attachment;filename*=UTF-8''{}".format(utf_filename)
    response.headers['Content-Type'] = "application/octet-stream; charset=UTF-8"
    return response
