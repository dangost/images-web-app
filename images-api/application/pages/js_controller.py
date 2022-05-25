from flask import Blueprint, current_app as app

js_controller = Blueprint("js_api", __name__, url_prefix="/js")


@js_controller.route("/<js_file>")
def user_js(js_file):
    return open(f"{app.config.views_folder}/js/{js_file}").read()

