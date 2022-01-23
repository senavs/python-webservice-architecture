from functools import wraps
from typing import Callable

from sqlalchemy.orm import Session

from .loader import create_all
from .session import create_session
from ..schemas.singleton import Singleton


class DBConnection(Singleton):
    def __init__(self):
        create_all()
        self._session = create_session()

    @property
    def session(self) -> Session:
        return self._session


def inject_conn(func: Callable) -> Callable:
    """Inject the same connection and handle exception"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = DBConnection()

        try:
            resp = func(conn=conn, *args, **kwargs)
        except Exception:
            conn.session.rollback()
            raise
        else:
            conn.session.commit()

        return resp

    return wrapper
