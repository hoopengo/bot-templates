FROM python:3.11.2-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.2 \
    DISABLE_POETRY_CREATE_RUNTIME_FILE=1 \
    POETRY_EXPORT_DEV_REQUIREMENTS=0 \
    PYTHON_RUNTIME_VERSION=3.11.2

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --without dev --no-interaction --no-ansi

COPY src/ /usr/src/app/

CMD [ "sh", "run.sh" ]
