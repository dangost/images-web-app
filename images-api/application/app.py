from flask import Flask, jsonify

from application.common.exceptions import HttpException
from application.app_config import AppConfig


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_error_handler(HttpException, error_handler)
    init_blueprints(app)

    app_config = AppConfig()

    app_config.sql_config.metadata.create_all(checkfirst=True)

    init_services(app, app_config)
    app.config.startup = app_config.startup_config
    return app


def init_blueprints(app: Flask):
    pass


def init_services(app: Flask, config: AppConfig):
    pass


def error_handler(exc: HttpException):
    return jsonify(
        {
            "status_code": exc.status_code,
            "message": exc.message
        }
    ), exc.status_code


if __name__ == "__main__":
    __app = create_app()
    __app.run(
        host=__app.config.startup.host,
        port=__app.config.startup.port
    )
