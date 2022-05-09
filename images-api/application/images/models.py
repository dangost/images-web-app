from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ImageView:
    id: str
    source: str
    description: str
    upload_date: datetime


@dataclass(frozen=True)
class Image:
    id: str
    login: str
    description: str
    source: str
    data: bytes
    upload_date: datetime


@dataclass(frozen=True)
class ImageUpload:
    data_base64: str
    description: str
