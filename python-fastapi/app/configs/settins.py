from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # Database configuration
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str
    db_dsn: str
    db_overflow_size: int = 10
    db_max_pool_size: int = 5


@lru_cache
def get_db_settings(env: Optional[str] = None) -> DBSettings:
    if env is None:
        return DBSettings()

    return DBSettings(_env_file=f".env.{env}")
