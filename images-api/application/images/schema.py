from marshmallow import Schema, fields, post_load

from application.images.models import Image, ImageUpload


class ImageViewSchema(Schema):
    id = fields.String(data_key="id", required=True)
    source = fields.String(data_key="source", required=True)
    description = fields.String(data_key="description", required=True)
    upload_date = fields.String(data_key="upload_date", required=True)

    @post_load
    def make(self, data, **kwargs):
        return Image(**data)


class ImageSchema(Schema):
    id = fields.String(data_key="id", required=True)
    login = fields.String(data_key="login", required=True)
    upload_date = fields.String(data_key="upload_date", required=True)
    source = fields.String(data_key="source", required=True)

    @post_load
    def make(self, data, **kwargs):
        return Image(**data)


class ImageUploadSchema(Schema):
    data_base64 = fields.String(data_key="data_base64", required=True)
    description = fields.String(data_key="description", required=True)

    @post_load
    def make(self, data, **kwargs):
        return ImageUpload(**data)


image_view_schema = ImageViewSchema()
image_schema = ImageSchema()
image_upload_schema = ImageUploadSchema()

