lint:
	poetry run flake8
test:
	poetry run pytest -vv
check: selfcheck test lint
selfcheck:
	poetry check
test cov:
	poetry run pytest --cov=app --cov-report xml
