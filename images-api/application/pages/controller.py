from flask import Blueprint, current_app as app

pages = Blueprint("pages", __name__, url_prefix="/")


@pages.route("/")
def index():
    path = app.config.views_folder + "/index.html"
    return open(path, encoding="UTF-8").read()


@pages.route("/signup")
def signup():
    path = app.config.views_folder + "/signup.html"
    return open(path, encoding="UTF-8").read()


@pages.route("/upload")
def upload():
    path = app.config.views_folder + "/upload.html"
    return open(path, encoding="UTF-8").read()
