from dataclasses import dataclass
from datetime import datetime

from application.images.models import ImageView


@dataclass(frozen=True)
class UserView:
    id: str
    login: str
    profile_description: str
    images: list[ImageView]


@dataclass(frozen=True)
class User:
    id: str
    login: str
    email: str
    profile_description: str
    create_time: datetime


@dataclass(frozen=True)
class UserLoginDetails:
    login: str
    password: str


@dataclass(frozen=True)
class UserRegistrationDetails:
    login: str
    email: str
    password: str
