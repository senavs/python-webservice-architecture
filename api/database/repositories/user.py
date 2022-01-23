from typing import Optional

from sqlalchemy import or_

from . import BaseRepository, BaseCRUDRepository
from .. import UserModel
from ..connection import inject_conn, DBConnection


class UserCRUDRepository(BaseCRUDRepository):
    _table: UserModel = UserModel


class UserSearchRepository(BaseRepository):
    _table: UserModel = UserModel

    @classmethod
    @inject_conn
    def search_by_username(cls, username: str, *, conn: DBConnection = None) -> Optional[UserModel]:
        return conn.session.query(cls._table).filter(cls._table.username == username).first()

    @classmethod
    @inject_conn
    def search_by_email(cls, email: str, *, conn: DBConnection = None) -> Optional[UserModel]:
        return conn.session.query(cls._table).filter(cls._table.email == email).first()

    @classmethod
    @inject_conn
    def search_by_username_or_email(cls, username: str, email: str, *, conn: DBConnection = None) -> Optional[UserModel]:
        return (
            conn.session.query(cls._table)
            .filter(or_(cls._table.username == username, cls._table.email == email))
            .first()
        )
