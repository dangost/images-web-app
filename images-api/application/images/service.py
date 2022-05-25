import base64
from uuid import uuid4
from datetime import datetime, timezone

from application.images.exceptions import ImageNotFound
from application.images.models import Image, ImageUpload, ImageView
from application.images.repository import ImagesSqlRepo
from application.sql_config import SqlConfig
from application.users.exceptions import UserNotFoundException
from application.users.models import User


class ImagesService:
    def __init__(self, sql_config: SqlConfig):
        self.sql_repo = ImagesSqlRepo(sql_config)

    def get_image(self, image_id: str) -> bytes:
        """
        Get image from db by Id
        :param image_id: uuid id of image
        :return: bytearray of image
        """
        try:
            data = self.sql_repo.get_by_id(image_id)
        except Exception:
            data = None
        if not data:
            raise ImageNotFound(image_id)
        return data

    def feed(self):
        try:
            posts = self.sql_repo.get_feed()
        except Exception:
            return []
        return posts

    def get_users_images(self, username: str) -> list[ImageView]:
        """
        :param username:
        :return:
        """
        try:
            images = self.sql_repo.get_user_images(username)
        except Exception:
            raise UserNotFoundException(username)
        return images

    def upload_image(self, upload_image: ImageUpload, user: User) -> Image:
        id_ = str(uuid4())
        data = base64.b64decode(upload_image.data_base64.encode("UTF-8"))
        image = Image(
            id=id_,
            login=user.login,
            description=upload_image.description,
            source=f"/api/images/{id_}",
            data=data,
            upload_date=datetime.now(tz=timezone.utc)
        )
        self.sql_repo.insert(image)
        return image
