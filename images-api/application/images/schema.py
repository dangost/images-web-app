from marshmallow import Schema, fields, post_load

from application.images.models import Image, ImageUpload


class ImageSchema(Schema):
    id = fields.String(data_key="id", required=True)
    user_login = fields.String(data_key="user_login", required=True)
    upload_date = fields.String(data_key="upload_date", required=True)
    image_link = fields.String(data_key="image_link", required=True)

    @post_load
    def make(self, data, **kwargs):
        return Image(**data)


class ImageUploadSchema(Schema):
    login = fields.String(data_key="login", required=True)
    data = fields.String(data_key="data", required=True)

    @post_load
    def make(self, data, **kwargs):
        return ImageUpload(**data)

