FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock .env /app/
COPY application/ /app/application

RUN pip install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install --no-dev

CMD ["poe", "prod"]