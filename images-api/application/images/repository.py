from typing import Union, Optional

from sqlalchemy import Table, MetaData, Column, String, ForeignKey, BINARY, TIMESTAMP

from application.images.models import Image, ImageView
from application.sql_config import SqlConfig

IMAGES: Table


def describe_table(metadata: MetaData):
    return Table(
        "images",
        metadata,
        Column("id", String, primary_key=True, nullable=True, unique=True),
        Column("login", String, ForeignKey("users.login"), nullable=True),
        Column("description", String, nullable=True),
        Column("upload_date", TIMESTAMP, nullable=True),
        Column("source", String, nullable=False),
        Column("data", BINARY, nullable=False),
    )


class ImagesSqlRepo:
    def __init__(self, sql_config: SqlConfig):
        global IMAGES
        IMAGES = describe_table(sql_config.metadata)
        self.engine = sql_config.engine

    def insert(self, image: Image) -> None:
        statement = IMAGES.insert().values(
            id=image.id,
            login=image.login,
            description=image.description,
            upload_date=image.upload_date,
            source=image.source,
            data=image.data
        )

        with self.engine.begin() as connection:
            connection.execute(statement)

    def get_by_id(self, image_id: str) -> Optional[bytes]:
        statement = IMAGES.select().where(IMAGES.c.id == image_id)

        with self.engine.connect() as connection:
            row = connection.execute(statement).one_or_none()

        if not row:
            return None
        return row.data

    def get_feed(self) -> list[ImageView]:
        statement = IMAGES.select()

        with self.engine.connect() as connection:
            rows = connection.execute(statement).all()

        return [self._row_to_image_view(row) for row in rows]

    def get_user_images(self, login: str) -> list[ImageView]:
        statement = IMAGES.select().where(IMAGES.c.login == login)

        with self.engine.connect() as connection:
            rows = connection.execute(statement).all()

        return [self._row_to_image_view(row) for row in rows]

    @staticmethod
    def _row_to_image(row):
        return Image(
            id=row.id,
            login=row.login,
            upload_date=row.upload_date,
            description=row.description,
            source=row.source
        ) if row else None

    @staticmethod
    def _row_to_image_view(row):
        return ImageView(
            id=row.id,
            source=row.source,
            description=row.description,
            upload_date=row.upload_date
        ) if row else None
