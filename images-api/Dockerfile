FROM python:3.10

WORKDIR /app

COPY pyproject.toml .env /app/
COPY application/ /app/application

ENV CONFIG_FILE = "/root/app/config.json"

RUN pip install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install --no-dev

CMD ["poe", "prod"]