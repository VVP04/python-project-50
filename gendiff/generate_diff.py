from gendiff.diff import get_diff
from gendiff.formatters.diff_formatter import format_diff
from gendiff.parser import parse_file


def generate_diff(file1, file2, format_name='stylish'):
    dict1 = parse_file(file1)
    dict2 = parse_file(file2)
    diff_dict = get_diff(dict1, dict2)
    formatted_diff = format_diff(diff_dict, format_name)
    return formatted_diff