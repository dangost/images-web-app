from application.images.models import ImageView
from application.users.models import User, UserView


def to_user_view(user: User, images: list[ImageView]) -> UserView:
    return UserView(
        id=user.id,
        login=user.login,
        profile_description=user.profile_description,
        images=images
    )