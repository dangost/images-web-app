from flask import Blueprint, current_app as app, make_response

assets_controller = Blueprint("assets_api", __name__, url_prefix="/assets")


@assets_controller.route("/svg/<filename>")
def svg(filename):
    data = open(f"{app.config.views_folder}/assets/svg/{filename}", 'rb').read()
    response = make_response(data)
    response.headers.set('Content-Type', 'image/svg+xml')
    return response


@assets_controller.route("/img/<filename>")
def img(filename):
    data = open(f"{app.config.views_folder}/assets/img/{filename}", 'rb').read()
    response = make_response(data)
    response.headers.set('Content-Type', 'image/jpeg')
    return response
