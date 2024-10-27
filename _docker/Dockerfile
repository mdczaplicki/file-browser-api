FROM python:3.12.7-bookworm

WORKDIR /opt/file_browser_api

RUN apt -y update  \
    && apt -y upgrade \
    && pip install --upgrade pip

# Install & configure Poetry
RUN python3 -m venv /opt/poetry \
    && /opt/poetry/bin/pip install poetry==1.8.4 \
    && /opt/poetry/bin/poetry --version
ENV PATH="/opt/poetry/bin:$PATH"

RUN poetry config virtualenvs.path /opt/virtualenvs

ADD _playground /opt/playground

# Install project dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

COPY . .
RUN poetry install --only-root

CMD ["CMD must be overridden during container instantiation."]