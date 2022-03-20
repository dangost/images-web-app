from sqlalchemy import Table, MetaData, Column, String, ForeignKey, TIMESTAMP

from application.images.models import Image
from application.sql_config import SqlConfig

IMAGES: Table


def describe_table(metadata: MetaData):
    return Table(
        "images",
        metadata,
        Column("id", String, primary_key=True, nullable=True),
        Column("user_login", String, ForeignKey("users.login"), nullable=True),
        Column("upload_date", TIMESTAMP, nullable=True),
        Column("image_data", String, nullable=False)
    )


class ImagesSqlRepo:
    def __init__(self, sql_config: SqlConfig):
        global IMAGES
        IMAGES = describe_table(sql_config.metadata)
        self.engine = sql_config.engine

    def insert(self, image: Image) -> None:
        statement = IMAGES.insert().values(
            id=image.id,
            user_login=image.user_login,
            upload_date=image.upload_date,
            image_data=image.image_data
        )

        with self.engine.begin() as connection:
            connection.execute(statement)

    def get_by_id(self, image_id: str) -> Image:
        statement = IMAGES.select().where(IMAGES.c.id == image_id)

        with self.engine.connect() as connection:
            row = connection.execute(statement).one_or_none()

        return self._row_to_image(row)

    def get_raw_by_id(self, image_id: str) -> str:
        statement = IMAGES.select().where(IMAGES.c.id == image_id)

        with self.engine.connect() as connection:
            row = connection.execute(statement).one_or_none()

        return row.image_data

    def get_user_images(self, user_login: str) -> list[Image]:
        statement = IMAGES.select().where(IMAGES.c.user_login == user_login)

        with self.engine.connect() as connection:
            rows = connection.execute(statement).all()

        return [self._row_to_image(row) for row in rows]

    @staticmethod
    def _row_to_image(row):
        return Image(
            id=row.id,
            user_login=row.user_login,
            upload_date=row.upload_date,
            image_data=row.image_data
        ) if row else None
