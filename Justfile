install:
    poetry install --no-root

test:
    pytest tests

start:
    poetry run ...

lock:
    poetry lock

check:
    ruff check
    ruff format --check

format:
    ruff check --fix
    ruff format