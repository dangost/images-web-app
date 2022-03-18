from flask import Flask

from app_config import AppConfig


def create_app() -> Flask:
    app = Flask(__name__)
    app_config = AppConfig()
    app.config.startup = app_config.startup_config
    return app


if __name__ == "__main__":
    __app = create_app()
    __app.run(
        host=__app.config.startup.host,
        port=__app.config.startup.port
    )
