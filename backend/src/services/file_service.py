from flask import send_file, send_from_directory


class FileService:
    @staticmethod
    def download(file_name):
        return send_file(file_name, as_attachment=True)

    @staticmethod
    def upload(file_name):
        pass
