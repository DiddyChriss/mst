build:
	docker compose build

run:
	docker compose up

stop:
	docker compose stop

logs:
	docker compose logs -f

tests:
	docker compose run --rm restaurant-web pytest

clean:
	docker compose down -v

setup:
	@make build
	@make run
	@make logs

first_setup:
	cp example.env .env
	@make build
	@make run
	@make logs

full_build:
	@make build

restart:
	@make stop
	@make run
	@make logs

black:
	docker compose run --rm restaurant-web black .

isort:
	docker compose run --rm restaurant-web isort .

mypy:
	docker compose run --rm restaurant-web mypy .

linter:
	@make black || true
	@make isort || true
	@make mypy || true