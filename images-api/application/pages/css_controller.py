from flask import Blueprint, current_app as app

css_controller = Blueprint("css_api", __name__, url_prefix="/css")


@css_controller.route("/<file>")
def css(file):
    return open(f"{app.config.views_folder}/css/{file}").read()

