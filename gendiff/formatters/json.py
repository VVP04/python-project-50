import json


def format_json(diff_dict):
    formatted_diff = json.dumps(diff_dict, indent=2)
    return formatted_diff