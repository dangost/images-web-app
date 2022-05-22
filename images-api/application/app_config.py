import os
import json

from application.sql_config import SqlConfig

ENV_CONFIG_FILE = "CONFIG_FILE"
CONFIG_HOST = "service_host"
CONFIG_PORT = "service_port"
CONFIG_JWT_SECRET = "service_jwt_secret"
CONFIG_DB_CONNECTION_STRING = "db_connection_string"


class AppConfig:
    def __init__(self):
        config_file = os.getenv(ENV_CONFIG_FILE, default="config.json")
        try:
            with open(config_file, 'r', encoding="UTF-8") as stream:
                config_json: dict = json.loads(stream.read())
        except Exception:
            raise Exception("Config json file not found or can't be deserialized")

        self.connection = config_json.get(CONFIG_DB_CONNECTION_STRING, "sqlite:///../data.db")
        self.sql_config = SqlConfig(self.connection)

        self.views_folder = str(os.getenv("VIEWS_FOLDER", ".")).replace('\\', '/')

        self.jwt_secret = config_json.get(CONFIG_JWT_SECRET, None)
        if not self.jwt_secret:
            raise Exception("No JWT Secret")

        self.startup_config = StartupConfig(config_json)


class StartupConfig:
    def __init__(self, config_json: dict):
        self.host = config_json.get(CONFIG_HOST, "0.0.0.0")
        self.port = config_json.get(CONFIG_PORT, 8080)
