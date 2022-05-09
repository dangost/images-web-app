from flask import Blueprint, request, jsonify, current_app as app

from application.common.converters import to_user_view
from application.users.schema import user_login_schema, user_registration_schema, user_schema, user_view_schema

users_api = Blueprint("users_controller_api", __name__, url_prefix="/api")

# todo get users pageable

# todo get user view

# todo user follow to user


# @users_api.route("")
# def user_view():


@users_api.route("/login", methods=['POST'])
def login():
    user_login = user_login_schema.load(request.json)
    jwt_token = app.config.users_service.login(user_login)
    return jsonify({"Authorization": jwt_token}), 200


@users_api.route("/registration", methods=['POST'])
def registration():
    user_registration = user_registration_schema.load(request.json)
    user = app.config.users_service.create(user_registration)

    return jsonify(user_schema.dump(user)), 200


@users_api.route("/user/<login_>", methods=['GET'])
def user_view(login_: str):
    user = app.config.users_service.get_by_login(login_)
    images = app.config.images_service.get_users_images(user.login)

    user_view_obj = to_user_view(user, images)

    result = user_view_schema.dump(user_view_obj)

    return jsonify(result)


@users_api.route("/me", methods=["GET"])
def me():
    user = app.config.users_service.auth(request.headers)
    images = app.config.images_service.get_users_images(user.login)

    user_view_obj = to_user_view(user, images)

    result = user_view_schema.dump(user_view_obj)

    return jsonify(result)
