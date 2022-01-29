from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from . import BaseRepository, BaseCRUDRepository
from .. import UserModel
from ..session import inject_session
from ...exception.user import UserNotFoundError, UserAlreadyRegisterError


class UserCRUDRepository(BaseCRUDRepository):
    _table: UserModel = UserModel


class UserSearchRepository(BaseRepository):
    _table: UserModel = UserModel

    @classmethod
    @inject_session
    def list_all(cls, *, session: Session = None) -> list[UserModel]:
        return session.query(cls._table).all()

    @classmethod
    @inject_session
    def search_by_username(cls, username: str, *, session: Session = None) -> Optional[UserModel]:
        return session.query(cls._table).filter(cls._table.username == username).first()

    @classmethod
    @inject_session
    def search_by_email(cls, email: str, *, session: Session = None) -> Optional[UserModel]:
        return session.query(cls._table).filter(cls._table.email == email).first()

    @classmethod
    @inject_session
    def search_by_username_or_email(cls, username: str, email: str, *, session: Session = None) -> Optional[UserModel]:
        return session.query(cls._table).filter(or_(cls._table.username == username, cls._table.email == email)).first()


class UserCreateRepository(BaseRepository):
    _table: UserModel = UserModel

    @classmethod
    @inject_session
    def create_new_user(cls, username: str, email: str, *, session: Session = None) -> Optional[UserModel]:
        if UserSearchRepository.search_by_username_or_email(username=username, email=email, session=session):
            raise UserAlreadyRegisterError

        user: UserModel = UserCRUDRepository.insert(username=username, email=email, session=session)
        return user


class UserUpdateRepository(BaseRepository):
    _table: UserModel = UserModel

    @classmethod
    @inject_session
    def update_user_email(cls, username: str, new_email: str, *, session: Session = None) -> Optional[UserModel]:
        user = UserSearchRepository.search_by_username(username=username, session=session)
        if not user:
            raise UserNotFoundError

        if UserSearchRepository.search_by_email(email=new_email, session=session):
            raise UserAlreadyRegisterError

        UserCRUDRepository.update(user, email=new_email, session=session)
        return user
