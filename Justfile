install:
    # Set up the environment
    docker compose build

up:
    # Start the application
    docker compose up -d

down:
    # Stop the application
    docker compose down

bash: up
    # Enter the container
    docker exec -it file_browser_api bash

test: up
    # Run the tests
    docker exec -it file_browser_api poetry run pytest tests

lock: up
    # Lock dependencies
    docker exec -it file_browser_api poetry lock

check: up
    # Lint the code
    docker exec -it file_browser_api poetry run ruff check
    docker exec -it file_browser_api poetry run ruff format --check
    docker exec -it file_browser_api poetry run mypy .

format: up
    # Format the code
    docker exec -it file_browser_api poetry run ruff format
    docker exec -it file_browser_api poetry run ruff check --fix