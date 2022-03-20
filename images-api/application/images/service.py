import base64
from uuid import uuid4
from datetime import datetime, timezone

from application.images.models import Image
from application.images.repository import ImagesSqlRepo
from application.sql_config import SqlConfig


class ImagesService:
    def __init__(self, sql_config: SqlConfig):
        self.sql_repo = ImagesSqlRepo(sql_config)

    def post_image(self, image: bytes, login: str) -> Image:
        image = Image(
            id=str(uuid4()),
            user_login=login,
            upload_date=datetime.now(tz=timezone.utc),
            image_data=base64.b64encode(image).decode("UTF-8")
        )
        self.sql_repo.insert(image)
        return image
