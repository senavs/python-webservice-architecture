from contextlib import contextmanager

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
