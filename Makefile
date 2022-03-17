migrate:
	python3 ./project/manage.py migrate

load-fixtures:
	python3 ./project/manage.py loaddata ./project/fixtures.json

initial: migrate load-fixtures

run:
	python3 ./project/manage.py runserver

lint:
	flake8
