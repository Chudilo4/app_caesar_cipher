lint:
	poetry run flake8
test:
	poetry run pytest -vv --cov=app --cov-report xml
check: selfcheck test lint
selfcheck:
	poetry check
