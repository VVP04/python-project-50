import json
from pathlib import Path

import yaml


def get_file_path(file):
    file_path = Path(file).resolve()
    return file_path


def parse_file(file):
    file_path = get_file_path(file)
    format_file = file_path.suffix[1:]
    if format_file == 'json':
        with open(file_path, 'r') as file_obj:
            data = json.load(file_obj)
        return data
    elif format_file in ('yaml', 'yml'):
        with open(file_path, 'r') as file_obj:
            data = yaml.safe_load(file_obj)
        return data