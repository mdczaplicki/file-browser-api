install:
    docker compose build

up:
    docker compose up -d

down:
    docker compose down

bash:
    docker exec -it file_browser_api bash

test:
    docker exec -it file_browser_api pytest tests

lock:
    docker exec -it file_browser_api poetry lock

check:
    docker exec -it file_browser_api ruff check
    docker exec -it file_browser_api ruff format --check
    docker exec -it file_browser_api ruff mypy .

format:
    docker exec -it file_browser_api ruff check --fix
    docker exec -it file_browser_api ruff format