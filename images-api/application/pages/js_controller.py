from flask import Blueprint

js_controller = Blueprint("js_api", __name__, url_prefix="/js")


@js_controller.route("/user.js")
def user_js():
    return open("/Users/gost/pets/images-web-app/images-api/views/js/user.js").read()

