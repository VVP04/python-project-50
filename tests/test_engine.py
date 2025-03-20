from gendiff import generate_diff
from pathlib import Path


file1_json = Path("tests/fixtures", "file1.json").resolve()
file2_json = Path("tests/fixtures", "file2.json").resolve()
expected_stylish_output = Path("tests/fixtures", "expected_stylish_output.txt").resolve()


def test_generate_diff_with_flat_json():
    with open(expected_stylish_output, 'r') as file:
        expected_output = file.read().strip()
    result = generate_diff(file1_json, file2_json)
    assert result == expected_output