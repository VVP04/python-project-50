import json
from pathlib import Path
from gendiff.formatters.stylish import make_string


def read_file(file):
    file_path = Path(file).resolve()
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = make_string(data1, data2)
    return diff