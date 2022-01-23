from typing import Optional

from .. import DeclarativeBase
from ..connection import DBConnection, inject_conn


class BaseRepository:
    _table: DeclarativeBase


class BaseCRUDRepository(BaseRepository):
    _table: DeclarativeBase

    @classmethod
    @inject_conn
    def search(cls, id: int, *, conn: DBConnection) -> Optional[DeclarativeBase]:
        return conn.session.query(cls._table).get(id)

    @classmethod
    @inject_conn
    def insert(cls, *, conn: DBConnection, commit: bool = True, flush: bool = True, **kwargs) -> DeclarativeBase:
        record = cls._table(**kwargs)

        conn.session.add(record)
        if commit:
            conn.session.commit()
        if flush:
            conn.session.flush()

        return record

    @classmethod
    def update(
            cls,
            record: DeclarativeBase,
            *,
            conn: DBConnection,
            exclude_none: bool = True,
            commit: bool = True,
            flush: bool = True,
            **kwargs,
    ) -> DeclarativeBase:
        for col, value in kwargs.items():
            if not hasattr(record, col):
                raise TypeError(f"{record.__class__.__name__} as no column {col}")
            if exclude_none and value is None:
                continue
            setattr(cls, record, value)

        if commit:
            conn.session.commit()
        if flush:
            conn.session.flush()

        return record

    @classmethod
    @inject_conn
    def delete(cls, record: DeclarativeBase, *, conn: DBConnection, commit: bool = True, flush: bool = True):
        conn.session.delete(record)

        if commit:
            conn.session.commit()
        if flush:
            conn.session.flush()
