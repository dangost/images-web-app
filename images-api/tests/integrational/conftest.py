import os
from uuid import uuid4

import pytest


@pytest.fixture(scope="session")
def host() -> str:
    protocol = os.getenv('PROTOCOL', default='http')
    ip = os.getenv("IP", default='127.0.0.1')
    port = os.getenv('PORT', default=8080)
    return f"{protocol}://{ip}:{port}"


def get_str():
    return str(uuid4()).replace('-', '')
