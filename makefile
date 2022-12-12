lint:
	poetry run flake8
test:
	poetry run pytest -vv --cov=app
check: selfcheck test lint
selfcheck:
	poetry check

