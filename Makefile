install:
	uv sync

package-install:
	uv tool install dist/*.whl

run:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check gendiff

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build