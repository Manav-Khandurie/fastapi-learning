# Makefile

.PHONY: code-coverage server prod-server test unit-test integration-test black isort flake8 bandit sql-fix sql-check requirements jaeger-start

code-coverage:
	poetry run pytest --cov=src tests/

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

sql-check:
	poetry run sqlfluff lint .

lint-all: black isort flake8 bandit sql-fix

requirements:
	poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

jaeger-start:
	docker run -d --name jaeger -e COLLECTOR_OTLP_ENABLED=true -p 16686:16686  -p 4317:4317 -p 4318:4318 jaegertracing/all-in-one:1.50  

jaeger-stop:
	docker stop jaeger && docker rm jaeger