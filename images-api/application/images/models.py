from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Image:
    id: str
    user_login: str
    upload_date: datetime
    image_link: str


@dataclass(frozen=True)
class ImageUpload:
    login: str
    data: str
    upload_date: datetime | None
