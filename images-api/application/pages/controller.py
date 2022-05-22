from flask import Blueprint, current_app as app

pages = Blueprint("pages", __name__, url_prefix="/")


@pages.route("/signup")
def signup():
    path = app.config.views_folder + "/signup.html"
    return open(path, encoding="UTF-8").read()


@pages.route("/<login>")
def profile(login: str):
    path = app.config.views_folder + "/profile.html"
    return open(path, encoding="UTF-8").read()
