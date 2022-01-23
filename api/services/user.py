from ..database import UserModel
from ..database.repositories.user import UserSearchRepository, UserCreateRepository, UserUpdateRepository
from ..exceptions.user import UserNotFoundError
from ..schemas.user import UserModelSchema


def search_user(username: str = None, email: str = None) -> UserModelSchema:
    assert bool(username) != bool(email), "select username or email filter, not both and at least one"

    user: UserModel = UserSearchRepository.search_by_username_or_email(username=username, email=email)
    if not user:
        raise UserNotFoundError

    return UserModelSchema.from_orm(user)


def create_user(username: str, email: str) -> UserModelSchema:
    user = UserCreateRepository.create_new_user(username=username, email=email)
    return UserModelSchema.from_orm(user)


def update_user_email(username: str, new_email: str) -> UserModelSchema:
    user = UserUpdateRepository.update_user_email(username=username, new_email=new_email)
    return UserModelSchema.from_orm(user)
