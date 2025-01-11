FROM python:3.12-slim AS builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /code

COPY poetry.lock pyproject.toml .
RUN poetry install --no-interaction --no-ansi

COPY rm_email_notifier ./rm_email_notifier

CMD ["fastapi", "run", "rm_email_notifier/main.py", "--port", "8080"]
