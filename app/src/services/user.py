from app.src.database.repositories.user import UserCreateRepository, UserSearchRepository, UserUpdateRepository
from app.src.exception.user import UserNotFoundError
from app.src.modules.user import is_valid_email
from app.src.schemas.user import UserModelSchema


def list_all_users() -> list[UserModelSchema]:
    users = UserSearchRepository.list_all()
    return [UserModelSchema.from_orm(user) for user in users]


def search_user_by_username(username: str) -> UserModelSchema:
    user = UserSearchRepository.search_by_username(username=username)
    if not user:
        raise UserNotFoundError

    return UserModelSchema.from_orm(user)


def search_user_by_email(email: str) -> UserModelSchema:
    user = UserSearchRepository.search_by_username(email=email)
    if not user:
        raise UserNotFoundError

    return UserModelSchema.from_orm(user)


def create_user(username: str, email: str) -> UserModelSchema:
    assert is_valid_email(email), "invalid email"

    user = UserCreateRepository.create_new_user(username=username, email=email)
    return UserModelSchema.from_orm(user)


def update_user_email(username: str, new_email: str) -> UserModelSchema:
    assert is_valid_email(new_email), "invalid email"

    user = UserUpdateRepository.update_user_email(username=username, new_email=new_email)
    return UserModelSchema.from_orm(user)
