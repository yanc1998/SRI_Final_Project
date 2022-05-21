import os


def redfiles(path: str) -> [str]:
    with os.scandir(path) as files:
        files = [file.name for file in files if file.is_file() and file.name.endswith('.txt')]
        return files
