FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        postgresql-client \
        libpq-dev \
        rabbitmq-server \
        curl \
        gnupg \
        wget \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev --no-root

COPY . .

CMD ["poetry", "run", "python", "manage.py", "collectstatic", "--no-input"]
CMD ["poetry", "run", "python", "manage.py", "migrate"]