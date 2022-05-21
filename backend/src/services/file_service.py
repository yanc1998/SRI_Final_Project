from ..utils.utils import read_doc
from flask import send_file


class FileService:
    @staticmethod
    def download(file_name):
        return send_file(file_name, as_attachment=True)

    @staticmethod
    def upload(file_name):
        pass
