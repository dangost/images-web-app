from application.common.exceptions import HttpException


class ImageException(HttpException):
    def __init__(self, code: int, message: str):
        super().__init__(code, message)


class ImageNotFound(ImageException):
    def __init__(self, image_id: str):
        self.code = 404
        self.message = f"Image {image_id} not found"
        super().__init__(self.code, self.message)

