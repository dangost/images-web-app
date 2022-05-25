from flask import Blueprint, jsonify, request, current_app as app, make_response

from application.images.schema import image_upload_schema, image_schema, image_view_schema

images_api = Blueprint("images_controller_api", __name__, url_prefix="/api/images")


# todo like post

# todo change image description

@images_api.route("<_id>", methods=['GET'])
def raw_image(_id: str):
    data = app.config.images_service.get_image(_id)
    response = make_response(data)
    response.headers.set('Content-Type', 'image/jpeg')
    return response


@images_api.route("/feed", methods=['GET'])
def get_feed():
    posts = app.config.images_service.feed()
    response = image_view_schema.dump(posts, many=True)
    return jsonify(response)


@images_api.route("", methods=['POST'])
def post_image():
    user = app.config.users_service.auth(request.headers)
    payload = request.json
    upload_image = image_upload_schema.load(payload)

    image = app.config.images_service.upload_image(upload_image, user)

    result = image_schema.dump(image)

    return jsonify(result)

