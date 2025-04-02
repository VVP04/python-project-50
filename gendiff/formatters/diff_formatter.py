from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def format_diff(diff_dict: dict, format: str):
    if format == 'stylish':
        return format_stylish(diff_dict)
    if format == 'plain':
        return format_plain(diff_dict)