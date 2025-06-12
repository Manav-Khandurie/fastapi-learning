# Makefile

.PHONY: code-coverage code-coverage-report server prod-server test unit-test integration-test black isort flake8 bandit sql-fix sql-check sql-fix-all requirements jaeger-start nbqa-lint-test nbqa-lint-all 

code-coverage:
	poetry run pytest --cov=src tests/

code-coverage-report:
	poetry run pytest --cov=src --cov-report=xml --cov-report=term

server:
	poetry run server

prod-server:
	poetry run gunicorn src.main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 -w 4 --access-logfile -

test:
	poetry run pytest tests/

unit-test:
	poetry run pytest -m "unit"

integration-test:
	poetry run pytest -m "integration"

black:
	poetry run black src/ tests/

isort:
	poetry run isort src/ tests/

flake8:
	poetry run flake8 --config=.flake8 src/ tests/

bandit:
	poetry run bandit -r src/ tests/ -c bandit.yaml

sql-fix:
	poetry run sqlfluff fix .

sql-fix-all:
	poetry run sqlfluff fix src/ tests/

sql-check:
	poetry run sqlfluff lint .

nbqa-lint-test:
	poetry run nbqa black notebooks/ETL.ipynb
	poetry run nbqa isort notebooks/ETL.ipynb
	poetry run nbqa flake8 notebooks/ETL.ipynb

nbqa-lint-all:
	poetry run nbqa black src/ tests/
	poetry run nbqa isort src/ tests/
	poetry run nbqa flake8 src/ tests/

lint-all: black isort flake8 bandit sql-fix-all nbqa-lint-all

requirements:
	poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

jaeger-start:
	docker run -d --name jaeger -e COLLECTOR_OTLP_ENABLED=true -p 16686:16686  -p 4317:4317 -p 4318:4318 jaegertracing/all-in-one:1.50  

jaeger-stop:
	docker stop jaeger && docker rm jaeger