FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY app/ /app/src

RUN pip install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install --no-dev

CMD []