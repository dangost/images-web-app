import os

from dotenv import load_dotenv

from sql_config import SqlConfig


class AppConfig:
    def __init__(self):
        load_dotenv()
        self.sql_config = SqlConfig()

        self.jwt_secret = os.getenv("JWT_SECRET")
        if not self.jwt_secret:
            raise Exception("No JWT Secret")

        self.startup_config = StartupConfig()


class StartupConfig:
    def __init__(self):
        self.host = os.getenv("HOST", default="0.0.0.0")
        self.port = os.getenv("PORT", default=8079)
