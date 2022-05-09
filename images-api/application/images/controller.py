from flask import Blueprint, jsonify, request, current_app as app

from application.images.schema import image_upload_schema, image_schema

images_api = Blueprint("images_controller_api", __name__, url_prefix="/api/images")
"""
[GET]
    get raw image
    get user images by id

[POST]
    add image
"""


@images_api.route("<_id>", methods=['GET'])
def raw_image(_id: str):
    data = app.config.images_service.get_image(_id)
    return data


@images_api.route("", methods=['POST'])
def post_image():
    user = app.config.users_service.auth(request.headers)
    payload = request.json
    upload_image = image_upload_schema.loads(payload)

    image = app.config.images_service.upload_image(upload_image, user)

    result = image_schema.dumps(image)

    return jsonify(result)

