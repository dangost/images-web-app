from flask import Blueprint, jsonify, current_app as app


images_api = Blueprint("images_controller_api", __name__)
"""
[GET]
    get raw image
    get user images by id

[POST]
    add image
"""


@images_api.route("/api/images/raw/<_id>", methods=['GET'])
def get_raw_image(_id: str):
    return jsonify({"id": _id})
