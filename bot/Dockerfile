FROM python:3.10.7-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    DISABLE_POETRY_CREATE_RUNTIME_FILE=1 \
    POETRY_EXPORT_DEV_REQUIREMENTS=0 \
    PYTHON_RUNTIME_VERSION=3.10.7


RUN pip install -U pip
RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /bot
WORKDIR /bot

COPY pyproject.toml /bot/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /bot
