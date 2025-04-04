from pathlib import Path

import pytest

from gendiff import generate_diff


@pytest.fixture
def expected_stylish_output():
    path = Path("tests/fixtures", "expected_stylish_output.txt").resolve()
    with open(path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def expected_plain_output():
    path = Path("tests/fixtures", "expected_plain_output.txt").resolve()
    with open(path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def expected_json_output():
    path = Path("tests/fixtures", "expected_json_output.txt").resolve()
    with open(path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize("file1, file2, format, expected_output", 
                        [
                            (
                                Path("tests/fixtures", "file1.json").resolve(), 
                                Path("tests/fixtures", "file2.json").resolve(), 
                                "stylish", "expected_stylish_output"
                            ),
                            (
                                Path("tests/fixtures", "file1.yaml").resolve(), 
                                Path("tests/fixtures", "file2.yaml").resolve(), 
                                "stylish", "expected_stylish_output"
                             ),
                            (
                                Path("tests/fixtures", "file1.json").resolve(), 
                                Path("tests/fixtures", "file2.json").resolve(), 
                                "plain", "expected_plain_output"
                            ),
                            (
                                Path("tests/fixtures", "file1.yaml").resolve(), 
                                Path("tests/fixtures", "file2.yaml").resolve(), 
                                "plain", "expected_plain_output"
                            ),
                            (
                                Path("tests/fixtures", "file1.json").resolve(), 
                                Path("tests/fixtures", "file2.json").resolve(), 
                                "json", "expected_json_output"
                            ),
                            (
                                Path("tests/fixtures", "file1.yaml").resolve(), 
                                Path("tests/fixtures", "file2.yaml").resolve(), 
                                "json", "expected_json_output"
                            )
                        ])
def test_generate_diff(file1, file2, format, expected_output, request):
    output = request.getfixturevalue(expected_output)
    result = generate_diff(file1, file2, format_name=format)
    assert result == output