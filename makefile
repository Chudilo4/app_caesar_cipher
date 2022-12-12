lint:
	poetry run flake8

check: selfcheck test lint changelog

selfcheck:
	poetry check

test:
	poetry run pytest --cov=app --cov-report xml

changelog:
	git log --pretty="- %s" > CHANGELOG.md
