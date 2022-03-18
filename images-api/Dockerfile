FROM python:3.10

WORKDIR /api

COPY pyproject.toml poetry.lock .env /app/
COPY application/ /app/app

RUN pip install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install --no-dev

CMD []