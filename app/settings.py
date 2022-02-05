import os.path
from enum import Enum

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)


class AccessLogEnum(Enum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"


class DeploySettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = False
    RELOAD: bool = False
    ACCESS_LOG: AccessLogEnum = AccessLogEnum.info


class DatabaseSession(BaseSettings):
    POSTGRES_HOST: str = "0.0.0.0"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "root"
    POSTGRES_DB: str = "EXAMPLE"

    @property
    def uri(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


deploy_settings = DeploySettings()
database_settings = DatabaseSession()
