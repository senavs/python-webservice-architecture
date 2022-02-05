from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.settings import database_settings

engine = create_engine(database_settings.uri)
DeclarativeBase = declarative_base()

from .models import *  # noqa F401
