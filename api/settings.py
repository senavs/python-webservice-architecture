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


deploy_settings = DeploySettings()
