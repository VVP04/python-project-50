import pytest
from gendiff.parser import parse_file
from tests.fixtures.json_file1_dict import JSON_FILE1_DICT
from pathlib import Path

@pytest.fixture
def file1_json():
    return Path("tests/fixtures/file1.json").resolve()

@pytest.fixture
def file1_yaml():
    return Path("tests/fixtures/file1.yaml").resolve()

def test_parse_json(file1_json):
    result = parse_file(file1_json)
    assert result == JSON_FILE1_DICT

def test_parse_yaml(file1_yaml):
    result = parse_file(file1_yaml)
    assert result == JSON_FILE1_DICT
