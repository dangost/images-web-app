from flask import Blueprint

pages = Blueprint("pages", __name__, url_prefix="/")


@pages.route("/signup")
def signup():
    return open("/Users/gost/pets/images-web-app/images-api/views/signup.html").read()


@pages.route("/<login>")
def profile(login: str):
    return open("/Users/gost/pets/images-web-app/images-api/views/profile.html").read()
