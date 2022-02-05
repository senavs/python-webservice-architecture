from sqlalchemy import Column, Integer, String

from .. import DeclarativeBase


class UserModel(DeclarativeBase):
    __tablename__ = "USER"

    id_user = Column("ID_USER", Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    username = Column("USERNAME", String(32), nullable=False, unique=True, index=True)
    email = Column("EMAIL", String(256), nullable=False, unique=True, index=True)
