import pytest
from gendiff import generate_diff
from pathlib import Path

@pytest.fixture
def expected_stylish_output():
    path = Path("tests/fixtures", "expected_stylish_output.txt").resolve()
    with open(path, 'r') as file:
        return file.read().strip()

@pytest.mark.parametrize("file1, file2", [
    (Path("tests/fixtures", "file1.json").resolve(), Path("tests/fixtures", "file2.json").resolve()),
    (Path("tests/fixtures", "file1.yaml").resolve(), Path("tests/fixtures", "file2.yaml").resolve()),
])

def test_generate_diff_with_flat_files(file1, file2, expected_stylish_output):
    result = generate_diff(file1, file2)
    assert result == expected_stylish_output