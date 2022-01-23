from ..database import UserModel
from ..database.repositories.user import UserCRUDRepository, UserSearchRepository
from ..exceptions.user import UserNotFoundError, UserAlreadyRegisterError
from ..schemas.user import UserModelSchema


def search_user(username: str = None, email: str = None) -> UserModelSchema:
    assert bool(username) != bool(email), "select username or email filter, not both and at least one"

    user: UserModel = UserSearchRepository.search_by_username_or_email(username=username, email=email)
    if not user:
        raise UserNotFoundError

    return user


def create_user(username: str, email: str) -> UserModelSchema:
    if UserSearchRepository.search_by_username_or_email(username=username, email=email):
        raise UserAlreadyRegisterError

    user: UserModel = UserCRUDRepository.insert(username=username, email=email)
    return UserModelSchema.from_orm(user)
