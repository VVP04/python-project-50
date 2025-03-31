from gendiff.diff import get_diff
from tests.fixtures.json_file1_dict import JSON_FILE1_DICT
from tests.fixtures.json_file2_dict import JSON_FILE2_DICT 
from tests.fixtures.expected_diff_dict import EXPECTED_DIFF_DICT
from pathlib import Path


def test_get_diff():
    dict1 = JSON_FILE1_DICT
    dict2 = JSON_FILE2_DICT
    assert get_diff(dict1, dict2) == EXPECTED_DIFF_DICT