dev-build:
	docker compose -f docker-compose.dev.yml build
dev-up:
	docker compose -f docker-compose.dev.yml up
dev-up-d:
	docker compose -f docker-compose.dev.yml up -d
dev-down:
	docker compose -f docker-compose.dev.yml down
dev-test:
	docker compose -f docker-compose.dev.yml run web sh -c 'pytest'

local-build:
	docker compose -f docker-compose.local.yml build
local-up:
	docker compose -f docker-compose.local.yml up
local-up-d:
	docker compose -f docker-compose.local.yml up -d
local-down:
	docker compose -f docker-compose.local.yml down
local-test:
	docker compose -f docker-compose.local.yml run web sh -c 'pytest'

install-dev-deps: dev-deps
	pip-sync requirements.txt dev-requirements.txt

install-deps: deps
	pip-sync requirements.txt

deps:
	pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml

dev-deps: deps
	pip-compile --resolver=backtracking --extra=dev --output-file=dev-requirements.txt pyproject.toml

fmt:
	cd src && autoflake --in-place --remove-all-unused-imports --recursive .
	cd src && isort .
	cd src && black .

lint:
	dotenv-linter src/app/.env.ci
	cd src && python manage.py check
	flake8 src
	cd src && mypy

test:
	mkdir -p src/static
	cd src && python manage.py makemigrations --dry-run --no-input --check
	cd src && python manage.py compilemessages
	cd src && pytest --dead-fixtures
	cd src && pytest -x

coverage:
	mkdir -p src/app/static
	cd src && python manage.py makemigrations --dry-run --no-input --check
	cd src && python manage.py compilemessages
	cd src && pytest --dead-fixtures
	cd src && coverage run -m pytest
	cd src && coverage html

migrations:
	cd src && python manage.py makemigrations