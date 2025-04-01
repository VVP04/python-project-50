from gendiff.formatters.stylish import format_stylish


def format_diff(diff_dict: dict, format: str):
    if format == 'stylish':
        return format_stylish(diff_dict)