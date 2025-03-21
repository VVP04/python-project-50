import json
from pathlib import Path

from gendiff.formatters.stylish import make_string
from gendiff.parser import parse_file


def generate_diff(file1, file2):
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff = make_string(data1, data2)
    return diff