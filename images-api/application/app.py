from flask import Flask, jsonify

from application.common.exceptions import HttpException
from application.app_config import AppConfig
from application.images.controller import images_api
from application.images.service import ImagesService
from application.pages.assets_controller import assets_controller
from application.pages.css_controller import css_controller
from application.pages.js_controller import js_controller
from application.pages.controller import pages
from application.users.controller import users_api
from application.users.service import UsersService


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_error_handler(HttpException, error_handler)
    init_blueprints(app)

    app_config = AppConfig()

    init_services(app, app_config)
    app.config.startup = app_config.startup_config

    app.config.views_folder = app_config.views_folder
    app.config.template_folder = app_config.views_folder

    app_config.sql_config.metadata.create_all(checkfirst=True)
    return app


def init_blueprints(app: Flask):
    app.register_blueprint(users_api)
    app.register_blueprint(images_api)
    app.register_blueprint(pages)
    app.register_blueprint(js_controller)
    app.register_blueprint(css_controller)
    app.register_blueprint(assets_controller)


def init_services(app: Flask, config: AppConfig):
    app.config.users_service = UsersService(config.sql_config, config.jwt_secret)
    app.config.images_service = ImagesService(config.sql_config)


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
