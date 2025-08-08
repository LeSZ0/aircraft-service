
.PHONY: run test lint mypy

run:
	poetry run uvicorn app.main:app --reload

test:
	poetry run pytest

lint:
	poetry run ruff check .

mypy:
	poetry run mypy app/
