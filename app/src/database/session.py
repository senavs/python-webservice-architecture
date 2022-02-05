from contextlib import contextmanager
from functools import wraps
from typing import Callable

from sqlalchemy.orm import Session

from . import engine


def create_session() -> Session:
    return Session(engine)


@contextmanager
def context_session() -> Session:
    with create_session() as session:
        session.begin()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()


def inject_session(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_session = kwargs.pop("session", None)
        if current_session:
            return func(*args, **kwargs, session=current_session)

        session = create_session()
        session.expire_on_commit = False
        session.begin()

        try:
            resp = func(*args, **kwargs, session=current_session or session)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            return resp

    return wrapper
