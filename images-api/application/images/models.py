from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Image:
    id: str
    user_login: str
    upload_date: datetime
    image_data: str  # base64 string
